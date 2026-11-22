# Open Source Media & CLI Tools Registry

This document maintains a catalog of system-level open-source tools, their underlying mechanics ("how they work"), supported features, and standard operational commands.

> [!NOTE]
> **Automated Rule**: Whenever any new tool or CLI utility is installed or updated on this machine, this file must be updated with the tool's name, version, operational architecture, and usage patterns.

---

## Quick Reference Table

| Tool / Package | Primary Binary / Import | Installed Version | Primary Role | Core Dependencies / Delegates |
| :--- | :--- | :--- | :--- | :--- |
| **FFmpeg** | `ffmpeg`, `ffprobe`, `ffplay` | `9.0.2` | Complete video/audio processing pipeline | `libx264`, `libx265`, `svt-av1`, `libvpx`, `libopus`, `lame`, `dav1d`, `libvmaf`, VideoToolbox |
| **ImageMagick** | `magick` | `7.1.2-34` | Image processing, conversion, & composition | `webp`, `png`, `jpeg-turbo`, `libtiff`, `libheif`, `freetype`, `little-cms2` |
| **SoX** | `sox`, `soxi` | `14.4.2` | Audio signal processing, manipulation, & effects | `libsndfile`, `flac`, `libvorbis`, `libogg`, `opusfile`, `mad` |
| **MediaInfo** | `mediainfo` | `26.10` | Deep metadata & stream parameter inspection | `libmediainfo`, `libzen`, `glib` |
| **MLT Melt** | `melt` | `7.43.0` | CLI multimedia authoring & non-linear video engine | MLT framework, FFmpeg, SDL, Qt, frei0r |
| **Kdenlive** | `kdenlive`, `kdenlive_render` | `26.04.2` | Open-source non-linear video editor & timeline rendering engine | MLT framework, Qt6, KDE Frameworks (KF6), FFmpeg, VideoToolbox |
| **SoundFile** | `import soundfile` | `0.14.0` | High-fidelity audio I/O directly into NumPy arrays | `libsndfile`, CFFI |
| **NumPy** | `import numpy` | `2.5.4` | Vectorized numerical matrix & buffer manipulation | C/BLAS/Accelerate SIMD |
| **SciPy** | `import scipy` | `1.18.1` | DSP, spectral filtering, FFT, & envelope detection | NumPy |
| **Pillow** | `import PIL` | `12.3.0` | Python Imaging Library (batch raster transforms) | `libjpeg`, `zlib`, `libtiff`, `freetype` |
| **Matplotlib** | `import matplotlib` | `3.11.2` | Waveform, spectrogram, & loudness plotting | NumPy, Pillow, ContourPy |
| **Voicebox** | `voicebox`, `voicebox-server`, `voicebox-mcp` | `0.5.0` | Open-source AI voice studio, neural TTS, voice cloning & MCP audio server | Apple Silicon MLX (Metal), PyTorch, FastAPI, Tauri, Spotify Pedalboard, SQLite |
| **Bionic (LM Studio)** | `Bionic.app`, `lms` | `1.1.8` | Local LLM runtime, MLX inference engine & OpenAI-compatible API server | MLX (Metal), Apple Silicon GPU/NE, llama.cpp, Electron |
| **Hermes Agent** | `hermes` | `0.22.5` | Autonomous self-improving AI agent, tool-calling harness & messaging gateway | Python 3.14, uv, SQLite FTS5, TUI / Web UI, multi-provider LLM router |
| **Hermes Desktop** | `Hermes.app`, `hermes desktop` | `0.21.2` | Native Electron desktop UI & visual workspace for Hermes Agent | Electron, React, Vite, Hermes core backend, IPC bridge |
| **Antigravity SDK** | `import google.antigravity` | `0.1.22` | Python SDK for building, leasing, and orchestrating Antigravity AI agents | Python 3.14, uv, `google-genai`, `mcp`, `localharness` (Go binary) |
| **OpenAI Whisper** | `whisper` | `20250625` | Neural speech recognition, word-level timestamping, & multilingual transcription | PyTorch, NumPy, Tiktoken, Numba, FFmpeg |
| **Node.js & npm** | `node`, `npm` | `26.12.1` / `11.20.0` | High-performance JavaScript runtime & package ecosystem | Google V8, libuv, c-ares, llhttp, OpenSSL |
| **OpenShorts** | `start.sh`, `app.py` | `Git (0.0.0)` | AI-powered vertical short-form video generator & interactive studio | FastAPI, Vite/React, Faster-Whisper, YOLOv8, MediaPipe, FFmpeg, Gemini |
| **Draw Things MCP** | `mcp-drawthings` | `1.1.2` | Local AI image generation & img2img transform via Draw Things API | Node.js, `@modelcontextprotocol/sdk`, Draw Things HTTP API (`:7860`), Apple Silicon |
| **Upscayl** | `upscayl`, `Upscayl.app`, `upscayl-bin` | `2.15.0` | Open-source AI image upscaler & super-resolution engine | MoltenVK (Vulkan over Metal), NCNN, Real-ESRGAN, Electron, Next.js, Node.js |
| **F5-TTS** | `f5-tts-webui`, `f5-tts-cli` | `0.1.2` (Git `ae1fcd9`) | Flow-matching diffusion zero-shot voice cloning & Hindi TTS | PyTorch MPS (Metal), TorchCodec, Vocos, Faster-Whisper, Gradio, Librosa |
| **OmniVoice** | `omnivoice`, `omnivoice-demo`, `omnivoice-infer` | `0.2.1` | Massively multilingual zero-shot TTS (600+ langs), voice cloning & voice design | PyTorch MPS (Metal), Hugging Face Transformers, Gradio, Whisper, SoundFile |
| **BlackHole** | `BlackHoleXch.driver`, `install_driver.sh` | `0.7.1` | Zero-latency virtual audio loopback driver & CoreAudio HAL plugin | CoreAudio HAL, `coreaudiod`, macOS Audio MIDI Setup |
| **Maya 2 Native** | `start_studio.sh`, `maya_tts.sh`, `mlx_audio` | `0.6.3` / Weights `BF16` | High-fidelity Indic & English neural TTS, streaming, Gradio studio & persistent voice cloning lab | Apple Silicon MLX (Metal), Qwen3-1.7B, Kyutai Mimi, SpeechBrain ECAPA |
| **IndicF5** | `infer.py`, `f5_tts` | `0.1.0` (Git `main`) | Near-human polyglot TTS & zero-shot voice cloning for 11 Indian languages | PyTorch MPS (Metal), Hugging Face Transformers, TorchCodec, Vocos (24kHz), DiT CFM |
| **Vocalis (AI Studio App)** | `npm run dev`, `server.ts` | `4.0.0` | Studio-grade AI script & voice TTS studio, dialogue generator & voice cloner | Express, Vite 8, React 19, `@google/genai` (Gemini 2.5/Flash), Tailwind CSS v4, tsx |
| **Flow MCP** | `flow-mcp`, `npm run login`, `npm run studio` | `0.1.0` (Git `main`) | Browser-driven Google Flow video/character automation & local studio MCP server | Node.js, Playwright, Chrome DevTools Protocol, `@modelcontextprotocol/sdk`, Kokoro |
| **Go (Golang)** | `go`, `gofmt` | `1.27.3` | Open-source statically typed compiled programming language & toolchain | Go compiler, linker, runtime GC, Darwin ARM64 assembler |
| **YouTube Uploader MCP** | `youtube-uploader-mcp` | `0.1.3` (Git `main`) | Automated YouTube video upload, OAuth2 management, video updates & MCP server | Go 1.27, `mcp-go`, Google APIs (`youtube/v3`), OAuth2 |
| **Demucs** | `demucs`, `uvx --with numpy --from demucs demucs` | `4.1.0` | Deep learning music source separation & AI vocal/watermark isolation | PyTorch, TorchAudio, NumPy, Meta Research Hybrid Transformer (`htdemucs`) |
| **MOSS-SoundEffect v2.0** | `run_mac_infer.sh`, `infer_from_pipeline.py`, `run_mac_webui.sh` | `0.1.0` (Git `main`) | 48kHz stereo text-to-sound-effect & scene foley generation via Flow Matching DiT | PyTorch MPS (Metal), Hugging Face Transformers, Qwen3 text encoder, Descript Audio Codec (DAC VAE) |
| **AutoFlowCut** | `run.sh`, `AutoFlowCut.app`, `autoflowcut-mcp` | `3.2.2` (Git `main`) | Automated AI image/video pipeline, Story Engine & 1-click NLE exporter (CapCut / Premiere / Vrew) | Electron 36, React 18, Vite 6, Google GenAI SDK (Gemini & Veo), Staged FFmpeg, MCP Server |
| **GitHub CLI** | `gh` | `2.104.0` | Official GitHub command-line tool for OAuth authentication, git credentials, repo management | Go, GitHub REST/GraphQL API, `osxkeychain` credential helper |
| **Antigravity CLI** | `agy` | `1.5.12` | Standalone terminal interface & prompt runner for Antigravity AI agents | Go native Mach-O ARM64, Google Auth OAuth2/OIDC, localharness |
| **Guney Motion Kit** | `npm run new-video`, `hyperframes` | `0.1.0` (HyperFrames `0.7.109`) | AI motion graphics kit, HTML-to-video rendering, 3D cards, UI zooms & Resolve finish | Node.js, HyperFrames, Puppeteer-Core, Chrome Headless Shell, FFmpeg, GSAP |
| **CapCut MCP (Direct)** | `node src/server.js`, `capcut-mcp` | `0.1.0` (Git `main`) | Direct JSON timeline layout, segment trim/split, text overlays & atomic draft manipulation | Node.js, `@modelcontextprotocol/sdk`, Zod, FFprobe |
| **CapCut AI Editor (SmartCut)** | `python -m smartcut.server`, `smartcut` | `0.2.0` (Git `main`) | Automated silence trimming, pause removal & duplicate take detection via CapCut auto-captions | Python 3.12, MCP SDK, Pydantic, FastMCP |
| **CapCut MCP Kit & VectCutAPI** | `start-server.sh`, `capcut-mcp-server` | `0.12.1` / `1.0.0` | High-level CapCut production suite: 65 camera moves, keyframing, audio ducking, VFX & transitions | Node.js, TypeScript, Python 3.12, Flask, MLX-Whisper (Metal GPU), VectCutAPI |


---

## Detailed Tool Profiles & Working Mechanics

### 1. FFmpeg (`ffmpeg`, `ffprobe`, `ffplay`)

#### How It Works
FFmpeg operates as a linear, pipelined media engine consisting of the following internal phases:
```
[Input File] 
    ↓ Demuxer (libavformat)
[Encoded Packets] 
    ↓ Decoder (libavcodec)
[Uncompressed Frames] 
    ↓ Filter Graph (libavfilter)
[Processed Frames] 
    ↓ Encoder (libavcodec)
[Encoded Packets] 
    ↓ Muxer (libavformat)
[Output File]
```
- **Demuxing & Decoding**: Separates containers (e.g. MP4, MKV) into streams (video, audio, subtitles) and decodes compressed bitstreams into raw uncompressed buffers (YUV/RGB pixels, PCM audio).
- **Filtering**: Processes frames through complex directional acyclic filtergraphs (rescaling, cropping, fps conversion, audio ducking, loudness normalization).
- **Encoding & Muxing**: Compresses processed buffers using codecs (e.g., H.264, H.265, AV1, AAC, Opus) and packages them into container formats.

#### Key Capabilities
- Video transcoding with CPU (`libx264`, `libx265`, `libsvtav1`) or Apple Silicon hardware acceleration (`h264_videotoolbox`, `hevc_videotoolbox`).
- Audio extraction, stream mapping (`-map`), volume filtering (`loudnorm`, `volume`).
- High-precision lossless stream copying (`-c copy`) for fast trims and segment extraction without re-encoding.

#### Common Commands
```bash
# 1. Inspect file details and stream mapping
ffprobe -hide_banner -v error -show_format -show_streams input.mp4

# 2. Fast lossless cut without re-encoding
ffmpeg -ss 00:01:30 -to 00:02:15 -i input.mp4 -c copy cut.mp4

# 3. Transcode to H.264 with AAC audio (YouTube standard)
ffmpeg -i input.mov -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 320k output.mp4

# 4. Extract audio track to WAV (e.g., for transcription / Audacity)
ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 audio.wav

# 5. Two-pass EBU R128 loudness normalization
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 normalized.wav
```

---

### 2. ImageMagick (`magick`)

#### How It Works
ImageMagick reads raster, vector, and raw image files into an in-memory pixel cache. It executes operations sequentially via its unified command line engine (`magick`):
- **Delegates**: Relies on specialized external libraries for decoding and encoding specific formats (e.g., `libheif` for HEIC, `libjpeg-turbo` for JPEG, `libpng` for PNG, `libwebp` for WebP, `freetype` for font rendering).
- **Color Pipeline**: Employs Little-CMS (`lcms2`) and High Dynamic Range Imaging (HDRI) with 16-bit floating point precision per channel (`Q16-HDRI`), preserving chromatic accuracy through repeated transforms.

#### Key Capabilities
- Multi-format conversion (JPG, PNG, WebP, HEIC, TIFF, GIF, SVG).
- Complex canvas operations: compositing, alpha masking, dropshadows, borders, and overlays.
- Batch resizing, cropping, aspect ratio fitting (`-resize`, `-gravity`, `-extent`).
- Color adjustments: contrast stretching, brightness/saturation, gamma, blur, and sharpening.

#### Common Commands
```bash
# 1. Convert format with quality optimization (e.g., PNG to WebP)
magick input.png -quality 85 output.webp

# 2. Resize maintaining aspect ratio to fit within 1920x1080
magick input.jpg -resize 1920x1080\> output.jpg

# 3. Smart crop to exact 16:9 1920x1080 from center
magick input.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 thumbnail.jpg

# 4. Create an overlay with transparency
magick background.png watermark.png -gravity southeast -geometry +20+20 -composite composed.png

# 5. Extract image metadata (dimensions, color space, depth)
magick identify -format "%w x %h | %m | %r\n" image.png
```

---

### 3. SoX - Sound eXchange (`sox`, `soxi`)

#### How It Works
SoX is the "Swiss Army knife of sound processing". It streams raw audio samples through a chained series of Digital Signal Processing (DSP) effect blocks:
```
[Input Sound File] 
    ↓ Format Handler (libsndfile, flac, mad)
[PCM Audio Sample Stream] 
    ↓ Chain of DSP Effects (gain, pad, trim, silence, rate)
[Processed PCM Stream] 
    ↓ Format Writer
[Output Sound File]
```
- **Single-Pass Stream Processing**: SoX handles audio in a memory-efficient streaming fashion, allowing fast transforms of large multitrack or multi-hour audio files.
- **Header Inspection (`soxi`)**: Dedicated companion utility to instantly extract sample rate, precision, bit rate, channels, and sample counts without loading audio data.

#### Key Capabilities
- Sample rate conversion using band-limited sinc interpolation (`rate`).
- Dynamic processing: compand, norm, gain, silence truncation.
- Channel manipulation: stereo-to-mono downmixing, channel extraction, channel swapping.
- Audio synthesis: tone generation, noise generation, sweep tones.

#### Common Commands
```bash
# 1. Inspect audio file headers and properties
soxi input.wav

# 2. Trim audio from 10 seconds for a duration of 30 seconds
sox input.wav output.wav trim 10 30

# 3. Trim leading and trailing silence
sox input.wav output.wav silence 1 0.1 1% reverse silence 1 0.1 1% reverse

# 4. Resample to 44.1kHz 16-bit mono
sox input.wav -r 44100 -b 16 -c 1 output.wav

# 5. Apply fade in (1s) and fade out (2s)
sox input.wav output.wav fade t 1 0 2
```

---

### 4. MediaInfo (`mediainfo`)

#### How It Works
MediaInfo utilizes `libmediainfo` and `libzen` to parse binary container structures, stream headers, and metadata atoms without decoding entire media streams:
- It scans container-level headers (e.g., MP4 atoms like `moov`, MKV EBML tags, RIFF chunks) and initial packet headers for each elementary stream.
- Computes exact technical parameters including container duration, codec IDs, profile levels, color spaces (matrix coefficients, color primaries), frame rate mode (CFR/VFR), audio channel positions, and bitrates.

#### Key Capabilities
- Instantaneous analysis of video/audio attributes without CPU-intensive decoding.
- Structured output formatting: plain text, CSV, JSON, and XML for easy integration in scripts and automation pipelines.
- Detection of variable frame rate (VFR) vs constant frame rate (CFR) issues critical for video editing sync.

#### Common Commands
```bash
# 1. Full human-readable technical report
mediainfo input.mp4

# 2. Machine-readable JSON output (ideal for automation scripts)
mediainfo --Output=JSON input.mp4

# 3. Extract specific property (e.g., Video duration or Frame rate)
mediainfo --Inform="Video;%Duration% ms, %FrameRate% fps, %Width%x%Height%" input.mp4

# 4. Check audio stream encoding details
mediainfo --Inform="Audio;Format: %Format%, BitRate: %BitRate/String%, Channels: %Channel(s)%" input.wav
```

