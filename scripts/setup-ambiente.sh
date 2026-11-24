#!/bin/bash
# Ferramentas de produção de vídeo (guia: fluxo-de-edicao/GUIA-PRODUCAO.md)
export PATH="/usr/local/bin:/opt/node22/bin:/root/.local/bin:$PATH"
ROOT=$(pwd)
# ffmpeg 7+ (o do Ubuntu é 6.1); binário estático do pacote imageio-ffmpeg (PyPI)
v=$(ffmpeg -version 2>/dev/null | head -1 | sed -E 's/^ffmpeg version n?([0-9]+).*/\1/')
if [ -z "$v" ] || [ "$v" -lt 7 ] 2>/dev/null; then
  d=$(mktemp -d)
  python3 -m pip download -q --no-deps imageio-ffmpeg -d "$d" \
    && python3 -m zipfile -e "$d"/*.whl "$d/x" \
    && install -m755 "$d"/x/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-* /usr/local/bin/ffmpeg
  rm -rf "$d"
fi
# Plugins: lemo-opuscar e pixelfx
claude plugin marketplace add lemomo-ai/lemo-opuscar || true
claude plugin install lemo-opuscar@lemolab || true
claude plugin marketplace add patch-gg/pixelfx || true
claude plugin install pixelfx@pixelfx || true
# Biblioteca e dependências do lemo-opuscar
S=$(ls ~/.claude/plugins/cache/lemolab/lemo-opuscar/*/skills/lemo-opuscar/scripts/setup.sh 2>/dev/null | head -1)
[ -n "$S" ] && { sh "$S" && sh "$S" deps voice music; } || true
# OpenCV (câmera e efeitos dos documentários) e fontes Cinzel/Montserrat (títulos e legendas)
[ -x /root/lemo-opuscar/.venv/bin/python ] && uv pip install -q --python /root/lemo-opuscar/.venv/bin/python opencv-python-headless noisereduce || true
mkdir -p /home/user/fonts && cp -n "$ROOT/fluxo-de-edicao/ferramentas/fontes/"*.ttf /home/user/fonts/ 2>/dev/null || true
# Skills: video-shotcraft e /produzir-video
mkdir -p ~/.claude/skills
[ -d ~/video-shotcraft ] || git clone -q --depth 1 https://github.com/Vincentwei1021/video-shotcraft ~/video-shotcraft || true
[ -d ~/video-shotcraft ] && ln -sfn ~/video-shotcraft ~/.claude/skills/video-shotcraft
[ -d "$ROOT/fluxo-de-edicao/skills/produzir-video" ] && ln -sfn "$ROOT/fluxo-de-edicao/skills/produzir-video" ~/.claude/skills/produzir-video
# Kit: librosa, three.js, física e pós-processamento
mkdir -p ~/motion-kit && cd ~/motion-kit || exit 0
[ -x .venv/bin/python ] || uv venv -q .venv
uv pip install -q --python .venv/bin/python librosa || true
[ -f package.json ] || npm init -y >/dev/null
npm i --silent --no-audit --no-fund three @react-three/fiber @react-three/drei @react-three/rapier @react-three/postprocessing postprocessing react react-dom || true
exit 0
