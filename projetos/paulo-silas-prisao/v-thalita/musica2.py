"""Trilha 2 (pedido do usuário): contínua, emocional e acolhedora. Piano com arpejo e melodia sobre cordas
quentes, progressão si menor → sol → ré → lá (vi–IV–I–V em ré maior), ~66 BPM, crescendo por cena.
O terremoto cai numa troca de acorde (grade alinhada). Gera audio/trilha.wav e audio/ambiente.wav."""
import sys
sys.path.insert(0, "/root/lemo-opuscar")
import numpy as np, soundfile as sf
from core.audio import sampler as S
from core.audio import sfx as X
import linha as L

S.seed(21)
C = [c["ini"] for c in L.CENAS]; FIM = [c["fim"] for c in L.CENAS]; DUR = L.DUR + 1.5
T = L.T_TERREMOTO
BEAT = 60 / 66; BAR = 4 * BEAT                     # um acorde por compasso
t0 = (T % BAR) - BAR if (T % BAR) > 0.5 else (T % BAR)   # grade alinhada: um compasso começa no terremoto
t0 -= BAR * 0                                      # (t0 pode ser negativo: o 1º compasso começa antes do 0)
# acordes: (baixo, notas do piano, notas das cordas)
CH = {"Bm": ("B1", ["B2", "F#3", "B3", "D4", "F#4"], ["B2", "F#3", "D4"]),
      "G": ("G1", ["G2", "D3", "G3", "B3", "D4"], ["G2", "D3", "B3"]),
      "D": ("D2", ["D3", "A3", "D4", "F#4", "A4"], ["D3", "A3", "F#4"]),
      "A": ("A1", ["A2", "E3", "A3", "C#4", "E4"], ["A2", "E3", "C#4"]),
      "Em": ("E2", ["E3", "B3", "E4", "G4", "B4"], ["E3", "B3", "G4"]),
      "F#m": ("F#1", ["F#2", "C#3", "F#3", "A3", "C#4"], ["F#2", "C#3", "A3"])}
PROG = ["Bm", "G", "D", "A", "Bm", "G", "Em", "A", "G", "D", "A", "Bm", "G", "D", "Em", "A"]
# melodia do piano (mão direita): uma nota por tempo forte, por acorde (motivo que volta)
MEL = {"Bm": ["D5", "C#5", "B4", "F#4"], "G": ["B4", "A4", "G4", "D5"], "D": ["A4", "F#4", "D5", "A4"],
       "A": ["C#5", "E5", "A4", "C#5"], "Em": ["G4", "B4", "E5", "D5"], "F#m": ["A4", "C#5", "F#4", "A4"]}
def secao(t):
    for k in range(len(C) - 1, -1, -1):
        if t >= C[k] - 0.3: return k + 1
    return 1
# intensidade por cena (0..1): começa íntimo, cresce no louvor, pico no terremoto, respira, abre no final
INT = {1: 0.30, 2: 0.48, 3: 0.82, 4: 0.50, 5: 0.55, 6: 0.80, 7: 0.55}
ev = []
def E(t, inst, p, d, v, pan=0.0, g=1.0, **kw):
    if t < 0: return
    ev.append(dict(t=t, inst=inst, pitch=p, dur=d, vel=v, pan=pan, gain=g, **kw))
