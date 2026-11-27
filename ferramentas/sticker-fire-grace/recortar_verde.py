"""Recorta o fundo verde do sticker do canal (feito no CapCut) -> PNGs com transparência.
Uso: python recortar_verde.py <video_verde.mp4> <pasta_saida>
- ignora os 150 px de cima (marca d'água do CapCut);
- alfa suave pela "quantidade de verde" (verde - max(vermelho, azul)) e tira o reflexo verde das bordas;
- corta só a área do sticker. Usado no clipe com escala 0,55 em (16, 150) no 1920x1080."""
import sys, os, cv2, numpy as np
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
cap = cv2.VideoCapture(src); fr = []
while True:
    ok, f = cap.read()
    if not ok: break
    fr.append(f)
def alpha(f):
    b, g, r = [f[..., i].astype(np.float32) for i in range(3)]
    a = np.clip(1 - ((g - np.maximum(r, b)) - 30) / 70, 0, 1); a[:150] = 0; return a
vis, mn, mx = [], [9999, 9999], [0, 0]
for f in fr:
    a = alpha(f)
    if (a > 0.5).mean() > 0.4: vis.append(False); continue       # quadro preto do fim
    ys, xs = np.nonzero(a > 0.5); ok = len(xs) > 200; vis.append(ok)
    if ok: mn = [min(mn[0], xs.min()), min(mn[1], ys.min())]; mx = [max(mx[0], xs.max()), max(mx[1], ys.max())]
x0, y0, x1, y1 = max(0, mn[0] - 10), max(0, mn[1] - 10), min(fr[0].shape[1], mx[0] + 10), min(fr[0].shape[0], mx[1] + 10)
for i, f in enumerate(fr):
    if not vis[i] and i > len(fr) - 15: break
    a = alpha(f) if vis[i] else np.zeros(f.shape[:2], np.float32)
    o = f.astype(np.float32); o[..., 1] = np.minimum(o[..., 1], np.maximum(o[..., 0], o[..., 2]) + 8)
    cv2.imwrite(f"{out}/s{i:03d}.png", np.dstack([o, a * 255]).clip(0, 255).astype(np.uint8)[y0:y1, x0:x1])
print("ok", out, (x0, y0, x1, y1))
