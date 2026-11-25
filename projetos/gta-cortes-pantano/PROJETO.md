# 5 Shorts da gameplay de 2h25 (missão do pântano) — 24/11/2026
Fonte: gameplay do usuário no Drive (1,6 GB, 1280×720, 2h25), baixada direto (`drive.usercontent.google.com`).

## Como os momentos foram achados (`analisar.py`, grátis)
Áudio a 16 kHz + quadros 96×54 a 2 fps → por segundo: volume, "estalos" (subida >9 dB em 10 ms = tiros/batidas/explosões), movimento na tela, brilho (tela escura/menu perde nota). Janelas de 25 s ranqueadas, sem sobrepor → folhas de contato → escolha visual. ⚠️ Rádio do carro gera "estalos" falsos: sempre olhar os quadros. A noite (depois de 1:20) é escura e rende pouco.

## Os 5 Shorts (aprovados pelo usuário)
| # | Trecho | Dur. | Título (2 linhas) |
|---|---|---|---|
| 1 | 0:42:16–0:42:41 | 25 s | TIROTEIO NO / PÂNTANO! |
| 2 | 0:43:01–0:43:26 | 25 s | ESSE MURO FOI / SALVADOR! (título do usuário; não gostou de "acuado") |
| 3 | 0:44:09–0:44:34 | 25 s | FUGA DE / HELICÓPTERO! |
| 4 | 0:46:16–0:46:42 | 26 s | QUE EXPLOSÃO / FOI ESSA?! |
| 5 | 0:47:56–0:48:31 | **35 s** (a pedido: mostrar mais do jogo; `LIMITE=36`) | BRIGA NO BARCO / ACABOU NA HÉLICE! (trocado a pedido: briga corpo a corpo no aerobarco, cabeça na hélice) |
Reservas: 0:03:56 pasto pegando fogo; 0:48:27 pouso do helicóptero.

## Montagem (`fazer_short.sh`)
Gameplay 16:9 no centro + cópia desfocada e escurecida atrás (1080×1920), título y=410/515, sticker "Inscreva-se" 5,6 s a partir de 1,0 s (overlay 160:110), só o som do jogo, −14 LUFS, sem acelerar. Duração conferida no ffprobe (todos ≤ 26 s), sem quadros pretos.

## Correções do usuário (24/11/2026)
- ★ **Falas do jogo grandes na faixa de baixo**, logo abaixo do gameplay (y=1290): nome em amarelo, fala em branco, Montserrat ExtraBold 54, contorno preto. Sincronizadas com a legenda do jogo.
- Como: `legendas_jogo.py` acha quando a legenda do jogo muda (recorte y 578–672, 5 qps, máscara do texto) e monta uma folha; eu leio o texto na folha e escrevo `falas.json`; `legenda_png.py` desenha cada fala; `fazer_short.py` (substitui o .sh) sobrepõe com `enable=between(t,a,b)` e confere que nenhum passa de 30 s.
- Palavrões com asterisco só na legenda grande (c*ralho, p*rra, f*der, p*ta, m*rda), para não atrapalhar a monetização; o som do jogo fica igual. (Avisado ao usuário; pode tirar se ele pedir.)
- Short 5 refeito: a briga no barco (0:48:00–0:48:26).

