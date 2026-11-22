#!/bin/bash
# make.sh <saida> <inicio_s> <fim_s> "<linha1>" "<linha2>"
set -e
SRC=${SRC:-parte-drive.mp4}; OUT=$1; S=$2; E=$3; L1=$4; L2=$5
D=$(echo "$E - $S" | bc)
FONT=/usr/share/fonts/opentype/inter/InterDisplay-Black.otf
[ -f $FONT ] || FONT=/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf
FO=$(echo "$D - 0.5" | bc)
printf '%s' "$L1" > /tmp/l1.txt; printf '%s' "$L2" > /tmp/l2.txt
# título no topo (área desfocada), entra com pulo nos primeiros 0,25 s; vídeo em 1080x1920
VF="scale=1080:1920:flags=lanczos,\
drawtext=fontfile=$FONT:textfile=/tmp/l1.txt:fontsize='if(lt(t,0.25),40+t*200,90)':fontcolor=white:borderw=8:bordercolor=black:x=(w-text_w)/2:y=${Y1:-410},\
drawtext=fontfile=$FONT:textfile=/tmp/l2.txt:fontsize='if(lt(t,0.25),40+t*200,90)':fontcolor=0xFFD21F:borderw=8:bordercolor=black:x=(w-text_w)/2:y=${Y2:-515},\
fade=t=in:st=0:d=0.15,fade=t=out:st=$FO:d=0.5"
# 1ª passada: medir volume
J=$(ffmpeg -hide_banner -ss $S -t $D -i $SRC -vn -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | python3 -c "import sys,re;t=sys.stdin.read();print(t[t.rfind('{'):t.rfind('}')+1])")
g(){ echo "$J" | python3 -c "import sys,json;print(json.load(sys.stdin)['$1'])"; }
AF="afade=t=in:st=0:d=0.1,afade=t=out:st=$FO:d=0.5,loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000"
ffmpeg -v error -y -ss $S -t $D -i $SRC -vf "$VF" -af "$AF" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -movflags +faststart $OUT
echo "ok $OUT ($D s)"
