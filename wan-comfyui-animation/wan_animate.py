#!/usr/bin/env python3
"""
CLI runner for Wan 2.1 / AniWan I2V animation on local or remote ComfyUI servers.

Resizes the source graphic to 832x480 (LANCZOS), uploads via /upload/image,
submits either the 6-step LightX2V Turbo pipeline (default) or 20-step
CFGZeroStar + TeaCache Precision pipeline, polls /history, downloads the MP4,
and extracts 3 sample frames + a preview GIF for visual QC.
"""

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from PIL import Image

DEFAULT_UNET = "aniWan2114BFp8E4m3fn_i2v480pNew.safetensors"
DEFAULT_CLIP = "umt5_xxl_fp8_e4m3fn_scaled.safetensors"
DEFAULT_VAE = "wan_2.1_vae.safetensors"
DEFAULT_CLIP_VISION = "clip_vision_h.safetensors"
DEFAULT_LORA = "lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors"
DEFAULT_NEGATIVE = (
    "blurry, distorted, deformed faces, extra limbs, green tint, yellow tint, "
    "dot matrix, crosshatch, noisy, low quality, fast chaotic motion, morphing"
)


def query_node_info(base_url: str, node_name: str) -> dict:
    """Fetch schema for a single ComfyUI node to avoid full /object_info timeouts."""
    req = urllib.request.urlopen(f"{base_url}/object_info/{node_name}", timeout=15)
    return json.loads(req.read().decode("utf-8"))


def run_preflight(base_url: str, mode: str) -> bool:
    """Verify required models, text encoder, VAE, and nodes exist on the server."""
    base_url = base_url.rstrip("/")
    ok = True

    stats = json.loads(urllib.request.urlopen(f"{base_url}/system_stats", timeout=10).read().decode("utf-8"))
    for dev in stats.get("devices", []):
        vram_gb = dev.get("vram_total", 0) / (1024**3)
        print(f"GPU: {dev.get('name')} ({vram_gb:.1f} GB VRAM)")

    checks = [
        ("UNETLoader", "unet_name", DEFAULT_UNET),
        ("CLIPLoader", "clip_name", DEFAULT_CLIP),
        ("VAELoader", "vae_name", DEFAULT_VAE),
        ("CLIPVisionLoader", "clip_name", DEFAULT_CLIP_VISION),
    ]
    if mode == "turbo":
        checks.append(("LoraLoaderModelOnly", "lora_name", DEFAULT_LORA))

    for node, field, expected in checks:
        info = query_node_info(base_url, node)
        choices = info.get(node, {}).get("input", {}).get("required", {}).get(field, [[]])[0]
        present = expected in choices
        print(f"[{'OK' if present else 'MISSING'}] {node}.{field}: {expected}")
        if not present:
            print(f"   Available: {choices}")
            ok = False

    required_nodes = ["WanImageToVideo", "ModelSamplingSD3", "VHS_VideoCombine"]
    if mode == "precision":
        required_nodes.extend(["CFGZeroStar", "WanVideoTeaCacheKJ"])
    for node in required_nodes:
        info = query_node_info(base_url, node)
        present = node in info
        print(f"[{'OK' if present else 'MISSING'}] Node: {node}")
        if not present:
            ok = False

    return ok


def upload_resized_image(base_url: str, src_path: str, work_dir: str) -> str:
    """Resize source image to 832x480 LANCZOS and upload to ComfyUI /upload/image."""
    stem = os.path.splitext(os.path.basename(src_path))[0]
    resized_path = os.path.join(work_dir, f"{stem}_832x480.png")
    im = Image.open(src_path).convert("RGB").resize((832, 480), Image.Resampling.LANCZOS)
    im.save(resized_path)

    boundary = uuid.uuid4().hex
    with open(resized_path, "rb") as f:
        img_bytes = f.read()

    fname = os.path.basename(resized_path)
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="image"; filename="{fname}"\r\n'
        f"Content-Type: image/png\r\n\r\n"
    ).encode("utf-8") + img_bytes + f"\r\n--{boundary}--\r\n".encode("utf-8")

    req = urllib.request.Request(
        f"{base_url}/upload/image",
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
    )
    res = json.loads(urllib.request.urlopen(req, timeout=30).read().decode("utf-8"))
    return res["name"]


