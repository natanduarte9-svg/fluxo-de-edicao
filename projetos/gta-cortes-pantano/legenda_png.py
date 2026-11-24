"""Gera um PNG transparente (1080x560) por fala, para a faixa de baixo do Short: nome em amarelo, fala em branco,
letras grandes com contorno preto. Palavrões levam asterisco (monetização). Uso: python legenda_png.py <n>"""
import sys, json, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
n = sys.argv[1]
F = ImageFont.truetype("/home/user/fonts/Montserrat.ttf", 54); F.set_variation_by_name("ExtraBold")
CENS = {"caralho": "c*ralho", "porra": "p*rra", "foder": "f*der", "puta": "p*ta", "merda": "m*rda"}
def censura(s):
    return re.sub(r"\b(" + "|".join(CENS) + r")\b", lambda m: (lambda w: w[0] + "*" + w[2:])(m.group(0)), s, flags=re.I)
def wrap(d, txt, maxw):
    out, cur = [], ""
    for w in txt.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=F) <= maxw or not cur: cur = t
        else: out.append(cur); cur = w
    out.append(cur); return out
falas = json.load(open("falas.json"))[n]
for j, (a, b, linhas) in enumerate(falas):
    im = Image.new("RGBA", (1080, 560)); d = ImageDraw.Draw(im)
    rows = []
    for quem, txt in linhas:
        ws = wrap(d, quem + ": " + censura(txt), 960)
        for k, ln in enumerate(ws): rows.append((quem if k == 0 else None, ln))
    y = 20
    for quem, ln in rows:
        x = (1080 - d.textlength(ln, font=F)) / 2
        if quem:
            nome = quem + ":"; d.text((x, y), nome, font=F, fill=(255, 210, 31), stroke_width=6, stroke_fill="black")
            x2 = x + d.textlength(nome + " ", font=F); d.text((x2, y), ln[len(nome) + 1:], font=F, fill="white", stroke_width=6, stroke_fill="black")
        else:
            d.text((x, y), ln, font=F, fill="white", stroke_width=6, stroke_fill="black")
        y += 70
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); sh.putalpha(im.split()[3].filter(ImageFilter.GaussianBlur(8)).point(lambda v: v * 150 // 255))
    Image.alpha_composite(sh, im).save(f"tmp/cap_{n}_{j}.png")
print(n, len(falas))
