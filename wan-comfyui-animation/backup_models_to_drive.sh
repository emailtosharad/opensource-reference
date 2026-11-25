#!/usr/bin/env bash
set -euo pipefail

# Offline archive script: downloads all 5 verified .safetensors (~23.4 GB)
# into a target backup folder (e.g., an external drive under /Volumes/).

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <target_backup_dir>"
  echo "Example: $0 \"/Volumes/MyExternalSSD/Wan21_AniWan_Backup\""
  exit 1
fi

TARGET_DIR="$1/models"
mkdir -p \
  "${TARGET_DIR}/diffusion_models" \
  "${TARGET_DIR}/clip" \
  "${TARGET_DIR}/vae" \
  "${TARGET_DIR}/clip_vision" \
  "${TARGET_DIR}/loras"

download_file() {
  local dest_dir="$1"
  local url="$2"
  local fname
  fname="$(basename "$url")"
  echo ">>> Downloading ${fname} -> ${dest_dir}/"
  curl -L -C - --fail --progress-bar -o "${dest_dir}/${fname}" "$url"
}

download_file "${TARGET_DIR}/diffusion_models" \
  "https://huggingface.co/852wa/ani_wan2.1/resolve/main/aniWan2114BFp8E4m3fn_i2v480pNew.safetensors"

download_file "${TARGET_DIR}/clip" \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors"

download_file "${TARGET_DIR}/vae" \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors"

download_file "${TARGET_DIR}/clip_vision" \
  "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors"

download_file "${TARGET_DIR}/loras" \
  "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors"

echo ">>> Offline model backup complete at: ${TARGET_DIR}"
ls -lh "${TARGET_DIR}"/*/*
