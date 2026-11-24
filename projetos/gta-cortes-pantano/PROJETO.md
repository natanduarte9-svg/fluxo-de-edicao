# 5 Shorts da gameplay de 2h25 (missão do pântano) — 24/11/2026
Fonte: gameplay do usuário no Drive (1,6 GB, 1280×720, 2h25), baixada direto (`drive.usercontent.google.com`).

## Como os momentos foram achados (`analisar.py`, grátis)
Áudio a 16 kHz + quadros 96×54 a 2 fps → por segundo: volume, "estalos" (subida >9 dB em 10 ms = tiros/batidas/explosões), movimento na tela, brilho (tela escura/menu perde nota). Janelas de 25 s ranqueadas, sem sobrepor → folhas de contato → escolha visual. ⚠️ Rádio do carro gera "estalos" falsos: sempre olhar os quadros. A noite (depois de 1:20) é escura e rende pouco.

## Os 5 Shorts (aprovados pelo usuário)
| # | Trecho | Dur. | Título (2 linhas) |
|---|---|---|---|
| 1 | 0:42:16–0:42:41 | 25 s | TIROTEIO NO / PÂNTANO! |
| 2 | 0:43:01–0:43:26 | 25 s | ACUADO ATRÁS / DO MURO! |
| 3 | 0:44:09–0:44:34 | 25 s | FUGA DE / HELICÓPTERO! |
| 4 | 0:46:16–0:46:42 | 26 s | QUE EXPLOSÃO / FOI ESSA?! |
| 5 | 0:46:45–0:47:11 | 26 s | FUGA DE BARCO / NO PÂNTANO! |
Reservas: 0:03:56 pasto pegando fogo; 0:48:27 pouso do helicóptero.

## Montagem (`fazer_short.sh`)
Gameplay 16:9 no centro + cópia desfocada e escurecida atrás (1080×1920), título y=410/515, sticker "Inscreva-se" 5,6 s a partir de 1,0 s (overlay 160:110), só o som do jogo, −14 LUFS, sem acelerar. Duração conferida no ffprobe (todos ≤ 26 s), sem quadros pretos.
