# Câmera lenta com quadros intermediários reais (fluxo óptico) para cada clipe caber no tempo da narração.
cd /home/user/projeto_elias
eval $(python3 -c "
import linha as L
for k in range(1,7):
    c=L.CENAS[k-1]; a=0 if k==1 else c['ini']-0.45; b=c['fim']+0.45
    print(f'D{k}={b-a:.3f}')")
for k in 1 2 3 4 5 6; do
  D=$(eval echo \$D$k); F=$(python3 -c "print($D/10.054)")
  mkdir -p temporarios/q$k
  ffmpeg -v error -y -i videos_originais/clipe$k.mp4 -an -vf "scale=1080:1920:flags=lanczos,setpts=PTS*$F,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" -q:v 2 temporarios/q$k/%05d.jpg &
done
wait; for k in 1 2 3 4 5 6; do echo q$k $(ls temporarios/q$k | wc -l) $(eval echo \$D$k); done
