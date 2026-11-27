# Clipe "NO DESERTO, ELE VENCEU" (FIRE & GRACE, 27/11/2026)

Música do Natan (Suno, plano pago = pode monetizar). Imagem estática 16:9 dele, com o título já na arte.

## Material (fora do repositório, em /home/user/clipe-deserto)
- `capa.png` (1672x941), `musica.mp3` (282 s; a tag do Suno diz "VENDEU", o certo é **VENCEU**)
- `palavras.json`: 369 palavras com início/fim (transcrição ElevenLabs Scribe, 2.585 créditos)
- `batidas.npy`: batidas (librosa, 137,9 BPM)
- `fontes/CinzelBlack.ttf`: Cinzel peso 800 com o nome "Cinzel Deserto" (o libass não escolhe peso de fonte variável)
- `sticker/`: `ferramentas/sticker-inscreva.py sticker 10`

## Como refazer
```bash
cd /home/user/clipe-deserto
python3 <repo>/projetos/clipe-no-deserto/legendas_karaoke.py .        # karaoke.ass
/root/lemo-opuscar/.venv/bin/python <repo>/projetos/clipe-no-deserto/animar.py .            # clipe.mp4 (~15 min)
/root/lemo-opuscar/.venv/bin/python <repo>/projetos/clipe-no-deserto/animar.py . 9 21       # prévia de um trecho
QUADRO=5,90 /root/lemo-opuscar/.venv/bin/python <repo>/projetos/clipe-no-deserto/animar.py . # só quadros soltos
```

## Decisões
- **Movimento:** câmera lenta com 16 pontos-chave: aproxima nos versos (até 1,10x), abre nos refrões
  (83 s, 168 s, 228 s), passeia até o tentador quando a letra fala da tentação, termina aproximando.
  Âncora vertical sempre perto do topo: **o título da arte nunca é cortado**.
- **Luz:** sol que respira (ciclo de 6,4 s), raios animados no céu, mais brilho nos refrões
  (com moderação: brilho forte deixou o céu amarelo demais no 1º teste), pulso de luz na batida só no refrão.
- **Poeira dourada** em 2 profundidades (pontinhos + bokeh desfocado), vento para a direita.
- **Karaokê:** ASS com `\kf`; a palavra se preenche de dourado só enquanto é cantada (nas pausas fica parada).
  Trechos por frase, no máximo 2 linhas, embaixo, sobre a túnica (sem cobrir rostos). Cinzel peso 800.
- **Sticker Inscreva-se/Like:** 3 vezes de 10 s (2 s, meio, últimos 10,6 s), no céu à esquerda.
- Áudio só a música, -14 LUFS em dois passes, fade de 2,5 s no fim.
