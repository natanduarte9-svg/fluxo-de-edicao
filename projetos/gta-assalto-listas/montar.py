"""Monta um Short do Jogatina Fácil (estilo Painel + narração do Suno) a partir de vários trechos da gameplay.
Uso: python montar.py <spec.json> <n>   (pasta de trabalho: /home/user/gta2)
spec[n] = {
  "clips": [[inicio_s, dur_s], ...],                 # trechos da gameplay, colados com corte seco
  "narr": "n1",                                       # narr/<n>.mp3 + narr/<n>_words.json (Scribe)
  "frases": [[i0, i1, t_no_video], ...],              # palavras i0..i1 da narração começam em t_no_video
  "numeros": [[t, "3"], ...],                         # (listas) número gigante + som de impacto
  "titulo": [fig, linha1, linha2], "titulo_ate": s, "etiquetas": [[a, b, [rot, txt, cor, borda]], ...],
  "camera": ["CAM 01", "LUCIA"], "sticker": s, "chave": [palavras em laranja]
}
Faz: w<n>/src/gameplay.mp4 (montagem 16:9 com som do jogo), mix (voz + jogo −13 dB na fala + impactos),
legendas palavra por palavra (3 palavras por vez, chave em laranja), e chama ferramentas/painel/painel.py."""
import sys, os, json, subprocess, shutil
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, "/root/lemo-opuscar")
from core.audio import sfx as X

G = "/home/user/gta2"; SR = 48000
SPEC = json.load(open(sys.argv[1]))[sys.argv[2]]; N = sys.argv[2]
WD = f"{G}/w{N}"; os.makedirs(f"{WD}/src", exist_ok=True); os.makedirs(f"{WD}/tmp", exist_ok=True)
if not os.path.exists(f"{WD}/sticker"): os.symlink("/home/user/gta-cortes/sticker", f"{WD}/sticker")

# 1) montagem 16:9 (re-codifica cada trecho no tempo exato e cola)
parts = []
for k, (a, d) in enumerate(SPEC["clips"]):
    p = f"{WD}/tmp/c{k}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-t", str(d), "-i", f"{G}/src.mp4", "-vf", "fps=30,scale=1280:720",
                    "-af", "aresample=48000", "-ac", "2", "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-c:a", "pcm_s16le", p], check=True)
    parts.append(p)
open(f"{WD}/tmp/lista.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{WD}/tmp/lista.txt", "-c:v", "copy", "-c:a", "pcm_s16le",
                f"{WD}/src/gameplay.mov"], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{WD}/src/gameplay.mov", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", f"{WD}/src/gameplay.mp4"], check=True)
D = sum(d for _, d in SPEC["clips"])

