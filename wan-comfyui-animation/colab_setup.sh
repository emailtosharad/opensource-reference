#!/usr/bin/env bash
set -euo pipefail

# One-command setup for Colab (/content/ComfyUI) or Kaggle (/kaggle/working/ComfyUI)
COMFY_DIR="${1:-/content/ComfyUI}"

echo "Installing AniWan 2.1 + LightX2V weights into: ${COMFY_DIR}"
mkdir -p \
  "${COMFY_DIR}/models/diffusion_models" \
  "${COMFY_DIR}/models/clip" \
  "${COMFY_DIR}/models/vae" \
  "${COMFY_DIR}/models/clip_vision" \
  "${COMFY_DIR}/models/loras"

# Remove incompatible Kijai text encoder if present
rm -f "${COMFY_DIR}/models/clip/umt5-xxl-enc-fp8_e4m3fn.safetensors"

wget -c -P "${COMFY_DIR}/models/diffusion_models/" \
  "https://huggingface.co/852wa/ani_wan2.1/resolve/main/aniWan2114BFp8E4m3fn_i2v480pNew.safetensors"

wget -c -P "${COMFY_DIR}/models/clip/" \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors"

wget -c -P "${COMFY_DIR}/models/vae/" \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors"

wget -c -P "${COMFY_DIR}/models/clip_vision/" \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors"

wget -c -P "${COMFY_DIR}/models/loras/" \
  "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors"

echo "All verified Wan 2.1 / AniWan models installed successfully."
