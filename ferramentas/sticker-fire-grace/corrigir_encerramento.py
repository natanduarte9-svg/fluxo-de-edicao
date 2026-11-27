"""Reescreve "FIRE & GRACE" inteiro no logo do encerramento oficial 9:16 (o logo original mostra "IRE & GRAC").
Uso: python corrigir_encerramento.py <entrada.mp4> <saida.mp4>
Logo: centro (539, 695), disco preto r<140 (anel branco/vermelho fora). Só nos quadros em que o logo já está parado (>= 52)."""
import sys, os, subprocess, tempfile, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
IN, OUT = sys.argv[1], sys.argv[2]
FONTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fontes", "Cinzel.ttf")
tmp = tempfile.mkdtemp()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", IN, f"{tmp}/e%03d.png"], check=True)
fs = sorted(os.listdir(tmp)); Hh, Ww = np.asarray(Image.open(f"{tmp}/{fs[0]}")).shape[:2]
CX, CY, R, Y0, Y1 = 539, 695, 139, 736, 788
yy, xx = np.mgrid[0:Hh, 0:Ww]; r = np.sqrt((xx - CX) ** 2 + (yy - CY) ** 2)
f = np.clip(np.minimum(yy - Y0, Y1 - yy) / 8.0, 0, 1)
band = (yy >= Y0) & (yy <= Y1) & (r < R)
S = 4; font = ImageFont.truetype(FONTE, 27 * S); txt, sp = "FIRE & GRACE", 2.6 * S
ws = [font.getlength(c) for c in txt]; tw = sum(ws) + sp * (len(txt) - 1)
lay = Image.new("L", (Ww * S, Hh * S), 0); d = ImageDraw.Draw(lay); x = CX * S - tw / 2
for c, w in zip(txt, ws): d.text((x, 749 * S), c, font=font, fill=255); x += w + sp
lay = lay.resize((Ww, Hh), Image.LANCZOS)
t = np.asarray(lay).astype(np.float32)[..., None] / 255
g = np.asarray(lay.filter(ImageFilter.GaussianBlur(4))).astype(np.float32)[..., None] / 255
for i, fn in enumerate(fs):
    if i + 1 < 52: continue
    a = np.asarray(Image.open(f"{tmp}/{fn}")).astype(np.float32)
    a[band] *= (1 - f[band])[:, None]
    a = a + g * np.array([210, 140, 60]) * 0.6
    a = a * (1 - t) + t * np.array([248, 234, 204])
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(f"{tmp}/{fn}")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "30", "-i", f"{tmp}/e%03d.png", "-c:v", "libx264", "-crf", "14",
                "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", OUT], check=True)
print("ok", OUT)