## Publicação (rascunhos no vidIQ, 24/11/2026 — aguardando o "sim")
Canal JOGATINA FACIL, público, categoria Jogos (20), um por dia às 20h (Brasília). Vídeo relacionado = live "Primeiras horas de gta6 parte 4" (https://youtu.be/663WXHGN_1I), link também na descrição.
| Dia | Short | postId | revision |
|---|---|---|---|
| 24/11 20h | 1 TIROTEIO NO PÂNTANO! 🔫 GTA 6 | c3217147-06be-425c-8f3a-329aaf3fa92a | 20785bc4 |
| 25/11 20h | 2 ESSE MURO FOI SALVADOR! 🧱 GTA 6 | 95d21c4d-b58c-4f65-a6bf-5a097c31a1b7 | 7a3c5d0b |
| 26/11 20h | 3 FUGA DE HELICÓPTERO NO PÂNTANO! 🚁 GTA 6 | 45ea831f-ceff-4cbd-ab83-f9229c949427 | ab5a2e72 |
| 27/11 20h | 4 QUE EXPLOSÃO FOI ESSA?! 💥 GTA 6 | 65a1a955-b7f5-460a-a689-1ba858447730 | fceb9b28 |
| 28/11 20h | 5 BRIGA NO BARCO ACABOU NA HÉLICE! 😱 GTA 6 | 6e1facdb-2b28-4c46-9cf4-340f9a7f3e60 | f469f1b6 |
- O vidIQ não define "vídeo relacionado", "não é para crianças" nem "uso de IA": o usuário confere no Studio depois que cada um processar.

## Short 6 — "UM AVIÃO CAIU / NO PASTO!" (pedido em 24/11/2026, até 40 s)
Montagem de 5 trechos com transição suave de 0,3 s (xfade + acrossfade), 37,8 s, sem falas do jogo:
0:03:47–0:03:54 (dirige até a fumaça) · 0:03:57–0:04:03 (pasto pegando fogo) · 0:04:22–0:04:27 (pega a carga e põe na caminhonete) · 0:04:47–0:05:03 (o pessoal chega na caminhonete preta e ele derruba todos) · 0:05:20–0:05:25 (explosão).
O jogo não mostra o avião caindo, só a coluna de fumaça (desde 0:02:52). Montagem: `SRC=tmp/aviao_16x9.mp4 LIMITE=40 python fazer_short.py ...`.

### Short 6 refeito a pedido (24/11): "ELES CHEGARAM / NA HORA ERRADA!" — 37,7 s
Trecho contínuo 0:04:30–0:05:04 (inimigos Kingfishers chegam enquanto ele carrega a carga → mira em câmera lenta no carro deles → troca de tiros → **tiro de espingarda na cabeça** em 0:05:02) + 0:05:21–0:05:25 (**o avião explode** ao fundo), transição de 0,3 s. Falas dos Kingfishers em legenda grande.

## Publicação — situação em 24/11/2026 (aprovado pelo usuário: "sim, pode incluir e siga com a programação")
- ✅ Programados e conferidos no YouTube (scheduledPublishAt 23:00 UTC = 20h Brasília): Short 1 G-xsMzqgS-g (24/11), Short 2 kQgLABooT70 (25/11), Short 3 WpCOhGSuE3M (26/11).
- ⏳ **Limite do vidIQ grátis: 3 envios ao YouTube por dia** (zera à meia-noite do Pacífico = 5h Brasília). Shorts 4 (27/11), 5 (28/11) e 6 (29/11, postId 17b20733-15d1-4b78-b596-1c6228062993, rev 52cc9fed) ficam para 25/11 às 6h (lembrete agendado).
- O canal já tinha 2 Shorts do usuário programados para 24/11 (19h00 "DROGA CAINDO DO CÉU" e 19h45 "ELE NÃO ESPERAVA POR ISSO").
- 24/11: o usuário pediu para tirar o Short 1 de hoje (já havia 2 Shorts dele às 19h e 19h45). Movido para **30/11 20h** com `vidiq_update_video` (5 créditos), mantendo um por dia: 25 muro · 26 helicóptero · 27 explosão · 28 hélice · 29 avião · 30 tiroteio.
- 25/11 6h: Shorts 4 (T7t5ot3lrUs, 27/11), 5 (bPfFXDEeJXU, 28/11) e 6 (ldgmhzUga98, 29/11) enviados e programados pelo vidIQ (status "completed"). Não deu para conferir o horário no YouTube: vidIQ com só 2 créditos (renova 27/11). Os 3 primeiros, conferidos antes, ficaram certos às 20h.
- 25/11 13h: a pedido do usuário (opção A), o **Short 4 de sexta (T7t5ot3lrUs) foi cancelado** no vidIQ (volta a privado, sem data) porque o mesmo trecho vai ao ar hoje às 18h no **formato novo** (Painel + narração do Suno), **postado manualmente pelo usuário** pelo app do YouTube. O vídeo antigo fica privado no Studio (o usuário pode apagar).
