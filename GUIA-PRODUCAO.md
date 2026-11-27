# Guia de produção: vídeos com IA + código

O que aprendi estudando 10 repositórios de motion graphics para o Claude Code (lista do vídeo "10 GitHub Repos to 10x Your AI Motion Graphics", de Matt Penny) e como juntar tudo num vídeo de qualidade.

---

## 1. A ideia central

- **Código faz gráficos animados, não vídeo realista.** Todos os repositórios concordam nisso. Pessoa andando, tecido real ou fogo fotográfico pedem um **modelo de vídeo por IA** (MiniMax, Veo, Seedance, Kling, Runway).
- **A melhor combinação:** a IA gera o movimento real, e o Claude faz o resto em código: roteiro, trilha, efeitos sonoros, títulos, transições, sincronia com a música e acabamento.
- **Peças prontas e testadas vencem "inventar do zero".** Estilos, receitas de planos, efeitos e prompts que já funcionaram são o que tira o vídeo da cara de "IA genérica".

---

## 2. Os repositórios e para que servem

| Repositório | Para que serve | Quando usar |
|---|---|---|
| [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 99 estilos de filme feitos em código, com método completo de direção | Vídeo inteiro num estilo (aquarela, nanquim, infográfico, anime...) |
| [three.js](https://github.com/mrdoob/three.js) | 3D, partículas, câmera voando pela cena | Profundidade, luz, partículas de fogo/brasas |
| [pixelfx](https://github.com/patch-gg/pixelfx) | 244 efeitos em pixel art (fogo, raio, explosão, **sagrado**) | Shorts de games (GTA), efeitos estilizados |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 124 receitas de planos de vídeo promocional (Remotion) + método de sincronia com a música | Promos, lançamentos, trailers |
| [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | Mascote animado com pincel, guia de animação de personagem | Explicações com personagem desenhado |
| [react-three-rapier](https://github.com/pmndrs/react-three-rapier) | Física real (dominós, queda, colisão) | Explicações e cenas com física |
| [react-postprocessing](https://github.com/pmndrs/react-postprocessing) | Brilho, profundidade de campo, granulado, glitch | Acabamento "caro" de cenas 3D |
| [librosa](https://github.com/librosa/librosa) | Acha a batida da música | Cortes e impactos no tempo da música |
| [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 703 prompts de vídeos que viralizaram | Inspiração e ponto de partida |
| [opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) | 18 prompts completos + lições de escrita | Como escrever o pedido |
| [mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | O Claude controla o Blender | **Não instalado** (decisão: pesado e sensível) |

### Efeitos "sagrados" do pixelfx (bons para o FIRE & GRACE)
`holy/halo` (auréola), `holy/holy-pillar` (luz rompendo do céu), `holy/smite` (raio de luz caindo como martelo), `holy/resurrection` (asas de luz), `holy/sunburst` (sol radiante), `holy/blessing` (cone de luz sobre a pessoa), `holy/divine-shield`. Também há 40 efeitos de fogo.

---

## 3. As regras que todos os guias repetem

### Planejar antes de fazer
1. **Roteiro primeiro, código depois.** Storyboard, minutagem segundo a segundo e mapa da música antes de qualquer linha de código. Assim dá para refazer só uma cena.
2. **Uma história simples:** um personagem, um objetivo, uma virada, um final que ecoa o começo.
3. **Gancho nos primeiros 3 segundos.** Nada de abrir com logo lento.

### Tempo e ritmo
4. **Tempo para o espectador.** Cada momento precisa de tempo para o olho achar, entender e registrar. A ação pode ser rápida; o significado precisa de pausa.
5. **É sempre mais lento do que parece.** Em todo retorno de cliente registrado, pediram "mais devagar", nunca "mais rápido". Ação de abertura: pelo menos **3 s**. Mensagem ou marca final: **1 s parada**.
6. **Variar a velocidade.** Alternar rápido e lento, ter uma aceleração clara e um respiro. Velocidade constante deixa o vídeo chato.
7. **Legendas:** no mínimo **1,8 s** na tela (ou a duração da fala + 0,6 s).
8. **Nada parado.** Uma tela 100% congelada parece defeito: sempre algo respira (nuvem, brasa, câmera derivando).

### Música
9. **A grade da música vem primeiro;** a imagem se encaixa nela.
10. **Sincronizar sem exagero:** os cortes caem na batida, mas impacto na tela inteira (tremor, flash, zoom brusco) **no máximo 3 vezes** no vídeo.
11. **librosa erra o BPM em cerca de 2%.** A correção: pegar a lista de batidas que ele dá e ajustar uma reta (`t = t0 + i·T`) por mínimos quadrados. Erro aceitável: até ±15 ms. Cuidado com BPM dobrado ou pela metade.

### Movimento
12. **Movimento com peso:** antecipação antes da ação, aceleração em vez de velocidade constante, uma pausa curta no impacto (até 0,2 s), recuperação.
13. **Nada se move em linha reta e velocidade constante.** Arcos, entrada e saída suaves.
14. **Evitar "gêmeos":** os dois braços iguais e tudo se movendo junto parece máquina.

### Câmera
15. **Pelo menos 4 movimentos de câmera diferentes** e um plano marcante que fique na memória.
16. **O assunto ocupa pelo menos 1/3 da altura da tela** nos momentos importantes.
17. **Transições com motivo** (luz que vira a próxima cena, som que atravessa o corte), não fades genéricos.

### Som
18. **Três camadas:** ambiente (vento, multidão), efeitos ligados às ações (passos, tecido, fogo) e música.
19. **Pelo menos dois silêncios** antes do clímax; o primeiro som depois do silêncio é um dos mais importantes.
20. **Frase sonora de impacto:** subida → impacto → brilho.
21. **Volume final: −14 LUFS** (o padrão do YouTube).
22. **Fugir do "piano e cordas genérico".**

### Elementos do canal
- **Acentos nas legendas:** usar fonte com todos os acentos maiúsculos (Ã, Õ, É, Í, À...). O CapCut já saiu com "NãO" e "PRISãO" por falta deles. Sempre conferir num quadro.
- **Nunca cobrir o sticker de "se inscrever"** nem outros elementos que o usuário colocou no CapCut. Antes de pôr título ou efeito, olhar os quadros onde eles aparecem e deixar espaço.

### O que evitar (cara de template de IA)
- Explosão de partículas genérica, separação RGB, reflexo de lente, neon e quique exagerado.
- Texto demais na tela; legenda cobrindo o assunto; assunto pequeno ou colado na borda.
- Imagem escura demais ou cor sobre a mesma cor.
- Quadros pretos nas transições.

### Revisão antes de entregar
- Folha de contato (um quadro a cada 1–2 s) e tiras de 0,2 s nos momentos-chave.
- Conferir volume (`ffmpeg -af ebur128`) e quadros pretos (`blackdetect`).
- Assistir uma vez inteira, com som, em velocidade normal.
- **Uma rodada de correções**, depois uma última conferida.

---

## 4. Como escrever o pedido (prompt)

- **Dê estrutura de diretor:** duração total, número de cenas, o que cada cena mostra, movimentos de câmera.
- **Mostre referências** (imagem, vídeo) em vez de empilhar adjetivos.
- **Liste o que é proibido** (ver "O que evitar").
- **Para modelos de vídeo por IA:** prompt curto e direto. A imagem de referência entra como **primeiro quadro** do vídeo, que é o que mais garante que a cena seja animada, e não recriada.
- **Não descreva uma ação que já está pronta na imagem.** Se os braços já estão erguidos, diga "continuam erguidos", não "levanta os braços".

---

## 5. Receita: vídeo bíblico vertical (ex.: Elias no altar)

1. **Movimento real (IA):** imagem como primeiro quadro, 9:16, 8–10 s.
   - Mais barato no vidIQ: MiniMax H3 (10 s ≈ 75 créditos). Alternativa: Veo 3.1 Lite (8 s ≈ 80 créditos).
2. **Batida:** librosa na música (ex.: faixa do Suno) para o fogo cair exatamente num tempo forte.
3. **Som:** vento → silêncio → trovão + rugido do fogo + estalo de brasas → música entra.
4. **Acabamento em código (opcional):** abertura/encerramento com luz e partículas (three.js) ou efeitos `holy/` do pixelfx; título com tempo de leitura.
5. **Entrega:** ffmpeg, 1080×1920, −14 LUFS, sem quadros pretos.

---

## 6. Reinstalar num ambiente novo

As instalações não sobrevivem ao fim de uma sessão na nuvem. O jeito mais fácil: rodar, a partir da pasta que contém o `fluxo-de-edicao`,

```bash
bash fluxo-de-edicao/scripts/setup-ambiente.sh
```

Ou, passo a passo:

```bash
# Plugins
claude plugin marketplace add lemomo-ai/lemo-opuscar && claude plugin install lemo-opuscar@lemolab
claude plugin marketplace add patch-gg/pixelfx && claude plugin install pixelfx@pixelfx

# Biblioteca e dependências do lemo-opuscar (precisa de ffmpeg 7+)
sh ~/.claude/plugins/cache/lemolab/lemo-opuscar/*/skills/lemo-opuscar/scripts/setup.sh
sh ~/.claude/plugins/cache/lemolab/lemo-opuscar/*/skills/lemo-opuscar/scripts/setup.sh deps voice music

# video-shotcraft como skill
git clone --depth 1 https://github.com/Vincentwei1021/video-shotcraft ~/video-shotcraft
mkdir -p ~/.claude/skills && ln -sfn ~/video-shotcraft ~/.claude/skills/video-shotcraft

# A palavra-mestra /produzir-video (skill deste repositório)
ln -sfn "$(pwd)/skills/produzir-video" ~/.claude/skills/produzir-video   # rode na raiz do fluxo-de-edicao

# Kit de bibliotecas (física, pós-processamento, batida)
mkdir -p ~/motion-kit && cd ~/motion-kit
uv venv .venv && uv pip install --python .venv/bin/python librosa
npm init -y && npm i three @react-three/fiber @react-three/drei @react-three/rapier @react-three/postprocessing postprocessing react react-dom
```

**ffmpeg 7+:** no ambiente na nuvem, os sites de build estática são bloqueados. O que funcionou foi tirar o binário do pacote `imageio-ffmpeg` do PyPI (`pip download --no-deps imageio-ffmpeg`, extrair o `.whl` e copiar `imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-*` para `/usr/local/bin/ffmpeg`).

**ClaudeAnimationBase sem placa de vídeo:** usar `--soft-gl` e apontar `--chrome` para o Chromium do Playwright. Fica lento (≈7 s por quadro).

---

## 7. Escolha do modelo: Opus 5.5, Fable 5.2 ou Sonnet 5.5

Pesquisa de 22/11/2026 (repositório `sandbase-lab/awesome-fable-5-2`, relatos de criadores na semana de lançamento; nada disso foi medido de forma independente ainda).

| Modelo | Quando usar | Custo |
|---|---|---|
| **Opus 5.5** (padrão) | O dia a dia: edição, Shorts, montagem, ffmpeg, roteiro | Incluído no plano Pro |
| **Fable 5.2** (lançado em 09/11/2026) | Peças especiais: motion graphics muito detalhado, cenas 3D, física, "vídeo vitrine" | **Mais caro, não mais barato**: criadores relatam 1,5x a 4x o custo do Opus na mesma cena (US$ 8 / US$ 40 por milhão de tokens). No Pro, o Fable pode exigir créditos de uso extra (relatado para o 5.1; confirmar no app antes de usar) |
| **Sonnet 5.5** | **Reserva quando o limite do Opus acabar**: tarefas simples, cortes, legendas, textos | O mais econômico dentro do plano |

**Importante:** o Fable **não serve de reserva para quando faltar limite**. Ele gasta mais. A reserva barata é o **Sonnet 5.5**.

### O que o Matt Penny mediu ("Claude Fable 5.2 Just Changed Motion Graphics Forever", transcrição lida em 22/11/2026)
- **Velocidade e custo:** na assinatura, o Fable 5.2 foi **~5x mais lento** e **~3 a 4x mais caro** que o Opus 5.5 para gerar o mesmo vídeo. Na API: Opus US$ 20 e Fable US$ 40 por milhão de tokens de saída.
- **Qualidade:** melhor (reflexos, iluminação, acabamento "premium"), mas **não é um salto enorme quando você usa os repositórios certos, referências e boas ferramentas**. Em vários testes, sem as etiquetas, ele não saberia dizer qual era qual. Diferença clara: cenas isométricas e 3D detalhadas.
- **Lançamento:** a Anthropic dá *resets* grátis no modelo novo; no começo ele tende a estar mais rápido e mais barato do que nunca.
- **Conclusão dele:** nem tudo precisa do Fable. Use quando a peça pede o detalhe extra.

### Como gastar menos (o que mais desperdiça é refazer)
1. **Manifesto de vídeo** (a dica nº 1): um arquivo com o seu jeito de fazer vídeo: ritmo, cores, espaçamento, tipografia, transições de entrada e saída, efeitos sonoros, música, e exemplos de vídeos anteriores. Com ele, o primeiro resultado já sai certo e não precisa refazer 3 ou 4 vezes. Dá para criar a partir de vídeos que você já editou (engenharia reversa) ou respondendo perguntas. **Os nossos ficam em `manifestos/`.**
2. **Fable planeja, Opus executa:** o modelo mais inteligente faz o plano (roteiro, storyboard, decisões) e o Opus constrói. Mais barato e mais rápido.

### As dicas dele (valem para qualquer modelo)
1. **Seja específico:** pense no que quer e descreva com o máximo de detalhe.
2. **Fale em vez de digitar:** pelo **microfone** do app. Falando, você dá mais contexto naturalmente, e é mais rápido.
3. **Use o manifesto de vídeo.**
4. **Mande referências:** print de um estilo de que gostou, ou o link de um vídeo para analisar.
5. **Storyboard antes de vídeos longos:** ver os quadros-chave antes de gastar tempo e dinheiro.
6. **Conecte ferramentas de IA:** vídeo/imagem por IA (Higgsfield, TopView, fal) e ElevenLabs para música e efeitos sonoros.

**Como trocar de modelo no Claude Code:** digite `/model` e escolha; ou toque no nome do modelo embaixo da caixa de mensagem (ex.: "Opus 5.5 Médio"). Todas as skills, o guia e as ferramentas funcionam igual em qualquer modelo.

**O que dizem do Fable 5.2:** mais detalhe, movimento e mecânica de jogo do que o Opus 5.5 ("um salto"); às vezes resolve em esforço *medium* o que o Opus precisava de *max*. Mesmo assim, ele **não assiste vídeo**: revisa quadros parados. Peça sempre a folha de quadros.

### Os 7 padrões de prompt que funcionaram com o Fable (valem para o Opus também)
1. **Diga o entregável e o renderizador na primeira frase:** "um arquivo HTML, 1080×1920, 15 segundos, Canvas/Three.js".
2. **Dê uma régua de qualidade em vez de especificação:** "como um keynote da Apple", "qualidade AAA", "o vídeo mais bonito que você conseguir".
3. **Dê um trabalho que não dá para fingir:** física real, mecanismo real, simulação.
4. **Coreografe o que se move, batida por batida:** descreva as transições (como um estado vira o próximo), não só a lista de cenas.
5. **Escreva a restrição física em voz alta:** "um plano contínuo, sem cortes", "a serpente nunca atravessa o casco".
6. **Escolha o esforço e diga qual:** comece em *medium* para rascunho; suba para *high/max* só quando a composição estiver certa (o custo pode dobrar).
7. **Mande ele conferir o próprio trabalho:** estudar as referências quadro a quadro (um quadro a cada 0,25 s) e abrir a página, corrigir erros e garantir o loop antes de entregar.

### Modelo de prompt (preencher)
```text
Um arquivo HTML autocontido, {1080x1920}, {segundos} segundos, {Canvas/Three.js}, sem arquivos externos.
Objetivo: {uma frase — o que o espectador deve sentir ou entender}.
Régua: {como um keynote da Apple / qualidade AAA / o mais bonito que você conseguir}.
Trabalho real: {o mecanismo que precisa funcionar — física, fogo, partículas}.
Batidas: abre em {primeiro quadro}; depois {transição 1 -> 2 -> 3}; fecha em {último quadro}.
Regra fixa: {o que nunca muda — um plano só, sem cortes, nunca atravessa X}.
Esforço: {medium|high|max}.
Antes de terminar: abra a página, corrija erros e garanta que a animação grava limpa em {segundos} s.
```

---

## 8. Claude + CapCut (vídeo do Matt Penny, transcrição lida em 22/11/2026)

### Como ele trabalha
- Uma **"CapCut Bridge"** (scripts) liga o Claude ao **CapCut instalado no computador**. O Claude cria o projeto, corta, põe textos, efeitos e músicas **dentro do CapCut**, e até aperta botões dele (ex.: remover fundo).
- **⚠️ Para nós: isso exige CapCut de computador.** O usuário trabalha só pelo **celular** (CapCut do celular não pode ser controlado). Então o nosso fluxo é: **eu edito aqui na nuvem e entrego o vídeo pronto** (ou partes separadas para ajustes no CapCut do celular).

### Lições que valem para nós
1. **Transcrição com o tempo de cada palavra** é a base de tudo: cortar silêncios e erros, encaixar legenda karaokê, efeitos e imagens no momento certo. Ele usa **Deepgram** (grátis para começar); nós já temos o **faster-whisper** instalado (grátis, roda aqui).
2. **IA faz 90%, você faz os 10% finais.** Ajuste pequeno (meio segundo, volume, posição) é mais rápido à mão do que pedindo para a IA renderizar tudo de novo. **Para o celular:** quando fizer sentido, entregar também **uma versão sem legenda** e o **arquivo de legenda (.srt)**, para o usuário ajustar no CapCut.
3. **Guia de estilo / manifesto** é "o ativo mais importante" (igual ao vídeo do Fable). Os nossos: `manifestos/`.
4. **Biblioteca de efeitos sonoros com "dicionário":** a IA não ouve áudio, então cada efeito precisa de uma **descrição em texto** (nome do arquivo + o que soa). Efeitos **pré-aprovados** soam melhor que efeitos gerados por IA (os gerados ficaram "50% ruins"). **Música de fundo por IA (ElevenLabs) funciona bem;** para áudio viral, usar biblioteca.
5. **Pedido específico** quando não há skill: dizer onde entra cada coisa, cores, fontes, e terminar com uma **checagem**: "assista tudo, veja se nada cobre o rosto, se texto não bate na legenda, se está tudo escrito certo e se não há trecho parado".
6. **Erros comuns viram skill de checagem:** depois de achar os erros que se repetem, criar uma checagem que os procura sempre.
7. **Processos com passos (ex.: rotoscopia: texto entre a pessoa e o fundo) viram skill:** descrever o passo a passo uma vez, salvar, e depois só pedir "rotoscopa aqui".
8. **Imagem real vs. imagem de IA:** para lugar, pessoa ou objeto real, buscar **foto real** (ele usa Brave Image Search, com chave de API); IA só para o que é ilustrativo.
9. **B-roll por IA:** pedir ideias à IA ("onde caberia um B-roll de 3–4 s e o que mostrar?"), escolher, e gerar com modelo e formato definidos (ex.: Kling, 720p, 16:9). Texto dentro de vídeo de IA costuma sair ilegível.
10. **Correção de cor:** acertar os valores uma vez e salvar como padrão.
11. **Não deixar a IA copiar edições antigas** do mesmo arquivo quando quiser uma nova ("não use edições anteriores deste clipe").

### O capcut-kit (github.com/matt-j-penny/capcut-kit), estudado em 22/11/2026
- **Precisa do CapCut de computador.** No **Mac** funciona tudo: edita os arquivos de projeto do CapCut e também "clica" nos botões dele. No **Windows**, só a parte de arquivos (criar o projeto com os cortes, textos, imagens, posição e keyframes), e ela **nunca foi testada** em Windows de verdade. **No celular não funciona.** Por isso não instalamos.
- Se um dia houver um computador próprio: instalar o CapCut, o Claude Code nele, `uv` e `ffmpeg`, e rodar `uv run capcut-bridge.py doctor` antes de confiar.
- Regras dele que valem para nós:
  - **Legenda sempre a partir de UMA transcrição oficial**, a do áudio que vai ser entregue. Transcrição de um pedaço solto faz a legenda escorregar no fim.
  - **Arquivo de correções** de palavras que a transcrição erra (ex.: nomes próprios, "Claude", termos bíblicos). Corrigir só o texto exibido e aumentar a lista a cada erro novo.
  - **Jogar fora "lascas" de palavra com menos de 0,2 s** (começos falsos nos cortes).
  - **Área segura nos verticais 1080×1920:** tudo que importa entre **y=200 e y=1620** (fora disso, a interface do Shorts/TikTok cobre).
  - **Último quadro:** evitar quadro preto no final, porque o Shorts repete o vídeo em loop e o preto vira uma "piscada". Segurar o último quadro (no FIRE & GRACE o final já é o cartão preto do encerramento, então tudo bem).
  - Dois estilos prontos de legenda dele: (A) caixa preta arredondada com palavras surgindo uma a uma, no centro; (B) Inter Bold branca com contorno preto, sem caixa, baixa, 3–4 palavras por linha, sem animação.

## 9. Narração e legenda sincronizada (aprendido no teste de 22/11/2026)
- **Voz grátis em português do Brasil:** Kokoro (já instalado no lemo-opuscar) tem `pm_alex`, `pm_santa` (masculinas) e `pf_dora` (feminina). Rodar `core/tts/tts.py` com `"lang": "pt-br"`. Escrever números por extenso no texto da voz ("GTA seis") e em algarismo na legenda ("GTA 6").
- **Tempo de cada palavra:** o modelo de transcrição (Whisper) não baixa aqui (Hugging Face bloqueado). Alternativa que funcionou: achar as pausas no áudio de cada frase e distribuir as palavras pelo tamanho. Para precisão total, liberar o Hugging Face no ambiente (pelo computador) e usar o faster-whisper.
- **Mix:** voz comprimida e à frente; música **abaixada ~12 dB** enquanto há voz (ducking); efeitos nos movimentos de câmera.
- **Legenda:** 2–3 palavras por vez, palavra falada em amarelo, faixa escura semitransparente atrás para ler sobre qualquer fundo; nunca em cima de cartão, título ou sticker.
- **Imagens de referência:** sites de jogos são bloqueados; miniaturas do YouTube (`i.ytimg.com/vi/<id>/maxresdefault.jpg`) funcionam para testes.

## 10. Rodízio de ferramentas grátis (regra do usuário, 22/11/2026)
Enquanto os canais não monetizam, **só créditos grátis**. Acabou numa, passa para a próxima da mesma linha, **sempre a de melhor qualidade disponível**. Conferir o saldo antes (ex.: `vidiq_balance`, `account_get_usage` do ElevenLabs, `opusclip_get_usage`).

| Precisa de... | 1ª opção (melhor) | Se acabar → | Último recurso (grátis e ilimitado) |
|---|---|---|---|
| **Vídeo com movimento real** (imagem → vídeo) | **vidIQ** (Veo 3.1 Lite / MiniMax H3), 150 créditos/mês, renova todo dia 27 | **YouTube Create** no celular (foto para vídeo com Veo, grátis; o usuário gera e manda pelo Drive) · planos grátis de outros geradores (Hailuo, Dreamina/CapCut, PixVerse) feitos pelo usuário | Animação em código (three.js, 2,5D): câmera, luz, partículas — sem movimento do personagem |
| **Voz / narração** | **ElevenLabs** (plano grátis: ~10 mil caracteres/mês) | **Vozes neurais da Microsoft (edge-tts)**, grátis e sem limite prático, bem naturais: `pt-BR-AntonioNeural` (masc.), `pt-BR-FranciscaNeural` (fem.), `pt-BR-ThalitaMultilingualNeural` (fem.) | **Kokoro** local (`pm_alex`, `pm_santa`, `pf_dora`): voz pouco natural, só se nada mais funcionar |
| **Cortes automáticos de vídeo longo** | **OpusClip** (teste: 90 min) | **Descript** (se tiver créditos) | Edição aqui com ffmpeg (grátis, sem marca d'água) |
| **Música** | Trilha original sintetizada aqui / biblioteca do lemo-opuscar (CC0/CC BY) | ElevenLabs Music (se houver créditos) | Trilha em código |
| **Edição, 3D, legendas, efeitos** | **Tudo aqui, grátis:** three.js + pós-processamento, lemo-opuscar, pixelfx, video-shotcraft, librosa, ffmpeg | — | — |

- Nunca gerar duas vezes por engano; nunca ativar plano pago, recarga ou "overage".
- ★ **Resolução padrão 1080** nos dois canais. Fazer a conta de créditos antes (resolução × duração × nº de cenas); se não couber, **avisar e propor** (720/768p ampliado, menos cenas ou esperar renovar) — nunca reduzir em silêncio.
- Se nenhuma opção grátis de alta qualidade sobrar para aquele passo, **avisar o usuário** e propor esperar a renovação (ex.: vidIQ dia 27) em vez de baixar a qualidade sem dizer.

### Vozes da Microsoft (edge-tts) — liberadas em 22/11/2026
- Host liberado no ambiente: `speech.platform.bing.com`. A biblioteca `edge-tts` já vem no nível "voice" do lemo-opuscar (`/root/lemo-opuscar/.venv`).
- **Precisa passar o proxy**: `edge_tts.Communicate(texto, "pt-BR-AntonioNeural", rate="+5%", proxy=os.environ["HTTPS_PROXY"])`.
- Vantagem extra: o edge-tts devolve o **tempo exato de cada palavra** (eventos `WordBoundary`), então a legenda karaokê fica **sincronizada de verdade**, sem estimativa.
- Para comparar: `projetos/gta-aula/comparacao-vozes.mp3` (Antonio, Francisca, Thalita, Kokoro).
- ★ **Pronúncia:** palavras com duas leituras saem erradas às vezes. Corrigir **só no texto da voz** (a legenda continua certa) com acento que marca o som: "a seca" (falta de chuva) → "a sêca". Ver `projetos/elias-documentario/v2/voz.py`. Ouvir com o usuário: ele aponta o que soou errado.
- ★ **Duas vozes oficiais (decisão do usuário, 23/11/2026): masculina `pt-BR-AntonioNeural` e feminina `pt-BR-ThalitaMultilingualNeural`.** O usuário indica qual em cada vídeo; se não disser, perguntar na rodada de perguntas. Comparação: `entregas/comparacao-vozes-documentario.mp3` (Antonio, Francisca, Thalita).
- ★ **Limpar SEMPRE a voz do edge-tts antes de mixar** (`ferramentas/limpar_voz.py`): ela vem em MP3 de 24 kHz/48 kbps com **chiado de compressão** (o usuário ouviu "um leve chiado" no Paulo e Silas, 24/11/2026). Redução de ruído espectral (`noisereduce`), de-esser 5–9 kHz e corte acima de 9,5 kHz: −7 dB de agudo, sem perder clareza. ⚠️ O chiado **não** vinha do ambiente (−58 dB) nem do som dos clipes (que já é retirado): medir antes de culpar.
- **Ambiente nos documentários:** evitar ruído contínuo (tochas, multidão feitos com ruído branco) — soa como chiado no celular. Usar só efeitos graves e pontuais (ronco do terremoto filtrado).
- ⚠️ **O edge-tts às vezes devolve a fala cortada** (falha de rede). Sempre conferir: nº de palavras = nº de palavras do texto e duração do áudio ≥ fim da última palavra; refazer só a fala que falhou (`voz.py <ritmo> <nºs das falas>`).
- (Histórico) Voz oficial dos dois canais até 23/11: `pt-BR-AntonioNeural` (escolha do usuário, 23/11/2026). Narração **só quando o usuário pedir**.

## 11. Clipes de IA curtos para narração longa (aprendido em 23/11/2026)
- Clipes de IA costumam ter 8–10 s. Para cobrir uma fala maior **sem refazer a cena**: câmera lenta com quadros intermediários de verdade (fluxo óptico): `setpts=PTS*F,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1`. Fica natural até ~1,7×; acima disso, pedir um clipe mais longo ou usar o último quadro com leve aproximação.
- Preservar o movimento do clipe: nada de zoom artificial nem efeito sobre os personagens; o acabamento vem de títulos, legenda, cor, som e transições suaves.
- Remover o áudio do clipe e fazer o ambiente aqui (controle total da mixagem).

## 12. Receita completa: mini documentário bíblico (Elias, 23/11/2026 — aprovado e publicado)
Modelo pronto em `projetos/elias-documentario/` (v1 = fotos; v2 = clipes; v2-thalita = voz feminina). Passo a passo:
1. **Prompt mestre + imagens do usuário** → ler, conferir a ordem e a precisão bíblica (referências, "redemoinho" leva Elias; a carruagem separa).
2. **Prompts de cena para o YouTube Create** (o usuário gera no celular, grátis): "Animate this exact image…", **"Main movement" primeiro**, "Also", câmera, "No new people, no text", **"Silent video: no sound, no music, no voices"**. **≤ 900 caracteres** (manter 400–650). Pessoas descritas pela aparência.
3. **Voz** (a que o usuário escolher: Antonio ou Thalita) por fala, com tempo de cada palavra; conferir se nenhuma fala veio cortada; corrigir pronúncia só no texto da voz ("a sêca").
   - **Pausas dramáticas** dentro da fala (antes de um grito, de uma resposta, da frase final): partes por cena em `voz.py` (modelo: `projetos/paulo-silas-prisao/`).
   - **Limpar a voz** com `ferramentas/limpar_voz.py` antes de mixar (sem chiado).
4. **Linha do tempo** (`linha.py`) a partir das falas: pré 0,45 s, pós 0,6–1,6 s, dissolve 0,9 s.
5. **Clipes**: câmera lenta por fluxo óptico até caber na fala (seção 11); sem zoom artificial; sem o áudio do clipe.
6. **Acabamento** (`render.py`): título em Cinzel + referência em dourado com contorno, legenda Montserrat palavra por palavra (palavras-chave em dourado, y≈1500, nunca sobre rosto), brilho suave, cor, vinheta, granulado leve, sticker "Inscreva-se" na palavra "inscrever", convite final (QUAL HISTÓRIA… + COMENTE / LIKE / INSCREVA-SE).
7. **Trilha original com instrumentos reais** (`musica.py`, `core/audio/sampler.py` do lemo-opuscar: piano Salamander + orquestra VSCO/VCSL; baixa sozinha do GitHub Releases). Arco: curiosidade → contemplação → cresce até o clímax (silêncio de 0,75 s antes) → delicado → esperança → grandioso → acolhedor. Acordes calculados pela duração de cada cena.
7b. **Se o usuário mandar uma música dele (Suno), ela é a trilha** (ver o fim da seção 13); senão, trilha emocional contínua (seção 13).
8. **Mixagem** (`mix.py`): trilha a ~24% da voz na fala, com os médios (1,5–4 kHz) da trilha reduzidos só durante a fala; sem ambiente de ruído contínuo; −14 LUFS em dois passes.
8b. **Fim do vídeo:** cartão com a referência bíblica + **convite narrado** ("se inscreva, deixe o like e comente qual outra história…") com pergunta, botões e sticker.
9. **Revisão**: folha de contato, quadros de perto (fogo, rostos), blackdetect, ebur128. Mandar **cópia leve** (crf 25) para o celular; guardar o mestre.
10. **Pacote de publicação** (`PUBLICACAO.md`): títulos, descrição com referências e **crédito obrigatório do piano** (CC BY 3.0), tags ≤ 450 caracteres, IA = SIM.
11. **Publicar** (só depois do "sim"): `vidiq_video_upload` com `localFile` (grátis, dá link público) → Metricool `createScheduledPost` (YouTube `short`, público, `isAiGeneratedContent: true`, `madeForKids: false`). Deixar um lembrete (`send_later`) 15 min depois do horário para conferir. ⚠️ **Em 23/11 o Metricool marcou "Publicado", mas no YouTube o Short ficou "Programado para 24/11 00:00"** (erro de fuso: não ficou público às 20h; 1 visualização). O status do Metricool **não basta**: pedir ao usuário um print de **Studio → Conteúdo → o vídeo → Visibilidade** logo depois do horário; se estiver "Programado", mudar para **Público** e salvar. Próxima vez, testar agendar com o horário em UTC ou usar o "autoPublish: false" (o usuário confirma pelo app do Metricool). Lembrar o usuário: conferir "Verificações" no Studio e **pôr na playlist "Mini Documentários"**.
- ⚠️ **vidIQ grátis: no máximo 3 envios ao YouTube por dia** (zera à meia-noite do Pacífico, 5h em Brasília). Com mais Shorts, programar 3 e deixar um lembrete (`send_later`) para o dia seguinte. Conferir o horário programado com `vidiq_user_videos` (scheduledPublishAt em UTC; 23:00Z = 20h).
- Duração: o texto inteiro do usuário vale mais que a meta de segundos; Shorts aceitam até 3 min. Avisar quando passar da meta.
- Tempo de produção aqui: ~25 min de câmera lenta + ~15 min de render (4 núcleos).

## 13. Trilha emocional para mini documentário (pedido do usuário, 24/11/2026)
O usuário pediu trilha **"mais envolvente, acolhedora, emocional, um pouco mais alta, abaixando na narração"**. Modelo: `projetos/paulo-silas-prisao/v-thalita/musica2.py`.
- **Uma música contínua** (não pedaços por cena): piano em arpejo de colcheias + melodia simples que volta, sobre cordas quentes com ataque lento; ~66 BPM, um acorde por compasso.
- Progressão emocional **Bm–G–D–A** (vi–IV–I–V), com Em/A de passagem; resolve em ré maior no fim.
- **Crescendo por cena** (intensidade 0,3 → 0,8): só piano e cordas graves no começo; violoncelo no louvor; violinos a partir do clímax; melodia nos violinos no final; harpa e sino na última nota.
- Clímax (ex.: terremoto) **numa troca de acorde** (grade alinhada), com subida de tímpano e trêmulo; impacto quente, sem metais estridentes.
- **Volume aprovado pelo usuário (2º ajuste, "mais alta um pouco"):** trilha a ~24% da voz na fala (−12,5 dB) e −4,5 dB nos intervalos, **com a faixa 1,5–4 kHz da trilha reduzida pela metade só enquanto há fala** (abre espaço para a voz ser entendida mesmo com a música mais alta). Fade de 1,2 s na entrada e 2 s na saída. Histórico: 13% → 18% → 24%.
- ★ **Quando o usuário manda uma música dele (Suno), ela vira a trilha** (24/11/2026: "Prayer at Midnight" no Paulo e Silas). Analisar a curva de energia (início calmo, crescimento, parte cheia, respiro, clímax final) e **montar dois trechos**: do início da música até perto da frase final, e o **clímax final da música** encaixado para terminar junto com o vídeo (`acrossfade` de 1,5 s). Mesmo ducking (≈24% + corte 1,5–4 kHz na fala). Crédito na descrição: nome da música + FIRE & GRACE.
- ⚠️ **Só mandar o vídeo depois que o ffmpeg terminar** (comando longo vai para segundo plano; esperar o aviso de conclusão). Em 24/11 um arquivo foi enviado antes de terminar e precisou ser reenviado.

## 14. Estilo "Painel de controle" (referência do usuário, 25/11/2026)
Vídeo de referência (story patrocinado de um criador de cortes de GTA, 18 s, gravação de tela): quadros em `manifestos/assets/estilo-painel-referencia.jpg`. **Aprender a técnica; usar a identidade dos nossos canais** (não copiar nome, textos nem o widget dele).
**Fundo:** azul-marinho escuro (≈ #0A1729 → #10243A) com **grade fina de planta técnica** (linhas azul-claras, bem transparentes, ~40 px).
**Janela do vídeo:** a cena fica numa "tela" retangular grande no meio, com **borda azul fina** e **cantoneiras douradas em L** nos 4 cantos (visor de câmera). Embaixo da janela, um rótulo pequeno espaçado: "FEED 01 · GTA VI · AO VIVO".
**Widget no topo esquerdo:** caixinha com borda azul, rótulo pequeno espaçado em azul-claro ("SENSOR DE ATENÇÃO") e uma **onda dourada animada** (senoide que se mexe).
**Títulos:**
- Legenda de figura pequena acima: "FIG. 01 — O QUE NINGUÉM PERCEBEU" (azul-claro, caixa alta, espaçada).
- **Título gigante** em 2 linhas, fonte pesada (tipo Montserrat Black): linha 1 branca, linha 2 **laranja-dourada**, com um **traço laranja** embaixo; fica **por cima da borda de cima da janela**.
- **Etiquetas de etapa** acima da janela: caixa escura com borda colorida, rótulo pequeno ("A MAIORIA FAZ", "ETAPA", "RECEITA") e texto grande ("📺 ASSISTIR LIVE" em vermelho, "PASSO A PASSO ↓" em branco, "$ FAZER DINHEIRO" em dourado, "1 · CONTA DE CORTES").
- **Número de impacto**: "90%" enorme em degradê dourado + "DO TRABALHO" branco, sobre a janela escurecida.
- **Painéis de interface** dentro da janela: barra de título ("FÁBRICA DE CORTES") com rótulo à direita ("ESTÚDIO DE VÍDEOS") e linha dourada embaixo.
**Rótulo de câmera (estilo CFTV)** no canto de baixo do vídeo: "CAM 04" dourado + nome em branco + pílula vermelha "AO VIVO".
**Legenda:** embaixo da janela, 1–3 palavras por vez, branco pesado, palavra-chave em laranja, sem caixa.
**Ritmo:** troca de cena a cada 1–2 s, narração falada do começo ao fim.
**Nossa versão (teste de 25/11/2026, Jogatina Fácil):** `ferramentas/painel/painel.py` + `painel_cfg.json` (rodar na pasta da gameplay). Widget **"RADAR JOGATINA"** com a onda **reagindo ao som do jogo**; título "FIG. 01 — …" + 2 linhas (branco/laranja) sobre a janela; janela do jogo 1000×760 (corte central) com cantoneiras douradas; rótulo "CAM 01 · JASON · AO VIVO"; etiquetas de etapa trocando conforme a cena; falas do jogo grandes embaixo; sticker embaixo da janela. ★ Pedido do usuário: **sem o "FEED" embaixo**; títulos **baseados no que acontece no nosso vídeo**; por enquanto **sem narração, só o som do jogo**.
**Com narração (teste de 25/11/2026, voz Will Brian):** `ferramentas/painel/montar_narracao.py` acha as frases do áudio (pausas), **encaixa cada frase no momento da cena** (ex.: "explosão gigante" na explosão, "e acerta!" no tiro), abaixa o jogo **−13 dB** enquanto ele fala (volta nas pausas), e gera a legenda da narração (até 3 palavras, palavras-chave em laranja). Depois `painel.py <saida> <ini> <fim> <cfg> W <mix.wav>`.

## 15. Vozes grátis × monetização (pesquisa de 25/11/2026 — conferir de novo antes de monetizar)
| Voz | Grátis? | Pode monetizar? |
|---|---|---|
| **ElevenLabs plano grátis** (Will Brian) | sim (10 mil caracteres/mês) | **Não**: o próprio ElevenLabs diz que o plano grátis não tem licença comercial; e áudio feito no grátis continua sem licença mesmo depois de assinar. |
| **Microsoft pelo edge-tts** (Antonio, Thalita) | sim | **Arriscado**: é um acesso não oficial; a Microsoft indica o Azure para uso comercial. |
| **Azure Speech, faixa grátis F0** (mesmas vozes Antonio/Thalita, oficial) | 500 mil caracteres/mês | **Incerto**: respostas conflitantes no fórum da Microsoft; exige conta Azure (pede cartão). |
| **Kokoro** (instalado aqui) | sim, sem limite | **Sim** (licença Apache 2.0), mas a voz é pouco natural. |
| **Voz do próprio usuário** (gravada no celular) | sim | **Sim, 100%**, e conta como conteúdo original para o YouTube. Aqui: limpar ruído, equalizar, cortar respiros, −14 LUFS. |
| **Suno** (músicas e voz) | plano grátis | **Não no plano grátis**: músicas do plano grátis são só para uso pessoal, não podem ser monetizadas (o Suno é dono); **Pro/Premier dão direito comercial**; assinar depois **não** libera músicas antigas. ✅ **O usuário tem plano pago do Suno (confirmado em 25/11/2026)**: músicas e vozes feitas durante a assinatura podem ser monetizadas (conferir se as antigas foram feitas já no plano pago). Uma voz de narração criada no Suno pago seria liberada para monetizar. |
Fontes: help center do ElevenLabs ("Can I publish the content I generate"), Microsoft Q&A sobre edge-tts e sobre o F0, help center do Suno ("What rights do I have with the free plan?").
- **Kokoro "melhorado" (teste 25/11/2026):** gerar frase por frase (`pm_alex`/`pm_santa`, `lang pt-br`, speed 1.05, "GTA seis" por extenso) e tratar com ffmpeg: 1 semitom mais grave (`asetrate=45306,aresample=48000,atempo=1.0595`), EQ de locutor (+3 dB 140 Hz, −2,5 dB 350 Hz, +2,5 dB 3,5 kHz, +1,5 dB 9 kHz), compressor 3:1 e eco curtinho de sala. Comparação: `entregas/comparacao-kokoro.mp3`. É a única voz de IA grátis liberada para monetizar.
- ★ **Voz do usuário (gravada no celular) — tratamento de rádio (25/11/2026):** a gravação dele veio boa (ruído −55 dB, fala −22 dB). Cadeia: `noisereduce` com o ruído das pontas da gravação (prop 0,8) → ffmpeg `highpass=80, +2,5 dB 120 Hz, −3 dB 300 Hz, +3 dB 3,5 kHz, +2 dB 10 kHz, deesser, compressor 4:1 (−22 dB), limiter`. Frases achadas pelas pausas e encaixadas na cena (`ferramentas/painel/montar_natan.py`). Antes/depois: `entregas/sua-voz-antes-depois.mp3`. Ele grava pelo gravador do celular e manda pelo **Drive** (o ditado do teclado vira texto, não áudio).
- ★ **Narração criada no SUNO (plano pago do usuário = liberada para monetizar), 25/11/2026.** Prompts que funcionaram (o usuário aprovou a voz "quase do jeito", parecida com o Will): estilo "a cappella, vocals only, spoken word, young adult Brazilian male voice, warm medium-deep tone, rich and smooth, confident and friendly, authentic conversational delivery, casual gamer talking to chat, relaxed natural pacing…, no music, no instruments…"; excluir "music, singing, … announcer, radio voice, theatrical, exaggerated, forced, high-pitched, very deep, documentary, monotone"; letra coloquial ("Mano…", "cara…", "do nada") com `[A cappella]` `[Spoken Word - … no music]`. Evitar marcações de emoção frase a frase e MAIÚSCULAS (fica forçado). Se vier música: "Get Stems" → Vocals.
- **Tempo exato das palavras** de qualquer narração: transcrição do **ElevenLabs Scribe** (`creative_attach_reference_file` com o link direto do Drive → `creative_transcribe_audio`; ~200 créditos grátis por 20 s). Depois `ferramentas/painel/montar_narracao_suno.py` encaixa as frases na cena e faz a legenda palavra por palavra (encolhe a fonte se passar de 1000 px, mantendo o Black).

## 16. Três referências do usuário (27/11/2026): o que aprender (sem copiar)
Vídeos verticais de anúncio/Reels mandados pelo Drive (gravação de tela). Aprender a **técnica**, usar com a **nossa identidade**.

**Ref. 1 — explicativo claro (fundo bege, laranja de destaque, 55 s)**
- Gancho em letras enormes, 3 linhas, **uma palavra na cor de destaque** ("VÍDEO DE 10 MINUTOS DE UMA **IDEIA**").
- **Legenda de 2 a 4 palavras numa "pílula" branca**, com a palavra-chave colorida. Muda a cada fala.
- Telas de app "falsas" que se escrevem sozinhas: terminal digitando, campo de texto sendo preenchido, lista com ✓ verde aparecendo um por um, barra de progresso até 100%.
- Transição: o quadro novo entra **desfocado e foca** (blur → nítido), com elementos que "pulam" (mola).
- Uma cor só de destaque no vídeo inteiro. Fim com cartão escuro "CLICA NO BOTÃO AQUI EMBAIXO" e seta animada.

**Ref. 2 — tecnológico escuro (preto + brilho laranja, 61 s)**
- Objetos 3D brilhando no centro (claquete com cadeado, placa de vídeo, uma "máquina diretora" que monta o filme).
- **Contadores animados** (0 → 37, 110/600) e **cartões que acendem um por um**.
- Legenda: texto branco simples + **palavra-chave em serifa itálica laranja** (mistura de 2 fontes).
- Lista de etapas com a etapa atual acesa e as outras apagadas (ROTEIRO ✓ → IMAGENS 2 → ...).
- Fim: cartão do perfil com **mãozinha clicando "Seguir" → "Seguindo ✓"** (igual ao nosso sticker).

**Ref. 3 — GTA 6 "17 coisas escondidas" (98 s, 84 mil curtidas)**
- **Formato lista com contador**: selo amarelo grande "8/17" + categoria pequena (VEÍCULOS) + nome do item. Um item a cada 3-5 s.
- **Controle animado** na tela mostrando o botão a apertar (PS e Xbox lado a lado).
- **Chips que pulam** com ícone resumindo o momento ("TEM SETA!", "FUGA RÁPIDA", "NINGUÉM TE VÊ", "CENSURADO", "%$#@!").
- Menus de rádio/atalhos desenhados por cima da cena.
- Fecha com pergunta para comentar: "**QUAL FICOU DE FORA?**" (puxa comentários = algoritmo).

**Como vamos usar** (★ só **opção guardada** para quando o usuário pedir algo diferente; o modelo padrão de cada canal continua o mesmo, ex.: GTA = Painel + narração Suno)
- **Jogatina Fácil:** série "X coisas que você não sabia no GTA 6" no estilo Painel (azul-marinho + amarelo), com contador N/X, chips que pulam, controle com o botão e pergunta no fim. A narração do Suno continua.
- **FIRE & GRACE:** legenda em pílula com a palavra-chave dourada; entrada com desfoque → foco; contador ou lista de etapas quando o tema pedir ("7 vezes que Deus respondeu com fogo"); pergunta no fim ("Qual história você quer na próxima?").
- **Todos:** uma única cor de destaque por vídeo; algo muda na tela a cada 2-4 s; pergunta no fim para comentar.

## 17. Título animado de abertura (pedido do usuário, 27/11/2026)
Referência: modelo do CapCut "Back to HOME" (usar só a **animação do título**, nunca o cenário).
`ferramentas/titulo_animado.py` (classe `Titulo`): cursiva branca escrita letra por letra (Kaushan Script)
→ palavra GRANDE amarela (Montserrat Black) com cada letra pulando e o espaçamento fechando
→ linha pequena espaçada (Montserrat SemiBold) → saída com fade e subida; clarões de luz quente
(filme queimado) na entrada de cada parte e na saída, **fracos** (0,42: forte deixa a tela toda amarela).
Clipe "No deserto": "No deserto," + "ELE VENCEU" + "FIRE & GRACE" de 1,2 s a 11,4 s (antes da voz), no
terço de baixo, sem cobrir rostos; o 1º sticker passou para 13 s para não brigar com o título.
- **Modo "sobe e fixa"** (pedido em 27/11): `Titulo(..., fixar=dict(t=7.2, dur=1.4, escala=0.62, y=0.105))` — o título
  aparece no meio, depois **sobe, diminui e fica fixo no alto** até o fim (a linha pequena some na subida; clarão
  suave quando ele "gruda"). Para isso a imagem precisa vir **sem** o título pintado (apagar por IA de imagem, só a
  faixa de cima; apagar por código deixa mancha).

### 17.1 Modelo aprovado de videoclipe com imagem estática (27/11/2026 — "ficou muito bom, excelente trabalho")
Receita do clipe "No deserto, Ele venceu" (`projetos/clipe-no-deserto/`), usar em todo clipe do Suno:
1. **Imagem SEM título** (pedir ao usuário a versão limpa; apagar título por código deixa mancha).
2. **Câmera de cinema lenta** sobre a imagem (push-in nos versos, abre nos refrões), **âncora vertical no topo**
   (zoom cresce para baixo, para os personagens não subirem para o título fixo).
3. **Abertura sem título** → aos ~1 s o **título animado** no meio (cursiva escrita letra por letra + palavra
   amarela pulando + linha pequena) → aos ~7 s ele **sobe, diminui e fica fixo no céu** até o fim, num canto
   sem rostos (aqui: céu à esquerda, `x=0.2, y=0.105, escala=0.55`).
4. Sol que respira, raios, poeira dourada, pulso de luz na batida só no refrão, clarões suaves (0,42).
5. **Karaokê** com a letra oficial (tempos da transcrição Scribe; conferir palavra por palavra), um verso por linha.
6. **Sticker do canal** (logo do leão, nome FIRE & GRACE inteiro) 3 vezes: depois do título, no meio e no fim,
   num canto livre (aqui: embaixo à esquerda, sobre as pedras).
7. Conferir quadros nos momentos de **zoom máximo** para ver se título/sticker/legenda não encostam em rostos.
8. -14 LUFS; arquivo acima de 400 MB → cópia CRF 20 para enviar.
