"""Shorts 9:16 (1080x1920) do clipe "NO DESERTO, ELE VENCEU", a partir da imagem VERTICAL do usuário.
Uso: python shorts.py <pasta> <imagem_vertical> <saida.mp4> <inicio_s> <fim_s>
Mesmo acabamento do clipe 16:9: câmera lenta (push-in), sol que respira (posição achada sozinha),
raios, poeira dourada, pulso de luz na batida no refrão, vinheta, grão;
título animado (cursiva + palavra amarela) que aparece no meio, SOBE e fica fixo no alto;
karaokê do mesmo karaoke.ass (recortado e deslocado, letras maiores, acima da área dos botões do Shorts);
sticker do canal 1 vez; áudio do trecho com -14 LUFS (2 passes), entrada/saída suaves. Limite 35 s."""
import sys, os, re, json, math, subprocess
import numpy as np, cv2
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ferramentas"))
from titulo_animado import Titulo, sobrepor

P, IMG, OUT, A, B = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
D = round(B - A, 3); assert D <= 35, "Short passou de 35 s"
FPS, OW, OH = 30, 1080, 1920
REFROES = [(83.3, 111.0), (168.5, 196.2), (227.7, 254.3)]
BEATS = np.load(f"{P}/batidas.npy")
CFG = json.loads(os.environ.get("CFG", "{}"))           # ajustes por imagem (posições)
TIT_Y = CFG.get("tit_y", 0.085); TIT_X = CFG.get("tit_x", 0.5); TIT_ESC = CFG.get("tit_esc", 0.8)
ST_Y = CFG.get("st_y", 0.60); LEG_MV = CFG.get("leg_mv", 380)

