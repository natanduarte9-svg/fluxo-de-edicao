"""Acha trechos de ação numa gameplay longa: som (volume e estalos/tiros) + movimento na tela.
Saída: an/curvas.npz e an/candidatos.json (janelas de 25 s com a maior nota, sem sobrepor)."""
import numpy as np, json
SR = 16000
a = np.fromfile("an/audio.f32", np.float32)
n = len(a) // SR
a = a[: n * SR]
# volume por segundo (dB) e "estalos" (transientes de 10 ms: tiros, batidas, explosões)
sec = a.reshape(n, SR)
rms = 20 * np.log10(np.sqrt((sec ** 2).mean(1)) + 1e-6)
f = a[: (len(a) // 160) * 160].reshape(-1, 160)
e = np.log10((f ** 2).mean(1) + 1e-9)
d = np.diff(e, prepend=e[0])
trans = (d > 0.9).astype(np.float32)          # subida brusca de >9 dB em 10 ms
tr = trans[: n * 100].reshape(n, 100).sum(1)
peak = 20 * np.log10(np.abs(sec).max(1) + 1e-6)
# movimento na tela (diferença média entre quadros a 2 fps) e cortes
g = np.fromfile("an/gray.raw", np.uint8)
fr = g[: (len(g) // (96 * 54)) * 96 * 54].reshape(-1, 54, 96).astype(np.float32)
mv = np.abs(np.diff(fr, axis=0)).mean((1, 2))
mv = np.concatenate([[0], mv])
m = min(n, len(mv) // 2)
mot = mv[: m * 2].reshape(m, 2).mean(1)
bright = fr[: m * 2].reshape(m, 2, 54, 96).mean((1, 2, 3))
n = m; rms, tr, peak = rms[:n], tr[:n], peak[:n]
def z(x):
    x = np.asarray(x, np.float64); return (x - np.median(x)) / (np.percentile(x, 90) - np.median(x) + 1e-6)
score = 0.9 * z(tr) + 0.6 * z(rms) + 0.8 * z(mot) + 0.3 * z(peak)
score[bright < 25] -= 3          # tela preta/carregando
np.savez("an/curvas.npz", rms=rms, tr=tr, mot=mot, peak=peak, bright=bright, score=score)
W = 25
cs = np.convolve(score, np.ones(W) / W, mode="valid")
# janela: média da nota + destaque do pico (clímax)
pk = np.array([score[i:i + W].max() for i in range(len(cs))])
tot = cs + 0.25 * pk
order = np.argsort(-tot); used = np.zeros(n, bool); cand = []
for i in order:
    if used[max(0, i - 10):i + W + 10].any(): continue
    used[i:i + W] = True
    cand.append(dict(ini=int(i), fim=int(i + W), nota=round(float(tot[i]), 2),
                     pico=int(i + np.argmax(score[i:i + W])), estalos=int(tr[i:i + W].sum())))
    if len(cand) >= 24: break
json.dump(cand, open("an/candidatos.json", "w"), indent=1)
for c in cand: print("%02d:%02d:%02d  nota %.2f  estalos %d  pico %ds" % (c["ini"] // 3600, c["ini"] // 60 % 60, c["ini"] % 60, c["nota"], c["estalos"], c["pico"] - c["ini"]))
