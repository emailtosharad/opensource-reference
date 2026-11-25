---
name: wan-comfyui-animation
description: >-
  End-to-end ComfyUI execution runbook and CLI automation for animating 2D literary storybook gouache and anime graphics using Wan 2.1 / AniWan I2V (`aniWan2114BFp8E4m3fn_i2v480pNew.safetensors`) and LightX2V 6-step distillation over local or remote (Colab/Kaggle Cloudflare tunnel) ComfyUI servers. Use when animating still story graphics into 16 fps MP4 clips with Wan 2.1/AniWan, diagnosing Wan latent/noise/CFG artifacts, or chaining scene transitions.
---

# Wan 2.1 / AniWan ComfyUI Animation Skill

Production-verified pipeline for turning static 2D Indian literary storybook gouache / anime illustrations into clean, artifact-free 16 fps MP4 animations via ComfyUI API (Colab, Kaggle, or local).

---

## 1. Non-Negotiable Technical Invariants

Violating any of these produces corrupted output or crashes:

1. **Use `aniWan2114BFp8E4m3fn_i2v480pNew.safetensors` for 2D Art**: Never use base live-action `wan2.1_i2v_480p_14B_fp8_e4m3fn.safetensors` on painted illustrations.
2. **Official Comfy-Org Text Encoder Only**: Always use `umt5_xxl_fp8_e4m3fn_scaled.safetensors` with `CLIPLoader(type="wan")`. Never use Kijai's `umt5-xxl-enc-fp8_e4m3fn.safetensors` (causes `NotImplementedError: Cannot copy out of meta tensor; no data!`).
3. **Use `WanImageToVideo`, NEVER `WanCameraImageToVideo`**: `WanCameraImageToVideo` + `WanCameraEmbedding` is strictly for `Wan2.1-Fun-Control-Camera` models. Wiring it into `aniWan` or standard `wan2.1_i2v` injects mismatched camera tensor channels that corrupt the latent space into a halftone / crosshatch dot-matrix grid.
4. **Always Include `ModelSamplingSD3`**: Wan 2.1 is a flow-matching DiT model. Always route the UNET/LoRA output through `ModelSamplingSD3` (`shift=5.0` for LightX2V Turbo, `shift=8.0` for standard 20-step Precision). Omitting it leaves un-denoised dot-matrix noise.
5. **CFG Burn Guard**: Never run `cfg >= 5.0` without `CFGZeroStar` (Precision mode). In Turbo mode with LightX2V, always set `cfg=1.0`.
6. **Tunnel Inspection Rule**: Never fetch the full `/object_info` over Cloudflare tunnels (multi-MB payload often times out). Always query `/object_info/<NodeName>` per node.

---

## 2. Remote Colab / Kaggle Setup Commands

If a fresh Colab/Kaggle instance is missing the verified weights, run these cells:

```bash
# 1. Anime/2D Fine-Tuned I2V Model (15.27 GB)
!wget -c -P /content/ComfyUI/models/diffusion_models/ \
  https://huggingface.co/852wa/ani_wan2.1/resolve/main/aniWan2114BFp8E4m3fn_i2v480pNew.safetensors

# 2. Official Comfy-Org Text Encoder (remove Kijai wrapper file if present)
!rm -f /content/ComfyUI/models/clip/umt5-xxl-enc-fp8_e4m3fn.safetensors
!wget -c -P /content/ComfyUI/models/clip/ \
  https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors

# 3. LightX2V 480p I2V Step+CFG Distillation LoRA (704 MB — 5.1x speedup)
!wget -c -P /content/ComfyUI/models/loras/ \
  https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
```

*(Replace `/content/ComfyUI` with `/kaggle/working/ComfyUI` when running on Kaggle.)*

---

## 3. Verified Pipeline Modes

| Mode | Chain & Sampler Settings | T4 Speed | L4 (24 GB) Est. |
|---|---|---|---|
| **`turbo` (Default)** | `UNETLoader` $\to$ `LoraLoaderModelOnly(lightx2v_...rank64_bf16, 1.0)` $\to$ `ModelSamplingSD3(shift=5.0)` $\to$ `KSampler(steps=6, cfg=1.0, euler, simple)` | **~7m 48s** | **~45–90s** |
| **`precision`** | `UNETLoader` $\to$ `ModelSamplingSD3(shift=8.0)` $\to$ `WanVideoTeaCacheKJ(0.3, 0.2, 1.0, offload_device, i2v_480)` $\to$ `CFGZeroStar` $\to$ `KSampler(steps=20, cfg=6.0, uni_pc, simple)` | ~40 min | ~3–4 min |

---

## 4. Execution via Helper Script

Use [wan_animate.py](./scripts/wan_animate.py) to run preflight checks, resize any source graphic to `832×480` (LANCZOS), upload it, queue the workflow, download the resulting `.mp4`, and extract 3 QC frames + preview `.gif`:

```bash
# 1. Preflight check on remote ComfyUI server
python3 ~/.gemini/config/skills/wan-comfyui-animation/scripts/wan_animate.py \
  --url https://<tunnel>.trycloudflare.com --check

# 2. Animate a story still (Turbo 6-step mode)
python3 ~/.gemini/config/skills/wan-comfyui-animation/scripts/wan_animate.py \
  --url https://<tunnel>.trycloudflare.com \
  --image "/path/to/Shot.png" \
  --prompt "2D Indian literary storybook gouache animation, characters gently speaking and gesturing warmly, soft breeze in flowering branches" \
  --out-dir "/path/to/output_dir"
```

---

## 5. Scene-Changing Options

When the user asks to change the scene via prompt:
1. **Prompt-Driven Transition (`WanImageToVideo`)**: Keep Frame 1 anchored on the input image and prompt a camera pan, walk-out, or lighting shift (e.g., characters walking out through a stone arch).
2. **Scene A $\to$ Scene B Morph (`WanFirstLastFrameToVideo`)**: Supply both `start_image` and `end_image` to transition between two locked stills.
3. **Chained Extended Shots (15–20s)**: Extract the last frame of Clip 1 and feed it as `--image` for Clip 2 with a new scene prompt.
4. **Pure Text-to-Video (`EmptyHunyuanLatentVideo`)**: Requires `aniWan2114BFp8E4m3fn_t2v.safetensors` (13.3 GB); suitable for generic B-roll, not locked recurring characters.

---

## 6. Mandatory Post-Render QC

Always inspect the 3 extracted sample frames (`*_frame_01.png`, `*_frame_02.png`, `*_frame_03.png`) using `read_file` before reporting success:
* Verify zero dot-matrix / crosshatch artifacts and zero neon solarization.
* Confirm character faces, outfits, and 1960s gouache palette remain faithful to the source graphic.
