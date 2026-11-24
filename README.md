# Open-Source Reference & System Recovery Registry

> **Hardware Baseline**: macOS Apple Silicon (M1/M2/M3/M4 Series)  
> **Maintainer**: Sharad Kumar ([@emailtosharad](https://github.com/emailtosharad))  
> **Primary Live Workspace**: `~/opensource`  
> **Registry Version**: 2.0 (November 2026)

---

## Overview

This repository serves as the **canonical backup, documentation registry, and automated disaster recovery suite** for the entire local AI audio, video production, motion graphics, and Model Context Protocol (MCP) agent infrastructure running on Apple Silicon.

In the event of hardware failure, machine migration, or OS reinstallation, this project allows you to completely rebuild and verify all **36 open-source tools, DAWs, neural synthesis models, and MCP servers** in under 15 minutes.

---

## Repository Contents

| File | Description |
|---|---|
| **[`TOOLS.md`](./TOOLS.md)** | **Master Tools Registry**: In-depth profiles of all 36 tools, exact installed versions, internal operating mechanics, key capabilities, operational CLI commands, and directory layouts. |
| **[`RESTORE.md`](./RESTORE.md)** | **Disaster Recovery Runbook**: Step-by-step restoration instructions covering Homebrew packages, Apple Silicon Metal GPU optimizations, Python 3.12 virtual environments, TypeScript builds, and verification smoke tests. |
| **[`restore.sh`](./restore.sh)** | **Automated Recovery Script**: One-command bash script that installs prerequisites, clones all 22 upstream repositories, configures virtual environments, compiles binaries, and restores the MCP configuration. |
| **[`mcp_config.example.json`](./mcp_config.example.json)** | **MCP Server Configuration**: Reference template containing connection parameters for all 11 local MCP servers (`kdenlive`, `audacity`, `drawthings`, `flow`, `splicekit`, `youtube_uploader`, `autoflowcut`, `capcut_direct`, `capcut_smartcut`, `capcut_kit`, `comfyui`). |
| **[`RESOURCES.md`](./RESOURCES.md)** | Curated list of web-based generative audio, music, and media tools. |

---

## 🚀 Quick Disaster Recovery (Fresh Mac)

To restore the complete environment on a fresh macOS installation:

```bash
# 1. Clone this reference repository
git clone https://github.com/emailtosharad/opensource-reference.git ~/Developer/opensource-reference
cd ~/Developer/opensource-reference

# 2. Make the bootstrap script executable and run it
chmod +x restore.sh
./restore.sh
```

---

## 🛠️ Tool Inventory Overview

The 36 tools cataloged in [`TOOLS.md`](./TOOLS.md) span 4 primary production domains:

1. **Video Production & NLE Engines**:
   - `AutoFlowCut` (AI image/video batch generation & NLE exporter)
   - `capcut-mcp` (Direct CapCut draft JSON manipulator)
   - `capcut-ai-editor` (SmartCut talking-head silence & duplicate take cutter)
   - `capcut-mcp-kit` (65 camera moves, keyframing & MLX music ducking)
   - `Kdenlive & MLT Melt` (Broadcast video editing & XML timeline assembly)
   - `SpliceKit` (Final Cut Pro AppleScript & runtime automation)
   - `Guney Motion Kit` (HTML-to-video motion graphics via HyperFrames)
   - `OpenShorts` (AI vertical short-form video studio)

2. **Audio DAWs & Neural Voice Synthesis**:
   - `Audacity MCP` (Multi-track acoustic editing & macro automation)
   - `Voicebox` (Neural voice studio & pedalboard DSP)
   - `F5-TTS & IndicF5` (Flow-matching diffusion zero-shot voice cloning)
   - `MOSS-TTS & MOSS-SoundEffect v2.0` (48kHz stereo Foley & soundscapes)
   - `Maya 2 Native TTS` (Apple Silicon MLX sub-second voice synthesis)
   - `Demucs` (Deep learning music source separation & vocal isolation)
   - `BlackHole` (Zero-latency virtual loopback audio driver)

3. **Visual Media & Super-Resolution**:
   - `Draw Things MCP` (Local Apple Silicon Metal GPU SDXL diffusion)
   - `ComfyUI MCP` (Official Comfy-Org workflow & template automation engine)
   - `Upscayl` (Real-ESRGAN NCNN 4x super-resolution)
   - `Flow MCP` (Google Flow cinematic AI video generation)
   - `LivePortrait` (Neural landmark deformation, 2D facial animation, gaze steering & dialogue articulation)
   - `ImageMagick & MediaInfo` (Image transformation and stream inspection)

4. **Agent Tooling & Cloud Automation**:
   - `Antigravity CLI (agy)` (Native terminal agent interface)
   - `YouTube Uploader MCP` (Automated publishing & OAuth metadata management)
   - `GitHub CLI (gh)` & `uv` (Fast Python package manager)

---

## 🔄 Maintenance Protocol

Whenever any open-source tool is installed, updated, or reconfigured:
1. Update `TOOLS.md` with the new tool version, operational mechanism, and CLI commands.
2. If the tool provides an MCP server, ensure it is added to `mcp_config.example.json`.
3. Commit and push the changes:
   ```bash
   cd ~/Developer/opensource-reference
   cp ~/opensource/TOOLS.md .
   git add -A && git commit -m "docs: update tools registry and recovery guide" && git push
   ```
