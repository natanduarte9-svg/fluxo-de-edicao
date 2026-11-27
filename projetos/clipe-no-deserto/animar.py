"""Clipe "NO DESERTO, ELE VENCEU": dá vida à imagem estática (16:9, 1920x1080, 30 fps) e grava o vídeo final.
Uso: python animar.py <pasta> [inicio_s fim_s]   (trecho opcional = prévia rápida)
Camadas: câmera de cinema lenta (push-in nos versos, abre nos refrões, nunca corta o título),
sol que "respira", raios de luz animados, poeira dourada em 2 profundidades (com bokeh),
pulso de luz na batida só nos refrões, vinheta, grão de filme, fade de entrada/saída.
Por cima (ffmpeg): karaokê (karaoke.ass) e o sticker Inscreva-se/Like 3 vezes (10 s cada).
Áudio: a música do Suno, -14 LUFS em dois passes."""
import sys, os, json, subprocess, math
import numpy as np, cv2

P = sys.argv[1]; FPS = 30; OW, OH = 1920, 1080
DUR = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{P}/musica.mp3"]))
T0, T1 = (float(sys.argv[2]), float(sys.argv[3])) if len(sys.argv) > 3 else (0.0, DUR)
OUT = f"{P}/clipe.mp4" if len(sys.argv) <= 3 else f"{P}/previa_{int(T0)}.mp4"
REFROES = [(83.3, 111.0), (168.5, 196.2), (227.7, 254.3)]
STICKERS = [2.0, DUR / 2 - 5, DUR - 10.6]           # começo, meio, fim (10 s cada)
BEATS = np.load(f"{P}/batidas.npy")

# ---------- base: imagem em resolução maior para a câmera andar sem perder nitidez ----------
src = cv2.imread(f"{P}/capa.png")
BW, BH = 2112, 1188
base = cv2.resize(src, (BW, BH), interpolation=cv2.INTER_LANCZOS4)
sx, sy = BW / src.shape[1], BH / src.shape[0]
SUN = (60 * sx, 300 * sy)                             # sol à esquerda
yy, xx = np.mgrid[0:BH, 0:BW].astype(np.float32)
dx, dy = xx - SUN[0], yy - SUN[1]; r = np.sqrt(dx * dx + dy * dy)
warm = np.array([55, 140, 255], np.float32)           # BGR dourado
glow = np.exp(-(r / 420) ** 2)[..., None] * warm * 0.9 + np.exp(-(r / 1100) ** 2)[..., None] * warm * 0.25
GLOW = np.clip(glow, 0, 255).astype(np.uint8)
ang = np.arctan2(dy, dx)
ceu = np.clip((560 * sy - yy) / (220 * sy), 0, 1)     # raios só no céu/horizonte
def raios(fase):
    rng = np.random.RandomState(int(fase * 10))
    s = np.zeros_like(ang)
    for f, a in [(9, .5), (17, .3), (31, .2)]: s += a * (0.5 + 0.5 * np.cos(ang * f + rng.rand() * 6.28))
    s = s ** 3 * np.exp(-(r / 1500)) * ceu
    return np.clip(s[..., None] * warm * 0.55, 0, 255).astype(np.uint8)
RA, RB = raios(1.0), raios(2.0)
del xx, yy, dx, dy, r, ang, glow

# vinheta e grão (pré-calculados)
vy, vx = np.mgrid[0:OH, 0:OW].astype(np.float32)
v = ((vx - OW / 2) / (OW * 0.62)) ** 2 + ((vy - OH * 0.48) / (OH * 0.68)) ** 2
VIG = np.clip(1.0 - 0.42 * np.clip(v, 0, 1.6) ** 1.4, 0, 1)
rng = np.random.RandomState(7)
GRAO = [cv2.GaussianBlur(rng.randint(0, 255, (OH, OW), np.uint8), (0, 0), 0.6) for _ in range(6)]
GRAO = [cv2.merge([g, g, g]) for g in GRAO]

# ---------- câmera: (tempo, zoom, âncora x, âncora y) com transição suave ----------
K = [(0, 1.00, .50, .00), (12.7, 1.05, .32, .15), (40, 1.10, .42, .20), (69, 1.07, .72, .18),
     (83.3, 1.02, .50, .00), (111, 1.05, .50, .08), (114, 1.05, .78, .15), (141, 1.10, .66, .20),
     (155, 1.08, .36, .20), (168.5, 1.02, .50, .00), (196.2, 1.05, .42, .10), (199.5, 1.06, .18, .15),
     (227.7, 1.00, .50, .00), (254.3, 1.04, .48, .06), (258, 1.07, .40, .18), (DUR, 1.11, .42, .20)]
def ease(x): x = min(1, max(0, x)); return x * x * x * (x * (6 * x - 15) + 10)
def cam(t):
    for i in range(len(K) - 1):
        a, b = K[i], K[i + 1]
        if a[0] <= t <= b[0]:
            u = ease((t - a[0]) / (b[0] - a[0]))
            return [a[j] + (b[j] - a[j]) * u for j in (1, 2, 3)]
    return list(K[-1][1:])
def env(t, ini, fim, at=1.5, rl=2.5):
    if t < ini or t > fim + rl: return 0.0
    return ease((t - ini) / at) if t < fim else 1 - ease((t - fim) / rl)
def refrao(t): return max(env(t, a, b) for a, b in REFROES)

