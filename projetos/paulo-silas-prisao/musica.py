"""Trilha original (instrumentos reais: piano Salamander + orquestra VSCO/VCSL) e ambiente para
"Paulo e Silas na prisão". Arco: tensão → esperança (louvor à meia-noite) → terremoto → suspense →
reflexão → paz. Gera audio/trilha.wav e audio/ambiente.wav (48 kHz)."""
import sys
sys.path.insert(0, "/root/lemo-opuscar")
import numpy as np, soundfile as sf
from core.audio import sampler as S
from core.audio import sfx as X
import linha as L

S.seed(16)
C = [c["ini"] for c in L.CENAS]; FIM = [c["fim"] for c in L.CENAS]; DUR = L.DUR + 1.0
T, G, CR, FN = L.T_TERREMOTO, L.T_GRITOU, L.T_CREIA, L.T_FINAL
ev = []
def E(t, inst, p, d, v, pan=0.0, g=1.0, **kw): ev.append(dict(t=t, inst=inst, pitch=p, dur=d, vel=v, pan=pan, gain=g, **kw))
def pad(t, d, notes, v=0.4, att=1.0, g=1.0):
    bass, cel, vla, vln = notes
    if bass: E(t, "contrabass", bass, d, v * 0.9, -0.1, g * 0.8, attack=att)
    if cel: E(t, "cellos", cel, d, v, -0.35, g, attack=att)
    if vla: E(t, "violas", vla, d, v * 0.9, 0.1, g * 0.85, attack=att)
    for i, n in enumerate(vln or []): E(t, "violins", n, d, v * 0.85, 0.35 - i * 0.15, g * 0.8, attack=att)
def seq(t0, t1, chords, v, att=1.0, g=1.0):
    st = (t1 - t0) / len(chords)
    for i, ch in enumerate(chords): pad(t0 + i * st, st + 0.3, ch, v=v, att=att, g=g)
    return st

# 1. A prisão — tensão (ré menor grave, pizzicato como passos, tímpano surdo)
st = seq(C[0] + 0.1, FIM[0], [("D2", "D3", "F3", None), ("Bb1", "D3", "F3", None), ("C2", "E3", "G3", None), ("A1", "E3", "A3", None)], 0.34, att=1.5)
t = C[0] + 0.4
while t < FIM[0] - 0.3:
    E(t, "cellos_pizz", "D3", 0.4, 0.32, -0.3, 0.7); E(t + 0.7, "contrabass_pizz", "A1", 0.4, 0.3, 0, 0.6); t += 1.4
for k in range(4): E(C[0] + 0.5 + k * 3.2, "timpani", "D2", 1.2, 0.22, 0, 0.5)
# 2. Louvor à meia-noite — esperança (fá maior, piano em arpejo e cordas que sobem)
st = seq(C[1] - 0.2, FIM[1], [("F2", "C3", "A3", ["F4"]), ("D2", "D3", "A3", ["F4"]), ("Bb1", "D3", "F3", ["D4", "F4"]), ("C2", "C3", "G3", ["E4", "G4"])], 0.34, att=1.2)
for i, ch in enumerate([["F3", "A3", "C4", "F4"], ["D3", "F3", "A3", "D4"], ["Bb2", "D3", "F3", "Bb3"], ["C3", "E3", "G3", "C4"]]):
    for j in range(2):
        for kk, n in enumerate(ch): E(C[1] + i * st + j * st / 2 + kk * 0.2, "piano", n, 1.4, 0.32, -0.15)
for i, n in enumerate(["C5", "D5", "F5", "E5", "C5", "D5"]): E(C[1] + 1.5 + i * (st * 4 - 2) / 6, "violin", n, 1.6, 0.36, 0.25, 0.7, attack=0.25)
# 3. Terremoto — subida, silêncio curto, impacto, brilho
SIL = T - 0.7
pad(C[2] - 0.3, SIL - C[2] + 0.3, ("C2", "C3", "G3", ["E4"]), v=0.45, att=0.8)
for j in range(int(1.6 / 0.07)): E(SIL - 1.6 + j * 0.07, "timpani", "C2", 0.12, 0.25 + 0.5 * j / 22, 0, 0.6)
E(T, "timpani", "D2", 2.5, 0.95, 0, 1.2); E(T, "gran_cassa", None, None, 0.9, 0, 1.0); E(T + 0.02, "sus_cymbal", None, None, 0.65, 0.2, 0.7)
for nm, p, pn in [("horn", "D4", -0.2), ("horn", "F4", 0.2), ("horn", "A3", 0), ("trombone", "D3", -0.1), ("tuba", "D2", 0)]: E(T, nm, p, 3.2, 0.78, pn, 0.85)
pad(T, 3.4, ("D2", "D3", "F3", ["A4", "D5"]), v=0.78, att=0.05, g=1.1)
seq(T + 3.3, FIM[2], [("Bb1", "D3", "F3", ["Bb4", "D5"]), ("C2", "E3", "G3", ["C5", "E5"]), ("D2", "A2", "F#3", ["A4", "D5"])], 0.6, att=0.4)
for i, n in enumerate(["D5", "F#5", "A5"]): E(FIM[2] - 1.6 + i * 0.12, "glockenspiel", n, 2.0, 0.3, 0.4, 0.5)
# 4. Carcereiro — suspense (lá menor, trêmulo) e pausa antes do grito de Paulo
pad(C[3] - 0.3, G - C[3] - 0.4, ("A1", "E3", "A3", ["C5"]), v=0.4, att=1.2)
E(C[3] + 1.0, "violins_trem", "E5", G - C[3] - 1.6, 0.32, 0.3, 0.6, attack=2.0)
E(C[3] + 3.0, "violins_trem", "F5", G - C[3] - 3.6, 0.28, -0.2, 0.5, attack=2.0)
seq(G + 0.05, FIM[3], [("F2", "C3", "A3", ["C5"]), ("G2", "D3", "B3", ["D5"]), ("C2", "C3", "G3", ["E5"])], 0.46, att=0.3)
E(G, "timpani", "A1", 1.5, 0.45, 0, 0.6)
# 5. A pergunta — reflexão (piano quase sozinho, cordas suaves)
st = seq(C[4] - 0.2, FIM[4], [("A1", "E3", "C4", None), ("F2", "C3", "A3", None), ("C2", "G2", "E3", None), ("G1", "D3", "B3", None)], 0.26, att=1.3)
for i, ch in enumerate([["A3", "C4", "E4"], ["F3", "A3", "C4"], ["C3", "E3", "G3"], ["G3", "B3", "D4"]]):
    for j in range(3): E(C[4] + 0.3 + i * st + j * st / 3, "piano", ch[j % 3], 2.0, 0.3, -0.1)
