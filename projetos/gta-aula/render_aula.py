"""'Aula de GTA' — estilo lousa com identidade própria: quadro-negro com moldura de madeira e canaleta de giz,
polaroids com fita, mapa preso com tachinha, seta e círculo de giz, post-its, apagador como transição, final 'prova'."""
import math, os, sys, json, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops

W, H, FPS, DUR = 1080, 1920, 30, 29.8
T = "/home/user/gta-mapa/thumbs/"; OUT = "frames"; os.makedirs(OUT, exist_ok=True)
CH = "/home/user/fonts/CabinSketch-Bold.ttf"; MK = "/home/user/fonts/PermanentMarker-Regular.ttf"; MONT = "/home/user/fonts/Montserrat.ttf"
def mont(sz, w="Black"):
    f = ImageFont.truetype(MONT, sz); f.set_variation_by_name(w); return f
rng = np.random.default_rng(5)
def clamp(x): return max(0.0, min(1.0, x))
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)
def back(x):
    x = clamp(x); c1, c3 = 1.70158, 2.70158; return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def lerp(a, b, k): return a + (b - a) * k

# ---------- cenário: lousa, moldura e canaleta ----------
def noise(h, w, sc, amp):
    s = rng.standard_normal((h // sc + 2, w // sc + 2))
    im = Image.fromarray(((s - s.min()) / np.ptp(s) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return (np.asarray(im, np.float32) / 255 - 0.5) * amp
def tex(col, h, w, gr):
    a = np.zeros((h, w, 3), np.float32) + np.array(col, np.float32)
    for sc, amp in gr: a += noise(h, w, sc, amp)[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
BX0, BY0, BX1, BY1 = 36, 56, 1044, 1648
SLATE = tex((44, 50, 54), BY1 - BY0, BX1 - BX0, ((2, 10), (25, 14), (140, 26)))
# marcas antigas de giz apagado
sm = Image.new("L", SLATE.size, 0); sd = ImageDraw.Draw(sm)
for _ in range(14):
    x, y = rng.integers(0, SLATE.width), rng.integers(0, SLATE.height); r = rng.integers(80, 260)
    sd.ellipse([x - r, y - r * 0.4, x + r, y + r * 0.4], fill=int(rng.integers(10, 26)))
SLATE = Image.composite(Image.new("RGB", SLATE.size, (150, 155, 158)), SLATE, sm.filter(ImageFilter.GaussianBlur(40)))
WOOD = tex((120, 74, 38), H, W, ((1, 18), (4, 24), (30, 30)))
# veios da madeira
wd = np.asarray(WOOD, np.float32); yy = np.arange(H)[:, None]; wd += (np.sin(yy / 7 + noise(H, W, 40, 6)) * 9)[..., None]; WOOD = Image.fromarray(np.clip(wd, 0, 255).astype(np.uint8))
BASE = WOOD.copy(); BASE.paste(SLATE, (BX0, BY0))
d0 = ImageDraw.Draw(BASE)
d0.rectangle([BX0 - 4, BY0 - 4, BX1 + 4, BY1 + 4], outline=(70, 40, 18), width=6)
# canaleta com giz e apagador
d0.rectangle([0, BY1 + 30, W, BY1 + 70], fill=(96, 58, 28)); d0.rectangle([0, BY1 + 70, W, BY1 + 82], fill=(60, 34, 14))
for x, col in ((150, (245, 245, 240)), (230, (250, 220, 90)), (300, (240, 150, 160))):
    d0.rounded_rectangle([x, BY1 + 40, x + 66, BY1 + 60], 8, fill=col)
d0.rounded_rectangle([760, BY1 + 18, 960, BY1 + 66], 10, fill=(150, 96, 50)); d0.rectangle([760, BY1 + 50, 960, BY1 + 66], fill=(70, 70, 76))
BASE = BASE.convert("RGBA")
CHALKMASK = Image.fromarray((np.clip(0.84 + noise(H, W, 2, 0.9), 0, 1) * 255).astype(np.uint8))

# ---------- imagens ----------
MAPB = Image.open(T + "gGvMUEJjKCs.jpg").convert("RGB").crop((700, 0, 1200, 720))
MAP = MAPB.resize((2000, 2880), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
def map_crop(p, wb=170, size=(620, 440)):
    cx = min(p[0] - 5, 500 - wb / 2 - 2); cy = p[1] - 20; hb = wb * size[1] / size[0]
    box = [int((cx - wb / 2) * 4), int((cy - hb / 2) * 4), int((cx + wb / 2) * 4), int((cy + hb / 2) * 4)]
    im = MAP.crop(box).resize(size, Image.LANCZOS)
    px = (p[0] - (cx - wb / 2)) / wb * size[0]; py = (p[1] - (cy - hb / 2)) / hb * size[1]
    return im, (px, py)
def photo(path, box, size):
    im = Image.open(path).convert("RGB").crop(box); r = max(size[0] / im.width, size[1] / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x0 = (im.width - size[0]) // 2; y0 = (im.height - size[1]) // 2
    return ImageEnhance.Contrast(im.crop((x0, y0, x0 + size[0], y0 + size[1]))).enhance(1.06)
CAR1 = photo(T + "MBn2O8b2T2Y.jpg", (520, 90, 1280, 690), (600, 430)); CAR2 = photo(T + "Hb6ZJf7Bpg4.jpg", (0, 48, 480, 312), (600, 430))
MAP1, MP1 = map_crop((440, 265)); MAP2, MP2 = map_crop((320, 270))

def polaroid(im, caption):
    pw, ph = im.width + 40, im.height + 120
    p = Image.new("RGBA", (pw + 40, ph + 40)); d = ImageDraw.Draw(p)
    d.rectangle([24, 26, pw + 24, ph + 26], fill=(0, 0, 0, 90))            # sombra
    d.rectangle([16, 16, pw + 16, ph + 16], fill=(246, 244, 238))
    p.paste(im, (36, 36))
    f = ImageFont.truetype(MK, 50); tw = d.textlength(caption, font=f); d.text(((pw + 32 - tw) / 2, im.height + 56), caption, font=f, fill=(40, 40, 46))
    return p.filter(ImageFilter.SMOOTH_MORE) if False else p
def tape(d, x, y, ang):
    w, h = 130, 40; c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    pts = [(x + dx * c - dy * s, y + dx * s + dy * c) for dx, dy in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2))]
    d.polygon(pts, fill=(240, 232, 200, 190))
def place(img, lay, cx, cy, ang, k):
    if k <= 0.05: return
    r = lay.rotate(ang, resample=Image.BICUBIC, expand=True)
    r = r.resize((max(1, int(r.width * k)), max(1, int(r.height * k))), Image.BICUBIC)
    img.alpha_composite(r, (int(cx - r.width / 2), int(cy - r.height / 2)))
POL1 = polaroid(CAR1, "Emerus Royal Ruby"); POL2 = polaroid(CAR2, "Pegassi Infernus")
MAPP1 = polaroid(MAP1, "Vespucci Island"); MAPP2 = polaroid(MAP2, "Crosstown, Vice City")

# ---------- giz ----------
def chalk_layer(draw_fn, reveal_rects, t):
    lay = Image.new("RGBA", (W, H)); draw_fn(ImageDraw.Draw(lay))
    m = Image.new("L", (W, H), 0); md = ImageDraw.Draw(m)
    for (x0, y0, x1, y1, ts, dur) in reveal_rects:
        k = ease((t - ts) / dur); md.rectangle([x0, y0, x0 + (x1 - x0) * k, y1], fill=255)
    a = ImageChops.multiply(ImageChops.multiply(lay.split()[3], m), CHALKMASK); lay.putalpha(a); return lay
def ctext(d, y, txt, font, col, x=None):
    tw = d.textlength(txt, font=font); d.text(((W - tw) / 2 if x is None else x, y), txt, font=font, fill=col)
def chalk_arrow(img, p0, p1, t0, t, col=(250, 222, 90)):
    if t < t0: return
    k = ease((t - t0) / 0.6); d = ImageDraw.Draw(img)
    mx, my = (p0[0] + p1[0]) / 2 + 80, (p0[1] + p1[1]) / 2 - 40
    pts = []
    for i in range(int(40 * k) + 1):
        u = i / 40; pts.append(((1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * mx + u * u * p1[0], (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * my + u * u * p1[1]))
    if len(pts) > 1:
        d.line(pts, fill=(25, 25, 28), width=20, joint="curve"); d.line(pts, fill=col, width=12, joint="curve")
    if k >= 1:
        ang = math.atan2(p1[1] - pts[-3][1], p1[0] - pts[-3][0])
        for da in (2.6, -2.6):
            q = (p1[0] + 52 * math.cos(ang + da), p1[1] + 52 * math.sin(ang + da))
            d.line([p1, q], fill=(25, 25, 28), width=20); d.line([p1, q], fill=col, width=12)
def chalk_circle(img, cx, cy, rx, ry, t0, t, col=(250, 222, 90)):
    if t < t0: return
    k = ease((t - t0) / 0.6); d = ImageDraw.Draw(img)
    for rep in range(2):
        pts = [(cx + rx * (1 + 0.05 * math.sin(i + rep)) * math.cos(-1.6 + 2.2 * math.pi * i / 70 + rep * .2),
                cy + ry * (1 + 0.05 * math.sin(i + rep)) * math.sin(-1.6 + 2.2 * math.pi * i / 70 + rep * .2)) for i in range(int(70 * k) + 1)]
        if len(pts) > 1:
            if rep == 0: d.line(pts, fill=(25, 25, 28), width=17, joint="curve")
            d.line(pts, fill=col, width=10 - 3 * rep, joint="curve")
def postit(img, xy, lines, t0, t, col=(252, 226, 92), ang=-5, ink=(40, 40, 46)):
    if t < t0: return
    k = back((t - t0) / 0.4); w = 300
    p = Image.new("RGBA", (w + 30, w + 30)); d = ImageDraw.Draw(p)
    d.rectangle([20, 22, w + 22, w + 24], fill=(0, 0, 0, 80)); d.rectangle([10, 10, w + 10, w + 10], fill=col)
    d.rectangle([10, 10, w + 10, 50], fill=tuple(max(0, c - 22) for c in col))
    tot = sum(s for _, s in lines) * 1.05; y = 10 + (w - tot) / 2 + 14
    for txt, s in lines:
        f = ImageFont.truetype(MK, s); tw = d.textlength(txt, font=f); d.text(((w + 20 - tw) / 2, y), txt, font=f, fill=ink); y += s * 1.05
    place(img, p, xy[0], xy[1], ang, k)
def pushpin(img, x, y):
    d = ImageDraw.Draw(img); d.ellipse([x - 22, y - 22, x + 22, y + 22], fill=(210, 30, 30), outline=(120, 10, 10), width=3); d.ellipse([x - 9, y - 12, x + 3, y], fill=(255, 140, 140))
def red_pin(img, x, y, num, t0, t):
    if t < t0: return
    k = back((t - t0) / 0.4); y -= (1 - k) * 120; d = ImageDraw.Draw(img)
    d.ellipse([x - 30, y - 80, x + 30, y - 20], fill=(232, 30, 30), outline="white", width=4); d.polygon([(x - 20, y - 34), (x + 20, y - 34), (x, y)], fill=(232, 30, 30))
    f = ImageFont.truetype(MK, 40); tw = d.textlength(str(num), font=f); d.text((x - tw / 2, y - 82), str(num), font=f, fill="white")

# ---------- legendas ----------
VOZ = {"a0": 0.3, "a1": 6.2, "a2": 14.6, "a3": 23.4, "a4": 26.9}
_W = json.load(open("voz/words.json")); WORDS = []
for kk, off in VOZ.items():
    for w, a, b in _W[kk]: WORDS.append((w.replace("seis:", "6:").replace("seis", "6"), off + a, off + b, kk))
GROUPS = []; cur = []
for wd in WORDS:
    glue = cur and cur[-1][0] == "GTA"
    if cur and not glue and (len(cur) >= 3 or sum(len(x[0]) + 1 for x in cur) + len(wd[0]) > 18 or cur[-1][3] != wd[3] or cur[-1][0][-1] in ".,:?!"):
        GROUPS.append(cur); cur = []
    cur.append(wd)
GROUPS.append(cur)
F_CAP = mont(64)
def captions(img, t):
    for gi, g in enumerate(GROUPS):
        s0 = g[0][1]; e = g[-1][2] + 0.25
        if gi + 1 < len(GROUPS) and GROUPS[gi + 1][0][3] == g[0][3]: e = min(e + 0.2, GROUPS[gi + 1][0][1])
        if not (s0 <= t < e): continue
        d = ImageDraw.Draw(img); ws = [w for w, *_ in g]
        ci = max([i for i, (w, a, b, _) in enumerate(g) if a <= t] or [0])
        wid = [d.textlength(w, font=F_CAP) for w in ws]; sp = 20; x = (W - (sum(wid) + sp * (len(ws) - 1))) / 2; y = 1500
        for i, w in enumerate(ws):
            d.text((x, y), w, font=F_CAP, fill=(250, 222, 90) if i == ci else (246, 246, 242), stroke_width=7, stroke_fill=(20, 22, 24)); x += wid[i] + sp

STK = "/home/user/gta-shorts/stk/"
def sticker(img, t, t0):
    i = int((t - t0) * FPS)
    if 0 <= i < 168: img.alpha_composite(Image.open(f"{STK}s{i:03d}.png").convert("RGBA"), (160, 110))

# ---------- cenas ----------
def header(img, t, ts, aula, title, sub):
    def dr(d):
        d.text((80, 96), aula, font=ImageFont.truetype(CH, 50), fill=(250, 222, 90))
        ctext(d, 160, title, ImageFont.truetype(CH, 104), (244, 244, 240))
        ctext(d, 286, sub, ImageFont.truetype(CH, 58), (170, 220, 250))
        d.line([(170, 360), (910, 352)], fill=(240, 150, 160), width=7)
    img.alpha_composite(chalk_layer(dr, [(60, 90, 500, 160, ts, 0.4), (60, 160, 1030, 290, ts + 0.2, 0.7), (60, 290, 1030, 380, ts + 0.6, 0.6)], t))

def intro(t):
    img = BASE.copy()
    def dr(d):
        ctext(d, 260, "AULA DE", ImageFont.truetype(CH, 96), (250, 222, 90))
        ctext(d, 370, "GTA 6", ImageFont.truetype(CH, 230), (246, 246, 242))
        ctext(d, 640, "2 supercarros escondidos", ImageFont.truetype(CH, 62), (170, 220, 250))
        ctext(d, 720, "e onde eles ficam", ImageFont.truetype(CH, 62), (170, 220, 250))
        cx, cy = 540, 1080
        body = [(cx - 300, cy + 40), (cx - 290, cy - 10), (cx - 170, cy - 40), (cx - 80, cy - 105), (cx + 90, cy - 110), (cx + 190, cy - 45), (cx + 300, cy - 25), (cx + 310, cy + 40)]
        d.line(body + [body[0]], fill=(246, 246, 242), width=9, joint="curve")
        for wx in (cx - 170, cx + 190): d.ellipse([wx - 58, cy - 10, wx + 58, cy + 106], outline=(246, 246, 242), width=9)
        d.text((870, 900), "?", font=ImageFont.truetype(CH, 240), fill=(240, 150, 160))
        d.text((90, 1270), "Lição 01", font=ImageFont.truetype(CH, 54), fill=(250, 222, 90))
    img.alpha_composite(chalk_layer(dr, [(40, 250, 1040, 370, 0.0, 0.5), (40, 370, 1040, 620, 0.35, 0.8), (40, 630, 1040, 800, 1.1, 0.9),
                                         (40, 880, 1040, 1230, 1.9, 1.0), (40, 1260, 600, 1340, 2.8, 0.4)], t))
    return img

def car_scene(t, ts, aula, title, sub, pol, mapp, mp, num, t_map, notes):
    img = BASE.copy(); header(img, t, ts, aula, title, sub)
    k_in = back((t - ts - 0.2) / 0.5)
    if t < t_map: place(img, pol, 540, 830, -3, k_in)                           # polaroid grande no centro
    else:
        k = ease((t - t_map) / 0.6)
        place(img, pol.resize((int(pol.width * lerp(1, 0.62, k)), int(pol.height * lerp(1, 0.62, k)))), lerp(540, 290, k), lerp(830, 640, k), lerp(-3, -7, k), 1)
        km = back((t - t_map - 0.15) / 0.5)
        mx, my = 600, 1060
        place(img, mapp, mx, my, 3, km * 0.86)
        if km >= 0.99:
            pushpin(img, mx + 4, my - mapp.height * 0.86 / 2 + 12)
            # pino vermelho no ponto exato dentro do mapa
            s = 0.86; ox = mx - mapp.width * s / 2; oy = my - mapp.height * s / 2
            px, py = ox + (mp[0] + 36) * s, oy + (mp[1] + 36) * s
            red_pin(img, px, py, num, t_map + 0.6, t)
            chalk_circle(img, px, py - 6, 70, 36, t_map + 1.1, t)
            chalk_arrow(img, (520, 690), (px - 60, py - 70), t_map + 0.9, t)
    for n in notes: n(img, t)
    return img

def eraser(prev, nxt, k):
    """Apagador atravessando a lousa: à esquerda do apagador já é a cena nova, com pó de giz."""
    x = lerp(-260, W + 260, ease(k)); base = nxt.copy()
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).rectangle([min(max(int(x), 0), W), 0, W, H], fill=255)
    base.paste(prev, (0, 0), m)
    dust = Image.new("RGBA", (W, H)); dd = ImageDraw.Draw(dust)
    for i in range(14):
        yy = BY0 + i * 115; dd.ellipse([x - 280, yy - 30, x - 20, yy + 140], fill=(200, 205, 208, 40))
    base.alpha_composite(dust.filter(ImageFilter.GaussianBlur(24)))
    e = Image.new("RGBA", (300, 170)); ed = ImageDraw.Draw(e)
    ed.rounded_rectangle([10, 10, 290, 160], 24, fill=(0, 0, 0, 90))
    ed.rounded_rectangle([0, 0, 280, 110], 22, fill=(156, 100, 52)); ed.rectangle([0, 96, 280, 150], fill=(72, 72, 78))
    ed.text((60, 26), "APAGADOR", font=mont(34, "ExtraBold"), fill=(230, 205, 170))
    ey = BY0 + 650 + 420 * math.sin(k * math.pi * 5)
    base.alpha_composite(e.rotate(-10, expand=True, resample=Image.BICUBIC), (int(x - 170), int(ey)))
    return base

def outro(t, ts):
    img = BASE.copy()
    def dr(d):
        ctext(d, 440, "PROVA FINAL", ImageFont.truetype(CH, 110), (250, 222, 90))
        ctext(d, 570, "Qual você pega primeiro?", ImageFont.truetype(CH, 66), (246, 246, 242))
        for i, (y, lab) in enumerate(((720, "1  Progen Emerus"), (840, "2  Pegassi Infernus"))):
            d.rectangle([150, y, 220, y + 70], outline=(246, 246, 242), width=7); d.text((250, y - 6), lab, font=ImageFont.truetype(CH, 70), fill=(246, 246, 242))
        ctext(d, 1010, "Responde nos comentários!", ImageFont.truetype(CH, 62), (170, 220, 250))
    img.alpha_composite(chalk_layer(dr, [(40, 430, 1040, 560, ts, 0.5), (40, 560, 1040, 660, ts + 0.4, 0.6), (40, 710, 1040, 800, ts + 0.9, 0.5),
                                         (40, 830, 1040, 920, ts + 1.2, 0.5), (40, 1000, 1040, 1090, ts + 1.6, 0.6)], t))
    # "x" de giz marcando as duas opções, piscando de uma para a outra
    if t > ts + 2.2:
        d = ImageDraw.Draw(img); y = 720 if int((t - ts) * 1.2) % 2 == 0 else 840
        d.line([(158, y + 8), (212, y + 62)], fill=(250, 222, 90), width=9); d.line([(212, y + 8), (158, y + 62)], fill=(250, 222, 90), width=9)
    postit(img, (800, 1230), [("SEGUE", 62), ("O CANAL!", 50)], ts + 3.6, t, col=(140, 220, 150), ang=6)
    sticker(img, t, ts + 0.4)
    return img

S1 = lambda t: car_scene(t, 6.0, "Aula 1", "PROGEN EMERUS", "Royal Ruby • Vespucci Island", POL1, MAPP1, MP1, 1, 8.6,
                         [lambda im, tt: postit(im, (230, 1250), [("GARAGEM", 50), ("DA ENTRADA", 44)], 11.7, tt)])
S2 = lambda t: car_scene(t, 14.4, "Aula 2", "PEGASSI INFERNUS", "Delegacia de Crosstown", POL2, MAPP2, MP2, 2, 16.6,
                         [lambda im, tt: postit(im, (230, 1250), [("SÉTIMO", 54), ("ANDAR", 54)], 18.8, tt),
                          lambda im, tt: postit(im, (880, 1330), [("TEM", 50), ("RASTREADOR!", 38)], 20.3, tt, col=(250, 150, 150), ang=7)])
def frame(i):
    t = i / FPS
    if t < 5.2: img = intro(t)
    elif t < 6.0: img = eraser(intro(5.2), S1(6.0), (t - 5.2) / 0.8)
    elif t < 13.6: img = S1(t)
    elif t < 14.4: img = eraser(S1(13.6), S2(14.4), (t - 13.6) / 0.8)
    elif t < 22.4: img = S2(t)
    elif t < 23.2: img = eraser(S2(22.4), outro(23.2, 23.2), (t - 22.4) / 0.8)
    else: img = outro(t, 23.2)
    captions(img, t)
    img.convert("RGB").save(f"{OUT}/{i:04d}.jpg", quality=92)

if __name__ == "__main__":
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (0, int(DUR * FPS))
    for i in range(a, b): frame(i)
