"""Reescreve "FIRE & GRACE" inteiro dentro do círculo do logo (o modelo do CapCut corta para "IRE & GRAC").
Uso: python corrigir_nome.py <pasta_pngs_recortados> <pasta_saida>
Faixa do nome escurecida (com degradê), aro laranja refeito, nome em Cinzel com brilho quente.
Medidas do recorte feito por recortar_verde.py (1034x397): centro (166,174), aro r=146, disco preto r<142."""
import sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
SRC, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
FONTE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fontes", "Cinzel.ttf")
ref = np.asarray(Image.open(f"{SRC}/s100.png")).astype(np.float32)
Hh, Ww = ref.shape[:2]
CX, CY, Y0, Y1 = 166, 174, 214, 258
yy, xx = np.mgrid[0:Hh, 0:Ww]; r = np.sqrt((xx - CX) ** 2 + (yy - CY) ** 2)
rgb = ref[..., :3]; A = ref[..., 3]
card = (rgb.min(2) > 225) & (A > 200) & (xx > 280)
inb = (yy >= Y0) & (yy <= Y1) & (xx < 312) & ~card
# degradê vertical: escuro no meio da faixa, some nas bordas de cima/baixo
f = np.clip(np.minimum(yy - Y0, Y1 - yy) / 7.0, 0, 1)
dentro = inb & (r < 145.5)
out = rgb.copy(); alpha = A.copy()
out[dentro] = out[dentro] * (1 - f[dentro][:, None])
# fora do disco, na faixa: aro laranja (r 142-149) e transparente depois
aro = inb & (r >= 145.5) & (r < 149)
out[aro] = np.array([196, 106, 52]); alpha[aro] = 255
fora = inb & (r >= 149); alpha[fora] = 0
# nome
S = 4
font = ImageFont.truetype(FONTE, 19 * S)
txt, sp = "FIRE & GRACE", 2.4 * S
ws = [font.getlength(c) for c in txt]; tw = sum(ws) + sp * (len(txt) - 1)
lay = Image.new("L", (Ww * S, Hh * S), 0); d = ImageDraw.Draw(lay)
x = CX * S - tw / 2
for c, w in zip(txt, ws): d.text((x, 224 * S), c, font=font, fill=255); x += w + sp
lay = lay.resize((Ww, Hh), Image.LANCZOS)
t = np.asarray(lay).astype(np.float32)[..., None] / 255
g = np.asarray(lay.filter(ImageFilter.GaussianBlur(3.5))).astype(np.float32)[..., None] / 255
out = out + g * np.array([210, 140, 60]) * 0.6
out = out * (1 - t) + t * np.array([248, 234, 204])
patch = np.dstack([np.clip(out, 0, 255), alpha]).astype(np.uint8)
pm = inb | (t[..., 0] > 0.01)
for fn in sorted(os.listdir(SRC)):
    i = int(fn[1:4]); a = np.asarray(Image.open(f"{SRC}/{fn}")).copy()
    if 26 <= i <= 236: a[pm] = patch[pm]          # só enquanto o logo está parado
    Image.fromarray(a).save(f"{OUT}/{fn}")
print("ok", OUT)