E(CR, "harp", "C5", 2.0, 0.4, 0.3, 0.6); E(CR + 0.15, "harp", "E5", 2.0, 0.38, 0.3, 0.6); E(CR + 0.3, "harp", "G5", 2.0, 0.36, 0.3, 0.6)
# 6. Nova vida — paz e esperança, cresce no final e resolve em ré maior
st = seq(C[5] - 0.2, FN, [("G1", "D3", "B3", ["D4"]), ("D2", "A2", "F#3", ["A4"]), ("E2", "B2", "G3", ["B4"]), ("C2", "G2", "E3", ["G4"]), ("D2", "A2", "F#3", ["F#4", "A4"])], 0.33, att=1.0)
for i, ch in enumerate([["G3", "B3", "D4"], ["D3", "F#3", "A3", "D4"], ["E3", "G3", "B3"], ["C3", "E3", "G3", "C4"], ["D3", "F#3", "A3"]]):
    for j in range(2): E(C[5] + 0.4 + i * st + j * st / 2, "piano", ch[j % len(ch)], 1.6, 0.3, -0.1)
seq(FN - 0.2, L.DUR - 0.3, [("G1", "D3", "B3", ["D5", "G5"]), ("A1", "E3", "C#4", ["E5", "A5"]), ("D2", "A2", "F#3", ["F#5", "A5", "D6"])], 0.5, att=0.6, g=1.05)
E(FN + 2.0, "horn", "D4", 4.0, 0.42, -0.3, 0.6, attack=0.8); E(FN + 2.0, "horn", "A3", 4.0, 0.4, 0.3, 0.6, attack=0.8)
for i, n in enumerate(["D6", "A5", "F#5", "D5", "A4", "F#4"]): E(L.DUR - 3.2 + i * 0.06, "harp", n, 2.5, 0.42, 0.35, 0.55)
E(L.DUR - 2.8, "glockenspiel", "A5", 2.2, 0.22, 0.3, 0.4)

mix = S.render(ev, dur=DUR); mix = S.room(mix, size=0.62, mix=0.24)
sf.write("audio/trilha.wav", mix.astype(np.float32), X.SR)
# ambiente discreto
amb = np.zeros((int(DUR * X.SR), 2), np.float32)
def place(sig, t, g, pan=0.0): X.add(amb, sig.astype(np.float32), t, g, pan)
def fade(sig, a, b):
    n = len(sig); e = np.ones(n); na, nb = int(a * X.SR), int(b * X.SR); e[:na] = np.linspace(0, 1, na); e[n - nb:] = np.linspace(1, 0, nb); return sig * e
d1 = FIM[0] + 0.5
place(fade(X.norm(X.bp(X.brown(d1), 200, 1500), 0.5), 0.5, 1.0), 0, 0.35, 0)           # multidão (murmúrio)
for k in (1, 3, 4, 5):                                                                    # cela: tochas estalando
    d = FIM[k] - C[k] + 0.9; tor = X.hp(X.noise(d), 2500) * (np.random.RandomState(k).rand(int(round(d * X.SR))) > 0.9985)
    place(fade(X.norm(X.lp(X.brown(d), 300) * 0.5 + tor * 3, 0.4), 0.5, 0.8), C[k] - 0.45, 0.22, 0.2)
place(fade(X.norm(X.rumble(4.5), 0.7), 0.3, 2.0), T - 0.4, 0.6, 0)                    # terremoto
place(X.norm(X.crash(), 0.6), T + 0.2, 0.35, -0.3)
sf.write("audio/ambiente.wav", amb, X.SR)
print("ok", round(DUR, 2), len(ev), "eventos")
