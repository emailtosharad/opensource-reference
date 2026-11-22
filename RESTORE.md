# macOS Apple Silicon Disaster Recovery & Open-Source Tools Restore Runbook

> **Purpose**: Complete end-to-end disaster recovery guide to rebuild the entire AI audio, video production, motion graphics, and MCP agent infrastructure on a fresh macOS installation or replacement Apple Silicon Mac.

---

## 1. System Prerequisites & Architecture Baseline

- **Hardware**: Apple Silicon (M1/M2/M3/M4 Series, Pro/Max/Ultra recommended for local DiT & diffusion).
- **OS**: macOS Sonoma (14.x) or macOS Sequoia (15.x+).
- **Core Shell**: `zsh` with `/opt/homebrew/bin` prioritized in `$PATH`.
- **Primary Workspace Directories**:
  - `~/opensource` (all cloned repos, DAWs, and MCP servers)
  - `~/Developer/opensource-reference` (this documentation & backup repository)
  - `~/.gemini/config` (MCP configurations, skills, and agent rules)
  - `~/Movies/CapCut/User Data/Projects/com.lveditor.draft` (CapCut Desktop drafts)

---

## 2. Phase 1: Base Toolchain & System Packages

Open a Terminal and execute the following in order:

### 1.1 Xcode Command Line Tools
```bash
xcode-select --install
```

### 1.2 Homebrew Package Manager
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH (Apple Silicon)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 1.3 Core Media Utilities, Compilers & Runtimes
```bash
# Core CLI tools & media libraries
brew install \
  git gh node ffmpeg imagemagick sox media-info go uv python@3.14

# Audio loopback and desktop applications
brew install --cask \
  blackhole-2ch audacity kdenlive
```