def build_prompt(
    img_name: str,
    positive: str,
    negative: str,
    mode: str,
    frames: int,
    seed: int,
    prefix: str,
) -> dict:
    """Build the verified WanImageToVideo API prompt graph."""
    prompt = {
        "1": {
            "class_type": "UNETLoader",
            "inputs": {"unet_name": DEFAULT_UNET, "weight_dtype": "default"},
        },
        "2": {
            "class_type": "CLIPLoader",
            "inputs": {"clip_name": DEFAULT_CLIP, "type": "wan"},
        },
        "3": {
            "class_type": "VAELoader",
            "inputs": {"vae_name": DEFAULT_VAE},
        },
        "4": {
            "class_type": "CLIPVisionLoader",
            "inputs": {"clip_name": DEFAULT_CLIP_VISION},
        },
        "5": {
            "class_type": "LoadImage",
            "inputs": {"image": img_name},
        },
        "6": {
            "class_type": "CLIPVisionEncode",
            "inputs": {"clip_vision": ["4", 0], "image": ["5", 0], "crop": "none"},
        },
        "7": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": positive, "clip": ["2", 0]},
        },
        "8": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": negative, "clip": ["2", 0]},
        },
        "10": {
            "class_type": "WanImageToVideo",
            "inputs": {
                "positive": ["7", 0],
                "negative": ["8", 0],
                "vae": ["3", 0],
                "clip_vision_output": ["6", 0],
                "start_image": ["5", 0],
                "width": 832,
                "height": 480,
                "length": frames,
                "batch_size": 1,
            },
        },
        "12": {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["11", 0], "vae": ["3", 0]},
        },
        "13": {
            "class_type": "VHS_VideoCombine",
            "inputs": {
                "images": ["12", 0],
                "frame_rate": 16.0,
                "loop_count": 0,
                "filename_prefix": prefix,
                "format": "video/h264-mp4",
                "pix_fmt": "yuv420p",
                "crf": 19,
                "save_metadata": True,
                "trim_to_audio": False,
                "pingpong": False,
                "save_output": True,
            },
        },
    }

    if mode == "turbo":
        prompt["14"] = {
            "class_type": "LoraLoaderModelOnly",
            "inputs": {
                "model": ["1", 0],
                "lora_name": DEFAULT_LORA,
                "strength_model": 1.0,
            },
        }
        prompt["15"] = {
            "class_type": "ModelSamplingSD3",
            "inputs": {"model": ["14", 0], "shift": 5.0},
        }
        prompt["11"] = {
            "class_type": "KSampler",
            "inputs": {
                "model": ["15", 0],
                "seed": seed,
                "steps": 6,
                "cfg": 1.0,
                "sampler_name": "euler",
                "scheduler": "simple",
                "positive": ["10", 0],
                "negative": ["10", 1],
                "latent_image": ["10", 2],
                "denoise": 1.0,
            },
        }
    else:
        prompt["15"] = {
            "class_type": "ModelSamplingSD3",
            "inputs": {"model": ["1", 0], "shift": 8.0},
        }
        prompt["17"] = {
            "class_type": "WanVideoTeaCacheKJ",
            "inputs": {
                "model": ["15", 0],
                "rel_l1_thresh": 0.3,
                "start_percent": 0.2,
                "end_percent": 1.0,
                "cache_device": "offload_device",
                "coefficients": "i2v_480",
            },
        }
        prompt["16"] = {
            "class_type": "CFGZeroStar",
            "inputs": {"model": ["17", 0]},
        }
        prompt["11"] = {
            "class_type": "KSampler",
            "inputs": {
                "model": ["16", 0],
                "seed": seed,
                "steps": 20,
                "cfg": 6.0,
                "sampler_name": "uni_pc",
                "scheduler": "simple",
                "positive": ["10", 0],
                "negative": ["10", 1],
                "latent_image": ["10", 2],
                "denoise": 1.0,
            },
        }

    return prompt


