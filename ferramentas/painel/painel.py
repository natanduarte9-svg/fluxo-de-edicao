"""Estilo "Painel de controle" (GUIA seção 14) aplicado a um trecho da gameplay — identidade Jogatina Fácil.
Fundo azul-marinho com grade técnica, janela do jogo com cantoneiras douradas, widget "RADAR JOGATINA" com
onda que reage ao som do jogo, título gigante (branco + laranja) por cima da janela, etiquetas de etapa,
rótulo de câmera, falas do jogo grandes embaixo e sticker "Inscreva-se". Só o som do jogo.
Uso: python painel.py <saida> <inicio_s> <fim_s> <n_falas>"""
import sys, json, math, subprocess, glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
OUT, S, E, NF = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
NFAL = sys.argv[5] if len(sys.argv) > 5 else NF; AUDIO = sys.argv[6] if len(sys.argv) > 6 else None
D = E - S; FPS = 30; W, H = 1080, 1920
MONT = "/home/user/fonts/Montserrat.ttf"
def F(size, var="Black"):
    f = ImageFont.truetype(MONT, size); f.set_variation_by_name(var); return f
NAVY1, NAVY2 = (10, 23, 41), (16, 36, 58)
GRID = (70, 120, 180); BLUE = (64, 130, 210); GOLD = (232, 170, 60); ORANGE = (245, 150, 40); LBLUE = (120, 170, 230)
# janela do jogo
FW, FH = 1000, 760; FX, FY = 40, 650

# ---------- camada fixa: fundo, grade, janela, widget ----------
base = Image.new("RGB", (W, H)); px = np.zeros((H, W, 3), np.float32)
yy = np.linspace(0, 1, H)[:, None]
for c in range(3): px[..., c] = NAVY1[c] * (1 - yy) + NAVY2[c] * yy * 0.9 + NAVY1[c] * 0.1
base = Image.fromarray(px.astype(np.uint8)).convert("RGBA")
g = Image.new("RGBA", (W, H)); dg = ImageDraw.Draw(g)
for x in range(0, W, 40): dg.line([(x, 0), (x, H)], fill=GRID + (28 if x % 200 else 50,), width=1)
for y in range(0, H, 40): dg.line([(0, y), (W, y)], fill=GRID + (28 if y % 200 else 50,), width=1)
base.alpha_composite(g)
d = ImageDraw.Draw(base)
d.rectangle([FX - 3, FY - 3, FX + FW + 2, FY + FH + 2], outline=BLUE + (255,), width=2)
L = 34
for (x, y, sx, sy) in [(FX - 10, FY - 10, 1, 1), (FX + FW + 9, FY - 10, -1, 1), (FX - 10, FY + FH + 9, 1, -1), (FX + FW + 9, FY + FH + 9, -1, -1)]:
    d.line([(x, y), (x + sx * L, y)], fill=GOLD + (255,), width=5); d.line([(x, y), (x, y + sy * L)], fill=GOLD + (255,), width=5)
# widget
WX, WY, WW, WH = 40, 110, 380, 140
d.rounded_rectangle([WX, WY, WX + WW, WY + WH], 10, fill=(8, 20, 38, 230), outline=BLUE + (255,), width=2)
d.text((WX + 16, WY + 12), "R A D A R   J O G A T I N A", font=F(22, "Bold"), fill=LBLUE)
BASE = base

# ---------- som do jogo: volume para a onda ----------
raw = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", str(S), "-t", str(D), "-i", "src/gameplay.mp4", "-vn", "-ac", "1", "-ar", "8000", "-f", "f32le", "-"])
au = np.frombuffer(raw, np.float32)
env = np.array([np.sqrt((au[int(i / FPS * 8000):int((i + 1) / FPS * 8000)] ** 2).mean() + 1e-9) for i in range(int(D * FPS) + 2)])
env = np.nan_to_num(env); env = np.convolve(env, np.ones(4) / 4, mode="same"); env = env / (np.percentile(env, 95) + 1e-9)

