"""Narração do Suno no estilo Painel: frases encaixadas na cena, legenda com o tempo EXATO de cada palavra
(transcrição do ElevenLabs Scribe), jogo −13 dB enquanto ele fala."""
import json, subprocess, numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S, E = 2776, 2804; SR = 48000; D = E - S
W = json.load(open("suno/words.json"))
FR = [(0, 10), (11, 18), (19, 27), (28, 32), (33, 40), (41, 46), (47, 52), (53, 54)]     # índices de palavras de cada frase
EM = [0.1, 3.5, 6.2, 9.0, 11.5, 21.2, 23.4, 25.2]                                        # onde cada frase começa no vídeo
def load(p): return np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]), np.float32).reshape(-1, 2)
voz_src = load("suno/v.wav")
game = np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-ss", str(S), "-t", str(D), "-i", "src/gameplay.mp4", "-vn", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]), np.float32).reshape(-1, 2).copy()
N = len(game); voz = np.zeros((N, 2), np.float32); mask = np.zeros(N, np.float32); words = []
for (i0, i1), t in zip(FR, EM):
    a, b = W[i0]["start"], W[i1]["end"]; pa, pb = int((a - 0.06) * SR), int((b + 0.12) * SR); pt = int(t * SR)
    seg = voz_src[pa:pb]; voz[pt:pt + len(seg)] += seg[:N - pt]
    mask[max(0, pt - int(0.15 * SR)):pt + len(seg) + int(0.25 * SR)] = 1
    for w in W[i0:i1 + 1]: words.append((w["text"], t + 0.06 + w["start"] - a, t + 0.06 + w["end"] - a, (i0, i1)))
k = int(0.25 * SR); sm = np.convolve(np.convolve(mask, np.ones(k) / k, "same"), np.ones(k) / k, "same")
def rms(x): return np.sqrt((x ** 2).mean() + 1e-12)
voz = voz / max(rms(voz[mask > 0.5]), 1e-6) * 0.12
game = game / max(rms(game), 1e-6) * 0.12 * 10 ** (-3 / 20)
out = voz + game * (1 - sm * (1 - 10 ** (-13 / 20)))[:, None]
fo = int(0.6 * SR); out[-fo:] *= np.linspace(1, 0, fo)[:, None]
sf.write("suno/mix_suno.wav", out.astype(np.float32), SR)
KEY = {"gta", "6:", "explosão", "gigante", "pântano,", "atirador", "helicóptero.", "doug", "lori,", "jason", "acerta.", "vivo.", "diferente?", "comenta"}
F = ImageFont.truetype("/home/user/fonts/Montserrat.ttf", 64); F.set_variation_by_name("Black")
caps = []; j = 0; i = 0
while i < len(words):
    g = [words[i]]
    while len(g) < 3 and i + len(g) < len(words) and words[i + len(g)][3] == words[i][3]: g.append(words[i + len(g)])
    i += len(g)
    im = Image.new("RGBA", (1080, 300)); d = ImageDraw.Draw(im); sp = 18
    txt = [w[0].upper().rstrip(":") for w in g]; Fg = F
    while sum(d.textlength(x, font=Fg) for x in txt) + sp * (len(g) - 1) > 1000:
        Fg = ImageFont.truetype("/home/user/fonts/Montserrat.ttf", Fg.size - 4); Fg.set_variation_by_name("Black")
    wl = [d.textlength(x, font=Fg) for x in txt]; x = (1080 - sum(wl) - sp * (len(g) - 1)) / 2
    for (w, _, _, _), tx, ww in zip(g, txt, wl):
        d.text((x, 40), tx, font=Fg, fill=(245, 150, 40) if w.lower() in KEY else (255, 255, 255), stroke_width=5, stroke_fill=(5, 12, 24)); x += ww + sp
    sh = Image.new("RGBA", im.size); sh.putalpha(im.split()[3].filter(ImageFilter.GaussianBlur(8)).point(lambda v: v * 160 // 255))
    Image.alpha_composite(sh, im).save(f"tmp/cap_S_{j}.png")
    nxt = words[i][1] if i < len(words) else 99
    caps.append([round(g[0][1] - 0.05, 2), round(min(g[-1][2] + 0.35, nxt - 0.03), 2), [["", " ".join(x[0] for x in g)]]]); j += 1
f = json.load(open("falas.json")); f["S"] = caps; json.dump(f, open("falas.json", "w"), ensure_ascii=False, indent=0)
print("ok", j, "legendas")
