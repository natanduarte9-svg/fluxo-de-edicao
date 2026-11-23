"""Mixagem: voz em primeiro plano; trilha e ambiente abaixam sozinhos durante a fala (ducking). Gera mix.wav."""
import sys, subprocess, io
sys.path.insert(0, "/root/lemo-opuscar")
import numpy as np, soundfile as sf
from scipy.ndimage import uniform_filter1d
from core.audio import sfx as X
import linha as L
SR = X.SR
def db(x): return 10 ** (x / 20)
def load_mp3(p):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"])
    return np.frombuffer(raw, np.float32)

mus, _ = sf.read("trilha.wav", dtype="float32"); amb, _ = sf.read("ambiente.wav", dtype="float32")
N = int((L.DUR + 0.3) * SR)
mus = np.pad(mus, ((0, max(0, N - len(mus))), (0, 0)))[:N]; amb = np.pad(amb, ((0, max(0, N - len(amb))), (0, 0)))[:N]

# voz
voz = np.zeros(N, np.float32)
for i, c in enumerate(L.CENAS, 1):
    v = load_mp3(f"voz/f{i}.mp3"); a = int(c["voz_em"] * SR); voz[a:a + len(v)] += v[:N - a]
voz = X.hp(voz, 85); voz = X.compress(voz, thr=0.2, ratio=2.5)
voz = voz / np.abs(voz).max() * 0.85

# onde há fala (juntando pausas curtas)
speech = np.zeros(N, bool)
for c in L.CENAS:
    ws = c["words"]; s0 = ws[0][1]; e0 = ws[0][2]
    for _, a, b in ws[1:]:
        if a - e0 < 0.45: e0 = b
        else: speech[int((s0 - 0.15) * SR):int((e0 + 0.3) * SR)] = True; s0, e0 = a, b
    speech[int((s0 - 0.15) * SR):int((e0 + 0.3) * SR)] = True
k = int(0.3 * SR); sp = uniform_filter1d(uniform_filter1d(speech.astype(np.float32), k), k)   # curva suave 0..1

v_rms = np.sqrt((voz[speech] ** 2).mean())
def env(x):
    e = np.sqrt(uniform_filter1d((x.mean(1) ** 2), int(0.25 * SR)) + 1e-10)
    return uniform_filter1d(e, int(0.25 * SR))
me = env(mus); med = np.median(me[me > 1e-4])
# sob a fala: trilha a ~ -18 dB da voz (≈12%), dinâmica comprimida; nos intervalos: ~ -8 dB, dinâmica quase livre
g_speech = v_rms * db(-18) / med * (me / med) ** (0.35 - 1)
g_gap = v_rms * db(-8.5) / med * (me / med) ** (0.75 - 1)
g = np.minimum(g_speech, 4) * sp + np.minimum(g_gap, 6) * (1 - sp)
g = uniform_filter1d(g, int(0.12 * SR))
ae = env(amb); amed = np.median(ae[ae > 1e-5]) if (ae > 1e-5).any() else 1
ga = (v_rms * db(-26) / amed) * sp + (v_rms * db(-15) / amed) * (1 - sp)

out = voz[:, None] * np.array([1, 1], np.float32) + mus * g[:, None] + amb * ga[:, None]
# fade final junto com a imagem
nf = int(0.9 * SR); e = int(L.DUR * SR); out[e - nf:e] *= np.linspace(1, 0, nf)[:, None]; out[e:] = 0
out = X.limit(out.astype(np.float32), ceil=0.95)
sf.write("mix.wav", out, SR)
# conferência: quanto a trilha fica abaixo da voz durante a fala
mr = np.sqrt(((mus * g[:, None]).mean(1)[speech] ** 2).mean())
print("trilha sob a voz: %.1f dB (%.0f%%)" % (20 * np.log10(mr / v_rms), 100 * mr / v_rms))
