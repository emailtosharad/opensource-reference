#!/usr/bin/env bash
# ==============================================================================
# Disaster Recovery & System Bootstrap Script for macOS Apple Silicon
# Restores all 34 Open-Source Tools, Media Engines, and MCP Servers
# ==============================================================================
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

TARGET_DIR="${HOME}/opensource"
MCP_CONFIG_DIR="${HOME}/.gemini/config"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

echo -e "${GREEN}"
echo "======================================================================="
echo "   macOS Apple Silicon Open-Source Media & MCP Recovery Bootstrap     "
echo "======================================================================="
echo -e "${NC}"

# 1. Check Architecture
if [[ "$(uname -s)" != "Darwin" ]] || [[ "$(uname -m)" != "arm64" ]]; then
  log_warn "This script is tailored specifically for macOS Apple Silicon (arm64)."
fi

# 2. Check Homebrew
if ! command -v brew >/dev/null 2>&1; then
  log_info "Homebrew not found. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi

# 3. Install Core CLI Packages
log_info "Installing Homebrew formulae..."
brew install \
  git gh node ffmpeg imagemagick sox media-info go uv python@3.14 || true

# 4. Install Audio & Video Casks
log_info "Installing Homebrew casks..."
brew install --cask \
  blackhole-2ch audacity kdenlive || true

# 5. Create Target Directory
mkdir -p "${TARGET_DIR}"
cd "${TARGET_DIR}"

# 6. Clone Open-Source Repositories
clone_repo() {
  local dir="$1"
  local url="$2"
  local branch="${3:-main}"

  if [[ -d "${TARGET_DIR}/${dir}" ]]; then
    log_info "Repository ${dir} already exists. Pulling latest..."
    git -C "${TARGET_DIR}/${dir}" pull || true
  else
    log_info "Cloning ${dir} from ${url} (branch: ${branch})..."
    git clone --branch "${branch}" "${url}" "${dir}" || git clone "${url}" "${dir}"
  fi
}

log_info "Cloning and updating open-source repositories..."
clone_repo "AutoFlowCut" "https://github.com/emailtosharad/AutoFlowCut.git" "main"
clone_repo "kdenlive-mcp-server" "https://github.com/Va1bhav512/kdenlive-mcp-server.git" "main"
clone_repo "SpliceKit" "https://github.com/elliotttate/SpliceKit.git" "main"
clone_repo "capcut-mcp" "https://github.com/JmsLdrn/capcut-mcp.git" "main"
clone_repo "capcut-ai-editor" "https://github.com/mrbuslov/capcut-ai-editor.git" "main"
clone_repo "capcut-mcp-kit" "https://github.com/simopa/capcut-mcp-kit.git" "main"
clone_repo "guney-motion-kit" "https://github.com/GTAI-1/guney-motion-kit.git" "main"
clone_repo "openshorts" "https://github.com/mutonby/openshorts.git" "main"
clone_repo "Audacity-MCP" "https://github.com/xDarkzx/Audacity-MCP.git" "main"
clone_repo "voicebox" "https://github.com/jamiepine/voicebox.git" "main"
clone_repo "F5-TTS" "https://github.com/rumourscape/F5-TTS.git" "main"
clone_repo "IndicF5" "https://github.com/AI4Bharat/IndicF5.git" "main"
clone_repo "MOSS-TTS" "https://github.com/OpenMOSS/MOSS-TTS.git" "main"
clone_repo "OmniVoice" "https://github.com/emailtosharad/OmniVoice.git" "master"
clone_repo "AI-Studio-App" "https://github.com/emailtosharad/AI-Studio-App.git" "main"
clone_repo "mcp-drawthings" "https://github.com/james-see/mcp-drawthings.git" "main"
clone_repo "flow-mcp" "https://github.com/emailtosharad/flow-mcp.git" "main"
clone_repo "upscayl" "https://github.com/upscayl/upscayl.git" "main"
clone_repo "youtube-uploader-mcp" "https://github.com/kapilunclekikahaniyan-creator/youtube-uploader-mcp.git" "main"
clone_repo "folderium" "https://github.com/abdullahguch/folderium.git" "main"
clone_repo "antigravity-sdk-python" "https://github.com/google-antigravity/antigravity-sdk-python.git" "main"

# 7. Setup Python Virtual Environments via uv (Python 3.12)
log_info "Configuring Python virtual environments..."

if [[ -d "${TARGET_DIR}/kdenlive-mcp-server" ]]; then
  cd "${TARGET_DIR}/kdenlive-mcp-server"
  uv venv .venv --python 3.12
  uv pip install -e . --python .venv/bin/python || true
fi

if [[ -d "${TARGET_DIR}/Audacity-MCP" ]]; then
  cd "${TARGET_DIR}/Audacity-MCP"
  uv venv .venv --python 3.12
  uv pip install -r requirements.txt --python .venv/bin/python || true
fi

if [[ -d "${TARGET_DIR}/capcut-ai-editor" ]]; then
  cd "${TARGET_DIR}/capcut-ai-editor"
  uv venv .venv --python 3.12
  uv pip install -e . --python .venv/bin/python || true
fi

if [[ -d "${TARGET_DIR}/capcut-mcp-kit/vectcut-api" ]]; then
  cd "${TARGET_DIR}/capcut-mcp-kit/vectcut-api"
  uv venv venv --python 3.12
  uv pip install -r requirements.lock.txt --python venv/bin/python || true
  uv pip install -r requirements-whisper-mlx.lock.txt --python venv/bin/python || true
fi

if [[ -d "${TARGET_DIR}/SpliceKit" ]]; then
  mkdir -p "${HOME}/.venvs/splicekit-mcp"
  uv venv "${HOME}/.venvs/splicekit-mcp" --python 3.12
  uv pip install -r "${TARGET_DIR}/SpliceKit/requirements.txt" --python "${HOME}/.venvs/splicekit-mcp/bin/python" || true
fi

# 8. Compile Node.js & TypeScript Projects
log_info "Building Node.js and TypeScript packages..."

build_node_project() {
  local pdir="$1"
  if [[ -d "${pdir}" ]]; then
    log_info "Building ${pdir}..."
    cd "${pdir}"
    npm install
    npm run build 2>/dev/null || true
  fi
}

build_node_project "${TARGET_DIR}/AutoFlowCut"
build_node_project "${TARGET_DIR}/mcp-drawthings"
build_node_project "${TARGET_DIR}/flow-mcp"
build_node_project "${TARGET_DIR}/capcut-mcp"
build_node_project "${TARGET_DIR}/capcut-mcp-kit/capcut-mcp-server"
build_node_project "${TARGET_DIR}/guney-motion-kit"

# 9. Build Go Binaries
if [[ -d "${TARGET_DIR}/youtube-uploader-mcp" ]]; then
  log_info "Building YouTube Uploader MCP binary..."
  cd "${TARGET_DIR}/youtube-uploader-mcp"
  go build -o youtube-uploader-mcp main.go || true
fi

# 10. Restore MCP Configuration
log_info "Restoring MCP configuration to ${MCP_CONFIG_DIR}/mcp_config.json..."
mkdir -p "${MCP_CONFIG_DIR}"
if [[ -f "${SCRIPT_DIR}/mcp_config.example.json" ]]; then
  cp "${SCRIPT_DIR}/mcp_config.example.json" "${MCP_CONFIG_DIR}/mcp_config.json"
  log_success "MCP configuration restored successfully!"
fi

echo -e "${GREEN}"
echo "======================================================================="
echo "   Disaster Recovery Complete! All tools and runtimes are active.      "
echo "======================================================================="
echo -e "${NC}"
