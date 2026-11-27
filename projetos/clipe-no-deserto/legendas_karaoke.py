"""Legendas karaokê (ASS, \\kf) a partir dos tempos palavra a palavra (palavras.json).
Uso: python legendas_karaoke.py <pasta>  -> <pasta>/karaoke.ass
Cada evento = um trecho da letra (frase, ou metade dela se for longa), em até 2 linhas.
A palavra se preenche de dourado no tempo em que é cantada."""
import json, sys, os
P = sys.argv[1]
# palavras_letra.json = texto da letra oficial + tempos da transcrição + marca de fim de linha da letra
LET = os.path.join(P, "palavras_letra.json")
W = json.load(open(LET)) if os.path.exists(LET) else [x + [False] for x in json.load(open(os.path.join(P, "palavras.json")))]

# trechos = versos da letra: dois versos curtos juntos (um em cada linha); verso longo sozinho
versos, cur = [], []
for w in W:
    cur.append(w)
    if w[3]: versos.append(cur); cur = []
if cur: versos.append(cur)
tam = lambda ws: len(" ".join(x[0] for x in ws))
evs, i = [], 0
while i < len(versos):
    v = versos[i]
    if (i + 1 < len(versos) and tam(v) <= 40 and tam(versos[i + 1]) <= 40 and tam(v) + tam(versos[i + 1]) <= 64
            and versos[i + 1][0][1] - v[-1][2] < 2.5):
        evs.append((v, versos[i + 1])); i += 2
    else:
        evs.append((v,)); i += 1

def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def linhas(grupo):
    """um verso por linha; um verso longo (>36) sozinho vira 2 linhas equilibradas"""
    if len(grupo) == 2: return list(grupo)
    ws = grupo[0]
    n = len(" ".join(x[0] for x in ws))
    if n <= 36: return [ws]
    best, k = 1e9, 1
    for i in range(1, len(ws)):
        a = len(" ".join(x[0] for x in ws[:i])); d = abs(a - n * 0.55) - (12 if ws[i - 1][3] else 4 if ws[i - 1][0][-1] in ",:" else 0)
        if d < best: best, k = d, i
    return [ws[:k], ws[k:]]

out = []
evs_w = [sum(g, []) for g in evs]
for i, (grupo, ws) in enumerate(zip(evs, evs_w)):
    ini = ws[0][1] - 0.45
    if i: ini = max(ini, evs_w[i - 1][-1][2] + 0.15)
    fim = ws[-1][2] + 0.9
    if i + 1 < len(evs): fim = min(fim, evs_w[i + 1][0][1] - 0.45)
    fim = max(fim, ws[-1][2] + 0.2)
    parts, t = [], ini
    lead = round((ws[0][1] - ini) * 100)
    if lead > 0: parts.append(f"{{\\k{lead}}}")
    rows = linhas(grupo)
    for r, row in enumerate(rows):
        for j, (w, a, b, _) in enumerate(row):
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
for g in evs: print(" | ".join(" ".join(x[0] for x in r) for r in linhas(g)))
