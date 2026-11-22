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
