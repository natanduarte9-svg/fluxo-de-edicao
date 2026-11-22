# Manifesto: FIRE & GRACE (gospel, @FireGraceGospelmusic)

**Rascunho**: ainda há pouca informação. Complete com o usuário (perguntas abaixo) ou por engenharia reversa de vídeos já publicados.

## O que já sabemos
- Canal de música gospel. As músicas são feitas no **Suno**; os vídeos usam **imagens** (estáticas) e o áudio da música.
- Há skills próprias: `fire-grace-musica-completa`, `fire-grace-video-editor`, `fire-grace-estrategia-semanal`.
- Estética do primeiro projeto (`projetos/elias-altar-fogo/`): **épico bíblico de cinema**, pôr do sol dourado, fogo divino, nuvens dramáticas, luz volumétrica; personagem bíblico com o rosto e as roupas preservados.
- Formato pedido até agora: **vertical 9:16**, 8–10 s para um clipe com movimento real.
- Movimento real (personagem, fogo, tecido) = **IA de vídeo** (vidIQ); acabamento em código.
- Sem texto, logos ou pessoas extras **dentro** da cena gerada por IA.

## Formatos e fluxo de publicação (respondido em 22/11/2026)
1. **Primeiro o vídeo longo:** a **música inteira**, **16:9** (1920×1080), postado no YouTube primeiro.
2. **Depois, 3 Shorts tirados desse vídeo longo:** **no máximo 35 s** cada, **9:16** (1080×1920).
3. **Coletâneas** também fazem parte do plano (várias músicas num vídeo longo).

### Em todos (longo e Shorts)
- **Legendas estilo karaokê** (a palavra cantada acende no tempo da música).

### Só nos Shorts
- **Sticker "Inscreva-se + deixe o like + ative o sininho"**, **no mesmo estilo do GTA** (`ferramentas/sticker-inscreva.py`: joinha, botão de inscrição e sino), **com até 10 s na tela** (usar `python ferramentas/sticker-inscreva.py <pasta> 10`).

### Respostas de 22/11/2026
- **Logo do canal: não usar.**
- **Sticker:** o mesmo do GTA, até 10 s (ver acima).
- **Imagens e ritmo:**
  - Vídeo feito a partir de **uma imagem estática de referência** → **não trocar a imagem**; o movimento vem dela.
  - **Criação de vídeo com movimento** → o usuário manda um prompt e **eu elaboro cena por cena** (storyboard com plano, câmera, duração e ação de cada cena) **antes de gerar**, para sair perfeito. Mostrar o roteiro de cenas e esperar a aprovação.
- **Abertura: não existe. Encerramento: existe** (copiar do vídeo de referência).
- **Efeitos, estilo da legenda karaokê e encerramento:** tirar do **vídeo de referência editado no CapCut** que o usuário vai mandar (link pendente). Estudar quadro a quadro e anotar aqui: fonte, cores, posição e animação da legenda; efeitos; encerramento.

## Engenharia reversa do vídeo de referência (22/11/2026)
Short "Deus Ainda Responde com Fogo", editado no CapCut: 2160×3840 (9:16, 4K), 60 fps, 54,5 s, −13,7 LUFS. Folha de quadros: `assets/fire-grace-referencia-folha.jpg`.

### Imagem e movimento
- **Uma única cena o vídeo todo** (Elias ajoelhado diante do altar, fogo descendo do céu), **com movimento real** (fogo vivo, nuvens, Elias muda os braços de posição): é um clipe de IA, não foto parada.
- **Aproximação lenta da câmera** (zoom de ~10% em ~48 s), quase imperceptível.
- **Título fixo no topo, "assado" na arte:** "DEUS AINDA / RESPONDE COM / **FOGO**". Serifada pesada, branco-prateado com contorno escuro, "RESPONDE COM" dourado e "FOGO" enorme, dourado com textura de fogo e brilho. O título é o nome da música.

### Legenda karaokê (`assets/fire-grace-legenda.jpg`)
- **Fonte:** condensada e pesada, caixa alta (tipo **Anton**/Bebas). **Branca** com contorno/sombra **preta** grossa.
- **A palavra cantada fica amarela (#FFFF00), maior e mais grossa.** A próxima palavra aparece pequena em amarelo, como uma "prévia", e cresce quando é cantada.
- **A frase se monta palavra por palavra**, em até 2 linhas, e some quando a frase termina.
- **Posição:** terço de baixo, sobre o chão/rochas (≈ 60–75% da altura), centralizada. Não cobre o rosto nem o fogo.

### Sticker
- Sticker do CapCut "SUBSCRIBED" (joinha + botão + sino com cursor), **logo abaixo do título**, de **~9 s a ~19 s (10 s)**.

### Encerramento (`assets/fire-grace-encerramento.jpg`)
- Em ~49 s a cena **escurece até o preto** (~0,7 s).
- **Cartão final de ~4,5 s, fundo preto:**
  - **Logo do canal no centro** (leão com "FIRE & GRACE"), em círculo com **borda vermelha brilhante**. Recorte em `assets/fire-grace-logo-recorte.png` (baixa qualidade; pedir o arquivo original ao usuário).
  - **"FIRE & GRACE"** em amarelo, fonte geométrica pesada (tipo Montserrat ExtraBold).
  - Três botões: **❤ LIKE** (pílula escura com círculo vermelho), **▶ YouTube** (vermelho, no meio), **🔔 INSCREVA-SE** (pílula escura com círculo vermelho).
  - Texto branco: **"ESCUTE ESSE HINO COMPLETO CLICANDO NO TÍTULO DESSE VÍDEO"** (nos Shorts, que levam ao vídeo longo).
  - Entra com um leve zoom/fade.

### Som
- Só a música (o hino), sem efeitos sonoros. Volume ≈ −14 LUFS.

## Pendente
- [x] Vídeo de referência estudado (seção acima).
- [ ] Pedir ao usuário o **arquivo original do logo** (o recorte do vídeo está em baixa qualidade).
- [ ] Montar o cartão de encerramento e a legenda karaokê como ferramentas reutilizáveis (no primeiro vídeo real).
- [ ] Confirmar no primeiro vídeo longo se ele também leva o sticker (até agora: só nos Shorts).
