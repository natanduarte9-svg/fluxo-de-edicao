"""Documentário de Elias (9:16, 1080x1920, 30 fps). Quadros JPG em ./frames.
Câmera cinematográfica sobre as 6 imagens + fogo vivo (cintilação e calor), brasas, poeira na luz, névoa,
brilho (bloom), granulado, vinheta, títulos com referência bíblica e legendas sincronizadas palavra a palavra.
Determinístico: cada quadro depende só do tempo. Uso: python render.py <ini> <fim> (índices de quadro)."""
import math, os, sys, glob
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import linha as L

W, H, FPS = 1080, 1920, 30
D = os.path.dirname(os.path.abspath(__file__))
OUT = f"{D}/frames"; os.makedirs(OUT, exist_ok=True)
CINZEL = "/home/user/fonts/Cinzel.ttf"; MONT = "/home/user/fonts/Montserrat.ttf"
GOLD = (242, 193, 78)

def font(path, size, var):
    f = ImageFont.truetype(path, size); f.set_variation_by_name(var); return f

# ---------------- utilidades de tempo ----------------
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def smooth(x): x = clamp(x); return x * x * (3 - 2 * x)
def ease_io(x): x = clamp(x); return 0.5 - 0.5 * math.cos(math.pi * x)
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def vnoise(t, seed):
    """ruído suave 1D (soma de senos com fases fixas) em -1..1"""
    r = np.random.RandomState(seed); fr = r.uniform(0.7, 3.5, 4); ph = r.uniform(0, 6.28, 4)
    return float(sum(math.sin(t * f * 6.28 + p) for f, p in zip(fr, ph)) / 4 * 1.6)

# ---------------- clipes (movimento real, em câmera lenta com quadros intermediários) ----------------
TRQ = 0.45
def win_start(k):
    return 0.0 if k == 1 else L.CENAS[k - 1]["ini"] - TRQ
NQ = {k: len(glob.glob(f"{D}/temporarios/q{k}/*.jpg")) for k in range(1, 7)}
def clip_frame(k, idx):
    idx = max(0, min(NQ[k] - 1, idx))
    return cv2.cvtColor(cv2.imread(f"{D}/temporarios/q{k}/{idx + 1:05d}.jpg"), cv2.COLOR_BGR2RGB).astype(np.float32) / 255
