"""Teste estilo LOUSA (referência: Reel "Emulador de Xbox"): quadro-negro de giz, cenas no quadro verde com monitor,
transição de papel desenhando o monitor, etiqueta amarela e legenda na faixa de terra. Quadros em ./frames2."""
import math, os, sys, json, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

W, H, FPS, DUR = 1080, 1920, 30, 28.4
T = "thumbs/"; OUT = "frames2"; os.makedirs(OUT, exist_ok=True)
LIL = "/home/user/fonts/LilitaOne-Regular.ttf"; CHALK = "/home/user/fonts/CabinSketch-Bold.ttf"; MONT = "/home/user/fonts/Montserrat.ttf"
def mont(sz, w="ExtraBold"):
    f = ImageFont.truetype(MONT, sz); f.set_variation_by_name(w); return f
rng = np.random.default_rng(3)

# ---------- texturas ----------
def noise(h, w, scale, amp):
    small = rng.standard_normal((h // scale + 2, w // scale + 2))
    im = Image.fromarray(((small - small.min()) / (np.ptp(small)) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return (np.asarray(im, dtype=np.float32) / 255 - 0.5) * amp
def textured(color, h=H, w=W, grains=((3, 26), (40, 30))):
    a = np.zeros((h, w, 3), np.float32) + np.array(color, np.float32)
    for sc, amp in grains: a += noise(h, w, sc, amp)[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
GREEN = textured((38, 128, 44), grains=((2, 34), (9, 18), (60, 26)))
GROUND_Y = 1385
DIRT = textured((128, 86, 50), h=H - GROUND_Y, grains=((2, 40), (14, 22)))
CHALKB = textured((36, 66, 52), grains=((2, 10), (30, 18), (120, 22)))
PAPER = textured((240, 233, 216), grains=((2, 8), (80, 10)))
def vignette(img, k=0.45):
    yy, xx = np.mgrid[0:H, 0:W]; d = np.sqrt(((xx - W / 2) / (W * 0.7)) ** 2 + ((yy - H / 2) / (H * 0.7)) ** 2)
    m = np.clip(1 - k * d ** 2, 0, 1)[..., None]
    return Image.fromarray((np.asarray(img, np.float32) * m).astype(np.uint8))
GREEN = vignette(GREEN, 0.35); CHALKB = vignette(CHALKB, 0.5)
BOARD = GREEN.copy(); BOARD.paste(DIRT, (0, GROUND_Y))
ImageDraw.Draw(BOARD).rectangle([0, GROUND_Y - 6, W, GROUND_Y + 4], fill=(70, 44, 22))
CHALK_TEX = Image.fromarray((np.clip(0.86 + noise(H, W, 2, 0.9), 0, 1) * 255).astype(np.uint8))  # máscara de giz

# ---------- imagens ----------
MAPB = Image.open(T + "gGvMUEJjKCs.jpg").convert("RGB").crop((700, 0, 1200, 720))
MAP = MAPB.resize((2000, 2880), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2)); MS = 4
SX0, SY0, SX1, SY1 = 110, 470, 970, 1010          # tela do monitor
SW, SH = SX1 - SX0, SY1 - SY0
def fit(path, box):
    im = Image.open(path).convert("RGB").crop(box); r = max(SW / im.width, SH / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x0 = (im.width - SW) // 2; y0 = (im.height - SH) // 2; return ImageEnhance.Contrast(im.crop((x0, y0, x0 + SW, y0 + SH))).enhance(1.06)
CAR1 = fit(T + "MBn2O8b2T2Y.jpg", (520, 90, 1280, 690)); CAR2 = fit(T + "Hb6ZJf7Bpg4.jpg", (0, 48, 480, 312))
PIN1, PIN2 = (440, 265), (320, 270)

# ---------- utilidades ----------
def clamp(x): return max(0.0, min(1.0, x))
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)
def back(x):
    x = clamp(x); c1, c3 = 1.70158, 2.70158; return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def lerp(a, b, k): return a + (b - a) * k

def cartoon_title(img, lines, t0, t, y0=120, gap=10):
    """Título estilo desenho: amarelo/creme, contorno marrom escuro, sombra, entra com pulo e balança de leve."""
    if t < t0: return
    k = back((t - t0) / 0.45); y = y0
    for i, (txt, size, col) in enumerate(lines):
        f = ImageFont.truetype(LIL, size)
        lay = Image.new("RGBA", (W, size + 60)); d = ImageDraw.Draw(lay)
        tw = d.textlength(txt, font=f); x = (W - tw) / 2
        d.text((x + 7, 14), txt, font=f, fill=(40, 22, 6, 200), stroke_width=12, stroke_fill=(40, 22, 6, 200))
        d.text((x, 6), txt, font=f, fill=col, stroke_width=10, stroke_fill=(58, 32, 10))
        ang = math.sin(t * 2.1 + i) * 1.2 - 1.5 + i * 2.5
        sc = max(0.05, k * (1 if i == 0 else back((t - t0 - 0.12) / 0.45)))
        lay = lay.rotate(ang, resample=Image.BICUBIC, center=(W / 2, (size + 60) / 2))
        lay = lay.resize((max(1, int(W * sc)), max(1, int((size + 60) * sc))), Image.BICUBIC)
        img.alpha_composite(lay, (int((W - lay.width) / 2), int(y + (size + 60) * (1 - sc) / 2)))
        y += size + gap

def sparkles(img, t, pts):
    d = ImageDraw.Draw(img)
    for i, (x, y) in enumerate(pts):
        s = 16 + 8 * math.sin(t * 3 + i * 1.7)
        d.polygon([(x, y - s), (x + s * 0.28, y - s * 0.28), (x + s, y), (x + s * 0.28, y + s * 0.28),
                   (x, y + s), (x - s * 0.28, y + s * 0.28), (x - s, y), (x - s * 0.28, y - s * 0.28)], fill=(255, 214, 80))

def monitor(img, content, t_draw=None):
    d = ImageDraw.Draw(img)
    d.rectangle([W / 2 - 22, SY1 + 20, W / 2 + 22, GROUND_Y + 10], fill=(48, 48, 52))
    d.rounded_rectangle([SX0 - 34, SY0 - 34, SX1 + 34, SY1 + 34], 34, fill=(36, 36, 40), outline=(18, 18, 20), width=6)
    img.paste(content, (SX0, SY0))
    d.rectangle([SX0, SY0, SX1, SY1], outline=(18, 18, 20), width=4)

def map_view(cx, cy, wbase):
    """Recorte do mapa centrado em (cx, cy) do mapa base, mostrando 'wbase' pixels de largura."""
    s = SW / wbase / MS; a = 1 / s
    c = cx * MS - (SW / 2) / s; f = cy * MS - (SH / 2) / s
    return MAP.transform((SW, SH), Image.AFFINE, (a, 0, c, 0, a, f), resample=Image.BILINEAR, fillcolor=(18, 120, 170)), (cx, cy, wbase)
def to_mon(p, view):
    cx, cy, wb = view; s = SW / wb
    return SX0 + SW / 2 + (p[0] - cx) * s, SY0 + SH / 2 + (p[1] - cy) * s

def pin(img, xy, t0, t, num):
    if t < t0: return
    k = back((t - t0) / 0.45); x, y = xy; y -= (1 - k) * 200; d = ImageDraw.Draw(img)
    d.ellipse([x - 40, y - 104, x + 40, y - 24], fill=(232, 30, 30), outline=(255, 255, 255), width=5)
    d.polygon([(x - 26, y - 44), (x + 26, y - 44), (x, y)], fill=(232, 30, 30))
    f = ImageFont.truetype(LIL, 50); tw = d.textlength(str(num), font=f); d.text((x - tw / 2, y - 98), str(num), font=f, fill="white")

def chalk_ellipse(img, cx, cy, rx, ry, t0, t, col=(255, 222, 70)):
    if t < t0: return
    k = ease((t - t0) / 0.6); d = ImageDraw.Draw(img); n = int(80 * k)
    for rep in range(2):
        pts = []
        for i in range(n + 1):
            a = -math.pi / 2 + 2.15 * math.pi * i / 80 + rep * 0.15
            j = 1 + 0.04 * math.sin(i * 1.7 + rep * 3)
            pts.append((cx + rx * j * math.cos(a), cy + ry * j * math.sin(a)))
        if len(pts) > 1: d.line(pts, fill=col, width=7 - rep * 2, joint="curve")

def badge(img, xy, r, lines, t0, t, ring=(255, 255, 255), fill=(30, 92, 40)):
    if t < t0: return
    k = back((t - t0) / 0.4); rr = r * k; x, y = xy
    if rr < 24: return
    lay = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(lay)
    d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=fill, outline=ring, width=max(1, int(9 * k)))
    d.ellipse([x - rr + 16, y - rr + 16, x + rr - 16, y + rr - 16], outline=ring + (120,), width=max(1, int(3 * k)))
    tot = sum(sz * 1.02 for _, sz in lines) * k; yy = y - tot / 2
    for i, (txt, sz) in enumerate(lines):
        f = ImageFont.truetype(LIL, max(8, int(sz * k))); tw = d.textlength(txt, font=f)
        d.text((x - tw / 2, yy), txt, font=f, fill="white"); yy += sz * 1.02 * k
    img.alpha_composite(lay)

def chip(img, txt):
    d = ImageDraw.Draw(img); f = mont(30, "ExtraBold"); tw = d.textlength(txt, font=f)
    d.rounded_rectangle([40, 1398, 40 + tw + 44, 1446], 12, fill=(250, 204, 60))
    d.text((62, 1404), txt, font=f, fill=(40, 28, 6))

# ---------- quadro-negro (gancho) ----------
def chalk_text(lay_d, xy, txt, font, col):
    lay_d.text(xy, txt, font=font, fill=col)
def chalk_scene(t):
    img = CHALKB.convert("RGBA"); lay = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(lay)
    fbig = ImageFont.truetype(CHALK, 150); fmid = ImageFont.truetype(CHALK, 84); fsm = ImageFont.truetype(CHALK, 70)
    def ctr(y, txt, f, col):
        tw = d.textlength(txt, font=f); d.text(((W - tw) / 2, y), txt, font=f, fill=col)
    ctr(330, "SUPERCARROS", ImageFont.truetype(CHALK, 128), (235, 238, 230))
    ctr(500, "escondidos no", fsm, (250, 214, 90))
    ctr(590, "GTA 6", fbig, (235, 238, 230))
    d.line([(250, 790), (830, 778)], fill=(250, 214, 90), width=8); d.line([(270, 806), (812, 796)], fill=(250, 214, 90), width=4)
    # desenho de carro esportivo em giz
    cx, cy = 470, 1080; body = [(cx - 300, cy + 40), (cx - 290, cy - 10), (cx - 170, cy - 40), (cx - 80, cy - 105), (cx + 90, cy - 110),
                                (cx + 190, cy - 45), (cx + 300, cy - 25), (cx + 310, cy + 40)]
    d.line(body + [body[0]], fill=(235, 238, 230), width=9, joint="curve")
    d.line([(cx - 70, cy - 95), (cx + 80, cy - 98), (cx + 160, cy - 45), (cx - 150, cy - 40), (cx - 70, cy - 95)], fill=(235, 238, 230), width=6)
    for wx in (cx - 170, cx + 190):
        d.ellipse([wx - 58, cy - 10, wx + 58, cy + 106], outline=(235, 238, 230), width=9); d.ellipse([wx - 20, cy + 28, wx + 20, cy + 68], outline=(235, 238, 230), width=6)
    ctr(980, "", fsm, "white")
    fq = ImageFont.truetype(CHALK, 260); d.text((845, 910), "?", font=fq, fill=(250, 214, 90))
    # revela da esquerda para a direita e de cima para baixo, como giz sendo escrito
    reveal = Image.new("L", (W, H), 0); rd = ImageDraw.Draw(reveal)
    for (y0, y1, ts) in ((300, 480, 0.0), (480, 580, 0.45), (580, 820, 0.7), (900, 1230, 1.2)):
        k = ease((t - ts) / 0.8); rd.rectangle([0, y0, int(W * k), y1], fill=255)
    a = ImageChops.multiply(lay.split()[3], reveal); a = ImageChops.multiply(a, CHALK_TEX)
    lay.putalpha(a); img.alpha_composite(lay); return img

# ---------- papel (transição) ----------
def paper_scene(k):
    img = PAPER.convert("RGBA"); d = ImageDraw.Draw(img)
    per = [(SX0 - 34, SY0 - 34), (SX1 + 34, SY0 - 34), (SX1 + 34, SY1 + 34), (SX0 - 34, SY1 + 34), (SX0 - 34, SY0 - 34)]
    L = [math.dist(per[i], per[i + 1]) for i in range(4)]; tot = sum(L)
    def draw(frac, col, w):
        left = tot * frac; pts = [per[0]]
        for i in range(4):
            if left <= 0: break
            seg = min(left, L[i]); r = seg / L[i]
            pts.append((lerp(per[i][0], per[i + 1][0], r), lerp(per[i][1], per[i + 1][1], r))); left -= seg
        if len(pts) > 1: d.line(pts, fill=col, width=w)
    draw(ease(k / 0.45), (150, 150, 150), 3)
    if k > 0.45:
        draw(ease((k - 0.45) / 0.4), (20, 20, 20), 10)
        kk = ease((k - 0.55) / 0.35); d.line([(W / 2 - 14, SY1 + 34), (W / 2 - 14, SY1 + 34 + (GROUND_Y - SY1) * kk)], fill=(20, 20, 20), width=8)
        d.line([(W / 2 + 14, SY1 + 34), (W / 2 + 14, SY1 + 34 + (GROUND_Y - SY1) * kk)], fill=(20, 20, 20), width=8)
    d.line([(0, GROUND_Y), (W * ease(k / 0.6), GROUND_Y)], fill=(60, 60, 60), width=5)
    return img

# ---------- legendas (palavra falada em amarelo) ----------
VOZ = {"l0": 0.25, "l1": 5.5, "l2": 13.7, "l3": 22.1, "l4": 24.6}
_W = json.load(open("voz/words.json")); WORDS = []
for kk, off in VOZ.items():
    for w, a, b in _W[kk]: WORDS.append((w.replace("seis!", "6!").replace("seis.", "6.").replace("seis", "6"), off + a, off + b, kk))
GROUPS = []; cur = []
for wd in WORDS:
    glue = cur and cur[-1][0] == "GTA"
    if cur and not glue and (len(cur) >= 3 or sum(len(x[0]) + 1 for x in cur) + len(wd[0]) > 19 or cur[-1][3] != wd[3] or cur[-1][0][-1] in ".,:?!"):
        GROUPS.append(cur); cur = []
    cur.append(wd)
GROUPS.append(cur)
F_CAP = mont(66, "Black")
def captions(img, t):
    for gi, g in enumerate(GROUPS):
        start = g[0][1]; end = g[-1][2] + 0.25
        if gi + 1 < len(GROUPS) and GROUPS[gi + 1][0][3] == g[0][3]: end = min(end + 0.2, GROUPS[gi + 1][0][1])
        if not (start <= t < end): continue
        d = ImageDraw.Draw(img)
        cur_i = max([i for i, (w, a, b, _) in enumerate(g) if a <= t] or [0])
        ws = [w for w, *_ in g]; widths = [d.textlength(w, font=F_CAP) for w in ws]; sp = 20
        x = 44; y = 1462
        if x + sum(widths) + sp * (len(ws) - 1) > W - 40: x = (W - (sum(widths) + sp * (len(ws) - 1))) / 2
        for i, w in enumerate(ws):
            col = (255, 214, 60) if i == cur_i else (255, 255, 255)
            d.text((x, y), w, font=F_CAP, fill=col, stroke_width=6, stroke_fill=(30, 18, 6)); x += widths[i] + sp

STK = "/home/user/gta-shorts/stk/"
def sticker(img, t, t0):
    i = int((t - t0) * FPS)
    if 0 <= i < 168:
        img.alpha_composite(Image.open(f"{STK}s{i:03d}.png").convert("RGBA"), (160, 110))

SP = [(90, 260), (990, 330), (70, 1150), (1010, 1100)]
def board_scene(t, title, tag, car, pinp, num, ts, t_map, extras):
    img = BOARD.convert("RGBA")
    sparkles(img, t, SP)
    cartoon_title(img, title, ts + 0.05, t, y0=110)
    if t < t_map:
        z = 1 + 0.05 * (t - ts); im = car.resize((int(SW * z), int(SH * z)), Image.BILINEAR)
        content = im.crop(((im.width - SW) // 2, (im.height - SH) // 2, (im.width - SW) // 2 + SW, (im.height - SH) // 2 + SH))
        view = None
    else:
        k = ease((t - t_map) / 1.6)
        wb = lerp(330, 170, k); cx = min(lerp(300, pinp[0] - 5, k), 500 - wb / 2 - 2); cy = lerp(330, pinp[1] - 30, k)
        content, view = map_view(cx, cy, wb)
        if t - t_map < 0.25:   # corte suave da foto para o mapa
            a = (t - t_map) / 0.25; content = Image.blend(car, content, a)
    monitor(img, content)
    if view:
        px, py = to_mon(pinp, view); pin(img, (px, py), t_map + 0.35, t, num)
        chalk_ellipse(img, px, py - 4, 92, 46, t_map + 1.0, t)
    for e in extras: e(img, t)
    chip(img, tag); return img

def outro(t, ts):
    img = BOARD.convert("RGBA"); sparkles(img, t, SP)
    cartoon_title(img, [("QUAL VOCÊ", 104, (255, 214, 90)), ("PEGA PRIMEIRO?", 92, (255, 245, 225))], ts + 0.05, t, y0=430)
    d = ImageDraw.Draw(img)
    for i, (car, x) in enumerate(((CAR1, 70), (CAR2, 560))):
        k = back((t - ts - 0.3 - i * 0.15) / 0.45)
        if k <= 0.12: continue
        w, h = int(450 * k), int(282 * k)
        thumb = car.resize((max(1, w), max(1, h)), Image.LANCZOS)
        cx = x + 225; cy = 900
        d.rounded_rectangle([cx - w / 2 - 18, cy - h / 2 - 18, cx + w / 2 + 18, cy + h / 2 + 18], 22, fill=(36, 36, 40))
        img.paste(thumb, (int(cx - w / 2), int(cy - h / 2)))
        d.rectangle([cx - 14, cy + h / 2 + 18, cx + 14, GROUND_Y], fill=(48, 48, 52))
        f = ImageFont.truetype(LIL, int(64 * k)); d.ellipse([cx - 44 * k, cy - h / 2 - 60 * k, cx + 44 * k, cy - h / 2 + 28 * k], fill=(232, 30, 30), outline="white", width=4)
        tw = d.textlength(str(i + 1), font=f); d.text((cx - tw / 2, cy - h / 2 - 56 * k), str(i + 1), font=f, fill="white")
    badge(img, (W / 2, 1230), 120, [("COMENTA!", 50)], ts + 1.2, t, ring=(255, 214, 90), fill=(30, 92, 40))
    sticker(img, t, ts + 0.3)
    chip(img, "• E VOCÊ? · JOGATINA FÁCIL"); return img

def frame(i):
    t = i / FPS
    if t < 4.4: img = chalk_scene(t)
    elif t < 5.3: img = paper_scene((t - 4.4) / 0.9)
    elif t < 12.6:
        img = board_scene(t, [("PROGEN EMERUS", 104, (255, 214, 90)), ("ROYAL RUBY", 74, (255, 245, 225))],
                          "• CARRO 1 · VESPUCCI ISLAND", CAR1, PIN1, 1, 5.3, 8.0,
                          [lambda im, tt: badge(im, (870, 1160), 130, [("GARAGEM", 40), ("DA", 34), ("ENTRADA", 40)], 10.4, tt)])
    elif t < 13.5: img = paper_scene((t - 12.6) / 0.9)
    elif t < 21.0:
        img = board_scene(t, [("PEGASSI INFERNUS", 96, (255, 214, 90)), ("DELEGACIA DE CROSSTOWN", 58, (255, 245, 225))],
                          "• CARRO 2 · VICE CITY", CAR2, PIN2, 2, 13.5, 16.0,
                          [lambda im, tt: badge(im, (870, 1160), 130, [("7º", 84), ("ANDAR", 44)], 17.2, tt),
                           lambda im, tt: badge(im, (210, 1160), 130, [("TEM", 46), ("RASTRE-", 40), ("ADOR", 40)], 19.6, tt, ring=(255, 90, 80), fill=(120, 26, 22))])
    elif t < 21.9: img = paper_scene((t - 21.0) / 0.9)
    else: img = outro(t, 21.9)
    if not (4.4 <= t < 5.3 or 12.6 <= t < 13.5 or 21.0 <= t < 21.9) or True: captions(img, t)
    img.convert("RGB").save(f"{OUT}/{i:04d}.jpg", quality=92)

if __name__ == "__main__":
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (0, int(DUR * FPS))
    for i in range(a, b): frame(i)
