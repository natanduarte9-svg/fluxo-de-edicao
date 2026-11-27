"""Legendas karaokê (ASS, \\kf) a partir dos tempos palavra a palavra (palavras.json).
Uso: python legendas_karaoke.py <pasta>  -> <pasta>/karaoke.ass
Cada evento = um trecho da letra (frase, ou metade dela se for longa), em até 2 linhas.
A palavra se preenche de dourado no tempo em que é cantada."""
import json, sys, os
P = sys.argv[1]
W = json.load(open(os.path.join(P, "palavras.json")))
FIX = {"benção,": "bênção,"}                      # acentos que a transcrição errou
W = [[FIX.get(w, w), a, b] for w, a, b in W]

# 1) quebra em pedaços nas vírgulas/pontos; 2) junta pedaços até ~60 caracteres (sem passar do ponto final)
chunks, cur = [], []
for w in W:
    cur.append(w)
    if w[0][-1] in ",.:;!?":
        chunks.append((cur, w[0][-1] in ".!?")); cur = []
if cur: chunks.append((cur, True))
evs, cur = [], []
for ws, fim in chunks:
    txt = " ".join(x[0] for x in cur + ws)
    if cur and len(txt) > 60: evs.append(cur); cur = []
    cur = cur + ws
    if fim: evs.append(cur); cur = []
if cur: evs.append(cur)

def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def linhas(ws):
    """divide em 2 linhas equilibradas se passar de 30 caracteres"""
    n = len(" ".join(x[0] for x in ws))
    if n <= 30: return [ws]
    best, k = 1e9, 1
    for i in range(1, len(ws)):
        a = len(" ".join(x[0] for x in ws[:i])); d = abs(a - n / 2) - (4 if ws[i - 1][0][-1] in ",:" else 0)
        if d < best: best, k = d, i
    return [ws[:k], ws[k:]]

out = []
for i, ws in enumerate(evs):
    ini = ws[0][1] - 0.45
    if i: ini = max(ini, evs[i - 1][-1][2] + 0.15)
    fim = ws[-1][2] + 0.9
    if i + 1 < len(evs): fim = min(fim, evs[i + 1][0][1] - 0.45)
    fim = max(fim, ws[-1][2] + 0.2)
    parts, t = [], ini
    lead = round((ws[0][1] - ini) * 100)
    if lead > 0: parts.append(f"{{\\k{lead}}}")
    rows = linhas(ws)
    for r, row in enumerate(rows):
        for j, (w, a, b) in enumerate(row):
            k = rows[r][j + 1][1] if j + 1 < len(row) else (rows[r + 1][0][1] if r + 1 < len(rows) else b)
            dur = max(1, round((min(b, k) - a) * 100)); gap = round((k - a) * 100) - dur
            parts.append(f"{{\\kf{dur}}}{w}" + (f"{{\\k{gap}}}" if gap > 0 else "") + (" " if j + 1 < len(row) else ""))
        if r + 1 < len(rows): parts.append("\\N")
    out.append(f"Dialogue: 0,{ts(ini)},{ts(fim)},Letra,,0,0,0,,{{\\fad(180,220)}}" + "".join(parts))

HDR = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Letra,Cinzel Deserto,66,&H0046C8FF,&H00F2F6FA,&H00101826,&H96000000,0,0,0,0,100,100,1,0,1,4,3,2,80,80,58,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open(os.path.join(P, "karaoke.ass"), "w").write(HDR + "\n".join(out) + "\n")
print(len(out), "trechos")
for ws in evs[:6]: print(" | ".join(" ".join(x[0] for x in r) for r in linhas(ws)))
