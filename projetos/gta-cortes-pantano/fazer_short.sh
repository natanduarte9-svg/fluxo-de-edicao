#!/bin/bash
# fazer_short.sh <saida> <inicio_s> <fim_s> "<linha1>" "<linha2>"
# gameplay 16:9 no centro + cópia desfocada atrás (1080x1920), título em 2 linhas abaixo do sticker,
# sticker "Inscreva-se" (5,6 s a partir de 1,0 s), som do jogo a -14 LUFS. Sem acelerar nada.
set -e
SRC=src/gameplay.mp4; OUT=$1; S=$2; E=$3
D=$(python3 -c "print($E-$S)"); FO=$(python3 -c "print($E-$S-0.5)")
FONT=/usr/share/fonts/opentype/inter/InterDisplay-Black.otf
mkdir -p tmp; printf '%s' "$4" > tmp/l1.txt; printf '%s' "$5" > tmp/l2.txt
VF="[0:v]split=2[a][b];\
[a]scale=-2:1920,crop=1080:1920,boxblur=24:3,eq=brightness=-0.12:saturation=1.1[bg];\
[b]scale=1080:-2:flags=lanczos[fg];\
[bg][fg]overlay=0:(H-h)/2[v0];\
[v0]drawtext=fontfile=$FONT:textfile=tmp/l1.txt:fontsize='if(lt(t,0.25),40+t*200,90)':fontcolor=white:borderw=8:bordercolor=black:x=(w-text_w)/2:y=410,\
drawtext=fontfile=$FONT:textfile=tmp/l2.txt:fontsize='if(lt(t,0.25),40+t*200,90)':fontcolor=0xFFD21F:borderw=8:bordercolor=black:x=(w-text_w)/2:y=515[v1];\
[1:v]setpts=PTS+1.0/TB[st];[v1][st]overlay=160:110:eof_action=pass,fade=t=in:st=0:d=0.15,fade=t=out:st=$FO:d=0.5,format=yuv420p[v]"
J=$(ffmpeg -hide_banner -ss $S -t $D -i $SRC -vn -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | python3 -c "import sys;t=sys.stdin.read();print(t[t.rfind('{'):t.rfind('}')+1])")
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
AF="afade=t=in:st=0:d=0.1,afade=t=out:st=$FO:d=0.5,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000"
ffmpeg -v error -y -ss $S -t $D -i $SRC -framerate 30 -i sticker/s%03d.png -filter_complex "$VF" -map "[v]" -map 0:a -af "$AF" -c:v libx264 -preset slow -crf 18 -r 30 -c:a aac -b:a 192k -movflags +faststart -t $D $OUT
echo "ok $OUT"
