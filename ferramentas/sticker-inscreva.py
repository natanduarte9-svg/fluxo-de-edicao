"""Sticker animado "Inscreva-se": PNGs com transparência, 30 fps, 4 s.
Uso: python sticker.py <pasta_saida> [duracao_s]  (padrão 5,6 s; FIRE & GRACE: 10 s)
Linha do tempo: 0-0.35 s entra (pop), 1.0-1.5 s cursor vai ao botão, 1.6 s clique (vira INSCRITO),
1.9-2.6 s sino balança, 3.6-4.0 s sai. Determinístico (sem aleatório)."""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
FPS, DUR = 30, float(sys.argv[2]) if len(sys.argv) > 2 else 5.6
W, H = 760, 300                      # quadro do sticker (com folga para rotação/cursor)
CW, CH = 560, 120                    # cartão
FB = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Black.otf", 34)
SS = 3                               # supersampling para bordas suaves

def ease_out_back(x):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2

def clamp(x): return max(0.0, min(1.0, x))

def card(subscribed, bell_angle, press):
    s = SS
    im = Image.new("RGBA", (CW * s, CH * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, CW * s - 1, CH * s - 1], radius=26 * s, fill=(255, 255, 255, 255),
                        outline=(220, 220, 220, 255), width=3 * s)
    # joinha (polegar estilizado)
    bx, by = 40 * s, 30 * s
    blue = (52, 120, 246, 255)
    d.rounded_rectangle([bx, by + 22 * s, bx + 16 * s, by + 62 * s], radius=4 * s, fill=blue)
    d.rounded_rectangle([bx + 20 * s, by + 22 * s, bx + 58 * s, by + 62 * s], radius=10 * s, fill=blue)
    d.polygon([(bx + 22 * s, by + 26 * s), (bx + 34 * s, by - 2 * s), (bx + 44 * s, by + 2 * s),
               (bx + 40 * s, by + 24 * s)], fill=blue)
    # botão
    k = 1 - 0.06 * press
    bw, bh = 300 * s * k, 70 * s * k
    cx, cy = 260 * s, CH * s / 2
    col = (200, 200, 200, 255) if subscribed else (230, 33, 23, 255)
    d.rounded_rectangle([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], radius=14 * s, fill=col)
    # ícone play
    px, py = cx - bw / 2 + 22 * s, cy
    d.rounded_rectangle([px, py - 15 * s, px + 40 * s, py + 15 * s], radius=7 * s, fill=(255, 255, 255, 255))
    d.polygon([(px + 15 * s, py - 8 * s), (px + 15 * s, py + 8 * s), (px + 28 * s, py)], fill=col)
    txt = "INSCRITO" if subscribed else "INSCREVA-SE"
    f = FB.font_variant(size=int(30 * s * k))
    tw = d.textlength(txt, font=f)
    tx = px + 50 * s + (cx + bw / 2 - px - 50 * s - tw) / 2
    d.text((tx, cy), txt, font=f, fill=(90, 90, 90, 255) if subscribed else (255, 255, 255, 255), anchor="lm")
    # sino
    bell = Image.new("RGBA", (80 * s, 80 * s), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bell)
    gold = (255, 196, 0, 255) if subscribed else (60, 60, 60, 255)
    bd.pieslice([18 * s, 12 * s, 62 * s, 64 * s], 180, 360, fill=gold)
    bd.rectangle([18 * s, 38 * s, 62 * s, 56 * s], fill=gold)
    bd.rounded_rectangle([12 * s, 54 * s, 68 * s, 62 * s], radius=4 * s, fill=gold)
    bd.ellipse([34 * s, 60 * s, 46 * s, 72 * s], fill=gold)
    bd.ellipse([36 * s, 6 * s, 44 * s, 14 * s], fill=gold)
    bell = bell.rotate(bell_angle, resample=Image.BICUBIC, center=(40 * s, 8 * s))
    im.alpha_composite(bell, (CW * s - 105 * s, int(CH * s / 2 - 40 * s)))
    return im.resize((CW, CH), Image.LANCZOS)

def cursor():
    s = SS
    c = Image.new("RGBA", (40 * s, 56 * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    pts = [(2, 2), (2, 44), (12, 34), (20, 52), (28, 48), (20, 31), (34, 31)]
    d.polygon([(x * s, y * s) for x, y in pts], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=3 * s)
    return c.resize((40, 56), Image.LANCZOS)

CUR = cursor()
n = int(FPS * DUR)
for i in range(n):
    t = i / FPS
    if t < 0.35: sc = ease_out_back(clamp(t / 0.35))
    elif t > DUR - 0.4: sc = 1 - clamp((t - (DUR - 0.4)) / 0.4) ** 2
    else: sc = 1.0
    subscribed = t >= 1.6
    press = max(0.0, 1 - abs(t - 1.6) / 0.12)
    bell = 0.0
    if 1.9 <= t <= 2.6: bell = 22 * math.sin((t - 1.9) * 2 * math.pi * 4) * (1 - (t - 1.9) / 0.7)
    c = card(subscribed, bell, press)
    frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if sc > 0.01:
        cw, ch = max(1, int(CW * sc)), max(1, int(CH * sc))
        cc = c.resize((cw, ch), Image.LANCZOS).rotate(-4, resample=Image.BICUBIC, expand=True)
        frame.alpha_composite(cc, ((W - cc.width) // 2, (H - cc.height) // 2))
    # cursor: entra de baixo-direita, vai ao botão, clica, sai
    if 0.9 <= t <= 3.2:
        tx, ty = W // 2 - 20, H // 2 + 5
        sx, sy = W - 90, H - 60
        p = clamp((t - 0.9) / 0.6); p = 1 - (1 - p) ** 3
        x = sx + (tx - sx) * p; y = sy + (ty - sy) * p
        if t > 2.2:
            q = clamp((t - 2.2) / 0.6); x += 140 * q; y += 60 * q
        ck = 1 - 0.15 * press
        cc = CUR.resize((int(40 * ck), int(56 * ck)), Image.LANCZOS)
        frame.alpha_composite(cc, (int(x), int(y)))
        if 1.6 <= t <= 1.95:   # onda do clique
            r = (t - 1.6) / 0.35
            dd = ImageDraw.Draw(frame)
            R = 10 + 30 * r
            dd.ellipse([x - R, y - R, x + R, y + R], outline=(255, 255, 255, int(220 * (1 - r))), width=4)
    frame.save(f"{OUT}/s{i:03d}.png")
print("ok", n, "quadros")