# ---------- poeira dourada (determinística) ----------
pr = np.random.RandomState(11); N = 260
PX, PY = pr.rand(N) * OW, pr.rand(N) * OH
PZ = pr.rand(N) ** 1.6                                 # 0 = longe, 1 = perto
PV = np.stack([18 + 30 * PZ, -6 - 10 * PZ], 1)        # vento: direita e para cima (px/s)
PPH = pr.rand(N) * 6.28; PF = 0.3 + pr.rand(N) * 0.8
def poeira(t, z, ox):
    small = np.zeros((OH // 2, OW // 2, 3), np.uint8); big = np.zeros((OH // 4, OW // 4, 3), np.uint8)
    x = (PX + PV[:, 0] * t + 14 * np.sin(PPH + t * PF) - ox * (0.3 + PZ)) % (OW + 80) - 40
    y = (PY + PV[:, 1] * t + 10 * np.cos(PPH * 1.3 + t * PF * .7)) % (OH + 80) - 40
    tw = 0.55 + 0.45 * np.sin(PPH * 3 + t * (1.5 + PF * 2))
    for i in range(N):
        b = tw[i] * (0.35 + 0.65 * (1 - abs(PZ[i] - 0.45))) * (1 + 0.6 * refrao(t))
        col = (int(90 * b), int(190 * b), int(255 * b))
        if PZ[i] > 0.82:                                    # perto: bokeh grande e desfocado
            cv2.circle(big, (int(x[i] / 4), int(y[i] / 4)), int(2 + 4 * PZ[i] * z), (int(col[0] * .5), int(col[1] * .5), int(col[2] * .5)), -1, cv2.LINE_AA)
        else:
            cv2.circle(small, (int(x[i] / 2), int(y[i] / 2)), 1 if PZ[i] < .5 else 2, col, -1, cv2.LINE_AA)
    small = cv2.GaussianBlur(small, (0, 0), 0.9); big = cv2.GaussianBlur(big, (0, 0), 2.2)
    return cv2.add(cv2.resize(small, (OW, OH), interpolation=cv2.INTER_LINEAR), cv2.resize(big, (OW, OH), interpolation=cv2.INTER_LINEAR))

def quadro(t):
    z, ax, ay = cam(t)
    rf = refrao(t)
    kg = 0.40 + 0.15 * math.sin(2 * math.pi * t / 6.4) + 0.18 * rf
    img = cv2.addWeighted(base, 1.0, GLOW, kg, 0)
    w = 0.5 + 0.5 * math.sin(2 * math.pi * t / 11.0)
    img = cv2.addWeighted(img, 1.0, RA, (0.30 + 0.3 * rf) * w, 0)
    img = cv2.addWeighted(img, 1.0, RB, (0.30 + 0.3 * rf) * (1 - w), 0)
    cw, ch = BW / z, BH / z
    x0 = ax * (BW - cw) + 2.0 * math.sin(t * 0.37) + 1.2 * math.sin(t * 0.91)     # "câmera na mão" sutil
    y0 = ay * (BH - ch) + 1.5 * math.sin(t * 0.29 + 1) + 0.8 * math.sin(t * 1.13)
    y0 = max(0.0, y0); x0 = min(max(0.0, x0), BW - cw)
    s = OW / cw
    M = np.float32([[s, 0, -x0 * s], [0, s, -y0 * s]])
    fr = cv2.warpAffine(img, M, (OW, OH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    fr = cv2.add(fr, poeira(t, z, x0 * s))
    # pulso na batida (só refrão) + fades
    pul = 0.0
    if rf > 0:
        k = np.searchsorted(BEATS, t) - 1
        if k >= 0: pul = 0.045 * rf * math.exp(-(t - BEATS[k]) / 0.22) * (1.0 if k % 2 == 0 else 0.5)
    fade = min(1.0, ease(t / 1.6), ease((DUR - t) / 2.5))
    g = VIG * ((1 + pul) * fade)
    fr = (fr.astype(np.float32) * g[..., None])
    fr = np.clip(fr, 0, 255).astype(np.uint8)
    fr = cv2.addWeighted(fr, 1.0, GRAO[int(t * FPS) % 6], 0.05, -0.05 * 127)
    return fr

if __name__ == "__main__":
    if os.environ.get("QUADRO"):
        for t in map(float, os.environ["QUADRO"].split(",")): cv2.imwrite(f"{P}/q_{t:.0f}.jpg", quadro(t), [cv2.IMWRITE_JPEG_QUALITY, 90])
        sys.exit()
    D = T1 - T0
    # loudnorm em dois passes (medido na música inteira)
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-i", f"{P}/musica.mp3", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(meas[meas.rfind("{"):meas.rfind("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
          f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000,"
          f"afade=t=out:st={DUR - T0 - 2.5:.2f}:d=2.5")
    inp = ["-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{OW}x{OH}", "-r", str(FPS), "-i", "-",
           "-ss", str(T0), "-t", str(D), "-i", f"{P}/musica.mp3"]
    fc = f"[0:v]setpts=PTS+{T0}/TB,ass={P}/karaoke.ass:fontsdir={P}/fontes,setpts=PTS-{T0}/TB[v0]"
    cur = "v0"
    for j, ts in enumerate(STICKERS):
        inp += ["-framerate", "30", "-i", f"{P}/sticker/s%03d.png"]
        fc += (f";[{j + 2}:v]scale=iw*0.66:-1,setpts=PTS+{ts - T0}/TB[s{j}]"
               f";[{cur}][s{j}]overlay=36:150:eof_action=pass[o{j}]"); cur = f"o{j}"
    fc += f";[{cur}]format=yuv420p[v]"
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", fc, "-map", "[v]", "-map", "1:a", "-af", af,
                           "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-tune", "film", "-r", str(FPS),
                           "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-t", str(D), OUT], stdin=subprocess.PIPE)
    n = int(round(D * FPS))
    for i in range(n):
        ff.stdin.write(quadro(T0 + i / FPS).tobytes())
        if i % 600 == 0: print(f"{i}/{n}", flush=True)
    ff.stdin.close(); ff.wait()
    print("ok", OUT)
