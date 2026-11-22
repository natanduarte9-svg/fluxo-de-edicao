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
- **Som: só o MP3 da música** que o usuário envia.

### Só no vídeo longo (16:9)
- **Sem encerramento** e sem o cartão final.

### Só nos Shorts (sempre 9:16)
- **Encerramento animado** (ver "Encerramento oficial"), sem o som dele.
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

## Referência 2: "Paulo e Silas na prisão" (YouTube Create) — **o padrão de vídeo com movimento**
Short 9:16, 2160×3840, 60 fps, 46,2 s, −13,8 LUFS. Folha de quadros a cada 0,5 s: `assets/fire-grace-ref2-folha.jpg`. **Este é o modelo de "como eu quero" para vídeos com movimento criados do zero.**

### Estrutura: história bíblica contada em cenas (Atos 16, meia-noite na prisão)
| Tempo | Cena | Plano e câmera |
|---|---|---|
| 0–5 s | Paulo ajoelhado, braços erguidos, orando na cela; tocha acesa, luz azul da janela gradeada | Plano médio-aberto, câmera parada/leve aproximação |
| 5–10 s | Rosto de Paulo cantando, com lágrimas; companheiros atrás | **Close**, aproximação lenta |
| 10,5–20 s | Paulo e os presos à luz azul da lua; ele canta e ergue as mãos; termina em close emocionado | Plano médio → close |
| 20–24 s | **Terremoto:** a parede racha, pedras voam, o companheiro segura Paulo | Plano médio com tremor |
| 24,5–28 s | **Portas de ferro e correntes caem**, a porta se abre e entra luz azul | Detalhe da porta, sem pessoas |
| 28,5–30 s | Os dois olham para cima, espantados | Plano médio |
| 30–39,5 s | Os dois de pé, portas abertas, **a luz do céu inunda a cela**, ficando dourada e branca; mãos erguidas em adoração | **Plano aberto simétrico**, clímax |
| 40 s | **Clarão branco com partículas** (transição) | — |
| 40,5–46 s | Cartão final animado | — |

- **8 cenas em ~40 s** (uma a cada 4–6 s). Mesmo personagem do começo ao fim (cabelo, barba, túnica vermelha e bege).
- **A história acompanha a letra:** "à meia-noite eu vou te adorar" (oração) → "correntes tentem me…" (presos) → "o impossível começa a acontecer" (terremoto) → "nenhuma corrente vai me prender" (portas caem) → "as cadeias vão cair, as portas vão se abrir" (luz) → "eu nasci pra te adorar" (final).
- **Luz conta a história:** azul-frio e escuro na prisão → dourado-quente e branco no milagre.
- **Transições:** dissolve suave (~0,5 s) entre as cenas; **clarão branco com partículas** antes do encerramento.

