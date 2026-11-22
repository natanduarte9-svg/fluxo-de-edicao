"""Troca LIKE -> CURTIR e SUBSCRIBE -> INSCREVA-SE no encerramento, quadro a quadro.
A pílula cinza (#282828) cresce para a direita; o texto novo aparece só dentro dela."""
import glob, os
from PIL import Image, ImageDraw, ImageFont

GRAY = (40, 40, 40)
FONT = "/home/user/fonts/Montserrat.ttf"
# zona de cada pílula: (busca_x0, busca_x1, texto_x0, texto_x1_max, texto)
PILLS = [(500, 820, 515, 760, "CURTIR"), (1235, 1560, 1243, 1500, "INSCREVA-SE")]
Y0, Y1, YROW, YC = 822, 891, 893, 856

def font_for(text, maxw):
    for size in range(60, 20, -1):
        f = ImageFont.truetype(FONT, size)
        f.set_variation_by_name("ExtraBold")
        if f.getlength(text) <= maxw:
            return f
    return f

RMAX = [0, 0]   # a pílula só cresce: usa o maior R já visto
FONTS = [font_for(t, x1 - x0 - 30) for (_, _, x0, x1, t) in PILLS]

def is_gray(p):
    r, g, b = p[:3]
    return 30 <= r <= 50 and abs(r - g) < 8 and abs(g - b) < 8

for path in sorted(glob.glob("fr/*.png")):
    idx = int(os.path.basename(path)[:3])
    im = Image.open(path).convert("RGB")
    d = ImageDraw.Draw(im)
    for k, ((sx0, sx1, tx0, tx1, text), f) in enumerate(zip(PILLS, FONTS)):
        # borda direita da pílula: último pixel cinza na linha sem texto
        # borda direita da parte cinza contínua, a partir do início do texto (linha sem texto)
        x = tx0
        while x < sx1 and (is_gray(im.getpixel((x, YROW))) or is_gray(im.getpixel((x, 819))) or is_gray(im.getpixel((x, 887)))):
            x += 1
        R = max(x, RMAX[k]) if x - tx0 >= 20 or RMAX[k] else x
        RMAX[k] = max(RMAX[k], R) if R - tx0 >= 20 else RMAX[k]
        if R - tx0 < 20:
            continue
        cover = R - 10                    # cobre todo o texto antigo dentro da pílula
        right = min(tx1, cover)           # o texto novo fica até aqui
        d.rectangle([tx0, 816, cover, 897], fill=GRAY)
        if idx <= 105:   # só enquanto as letras antigas pulam (depois, não apagar o brilho do título)
            d.rectangle([tx0, 770, max(cover, tx1), 812], fill=(0, 0, 0))
            d.rectangle([tx0, 902, max(cover, tx1), 940], fill=(0, 0, 0))
        # texto clipado à parte visível da pílula
        layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).text((tx0 + 8, YC), text, font=f, fill=(255, 255, 255, 255), anchor="lm")
        mask = Image.new("L", im.size, 0)
        ImageDraw.Draw(mask).rectangle([tx0, Y0, right, Y1], fill=255)
        im.paste(layer, (0, 0), Image.composite(layer, Image.new("RGBA", im.size), mask).split()[3])
    im.save(path.replace("fr/", "out/"))
print("ok")
