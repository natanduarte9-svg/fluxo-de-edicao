"""Trilha original (instrumentos reais gravados, VSCO 2 CE + Salamander) e ambiente, no tempo das cenas.
Gera trilha.wav e ambiente.wav (48 kHz estéreo)."""
import sys, os
sys.path.insert(0, "/root/lemo-opuscar")
import numpy as np, soundfile as sf
from core.audio import sampler as S
from core.audio import sfx as X
import linha as L

S.seed(11)
C = [c["ini"] for c in L.CENAS]; DUR = L.DUR + 1.0
F, R = L.T_FOGO, L.T_REDEMOINHO
ev = []
def E(t, inst, p, d, v, pan=0.0, g=1.0, **kw):
    ev.append(dict(t=t, inst=inst, pitch=p, dur=d, vel=v, pan=pan, gain=g, **kw))

def pad(t, d, notes, v=0.45, att=1.2, g=1.0):
    """acorde de cordas: (contrabaixo, violoncelos, violas, violinos)"""
    bass, cel, vla, vln = notes
    if bass: E(t, "contrabass", bass, d, v * 0.9, -0.1, g * 0.8, attack=att)
    if cel: E(t, "cellos", cel, d, v, -0.35, g, attack=att)
    if vla: E(t, "violas", vla, d, v * 0.9, 0.1, g * 0.85, attack=att)
    for i, n in enumerate(vln or []): E(t, "violins", n, d, v * 0.85, 0.35 - i * 0.15, g * 0.8, attack=att)

def piano(t, notes, v=0.5, gap=0.0, d=2.5, pan=-0.15):
    for i, n in enumerate(notes): E(t + i * gap, "piano", n, d, v, pan)

# ---------------- 1. Diante do rei Acabe (curiosidade) ----------------
t0 = C[0]
seq = [("D2", "D3", "A3", ["F4"]), ("Bb1", "D3", "F3", ["D4"]), ("F2", "C3", "A3", ["C4"]), ("A1", "E3", "A3", ["C#4"])]
S1 = (C[1] - C[0]) / 4
for i, ch in enumerate(seq): pad(t0 + 0.2 + i * S1, S1 + 0.2, ch, v=0.38, att=1.4 if i == 0 else 0.8)
for i, n in enumerate(["A4", "D5", "F5", "E5", "D5", "C5", "A4", "Bb4", "A4", "E5"]):
    piano(t0 + 0.5 + i * (C[1] - C[0] - 1.0) / 10, [n], v=0.42)

# ---------------- 2. Ribeiro de Querite (contemplativo) ----------------
t0 = C[1]
seq = [("D2", "D3", "F3", ["A4"]), ("Bb1", "D3", "F3", ["Bb4"]), ("G1", "D3", "G3", ["Bb4"]), ("A1", "C#3", "E3", ["A4"])]
S2 = (C[2] - C[1]) / 4
for i, ch in enumerate(seq): pad(t0 - 0.2 + i * S2, S2 + 0.25, ch, v=0.33, att=1.0)
arp = [["D4", "F4", "A4", "D5"], ["D4", "F4", "Bb4", "D5"], ["D4", "G4", "Bb4", "D5"], ["C#4", "E4", "A4", "C#5"]]
for i, a in enumerate(arp):
    for j in range(2):
        for kk, n in enumerate(a): E(t0 + i * S2 + j * S2 / 2 + kk * 0.18, "harp", n, 1.4, 0.42, 0.3)

# ---------------- 3. Monte Carmelo (cresce até o fogo) ----------------
t0 = C[2]
pad(t0 - 0.3, 4.6, ("D2", "D3", "A3", ["D4"]), v=0.4)
pad(t0 + 4.3, 4.5, ("Bb1", "D3", "F3", ["F4"]), v=0.48)
# ostinato de violoncelos a partir de 25,8 s, cada vez mais forte, para antes do silêncio
step = 0.3; t = t0 + 3.2; i = 0
SIL = F - 0.75   # silêncio antes do fogo
while t < SIL:
    k = (t - (t0 + 3.2)) / (SIL - (t0 + 3.2))
    E(t, "cellos_spic", "D3" if i % 4 != 3 else "A2", 0.25, 0.35 + 0.45 * k, -0.3, 0.9)
    E(t, "contrabass_pizz", "D2", 0.3, 0.3 + 0.4 * k, 0, 0.7) if i % 2 == 0 else None
    t += step; i += 1
