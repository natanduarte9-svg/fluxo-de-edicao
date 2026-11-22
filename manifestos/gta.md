# Manifesto: canal de GTA 6

Construído por engenharia reversa dos Shorts de 21–22/11/2026 (`projetos/gta-shorts-01/`) e dos pedidos do usuário. **Regras marcadas com ★ vieram de correções do usuário: não quebrar.**

## Formato
- **Shorts verticais 9:16, 1080×1920, 30 fps.**
- **Até 30 s** cada. Se o usuário pedir para juntar dois momentos, pode passar disso (já foi feito um de 1:06); o ideal é até 60 s.
- O usuário edita a base no **CapCut**: gameplay 16:9 no centro, com uma cópia **desfocada** ocupando a faixa de cima e a de baixo.

## Escolha dos momentos
- Ação que se entende sem contexto: **carros voando, saltos, perseguições, fugas, tiroteios, confrontos.**
- O gancho tem que estar nos primeiros 2–3 s.
- **Terminar logo depois do clímax** (cerca de 1,5 s depois), para dar tempo de ver o resultado. ★ Ex.: "deixe até o tiro na cabeça do rapaz ajoelhado".
- Para achar o momento exato: pico de som + quadros a cada 0,25 s.

## Texto na tela
- **Legendas do CapCut** (já vêm no vídeo): caixa alta, fonte condensada pesada, branco com a palavra-chave em **amarelo**, contorno preto, na faixa desfocada de baixo, em português. Manter.
- As legendas do próprio jogo também ficam.
- **Título (gancho):** 2 linhas na faixa desfocada de cima: linha 1 branca, linha 2 **amarela** (#FFD21F), Inter Display Black 90 px, contorno preto de 8 px, entrando com um "pulo" nos primeiros 0,25 s. Posição y=410 e y=515 (1080×1920). Frases curtas e curiosas: "OS CARROS VOARAM / DA PONTE!", "ELE NÃO ESPERAVA / POR ISSO...".

## Sticker "Inscreva-se"
- ★ **O sticker de se inscrever nunca pode ser coberto** por título, efeito ou qualquer outra coisa. O do CapCut aparece na faixa de cima (y≈180–375) no começo e em outros momentos: olhar os quadros antes de pôr texto.
- Se o vídeo não tiver sticker, usar o nosso (`ferramentas/sticker-inscreva.py`): cartão branco, joinha, botão INSCREVA-SE → clique → INSCRITO, sino. ★ **No mínimo 5 s na tela** (hoje 5,6 s). Em vídeos de ~1 min, aparecer 2 vezes (ex.: 0:04 e 0:40).

## Som
- ★ **Narração só quando o usuário pedir** (vídeos didáticos/explicativos). No dia a dia: **vozes e som do próprio jogo**.
- ★ **Voz escolhida para narrar: Microsoft `pt-BR-AntonioNeural`** (edge-tts, grátis; ElevenLabs só se o usuário pedir e houver crédito).
- ★ **Só o som do jogo, sem música** (pedido do usuário).
- Volume padrão do YouTube: **−14 LUFS**, pico −1,5 dB. Fade curto na entrada (0,1 s) e na saída (0,5 s).

## Transições
- Ao juntar trechos: fade de 0,3 s na imagem e no som.

## ★ Referência de qualidade feita pelo usuário (23/11/2026) — "é assim que eu quero"
Vídeo `minhaproducao.mp4` (30 s, 9:16), feito por ele no **YouTube Create + CapCut**. Quadros: `assets/gta-ref-usuario-mapa-carro.jpg`.
**Estrutura (uma tomada contínua, sem cortes secos):**
1. **0–8 s — mapa realista estilo satélite** de Leonida (relevo, mar turquesa, nomes das regiões), câmera **aproximando devagar** com **nuvens passando**; narração-gancho: "Você... para conhecer uma das máquinas mais impressionantes do GTA 6? Hoje vamos falar do Grotti Cheetah... **preste atenção no mapa e acompanhe**".
2. **8–13 s — mergulho** até a região (Port Gellhorn): o mapa vira **vista aérea 3D da cidade**, "é aqui que vamos investigar a localização desse supercarro".
3. **13–14 s — transição atravessando as nuvens** (a câmera desce do céu para a rua).
4. **14–16 s — cidade ao pôr do sol**, câmera descendo até o prédio: "agora olha só essa..."
5. **16–30 s — o carro em cena de cinema** (branco com faixa vermelha, chão molhado, palmeiras, hotel curvo), câmera **avançando/girando devagar** até um close na frente; **faróis acendendo** no final.
6. **Final:** pergunta para comentar ("e você teria esse carro na sua garagem? comenta") + **sticker de inscrição** (canto superior direito) nos últimos ~7 s.
**Texto na tela:** legenda **no topo** (y ≈ 15–25%), caixa alta, fonte condensada pesada, **branca com a palavra-chave em amarelo** e contorno preto, poucas palavras por vez.
**O que isso ensina (padrão a seguir):** cenas **realistas e cinematográficas** (não desenho), **um movimento contínuo de câmera do macro ao detalhe** (mapa → cidade → rua → carro), transições que **viajam pelo espaço** (nuvens), narração que **conduz o olhar** ("preste atenção no mapa"), revelação do carro como clímax e CTA no fim.
**Pontos a melhorar quando fizermos o nosso:** volume estava em **−18,6 LUFS** (usar −14); legenda quebrava palavra no meio ("M / ÁQUINAS", "PRESENÇ / A") e juntava palavras ("PRESTEATENÇÃO"); nome do carro saiu "GROTCHITA" (escrever "Grotti Cheetah"); exportar em **1080×1920** (veio em 720×1280).
**Como ele fez (processo do usuário):**
1. Pediu a uma IA de texto um **roteiro cena por cena**, com **prompt de cada cena** e **imagens de referência**.
2. Gerou **cada cena** no **YouTube Create** (foto/prompt → vídeo com IA, grátis).
3. **Montou no CapCut**: ordem, transições, narração, legenda, sticker.

★ **O nosso processo padrão para vídeos assim (divisão de trabalho):**
1. **Eu escrevo o roteiro cena por cena** (`ROTEIRO.md`): para cada cena, duração, movimento de câmera, o que acontece, **prompt pronto para o gerador de vídeo** (em inglês, curto) e, quando ajudar, **prompt da imagem de referência** ou o print do jogo a usar como primeiro quadro. Mostro antes e espero o "ok".
2. **As cenas são geradas** pelo gerador grátis da vez (rodízio): **YouTube Create pelo usuário** (ele manda os clipes pelo Drive) ou **vidIQ por mim** (com o custo mostrado antes).
3. **Eu monto tudo aqui**: ordem e transições (inclusive as "viagens" mapa → cidade → rua), narração Antonio quando pedida, legenda karaokê sincronizada, sticker, música/efeitos, **−14 LUFS**, **1080×1920**, revisão quadro a quadro.

**Como reproduzir esse nível aqui:** cena aérea/mapa realista e o carro com movimento → **IA de vídeo** (vidIQ Veo/MiniMax, ou YouTube Create no celular, conforme o rodízio grátis); mergulho mapa→cidade e travessia das nuvens → **three.js** (plano com textura do mapa + partículas de nuvem volumétrica + transição) ou IA de vídeo com quadro inicial/final; montagem, legenda karaokê sincronizada (edge-tts dá o tempo de cada palavra), sticker, −14 LUFS e 1080×1920 → **aqui, em código**.

## Formato "Aula de GTA" (lousa própria) — teste de 22/11/2026
- ★ **Não copiar o vídeo de referência de outra pessoa:** aproveitar só o estilo; usar voz, roteiro, cenário e transições próprios. Ver `projetos/gta-aula/PROJETO.md`.

## Formato "lousa" (didático) — primeiro teste de 22/11/2026 (parecido demais com a referência; usar a "Aula de GTA")
- Referência do usuário: Reel "Emulador de Xbox" (Instagram). Estrutura: **quadro-negro de giz** no gancho → **quadro verde** com título de desenho + **monitor no pedestal** + selos + estrelinhas → **transição de papel** desenhando o próximo monitor → final "SEGUE!/COMENTA!". **Etiqueta amarela** ("• CARRO 1 · LOCAL") acima da **legenda** na faixa de terra, palavra falada em amarelo.
- Didático: o monitor mostra **primeiro o que é** (foto) e **depois onde fica** (mapa com pino e círculo de giz), no ritmo da narração.
- Base em código: `projetos/gta-mapa-exoticos/render_lousa.py`.

## Publicação
- **Canal:** JOGATINA FACIL (`UCUVvM4v7SHp-wxtsFYrEmWA`, @natanduarte7304), **conectado ao vidIQ do Claude com permissão de publicar** (desde 22/11/2026). Upload e agendamento pelo vidIQ (`vidiq_video_upload` + `vidiq_social_post_*`), sempre com o "sim" do usuário.

- **Horário:** o Studio ainda não tem dados ("Não há dados suficientes", 21/11/2026). Canal pequeno: 17 espectadores/mês, 94% novos.
- ★ **Mesma agenda do FIRE & GRACE (pedido do usuário em 22/11/2026):**
  | Dia | Hora | O que |
  |---|---|---|
  | Dia 1 | **19h40** | **Vídeo longo** — sempre o primeiro |
  | Dia 1 | **20h00** | **Short 1** |
  | Dia 2 | **20h00** | **Short 2** |
  | Dia 3 | **20h00** | **Short 3** |
- ★ **Todo Short leva ao vídeo longo do Dia 1:** "Vídeo relacionado" do YouTube apontando para o longo + link do longo na descrição. Agendar o longo primeiro.
- Quando houver só Shorts soltos (sem vídeo longo), postar às **20h**, um por dia.

## ★ Checklist de publicação no YouTube (pedido do usuário em 22/11/2026, vale para os dois canais)
1. **Título chamativo** (até 100 caracteres).
2. **Descrição:** convite para **se inscrever**; contar um pouco do que acontece no vídeo; **uma pergunta para as pessoas comentarem**; **hashtags** no fim (as 3 primeiras aparecem acima do título). Nos Shorts, também o link do vídeo longo.
3. **Tags:** campo "Tags" do YouTube, **até 500 caracteres no total** (é esse o limite do YouTube; a descrição é que vai até 5.000).
4. **"Contém promoção paga": NÃO** (desmarcado).
5. ★ **"Conteúdo alterado ou sintético" (uso de IA): NÃO** — no Jogatina Fácil é gameplay real, sem IA.
6. Público: **"Não é conteúdo para crianças"**.
7. **Esperar o processamento chegar a 100%** antes de mexer na visibilidade.
8. Visibilidade: **Público**, com **programação** (data e hora da agenda).
9. Só então apertar **"Programar"**.
- Pelo Metricool/vidIQ, isso equivale a: `privacy: public` na data agendada, `madeForKids: false`, `isAiGeneratedContent: false`, sem promoção paga; conferir no Studio depois que o vídeo processar.

### ★ Passo a passo do usuário no YouTube Studio (gravação de 22/11/2026, usando o Short "OS CARROS VOARAM DA PONTE" só como EXEMPLO)
- ★ **Cada vídeo tem o seu próprio título, descrição, tags e hashtags**, criados para aquele vídeo. Nunca reaproveitar os do exemplo.
- ★ **O "vídeo relacionado" dos Shorts é o vídeo longo do mesmo conjunto.** ★ **Por enquanto, no Jogatina Fácil, os Shorts apontam para as LIVES de GTA do usuário** (os vídeos longos do canal são as transmissões ao vivo). Perguntar qual live usar em cada Short.
- ★ **Miniatura:** nenhuma nos Shorts; por enquanto também não há miniatura a fazer no canal (os longos são as lives).
Feito em **studio.youtube.com** (versão de computador, no navegador do celular):
1. **Criar → Enviar vídeos** → escolher o arquivo (pasta Downloads).
2. **Detalhes:**
   - **"Reutilizar detalhes"** de um vídeo anterior do canal (aproveita configurações) e depois troca o que for do vídeo novo.
   - **Título** e **descrição** colados (os do pacote preparado).
   - ★ **Miniatura: não precisa nos Shorts** (deixar a automática).
   - **Playlist:** **GTA6**.
   - **Público:** **"Não é conteúdo para crianças"**.
   - **"Mostrar mais"** → **Promoção paga: "Não, meu vídeo não inclui promoção paga"**.
   - **Uso de IA: "Não"** (Jogatina Fácil).
   - **Tags** coladas (o contador mostrou **406/500**: o YouTube conta um pouco diferente; manter folga abaixo de 500).
   - **Idioma:** Português (Brasil) · Certificação de legendas: Nenhum · Licença padrão do YouTube.
   - ✔ Permitir incorporação · ✔ Publicar no feed de inscrições e notificar.
   - **Remixes:** permitir áudio e vídeo.
   - **Categoria: Jogos.**
   - **Comentários:** ativados, moderação básica, qualquer pessoa pode comentar, ordenar por "Principais" · ✔ Mostrar curtidas.
3. **Elementos do vídeo:** **Vídeo relacionado → "Escolha um vídeo específico"** (no Short, escolher o vídeo longo).
4. **Verificação inicial:** esperar terminar (direitos autorais e diretrizes; levou ~5 min).
5. **Visibilidade:** abrir **"Programar"** → **data** e **hora** (ex.: **23 de nov., 20:00**) → o vídeo fica privado até a hora → apertar **"Programar"**.

## Entrega
- MP4 H.264 + AAC, sem marca d'água, mandado pelo chat.
- Ferramenta: `ferramentas/short-gameplay.sh`.

## Ainda não sabemos (perguntar quando surgir)
- Thumbnail/capa: estilo preferido.
- Título e descrição para o YouTube: tom e hashtags que o usuário usa.
- Vídeos longos: se terão música, narração, intro/outro.
