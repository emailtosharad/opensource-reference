# Wan 2.1 / AniWan + LightX2V — Agent Restore & Reconfiguration Guide

Use this file to restore your complete **Wan 2.1 AniWan 2D Animation** environment on a new Mac, fresh Colab/Kaggle notebook, or local ComfyUI installation.

---

## 1. One-Line Instruction to Give an AI Agent

If you ever need an agent to reconfigure everything from scratch, simply paste this instruction:

> **"Read `RESTORE_INSTRUCTIONS.md` in `/Volumes/Seagate2/AI Open Source BackUP/Wan21_AniWan_Backup/` (or from `https://github.com/emailtosharad/opensource-reference/tree/main/wan-comfyui-animation`) and restore my `wan-comfyui-animation` skill, scripts, and ComfyUI configuration."**

---

## 2. What Is Backed Up Here

| Item | Purpose | Location |
| :--- | :--- | :--- |
| **`SKILL.md` & `wan_animate.py`** | Antigravity skill runbook + Python CLI runner | `Wan21_AniWan_Backup/` & GitHub |
| **`MODELS_MANIFEST.md`** | Exact Hugging Face URLs, sizes, and folder mapping | `Wan21_AniWan_Backup/` & GitHub |
| **`colab_setup.sh`** | 1-command model installer for Colab / Kaggle | `Wan21_AniWan_Backup/` & GitHub |
| **`backup_models_to_drive.sh`** | Offline `.safetensors` downloader | `Wan21_AniWan_Backup/` & GitHub |
| **`models/` (`~23.4 GB`)** | Offline archive of all 5 verified `.safetensors` weights | `Seagate2/.../Wan21_AniWan_Backup/models/` |
| **Colab Notebook (`.ipynb`)** | Your Colab launch + Cloudflare tunnel notebook *(save here)* | `Seagate2/.../Wan21_AniWan_Backup/` |

---

## 3. Step-by-Step Restoration Checklist (For Agent or Manual Use)

### A. Restore Antigravity Skill & CLI on Mac
```bash
mkdir -p ~/.gemini/config/skills/wan-comfyui-animation/scripts
cp SKILL.md ~/.gemini/config/skills/wan-comfyui-animation/SKILL.md
cp wan_animate.py ~/.gemini/config/skills/wan-comfyui-animation/scripts/wan_animate.py
chmod +x ~/.gemini/config/skills/wan-comfyui-animation/scripts/wan_animate.py
```

### B. Restore Models to Colab / Kaggle Cloud Session
1. Upload/open your saved `.ipynb` Colab notebook (on **Tesla T4** free or **NVIDIA L4 24GB** Colab Pro for ~60s/clip).
2. Ensure ComfyUI has **`ComfyUI-VideoHelperSuite`** (`VHS_VideoCombine`) and **`ComfyUI-KJNodes`** (`WanVideoTeaCacheKJ`) installed.
3. Run `colab_setup.sh` inside a notebook cell:
   ```bash
   !bash colab_setup.sh /content/ComfyUI   # use /kaggle/working/ComfyUI on Kaggle
   ```
4. Start ComfyUI with Cloudflare tunnel (`cloudflared tunnel --url http://127.0.0.1:8188`).

### C. Restore Models to Local Mac / Local ComfyUI (Optional, Needs ~24 GB VRAM/Unified RAM)
Copy the `models/` folder from `Seagate2` directly into your local `ComfyUI/models/`:
```bash
rsync -avh --progress \
  "/Volumes/Seagate2/AI Open Source BackUP/Wan21_AniWan_Backup/models/" \
  "/Users/sharadkumar/ComfyUI-Installs/ComfyUI (2)/ComfyUI/models/"
```

### D. Verify & Run First Test Clip
```bash
python3 ~/.gemini/config/skills/wan-comfyui-animation/scripts/wan_animate.py \
  --url https://<your-tunnel>.trycloudflare.com --check
```

---

## 4. Non-Negotiable Technical Guardrails (Do Not Change)

1. **2D / Gouache Model**: `aniWan2114BFp8E4m3fn_i2v480pNew.safetensors` (`models/diffusion_models/`)
2. **Text Encoder**: `umt5_xxl_fp8_e4m3fn_scaled.safetensors` (`models/clip/`) — *never* use Kijai's `umt5-xxl-enc-fp8_e4m3fn.safetensors`.
3. **Conditioning Node**: `WanImageToVideo` — *never* use `WanCameraImageToVideo` (causes halftone dot-grid corruption).
4. **Turbo Pipeline (Default)**: `LoraLoaderModelOnly` (`lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors`, `strength: 1.0`) $\to$ `ModelSamplingSD3(shift: 5.0)` $\to$ `KSampler(steps: 6, cfg: 1.0, euler, simple)`.
5. **Precision Pipeline (No LoRA)**: `ModelSamplingSD3(shift: 8.0)` $\to$ `WanVideoTeaCacheKJ` $\to$ `CFGZeroStar` $\to$ `KSampler(steps: 20, cfg: 6.0, uni_pc, simple)`.