E(t0 + 3.5, "violins_trem", "A4", SIL - (t0 + 3.5), 0.35, 0.3, 0.8, attack=2.5)
E(t0 + 5.0, "violins_trem", "D5", SIL - (t0 + 5.0), 0.3, -0.2, 0.7, attack=3.0)
E(SIL - 3.0, "timpani", "D2", 3.0, 0.55, 0, 0.8, var="roll") if False else None
for j in range(int(3.0 / 0.07)):   # rufar dos tímpanos crescendo
    tt = SIL - 3.0 + j * 0.07; E(tt, "timpani", "D2", 0.12, 0.25 + 0.5 * j / 43, 0, 0.6)
# IMPACTO 1: o fogo cai
E(F, "timpani", "D2", 2.5, 0.95, 0, 1.2); E(F, "gran_cassa", None, None, 0.9, 0, 1.0)
E(F + 0.02, "sus_cymbal", None, None, 0.7, 0.2, 0.7)
for nm, p, pn in [("horn", "D4", -0.2), ("horn", "F#4", 0.2), ("horn", "A3", 0), ("trombone", "D3", -0.1), ("tuba", "D2", 0)]:
    E(F, nm, p, 3.6, 0.8, pn, 0.85)
pad(F, 3.8, ("D2", "D3", "F#3", ["A4", "D5"]), v=0.8, att=0.05, g=1.1)
pad(F + 3.6, 2.6, ("G1", "D3", "G3", ["B4", "D5"]), v=0.6, att=0.4)
pad(F + 6.1, 3.0, ("D2", "A2", "F#3", ["A4", "D5"]), v=0.55, att=0.4)
for i, n in enumerate(["D5", "F#5", "A5"]): E(F + 0.1 + i * 0.12, "glockenspiel", n, 2.0, 0.35, 0.4, 0.5)

# ---------------- 4. Deserto (emocional, delicado) ----------------
t0 = C[3]
seq = [("G1", "D3", "Bb3", None), ("Eb2", "Eb3", "G3", None), ("Bb1", "D3", "F3", None), ("F2", "C3", "A3", None)]
S4 = (C[4] - C[3]) / 4
for i, ch in enumerate(seq): pad(t0 + i * S4, S4 + 0.3, ch, v=0.28, att=1.3)
for i, ch in enumerate([["G3", "Bb3", "D4"], ["Eb3", "G3", "Bb3"], ["D3", "F3", "Bb3"], ["C3", "F3", "A3"]]):
    for j in range(3): piano(t0 + 0.3 + i * S4 + j * S4 / 3, [ch[j % 3], ch[(j + 1) % 3]], v=0.32, gap=0.35, d=2.0)
for t, n, d in [(1.5, "D5", 1.6), (3.2, "C5", 1.4), (4.8, "Bb4", 2.6), (8.0, "A4", 1.6), (9.8, "Bb4", 1.2), (11.2, "C5", 2.2)]:
    E(t0 + t * S4 / 3.3, "violin", n, d * S4 / 3.3, 0.42, 0.25, 0.75, attack=0.25)

# ---------------- 5. Chamado de Eliseu (esperança) ----------------
t0 = C[4]
seq = [("F2", "C3", "A3", ["F4"]), ("C2", "C3", "G3", ["E4"]), ("D2", "D3", "A3", ["F4"]), ("Bb1", "D3", "F3", ["D4", "F4"])]
S5 = (C[5] - C[4]) / 4
for i, ch in enumerate(seq): pad(t0 - 0.3 + i * S5, S5 + 0.25, ch, v=0.36 + i * 0.04, att=0.9)
for i, ch in enumerate([["F3", "A3", "C4", "F4"], ["E3", "G3", "C4", "E4"], ["D3", "F3", "A3", "D4"], ["D3", "F3", "Bb3", "D4"]]):
    for j in range(2):
        for kk, n in enumerate(ch): E(t0 + i * S5 + j * S5 / 2 + kk * 0.2, "piano", n, 1.2, 0.33, -0.1)
E(t0 + 2.0, "horn", "C4", 2.5, 0.3, -0.3, 0.55, attack=0.6); E(t0 + 3 * S5, "horn", "D4", 2.6, 0.32, -0.3, 0.55, attack=0.6)

# ---------------- 6. Subida ao céu (grandioso) ----------------
t0 = C[5]
pad(t0 - 0.3, 3.5, ("D2", "D3", "A3", ["D4"]), v=0.42)
pad(t0 + 3.0, R - (t0 + 3.0) + 0.2, ("Bb1", "D3", "F3", ["F4", "Bb4"]), v=0.5, att=2.0)
E(t0 + 3.0, "violins_trem", "F5", R - t0 - 3.0, 0.4, 0.3, 0.7, attack=2.5)
for j in range(int(2.2 / 0.07)):
    tt = R - 2.2 + j * 0.07; E(tt, "timpani", "A1", 0.12, 0.25 + 0.45 * j / 31, 0, 0.6)