### Legenda karaokê (`assets/fire-grace-ref2-legenda.jpg`)
- Fonte **geométrica arredondada e pesada** (tipo Montserrat Black/Poppins ExtraBold), caixa alta, **branca** com **brilho/sombra escura**.
- **Palavra cantada em amarelo (#FFFF00) com brilho amarelo**; poucas palavras por vez (2–4), em 1–2 linhas.
- Posição: **centro, a ~75% da altura**. A legenda **continua no cartão final** (sobre o preto).
- ⚠️ **Erro a não repetir:** a fonte do CapCut não tinha acentos maiúsculos e saiu "NãO", "PRISãO", "IMPOSSíVEL", "Fé". **Usar fonte com acentos completos** (Montserrat/Poppins/Anton têm) e conferir "NÃO", "PRISÃO", "FÉ", "À".

### Sticker
- Sticker do CapCut no **canto superior direito**, de **~6 s a ~10,5 s**, menor que no vídeo 1.

### Encerramento animado (`assets/fire-grace-ref2-encerramento*.jpg`)
1. 40,5 s: o **logo surge com um clarão de fogo** e o botão do YouTube aparece.
2. 42–43,5 s: as pílulas **LIKE** e **SUBSCRIBE** deslizam para fora do botão.
3. 44 s: **"FIRE & GRACE"** em amarelo com brilho.
4. 44,5 s: o texto se escreve com brilho amarelo e fica **"assista o vídeo completo clicando no título ."** (branco com brilho amarelo, minúsculas).
- Botões em inglês aqui (LIKE/SUBSCRIBE); no vídeo 1, em português (INSCREVA-SE). ★ **Decidido pelo usuário: sempre em português** — "CURTIR"/"LIKE" com coração e "INSCREVA-SE" com sino (como no vídeo 1).

### Som
- Só a música. A música segue tocando no cartão final.

## Encerramento oficial (pronto para usar)
- ★ **Só nos Shorts (9:16). Os vídeos longos NÃO levam encerramento** (pedido do usuário).
- ★ **Sem o som do encerramento:** a **música (o MP3 enviado) continua tocando** por cima do cartão até o fim do vídeo.
- Arquivo: **`assets/encerramento-pt-9x16.mp4`** (1080×1920, 6 s, **sem áudio**). ★ **Manter a frase "assista o vídeo completo clicando no título"** no final (aparece aos 3,9 s); aprovado pelo usuário em 22/11/2026.
- Feito a partir do encerramento enviado pelo usuário (1920×1080, 6 s): logo do leão surge com clarão, botão do YouTube, pílulas **CURTIR** e **INSCREVA-SE** (traduzidas quadro a quadro de LIKE/SUBSCRIBE com `ferramentas/traduzir-encerramento.py`, fonte Montserrat ExtraBold) e "FIRE & GRACE" em amarelo. A versão 16:9 ficou guardada em `ferramentas/extras/` só por segurança (não usar nos longos).
- Logo em PNG transparente: `assets/fire-grace-logo.png` (410×410).
- **Uso nos Shorts:** escurecer a cena até o preto (~0,7 s), colar o cartão, deixar a música seguindo; a legenda karaokê pode continuar por cima, como na referência 2. Contar os 6 s do cartão dentro do limite de 35 s do Short.

## Publicação (conectado em 22/11/2026)
- **Canal no YouTube:** FIRE & GRACE (`UCu2-et8aU5qh8zUYBAxkDDg`), conta Google natanmusicagospel@gmail.com.
- **Agendamento pelo Metricool** (marca `8216784`, dona: natanduarte9@gmail.com, fuso America/Sao_Paulo). O vidIQ do Claude não aceita um 2º canal no plano grátis.
- ★ **Agenda fixa de cada música (definida pelo usuário em 22/11/2026):**
  | Dia | Hora | O que |
  |---|---|---|
  | Dia 1 | **19h40** | **Vídeo longo** (16:9) — sempre o primeiro |
  | Dia 1 | **20h00** | **Short 1** |
  | Dia 2 | **20h00** | **Short 2** |
  | Dia 3 | **20h00** | **Short 3** |
- ★ **Todo Short leva ao vídeo longo do Dia 1:** usar o recurso **"Vídeo relacionado"** do Short no YouTube Studio (aparece como link embaixo do Short) apontando para o longo, além do cartão final "assista o vídeo completo clicando no título" e um link para o longo na descrição. O vídeo relacionado só pode ser escolhido **depois** que o longo estiver publicado (ou agendado), então agendar o longo primeiro.
- ⚠️ Os "melhores horários" do Metricool (16h/10h) **não são do canal**: o canal acabou de ser conectado e ele ainda não tem dados; é média geral. **Não usar.**
- **Fonte certa:** YouTube Studio → Análises → Público → "Quando seus espectadores estão no YouTube". **Em 21/11/2026 ainda dizia "Não há dados suficientes"**. Olhar de novo daqui a algumas semanas.
- **Público (Studio, últimos 28 dias, em 21/11/2026):** 1,8 mil espectadores por mês; +77 inscritos; **97,7% novos espectadores**; **85% no celular** (8,7% TV); **86% Brasil**; idade: **35–44 (28%)**, **25–34 (25,6%)**, 45–54 (15,9%), 13–17 (15%), 55–64 (11,5%); **60% mulheres**. Vídeos mais vistos: "À MEIA-NOITE EU VOU TE..." (1,4 mil) e "ELE MORREU POR AMOR" (1,1 mil).
- **Leitura:** adultos de 25 a 54 anos, no celular → o horário do usuário (**19h40 / depois das 20h**, à noite depois do trabalho, e **8h10** no começo do dia) faz sentido. Manter.
- **Para agendar:** o vídeo pronto precisa de um link público (ex.: Google Drive compartilhado); o Metricool importa. Sempre mostrar a agenda e esperar o "sim" do usuário.

## ★ Checklist de publicação no YouTube (pedido do usuário em 22/11/2026, vale para os dois canais)
1. **Título chamativo** (até 100 caracteres).
2. **Descrição:** convite para **se inscrever**; contar um pouco do que acontece no vídeo; **uma pergunta para as pessoas comentarem**; **hashtags** no fim (as 3 primeiras aparecem acima do título). Nos Shorts, também o link do vídeo longo.
3. **Tags:** campo "Tags" do YouTube, **até 500 caracteres no total** (é esse o limite do YouTube; a descrição é que vai até 5.000).
4. **"Contém promoção paga": NÃO** (desmarcado).
5. ★ **"Conteúdo alterado ou sintético" (uso de IA): SIM** — no FIRE & GRACE as cenas são criadas com IA (decidido pelo usuário em 22/11/2026). Vale para o longo e para os Shorts.
6. Público: **"Não é conteúdo para crianças"**.
7. **Esperar o processamento chegar a 100%** antes de mexer na visibilidade.
8. Visibilidade: **Público**, com **programação** (data e hora da agenda).
9. Só então apertar **"Programar"**.
- Pelo Metricool/vidIQ, isso equivale a: `privacy: public` na data agendada, `madeForKids: false`, `isAiGeneratedContent: true`, sem promoção paga; conferir no Studio depois que o vídeo processar.

- ★ **Miniatura:** **só no vídeo longo**, usando a **imagem de referência que o usuário enviar** (não criar outra). **Shorts: sem miniatura.**
- O passo a passo no YouTube Studio é o mesmo do GTA (ver `manifestos/gta.md`), trocando: **Uso de IA: "Sim"**, **categoria: Música**, playlist do canal gospel.

## Pendente
- [x] Vídeo de referência estudado (seção acima).
- [x] Encerramento original recebido e traduzido; logo extraído em boa qualidade.
- [ ] Montar o cartão de encerramento e a legenda karaokê como ferramentas reutilizáveis (no primeiro vídeo real).
- [ ] Confirmar no primeiro vídeo longo se ele também leva o sticker (até agora: só nos Shorts).
