"""Encaixa as frases do Will nos momentos da cena, abaixa o som do jogo enquanto ele fala (ducking)
e gera as legendas da narração (falas.json chave "W" + tmp/cap_W_<j>.png)."""
import json, subprocess, numpy as np, soundfile as sf, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S, E = 2776, 2804; SR = 48000; D = E - S
SEG_OLD = [(0.08, 2.54), (2.97, 5.48), (5.89, 9.18), (9.61, 11.03), (11.27, 13.10), (13.48, 14.25), (14.72, 15.25), (15.50, 16.68), (17.19, 17.65), (17.93, 18.97), (19.37, 19.88)]
TXT_OLD = ["Olha o que rolou nessa missão do GTA 6!", "Uma explosão gigante no meio do pântano...", "e aí aparece um atirador pendurado no helicóptero!",
       "O Doug agarra a Lori,", "mas o Jason mira com calma...", "e acerta!", "No final,", "todo mundo sai vivo.", "E você,", "teria feito diferente?", "Comenta aí!"]
SEG = [(2.30, 5.38), (5.88, 8.43), (9.14, 11.68), (12.71, 14.39), (14.68, 17.85), (18.77, 19.40), (19.74, 21.59), (22.14, 23.84), (24.09, 24.66)]
TXT = ["Olha só o que rolou nessa missão de GTA 6!", "Uma explosão gigante no meio do pântano...", "E aí aparece um atirador pendurado no helicóptero!",
       "O Doug agarra a Lori,", "mas o Jason mira com calma e acerta!", "No final,", "todo mundo sai vivo.", "E você, teria feito diferente?", "Comenta aí!"]
EM = [0.2, 3.4, 6.0, 8.9, 10.9, 21.2, 21.9, 24.0, 25.9]
EM_OLD = [0.2, 2.75, 5.5, 9.3, 11.0, 13.35, 21.2, 21.75, 23.4, 24.05, 25.35]      # onde cada frase começa no vídeo
def load(p, sr):
    return np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(sr), "-f", "f32le", "-"]), np.float32).reshape(-1, 2)
will = load("natan/voz_radio.wav", SR)
game = np.frombuffer(subprocess.check_output(["ffmpeg", "-v", "error", "-ss", str(S), "-t", str(D), "-i", "src/gameplay.mp4", "-vn", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]), np.float32).reshape(-1, 2).copy()
N = len(game); voz = np.zeros((N, 2), np.float32); mask = np.zeros(N, np.float32)
for (a, b), t in zip(SEG, EM):
    pa, pb = int((a - 0.05) * SR), int((b + 0.08) * SR); pt = int(t * SR); seg = will[pa:pb]
    voz[pt:pt + len(seg)] += seg[:N - pt]; mask[max(0, pt - int(0.15 * SR)):pt + len(seg) + int(0.25 * SR)] = 1
k = int(0.25 * SR); sm = np.convolve(np.convolve(mask, np.ones(k) / k, "same"), np.ones(k) / k, "same")
def rms(x): return np.sqrt((x ** 2).mean() + 1e-12)
gv = rms(voz[mask > 0.5]) / max(rms(game), 1e-6)
voz = voz / max(rms(voz[mask > 0.5]), 1e-6) * 0.12                                   # voz num nível fixo
game = game / max(rms(game), 1e-6) * 0.12 * (10 ** (-3 / 20))                       # jogo um pouco abaixo da voz
out = voz + game * (1 - sm * (1 - 10 ** (-13 / 20)))[:, None]                      # jogo −13 dB enquanto o Will fala
fo = int(0.6 * SR); out[-fo:] *= np.linspace(1, 0, fo)[:, None]
sf.write("natan/mix_natan.wav", out.astype(np.float32), SR)
# legendas: grupos de até 3 palavras, tempo proporcional às letras dentro de cada frase
KEY = {"gta", "6!", "explosão", "gigante", "pântano...", "atirador", "helicóptero!", "doug", "lori,", "jason", "acerta!", "vivo.", "diferente?", "comenta"}
F = ImageFont.truetype("/home/user/fonts/Montserrat.ttf", 64); F.set_variation_by_name("Black")
caps = []; j = 0
for (a, b), t, txt in zip(SEG, EM, TXT):
    ws = txt.split(); dur = b - a; tot = sum(len(w) for w in ws); acc = 0
    grupos = [ws[i:i + 3] for i in range(0, len(ws), 3)]
    for g in grupos:
        g0 = t + dur * acc / tot; acc += sum(len(w) for w in g); g1 = t + dur * acc / tot
        im = Image.new("RGBA", (1080, 300)); d = ImageDraw.Draw(im)
        sp = 18; wl = [d.textlength(w.upper(), font=F) for w in g]; x = (1080 - sum(wl) - sp * (len(g) - 1)) / 2
        for w, ww in zip(g, wl):
            cor = (245, 150, 40) if w.lower() in KEY else (255, 255, 255)
            d.text((x, 40), w.upper(), font=F, fill=cor, stroke_width=5, stroke_fill=(5, 12, 24)); x += ww + sp
        sh = Image.new("RGBA", im.size); sh.putalpha(im.split()[3].filter(ImageFilter.GaussianBlur(8)).point(lambda v: v * 160 // 255))
        Image.alpha_composite(sh, im).save(f"tmp/cap_N_{j}.png"); caps.append([round(g0, 2), round(max(g1, g0 + 0.35), 2), [["", " ".join(g)]]]); j += 1
f = json.load(open("falas.json")); f["N"] = caps; json.dump(f, open("falas.json", "w"), ensure_ascii=False, indent=0)
print("ok", j, "legendas")