# 2) áudio: jogo + narração encaixada + impactos
def load(p, ss=None, t=None):
    cmd = ["ffmpeg", "-v", "error"] + (["-ss", str(ss), "-t", str(t)] if ss is not None else []) + ["-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.check_output(cmd), np.float32).reshape(-1, 2).copy()
game = load(f"{WD}/src/gameplay.mov"); L = len(game)
voz_src = load(f"{G}/narr/{SPEC['narr']}.mp3"); W = json.load(open(f"{G}/narr/{SPEC['narr']}_words.json"))
voz = np.zeros((L, 2), np.float32); mask = np.zeros(L, np.float32); words = []
for i0, i1, t in SPEC["frases"]:
    a, b = W[i0][1], W[i1][2]; pa, pb = int((a - 0.08) * SR), int((b + 0.15) * SR); pt = int(t * SR)
    seg = voz_src[pa:pb][:max(0, L - pt)]; voz[pt:pt + len(seg)] += seg
    mask[max(0, pt - int(0.15 * SR)):pt + len(seg) + int(0.25 * SR)] = 1
    for w in W[i0:i1 + 1]: words.append((w[0], t + 0.08 + w[1] - a, t + 0.08 + w[2] - a, (i0, i1)))
k = int(0.25 * SR); sm = np.convolve(np.convolve(mask, np.ones(k) / k, "same"), np.ones(k) / k, "same")
def rms(x): return np.sqrt((x ** 2).mean() + 1e-12)
voz = voz / max(rms(voz[mask > 0.5]), 1e-6) * 0.12
game = game / max(rms(game), 1e-6) * 0.12 * 10 ** (-3 / 20)
out = voz + game * (1 - sm * (1 - 10 ** (-13 / 20)))[:, None]
for t, _ in SPEC.get("numeros", []):        # impacto grave + whoosh curto na entrada do número
    th = X.norm(X.thump(1.0, 55), 0.55); wh = X.norm(X.whoosh(0.32), 0.22)
    s0 = int((t - 0.18) * SR); w0 = np.interp(np.arange(int(len(wh) * SR / X.SR)) * X.SR / SR, np.arange(len(wh)), wh)
    t0 = int(t * SR); th2 = np.interp(np.arange(int(len(th) * SR / X.SR)) * X.SR / SR, np.arange(len(th)), th)
    out[s0:s0 + len(w0)] += (w0[:max(0, L - s0)])[:, None]; out[t0:t0 + len(th2)] += (th2[:max(0, L - t0)])[:, None]
fo = int(0.6 * SR); out[-fo:] *= np.linspace(1, 0, fo)[:, None]
sf.write(f"{WD}/tmp/mix.wav", out.astype(np.float32), SR)

# 3) legendas da narração (3 palavras por vez, palavra-chave em laranja)
KEY = set(x.lower() for x in SPEC.get("chave", []))
F0 = "/home/user/fonts/Montserrat.ttf"
def font(s): f = ImageFont.truetype(F0, s); f.set_variation_by_name("Black"); return f
caps = []; j = 0; i = 0
while i < len(words):
    g = [words[i]]
    while len(g) < 3 and i + len(g) < len(words) and words[i + len(g)][3] == words[i][3]: g.append(words[i + len(g)])
    i += len(g)
    im = Image.new("RGBA", (1080, 300)); d = ImageDraw.Draw(im); sp = 18
    txt = [w[0].upper().rstrip(":") for w in g]; Fg = font(64)
    while sum(d.textlength(x, font=Fg) for x in txt) + sp * (len(g) - 1) > 1000: Fg = font(Fg.size - 4)
    wl = [d.textlength(x, font=Fg) for x in txt]; x = (1080 - sum(wl) - sp * (len(g) - 1)) / 2
    for (w, _, _, _), tx, ww in zip(g, txt, wl):
        cor = (245, 150, 40) if w.lower().strip(",.!?:") in KEY else (255, 255, 255)
        d.text((x, 40), tx, font=Fg, fill=cor, stroke_width=5, stroke_fill=(5, 12, 24)); x += ww + sp
    sh = Image.new("RGBA", im.size); sh.putalpha(im.split()[3].filter(ImageFilter.GaussianBlur(8)).point(lambda v: v * 160 // 255))
    Image.alpha_composite(sh, im).save(f"{WD}/tmp/cap_{N}_{j}.png")
    nxt = words[i][1] if i < len(words) else 99
    caps.append([round(g[0][1] - 0.05, 2), round(min(g[-1][2] + 0.35, nxt - 0.03), 2), [["", " ".join(x[0] for x in g)]]]); j += 1
json.dump({N: caps}, open(f"{WD}/falas.json", "w"), ensure_ascii=False)
cfg = {k: SPEC[k] for k in ("titulo", "titulo_ate", "camera", "etiquetas", "sticker") if k in SPEC}
cfg["numeros"] = SPEC.get("numeros", [])
json.dump({N: cfg}, open(f"{WD}/painel_cfg.json", "w"), ensure_ascii=False)

# 4) Painel
saida = f"{G}/short{N}.mp4"
subprocess.run(["/root/lemo-opuscar/.venv/bin/python", "/home/user/fluxo-de-edicao/ferramentas/painel/painel.py", saida, "0", str(D), N, N, f"{WD}/tmp/mix.wav"],
               cwd=WD, check=True)
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", saida]))
assert dur <= 40.05, f"passou de 40 s: {dur}"
print("ok", saida, round(dur, 2), "s")