# IMPACTO 2: redemoinho
E(R, "timpani", "D2", 2.5, 0.9, 0, 1.1); E(R + 0.02, "sus_cymbal", None, None, 0.65, -0.2, 0.7)
grand = [(0.0, ("D2", "D3", "F#3", ["A4", "D5"]), ["D4", "F#4", "A3"]), (2.6, ("G1", "D3", "G3", ["B4", "D5"]), ["D4", "G4", "B3"]),
         (5.0, ("B1", "D3", "F#3", ["B4", "F#5"]), ["D4", "F#4", "B3"]), (7.0, ("A1", "C#3", "E3", ["A4", "E5"]), ["C#4", "E4", "A3"])]
for dt, ch, hn in grand:
    pad(R + dt, 2.8 if dt < 7 else R - R + 2.6, ch, v=0.72, att=0.15 if dt == 0 else 0.4, g=1.05)
    for kk, n in enumerate(hn): E(R + dt, "horn", n, 2.7, 0.62, -0.3 + kk * 0.3, 0.75)
    E(R + dt, "trombone", ch[1], 2.7, 0.5, 0, 0.6); E(R + dt, "timpani", ch[0][:-1] + "2" if ch[0][0] in "DA" else "D2", 1.5, 0.5, 0, 0.6)
for i, n in enumerate(["D6", "A5", "F#5", "D5", "A4", "F#4", "D4"]): E(R + 0.05 + i * 0.05, "harp", n, 2.0, 0.5, 0.35, 0.6)

# ---------------- 7. Convite (suave, acolhedor) ----------------
t0 = C[6]
seq = [("D2", "D3", "A3", ["F#4"]), ("C#2", "E3", "A3", ["E4"]), ("B1", "D3", "F#3", ["D4"]), ("G1", "D3", "G3", ["B3", "D4"]),
       ("D2", "A2", "F#3", ["A3", "D4"])]
S7 = (L.DUR - C[6] - 1.0) / 5
for i, ch in enumerate(seq): pad(t0 + 0.2 + i * S7, S7 + 0.5 if i < 4 else S7 + 1.5, ch, v=0.3, att=1.0)
for i, ch in enumerate([["D4", "F#4", "A4"], ["C#4", "E4", "A4"], ["B3", "D4", "F#4"], ["G3", "B3", "D4"], ["D4", "F#4", "A4", "D5"]]):
    for j in range(2): piano(t0 + 0.4 + i * S7 + j * S7 / 2, ch, v=0.3, gap=0.16, d=1.6)
E(L.DUR - 2.2, "glockenspiel", "A5", 2.0, 0.25, 0.3, 0.4); E(L.DUR - 1.9, "glockenspiel", "D6", 2.0, 0.22, 0.3, 0.4)

ev = [e for e in ev if e is not None]
mix = S.render(ev, dur=DUR)
mix = S.room(mix, size=0.62, mix=0.24)
sf.write("trilha.wav", mix.astype(np.float32), X.SR)

# ---------------- ambiente (bem baixo) ----------------
amb = np.zeros((int(DUR * X.SR), 2), np.float32)
def place(sig, t, g, pan=0.0): X.add(amb, sig.astype(np.float32), t, g, pan)
def fade(sig, a, b):
    n = len(sig); e = np.ones(n); na, nb = int(a * X.SR), int(b * X.SR)
    e[:na] = np.linspace(0, 1, na); e[n - nb:] = np.linspace(1, 0, nb); return sig * e
c2 = L.CENAS[1]; d2 = c2["fim"] - c2["ini"] + 0.9
river = X.bp(X.noise(d2), 300, 3500) * 0.5 + X.hp(X.noise(d2), 3000) * 0.15
place(fade(X.norm(river, 0.5), 1.0, 1.0), c2["ini"] - 0.45, 0.35, -0.2)
c3 = L.CENAS[2]
place(fade(X.norm(X.roar(c3["fim"] - F + 0.5), 0.6), 0.05, 1.5), F, 0.55, 0.0)
place(X.norm(X.ignite(), 0.8), F - 0.05, 0.6, 0.0)
place(fade(X.norm(X.lp(X.brown(3.0), 400), 0.5), 0.1, 1.0), F, 0.5, 0)
c6 = L.CENAS[5]; d6 = c6["fim"] - c6["ini"] + 0.9
wind = X.bp(X.brown(d6) if hasattr(X, "brown") else X.noise(d6), 150, 1200)
place(fade(X.norm(wind, 0.5), 2.0, 1.5), c6["ini"] - 0.45, 0.4, 0.15)
place(fade(X.norm(X.roar(6.0), 0.6), 0.6, 2.5), R - 0.2, 0.4, 0.0)
sf.write("ambiente.wav", amb, X.SR)
print("ok", DUR, len(ev), "eventos")