def main() -> int:
    parser = argparse.ArgumentParser(description="Animate a 2D story image using AniWan 2.1 on ComfyUI.")
    parser.add_argument("--url", required=True, help="ComfyUI base URL (e.g. https://xxx.trycloudflare.com)")
    parser.add_argument("--check", action="store_true", help="Run preflight check only and exit")
    parser.add_argument("--image", help="Path to source image (PNG/JPG)")
    parser.add_argument("--prompt", help="Positive animation prompt")
    parser.add_argument("--negative", default=DEFAULT_NEGATIVE, help="Negative prompt")
    parser.add_argument("--mode", choices=["turbo", "precision"], default="turbo", help="Sampling pipeline mode")
    parser.add_argument("--frames", type=int, default=49, help="Frame count (49 = ~3s @ 16fps)")
    parser.add_argument("--seed", type=int, default=778899, help="Random seed")
    parser.add_argument("--prefix", default="AniWan_Output", help="Output filename prefix")
    parser.add_argument("--out-dir", default=".", help="Directory to save downloaded MP4, frames, and GIF")
    args = parser.parse_args()

    base_url = args.url.rstrip("/")

    if args.check:
        return 0 if run_preflight(base_url, args.mode) else 1

    if not args.image or not args.prompt:
        parser.error("--image and --prompt are required unless --check is set")

    os.makedirs(args.out_dir, exist_ok=True)
    if not run_preflight(base_url, args.mode):
        print("Preflight check failed. Fix missing models/nodes before rendering.", file=sys.stderr)
        return 1

    img_name = upload_resized_image(base_url, args.image, args.out_dir)
    print(f"Uploaded resized 832x480 image as: {img_name}")

    prompt = build_prompt(img_name, args.prompt, args.negative, args.mode, args.frames, args.seed, args.prefix)
    data = json.dumps({"prompt": prompt}).encode("utf-8")
    req = urllib.request.Request(f"{base_url}/prompt", data=data, headers={"Content-Type": "application/json"})
    res = json.loads(urllib.request.urlopen(req, timeout=20).read().decode("utf-8"))
    pid = res["prompt_id"]
    print(f"Queued prompt_id={pid} (mode={args.mode}, frames={args.frames})")

    start = time.time()
    while True:
        time.sleep(15)
        try:
            hist = json.loads(urllib.request.urlopen(f"{base_url}/history/{pid}", timeout=15).read().decode("utf-8"))
            if pid not in hist:
                continue
            status = hist[pid].get("status", {})
            elapsed = int(time.time() - start)
            print(f"Finished in {elapsed}s! Status: {status.get('status_str')}")
            if status.get("status_str") == "error":
                print(json.dumps(status.get("messages", []), indent=2), file=sys.stderr)
                return 1
            for _, nout in hist[pid].get("outputs", {}).items():
                for key in ("gifs", "videos", "images"):
                    for item in nout.get(key, []):
                        fname = item["filename"]
                        sub = item.get("subfolder", "")
                        ftype = item.get("type", "output")
                        dl_url = (
                            f"{base_url}/view?filename={urllib.parse.quote(fname)}"
                            f"&subfolder={urllib.parse.quote(sub)}&type={ftype}"
                        )
                        local_mp4 = os.path.join(args.out_dir, fname)
                        urllib.request.urlretrieve(dl_url, local_mp4)
                        print(f"Downloaded: {local_mp4} ({os.path.getsize(local_mp4)} bytes)")
                        if fname.endswith(".mp4"):
                            stem = os.path.splitext(fname)[0]
                            for idx, ts in enumerate(("0.2", "1.5", "2.8"), 1):
                                f_out = os.path.join(args.out_dir, f"{stem}_frame_{idx:02d}.png")
                                subprocess.run(
                                    ["ffmpeg", "-y", "-ss", ts, "-i", local_mp4, "-frames:v", "1", f_out],
                                    capture_output=True,
                                )
                                print(f"Extracted frame: {f_out}")
                            gif_out = os.path.join(args.out_dir, f"{stem}.gif")
                            subprocess.run(
                                [
                                    "ffmpeg", "-y", "-i", local_mp4,
                                    "-vf", "fps=12,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
                                    gif_out,
                                ],
                                capture_output=True,
                            )
                            print(f"Preview GIF: {gif_out}")
            return 0
        except Exception as exc:
            print(f"Poll warning ({int(time.time() - start)}s): {exc}")


if __name__ == "__main__":
    sys.exit(main())