n = int((DUR - t0) / BAR) + 1
for i in range(n):
    ts = t0 + i * BAR
    if ts > L.DUR - 0.5: break
    k = secao(max(ts, 0)); I = INT[k]
    name = PROG[i % len(PROG)]
    if ts + BAR > L.DUR - 0.6: name = "D"                                 # resolve em ré maior
    bass, pn, st = CH[name]
    # piano: arpejo em colcheias (8 por compasso), mão esquerda grave
    E(ts, "piano", bass[:-1] + str(int(bass[-1]) + 1), BAR, 0.38 + 0.15 * I, -0.2)
    arp = [pn[0], pn[1], pn[2], pn[3], pn[4], pn[3], pn[2], pn[1]]
    for j, nt in enumerate(arp): E(ts + j * BEAT / 2, "piano", nt, BEAT * 1.6, 0.20 + 0.14 * I, -0.15 + 0.04 * j)
    # melodia (a partir do louvor), mais presente no final
    if k >= 2:
        for j, nt in enumerate(MEL[name]):
            E(ts + j * BEAT, "piano", nt, BEAT * 1.8, 0.30 + 0.2 * I, 0.1)
    # cordas quentes (entram devagar e crescem)
    E(ts, "contrabass", bass, BAR + 0.4, 0.25 + 0.35 * I, 0, 0.7, attack=0.8)
    E(ts, "cellos", st[0] if k >= 2 else bass[:-1] + str(int(bass[-1]) + 1), BAR + 0.4, 0.28 + 0.4 * I, -0.35, 0.9, attack=0.9)
    E(ts, "violas", st[1], BAR + 0.4, 0.22 + 0.4 * I, 0.1, 0.8, attack=1.0)
    if k >= 3 or k == 6: E(ts, "violins", st[2], BAR + 0.4, 0.2 + 0.45 * I, 0.35, 0.8, attack=1.0)
    # linha do violoncelo (louvor) e dos violinos (final): melodia longa
    if k == 2 and i % 2 == 0: E(ts, "cello" if False else "cellos", MEL[name][0][:-1] + "3", BAR * 2, 0.32, -0.3, 0.8, attack=0.6)
    if k in (6, 7): E(ts + BEAT, "violins", MEL[name][0], BAR - BEAT + 0.3, 0.32 + 0.25 * I, 0.3, 0.85, attack=0.5)
# terremoto: subida nas cordas e no tímpano antes, impacto quente (sem metais estridentes)
for j in range(int(2.0 / 0.08)): E(T - 2.0 + j * 0.08, "timpani", "D2", 0.12, 0.18 + 0.5 * j / 25, 0, 0.55)
E(T - 3.0, "violins_trem", "F#4", 3.0, 0.32, 0.3, 0.7, attack=2.5)
E(T, "timpani", "B1", 2.5, 0.85, 0, 1.0); E(T + 0.02, "sus_cymbal", None, None, 0.45, 0.2, 0.55); E(T, "gran_cassa", None, None, 0.6, 0, 0.7)
E(T, "horn", "D4", 3.5, 0.5, -0.2, 0.6, attack=0.2); E(T, "horn", "F#4", 3.5, 0.45, 0.2, 0.55, attack=0.2)
# final: harpa e sino suave
for i, nt in enumerate(["D6", "A5", "F#5", "D5", "A4", "F#4"]): E(L.DUR - 3.0 + i * 0.07, "harp", nt, 2.5, 0.4, 0.35, 0.55)
E(L.DUR - 2.6, "glockenspiel", "F#5", 2.4, 0.2, 0.3, 0.35)
mix = S.render(ev, dur=DUR); mix = S.room(mix, size=0.7, mix=0.3)
# fade de entrada e de saída suaves
nf = int(1.2 * X.SR); mix[:nf] *= np.linspace(0, 1, nf)[:, None]
ne = int(L.DUR * X.SR); nfo = int(2.0 * X.SR); mix[ne - nfo:ne] *= np.linspace(1, 0, nfo)[:, None]; mix[ne:] = 0
sf.write("audio/trilha.wav", mix.astype(np.float32), X.SR)
amb = np.zeros((int(DUR * X.SR), 2), np.float32)
r = X.lp(X.rumble(4.5), 180); r = X.norm(r, 0.7); e = np.ones(len(r)); e[:int(.3 * X.SR)] = np.linspace(0, 1, int(.3 * X.SR)); e[-int(2 * X.SR):] = np.linspace(1, 0, int(2 * X.SR))
X.add(amb, (r * e).astype(np.float32), T - 0.4, 0.5, 0)
sf.write("audio/ambiente.wav", amb, X.SR)
print("ok", len(ev), "eventos, grade", round(t0, 2), "compasso", round(BAR, 2))