---

### 5. MLT Melt (`melt`)

#### How It Works
`melt` is the testbed and command-line playout/authoring tool for the **MLT (Media Lovin' Toolkit)** non-linear video editing framework. It orchestrates service graphs:
```
[Producers: Video/Audio Clips, MLT XML]
    ↓ Filters (scale, frei0r, affine, volume)
[Multitrack / Tractor]
    ↓ Transitions (mix, composite, luma wipes)
[Consumer: SDL Window / avformat Encoder]
```
- **Graph-Based Composition**: Constructs dynamic media trees consisting of producers (sources), tractors (multitrack containers), transitions, and filters.
- **Direct MLT XML Parsing**: Directly ingests Kdenlive `.kdenlive` or `.mlt` XML project files and processes timeline tracks frame-by-frame.
- **Headless Pipeline**: Eliminates the overhead of launching a graphical user interface when executing renders, testing transitions, or extracting frames.

#### Key Capabilities
- Headless command-line rendering of Kdenlive projects directly to final MP4/MKV video.
- Real-time video/audio playback and timeline scrub verification.
- Querying available MLT plugins, transitions, and audio/video filters (`-query`).
- In-place clip stitching, splitting, and effects chaining from the command line.

#### Common Commands
```bash
# 1. Inspect installed MLT producers, filters, and consumers
melt -query "producers"
melt -query "filters"
melt -query "consumers"

# 2. Preview/play an MLT or Kdenlive project in an SDL window
melt project.kdenlive

# 3. Render a Kdenlive MLT XML timeline to MP4 using avformat consumer
melt project.kdenlive -consumer avformat:output.mp4 acodec=aac vcodec=libx264 crf=18 preset=slow

# 4. Join two clips with an affine fade/dissolve transition
melt clip1.mp4 clip2.mp4 -attach-cut luma
```

---

### 6. Kdenlive & Kdenlive Render (`kdenlive`, `kdenlive_render`)

#### How It Works
Kdenlive is a full-featured, professional open-source non-linear video editing (NLE) application built on top of the MLT multimedia framework, Qt6, and KDE Frameworks (KF6):
- **Timeline Engine & Composition**: All video tracks, audio channels, transitions, cuts, and filters are represented as MLT nodes (`producers`, `tractors`, `multitracks`, and `filters`) and serialized directly into standard MLT XML (`.kdenlive` or `.mlt` files).
- **Process Isolation & Background Rendering**: Kdenlive delegates video export and timeline caching jobs to `kdenlive_render` as decoupled background worker processes. This prevents the editing interface from locking or stuttering during compute-heavy rendering.
- **Hardware Acceleration**: Natively delegates hardware-accelerated video decoding and encoding to Apple Silicon VideoToolbox (`h264_videotoolbox`, `hevc_videotoolbox`) via bundled FFmpeg libraries.
- **Execution Modes (`kdenlive_render`)**:
  - `delivery`: Final video rendering of the entire timeline or selected in/out frame zones.
  - `preview-chunks`: Background timeline rendering that computes frame chunks for real-time smooth playback cache.
- **MCP & Automation Interoperability**: Direct programmatic timeline assembly, track management, EDL syncing, and rendering control via the native `kdenlive-mcp-server`.

#### Key Capabilities
- Full non-linear multi-track editing (video, audio, text titles, and subtitle tracks).
- Keyframable motion graphics, color grading, audio leveling, and frei0r video effects.
- Headless batch rendering of queued Kdenlive jobs via `kdenlive_render` and `melt` without keeping the GUI open.
- Frame-accurate zone rendering (`in=`, `out=`).
- Native integration with the `kdenlive-mcp-server` for automated video generation pipelines.

#### Common Commands
```bash
# 1. Check installed version
/Applications/kdenlive.app/Contents/MacOS/kdenlive --version

# 2. Launch Kdenlive editor GUI
open /Applications/kdenlive.app

# 3. View usage and mode options for kdenlive_render
/Applications/kdenlive.app/Contents/MacOS/kdenlive_render --help

# 4. Render export job in delivery mode headless
/Applications/kdenlive.app/Contents/MacOS/kdenlive_render delivery in=0 out=1500 project.mlt output.mp4
```

---

### 7. Python Scientific & Audio/Media Stack

#### How It Works
The installed Python libraries form a high-performance programmatic processing pipeline for acoustic analysis, waveform audit, and programmatic image generation:
```
[Audio/Image File]
    ↓ SoundFile / Pillow (C-library bindings)
[Raw Samples / Pixel Matrices in NumPy]
    ↓ Vectorized Signal Processing / SciPy (FFT, RMS, Butterworth filters)
[Acoustic Envelopes / Spectral Peaks]
    ↓ Matplotlib / Export
[Visualizations, EDL Sync Markers, Audit Reports]
```
- **SoundFile (`0.14.0`)**: Interfaces with `libsndfile` via CFFI to read/write uncompressed PCM or FLAC/OGG audio directly into NumPy arrays as floating-point float32/float64 without intermediate temporary files.
- **NumPy (`2.5.4`)**: Implements strided multi-dimensional arrays (`ndarray`) with C/SIMD vectorization for ultra-fast calculation of root-mean-square (RMS) energy, dBFS loudness, and channel separation.
- **SciPy (`1.18.1`)**: Provides `scipy.signal` for short-time Fourier transform (STFT), spectrogram calculation, bandpass filtering, and speech/silence peak detection.
- **Pillow (`12.3.0`)**: Fast image format conversions, alpha channel manipulation, text watermarking, and thumbnail generation.
- **Matplotlib (`3.11.2`)**: Renders publication-grade waveforms, spectrograms, loudness curves, and edit timeline heatmaps.

#### Key Capabilities
- Acoustic speech boundary detection and silence measurement.
- Programmatic generation of storyboard cards, chapter slides, and thumbnails.
- Automated waveform verification and audio leveling validation for story audio.

#### Common Python Snippets
```python
import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt

# 1. Load audio file directly into NumPy array
data, samplerate = sf.read("narration.wav")

# 2. Compute RMS energy in 50ms windows for silence detection
window_len = int(samplerate * 0.05)
rms = np.sqrt(np.convolve(data**2, np.ones(window_len)/window_len, mode='valid'))
dbfs = 20 * np.log10(np.maximum(rms, 1e-5))

# 3. Detect silence regions below -45 dBFS
silence_mask = dbfs < -45

# 4. Generate and save a spectrogram plot
frequencies, times, spectrogram = signal.spectrogram(data, samplerate)
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram + 1e-10))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.savefig('spectrogram.png')
```

---

### 8. Voicebox (`voicebox`, `voicebox-server`, `voicebox-mcp`)

#### How It Works
Voicebox is an end-to-end, local AI voice studio and neural speech synthesis platform operating completely on-device without cloud dependencies. It functions across three interconnected architectural tiers:
```
[User UI / REST API / MCP Client (Claude, Cursor, Antigravity)]
    ↓ HTTP (Port 17493) / JSON-RPC stdio
[Voicebox FastAPI Backend Server]
    ↓ SQLite (sh.voicebox.app/voicebox.db) & Model Router
[TTS / STT Inference Engines]
    ├── MLX Metal Engine (Apple Silicon GPU/Neural Engine: Qwen3-TTS)
    ├── Fast Zero-Shot Cloning (LuxTTS, Kokoro 82M CPU)
    ├── Expressive Speech (Chatterbox Turbo with emotion & paralinguistic tags)
    └── Long-Form Acoustic (HumeAI TADA 1B/3B)
    ↓ Raw Waveform Buffer
[Spotify Pedalboard DSP Chain] (Pitch shift, Reverb, Delay, Chorus, Compressor, Filters)
    ↓ Output WAV / Direct Streaming Playback / Dictation Injection
[Audio Playback / Target Application Input]
```
- **Desktop & IPC Layer**: Tauri v2 native desktop shell providing a responsive GUI. Manages the lifecycle of the Python backend sidecar (`voicebox-server`) and monitors the parent PID watchdog.
- **Backend & Model Orchestration**: FastAPI and Uvicorn server managing a serialized GPU task queue to prevent concurrent VRAM contention. Auto-initializes local SQLite schemas for voice profiles, generation history, audio captures, and preset configurations.
- **Hardware Acceleration**: On macOS Apple Silicon (`arm64`), inference is driven natively by **MLX** via Apple Metal Performance Shaders (MPS) and the Apple Neural Engine, achieving 4-5x real-time generation speed.
- **Audio DSP Pipeline**: Post-processing utilizes Spotify's `pedalboard` library to apply real-time parametric audio filters, pitch shifting, dynamic range compression, and spatial reverbs.
- **Agent Interoperability (MCP & REST)**: Mounts a native Model Context Protocol (MCP) server at `/mcp` and provides the standalone `voicebox-mcp` stdio bridge. Local AI coding assistants can seamlessly call tools like `voicebox_speak` (with optional personality rewrites), `voicebox_transcribe`, and `voicebox_list_profiles`.

#### Key Capabilities
- **Zero-Shot Voice Cloning**: Clone reference voices from short audio samples (<10 seconds).
- **Multi-Engine Speech Generation**:
  - **Qwen3-TTS**: High-fidelity foundation voice cloning with voice design capabilities.
  - **LuxTTS**: Ultra-lightweight (~1GB VRAM), 48kHz output, up to 150x real-time on CPU.
  - **Chatterbox Multilingual**: Coverage across 23 languages (including Hindi, Arabic, Japanese, Spanish, etc.).
  - **Chatterbox Turbo**: Expressive speech supporting paralinguistic tags (`[laugh]`, `[sigh]`, `[whispering]`, `[gasp]`, `[angry]`, etc.).
  - **HumeAI TADA**: Coherent acoustic generation for extended story narration (700s+ dual alignment).
  - **Kokoro**: Ultra-fast, lightweight 82M parameter model running on CPU.
- **Voice Personalities**: Integrated local LLM (Qwen3) that automatically rewrites text into character persona before synthesis.
- **Local Dictation & Refinement**: Audio transcription into any application paired with local LLM cleanup.
- **Studio Audio Effects**: Integrated Spotify Pedalboard chain (Pitch Shift, Reverb, Delay, Chorus/Flanger, Compressor, Gain, High-Pass/Low-Pass filters).

#### Common Operational Commands
```bash
# 1. Launch Voicebox Desktop Application
open -a Voicebox
# or launch binary directly
voicebox

# 2. Run Headless Voicebox Server on Custom Port / Data Directory
voicebox-server --host 127.0.0.1 --port 17493 --data-dir "$HOME/Library/Application Support/sh.voicebox.app"

# 3. Generate Speech via REST API
curl -X POST http://127.0.0.1:17493/generate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Welcome to Voicebox local voice studio.",
    "profile_id": "<profile-uuid>",
    "language": "en"
  }'

# 4. Speak as an Agent via REST API
curl -X POST http://127.0.0.1:17493/speak \
  -H "Content-Type: application/json" \
  -H "X-Voicebox-Client-Id: terminal-agent" \
  -d '{
    "text": "Task completed successfully.",
    "profile": "Default"
  }'

# 5. Connect AI Coding Assistants via MCP stdio Bridge
# (Add to .mcp.json or agent configuration)
# {
#   "mcpServers": {
#     "voicebox": {
#       "command": "voicebox-mcp"
#     }
#   }
# }
```

---

### 9. Bionic / LM Studio (`Bionic.app`, `lms`)

#### How It Works
Bionic is an Apple Silicon-optimized local LLM workstation and inference environment based on LM Studio. It runs models like Google Gemma (`gemma-4-26B-A4B-it-QAT-MLX-4bit`) natively on Apple Silicon using Apple MLX / Metal:
```
[Client Application / Agent / Script]
    ↓ HTTP REST (Port 1234: /v1/chat/completions)
[Bionic / LM Studio Local Inference Daemon]
    ↓ MLX / Metal Unified Memory Architecture
[Local Model Weights (e.g. Gemma 4 MLX-4bit in ~/.lmstudio/models)]
    ↓ Apple Silicon GPU / Neural Engine Acceleration
[Generated Text Response (Streaming / JSON)]
```
- **Local Zero-Cost Compute**: All inference computations occur 100% on-device utilizing macOS Unified Memory and Metal shaders. No external API tokens, billing, or telemetry.
- **OpenAI-Compatible Standard**: Exposes a drop-in `/v1/chat/completions`, `/v1/models`, and `/v1/completions` API server for seamless integration with coding agents, scripts, and local applications.
- **Model Storage**: Model weights are stored under `~/.lmstudio/models/` in quantized GGUF or MLX safetensors formats.

#### Key Capabilities
- Native Apple Silicon MLX 4-bit quantization support for large models (e.g. Gemma 26B).
- Headless or GUI-driven local API server on `http://127.0.0.1:1234/v1`.
- CLI automation via `lms` (`lms load`, `lms server start`, `lms chat`).

#### Common Operational Commands
```bash
# 1. Launch Bionic Desktop App
open -a Bionic

# 2. Check Local Models via CLI
lms ls

# 3. Query Local Model via OpenAI-Compatible API
curl http://127.0.0.1:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma-4-26B-A4B-it-QAT-MLX-4bit",
    "messages": [{"role": "user", "content": "Hello Gemma!"}],
    "temperature": 0.7
  }'
```

---

### 10. Hermes Agent (`hermes`)

#### How It Works
Hermes Agent is an autonomous, self-improving AI agent harness and runtime developed by Nous Research. It operates as an extensible agent loop with persistent memory, tool sandboxing, and multi-channel messaging:
```
[User Interfaces: Terminal TUI / CLI / Web / Telegram / Discord / Slack / WhatsApp]
    ↓ Unified Messaging Gateway & Session Router
[Hermes Agent Core Engine]
    ├── Multi-Provider Model Router (Nous Portal, OpenRouter, OpenAI, Local Bionic/LM Studio)
    ├── Tool Execution Sandbox (Terminal, Browser, Python execution, File I/O, Cron)
    ├── Dynamic Skill Manager (58+ bundled skills, autonomous skill synthesis)
    ├── Dialectic Memory & Recall (SQLite FTS5, Honcho dialectic user modeling, SOUL.md)
    └── Subagent Delegation (Isolated parallel workstreams & RPC tool calls)
    ↓ Tool Executions / Natural Language Responses / Scheduled Deliveries
```
- **Closed Learning Loop**: The agent observes its own problem-solving trajectories, autonomously creates new skill modules after complex workflows, and optimizes existing skills over time via background curation (`hermes curator`).
- **Memory & Cross-Session Search**: Utilizes SQLite with FTS5 full-text indexing to search past conversations, extract high-level user context, and maintain persistent identity (`SOUL.md`) and user profiles (`USER.md`, `MEMORY.md`).
- **Unified Gateway**: Operates a single gateway process capable of simultaneously managing interactive CLI sessions alongside messaging bots (Telegram, Discord, Slack, WhatsApp, Signal) with unified session context.
- **Provider-Agnostic Router**: Dynamically switches between commercial cloud endpoints (Nous Portal, OpenRouter, Anthropic, OpenAI) and local models (such as Google Gemma running on Bionic / LM Studio at `http://127.0.0.1:1234/v1`).

#### Key Capabilities
- **Native Desktop Application (Hermes Desktop)**: Full-featured Electron GUI (`/Applications/Hermes.app`) supporting multi-session workspaces, drag-and-drop file attachments, live streaming tool visualizers, side-by-side artifact/code previews, and integrated local model controls.
- **Terminal TUI**: Interactive terminal interface with slash-command autocomplete, multiline editing, streaming tool output, and interrupt-and-redirect controls.
- **Autonomous Skill Evolution**: Learns from task execution, generates domain skills, and manages 58+ built-in automation skills.
- **Scheduled Automations**: Embedded natural-language cron scheduler capable of executing unattended tasks (nightly audits, backups, monitoring) and routing output to any platform.
- **Subagent Parallelization**: Delegates tasks to isolated subagents to parallelize complex workflows without inflating primary context windows.
- **Local LLM Integration**: Connects directly to local OpenAI-compatible backends like Bionic (`gemma-4-26B-A4B-it-QAT-MLX-4bit`) with zero API costs.

#### Common Operational Commands
```bash
# 1. Start Interactive Chat Session
hermes

# 2. Run Interactive Setup Wizard (Configure API Keys & Providers)
hermes setup

# 3. Select Model / Provider (Switch to Local or Cloud)
hermes model

# 4. Quick Single-Prompt Execution
hermes chat -z "Explain the current workspace setup."

# 5. Connect to Local Gemma on Bionic
hermes --provider openai --model gemma-4-26B-A4B-it-QAT-MLX-4bit

# 6. Run Background Skill Curator / Maintenance
hermes curator run --dry-run

# 7. Launch Native Desktop App
open /Applications/Hermes.app
# Or launch/build from CLI
hermes desktop
```

### 11. Google Antigravity Python SDK (`google-antigravity`)

#### How It Works
The Google Antigravity SDK is a native Python SDK and execution runtime for orchestrating AI coding and autonomous agents powered by Antigravity and Gemini. It pairs high-level Python abstractions with a compiled, platform-native Go binary runtime (`localharness`):
```
[Python Script / Application / CLI]
    ↓ Python SDK API (Agent, LocalAgentConfig, CapabilitiesConfig)
[Antigravity Python Runtime Layer]
    ↓ WebSockets / Subprocess IPC (Bidirectional Protobuf Events)
[localharness Go Binary (google/antigravity/bin/localharness)]
    ├── Model Router & Provider Interface (Gemini 3.8 / 3.0 Pro/Flash, Vertex AI, Local LLMs)
    ├── Tool Execution Engine (Built-in run_command, view_file, edit_file + Custom Python Callables)
    ├── MCP Client Bridge (Stdio & SSE Model Context Protocol servers)
    ├── Hook & Policy Manager (Rule-based approvals, ask_user callbacks, telemetry hooks)
    └── Native Workspace & Process Containment
    ↓ Streaming Response Tokens / Thought Deltas / Tool Call Executions
```
- **Compiled Native Runtime (`localharness`)**: The SDK delegates sandboxing, event multiplexing, and core tool execution to a platform-native Mach-O arm64 executable (`localharness`) bundled inside the PyPI wheel.
- **Asynchronous Agent Lifecycle**: Agents run inside an `async with Agent(config) as agent:` context manager that automatically handles process spawning, heartbeat liveness, protocol handshakes, and clean teardown.
- **Streaming Tokens, Thoughts, & Tool Calls**: Yields response text chunks (`async for token in response:`), thought deltas (`async for thought in response.thoughts:`), and tool invocation events (`async for call in response.tool_calls:`) as they arrive.
- **Unified Provider & Auth Flexibility**: Supports direct Gemini Developer API (`GEMINI_API_KEY`), Gemini Enterprise Agent Platform (formerly Vertex AI) in Express Mode (API Key) or Standard Mode (GCP Project + ADC), and local OpenAI-compatible endpoints (e.g., Bionic / LM Studio).
- **Extensible Tooling & MCP Integration**: Any Python function with docstrings and type annotations can be exposed directly as an agent tool via `tools=[my_func]`. External MCP servers are attached seamlessly via `types.McpStdioServer`.

#### Key Capabilities
- **Programmatic Agent Leasing**: Spin up, configure, and communicate with agents directly within Python workflows, scripts, or testing suites.
- **Human-in-the-Loop Policies**: Intercept tool execution requests with interactive terminal prompts, automated approval rules (`policy.allow`, `policy.deny`), or custom dynamic policy callbacks.
- **Multi-Turn Trajectory & Telemetry**: Full token usage telemetry (prompt, cached, thought, output tokens) and step-by-step trajectory inspection via `agent.conversation.history`.
- **Integrated MCP Bridge**: Connect external tools from any Model Context Protocol (MCP) server over stdio or SSE.
- **Workspace Sandboxing**: Enforces workspace containment and tool permission boundaries natively.

#### Common Operational Commands
```bash
# 1. Activate Antigravity SDK Virtual Environment
source /Users/sharadkumar/opensource/antigravity-sdk-python/.venv/bin/activate

# 2. Verify SDK Installation & Binary Discovery
python -c "import google.antigravity as ag; print('Antigravity SDK ready:', ag.__file__)"

# 3. Run Quickstart / Hello World Example
export GEMINI_API_KEY="your_api_key_here"
python /Users/sharadkumar/opensource/antigravity-sdk-python/examples/getting_started/hello_world.py

# 4. Launch Interactive CLI Demo
python /Users/sharadkumar/opensource/antigravity-sdk-python/examples/deep_dives/interactive_cli.py

# 5. Run Unit Test Suite
pytest /Users/sharadkumar/opensource/antigravity-sdk-python/google/antigravity/hooks/policy_test.py
```

---

### 12. OpenAI Whisper (`whisper`)

#### How It Works
OpenAI Whisper is an end-to-end, encoder-decoder Transformer model trained on 680,000 hours of multilingual and multitask supervised audio data:
```
[Input Audio / Video (WAV, MP3, MP4, MKV)]
    ↓ Audio Ingestion & Resampling (FFmpeg → 16 kHz mono)
[16 kHz Mono Audio Buffer]
    ↓ 80-channel Log-Magnitude Mel Spectrogram (25 ms window, 10 ms hop)
[Audio Feature Representation (T × 80)]
    ↓ Transformer Audio Encoder (Convolutional stem + Multi-Head Self-Attention)
[Encoded Audio Representations]
    ↓ Cross-Attention Transformer Decoder + Text Prompt / Task Tokens
[Autoregressive Next-Token Predictions]
    ├── Multitask Prefix: <|startoftranscript|> <|lang|> <|transcribe|translate|> <|notimestamps|>
    ├── Word-Level Timestamp Alignment via Dynamic Time Warping (DTW) on Cross-Attention Weights
    └── Temperature Fallback Loop (0.0 → 0.2 → 0.4 → 0.6 → 0.8 → 1.0 on low logprob / high compression)
    ↓
[Synchronized Transcripts (.srt, .vtt, .tsv, .json, .txt)]
```
- **Acoustic Front-End**: Audio files are ingested via FFmpeg and converted to 16,000 Hz 32-bit float mono buffers, then segmented into 30-second windows and mapped into 80-channel log-Mel spectrograms.
- **Multitask Autoregressive Decoder**: A single model controls language detection, speech recognition, voice activity detection (no-speech probability scoring), and speech translation to English via special token conditioning.
- **Timestamp Dynamic Time Warping (DTW)**: Computes cross-attention alignment matrices between decoded text tokens and encoder frame features, generating frame-accurate word-level timestamps without an external phoneme aligner.
- **Temperature Fallback Heuristic**: Detects transcription failure modes (hallucinations, repetitive loops) using gzip compression ratios and average token log probabilities, automatically retrying with higher sampling temperatures when thresholds are exceeded.

#### Key Capabilities
- **Robust Multilingual Speech Recognition**: Accurately transcribes spoken content in 99+ languages even in noisy environments or low bitrates.
- **Direct Speech Translation**: Translates any spoken language directly into English text transcripts in a single inference pass.
- **Word-Level Subtitle Generation**: Produces frame-accurate word and sentence timings for `.srt` and `.vtt` subtitles suitable for vertical Shorts, Reels, and TikToks.
- **Automated Voice Activity & Silence Detection**: Evaluates no-speech probabilities to skip music beds and long story silences without hallucinating phantom text.
- **Hardware Acceleration**: Executes on Apple Silicon using PyTorch's Metal Performance Shaders (`mps`) or CPU with vectorized float operations.

#### Common Operational Commands
```bash
# 1. Basic Transcription (Default model: small, auto-detect language)
whisper audio.mp3 --output_dir ./transcripts

# 2. Transcribe for Shorts / Subtitles with Word-Level Timestamps
whisper podcast.mp4 --model small --word_timestamps True --output_format srt --output_dir ./subtitles

# 3. Fast High-Accuracy Transcription with Language Hint
whisper voiceover.wav --model medium --language Hindi --output_format all

# 4. Direct Translation to English
whisper foreign_interview.m4a --task translate --model small

# 5. Extract Rich JSON (Tokens, Probabilities, Exact Timestamps)
whisper dialogue.wav --model base --output_format json

# 6. Python API Execution
python3 -c "
import whisper
model = whisper.load_model('base')
result = model.transcribe('audio.mp3', word_timestamps=True)
print(result['text'])
"
```

---

### 13. Node.js & npm (`node`, `npm`)

#### How It Works
Node.js executes JavaScript server-side using Google Chrome's V8 high-performance engine combined with an asynchronous event-driven I/O loop managed by `libuv`:
```
[JavaScript / TypeScript Application Code]
    ↓ V8 Just-In-Time (JIT) Compiler (Bytecode & Native Machine Code)
[Node.js Core Bindings & C++ Addons]
    ↓ libuv Event Loop & Thread Pool
[Asynchronous Non-Blocking I/O (File System, Sockets, Child Processes, Timers)]
    ↓ Completion Callbacks & Microtask Queue
[Browser / Frontend / Backend Responses]
```
- **V8 JIT Optimization**: Translates high-level ECMAScript directly into native ARM64 instructions on Apple Silicon.
- **Single-Threaded Event Loop**: Handles thousands of concurrent network connections without thread context-switching overhead.
- **Integrated Package Manager (`npm`)**: Resolves, hashes, caches, and installs dependency trees into `node_modules` with deterministic dependency lockfiles.

#### Key Capabilities
- **Frontend Build & Bundling**: Powers Vite, Webpack, PostCSS, and Tailwind compiler pipelines with instantaneous Hot Module Replacement (HMR).
- **Universal JavaScript Runtime**: Executes headless tooling, local API dev servers, and media editing interfaces (like OpenShorts dashboard and Remotion).

#### Common Operational Commands
```bash
# 1. Check Node and npm versions
node -v && npm -v

# 2. Run local script or server
node server.js

# 3. Install project dependencies
npm install

# 4. Launch Vite / Next.js development server
npm run dev

# 5. Build production bundle
npm run build
```

---

### 14. OpenShorts (`start.sh`, `app.py`, `dashboard`)

#### How It Works
OpenShorts is an automated, AI-driven short-form video creation platform and editing studio. It converts long horizontal videos (podcasts, lectures, gameplay, interviews) into viral 9:16 vertical clips formatted for YouTube Shorts, Instagram Reels, and TikTok:
```
[Input Long-Form Video (Local File or YouTube URL via yt-dlp)]
    ├── Audio Extraction → 16 kHz Mono
    │       ↓
    │   faster-whisper (Word-level timestamps & speech recognition)
    │       ↓
    │   Timestamped Transcript Representation
    │       ↓
    │   Google Gemini Flash (LLM viral moment scoring & title generation)
    └── Video Stream → Content-Aware Scene Detection (PySceneDetect / TransNetV2)
            ↓
[Moment Candidate Windows (15–60 seconds)]
    ↓ Dual-Mode Computer Vision Auto-Framing (YOLOv8 + MediaPipe Active Speaker Tracking)
[Calculated 9:16 Dynamic Pan & Scan Trajectories / Layout Bounding Boxes]
    ↓ Multi-Filter FFmpeg Graph (Reframing, Aspect Ratio Scaling, Crop Adjustments)
[Rendered Vertical 9:16 Video Base]
    ↓ Subtitle Generation (Dynamic word-by-word karaoke captions burned via ASS/SRT)
[Final Polished Short + Interactive Preview in React/Vite Dashboard]
```
- **Viral Moment Discovery**: Analyzes speech transcripts alongside scene boundary markers. Queries Google Gemini to detect narrative peaks, punchlines, or key insights, returning precise in/out cuts.
- **Dynamic Active Speaker Auto-Centering**: Uses YOLOv8 object detection to locate human bodies and MediaPipe Face Mesh to identify facial motion and mouth movements, dynamically shifting the 9:16 bounding box to keep the speaking individual centered.
- **Dual-Engine Architecture**: Built on a modular FastAPI backend (`app.py`, port 8000) managing job queues and child processing workers, coupled to a React 18 / Vite interactive timeline dashboard (`dashboard/`, port 5173).

#### Key Capabilities
- **Batch Highlight Extraction**: Converts a single long-form video into multiple viral clips in one pass.
- **Canonical Devanagari Screenplay Alignment**: Built-in 4-layer alignment engine eliminating 100% of Faster-Whisper phonetic and slurred ASR spelling errors ("परीचे" ➔ "परिचय", "पट जाएगा" ➔ "फट जाएगा", "मंतुरी" ➔ "मंत्री", "संकेट" ➔ "संकेत", "लिकिन" ➔ "लेकिन"). Force-aligns ground-truth canonical screenplay text against Whisper acoustic millisecond word boundaries using `difflib.SequenceMatcher`.
- **Automatic Story Screenplay Discovery**: Automatically crawls up directory trees (up to 4 levels) to auto-detect canonical screenplay JSON/MD files (`Script/*Canonical*.json`, `*Clips*.json`, `*Screenplay*.md`) when processing story videos.
- **Phonetic & Contextual Fallback Dictionary**: Even when no external screenplay is supplied, `subtitles.py` runs `clean_devanagari_word` and contextual grammar heuristics to sanitize known Whisper acoustic distortions.
- **Word-Level Subtitles & Effects**: Burns stylized, color-highlighted subtitles directly into the video stream.
- **Devanagari & Multilingual Typography**: Automatic script-aware font routing to `Noto Sans Devanagari` for Hindi/Devanagari text, with uppercase suppression, bright `#FFE500` active word pop, and font fallback mapping in `openshorts-fontmap.conf`.
- **CoreText Indic Typography Shaper (`bin/render_devanagari_banner.swift` & `bin/render_devanagari_banner`)**: Native Apple CoreText / CoreGraphics typography engine compiled for Apple Silicon macOS. Provides 100% grammatically and typographically accurate Indic matra positioning and conjunct shaping ("विक्रम", "सिर", "बुद्धिमान", "परिचय") with zero Pillow non-Raqm displacement artifacts. Features two dedicated modes:
  * **Banner Pill Mode (`--mode banner`)**: Supports both tight cropped pills (`--box-only` for OpenShorts `hooks.py` video overlays) and full 1080x1920 canvas overlays (`--full-canvas` for thumbnail compositing) with rounded dark pills, gold outline, inner glow, and centered Indic typography.
  * **Thumbnail Text Mode (`--mode thumbnail`)**: Renders high-impact YouTube thumbnail headlines into clean transparent overlays with heavy strokes and Gaussian blurred drop shadows for `thumbnail.py` (`burn_thumbnail_text`).
- **Whisper Medium Integration**: Powered by local Faster-Whisper `medium` (int8) with explicit Hindi language forcing (`WHISPER_LANGUAGE=hi`), Devanagari script priming (`WHISPER_INITIAL_PROMPT`), and CLI flags (`-l` / `--language`, `--whisper-model`, `--canonical-script`).
- **Interactive Web Timeline**: Preview clips, adjust crop boundaries, tweak text/fonts, and trigger re-renders instantly in the browser.
- **Local-First Privacy**: Runs completely on local hardware using faster-whisper and FFmpeg, avoiding recurring SaaS per-clip subscriptions.

#### Common Operational Commands
```bash
# 1. Launch OpenShorts (Starts both FastAPI backend on :8000 and Vite dashboard on :5173)
/Users/sharadkumar/opensource/openshorts/start.sh

# 2. Access Web Dashboard
open http://localhost:5173

# 3. Access Interactive Backend Swagger API Docs
open http://localhost:8000/docs

# 4. Activate Dedicated Virtual Environment
source /Users/sharadkumar/opensource/openshorts/.venv/bin/activate

# 5. Run Single Video Pipeline via CLI with Canonical Hindi Screenplay Alignment
python /Users/sharadkumar/opensource/openshorts/main.py \
  --input video.mp4 \
  --output ./output \
  --canonical-script /path/to/canonical_screenplay.json \
  --language hi \
  --whisper-model medium
```

---

### 15. Draw Things MCP Server (`mcp-drawthings`)

#### How It Works
`mcp-drawthings` is a Model Context Protocol (MCP) server that provides a bridge between AI agent orchestrators (Antigravity, Claude, Cursor) and the [Draw Things](https://drawthings.ai/) native macOS application. It handles local AI image generation and image editing offline using Apple Silicon hardware:
```
[MCP Client (Antigravity / Claude / Cursor)]
    ↓ stdio JSON-RPC (Tools: generate_image, transform_image, get_config, check_status)
[mcp-drawthings Node.js Service (dist/index.js)]
    ↓ HTTP REST API Requests (Port 7860)
[Draw Things App Built-in API Server]
    ↓ Apple Silicon Neural Engine / Metal Acceleration
[Diffusion Pipeline (FLUX.1, SDXL, Stable Diffusion 1.5/2.1, LoRAs)]
    ↓ Rendered Image Buffer (Base64)
[Local Storage: ~/Pictures/drawthings-mcp or custom output path]
```
- **Standard Protocol Bridge**: Implements the MCP protocol over `stdio`, translating high-level agent tool calls into Draw Things REST API requests (`/sdapi/v1/txt2img`, `/sdapi/v1/img2img`, `/sdapi/v1/options`).
- **Hardware-Accelerated Local Inference**: Utilizes Draw Things' Metal and Apple Neural Engine optimizations to execute inference locally without external cloud API dependencies.
- **Image Lifecycle Management**: Automatically decodes output base64 data streams, generates unique filenames or saves to custom paths, and passes structured file locations back to the requesting agent.

#### Key Capabilities & Tool Definitions
| Tool | Purpose | Core Parameters | Output |
| :--- | :--- | :--- | :--- |
| `check_status` | Verifies whether the Draw Things API server is running and accessible. | None | Server health status (`running: true/false`, URL) |
| `get_config` | Retrieves the active model, dimensions, sampler, and settings currently loaded in Draw Things. | None | Loaded model name, current sampler, default dimensions, step counts |
| `generate_image` | Generates a new image from a text prompt. | `prompt` (required), `negative_prompt`, `width` (default: 512), `height` (default: 512), `steps` (default: 20), `cfg_scale` (default: 7.5), `seed` (-1 for random), `output_path` | Saved image file path, dimensions, generation metadata |
| `transform_image` | Edits/transforms an existing image using prompt guidance (img2img). | `prompt` (required), `image_path` or `image_base64` (required), `denoising_strength` (0.0–1.0, default: 0.75), `steps`, `cfg_scale`, `seed`, `output_path` | Saved transformed image path, generation metadata |

#### Configuration & Environment Variables
The MCP server accepts the following environment variables to customize runtime network binding and asset destinations:
- **`DRAWTHINGS_HOST`**: Host address where Draw Things API is listening (default: `127.0.0.1` or `localhost`).
- **`DRAWTHINGS_PORT`**: Port number for Draw Things API (default: `7860`).
- **`DRAWTHINGS_OUTPUT_DIR`**: Default storage directory for generated images (default: `~/Pictures/drawthings-mcp`).

#### Setup & How to Run

##### Step 1: Start Draw Things & Enable API Server
1. Launch the **Draw Things** app on macOS (`open -a "Draw Things"` or via Spotlight).
2. Click the **Settings (⚙️)** gear icon.
3. Scroll to **API Server / HTTP Server** and toggle it **On** (runs on port `7860`).
4. Ensure a base model (e.g. *Generic (Stable Diffusion v1.5)*, *SDXL*, or *FLUX.1 [schnell]*) is selected/downloaded in the app interface.

##### Step 2: Global MCP Registration
Configured in `~/.gemini/config/mcp_config.json`:
```json
{
  "mcpServers": {
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
    }
  }
}
```

##### Step 3: Operational Verification Commands
```bash
# 1. Verify Draw Things HTTP API server connectivity
curl -s http://127.0.0.1:7860/sdapi/v1/options | jq .

# 2. Check loaded model names in Draw Things
curl -s http://127.0.0.1:7860/sdapi/v1/sd-models | jq .

# 3. Test direct REST text-to-image generation via curl
curl -X POST http://127.0.0.1:7860/sdapi/v1/txt2img \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "cinematic portrait of an ancient indian storyteller, 8k resolution, detailed lighting",
    "negative_prompt": "blurry, low quality, distorted",
    "width": 512,
    "height": 512,
    "steps": 20,
    "cfg_scale": 7.5
  }' -o /tmp/dt_response.json

# 4. Rebuild MCP server from TypeScript source
cd /Users/sharadkumar/opensource/mcp-drawthings
npm install && npm run build

# 5. Test manual stdio launch of the MCP server
node /Users/sharadkumar/opensource/mcp-drawthings/dist/index.js

# 6. Check global Antigravity MCP server configuration
cat ~/.gemini/config/mcp_config.json | jq .
```

#### Troubleshooting
- **Connection Refused (`ECONNREFUSED 127.0.0.1:7860`)**: The Draw Things app is not open or the API Server toggle is switched off in Settings (⚙️). Open Draw Things and turn on the API Server.
- **Port Conflict**: If another local process uses port `7860` (e.g. WebUI or Gradio), change the port in Draw Things settings and update `DRAWTHINGS_PORT` in `~/.gemini/config/mcp_config.json`.
- **Missing Output Directory**: Ensure `~/Pictures/drawthings-mcp` exists (`mkdir -p ~/Pictures/drawthings-mcp`) so generated images write without permission hurdles.

---

### 16. Upscayl (`upscayl`, `Upscayl.app`, `upscayl-bin`)

#### How It Works
Upscayl is a high-performance open-source AI image upscaler and super-resolution studio operating completely on-device without external cloud services. It combines an Electron/Next.js desktop workstation with an optimized C++ neural network inference core (`upscayl-bin` powered by Tencent NCNN and MoltenVK):
```
[Low-Res Input Image (JPG / PNG / WEBP)]
        ↓ Image Loader (libwebp / stb_image)
[RGB Planar Tensors (Normalized FP32 / FP16)]
        ↓ Vulkan API Pipeline (MoltenVK Driver Bridge)
[Apple Metal Compute Shaders on Apple Silicon GPU]
        ↓ NCNN Neural Super-Resolution Graph Execution
  ┌────────────────────────────────────────────────────────┐
  │  Deep Residual Dense Network (RRDBNet / Compact Net)  │
  │  Multi-Layer Feature Extraction & Residual Scaling    │
  │  Weights: upscayl-standard / ultrasharp / remacri     │
  └────────────────────────────────────────────────────────┘
        ↓ Dynamic Tiled Synthesis (-t) + Optional TTA (-x)
[High-Res Uncompressed Frame Buffer (2x, 3x, 4x Scale)]
        ↓ Multi-Format Encoder (libpng / libwebp / libjpeg)
[High-Res Enhanced Output Image File]
```
- **NCNN + MoltenVK Inference Engine**: `upscayl-bin` executes deep convolutional neural network graphs via Tencent NCNN compiled with a Vulkan compute backend. On macOS Apple Silicon (`arm64`), Vulkan commands map directly to native Metal compute shaders via MoltenVK (`[0 Apple M6]`), enabling ultra-fast hardware acceleration without CPU overhead or thermal throttling.
- **Dynamic Tiling Subsystem (`-t`)**: High-resolution image generation automatically segments inputs into overlapping square tiles (e.g. 256x256 or 512x512). This ensures processing large multi-megapixel images never exceeds GPU unified memory limits, fusing the tiles seamlessly back into the canvas with anti-seam feathering.
- **Test-Time Augmentation (TTA, `-x`)**: Performs spatial inference over 8 augmented variants of each tile (rotations and flips) and aggregates the predictions, eliminating directional aliasing and maximizing edge reconstruction fidelity.
- **Component & Workspace Architecture**:
  - **Source Repository**: `/Users/sharadkumar/opensource/upscayl` (TypeScript, Next.js 15, Electron 33).
  - **Packaged Desktop App**: `/Applications/Upscayl.app` (includes bundled models and universal binaries).
  - **Global CLI Utility**: `/Users/sharadkumar/.local/bin/upscayl` (universal wrapper supporting CLI flags, auto-pathing, and GUI launching).
  - **Inference Binary**: `/Applications/Upscayl.app/Contents/Resources/bin/upscayl-bin`.
  - **Model Repository**: `/Applications/Upscayl.app/Contents/Resources/models/` (`.bin` weights + `.param` network topologies).

#### Supported AI Models & Neural Weights
All pre-trained neural models are locally installed and immediately accessible:

| Model Identifier (`-n`) | Neural Architecture | Native Scale | Target Content & Domain Specialization | Param / Weight Files |
| :--- | :--- | :--- | :--- | :--- |
| **`upscayl-standard-4x`** | Real-ESRGAN (RRDBNet) | 4x *(Default)* | Natural photography, landscapes, real-world textures, and general graphics. | `upscayl-standard-4x.param` / `.bin` |
| **`ultrasharp-4x`** | Compact-ESRGAN UltraSharp | 4x | Micro-detail enhancement, architectural lines, jewelry, hair strands, and crisp edges. | `ultrasharp-4x.param` / `.bin` |
| **`remacri-4x`** | Remacri Architecture | 4x | Organic textures, human portraiture, skin tones, and film grain preservation. | `remacri-4x.param` / `.bin` |
| **`ultramix-balanced-4x`** | Hybrid Ensemble | 4x | Balanced blend between razor sharpness and smooth tonal gradation; ideal for stylized photos. | `ultramix-balanced-4x.param` / `.bin` |
| **`digital-art-4x`** | Anime / Illustration ESRGAN | 4x | 2D animations, anime, manga, cel-shaded graphics, vector art, and digital paintings. | `digital-art-4x.param` / `.bin` |
| **`high-fidelity-4x`** | High-Fidelity Denoising | 4x | Heavy JPEG artifact removal, noisy scans, low-light photograph restoration. | `high-fidelity-4x.param` / `.bin` |
| **`upscayl-lite-4x`** | MobileNet Ultra-Lite | 4x | Ultra-fast preview upscaling with minimal memory footprint and instant turnaround. | `upscayl-lite-4x.param` / `.bin` |

#### CLI Parameters & Operational Flags Reference
The global `upscayl` command accepts the following options:

| Flag | Parameter | Default | Description |
| :--- | :--- | :--- | :--- |
| `-i` | `<path>` | **Required** | Path to input image file (`.jpg`, `.png`, `.webp`) or directory of images. |
| `-o` | `<path>` | **Required** | Destination path for the upscaled image or target output folder. |
| `-n` | `<name>` | `upscayl-standard-4x` | Name of the AI model to execute (e.g. `ultrasharp-4x`, `digital-art-4x`). |
| `-s` | `<int>` | `4` | Custom output scale factor (`2`, `3`, or `4`). |
| `-z` | `<int>` | `4` | Scale factor according to the model architecture (`2`, `3`, or `4`). |
| `-m` | `<dir>` | App Models Folder | Path to pre-trained model directory containing `.param` and `.bin` files. |
| `-f` | `<ext>` | Same as input / `png` | Output image encoding format (`png`, `jpg`, `webp`). |
| `-c` | `<int>` | `0` | Output compression quality level (`0` to `100`). |
| `-r` | `<WxH>` | None | Resize output to specific target dimensions (e.g. `1920x1080` or `3840x2160`). |
| `-w` | `<width>`| None | Resize output proportionally to target pixel width. |
| `-t` | `<size>` | `0` (Auto) | Tile size for GPU inference (`0` = automatic; `256`, `512` for manual memory limits). |
| `-g` | `<id>` | `auto` | GPU device ID to utilize (`0` for primary Apple Silicon GPU). |
| `-j` | `<l:p:s>`| `1:2:2` | Thread allocation for `load:process:save` pipeline stages. |
| `-x` | None | Disabled | Enables Test-Time Augmentation (TTA) for enhanced edge reconstruction. |
| `-v` | None | Disabled | Enables verbose operational logging to console. |
| `--list-models` | None | - | Lists all installed models in the current models directory. |
| `--gui` / `--app`| None | - | Launches the native Upscayl desktop GUI application. |

#### Key Capabilities
- **Local Super-Resolution**: Lossless 2x, 3x, and 4x neural upscaling for raster assets without cloud subscriptions.
- **Metal Hardware Acceleration**: Direct Apple Silicon GPU acceleration via MoltenVK compute shaders.
- **Directory Batching**: One-shot batch enhancement of whole folders with identical or custom model parameters.
- **Flexible Rescaling & Resizing**: Automatic scaling coupled with explicit pixel dimension targeting (`-r`, `-w`).
- **Interactive Desktop Studio**: Side-by-side split screen comparison slider, batch queues, and custom model import in `/Applications/Upscayl.app`.

#### Common Operational Commands
```bash
# 1. Basic 4x upscale of a single image using the default model
upscayl -i lowres.jpg -o hires.png

# 2. Upscale with UltraSharp model for razor-sharp textures and intricate details
upscayl -i product.jpg -o product_sharp.png -n ultrasharp-4x

# 3. Upscale anime, digital artwork, or 2D illustration
upscayl -i sketch.png -o sketch_4x.png -n digital-art-4x

# 4. Upscale with human portrait / natural skin enhancement (Remacri)
upscayl -i portrait.jpg -o portrait_enhanced.png -n remacri-4x

# 5. Upscale to 2x resolution (downscaling 4x model inference cleanly)
upscayl -i avatar.png -o avatar_2x.png -s 2

# 6. Upscale and re-encode to high-efficiency WebP with 90% quality compression
upscayl -i hero.png -o hero_4x.webp -f webp -c 90

# 7. Maximum quality restoration using Test-Time Augmentation (TTA mode)
upscayl -i archival.jpg -o archival_restored.png -n high-fidelity-4x -x -v

# 8. Batch upscale an entire directory of video frames or storyboard panels
upscayl -i ./frames_input/ -o ./frames_upscaled/ -n upscayl-standard-4x

# 9. List all installed AI models and check model repository status
upscayl --list-models

# 10. Launch Upscayl Desktop Graphical Interface
upscayl --gui
# or via macOS open:
open -a Upscayl
```

#### Troubleshooting & Optimization
- **High VRAM / Out of Memory on Massive Images**: If upscaling images larger than 8K, pass an explicit tile size such as `-t 256` or `-t 512` to reduce GPU memory footprint during NCNN convolution.
- **macOS Gatekeeper Permissions**: If launching the desktop app reports an unverified developer warning, clear quarantine attributes:
  ```bash
  xattr -dr com.apple.quarantine /Applications/Upscayl.app
  ```
- **CLI Model Resolution**: The CLI wrapper automatically discovers models located at `/Applications/Upscayl.app/Contents/Resources/models` or falls back to `/Users/sharadkumar/opensource/upscayl/resources/models`. Custom models can be supplied anytime via the `-m <path_to_models>` flag.

---

### 17. F5-TTS (`f5-tts-webui`, `f5-tts-cli`)

#### How It Works
F5-TTS implements speech synthesis as a flow-matching in-filling task powered by a Diffusion Transformer (DiT) with ConvNeXt V2 blocks:
```
[Reference Audio (3–10s)] ──► Mel-Spectrogram (Vocos, 100 bands) ──┐
[Reference Text + Target Text] ──► Tokenization / Pinyin / Devanagari ──┼──► Conditional Flow Matching (DiT / ConvNeXt V2)
[Initial Gaussian Noise] ──────────────────────────────────────────┘        │ (Euler ODE with Sway Sampling, 16–32 NFE)
                                                                            ▼
                                                                [Predicted Target Mel-Spectrogram]
                                                                            │
                                                                            ▼
                                                                [Vocos Vocoder (24kHz PCM Audio)]
```
- **Acoustic In-filling**: The reference audio and target text sequence are concatenated into a joint continuous representation. The model reconstructs the target speech portion by learning the optimal vector field connecting Gaussian noise to speech mel-spectrograms.
- **Sway Sampling**: Employs non-linear time-step scheduling during inference to prioritize trajectory refinement in high-impact flow intervals, allowing high-quality voice cloning in just 16–32 function evaluations (NFE).
- **Apple Silicon Hardware Acceleration**: Configured with PyTorch `mps` (Metal Performance Shaders) backend and `PYTORCH_ENABLE_MPS_FALLBACK=1` for GPU-accelerated local synthesis.
- **Fork Specifics (`rumourscape/F5-TTS`)**: Integrates pretrained IIT Madras Hindi checkpoint (`SPRINGLab/F5-Hindi-24KHz`) and exposes explicit `--nfe` parameter control in both CLI and Gradio UI.

#### Key Capabilities
- **Zero-Shot Voice Cloning**: Clones any voice without fine-tuning using only 5–10 seconds of clean reference speech.
- **Audio-Conditioned Emotion & Prosody**: Inherits cadence, whisper, drama, or calm demeanor directly from the reference audio clip.
- **Hindi Storytelling & Dialogue**: Preloaded with high-fidelity Hindi 24kHz model trained on IndicTTS and IndicVoices datasets.
- **Multi-Speaker / Multi-Speech Mode**: Generate full multi-speaker conversational podcast/audiobook tracks by assigning different reference audios to script lines.
- **Configurable Speed & Denoising**: Independent speed scaling (`--speed 0.8` to `1.5`) and step controls (`--nfe 16` to `64`).

#### Common Commands
```bash
# 1. Launch Gradio Interactive Web UI (runs on http://127.0.0.1:7860)
f5-tts-webui

# Or run directly from repo:
cd /Users/sharadkumar/opensource/F5-TTS && ./start_webui.sh

# 2. CLI inference with custom reference audio
f5-tts-cli \
  --ref_audio "/path/to/sample.wav" \
  --ref_text "Exact words spoken in the reference audio sample." \
  --gen_text "यह एक नया वाक्य है जो उसी आवाज़ में उत्पन्न होगा।" \
  --output_dir "./outputs" \
  --output_file "output.wav" \
  --speed 1.0 \
  --nfe 32

# 3. Hindi synthesis with IIT Madras 24KHz Small model
f5-tts-cli \
  -m "F5-TTS-small" \
  -p "SPRINGLab/F5-Hindi-24KHz/model_2500000.safetensors" \
  -v "SPRINGLab/F5-Hindi-24KHz/vocab.txt" \
  -r "hindi_narrator_ref.wav" \
  -s "एक जंगल में एक शेर रहता था।" \
  -t "वह रोज़ सुबह नदी किनारे पानी पीने जाता था।" \
  -o "./outputs" -w "story_segment.wav"
```

#### Workspace Integration
- Installed at `/Users/sharadkumar/opensource/F5-TTS` with an isolated Python 3.12 virtual environment (`.venv`).
- Global CLI commands symlinked to `/Users/sharadkumar/.local/bin/f5-tts-webui` and `/Users/sharadkumar/.local/bin/f5-tts-cli`.
- Complements `whisper` for reference audio transcription, `Audacity-MCP` for post-production DSP leveling, and `kdenlive-mcp-server` for timeline placement.

---

### 18. OmniVoice (`omnivoice`, `omnivoice-demo`, `omnivoice-infer`, `omnivoice-infer-batch`)

#### How It Works
OmniVoice uses a diffusion language model (DLM) architecture for massively multilingual zero-shot speech synthesis across 600+ languages. Its internal pipeline operates as follows:
```
[Input Text / Attributes / Ref Audio]
    ↓ Text Tokenizer & Language Embedding
[Semantic Representation]
    ↓ Multi-Codebook Diffusion Language Model (Transformer + Continuous Flow)
[Acoustic Latents (8 Codebooks, 24 kHz)]
    ↓ Neural Audio Decoder
[Synthesized 24kHz Waveform (NumPy / SoundFile)]
```
- **Diffusion Language Model Architecture**: Combines autoregressive sequence conditioning with continuous diffusion for speech synthesis, achieving inference real-time factors (RTF) as fast as 0.025 (~40x faster than real-time).
- **Multi-Codebook Audio Representation**: Decodes speech into 8 acoustic codebooks at 24 kHz sample rate for zero-shot fidelity.
- **Reference Transcription Engine**: Directly couples with `openai/whisper-large-v3-turbo` for zero-friction reference audio auto-transcription during voice cloning.
- **Apple Silicon Acceleration**: Fully runs on Apple Silicon Metal via PyTorch MPS backend (`PYTORCH_ENABLE_MPS_FALLBACK=1`) with scaled dot-product attention (SDPA) kernel fallback.

#### Key Capabilities
- **600+ Languages**: Industry-leading multilingual zero-shot speech coverage across European, Asian, African, and indigenous language groups.
- **Zero-Shot Voice Cloning**: Clones speaker timbre, room acoustics, and cadence from 3–10 seconds of reference audio (`--ref_audio sample.wav`).
- **Prompt Caching**: Allows encoding reference audio once into a `.pt` prompt (`model.create_voice_clone_prompt()`) and reusing it instantly across subsequent inference runs without re-transcription.
- **Natural Language Voice Design**: Synthesizes voices purely from attribute descriptions (`--instruct "female, low pitch, british accent"` or `"whisper, elderly male"`).
- **Autonomous Auto Voice**: Generates diverse, natural voice signatures without requiring any reference audio or prompts.
- **Non-Verbal Tags & Pronunciation Rules**: Inline emotional and conversational tokens (`[laughter]`, `[sigh]`, `[confirmation-en]`, `[surprise-wa]`, etc.) and phoneme dictionary overrides (`[B EY1 S]`).
- **Distributed & Batch Inference**: High-throughput multi-speaker synthesis via JSONL batch lists (`omnivoice-infer-batch`).

#### Common Commands
```bash
# 1. Launch Gradio Web UI (runs on http://127.0.0.1:8001)
omnivoice-demo

# Or launch via master dispatcher:
omnivoice demo

# Or run directly from repo:
cd /Users/sharadkumar/opensource/OmniVoice && ./start_demo.sh

# 2. Zero-shot voice cloning from reference audio (Whisper auto-transcribes ref audio if ref_text is omitted)
omnivoice-infer \
  --model k2-fsa/OmniVoice \
  --text "Zero-shot multilingual speech synthesis on Apple Silicon." \
  --ref_audio "/path/to/reference.wav" \
  --output "output_cloned.wav"

# 3. Voice design using descriptive speaker attributes
omnivoice-infer \
  --model k2-fsa/OmniVoice \
  --text "Welcome to the story. Deep in the mountains lived an old sage." \
  --instruct "elderly male, low pitch, calm narration" \
  --output "story_intro.wav"

# 4. Auto-voice synthesis with non-verbal sound tags
omnivoice-infer \
  --model k2-fsa/OmniVoice \
  --text "[laughter] That was completely unexpected, but brilliant!" \
  --output "laughter_sample.wav"

# 5. Batch inference from a JSONL specification
omnivoice-infer-batch \
  --model k2-fsa/OmniVoice \
  --test_list batch_manifest.jsonl \
  --res_dir ./batch_results
```

#### Workspace Integration
- Installed at `/Users/sharadkumar/opensource/OmniVoice` with an isolated Python 3.12 virtual environment (`.venv`).
- Global CLI commands symlinked to `/Users/sharadkumar/.local/bin/omnivoice`, `/Users/sharadkumar/.local/bin/omnivoice-demo`, `/Users/sharadkumar/.local/bin/omnivoice-infer`, and `/Users/sharadkumar/.local/bin/omnivoice-infer-batch`.
- Integrates with `Audacity-MCP` for post-generation normalization/DSP, `kdenlive-mcp-server` for timeline assembly, and `whisper` for acoustic transcription validation.

---

### 19. BlackHole Audio Loopback Driver (`BlackHole`)

#### How It Works
BlackHole is a high-performance, modern macOS virtual audio driver developed as a native CoreAudio Hardware Abstraction Layer (HAL) plugin:
```
[Source Application (DAW / Browser / Voicebox)]
    ↓ Output Stream (PCM Audio Samples)
[CoreAudio Hardware Abstraction Layer (HAL)]
    ↓ Zero-Latency Ring Buffer
[BlackHole Virtual Audio Driver (BlackHoleXch.driver)]
    ↓ Mirrored Read Stream
[Receiving Application (Audacity / OBS / Whisper / Python)]
```
- **User-Space Kernel-Less Architecture**: Unlike legacy audio loopback tools (e.g., Soundflower) that relied on fragile kernel extensions (KEXTs), BlackHole executes entirely within user space inside Apple's CoreAudio daemon (`coreaudiod`). It requires no disabling of System Integrity Protection (SIP) and operates on Apple Silicon (ARM64) and Intel (x86_64).
- **Circular Ring Buffer**: Transfers audio frames directly from output write heads to input read heads using shared memory ring buffers with zero added algorithm latency (0 samples delay beyond hardware/buffer block size).
- **Driver Variants**:
  - `BlackHole 2ch`: Standard stereo (2-in / 2-out) for system audio recording, DAW loopback, screen recorders, and meeting bridge audio.
  - `BlackHole 16ch`: Multichannel routing for individual stem separation, multi-track podcast capture, and intermediate audio buses.
  - `BlackHole 64ch`: High-density routing for surround sound, ambisonics, and complex DAW mixing matrices.
- **Clock Synchronization & Sample Rates**: Operates from 8 kHz up to 768 kHz with support for Aggregate Devices and Multi-Output Devices in macOS `Audio MIDI Setup` with automatic drift correction.

#### Key Capabilities
- **Zero Additional Latency**: Passes uncompressed floating-point audio between applications with zero additional algorithmic delay.
- **System Audio Capture**: Allows capturing desktop, browser, video meeting, or game audio directly into DAWs (Audacity, Logic Pro, GarageBand) or Python processing pipelines.
- **Inter-App Audio Routing**: Streams real-time synthesized speech from local AI models (Voicebox, F5-TTS, OmniVoice) directly into live communication apps (Zoom, Google Meet, Discord, OBS).
- **Customizable Topologies**: Supports customizable channel counts (2, 16, 64, 128, 256), custom driver names, hidden mirrored devices, and buffer sizes via Xcode build preprocessor definitions.

#### Common Commands & Operational Procedures
```bash
# 1. Launch graphical installer (Touch ID / GUI prompt) for BlackHole 2ch
cd /Users/sharadkumar/opensource/BlackHole && ./install_driver.sh --gui -c 2

# 2. Command-line silent installation for 2ch, 16ch, or 64ch
sudo ./install_driver.sh -c 2
sudo ./install_driver.sh -c 16
sudo ./install_driver.sh -c 64

# 3. Verify installed HAL drivers
ls -l /Library/Audio/Plug-Ins/HAL/

# 4. Restart CoreAudio daemon to reload driver plugins
sudo killall -9 coreaudiod

# 5. List recognized system audio devices via system_profiler
system_profiler SPAudioDataType | grep -A 5 -B 2 "BlackHole"

# 6. Manual uninstallation
sudo rm -rf /Library/Audio/Plug-Ins/HAL/BlackHole*.driver
sudo killall -9 coreaudiod
```

#### Workspace Integration
- Source repository located at `/Users/sharadkumar/opensource/BlackHole`.
- Pre-packaged official macOS `.pkg` installers cached at `/Users/sharadkumar/opensource/BlackHole/BlackHole2ch-0.7.1.pkg`, `BlackHole16ch-0.7.1.pkg`, and `BlackHole64ch-0.7.1.pkg`.
- Automated helper script provided at `/Users/sharadkumar/opensource/BlackHole/install_driver.sh`.
- Integrates with `Audacity-MCP` and local speech engines (`Voicebox`, `F5-TTS`, `OmniVoice`) to capture and loop back system audio streams into editing workflows.

---

### 20. Maya 2 Native TTS (`MayaTTS` / `mlx-audio`)

#### How It Works
Maya 2 Native is an advanced neural speech generation system created by Maya Research, converted to native Apple Silicon MLX format (`BF16`) for zero-overhead GPU acceleration on Apple M-series chips via the Metal framework:
```
[Input Text (Devanagari Hindi / English / 10 Indic Langs)]
    ↓ Built-in Text Normalizer (Rule-based expansion of numbers, dates, currency, OTP, percentages)
[Normalized Token Stream + Conditioning (20 Named Personas or ECAPA Reference Embedding)]
    ↓ Autoregressive Backbone: Qwen3-1.7B-Base (28 Layers, 16 Attention Heads, MLX BF16)
[Acoustic Latent Tokens (32 Codebooks @ 12.5 Hz Frame Rate)]
    ↓ Depth Transformer (4 Layers, 16 Heads) + Kyutai Mimi Neural Audio Codec Decoder
[Output Audio Waveform: 24,000 Hz, 16-bit Mono PCM]
```
- **Native MLX Metal Engine**: Unlike Docker or PyTorch emulation layers that incur virtualization bottlenecks, Maya 2 runs directly on Apple Silicon unified memory using Apple's MLX C++ and Metal compute kernels. On Apple M4, model loading takes ~0.97s, and total RAM occupancy is ~5.2–5.6 GB (leaving >26 GB free unified memory).
- **Sub-Second Real-Time Factor (RTF)**: Benchmarked on Apple M4 at **0.68x–0.73x RTF** (faster than real time), generating a 5-second sentence in ~3.5 seconds and a 23-second story in ~15.3 seconds.
- **20 Built-in Named Personas**: Includes 20 native character voices covering diverse genders, age bands, and styles (e.g., `Malini` mature narrator, `Siddhant` professional adult male, `Ahana` youthful female, `Ritvik` conversational Hindi male, `Vaidehi` gentle calm female).
- **Cross-Lingual Zero-Shot Voice Cloning**: Embeds reference audio (3–10 seconds clean sample) via SpeechBrain ECAPA-TDNN (20M MLX export) to clone the speaker's vocal timbre into another language (e.g., English speech reference seamlessly driving Hindi storytelling).
- **Rule-Based Normalization**: Native expansion for Indian numbering systems (lakhs, crores), dates (day/month/year), INR currency symbols (`₹`), percentages, and phone/OTP digit sequences.

#### Key Capabilities
- **24 kHz Studio Speech**: Synthesizes uncompressed, broadcast-ready 24,000 Hz 16-bit mono PCM audio.
- **12 Supported Languages**: Hindi (`hi`), English (`en`), Bengali (`bn`), Tamil (`ta`), Telugu (`te`), Marathi (`mr`), Gujarati (`gu`), Kannada (`kn`), Malayalam (`ml`), Punjabi (`pa`), Odia (`or`), Assamese (`as`).
- **Streaming Generation**: Supports chunked generator streaming (`stream=True`, `streaming_interval=0.32s`) for conversational or live-playback pipelines.
- **Narrative Story Pacing**: Sustains acoustic consistency across multi-sentence story paragraphs without drift, hallucination, or vocal collapse.

#### Common Commands & Operational Procedures
```bash
# 1. Quick CLI synthesis via wrapper script
cd /Users/sharadkumar/opensource/MayaTTS
./maya_tts.sh --text "नमस्कार दोस्तों! आज की कहानी बहुत ही रोमांचक है।" --voice Malini --out story.wav

# 2. Hindi synthesis with male professional voice
./maya_tts.sh --text "आपका स्वागत है हमारे चैनल पर।" --voice Siddhant --lang hi --out intro.wav

# 3. Cross-lingual voice cloning (English reference -> Hindi narration)
./maya_tts.sh --text "प्रकृति हमेशा जीवित रहती है।" \
  --ref-audio "/Users/sharadkumar/opensource/F5-TTS/src/f5_tts/infer/examples/basic/basic_ref_en.wav" \
  --ref-text "Some call me nature, others call me mother nature." \
  --ref-lang en --lang hi --out clone_hindi.wav

# 4. Run the comprehensive evaluation benchmark suite
/Users/sharadkumar/opensource/MayaTTS/.venv/bin/python /Users/sharadkumar/opensource/MayaTTS/evaluate_maya.py

# 5. Launch the Interactive Gradio Voice Studio & Story Lab
cd /Users/sharadkumar/opensource/MayaTTS && ./start_studio.sh
# Access the web UI at: http://127.0.0.1:7862

# 6. Native mlx-audio CLI command
/Users/sharadkumar/opensource/MayaTTS/.venv/bin/mlx_audio.tts.generate \
  --model /Users/sharadkumar/opensource/MayaTTS/models/maya2 \
  --text "नमस्ते दुनिया!" --voice Ritvik --lang_code hi
```

#### Workspace Integration
- **Directory**: `/Users/sharadkumar/opensource/MayaTTS`
- **Environment**: Dedicated Python 3.11 virtual environment at `/Users/sharadkumar/opensource/MayaTTS/.venv`
- **Model Storage**: 4.7 GB BF16 model weights at `/Users/sharadkumar/opensource/MayaTTS/models/maya2`
- **Evaluation Audio Samples**: Cached at `/Users/sharadkumar/opensource/MayaTTS/eval_samples/`
- **Interactive Web Studio**: Gradio 6.31 web app at `/Users/sharadkumar/opensource/MayaTTS/app.py` (`./start_studio.sh`) on port `7862`
- **Persistent Voice Library**: Storage at `/Users/sharadkumar/opensource/MayaTTS/voice_profiles/voices.json` with reference audio repository in `voice_profiles/audio/` (pre-loaded with Nandani & Kapil Uncle)
- **CLI Utility**: `/Users/sharadkumar/opensource/MayaTTS/maya_tts.sh` and `synthesize.py`
- **Skill Synergies**: Feeds narrative voice tracks into `story-editor` and `storyBackgroundmusic` skills for Katha Sansar and Kapil Uncle storytelling videos.

---

### 21. IndicF5 (`infer.py`, `f5_tts`)

#### How It Works
IndicF5 is a near-human polyglot Text-to-Speech (TTS) and zero-shot voice cloning model developed by AI4Bharat (IIT Madras), trained on 1,417 hours of high-quality Indian speech data from Rasa, IndicTTS, LIMMITS, and IndicVoices-R:
```
[Reference Audio Prompt (.wav)] ──> [TorchCodec Decoder] ──> [Vocos Mel-Spectrogram Extraction]
                                                                        │
[Reference Prompt Text + Target Text] ──> [Token Vocabulary Lookup]     │
                                                        │               │
                                                        ▼               ▼
                                           [Diffusion Transformer (DiT)]
                                           - 22 Layers, 16 Attention Heads
                                           - 1024 Hidden Dim, 512 Text Dim
                                           - 4 ConvNeXt V2 Layers
                                                        │
                                                        ▼
                                           [Flow-Matching ODE Solver (Euler)]
                                                        │
                                                        ▼
                                           [Vocos Neural Vocoder (24 kHz)]
                                                        │
                                                        ▼
                                      [Synthesized Speech: 24,000 Hz 16-bit Mono PCM]
```
- **Diffusion Transformer (DiT) & Flow Matching**: Employs continuous normalizing flow (CNF) matching over speech mel-spectrogram latents, in-filling prospective frames conditioned on the reference acoustic prompt and text sequence.
- **Polyglot Indian Language Coverage**: Pre-trained on 11 major Indian languages: Hindi (`hi`), Bengali (`bn`), Tamil (`ta`), Telugu (`te`), Marathi (`mr`), Gujarati (`gu`), Kannada (`kn`), Malayalam (`ml`), Punjabi (`pa`), Odia (`or`), and Assamese (`as`).
- **Zero-Shot Voice Cloning**: Accurately mimics speaker prosody, emotional tone, and vocal characteristics across languages from 3–10 seconds of reference speech.

#### Key Capabilities
- **Broadcast-Grade Audio**: 24,000 Hz, 16-bit signed integer mono PCM output.
- **Cross-Lingual Synthesis**: Generates speech in Hindi or other Indic languages while adopting speaker timbre from Punjabi, Marathi, Tamil, or Kannada reference prompts.
- **Integrated Silence Trimming & Loudness Normalization**: Automated split-on-silence trimming and target -20.0 dBFS normalization.

#### Common Commands & Operational Procedures
```bash
# 1. Quick CLI inference using infer.py wrapper
cd /Users/sharadkumar/opensource/IndicF5
.venv/bin/python infer.py \
  --text "नमस्ते! संगीत की तरह जीवन भी खूबसूरत होता है, बस इसे सही ताल में जीना आना चाहिए।" \
  --ref-audio "prompts/PAN_F_HAPPY_00001.wav" \
  --ref-text "ਭਹੰਪੀ ਵਿੱਚ ਸਮਾਰਕਾਂ ਦੇ ਭਵਨ ਨਿਰਮਾਣ ਕਲਾ ਦੇ ਵੇਰਵੇ ਗੁੰਝਲਦਾਰ ਅਤੇ ਹੈਰਾਨ ਕਰਨ ਵਾਲੇ ਹਨ, ਜੋ ਮੈਨੂੰ ਖੁਸ਼ ਕਰਦੇ  ਹਨ।" \
  --output "samples/hindi_sample.wav"

# 2. Python API synthesis via Hugging Face Transformers
from transformers import AutoModel
import numpy as np
import soundfile as sf

repo_id = "rsolanki1822/IndicF5-mirror"  # or "ai4bharat/IndicF5" with HF token
model = AutoModel.from_pretrained(repo_id, trust_remote_code=True)

audio = model(
    "प्रकृति हमेशा जीवित रहती है और हमें जीना सिखाती है।",
    ref_audio_path="prompts/PAN_F_HAPPY_00001.wav",
    ref_text="ਭਹੰਪੀ ਵਿੱਚ ਸਮਾਰਕਾਂ ਦੇ ਭਵਨ ਨਿਰਮਾਣ ਕਲਾ ਦੇ ਵੇਰਵੇ ਗੁੰਝਲਦਾਰ ਅਤੇ ਹੈਰਾਨ ਕਰਨ ਵਾਲੇ ਹਨ, ਜੋ ਮੈਨੂੰ ਖੁਸ਼ ਕਰਦੇ  ਹਨ।"
)

if audio.dtype == np.int16:
    audio = audio.astype(np.float32) / 32768.0
sf.write("samples/output.wav", np.array(audio, dtype=np.float32), samplerate=24000)
```

#### Workspace Integration
- **Directory**: `/Users/sharadkumar/opensource/IndicF5`
- **Environment**: Dedicated Python 3.10 virtual environment at `/Users/sharadkumar/opensource/IndicF5/.venv` (built via `uv`)
- **Model Checkpoints**: Safetensors checkpoint (350M parameters, 1.40 GB) and Vocos vocoder cached locally in `~/.cache/huggingface/hub/`
- **Reference Prompts**: Pre-bundled reference voices for Kannada, Marathi, Punjabi, and Tamil in `/Users/sharadkumar/opensource/IndicF5/prompts/`
- **Output Samples**: Synthesized verification audio stored in `/Users/sharadkumar/opensource/IndicF5/samples/`
- **CLI Utility**: Executable CLI runner at `/Users/sharadkumar/opensource/IndicF5/infer.py`

### 22. Vocalis - AI Script & Voice TTS Studio (`Vocalis` / `AI-Studio-App`)

#### How It Works
Vocalis is a studio-grade neural text-to-speech, script assistant, and voice cloning web application engineered for Google AI Studio and local operation. Its architecture consists of:
```
[User Browser / React 19 Frontend]
        ↓ HTTP REST API & JSON Payloads
[Express Server (server.ts / tsx)]
        ↓ Server-side Gemini SDK (@google/genai)
[Google Gemini Multimodal API (gemini-2.5-flash / gemini-2.5-pro)]
        ↓ Audio PCM / Text Streams
[Audio Pipeline (concatWavBuffers 24kHz 16-bit Mono PCM)]
        ↓ Audio Playback & Persistent JSON Store (data/clones.json, data/character-voices.json)
[Client Player / Export]
```
1. **Server-Side AI Dispatch**: Routes prompt analysis, script pacing, voice cloning definitions, and multi-speaker TTS to Gemini using automatic fallback cascade (`gemini-2.5-flash`, `gemini-2.5-pro`, `gemini-2.0-flash`) if transient rate limits (429/503) occur.
2. **Lossless Audio Concatenation**: Assembles multi-segment dialogue chunks directly from 24kHz 16-bit mono PCM buffers into unified RIFF WAV headers.
3. **Vite SPA Middleware**: In development mode, Express attaches Vite directly via `createServer({ server: { middlewareMode: true }, appType: 'spa' })` to deliver instant hot-reloading React 19 UI without separate proxy processes.

#### Key Capabilities
- **Multi-Speaker Dialogue Generation**: Synthesize multi-character conversations with distinct voice styles, moods, and emotional pacing.
- **Voice Analysis & Style Cloning**: Analyze reference audio or style descriptions to create reusable cloned voice profiles.
- **Script Assistant**: Polish dialogue, adjust cadence, format narration lines, and generate speaker tags.
- **Persistent Local Library**: Saves cloned voices and character presets to `data/clones.json` and `data/character-voices.json`.
- **Broadcast Master Output**: Concatenates chunks into seamless 24 kHz 16-bit uncompressed WAV streams.

#### Common Commands & Operational Procedures
```bash
# 1. Start development server (Express backend + Vite HMR)
cd /Users/sharadkumar/opensource/Vocalis/AI-Studio-App-main
npm run dev

# 2. Build production assets
npm run build

# 3. Test API health
curl -s http://localhost:3000/api/health

# 4. Inspect saved character voices and clones
curl -s http://localhost:3000/api/character-voices
curl -s http://localhost:3000/api/clones
```

#### Workspace Integration
- **Directory**: `/Users/sharadkumar/opensource/Vocalis/AI-Studio-App-main` (Symlinked at `/Users/sharadkumar/opensource/AI-Studio-App`)
- **Environment**: Node.js v26.12.1 + npm 11.20.0, `.env` configured with `GEMINI_API_KEY` and `PORT=3000`
- **Storage**: Persistent JSON databases at `data/clones.json` and `data/character-voices.json`
- **Access URL**: `http://localhost:3000`

---

### 23. Flow MCP (`flow-mcp`, `Flow Studio`)
- **Version**: `0.1.0` (Updated: Added Dual-Slot Character Architecture `body_image` support & Multi-Profile Switcher)
- **Directory**: `/Users/sharadkumar/opensource/flow-mcp`
- **Capabilities**: Dual-slot character builder (`image` for Portrait facial bust + `body_image` for standing turnaround under `Create body`), multi-account Chrome profile switcher (`npm run profile [browsefuture|sharad]`, `flow_profiles`, `flow_switch_profile`), batch scene generation, asset management, and studio interface.

#### How It Works
Flow MCP connects AI assistants (Claude, Codex, Antigravity) or its standalone Web UI directly to Google Flow (`flow.google.com`) using Chrome DevTools Protocol (CDP) and Playwright:
```
[Antigravity / Codex / Claude]
          │ (Stdio JSON-RPC MCP)
          ▼
   [flow-mcp server]
          │ (Chrome DevTools Protocol - CDP :9333)
          ▼
   [Dedicated Chrome Profile] (~/.flow-mcp/chrome-profile)
          │ (Simulates user interactions, button clicks, quotes)
          ▼
   [Google Flow Web App] (flow.google.com)
          │
    ┌─────┴──────────────────┬─────────────────────┐
    ▼                        ▼                     ▼
[Character Generator]  [Keyframe Stills]   [Video Shot Generations]
    │                        │                     │
    └────────────────────────┼─────────────────────┘
                             ▼
     [Kokoro TTS / Gemini Voice / FFmpeg Assembler]
                             ▼
              [Output Films: ~/flow-mcp-out/]
```
1. **Dedicated Chrome Session**: Launches Google Chrome with a dedicated `--user-data-dir=~/.flow-mcp/chrome-profile` and `--remote-debugging-port=9333`. The user signs in once manually via `npm run login`. Session cookies and authentication are safely persisted locally without handling passwords.
2. **Real-time Flow Automation**: Connects over CDP using Playwright Core to interact with Flow's native UI elements (project selection, character builder, keyframe prompts, and video renders), consuming Flow's daily free credits (50/day) rather than paid API tokens.
3. **Audio & Video Post-Processing**: Includes local neural narration generation via Kokoro TTS (28 offline voices) or Google AI Studio voices, plus FFmpeg concatenation, music mixing, and optional whisper.cpp subtitles.
4. **Standalone Web Studio**: Serves an integrated local dashboard (`Flow Studio`) on `http://127.0.0.1:8787` for managing Cast, Frames, Shots, Voice narration, Restyling, and Video Cutting without an AI assistant.

#### Key Capabilities
- **Character Consistency (Cast)**: Create, persist, and reference named characters with portraits across shots.
- **Match Previous Frame (Frames)**: Generate sequential keyframe stills with automatic visual style matching.
- **Credit-Controlled Shots**: Quote check before video generation with hard credit caps to prevent unwanted credit drain.
- **Integrated Voice Narration**: Local zero-cost speech synthesis using Kokoro-JS and cloud Gemini voices.
- **Automatic Assembly & Cutting**: Join shots, overlay narration, add background music bed with ducking, and burn subtitles.

#### Common Commands & Operational Procedures
```bash
# 1. Initial Google sign-in (opens dedicated Chrome profile)
cd /Users/sharadkumar/opensource/flow-mcp
npm run login

# 2. Launch Flow Studio Web UI (http://127.0.0.1:8787)
cd /Users/sharadkumar/opensource/flow-mcp
npm run studio
# Or double-click "Flow Studio.command"

# 3. Build TypeScript source
cd /Users/sharadkumar/opensource/flow-mcp
npm run build

# 4. Start MCP server directly (Stdio)
/opt/homebrew/bin/node /Users/sharadkumar/opensource/flow-mcp/dist/index.js
```

#### Workspace Integration
- **Directory**: `/Users/sharadkumar/opensource/flow-mcp`
- **Environment**: Node.js v26.12.1 + npm 11.20.0, TypeScript 7.0.2
- **Chrome Profile**: `~/.flow-mcp/chrome-profile` (CDP port: `9333`)
- **Render Output**: `~/flow-mcp-out/<project>/`
- **MCP Configurations**:
  - Antigravity: `~/.gemini/config/mcp_config.json` (`flow` server)
  - Codex: `~/.codex/config.toml` (`[mcp_servers.flow]`)

---

### 24. SpliceKit (`SpliceKit`, `splicekit-mcp`, `Final Cut Pro.app`)

#### How It Works
SpliceKit injects an Objective-C dynamic library directly into Final Cut Pro's runtime via Mach-O `LC_LOAD_DYLIB` in a sandbox-exempt copy of Final Cut Pro located at `~/Applications/SpliceKit/Final Cut Pro.app`:
```
[Antigravity / Claude / Codex]
          │ (Stdio FastMCP)
          ▼
   [mcp/server.py] (~/.venvs/splicekit-mcp)
          │ (TCP JSON-RPC :9876)
          ▼
   [SpliceKit Framework / Dylib] (Injected into FCP process)
          │ (Direct objc_msgSend / Responder Chain / FFUndoManager)
          ▼
   [Final Cut Pro Runtime] (78,000+ internal ObjC classes)
          │
    ┌─────┴──────────────────┬─────────────────────┐
    ▼                        ▼                     ▼
[Timeline Operations]   [Audio Bus Mixer]     [Command Palette (Cmd+Shift+P)]
(Blade, Select, Retime)  (Role-based EQ/Comp)   (Apple Intelligence On-Device)
```
1. **Dynamic Injection & Mach-O Patching**: Clones the native `/Applications/Final Cut Pro.app` to `~/Applications/SpliceKit/Final Cut Pro.app`, patches the Mach-O binary using `insert_dylib` with `@rpath/SpliceKit.framework/Versions/A/SpliceKit`, and re-signs it with entitlements (`com.apple.security.app-sandbox: false`, `disable-library-validation: true`).
2. **In-Process JSON-RPC Server**: Starts an embedded server on `127.0.0.1:9876` listening for JSON-RPC 2.0 requests. Rather than relying on UI automation or AppleScript, SpliceKit executes direct ObjC calls (`FFAnchoredSequence`, `FFAnchoredTimelineModule`, `FFUndoManager`, etc.) directly on the main thread via `objc_msgSend`.
3. **Model Context Protocol (MCP) Server**: Exposes ~200 FastMCP tools over Stdio via `mcp/server.py`, allowing AI pair programmers to inspect timeline contents, cut/blade clips, detect silences, apply effects, manage audio roles, and export.
4. **Command Palette & UI Overlays**: Injects a custom floating spotlight HUD (`Cmd+Shift+P`) with local speech recognition, an on-timeline sections visualizer, and a role-based audio mixer panel.

#### Key Capabilities
- **Direct ObjC Runtime Control**: Programmatically inspects, selects, navigates, and modifies timeline clips, sequences, and libraries without GUI simulation.
- **MCP Server for AI Pair-Editing**: 200+ specialized editing tools for LLMs (blade, trim, retime, markers, color board, transitions, export).
- **Command Palette (`Cmd+Shift+P`)**: Instant fuzzy-search and natural language execution powered by on-device Apple Intelligence.
- **Audio Bus Mixing by Role**: Route audio processing (compressor, EQ, reverb) by role (Dialogue, Effects, Music) instead of clip-by-clip.
- **Silence & Beat Detection**: Native AVFoundation silence detection and song cut workflow.
- **Format Readers & Codecs**: Native MediaExtension support for Blackmagic RAW (BRAW) and VP9/WebM import without external transcoding.

#### Common Commands & Operational Procedures
```bash
# 1. Setup Python MCP virtual environment
cd /Users/sharadkumar/opensource/SpliceKit
make mcp-setup

# 2. Verify MCP configuration and bridge status
make mcp-doctor

# 3. Compile SpliceKit dylib
make -j8

# 4. Patch & install modded FCP to ~/Applications/SpliceKit
bash patcher/patch_fcp.sh

# 5. Launch modded Final Cut Pro
open "$HOME/Applications/SpliceKit/Final Cut Pro.app"
# Or run binary directly in terminal to monitor stdout/stderr:
"$HOME/Applications/SpliceKit/Final Cut Pro.app/Contents/MacOS/Final Cut Pro"

# 6. Test JSON-RPC bridge connection (when FCP is running)
echo '{"jsonrpc":"2.0","method":"system.version","id":1}' | nc 127.0.0.1 9876

# 7. Start MCP server directly via CLI
~/.venvs/splicekit-mcp/bin/python /Users/sharadkumar/opensource/SpliceKit/mcp/server.py
```

#### Workspace Integration
- **Directory**: `/Users/sharadkumar/opensource/SpliceKit`
- **Installed App**: `~/Applications/SpliceKit/Final Cut Pro.app`
- **Environment**: Python 3.14 (venv at `~/.venvs/splicekit-mcp`), Clang Apple Swift 6.4
- **Bridge Port**: `127.0.0.1:9876` (TCP JSON-RPC)
- **MCP Configurations**:
  - Antigravity: `~/.gemini/config/mcp_config.json` (`splicekit` server)
  - Codex: `~/.codex/config.toml` (`[mcp_servers.splicekit]`)
  - Repo root: `/Users/sharadkumar/opensource/SpliceKit/.mcp.json`

---

### 25. Go Programming Language & Toolchain (`go`, `gofmt`)

#### How It Works
Go is an open-source, statically typed, compiled programming language developed by Google. It compiles directly into native machine code (Mach-O ARM64 on Apple Silicon) without requiring an external runtime VM. Go includes a built-in concurrent runtime featuring lightweight user-space threads (goroutines), channel-based communication (CSP model), and an efficient concurrent mark-sweep garbage collector.

```
[Go Source (.go)]
    ↓ Lexing & Parsing (AST)
[Intermediate Representation (SSA)]
    ↓ Optimization & Machine Codegen
[Native Mach-O Binary (ARM64)]
```

#### Key Capabilities
- **Fast Single-Binary Compilation**: Compiles complex programs into self-contained statically linked or dynamic Mach-O binaries.
- **Cross-Compilation**: Easily targets other architectures and operating systems via `GOOS` and `GOARCH` flags.
- **Built-in Tooling**: Dependency management via `go mod`, code formatting via `gofmt`, testing via `go test`.
- **High Concurrency**: Goroutines and channels enable high-throughput server and MCP integrations.

#### Common Commands & Operational Procedures
```bash
# Check installed version and environment
go version
go env

# Download dependencies and tidy module
go mod tidy
go mod download

# Compile for native Apple Silicon (darwin-arm64)
go build -ldflags "-s -w" -o mybinary .

# Cross-compile for Linux x86_64
GOOS=linux GOARCH=amd64 go build -o mybinary-linux-amd64 .
```

#### Workspace Integration
- **Binary**: `/opt/homebrew/bin/go` (v1.27.3)
- **Primary Tooling**: `go`, `gofmt`, `godoc`
- **Used by**: `youtube-uploader-mcp`, local CLI harnesses.

---

### 26. YouTube Uploader MCP (`youtube-uploader-mcp`)

#### How It Works
`youtube-uploader-mcp` is an open-source Model Context Protocol (MCP) server written in Go that provides programmatic control over YouTube video uploads, metadata editing, thumbnail updates, and OAuth2 credential management. It communicates with clients (Antigravity, Cursor, Claude) over Stdio using JSON-RPC 2.0 via `mcp-go`.

```
[MCP Client (Antigravity / Cursor)]
    │  Stdio (JSON-RPC 2.0)
    ▼
[youtube-uploader-mcp Binary]
    │  OAuth 2.0 Token Exchange / Refresh
    ▼
[Google OAuth2 / YouTube Data API v3]
    ├── Upload Video Chunked Media Stream
    ├── Set Metadata (Title, Description, Tags, Category, Kids status)
    ├── Update Captions / Subtitles (`youtube.force-ssl`)
    └── Set Custom Thumbnails (< 2MB)
```

1. **OAuth2 Workflow**: Generates OAuth2 consent URLs using Google Client Secret JSON, captures authorization codes, and persists refresh tokens locally in `.youtube_uploader_channels_cache`.
2. **Chunked Resumable Uploads**: Uploads media files directly to YouTube with configurable privacy (`public`, `unlisted`, `private`) and scheduled publish time (`publish_at`).
3. **Decoupled Video Post-Processing (`update_video`)**: Attaches subtitle tracks (`.srt`, `.vtt`), updates video descriptions/titles, sets custom thumbnails, flags synthetic/AI media disclosure, and assigns videos to playlists.

#### Key Capabilities
- **OAuth2 Token Lifecycle**: Multi-channel authentication, local token persistence, and automatic token refresh.
- **Direct Video Upload**: Fast chunked video uploading with privacy states and scheduled publication timestamps.
- **Post-Upload Control**: Custom thumbnail attachment, subtitle upload via `youtube.force-ssl`, playlist assignment, and AI-generated content disclosure (`contains_synthetic_media`).
- **Channel & Video Catalog**: List uploaded channel videos with filtering by status and search queries.

#### Common Commands & Operational Procedures
```bash
# Verify version
youtube-uploader-mcp -version

# Run server manually over stdio
youtube-uploader-mcp \
  -client_secret_file /Users/sharadkumar/opensource/youtube-uploader-mcp/client_secret.json \
  -working_dir /Users/sharadkumar/opensource/youtube-uploader-mcp

# Build from source
cd /Users/sharadkumar/opensource/youtube-uploader-mcp
go build -ldflags "-s -w -X github.com/anwerj/youtube-uploader-mcp/yum.Version=0.1.3" -o youtube-uploader-mcp-darwin-arm64 .
```

#### Workspace Integration
- **Source Repository**: `/Users/sharadkumar/opensource/youtube-uploader-mcp`
- **Native Binary**: `/Users/sharadkumar/opensource/youtube-uploader-mcp/youtube-uploader-mcp-darwin-arm64` (symlinked to `/Users/sharadkumar/.local/bin/youtube-uploader-mcp`)
- **Client Secret**: `/Users/sharadkumar/opensource/youtube-uploader-mcp/client_secret.json`
- **Antigravity MCP Configuration**: Configured under `"youtube_uploader"` in `/Users/sharadkumar/.gemini/config/mcp_config.json`
- **Tool Schemas**: Stored in `/Users/sharadkumar/.gemini/antigravity/mcp/youtube_uploader/`

---

### 27. Demucs - Deep Music Source Separation (`demucs`)

#### How It Works
Demucs is a state-of-the-art deep learning music source separation engine developed by Meta AI Research. It uses a Hybrid Transformer architecture (`htdemucs`) operating simultaneously in both the time domain (waveform Conv-TasNet / U-Net) and frequency domain (spectrogram cross-attention Transformer):
```
[Mixed Audio Input (Stereo WAV/MP3)]
                ↓
    [Hybrid Spectrogram / Waveform Encoder]
                ↓
    [Cross-Domain Transformer Backbone]
                ↓
    [Multi-Stem Decoder Masks]
   ┌────────────┬────────────┬────────────┐
   ↓            ↓            ↓            ↓
[Drums]      [Bass]       [Other]     [Vocals]
   └────────────┴────────────┘            │
                ↓                         ↓
         [no_vocals.wav]            [vocals.wav]
   (Clean Instrumental Bed)      (Isolated Speech/Watermark)
```
- **Equivariant Stabilization (`--shifts`)**: Introduces random temporal shifts during inference to eliminate phase artifacts and spectral smearing.
- **Two-Stem Separation (`--two-stems vocals`)**: Optimizes inference speed and memory by directly producing `{track}/vocals.wav` and `{track}/no_vocals.wav` without decoding unnecessary stems.
- **High-Fidelity Watermark Extraction**: Accurately detects and strips spoken vocal watermarks, spoken intros, and narration while preserving 100% of underlying musical dynamics, bass, and percussion.

#### Key Capabilities
- **Neural Vocal Extraction & Stripping**: Completely separates spoken voices, dialogues, and vocal audio watermarks from background music tracks.
- **4-Stem Decomposition**: Separates mixed music into `drums`, `bass`, `other`, and `vocals`.
- **Apple Silicon Execution**: High-throughput CPU/MPS acceleration via PyTorch, separating full 3-minute stereo tracks in ~6 seconds on Apple Silicon.
- **Direct Ephemeral Runner**: Invoked seamlessly via `uvx --with numpy --from demucs demucs` without contaminating global Python environments.

#### Common Commands & Operational Procedures
```bash
# 1. Strip vocals and watermarks into clean instrumental (no_vocals.wav)
uvx --with numpy --from demucs demucs --two-stems vocals -o /tmp/demucs_out input_song.mp3

# 2. Extract full 4 stems (drums, bass, other, vocals)
uvx --with numpy --from demucs demucs -o /tmp/stems_out input_song.wav

# 3. Use 2 random shifts for higher separation quality
uvx --with numpy --from demucs demucs --shifts 2 --two-stems vocals input_song.mp3
```

#### Workspace Integration
- **Execution Vector**: `uvx --with numpy --from demucs demucs`
- **Installed Version**: `4.1.0` (Hybrid Transformer `htdemucs`)
- **Primary Use Case**: Removing speech watermarks and voice prompts from stock background music tracks in storytelling pipelines (`storyBackgroundmusic` skill).

---

### 28. MOSS-SoundEffect v2.0 (`run_mac_infer.sh`, `infer_from_pipeline.py`, `run_mac_webui.sh`)

#### How It Works
MOSS-SoundEffect v2.0 is a 1B-parameter text-to-audio diffusion foundation model trained by the OpenMOSS Team using the Flow Matching objective. It abandons the discrete acoustic token autoregression used in MOSS v1 in favor of a continuous Diffusion Transformer (DiT) backbone paired with a frozen Qwen3 text encoder and a Descript Audio Codec (DAC) VAE:
```
[Text Prompt (Scene Foley / Action Description)]
                     ↓
        [Frozen Qwen3 Text Encoder]
                     ↓
    [Flow-Matching DiT Backbone (1B Params)]
    (Continuous Vector Field Velocity Prediction)
                     ↓
      [Descript Audio Codec (DAC VAE Decoder)]
                     ↓
[High-Fidelity 48 kHz Stereo Foley WAV (up to 30s)]
```
- **Diffusion Transformer (DiT) & Flow Matching**: Rather than predicting discrete acoustic tokens sequentially, the model iteratively denoises continuous latent representations across 50–100 flow-matching steps.
- **DAC VAE Latent Compression**: Employs Descript Audio Codec operating at 48 kHz stereo with a 128-dimensional latent space, preserving crisp high-frequency transients (metal impacts, cloth rustles, footsteps, environmental ambience).
- **Apple Silicon Optimization**: Runs natively on Apple Silicon (M4 / MPS) with PyTorch 2.9 under `TORCHDYNAMO_DISABLE=1` and `bfloat16` precision. Patched `precompute_freqs_cis` to emit `complex64` (rather than unsupported `complex128`) and `sinusoidal_embedding_1d` to safely compute on float64 CPU/float32 MPS, enabling full hardware GPU acceleration at ~1.4s/step without CPU fallback.

#### Key Capabilities
- **48 kHz High-Fidelity Stereo Foley**: Generates studio-grade stereo sound effects up to 30 seconds long with clean spatial separation and high dynamic range.
- **Natural Environmental Ambiance & Foley**: Specialized in physical sound effects (door creaks, footsteps, mechanical clatter, wind, rain, magic whooshes, atmospheric drone beds).
- **32GB Unified Memory Footprint**: Requires only ~11.2GB memory, allowing concurrent execution alongside Kdenlive, Audacity, or Vocalis with >20GB RAM headroom on Mac mini M4.
- **Interactive Web UI & Batch CLI**: Ships both a Gradio web studio interface (`run_mac_webui.sh` on port `7865`) and scripted CLI pipeline runner (`run_mac_infer.sh`).

#### Common Commands & Operational Procedures
```bash
# 1. Quick CLI sound effect generation on Apple Silicon (MPS)
cd /Users/sharadkumar/opensource/MOSS-TTS/moss_soundeffect_v2
./run_mac_infer.sh "Heavy wooden door creaking open slowly in a stone dungeon"

# 2. Custom duration (e.g., 8s) and specific output path
SECONDS_=8.0 OUTPUT="/Users/sharadkumar/YouTube/Nandani/sfx_door.wav" \
./run_mac_infer.sh "Rain pouring on a tin roof with distant rolling thunder"

# 3. Direct Python pipeline inference with fine-grained control
source .venv/bin/activate
TORCHDYNAMO_DISABLE=1 python infer_from_pipeline.py \
  --model_dir OpenMOSS-Team/MOSS-SoundEffect-v2.0 \
  --prompt "Sword blade unsheathing with a metallic ringing whoosh" \
  --seconds 4.0 \
  --steps 50 \
  --cfg_scale 4.5 \
  --device mps \
  --torch_dtype bfloat16 \
  --output output/sword_whoosh.wav

# 4. Launch Gradio Web UI Studio
./run_mac_webui.sh
```

#### Workspace Integration
- **Repository Location**: `/Users/sharadkumar/opensource/MOSS-TTS`
- **Subproject Directory**: `/Users/sharadkumar/opensource/MOSS-TTS/moss_soundeffect_v2`
- **Dedicated Environment**: Dedicated Python 3.12 venv at `moss_soundeffect_v2/.venv`
- **Primary Use Case**: Generating Foley and cinematic sound effects for narrative storytelling (`backgroundMusicandSFX` skill, `Katha Sansar By Nandini`, `Kapil Uncle Ki Kahaniyan`).

---

### 23. AutoFlowCut (`AutoFlowCut.app`, `run.sh`, `autoflowcut-mcp`)

#### How It Works
AutoFlowCut operates as an automated desktop production bridge that links AI visual generation (Google GenAI / Gemini / Veo 3.1) with non-linear video editors (CapCut, Premiere Pro `.prproj`, and Vrew `.vrew`).

```
[Script / CSV / SRT Prompts]
          ↓
[AutoFlowCut Desktop / Story Engine v2]
  ├── Google Flow Login / BYOK API Key (Gemini & Veo 3.1)
  ├── Character & Background Reference System (Tag Matching)
  └── Multi-Track Audio & SFX Timeline Alignment (.audio_overrides.json)
          ↓
[1-Click Native Project Exporter]
  ├── CapCut Native Project Structure
  ├── Adobe Premiere Pro XML / .prproj
  └── Vrew Project (.vrew)
```

1. **Dual Generation Modes**:
   - **Google Flow Login**: Browser-driven session authentication for Google Flow generation.
   - **BYOK (API Key)**: Direct official Google GenAI APIs (`gemini-2.5-flash-image`, `veo-3.1-fast-generate-preview`) with encrypted OS Keychain storage (`safeStorage`).
2. **Visual Consistency & Media Priority**:
   - Resolves character, style, and environment anchor tags against reference sets.
   - Automatically assigns the best asset per scene following the hierarchy: `I2V (Image-to-Video) > T2V (Text-to-Video) > Image`.
3. **Multi-Track Audio Snapping**:
   - Ingests narration, dialogue voices, and SFX; locks clips to subtitle timecodes without altering original audio files.
4. **Agent Integration & MCP Server**:
   - Embeds a stdio MCP server (`mcp-server/index.js`) and HTTP API (`:3210`) enabling AI agents to programmatically query scenes, update prompts, inspect references, and trigger exports.

#### Key Capabilities
- Batch image generation (100+ scenes in ~2–5 minutes via BYOK API key).
- High-fidelity Veo 3.1 video generation (Text-to-Video and Image-to-Video).
- 87 built-in style presets with automatic prompt injection.
- Complete 1-click project export: timeline cuts, Ken Burns camera animation, audio tracks, and multilingual subtitles.
- Direct desktop app launch via macOS app bundle (`AutoFlowCut.app`).

#### Common Commands
```bash
# 1. Launch packaged macOS application
cd /Users/sharadkumar/opensource/AutoFlowCut
./run.sh

# 2. Run in live Vite + Electron development mode
./run.sh --dev

# 3. Start AutoFlowCut stdio MCP Server for AI agents
./run.sh --mcp
# or directly:
node mcp-server/index.js

# 4. Rebuild preloads and Vite production assets
./run.sh --build
```

#### Workspace Integration
- **Repository Location**: `/Users/sharadkumar/opensource/AutoFlowCut`
- **Application Binary**: `/Users/sharadkumar/opensource/AutoFlowCut/release/mac-arm64/AutoFlowCut.app`
- **Launcher Script**: `/Users/sharadkumar/opensource/AutoFlowCut/run.sh`
- **MCP Server**: `/Users/sharadkumar/opensource/AutoFlowCut/mcp-server/index.js`
- **Primary Use Case**: Automated AI image/video batch generation, Story Engine pipeline, and 1-click timeline export directly into CapCut, Adobe Premiere Pro, and Vrew.

---

### 30. Antigravity CLI (`agy`)

#### How It Works
Antigravity CLI is a compiled, standalone native Mach-O ARM64 binary written in Go that acts as the terminal-first interface to the Antigravity agentic engine:
```
[Terminal User / Shell Pipe]
    ↓ (stdin / CLI flags)
[agy CLI Binary (~/.local/bin/agy)]
    ↓ (OAuth2 / Google Auth Token Cache)
[Antigravity Agent Runtime / API Gateway]
    ↓ (Tool Calling / Subagents / MCP / Shell)
[Execution Result / Streaming TUI]
```
- **Authentication**: Native browser-based OAuth2 / OIDC authentication flow with Google accounts; credentials cached securely at `~/.gemini/antigravity-cli/`.
- **Dual Execution Modes**: 
  - **Full TUI Mode**: Rich interactive terminal session supporting multi-turn conversation, inline tool approval prompts, slash commands (`/help`, `/plan`, `/compact`), and real-time streaming tokens.
  - **Headless Prompt Runner Mode**: Accepts one-shot prompts via arguments (`agy -p "..."` or `agy "..."`) or Unix standard input pipes (`cat error.log | agy "diagnose"`), outputting plain text or scriptable responses directly to `stdout`.
- **Auto-Updater**: Integrates a background self-update mechanism checking for newer builds against Google Antigravity release endpoints.

#### Key Capabilities
- Autonomous coding, refactoring, script writing, and terminal command execution directly from the command line.
- Seamless project context loading based on current working directory.
- Configurable model selection, permissions, and tool execution gates via `~/.gemini/antigravity-cli/settings.json`.
- Support for piping input from git diffs, build logs, and source files.

#### Common Commands
```bash
# 1. Launch interactive terminal interface (TUI)
agy

# 2. Execute a direct one-shot instruction
agy "Review git diff and generate a summary of changes"

# 3. Headless prompt execution
agy -p "Write a python script to convert WAV files to 24kHz mono"

# 4. Pipe command output or file content into agy
cat build.log | agy "Explain the root cause of this failure"
git diff | agy "Generate a conventional git commit message"

# 5. Display help and command-line flags
agy --help

# 6. Check installed CLI version
agy --version
```

#### Workspace Integration
- **Binary Path**: `/Users/sharadkumar/.local/bin/agy`
- **Configuration Directory**: `~/.gemini/antigravity-cli/settings.json`
- **Primary Use Case**: Fast terminal-based agent interactions, CI/CD pipeline automation, code refactoring, and headless shell script orchestration.

---

### 31. Guney Motion Kit (`guney-motion-kit`, `hyperframes`)

#### How It Works
Guney Motion Kit is a programmatic motion graphics production framework built on top of **HyperFrames** (HeyGen's open-source HTML/CSS/JavaScript-to-video rendering engine). It converts web standard compositions (DOM, CSS transforms, SVG, WebGL, Canvas) into broadcast-quality 60fps MP4/WebM video with frame-level determinism.

```
[HTML5 / CSS / GSAP Composition]
       ↓
[HyperFrames Engine (Node.js + puppeteer-core)]
       ↓
[Chrome Headless Shell (v152.0.7928.2 ARM64)]
       ↓ (Deterministic beginFrame capture)
[Uncompressed 60fps PNG Frame Buffer]
       ↓ (FFmpeg 9.0.2 pipe)
[H.264 / ProRes 4444 Alpha Master Video]
```

- **Deterministic Frame Clock (`lib/stage.js`)**: Replaces non-deterministic browser animation clocks (`requestAnimationFrame`) with a discrete virtual time stepper (`STAGE.driver`). Ensures identical rendering across local machines and cloud runners. Provides seeded pseudo-randomness (`STAGE.mulberry32`) so generative visual noise is 100% reproducible.
- **Headless Chrome Pipeline**: Automates a cached Chrome Headless Shell binary (`~/.cache/hyperframes/chrome/...`) via `puppeteer-core`. Utilizes the Chromium `HeadlessExperimental.beginFrame` DevTools protocol to advance the timeline frame by frame, capturing full 1920x1080 frames without frame dropping or tearing.
- **Modular Component Library (`lib/`)**:
  - `backdrop.js`: Infinite dynamic background canvases (gradients, subtle grain, floating ambient geometry).
  - `text.js`: Big, high-contrast, phone-readable animated typography, word-by-word staggered reveals, and responsive typography bounds.
  - `cards.js`: 3D-perspective CSS cards, floating multi-layered cards with realistic soft shadows and tilt physics.
  - `build.js`: Progressive UI assembly animations where diagrams, node graphs, or interface elements self-assemble.
  - `claudewin.js`: Claude-style chat interface simulation with kinetic camera zooms, simulated typing strokes, and message card reveals.
- **Procedural Sound Design (`tools/audio/`, `sfx/`)**: Programmatic Foley sound effects generation and timeline audio mixing for keystrokes, UI clicks, pops, and whooshes.
- **Automated Frame Quality Gate (`tools/qa/`)**: Python-based computer vision script (`numpy`, `PIL`) that inspects rendered frame sequences for text readability, contrast ratios, dead zones, and pacing holds before final delivery.
- **NLE Overlay Compositing (`tools/resolve/`, `docs/RESOLVE.md`)**: Renders transparent alpha channels (ProRes 4444 or PNG image sequences) to seamlessly overlay motion graphics on top of DaVinci Resolve or CapCut footage timelines.

#### Key Capabilities
- Fast local rendering on Apple Silicon using multi-worker parallel frame capture (10-second 60fps full HD composition renders in ~10 seconds).
- Zero-cost, open-source local rendering without third-party cloud API dependencies.
- Standard web stack (HTML5, CSS3, GSAP 3) allows rapid prototyping and complete design freedom.
- Built-in live browser preview with scrubbing and playback controls (`npx hyperframes preview`).
- Transparent alpha channel rendering for non-linear editor (NLE) video compositing.

#### Common Commands & Operational Procedures
```bash
# 1. Quick health check (verifies Node, FFmpeg, Chrome headless shell, and test render)
npm run check

# 2. Scaffold a new video project
npm run new-video -- intro-sequence

# 3. Live interactive browser preview (with timeline scrubber)
cd video-projects/intro-sequence
npx hyperframes preview

# 4. Render broadcast master (60fps, high quality)
npx hyperframes render -o renders/intro-sequence.mp4 --fps 60 --quality high

# 5. Render transparent alpha overlay for DaVinci Resolve / CapCut
npx hyperframes render -o renders/overlay.mov --format mov --codec prores_ks --pix-fmt yuva444p10le

# 6. Synchronize AI assistant rules and agent skills
npm run sync
```

#### Workspace Integration
- **Installation Path**: `/Users/sharadkumar/opensource/guney-motion-kit`
- **Render Browser Cache**: `/Users/sharadkumar/.cache/hyperframes/chrome/`
- **Configuration**: `/Users/sharadkumar/opensource/guney-motion-kit/kit.config.json` (User: `Sharad`, House Style: `true`)
- **Primary Use Case**: YouTube video intros, dynamic callout cards, animated UI mockups, technical explanations, and title motion graphics.

---

---

### 32. CapCut MCP - Direct Draft Engine (`capcut-mcp`)

#### How It Works
`capcut-mcp` operates as a lightweight, zero-daemon stdio Model Context Protocol server that directly inspects and edits CapCut desktop project drafts (`draft_info.json` on macOS and `draft_content.json` on Windows). It uses defensive template cloning to ensure valid schema generation, checks if CapCut is open to prevent autosave clobbering, and writes changes atomically with companion `.mcpbak` backups.

```
[Claude / Coding Agent]
          ↓ (stdio MCP / JSON-RPC)
[capcut-mcp Server (Node.js)]
          ↓ (Atomic validation & template harvesting)
[~/Movies/CapCut/User Data/Projects/com.lveditor.draft/<Project>/draft_info.json]
```

#### Key Capabilities
- Direct inspection and listing of all local CapCut drafts and timeline tracks.
- Media placement on existing or new tracks (`capcut_add_video`, `capcut_add_audio`, `capcut_add_image`).
- Text overlay injection with harvested font styling (`capcut_add_text`).
- Timeline manipulations: trimming (`capcut_trim_segment`), splitting (`capcut_split_segment`), moving (`capcut_move_segment`), and deleting (`capcut_delete_segment`).
- Spatial transform adjustment: position, scale, rotation, and opacity (`capcut_set_props`).
- Zero background daemon requirement: runs instantly in-process via Node.js.

#### Common Commands
```bash
# 1. Run MCP server via stdio
cd /Users/sharadkumar/opensource/capcut-mcp
node src/server.js

# 2. Inspect timeline via Node one-liner
node -e "import('./src/core.js').then(({ listDrafts, CapCutDraft }) => console.log(listDrafts()));"
```

#### Workspace Integration
- **Repository Location**: `/Users/sharadkumar/opensource/capcut-mcp`
- **Entrypoint**: `/Users/sharadkumar/opensource/capcut-mcp/src/server.js`
- **MCP Server Name**: `capcut_direct` (in `~/.gemini/config/mcp_config.json`)
- **Primary Use Case**: Fast, programmatic timeline assembly, clip trimming, layout adjustments, and basic text overlays with zero overhead.

---

### 33. CapCut AI Editor - SmartCut (`capcut-ai-editor`)

#### How It Works
`capcut-ai-editor` (SmartCut) is a Python-based MCP server specialized in automated talking-head video editing. Instead of re-transcribing media from scratch, it reads the high-precision auto-generated captions already produced by CapCut Desktop (`draft_info.json`). It analyzes speech gaps, flags pauses exceeding a configurable threshold (e.g., > 1.0s), detects duplicate takes from stumbled sentences, and cuts the timeline directly in the project file.

```
[CapCut Video with Auto Captions] 
          ↓
[SmartCut MCP Server (Python)] 
  ├── Parses auto-generated subtitle timestamps
  ├── Heuristic / LLM duplicate take detection
  └── Computes cut boundaries
          ↓
[Rewrites draft_info.json with clean jump-cuts]
```

#### Key Capabilities
- Automated pause and silence cutting with customizable minimum pause thresholds.
- Duplicate take detection: keeps the last successful take and eliminates prior false starts.
- Subtitle editing, batch correction, splitting, and merging.
- Word-level timing adjustment and alignment.
- Works 100% locally with heuristic algorithms (no API keys required), with optional OpenAI enhancement.

#### Common Commands
```bash
# 1. Run SmartCut MCP server
cd /Users/sharadkumar/opensource/capcut-ai-editor
.venv/bin/python -m smartcut.server

# 2. Run smart cut programmatically
.venv/bin/python -c "import asyncio; from smartcut.tools.capcut_projects import smart_cut_project; asyncio.run(smart_cut_project(project_name='MyDraft', min_pause_sec=1.0))"
```

#### Workspace Integration
- **Repository Location**: `/Users/sharadkumar/opensource/capcut-ai-editor`
- **Python Environment**: `/Users/sharadkumar/opensource/capcut-ai-editor/.venv` (Python 3.12)
- **MCP Server Name**: `capcut_smartcut` (in `~/.gemini/config/mcp_config.json`)
- **Primary Use Case**: Automated A-roll speech cleanup, podcast rough-cuts, and talking-head silence/stumble elimination.

---

### 34. CapCut MCP Kit & VectCutAPI (`capcut-mcp-kit`)

#### How It Works
`capcut-mcp-kit` is a comprehensive video production toolkit combining a TypeScript MCP server with an enhanced `VectCutAPI` backend. It auto-spawns a local Flask service on `http://localhost:9001` running on Apple Silicon GPU (`mlx-metal` / `mlx-whisper`). It exposes high-level directorial capabilities including 65 cinematic camera movements, keyframe motion choreography, video effects, transitions, and automatic background music ducking.

```
[Claude / Coding Agent]
          ↓ (stdio MCP)
[capcut-mcp-server (Node.js TypeScript)]
          ↓ (Authenticated HTTP / X-CapCut-Kit-Token)
[VectCutAPI Backend (Flask on :9001)]
  ├── MLX-Whisper (Apple Silicon Metal GPU)
  ├── 65 Camera Movement Choreographies (Quad Ease)
  └── Multi-Track Audio Snapping & Auto-Ducking
          ↓
[CapCut Draft Projects (~/Movies/CapCut/...)]
```

#### Key Capabilities
- 65 professional camera movement presets (slow zoom, punch-in, whip pan, tilt, tracking moves).
- Bezier and Quad-Ease keyframing for smooth scale, position, and rotation animation.
- Background music insertion with automatic volume ducking under spoken dialogue.
- Subtitle stylization, sticker insertion, video filters, and transition assignment.
- Dual-mode server: stdio MCP interface with automated backend daemon lifecycle management.

#### Common Commands
```bash
# 1. Start VectCutAPI standalone backend
cd /Users/sharadkumar/opensource/capcut-mcp-kit
./start-server.sh

# 2. Run MCP server via stdio
cd /Users/sharadkumar/opensource/capcut-mcp-kit/capcut-mcp-server
node dist/index.js
```

#### Workspace Integration
- **Repository Location**: `/Users/sharadkumar/opensource/capcut-mcp-kit`
- **Python Environment**: `/Users/sharadkumar/opensource/capcut-mcp-kit/vectcut-api/venv` (Python 3.12, MLX Metal)
- **Token Location**: `~/Library/Application Support/capcut-mcp-kit/token`
- **MCP Server Name**: `capcut_kit` (in `~/.gemini/config/mcp_config.json`)
- **Primary Use Case**: High-end cinematic polish, dynamic camera motions, keyframe choreography, and auto-ducked music integration.

---

## Workspace Integration

The tools above integrate with the existing MCP servers located in this directory:
- **`guney-motion-kit`**: Open-source HTML-to-video motion graphics production engine at `opensource/guney-motion-kit`. Uses HyperFrames and Chrome Headless Shell to render 60fps animations, 3D cards, animated text, and transparent NLE overlays for DaVinci Resolve and CapCut.
- **`Audacity-MCP`**: Automated multi-track editing, spectral repair, and acoustic leveling.
- **`kdenlive-mcp-server`**: Timeline assembly, EDL sync, clip sequencing, and XML project exports. Can directly invoke `melt` and `kdenlive_render` for automated background exports.
- **`demucs`**: Neural source separation and voice watermark removal for clean background music beds.
- **`moss-soundeffect-v2`**: 48kHz stereo text-to-foley diffusion engine at `opensource/MOSS-TTS/moss_soundeffect_v2` for automated scene sound effect and Foley design.
- **`drawthings` (`mcp-drawthings`)**: Local AI text-to-image and image-to-image generation powered by Draw Things app on Apple Silicon, configured in `~/.gemini/config/mcp_config.json`.
- **`upscayl`**: Neural super-resolution image upscaling (2x–4x) powered by Real-ESRGAN/NCNN on Apple Silicon GPU, available via `/Users/sharadkumar/.local/bin/upscayl` and `/Applications/Upscayl.app`.
- **`folderium`**: File organization and workspace structure automation.
- **Python Audio/Image Stack**: Enables offline validation scripts (`story-editor` skill) to compute exact RMS silence thresholds, verify video frame alignment, and automate timeline sync.
- **`voicebox`**: Local AI voice studio providing neural voice cloning, multi-engine text-to-speech, audio effects DSP (Spotify Pedalboard), and agent voice synthesis via REST API (`17493`) and native MCP server (`voicebox-mcp`).
- **`Bionic (LM Studio)`**: Local LLM host and OpenAI-compatible server on `127.0.0.1:1234` running Google Gemma on Apple Silicon MLX GPU with zero API cost.
- **`hermes-agent`**: Autonomous self-improving AI agent harness at `opensource/hermes-agent`. Can operate locally via TUI, connect to Gemma on Bionic, and automate multi-channel tasks via Telegram, Discord, or CLI.
- **`whisper`**: Neural speech-to-text pipeline providing frame-accurate word-level transcription and `.srt`/`.vtt` generation for vertical video Shorts and timeline sync validation (`story-editor` skill).
- **`openshorts`**: AI-powered vertical short-form video generation studio at `opensource/openshorts`. Integrates local Faster-Whisper, YOLOv8/MediaPipe speaker tracking, and interactive Vite/React dashboard on `http://localhost:5173`.
- **`f5-tts`**: Flow-matching diffusion zero-shot voice cloning and Hindi/multilingual TTS engine at `opensource/F5-TTS`, providing instant custom voice cloning for storytelling narrators and character voices.
- **`omnivoice`**: Massively multilingual diffusion zero-shot TTS engine (600+ languages), natural language voice design, and expressive speech synthesis at `opensource/OmniVoice`, providing global and character voice generation.
- **`blackhole`**: Zero-latency virtual audio loopback driver at `opensource/BlackHole`. Connects system sound, DAW tracks, and AI voice engines (`voicebox`, `f5-tts`, `omnivoice`) to `Audacity` and screen capture tools with zero extra latency.
- **`maya2-native`**: High-fidelity Indic & English neural TTS, streaming, and cross-lingual voice cloning at `opensource/MayaTTS`. Powered by native Apple Silicon MLX on M4 Metal GPU, delivering sub-second real-time factor (0.68x–0.73x) for Hindi storytelling narration and character voice synthesis.
- **`indicf5`**: AI4Bharat's near-human polyglot TTS and zero-shot voice cloning model across 11 Indian languages at `opensource/IndicF5`, generating 24 kHz studio speech via flow-matching DiT and Vocos vocoder.
- **`vocalis` (`AI-Studio-App`)**: AI Script & Voice TTS Studio at `opensource/Vocalis/AI-Studio-App-main` (symlinked at `opensource/AI-Studio-App`), delivering script polishing, multi-speaker dialogues, voice analysis, and Gemini-powered audio synthesis on `http://localhost:3000`.
- **`flow-mcp`**: Google Flow browser automation and MCP server at `opensource/flow-mcp`, driving AI video generation, character design, keyframing, and local studio dashboard on `http://127.0.0.1:8787`.
- **`splicekit`**: Final Cut Pro runtime injection, Command Palette (`Cmd+Shift+P`), and programmatic MCP server (~200 tools) for direct timeline and audio control at `opensource/SpliceKit`.
- **`youtube_uploader` (`youtube-uploader-mcp`)**: Programmatic YouTube video upload, metadata management, OAuth2 multi-channel credentials, subtitle attaching, and custom thumbnail setting at `opensource/youtube-uploader-mcp`.
- **`autoflowcut` (`autoflowcut-mcp`)**: AI visual production, Story Engine v2 pipeline, batch Gemini/Veo generation, and 1-click CapCut/Premiere/Vrew export bridge at `opensource/AutoFlowCut`.
- **`capcut_direct` (`capcut-mcp`)**: Lightweight zero-daemon direct draft JSON editor at `opensource/capcut-mcp` for instant timeline layout, clip trimming, splitting, and text styling.
- **`capcut_smartcut` (`capcut-ai-editor`)**: Intelligent talking-head audio/video silence and stumble cutter at `opensource/capcut-ai-editor` utilizing CapCut auto-captions.
- **`capcut_kit` (`capcut-mcp-kit`)**: High-level production suite at `opensource/capcut-mcp-kit` featuring 65 camera moves, keyframing, transitions, and MLX-accelerated music ducking via VectCutAPI.

