cd /home/user/projeto_elias
N=$(python3 -c "import linha as L;print(int(L.DUR*30))")
P=/root/lemo-opuscar/.venv/bin/python
Q=$(( (N+3)/4 ))
for k in 0 1 2 3; do $P render.py $((k*Q)) $(((k+1)*Q)) & done; wait; echo done $N
