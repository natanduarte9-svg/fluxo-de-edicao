"""Short do Jogatina Fácil a partir da gameplay longa.
Uso: python fazer_short.py <saida> <inicio_s> <fim_s> "<linha1>" "<linha2>" [n_falas]
- gameplay 16:9 no centro + cópia desfocada atrás (1080x1920);
- título em 2 linhas (y 410/515) abaixo do sticker; sticker "Inscreva-se" 5,6 s a partir de 1,0 s;
- falas do jogo GRANDES na faixa de baixo (tmp/cap_<n>_<j>.png + tempos em falas.json), se n_falas;
- só o som do jogo, -14 LUFS em dois passes; nada acelerado. Confere a duração no final."""
import sys, json, subprocess
out, S, E, L1, L2 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5]
n = sys.argv[6] if len(sys.argv) > 6 else None
D = round(E - S, 3); FO = D - 0.5
SRC = "src/gameplay.mp4"; FONT = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
open("tmp/l1.txt", "w").write(L1); open("tmp/l2.txt", "w").write(L2)
fz = "if(lt(t,0.25),40+t*200,90)"
fc = ("[0:v]split=2[a][b];"
      "[a]scale=-2:1920,crop=1080:1920,boxblur=24:3,eq=brightness=-0.12:saturation=1.1[bg];"
      "[b]scale=1080:-2:flags=lanczos[fg];[bg][fg]overlay=0:(H-h)/2[v0];"
      f"[v0]drawtext=fontfile={FONT}:textfile=tmp/l1.txt:fontsize='{fz}':fontcolor=white:borderw=8:bordercolor=black:x=(w-text_w)/2:y=410,"
      f"drawtext=fontfile={FONT}:textfile=tmp/l2.txt:fontsize='{fz}':fontcolor=0xFFD21F:borderw=8:bordercolor=black:x=(w-text_w)/2:y=515[v1];"
      "[1:v]setpts=PTS+1.0/TB[st];[v1][st]overlay=160:110:eof_action=pass[c]")
inputs = ["-ss", str(S), "-t", str(D), "-i", SRC, "-framerate", "30", "-i", "sticker/s%03d.png"]
cur = "c"
if n:
    for j, (a, b, _) in enumerate(json.load(open("falas.json"))[n]):
        inputs += ["-loop", "1", "-framerate", "30", "-t", str(D), "-i", f"tmp/cap_{n}_{j}.png"]
        fc += f";[{cur}][{j + 2}:v]overlay=0:1290:enable='between(t,{a},{min(b, D)})'[k{j}]"; cur = f"k{j}"
fc += f";[{cur}]fade=t=in:st=0:d=0.15,fade=t=out:st={FO}:d=0.5,format=yuv420p[v]"
meas = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(S), "-t", str(D), "-i", SRC, "-vn", "-af",
                       "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
m = json.loads(meas[meas.rfind("{"):meas.rfind("}") + 1])
af = (f"afade=t=in:st=0:d=0.1,afade=t=out:st={FO}:d=0.5,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:"
      f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "0:a", "-af", af,
                "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-r", "30", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", "-t", str(D), out], check=True)
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]))
LIM = float(__import__("os").environ.get("LIMITE", "30")); assert dur <= LIM, f"{out} passou de {LIM} s: {dur}"
print(f"ok {out} {dur:.2f} s")