LAST6 = None
def zoom_center(img, z):
    if z <= 1.0001: return img
    M = np.float32([[z, 0, W / 2 * (1 - z)], [0, z, H / 2 * (1 - z)]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
TR = TRQ  # meia transição (dissolve de 0,9 s)

def cam_at(k, t):
    c = L.CENAS[k - 1]
    u = ease_io((t - (c["ini"] - TR)) / (c["fim"] - c["ini"] + 2 * TR))
    a, b = CAM[k]
    z, cx, cy = (a[i] + (b[i] - a[i]) * u for i in range(3))
    return z, cx, cy

def shake(t):
    d = t - L.T_FOGO
    if d < 0 or d > 0.45: return 0.0, 0.0
    a = 7 * (1 - d / 0.45) ** 2
    return a * math.sin(d * 71), a * math.cos(d * 53)

def warp(src, z, cx, cy, sx=0.0, sy=0.0, interp=cv2.INTER_LANCZOS4):
    s = BASE * z
    # garante que a tela fique toda coberta
    hw, hh = W / 2 / s, H / 2 / s
    px = min(max(cx * IW, hw), IW - hw); py = min(max(cy * IH, hh), IH - hh)
    M = np.float32([[s, 0, W / 2 - px * s + sx], [0, s, H / 2 - py * s + sy]])
    return cv2.warpAffine(src, M, (W, H), flags=interp, borderMode=cv2.BORDER_REFLECT)

# ---------------- partículas ----------------
def sprite(r):
    n = int(r * 4) | 1; y, x = np.mgrid[:n, :n] - n // 2
    return np.exp(-(x * x + y * y) / (2 * r * r)).astype(np.float32)
SPR = {r: sprite(r) for r in (1.2, 1.8, 2.5, 3.5, 5.0)}
def put(buf, x, y, spr, col, a):
    n = spr.shape[0]; x0 = int(x) - n // 2; y0 = int(y) - n // 2
    if x0 < 0 or y0 < 0 or x0 + n > W or y0 + n > H: return
    buf[y0:y0 + n, x0:x0 + n] += spr[..., None] * (np.array(col, np.float32) * a)

R = np.random.RandomState(7)
EMB = [dict(x=R.uniform(0, W), ph=R.uniform(0, 1), sp=R.uniform(70, 190), sw=R.uniform(10, 40), sf=R.uniform(0.3, 1.1),
            r=R.choice([1.2, 1.8, 2.5, 3.5]), fl=R.uniform(4, 11), seed=R.randint(1e6)) for _ in range(150)]
DUST = [dict(x=R.uniform(0, W), y=R.uniform(0, H), vx=R.uniform(-9, 9), vy=R.uniform(-6, 4), r=R.choice([1.2, 1.8, 2.5]),
             tw=R.uniform(0.2, 0.9), ph=R.uniform(0, 6.28)) for _ in range(90)]

def embers(buf, t, k, amt, cx_shift):
    for e in EMB:
        span = H + 300
        y = H + 100 - ((t * e["sp"] + e["ph"] * span) % span)
        x = (e["x"] + math.sin(t * e["sf"] + e["ph"] * 9) * e["sw"] + cx_shift * (e["r"] / 2)) % W
        life = 1 - abs((y / H) - 0.5) * 1.2
        a = amt * clamp(life) * (0.55 + 0.45 * math.sin(t * e["fl"] + e["seed"]))
        put(buf, x, y, SPR[e["r"]], (1.0, 0.55, 0.18), a * 1.3)

def dust(buf, t, amt, cx_shift):
    for p in DUST:
        x = (p["x"] + p["vx"] * t + cx_shift * p["r"] * 0.6) % W
        y = (p["y"] + p["vy"] * t) % H
        a = amt * (0.5 + 0.5 * math.sin(t * p["tw"] * 3 + p["ph"])) * clamp(1.2 - y / H)
        put(buf, x, y, SPR[p["r"]], (1.0, 0.92, 0.75), a * 0.55)

# névoa (cena 2): textura de ruído fractal que desliza devagar
def fbm(h, w, seed):
    r = np.random.RandomState(seed); acc = np.zeros((h, w), np.float32); amp = 1.0
    for o in range(5):
        g = r.rand(4 * 2 ** o + 1, 3 * 2 ** o + 1).astype(np.float32)
        acc += cv2.resize(g, (w, h), interpolation=cv2.INTER_CUBIC) * amp; amp *= 0.5
    acc = (acc - acc.min()) / (acc.max() - acc.min()); return acc
MIST = fbm(1100, 2400, 3)

# ---------------- gradação de cor e acabamento ----------------
yy, xx = np.mgrid[:H, :W].astype(np.float32)
VIG = (1 - 0.32 * np.clip(((xx - W / 2) / (W * 0.62)) ** 2 + ((yy - H / 2) / (H * 0.62)) ** 2, 0, 1.4) ** 1.3)[..., None]
TOPG = np.clip(1 - yy / 560, 0, 1)[..., None] ** 1.5
BOTG = np.clip((yy - 1300) / 620, 0, 1)[..., None] ** 1.4

def grade(img):
    img = np.clip(img, 0, 1)
    img = img + 0.07 * (img - 0.5) * (1 - np.abs(img - 0.5) * 2)   # curva em S suave
    lum = img.mean(axis=2, keepdims=True)
    img = img + (lum - img) * -0.06                                   # +6% de saturação
    return img

def bloom(img, amt):
    small = cv2.resize(img, (W // 4, H // 4), interpolation=cv2.INTER_AREA)
    lum = small.max(axis=2, keepdims=True)
    hi = small * np.clip((lum - 0.68) / 0.32, 0, 1)
    hi = cv2.GaussianBlur(hi, (0, 0), 9)
    return img + amt * cv2.resize(hi, (W, H), interpolation=cv2.INTER_LINEAR)

def sharpen(img, a=0.35):
    return img + a * (img - cv2.GaussianBlur(img, (0, 0), 1.2))

# ---------------- uma cena num instante ----------------
def scene(k, t):
    global LAST6
    if k <= 6:
        return clip_frame(k, int(round((t - win_start(k)) * FPS)))
    # cena 7: último quadro da subida (carruagem sumindo no redemoinho), leve aproximação + brasas
    if LAST6 is None: LAST6 = clip_frame(6, NQ[6] - 1)
    c = L.CENAS[6]; u = ease_io((t - c["ini"]) / (c["fim"] - c["ini"]))
    img = zoom_center(LAST6, 1.0 + 0.05 * u).copy()
    embers(img, t + 91, 7, 0.4, 0.0)
    return img

# ---------------- texto ----------------
F_TIT = font(CINZEL, 70, "Bold"); F_REF = font(MONT, 34, "SemiBold")
F_CAP = font(MONT, 60, "ExtraBold"); F_Q = font(CINZEL, 66, "Bold"); F_PILL = font(MONT, 46, "ExtraBold")

def wrap(d, txt, f, maxw):
    lines, cur = [], ""
    for w in txt.split():
        tryl = (cur + " " + w).strip()
        if d.textlength(tryl, font=f) <= maxw or not cur: cur = tryl
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def shadowed(layer_draw_fn, blur=10, sh_alpha=200):
    """desenha num RGBA e cria sombra suave por baixo"""
    lay = Image.new("RGBA", (W, H)); layer_draw_fn(ImageDraw.Draw(lay))
    a = lay.split()[3].filter(ImageFilter.GaussianBlur(blur)).point(lambda v: min(255, v * sh_alpha // 255))
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh.putalpha(a)
    return Image.alpha_composite(sh, lay)

_cache = {}
def title_layer(k):
    if ("t", k) in _cache: return _cache[("t", k)]
    c = L.CENAS[k - 1]; d0 = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    lines = wrap(d0, c["titulo"], F_TIT, 940)
    y_end = [0]
    def draw(d):
        y = 215
        for ln in lines:
            w = d.textlength(ln, font=F_TIT); d.text(((W - w) / 2, y), ln, font=F_TIT, fill=(255, 250, 240)); y += 86
        y_end[0] = y
    lay = shadowed(draw, 9, 230)
    _cache[("t", k)] = (lay, y_end[0]); return _cache[("t", k)]

def ref_layer(k, y):
    if ("r", k) in _cache: return _cache[("r", k)]
    ref = L.CENAS[k - 1]["ref"]
    def draw(d):
        txt = " ".join(ref)  # espaçamento entre letras
        txt = ref.replace(" ", "  ")
        w = d.textlength(txt, font=F_REF); x = (W - w) / 2
        d.line([(x - 70, y + 22), (x - 20, y + 22)], fill=GOLD + (255,), width=3)
        d.line([(x + w + 20, y + 22), (x + w + 70, y + 22)], fill=GOLD + (255,), width=3)
        d.text((x, y), txt, font=F_REF, fill=GOLD + (255,), stroke_width=3, stroke_fill=(20, 12, 6, 255))
    lay = shadowed(draw, 6, 230); _cache[("r", k)] = lay; return lay

def fade_layer(lay, a, dy=0):
    if a <= 0: return None
    if dy: lay = lay.transform(lay.size, Image.AFFINE, (1, 0, 0, 0, 1, -dy))
    if a < 1:
        r, g, b, al = lay.split(); al = al.point(lambda v: int(v * a)); lay = Image.merge("RGBA", (r, g, b, al))
    return lay

# legendas: grupos de até 3 palavras / 20 letras, quebrando nas pontuações
KEY = {"elias", "deus", "acabe", "israel", "senhor", "querite", "corvos", "carmelo", "baal", "fogo", "anjo", "eliseu",
       "céu", "redemoinho", "carruagem", "fé", "coragem", "like", "inscrever", "comente", "seca", "manto"}
FALAS = open(f"{D}/voz.py").read()
import ast
_tok = ast.literal_eval(FALAS.split("FALAS = ")[1].split("]\n")[0] + "]")
GROUPS = []
for ci, c in enumerate(L.CENAS):
    toks = _tok[ci].split(); cur = []
    for tk, (_, a, b) in zip(toks, c["words"]):
        if cur and (len(cur) >= 3 or sum(len(x[0]) + 1 for x in cur) + len(tk) > 20):
            GROUPS.append(cur); cur = []
        cur.append((tk, a, b))
        if tk[-1] in ".,!?:": GROUPS.append(cur); cur = []
    if cur: GROUPS.append(cur)
for gi, g in enumerate(GROUPS):
    nxt = GROUPS[gi + 1][0][1] if gi + 1 < len(GROUPS) else 1e9
    g_end = min(g[-1][2] + 0.45, nxt - 0.07)
    GROUPS[gi] = (g, g[0][1] - 0.06, g_end)

def cap_layer(gi, n_on):
    key = ("c", gi, n_on)
    if key in _cache: return _cache[key]
    g = GROUPS[gi][0]
    words = [w.upper() for w, _, _ in g]
    def draw(d):
        sp = 20; ws = [d.textlength(w, font=F_CAP) for w in words]
        x = (W - sum(ws) - sp * (len(ws) - 1)) / 2; y = 1500
        for i, w in enumerate(words):
            k = w.strip(".,!?:").lower() in KEY
            col = (GOLD if k else (255, 255, 255)) + ((255,) if i < n_on else (95,))
            d.text((x, y), w, font=F_CAP, fill=col, stroke_width=6, stroke_fill=(0, 0, 0, 255 if i < n_on else 90))
            x += ws[i] + sp
    lay = shadowed(draw, 8, 170)
    if len(_cache) > 400: [_cache.pop(k) for k in [k for k in _cache if k[0] == "c"][:200]]
    _cache[key] = lay; return lay

# chamada final (cena 7)
T_COMENTE = L.quando(7, "comente"); T_LIKE = L.quando(7, "like")
def cta_layers(t):
    out = []
    a = smooth((t - (T_COMENTE - 0.5)) / 0.6)
    if a > 0:
        if "q" not in _cache:
            def draw(d):
                y = 620
                for ln in ["QUAL HISTÓRIA", "VOCÊ QUER VER AQUI?"]:
                    w = d.textlength(ln, font=F_Q); d.text(((W - w) / 2, y), ln, font=F_Q, fill=(255, 250, 240)); y += 84
            _cache["q"] = shadowed(draw, 10, 240)
        out.append(fade_layer(_cache["q"], a, dy=int((1 - a) * 25)))
    for i, (txt, t0, hot) in enumerate([("COMENTE", T_COMENTE, False), ("DEIXE SEU LIKE", T_LIKE, False),
                                         ("INSCREVA-SE", L.T_INSCREVER, True)]):
        k = ease_out((t - t0 + 0.1) / 0.35)
        if k <= 0: continue
        key = ("p", i)
        if key not in _cache:
            def draw(d, txt=txt, hot=hot, i=i):
                f = font(MONT, 54 if hot else 46, "ExtraBold")
                w = d.textlength(txt, font=f); pw, ph = w + 90, (96 if hot else 84)
                x0 = (W - pw) / 2; y0 = 900 + i * 118
                if hot:
                    d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], ph / 2, fill=(214, 40, 40, 255), outline=(255, 255, 255, 255), width=4)
                else:
                    d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], ph / 2, fill=(15, 12, 10, 200), outline=GOLD + (255,), width=3)
                d.text((x0 + 45, y0 + ph / 2), txt, font=f, fill=(255, 255, 255, 255), anchor="lm")
            _cache[key] = shadowed(draw, 8, 200)
        lay = _cache[key]
        if k < 1:  # entra crescendo a partir do centro do botão
            s = 0.6 + 0.4 * k; lay = lay.transform(lay.size, Image.AFFINE, (1 / s, 0, W / 2 * (1 - 1 / s), 0, 1 / s, (960 + i * 118) * (1 - 1 / s)))
        out.append(fade_layer(lay, min(1, k * 1.5)))
    return out

STK = sorted(glob.glob(f"{D}/sticker/s*.png")); T_STK = L.T_INSCREVER - 1.6

# ---------------- quadro final ----------------
def frame(i):
    t = i / FPS
    ks = [k for k in range(1, 8) if L.CENAS[k - 1]["ini"] - TR <= t < L.CENAS[k - 1]["fim"] + TR]
    imgs = []
    for k in ks:
        c = L.CENAS[k - 1]
        if k == 1: wgt = 1.0 if t < c["fim"] - TR else 1 - ease_io((t - (c["fim"] - TR)) / (2 * TR))
        else:
            wgt = ease_io((t - (c["ini"] - TR)) / (2 * TR))
        imgs.append((k, wgt))
    # dissolve: a cena nova entra por cima da anterior
    img = None
    for k, wgt in imgs:
        s = scene(k, t)
        img = s if img is None else img * (1 - wgt) + s * wgt
    # luz que vira a próxima cena (3→4 e 5→6)
    # cena 7: escurece e desfoca o fundo para o convite ficar legível
    c7 = L.CENAS[6]
    a7 = smooth((t - c7["ini"]) / 1.6)
    if a7 > 0:
        bl = cv2.GaussianBlur(img, (0, 0), 7)
        img = (img * (1 - a7) + bl * a7) * (1 - 0.42 * a7)
    # bloom (mais forte no fogo e na subida)
    bamt = 0.16 + 0.10 * math.exp(-abs(t - L.T_FOGO - 0.3) / 0.9) + 0.12 * math.exp(-abs(t - L.T_REDEMOINHO - 0.3) / 1.2)
    img = bloom(img, bamt)
    img = grade(img) * VIG
    # escurecimento leve no topo (títulos) e embaixo (legendas)
    tit_on = any(L.CENAS[k - 1]["titulo"] and L.CENAS[k - 1]["ini"] - 0.3 <= t <= L.CENAS[k - 1]["fim"] for k in range(1, 7))
    img = img * (1 - 0.38 * TOPG * tit_on) * (1 - 0.42 * BOTG)
    # granulado de filme
    rng = np.random.RandomState(i)
    img = img + rng.normal(0, 0.012, (H // 2, W // 2, 1)).astype(np.float32).repeat(2, 0).repeat(2, 1)
    # fade final
    img = img * (1 - smooth((t - (L.DUR - 0.8)) / 0.8)) * smooth(t / 0.25 + 0.6)
    out = Image.fromarray((np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)).convert("RGBA")
    # títulos e referências
    for k in range(1, 7):
        c = L.CENAS[k - 1]
        if not (c["ini"] - 0.5 <= t <= c["fim"] + 0.5): continue
        ti = c["ini"] + (0.15 if k == 1 else 0.35); tout = c["ini"] + 6.0
        a = smooth((t - ti) / 0.6) * (1 - smooth((t - tout) / 0.7))
        lay, yend = title_layer(k)
        la = fade_layer(lay, a, dy=int((1 - smooth((t - ti) / 0.8)) * 22))
        if la: out.alpha_composite(la)
        ar = smooth((t - ti - 0.35) / 0.6) * (1 - smooth((t - (c["fim"] - 0.5)) / 0.5))
        la = fade_layer(ref_layer(k, yend + 18), ar)
        if la: out.alpha_composite(la)
    for la in cta_layers(t):
        if la: out.alpha_composite(la)
    # legendas
    for gi, (g, a, b) in enumerate(GROUPS):
        if a <= t < b:
            n_on = sum(1 for _, wa, _ in g if wa <= t)
            ga = smooth((t - a) / 0.12) * (1 - smooth((t - (b - 0.12)) / 0.12))
            la = fade_layer(cap_layer(gi, n_on), ga)
            if la: out.alpha_composite(la)
    # sticker "Inscreva-se" (acompanha a fala "se inscrever")
    j = int((t - T_STK) * FPS)
    if STK and 0 <= j < len(STK):
        out.alpha_composite(Image.open(STK[j]).convert("RGBA"), (160, 110))
    out.convert("RGB").save(f"{OUT}/{i:05d}.jpg", quality=93)

if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    for i in range(a, min(b, int(L.DUR * FPS))): frame(i)