### 1.4 Standalone Creative Applications
Install the following from the Mac App Store or vendor websites:
- **CapCut Desktop**: Install from Mac App Store (required for `capcut-mcp`, `capcut-ai-editor`, and `capcut-mcp-kit`). Open once to initialize `~/Movies/CapCut`.
- **Draw Things**: Install from Mac App Store (enables local Metal GPU text-to-image on port 7860).
- **Upscayl**: Download DMG from [upscayl.org](https://www.upscayl.org/) or install via GitHub release.
- **LM Studio / Bionic**: Download from [lmstudio.ai](https://lmstudio.ai/) (local LLM server on `127.0.0.1:1234`).
- **Antigravity CLI (`agy`)**: Install via official Google Antigravity installer.

---

## 3. Phase 2: Clone All Open-Source Repositories

Create the primary tools folder and clone all 22 active open-source components:

```bash
mkdir -p ~/opensource
cd ~/opensource

# 1. Video Editors & NLE Integrations
git clone https://github.com/emailtosharad/AutoFlowCut.git AutoFlowCut
git clone https://github.com/Va1bhav512/kdenlive-mcp-server.git kdenlive-mcp-server
git clone https://github.com/elliotttate/SpliceKit.git SpliceKit
git clone https://github.com/JmsLdrn/capcut-mcp.git capcut-mcp
git clone https://github.com/mrbuslov/capcut-ai-editor.git capcut-ai-editor
git clone https://github.com/simopa/capcut-mcp-kit.git capcut-mcp-kit
git clone https://github.com/GTAI-1/guney-motion-kit.git guney-motion-kit
git clone https://github.com/mutonby/openshorts.git openshorts

# 2. Audio DAWs, Speech & Acoustic Pipelines
git clone https://github.com/xDarkzx/Audacity-MCP.git Audacity-MCP
git clone https://github.com/jamiepine/voicebox.git voicebox
git clone https://github.com/rumourscape/F5-TTS.git F5-TTS
git clone https://github.com/AI4Bharat/IndicF5.git IndicF5
git clone https://github.com/OpenMOSS/MOSS-TTS.git MOSS-TTS
git clone https://github.com/emailtosharad/OmniVoice.git OmniVoice
git clone https://github.com/emailtosharad/AI-Studio-App.git AI-Studio-App
git clone https://github.com/existentialaudio/blackhole.git BlackHole

# 3. Visual Diffusion, Google Flow & Cloud Publishing
git clone https://github.com/james-see/mcp-drawthings.git mcp-drawthings
git clone https://github.com/emailtosharad/flow-mcp.git flow-mcp
git clone https://github.com/upscayl/upscayl.git upscayl
git clone https://github.com/kapilunclekikahaniyan-creator/youtube-uploader-mcp.git youtube-uploader-mcp
git clone https://github.com/abdullahguch/folderium.git folderium
git clone https://github.com/google-antigravity/antigravity-sdk-python.git antigravity-sdk-python
```

---

## 4. Phase 3: Setup Environments & Compile Toolchains

### 4.1 Python Virtual Environments (Apple Silicon Metal & uv)
We use `uv` with Python 3.12 for guaranteed wheel compatibility:

```bash
# 1. Kdenlive MCP Server
cd ~/opensource/kdenlive-mcp-server
uv venv .venv --python 3.12
uv pip install -e . --python .venv/bin/python

# 2. Audacity MCP
cd ~/opensource/Audacity-MCP
uv venv .venv --python 3.12
uv pip install -r requirements.txt --python .venv/bin/python

# 3. CapCut AI Editor (SmartCut)
cd ~/opensource/capcut-ai-editor
uv venv .venv --python 3.12
uv pip install -e . --python .venv/bin/python

# 4. CapCut MCP Kit (VectCutAPI Backend + Apple Silicon MLX GPU)
cd ~/opensource/capcut-mcp-kit/vectcut-api
uv venv venv --python 3.12
uv pip install -r requirements.lock.txt --python venv/bin/python
uv pip install -r requirements-whisper-mlx.lock.txt --python venv/bin/python

# 5. SpliceKit (Final Cut Pro MCP)
mkdir -p ~/.venvs/splicekit-mcp
uv venv ~/.venvs/splicekit-mcp --python 3.12
uv pip install -r ~/opensource/SpliceKit/requirements.txt --python ~/.venvs/splicekit-mcp/bin/python

# 6. Demucs (Neural Vocal/Watermark Isolation)
uv tool install demucs
```

### 4.2 Node.js & TypeScript Toolchains
```bash
# 1. AutoFlowCut Desktop & MCP Server
cd ~/opensource/AutoFlowCut
npm install
npm run build

# 2. Draw Things MCP Server
cd ~/opensource/mcp-drawthings
npm install
npm run build

# 3. Google Flow MCP Server
cd ~/opensource/flow-mcp
npm install
npm run build

# 4. CapCut Direct MCP (Node stdio)
cd ~/opensource/capcut-mcp
npm install

# 5. CapCut Kit MCP Server
cd ~/opensource/capcut-mcp-kit/capcut-mcp-server
npm install
npm run build

# 6. Guney Motion Kit (HyperFrames)
cd ~/opensource/guney-motion-kit
npm install
```

### 4.3 Go Binaries
```bash
# YouTube Uploader MCP
cd ~/opensource/youtube-uploader-mcp
go build -o youtube-uploader-mcp main.go
```

---

## 5. Phase 4: Restore MCP Server Configuration

Restore the active MCP config at `~/.gemini/config/mcp_config.json`:

```bash
mkdir -p ~/.gemini/config

cat << 'EOF' > ~/.gemini/config/mcp_config.json
{
  "mcpServers": {
    "kdenlive": {
      "command": "/Users/sharadkumar/opensource/kdenlive-mcp-server/.venv/bin/kdenlive-mcp",
      "args": []
    },
    "audacity": {
      "command": "/Users/sharadkumar/opensource/Audacity-MCP/.venv/bin/audacity-mcp",
      "args": []
    },
    "drawthings": {
      "command": "/opt/homebrew/bin/node",
      "args": [
        "/Users/sharadkumar/opensource/mcp-drawthings/dist/index.js"
      ],
      "env": {
        "DRAWTHINGS_HOST": "127.0.0.1",
        "DRAWTHINGS_PORT": "7860",
        "DRAWTHINGS_OUTPUT_DIR": "/Users/sharadkumar/Pictures/drawthings-mcp"
      }
    },
    "flow": {
      "command": "/opt/homebrew/bin/node",
      "args": [
        "/Users/sharadkumar/opensource/flow-mcp/dist/index.js"
      ]
    },
    "splicekit": {
      "command": "/Users/sharadkumar/.venvs/splicekit-mcp/bin/python",
      "args": [
        "/Users/sharadkumar/opensource/SpliceKit/mcp/server.py"
      ]
    },
    "youtube_uploader": {
      "command": "/Users/sharadkumar/opensource/youtube-uploader-mcp/youtube-uploader-mcp",
      "args": [
        "-client_secret_file",
        "/Users/sharadkumar/opensource/youtube-uploader-mcp/client_secret.json",
        "-working_dir",
        "/Users/sharadkumar/opensource/youtube-uploader-mcp"
      ]
    },
    "autoflowcut": {
      "command": "/opt/homebrew/bin/node",
      "args": [
        "/Users/sharadkumar/opensource/AutoFlowCut/mcp-server/index.js"
      ]
    },
    "capcut_direct": {
      "command": "/opt/homebrew/bin/node",
      "args": [
        "/Users/sharadkumar/opensource/capcut-mcp/src/server.js"
      ],
      "env": {
        "CAPCUT_DRAFTS_DIR": "/Users/sharadkumar/Movies/CapCut/User Data/Projects/com.lveditor.draft"
      }
    },
    "capcut_smartcut": {
      "command": "/Users/sharadkumar/opensource/capcut-ai-editor/.venv/bin/python",
      "args": [
        "-m",
        "smartcut.server"
      ],
      "env": {
        "CAPCUT_DRAFTS_DIR": "/Users/sharadkumar/Movies/CapCut/User Data/Projects/com.lveditor.draft"
      }
    },
    "capcut_kit": {
      "command": "/opt/homebrew/bin/node",
      "args": [
        "/Users/sharadkumar/opensource/capcut-mcp-kit/capcut-mcp-server/dist/index.js"
      ],
      "env": {
        "CAPCUT_API_URL": "http://localhost:9001"
      }
    }
  }
}
EOF
```

---

## 6. Phase 5: Verification & Smoke Test Protocol

Run these one-line commands to verify every critical layer is fully operational:

```bash
# 1. Verify Audio Stack
ffmpeg -version | head -n 1
sox --version
demucs --help | head -n 2

# 2. Verify CapCut Direct MCP
node -e "import('/Users/sharadkumar/opensource/capcut-mcp/src/core.js').then(({ listDrafts }) => console.log('CapCut Drafts:', listDrafts()));"

# 3. Verify CapCut SmartCut AI
/Users/sharadkumar/opensource/capcut-ai-editor/.venv/bin/python -c "from smartcut.core.capcut_finder import list_projects; print('SmartCut Projects:', len(list_projects()))"

# 4. Verify CapCut Kit Backend
cd /Users/sharadkumar/opensource/capcut-mcp-kit/vectcut-api && ./venv/bin/python -c "import capcut_server, mlx_whisper; print('VectCutAPI + MLX Whisper ready')"

# 5. Verify Draw Things MCP
node /Users/sharadkumar/opensource/mcp-drawthings/dist/index.js --help 2>&1 | head -n 2

# 6. Verify YouTube Uploader MCP
/Users/sharadkumar/opensource/youtube-uploader-mcp/youtube-uploader-mcp -h 2>&1 | head -n 2
```

---

## 7. Automated One-Command Recovery Script

To restore everything completely unattended, run:
```bash
cd ~/Developer/opensource-reference
chmod +x restore.sh
./restore.sh --all
```