# ---------- base ----------
src = cv2.imread(IMG)
sc0 = max(OW / src.shape[1], OH / src.shape[0])           # cobre 1080x1920
BW, BH = int(round(src.shape[1] * sc0 * 1.12)), int(round(src.shape[0] * sc0 * 1.12))
base = cv2.resize(src, (BW, BH), interpolation=cv2.INTER_LANCZOS4)
# sol: ponto mais claro da metade de cima (desfocado)
lum = cv2.GaussianBlur(cv2.cvtColor(base, cv2.COLOR_BGR2GRAY).astype(np.float32), (0, 0), BW / 30)
lum[BH // 2:] = 0
sy_, sx_ = np.unravel_index(np.argmax(lum), lum.shape); SUN = (float(sx_), float(sy_))
yy, xx = np.mgrid[0:BH, 0:BW].astype(np.float32)
dx, dy = xx - SUN[0], yy - SUN[1]; r = np.sqrt(dx * dx + dy * dy)
warm = np.array([55, 140, 255], np.float32)
GLOW = np.clip(np.exp(-(r / (BW * 0.33)) ** 2)[..., None] * warm * 0.8 + np.exp(-(r / (BW * 0.9)) ** 2)[..., None] * warm * 0.2, 0, 255).astype(np.uint8)
ang = np.arctan2(dy, dx); ceu = np.clip((SUN[1] + BH * 0.18 - yy) / (BH * 0.15), 0, 1)
def raios(fase):
    rng = np.random.RandomState(int(fase * 10)); s = np.zeros_like(ang)
    for f, a in [(9, .5), (17, .3), (31, .2)]: s += a * (0.5 + 0.5 * np.cos(ang * f + rng.rand() * 6.28))
    return np.clip((s ** 3 * np.exp(-(r / (BW * 1.2))) * ceu)[..., None] * warm * 0.5, 0, 255).astype(np.uint8)
RA, RB = raios(1.0), raios(2.0)
del xx, yy, dx, dy, r, ang
vy, vx = np.mgrid[0:OH, 0:OW].astype(np.float32)
VIG = np.clip(1.0 - 0.40 * np.clip(((vx - OW / 2) / (OW * 0.66)) ** 2 + ((vy - OH * 0.48) / (OH * 0.62)) ** 2, 0, 1.6) ** 1.4, 0, 1)
rng = np.random.RandomState(7)
GRAO = [cv2.merge([g, g, g]) for g in (cv2.GaussianBlur(rng.randint(0, 255, (OH, OW), np.uint8), (0, 0), 0.6) for _ in range(6))]

def ease(x): x = min(1, max(0, x)); return x * x * x * (x * (6 * x - 15) + 10)
def env(t, ini, fim, at=1.0, rl=2.0):
    if t < ini or t > fim + rl: return 0.0
    return ease((t - ini) / at) if t < fim else 1 - ease((t - fim) / rl)
def refrao(ta): return max(env(ta, a, b) for a, b in REFROES)

# poeira
pr = np.random.RandomState(11); N = 240
PX, PY = pr.rand(N) * OW, pr.rand(N) * OH; PZ = pr.rand(N) ** 1.6
PV = np.stack([14 + 26 * PZ, -10 - 14 * PZ], 1); PPH = pr.rand(N) * 6.28; PF = 0.3 + pr.rand(N) * 0.8
def poeira(t, rf):
    small = np.zeros((OH // 2, OW // 2, 3), np.uint8); big = np.zeros((OH // 4, OW // 4, 3), np.uint8)
    x = (PX + PV[:, 0] * t + 14 * np.sin(PPH + t * PF)) % (OW + 80) - 40
    y = (PY + PV[:, 1] * t + 10 * np.cos(PPH * 1.3 + t * PF * .7)) % (OH + 80) - 40
    tw = 0.55 + 0.45 * np.sin(PPH * 3 + t * (1.5 + PF * 2))
    for i in range(N):
        b = tw[i] * (0.35 + 0.65 * (1 - abs(PZ[i] - 0.45))) * (1 + 0.6 * rf)
        col = (int(90 * b), int(190 * b), int(255 * b))
        if PZ[i] > 0.82: cv2.circle(big, (int(x[i] / 4), int(y[i] / 4)), int(2 + 4 * PZ[i]), tuple(int(c * .5) for c in col), -1, cv2.LINE_AA)
        else: cv2.circle(small, (int(x[i] / 2), int(y[i] / 2)), 1 if PZ[i] < .5 else 2, col, -1, cv2.LINE_AA)
    small = cv2.GaussianBlur(small, (0, 0), 0.9); big = cv2.GaussianBlur(big, (0, 0), 2.2)
    return cv2.add(cv2.resize(small, (OW, OH)), cv2.resize(big, (OW, OH)))

# título: aparece logo no começo, sobe e fica fixo no alto
TIT = Titulo(OW, OH, cursiva="No deserto,", forte="ELE VENCEU", linha="FIRE & GRACE", t0=0.15, cy=CFG.get("tit_cy", 0.42), tam=0.52,
             fixar=dict(t=2.9, dur=1.0, escala=TIT_ESC, y=TIT_Y, x=TIT_X))
TIT.dc = 0.07; TIT.tf = TIT.t0 + len(TIT.c) * TIT.dc + 0.2; TIT.df = 0.06; TIT.tl = TIT.tf + len(TIT.f) * TIT.df + 0.25
TIT.claroes = [(TIT.tc + 0.2, 0.7, 0.0), (TIT.tf + 0.15, 0.8, 1.7), (2.9 + 0.7, 0.8, 3.1)]

def quadro(t):
    ta = A + t; rf = refrao(ta)
    z = 1.0 + 0.09 * ease(t / D); ax = 0.5 + 0.12 * math.sin(t / D * math.pi - math.pi / 2) * 0.5; ay = 0.35
    kg = 0.38 + 0.14 * math.sin(2 * math.pi * t / 6.4) + 0.16 * rf
    img = cv2.addWeighted(base, 1.0, GLOW, kg, 0)
    w = 0.5 + 0.5 * math.sin(2 * math.pi * t / 11.0)
    img = cv2.addWeighted(img, 1.0, RA, (0.28 + 0.25 * rf) * w, 0); img = cv2.addWeighted(img, 1.0, RB, (0.28 + 0.25 * rf) * (1 - w), 0)
    cw = OW * 1.12 / z; ch = cw * OH / OW                # janela na base (base = imagem que cobre 1080x1920, x1,12)
    x0 = ax * (BW - cw) + 2.0 * math.sin(t * 0.37); y0 = ay * (BH - ch) + 1.5 * math.sin(t * 0.29 + 1)
    x0 = min(max(0.0, x0), BW - cw); y0 = min(max(0.0, y0), BH - ch)
    s = OW / cw
    fr = cv2.warpAffine(img, np.float32([[s, 0, -x0 * s], [0, s, -y0 * s]]), (OW, OH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    fr = cv2.add(fr, poeira(t, rf))
    pul = 0.0
    if rf > 0:
        k = np.searchsorted(BEATS, ta) - 1
        if k >= 0: pul = 0.045 * rf * math.exp(-(ta - BEATS[k]) / 0.22) * (1.0 if k % 2 == 0 else 0.5)
    fade = min(1.0, ease(t / 0.35), ease((D - t) / 1.2))
    fr = np.clip(fr.astype(np.float32) * (VIG * ((1 + pul) * fade))[..., None], 0, 255).astype(np.uint8)
    lz = TIT.clarao(t)
    if lz is not None: fr = cv2.add(fr, lz)
    tl = TIT.camada(t)
    if tl is not None: fr = sobrepor(fr, tl)
    return cv2.addWeighted(fr, 1.0, GRAO[int(t * FPS) % 6], 0.05, -0.05 * 127)

def ass_vertical():
    """recorta o karaoke.ass do clipe para o trecho, desloca os tempos e aumenta as letras"""
    def sec(x): h, m, s = x.split(":"); return int(h) * 3600 + int(m) * 60 + float(s)
    def ts(t): t = max(0, t); return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"
    out = []
    for ln in open(f"{P}/karaoke.ass"):
        if ln.startswith("PlayResX"): ln = "PlayResX: 1080\n"
        elif ln.startswith("PlayResY"): ln = "PlayResY: 1920\n"
        elif ln.startswith("Style: Letra"):
            f = ln.split(","); f[2] = "62"; f[16] = "5"; f[17] = "3"; f[19] = "50"; f[20] = "50"; f[21] = str(LEG_MV); ln = ",".join(f)
        elif ln.startswith("Dialogue"):
            f = ln.split(",", 9); a, b = sec(f[1]), sec(f[2])
            if b <= A or a >= B: continue
            na, nb = a - A, min(b, B) - A
            txt = f[9]
            if na < 0:                                    # trecho começou antes: tira o atraso do karaokê
                cut = int(round(-na * 100)); parts = re.split(r"(\{\\k[f]?\d+\})", txt); nt = ""
                for p in parts:
                    m = re.match(r"\{\\(kf?)(\d+)\}", p)
                    if m and cut > 0:
                        d = int(m.group(2)); u = min(d, cut); cut -= u; d -= u; p = f"{{\\{m.group(1)}{d}}}"
                    nt += p
                txt = nt; na = 0
            f[1], f[2], f[9] = ts(na), ts(nb), txt; ln = ",".join(f)
        out.append(ln)
    path = OUT.replace(".mp4", ".ass"); open(path, "w").writelines(out); return path

if __name__ == "__main__":
    if os.environ.get("QUADRO"):
        for t in map(float, os.environ["QUADRO"].split(",")): cv2.imwrite(OUT.replace(".mp4", f"_q{t:.1f}.jpg"), quadro(t), [cv2.IMWRITE_JPEG_QUALITY, 90])
        print("sol em", SUN, "base", BW, BH); sys.exit()
    ass = ass_vertical()
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(A), "-t", str(D), "-i", f"{P}/musica.mp3", "-af",
                           "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(meas[meas.rfind("{"):meas.rfind("}") + 1])
    af = (f"afade=t=in:st=0:d=0.3,afade=t=out:st={D - 1.2:.2f}:d=1.2,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:"
          f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000")
    st_t = CFG.get("st_t", 4.2); st_dir = f"{P}/sticker_fg"
    stw = cv2.imread(f"{st_dir}/s100.png", cv2.IMREAD_UNCHANGED).shape[1]; st_sc = 0.78; st_x = int((OW - stw * st_sc) / 2 + 20)
    fc = (f"[0:v]ass={ass}:fontsdir={P}/fontes[v0];[2:v]scale=iw*{st_sc}:-1,setpts=PTS+{st_t}/TB[st];"
          f"[v0][st]overlay={st_x}:{int(OH * ST_Y)}:eof_action=pass,format=yuv420p[v]")
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{OW}x{OH}", "-r", str(FPS), "-i", "-",
                           "-ss", str(A), "-t", str(D), "-i", f"{P}/musica.mp3", "-framerate", "30", "-i", f"{st_dir}/s%03d.png",
                           "-filter_complex", fc, "-map", "[v]", "-map", "1:a", "-af", af,
                           "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-tune", "film", "-r", str(FPS),
                           "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-t", str(D), OUT], stdin=subprocess.PIPE)
    for i in range(int(round(D * FPS))): ff.stdin.write(quadro(i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", OUT]))
    assert dur <= 35.05, f"{OUT}: {dur}"
    print(f"ok {OUT} {dur:.2f} s")