# ---------- textos ----------
def shadow(lay, r=10, a=200):
    al = lay.split()[3].filter(ImageFilter.GaussianBlur(r)).point(lambda v: min(255, v * a // 255))
    sh = Image.new("RGBA", lay.size); sh.putalpha(al); return Image.alpha_composite(sh, lay)
def titulo(fig, l1, l2):
    lay = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(lay)
    d.text((44, 400), fig, font=F(26, "Bold"), fill=LBLUE)
    f = F(112, "Black"); d.text((40, 435), l1, font=f, fill=(255, 255, 255), stroke_width=3, stroke_fill=(5, 12, 24))
    d.text((40, 545), l2, font=f, fill=ORANGE, stroke_width=3, stroke_fill=(5, 12, 24))
    w2 = d.textlength(l2, font=f); d.rectangle([44, 672, 44 + w2 * 0.85, 680], fill=ORANGE)
    return shadow(lay, 12, 210)
def etiqueta(rot, txt, cor, borda):
    cor, borda = tuple(cor), tuple(borda)
    lay = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(lay)
    f = F(58, "Black"); w = d.textlength(txt, font=f)
    x0, y0 = FX, FY - 128; d.rectangle([x0, y0, x0 + w + 44, y0 + 112], fill=(6, 15, 30, 235), outline=borda + (255,), width=3)
    d.rectangle([x0, y0, x0 + 8, y0 + 112], fill=borda + (255,))
    d.text((x0 + 26, y0 + 10), rot, font=F(24, "Bold"), fill=(220, 225, 235)); d.text((x0 + 24, y0 + 38), txt, font=f, fill=cor)
    return shadow(lay, 8, 180)
def camera(cam, nome):
    lay = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(lay)
    x, y = FX + 18, FY + FH - 62
    f1, f2, f3 = F(26, "ExtraBold"), F(34, "Black"), F(22, "ExtraBold")
    w1 = d.textlength(cam, font=f1); w2 = d.textlength(nome, font=f2); w3 = d.textlength("AO VIVO", font=f3)
    d.rectangle([x - 8, y - 6, x + w1 + w2 + w3 + 70, y + 44], fill=(5, 12, 24, 200))
    d.text((x, y + 6), cam, font=f1, fill=GOLD); d.text((x + w1 + 16, y), nome, font=f2, fill=(255, 255, 255))
    xr = x + w1 + w2 + 34; d.rounded_rectangle([xr, y + 6, xr + w3 + 22, y + 36], 6, fill=(220, 40, 45)); d.text((xr + 11, y + 9), "AO VIVO", font=f3, fill=(255, 255, 255))
    return lay
CFG = json.load(open("painel_cfg.json"))[NF]
TIT = titulo(*CFG["titulo"]); CAM = camera(*CFG["camera"])
ETQ = [(a, b, etiqueta(*x)) for a, b, x in CFG["etiquetas"]]
FALAS = json.load(open("falas.json")).get(NFAL, [])
CAPS = [(a, b, Image.open(f"tmp/cap_{NFAL}_{j}.png").convert("RGBA")) for j, (a, b, _) in enumerate(FALAS)]
STK = sorted(glob.glob("sticker/s*.png")); T_STK = CFG.get("sticker", 1.0)
# (listas) número gigante "#3" que salta no meio da janela do jogo (técnica do canal Desbugando)
def numero(n):
    lay = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(lay); f = F(300, "Black"); txt = f"#{n}"
    tw = d.textlength(txt, font=f); x, y = FX + (FW - tw) / 2, FY + FH / 2 - 190
    d.text((x, y), txt, font=f, fill=ORANGE, stroke_width=10, stroke_fill=(5, 12, 24))
    return shadow(lay, 16, 230)
NUMS = [(t, numero(n)) for t, n in CFG.get("numeros", [])]
def fade(lay, a):
    if a >= 1: return lay
    r, g_, b, al = lay.split(); return Image.merge("RGBA", (r, g_, b, al.point(lambda v: int(v * a))))
def sm(x): x = max(0, min(1, x)); return x * x * (3 - 2 * x)

# ---------- quadros ----------
proc = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(S), "-t", str(D), "-i", "src/gameplay.mp4", "-vf", f"scale=-2:{FH}:flags=lanczos,crop={FW}:{FH},fps={FPS}",
                         "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "tmp/painel_video.mp4"], stdin=subprocess.PIPE)
i = 0
while True:
    buf = proc.stdout.read(FW * FH * 3)
    if len(buf) < FW * FH * 3: break
    t = i / FPS
    img = BASE.copy()
    img.paste(Image.frombytes("RGB", (FW, FH), buf), (FX, FY))
    img.alpha_composite(CAM)
    d = ImageDraw.Draw(img)
    # onda do radar: senoide que anda, altura pelo som do jogo
    amp = 10 + 34 * min(1.6, env[min(i, len(env) - 1)])
    pts = [(WX + 16 + k * 3.45, WY + 92 + amp * math.sin(k * 0.11 + t * 7) * (0.6 + 0.4 * math.sin(k * 0.03 + t * 2))) for k in range(101)]
    d.line(pts, fill=GOLD + (255,), width=4)
    # título (entra com subida curta) e etiquetas
    ta = sm(t / 0.35) * (1 - sm((t - CFG["titulo_ate"]) / 0.3))
    if ta > 0: img.alpha_composite(fade(TIT.transform(TIT.size, Image.AFFINE, (1, 0, 0, 0, 1, -int((1 - sm(t / 0.35)) * 30))), ta))
    for a, b, lay in ETQ:
        if a - 0.01 <= t < b + 0.25: img.alpha_composite(fade(lay, sm((t - a) / 0.2) * (1 - sm((t - b) / 0.25))))
    for tn, lay in NUMS:
        u = (t - tn) / 0.9
        if 0 <= u < 1:
            sc = 1.6 - 0.6 * sm(u / 0.25) if u < 0.25 else 1.0          # entra grande e assenta
            al = sm(u / 0.12) * (1 - sm((u - 0.75) / 0.25))
            cx, cy = FX + FW / 2, FY + FH / 2
            m = lay.transform(lay.size, Image.AFFINE, (1 / sc, 0, cx - cx / sc, 0, 1 / sc, cy - cy / sc), resample=Image.BILINEAR)
            img.alpha_composite(fade(m, al))
    for a, b, lay in CAPS:
        if a <= t < b: img.alpha_composite(lay, (0, FY + FH + 40 - 20))
    j = int((t - T_STK) * FPS)
    if 0 <= j < len(STK): img.alpha_composite(Image.open(STK[j]).convert("RGBA"), (160, FY + FH + 150))
    enc.stdin.write(img.convert("RGB").tobytes()); i += 1
enc.stdin.close(); enc.wait(); proc.wait()
if AUDIO:   # narração já mixada com o jogo
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", AUDIO, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(m[m.rfind("{"):m.rfind("}") + 1])
    af = f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "tmp/painel_video.mp4", "-i", AUDIO, "-map", "0:v", "-map", "1:a", "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", OUT], check=True)
    print("ok", OUT, i, "quadros (com narração)"); sys.exit(0)
# som do jogo a -14 LUFS
m = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(S), "-t", str(D), "-i", "src/gameplay.mp4", "-vn", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
m = json.loads(m[m.rfind("{"):m.rfind("}") + 1])
af = f"afade=t=in:st=0:d=0.1,afade=t=out:st={D - 0.5}:d=0.5,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "tmp/painel_video.mp4", "-ss", str(S), "-t", str(D), "-i", "src/gameplay.mp4", "-map", "0:v", "-map", "1:a",
                "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", OUT], check=True)
print("ok", OUT, i, "quadros")
