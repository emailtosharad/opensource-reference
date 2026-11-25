# Wan 2.1 / AniWan ComfyUI Production Backup Manifest

Verified configuration for animating 2D Indian literary storybook gouache graphics (`832x480`, 16 fps) using **AniWan 2.1 14B I2V** + **LightX2V 6-step Turbo LoRA**.

---

## 1. Locked Model Files (`~23.4 GB` Total)

> **Note**: `.safetensors` files exceed GitHub's 100 MB limit and are archived offline on an external drive using `./backup_models_to_drive.sh`.

| Component | Exact Filename | Approx. Size | ComfyUI Folder | Verified Download URL |
| :--- | :--- | :--- | :--- | :--- |
| **Diffusion UNET (2D/Anime I2V)** | `aniWan2114BFp8E4m3fn_i2v480pNew.safetensors` | 15.27 GB | `models/diffusion_models/` | https://huggingface.co/852wa/ani_wan2.1/resolve/main/aniWan2114BFp8E4m3fn_i2v480pNew.safetensors |
| **Text Encoder (Official Comfy-Org)** | `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | ~4.8 GB | `models/clip/` | https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors |
| **VAE** | `wan_2.1_vae.safetensors` | ~1.4 GB | `models/vae/` | https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors |
| **CLIP Vision** | `clip_vision_h.safetensors` | ~1.2 GB | `models/clip_vision/` | https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors |
| **Turbo Distillation LoRA (6-step)** | `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | 704 MB | `models/loras/` | https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors |

---

## 2. Critical Pipeline Invariants

1. **Conditioning**: Always use `WanImageToVideo` (NEVER `WanCameraImageToVideo`, which corrupts standard I2V latents into halftone dot-grids).
2. **Text Encoder**: Always use `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (NEVER Kijai's `umt5-xxl-enc-fp8_e4m3fn.safetensors`, which triggers `NotImplementedError: Cannot copy out of meta tensor`).
3. **Timestep Shift**: Always route through `ModelSamplingSD3` (`shift: 5.0` for LightX2V Turbo; `shift: 8.0` for 20-step Precision).
4. **Turbo Sampler**: `steps: 6`, `cfg: 1.0`, `sampler_name: euler`, `scheduler: simple` (~7m 48s on T4, ~45–90s on L4 24GB).

---

## 3. Restore / Backup Commands

* **Backup all `.safetensors` to an external drive**:
  ```bash
  ./backup_models_to_drive.sh "/Volumes/<YourDriveName>/Wan21_AniWan_Backup"
  ```
* **Restore weights on Colab / Kaggle**:
  ```bash
  bash colab_setup.sh /content/ComfyUI   # or /kaggle/working/ComfyUI
  ```
* **Run animation CLI**:
  ```bash
  python3 wan_animate.py --url https://<tunnel>.trycloudflare.com --image Shot.png --prompt "..." --out-dir ./out
  ```
