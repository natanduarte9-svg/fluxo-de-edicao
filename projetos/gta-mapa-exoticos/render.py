"""Teste: Short 9:16 "2 supercarros no GTA 6" com mapa, pinos e cartões. Gera quadros PNG em ./frames."""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H, FPS, DUR = 1080, 1920, 30, 22.0
T = "thumbs/"
OUT = "frames"; os.makedirs(OUT, exist_ok=True)
FB = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
MONT = "/home/user/fonts/Montserrat.ttf"

def mont(size, w="Bold"):
    f = ImageFont.truetype(MONT, size); f.set_variation_by_name(w); return f
F_TITLE = ImageFont.truetype(FB, 88)
F_NAME = ImageFont.truetype(FB, 66)
F_SUB = mont(36, "SemiBold"); F_LINE = mont(40, "Bold"); F_NUM = ImageFont.truetype(FB, 54)

# ---------- recursos ----------
MAP = Image.open(T + "gGvMUEJjKCs.jpg").convert("RGB").crop((700, 0, 1200, 720))
MAP = MAP.resize((MAP.width * 4, MAP.height * 4), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 60, 2))
MS = 4  # escala do mapa ampliado
def photo(path, box, size):
    im = Image.open(path).convert("RGB").crop(box)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    tw, th = size; r = max(tw / im.width, th / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x0 = (im.width - tw) // 2; y0 = (im.height - th) // 2
    im = im.crop((x0, y0, x0 + tw, y0 + th))
    m = Image.new("L", size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, tw - 1, th - 1], 28, fill=255)
    out = Image.new("RGBA", size); out.paste(im, (0, 0), m); return out
P1 = photo(T + "MBn2O8b2T2Y.jpg", (590, 170, 1280, 620), (940, 420))
P2 = photo(T + "Hb6ZJf7Bpg4.jpg", (0, 50, 480, 310), (940, 420))

PIN1 = (440, 265)   # Vespucci Island (coordenadas no recorte do mapa, 500x720)
PIN2 = (320, 270)   # Crosstown, Vice City

# ---------- tempo ----------
def clamp(x): return max(0.0, min(1.0, x))
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def back(x):
    x = clamp(x); c1, c3 = 1.70158, 2.70158; return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def lerp(a, b, k): return a + (b - a) * k

# câmera: (tempo, cx, cy, zoom)
KEYS = [(0.0, 250, 360, 1.00), (3.2, 250, 340, 1.12), (4.4, 420, 300, 2.6),
        (10.6, 418, 300, 2.7), (11.8, 330, 300, 2.6), (18.2, 332, 300, 2.7), (19.4, 352, 330, 1.35), (22.0, 352, 330, 1.42)]
def camera(t):
    for (t0, x0, y0, z0), (t1, x1, y1, z1) in zip(KEYS, KEYS[1:]):
        if t0 <= t <= t1:
            k = ease((t - t0) / (t1 - t0)) if (t1 - t0) < 2 else (t - t0) / (t1 - t0)
            return lerp(x0, x1, k), lerp(y0, y1, k), lerp(z0, z1, k)
    return KEYS[-1][1:]
S0 = H / 720.0
def to_screen(p, cam):
    cx, cy, z = cam; s = S0 * z
    return W / 2 + (p[0] - cx) * s, H / 2 + (p[1] - cy) * s

def render_map(cam):
    cx, cy, z = cam; s = S0 * z / MS        # pixels de tela por pixel do mapa ampliado
    # transformação afim: tela -> mapa
    a = 1 / s; c = cx * MS - (W / 2) / s; f = cy * MS - (H / 2) / s
    return MAP.transform((W, H), Image.AFFINE, (a, 0, c, 0, a, f), resample=Image.BILINEAR, fillcolor=(18, 120, 170))

def text_c(d, y, txt, font, fill, stroke=8, sc=(0, 0, 0)):
    w = d.textlength(txt, font=font); d.text(((W - w) / 2, y), txt, font=font, fill=fill, stroke_width=stroke, stroke_fill=sc)

