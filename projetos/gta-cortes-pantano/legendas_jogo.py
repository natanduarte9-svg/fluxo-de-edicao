"""Acha os trechos de legenda do jogo (região y 578–672 do 1280x720) a cada 0,2 s e gera uma folha
com um recorte por trecho, para eu ler o texto. Saída: an/leg_<n>.json e an/leg_<n>.jpg"""
import sys, subprocess, json, numpy as np
from PIL import Image, ImageDraw
n, S, E = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
X0, Y0, X1, Y1 = 160, 578, 1120, 672
w, h = X1 - X0, Y1 - Y0
raw = subprocess.check_output(["ffmpeg", "-v", "error", "-ss", str(S), "-t", str(E - S), "-i", "src/gameplay.mp4",
    "-vf", f"fps=5,crop={w}:{h}:{X0}:{Y0}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)
lum = fr.mean(3); mask = (lum > 175) & (fr.min(3) > 120)        # texto branco/amarelado
segs = []; cur = None
for i, m in enumerate(mask):
    on = m.sum() > 150
    if cur and on:
        inter = (m & cur["m"]).sum(); uni = (m | cur["m"]).sum()
        if inter / max(uni, 1) > 0.55: cur["fim"] = i; continue
    if cur: segs.append(cur); cur = None
    if on: cur = dict(ini=i, fim=i, m=m, k=i)
if cur: segs.append(cur)
segs = [s for s in segs if s["fim"] - s["ini"] >= 3]          # pelo menos 0,6 s
out = []; sheet = Image.new("RGB", (w, (h + 24) * max(1, len(segs))), (0, 0, 0)); d = ImageDraw.Draw(sheet)
for j, s in enumerate(segs):
    mid = (s["ini"] + s["fim"]) // 2
    sheet.paste(Image.fromarray(fr[mid]), (0, j * (h + 24) + 24))
    d.text((5, j * (h + 24) + 5), f"#{j}  {s['ini']/5:.1f}s -> {(s['fim']+1)/5:.1f}s", fill="yellow")
    out.append(dict(i=j, ini=round(s["ini"] / 5, 2), fim=round((s["fim"] + 1) / 5, 2)))
sheet.save(f"an/leg_{n}.jpg", quality=88)
json.dump(out, open(f"an/leg_{n}.json", "w"), indent=0)
print(n, len(out), "trechos")