def pin(img, xy, t0, t, num):
    if t < t0: return
    k = back((t - t0) / 0.45); x, y = xy; y -= (1 - k) * 260
    d = ImageDraw.Draw(img)
    if t > t0 + 0.4:   # pulso no chão
        ph = ((t - t0 - 0.4) % 1.4) / 1.4; r = 20 + 70 * ph
        d.ellipse([x - r, xy[1] - r * 0.45, x + r, xy[1] + r * 0.45], outline=(255, 60, 60, int(230 * (1 - ph))), width=6)
    d.ellipse([x - 46, y - 120, x + 46, y - 28], fill=(232, 30, 30), outline=(255, 255, 255), width=6)
    d.polygon([(x - 30, y - 50), (x + 30, y - 50), (x, y)], fill=(232, 30, 30))
    tw = d.textlength(str(num), font=F_NUM); d.text((x - tw / 2, y - 107), str(num), font=F_NUM, fill="white")

def card(img, t, t_in, t_out, ph, name, sub, l1, l2):
    if t < t_in or t > t_out + 0.35: return
    k = ease_out((t - t_in) / 0.5) if t < t_out else 1 - ease((t - t_out) / 0.35)
    y0 = int(1000 + (1 - k) * 700)
    panel = Image.new("RGBA", (1000, 620), (0, 0, 0, 0)); d = ImageDraw.Draw(panel)
    d.rounded_rectangle([0, 0, 999, 619], 40, fill=(12, 12, 16, 235), outline=(255, 210, 31, 255), width=5)
    panel.alpha_composite(ph, (30, 30))
    d.text((40, 520), name, font=F_NAME, fill=(255, 210, 31), anchor="ls")
    nw = d.textlength(name, font=F_NAME); d.text((56 + nw, 516), sub, font=F_SUB, fill=(255, 255, 255), anchor="ls")
    d.text((40, 562), "📍 " if False else "", font=F_LINE)
    d.text((40, 570), l1, font=F_LINE, fill="white", anchor="ls")
    d.text((40, 608), l2, font=mont(32, "SemiBold"), fill=(200, 200, 205), anchor="ls")
    img.alpha_composite(panel, (40, y0))

def frame(i):
    t = i / FPS
    cam = camera(t)
    img = render_map(cam).convert("RGBA")
    # escurece as bordas (vinheta) e as faixas de texto
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for y in range(0, 720, 10): d.rectangle([0, y, W, y + 10], fill=(0, 0, 0, int(215 * (1 - (y / 720) ** 1.6))))
    img.alpha_composite(ov)
    pin(img, to_screen(PIN1, cam), 4.4, t, 1)
    pin(img, to_screen(PIN2, cam), 11.9, t, 2)
    d = ImageDraw.Draw(img)
    # gancho (0–3,6 s) e chamada final (19,4 s+): sempre abaixo da faixa do sticker (y>=410)
    if t < 3.6:
        a = 1 if t < 3.3 else 1 - (t - 3.3) / 0.3
        k = back(t / 0.35)
        f1 = F_TITLE.font_variant(size=int(40 + 48 * k))
        lay = Image.new("RGBA", (W, H)); dl = ImageDraw.Draw(lay)
        text_c(dl, 410, "2 SUPERCARROS", f1, (255, 255, 255)); text_c(dl, 515, "ESCONDIDOS NO GTA 6", f1, (255, 210, 31))
        lay.putalpha(Image.eval(lay.split()[3], lambda v: int(v * a))); img.alpha_composite(lay)
    if t > 19.4:
        k = back((t - 19.4) / 0.35); f1 = F_TITLE.font_variant(size=int(40 + 44 * k))
        text_c(d, 410, "QUAL VOCÊ PEGA", f1, (255, 255, 255)); text_c(d, 515, "PRIMEIRO? COMENTA!", f1, (255, 210, 31))
    card(img, t, 4.9, 10.5, P1, "PROGEN EMERUS", "Royal Ruby", "Vespucci Mansion • Vespucci Island", "Na garagem da entrada da mansão")
    card(img, t, 12.4, 18.1, P2, "PEGASSI INFERNUS", "", "Delegacia de Crosstown • Vice City", "7º andar do estacionamento • tem rastreador")
    img.convert("RGB").save(f"{OUT}/{i:04d}.jpg", quality=92)

if __name__ == "__main__":
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (0, int(DUR * FPS))
    for i in range(a, b): frame(i)
