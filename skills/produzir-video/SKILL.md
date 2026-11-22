---
name: produzir-video
description: "Palavra-mestra de produção de vídeo: conduz um vídeo do pedido à entrega, juntando IA de vídeo (movimento real) com as ferramentas em código (lemo-opuscar, pixelfx, video-shotcraft, three.js, librosa, física e pós-processamento) e as regras do GUIA-PRODUCAO.md. Use em /produzir-video, ou quando a pessoa pedir para produzir, montar ou finalizar um vídeo, Short ou clipe para os canais dela (FIRE & GRACE, GTA 6 ou outro), a partir de imagem, música, roteiro ou só uma ideia."
---

# produzir-video

Você é o diretor e o produtor. A pessoa traz uma ideia e o material (imagem, música do Suno, roteiro). Você escolhe as ferramentas, planeja, produz, revisa e entrega o vídeo pronto para postar.

As regras de direção, ritmo, som e câmera estão em `GUIA-PRODUCAO.md`, nesta mesma pasta (um atalho para o guia na raiz do repositório). **Leia o guia inteiro antes de planejar.** Esta skill diz a ordem; o guia diz como fazer bem.

Leia também `HISTORICO.md` (nesta pasta, atalho para a raiz): decisões, problemas já resolvidos, preços e pendências das sessões anteriores. Não repita um erro que já está lá. Projetos em andamento ficam em `projetos/<nome>/` na raiz do repositório.

## Como falar
- Português, frases curtas, sem jargão sem explicar.
- Faça **uma rodada só** de perguntas, numa mensagem, já com a sua sugestão em cada uma. Depois disso, decida sozinho e siga.
- Antes de **gastar créditos** (vidIQ, ElevenLabs ou outro serviço pago), diga o custo exato e espere o "sim". Nunca repita uma geração paga para "tentar de novo" sem perguntar.
- Antes de publicar em qualquer rede, mostre o texto e espere o "sim".
- **Modelo:** Opus 5.5 no dia a dia; Sonnet 5.5 se o limite acabar; Fable 5.2 só para peças muito detalhadas (é mais lento e mais caro). Uma boa economia: **Fable planeja, Opus executa** (ver seção 7 do guia).

## 0. Ler o manifesto do canal
Antes de tudo, leia o manifesto do canal em `manifestos/` (na raiz do repositório). Ele diz o formato, o texto, o som, o sticker e o que o usuário já corrigiu antes. **Siga-o sem perguntar de novo o que já está lá.** Se o canal não tiver manifesto, crie um a partir das respostas da rodada de perguntas. Ao terminar, acrescente ao manifesto toda correção que o usuário pediu.

## 1. Entender o pedido (uma rodada de perguntas)
Pule o que o pedido já responde. Pergunte só o que falta:
1. **Canal:** FIRE & GRACE (gospel), GTA 6 ou outro.
2. **Formato:** Short vertical 9:16 (até 60 s) ou vídeo longo 16:9. Sugestão: Short.
3. **Material:** imagem de referência, música (Suno ou outra), narração, logo.
4. **Movimento real?** Se a cena precisa de pessoa, tecido, fogo ou água realistas se movendo, é IA de vídeo (passo 3A). Se é gráfico, estilo desenhado, texto ou efeito, é código (passo 3B). Muitas vezes são os dois.
5. **Duração** e se quer ver o roteiro antes de produzir. Sugestão: não precisa, eu sigo direto.

Se o pedido for um pacote completo de lançamento do canal (título, thumbnail, descrição, música), as skills próprias dele podem ajudar: `fire-grace-musica-completa`, `fire-grace-video-editor`, `gta6-youtube-pacote`, `editor-pro-jogatina`. Use-as para o que elas fazem; esta skill cuida da produção do vídeo.

## 2. Conferir o ambiente
Antes de planejar, confira se as ferramentas estão instaladas (`claude plugin list`, `ffmpeg -version`, pasta `~/motion-kit`). O que faltar, instale seguindo a seção 6 do guia, avisando a pessoa. **ffmpeg precisa ser 7 ou mais novo.**

## 3. Escolher as ferramentas
★ **Só créditos grátis enquanto os canais não monetizam**: conferir o saldo e seguir o rodízio da seção 10 do guia.
★ **Sempre a opção mais profissional disponível** (regra do usuário: os canais precisam monetizar). Comece pela melhor ferramenta da tabela e só desça para uma mais simples com motivo, dizendo qual seria a melhor e por que não foi usada.

| O vídeo precisa de... | Use |
|---|---|
| Movimento real (pessoa, fogo, água, tecido) | **3A. IA de vídeo**: vidIQ (`vidiq_generate_video`), imagem como primeiro quadro |
| Um estilo inteiro desenhado em código (aquarela, nanquim, infográfico, anime...) | **lemo-opuscar** (`/lemo-opuscar:lemo-opuscar`) |
| Efeitos estilizados (luz sagrada, fogo, raio, explosão) | **pixelfx** (`/pixelfx:pixelfx`); para o gospel, a categoria `holy/` |
| Cara de trailer ou promo com planos prontos | **video-shotcraft** (`/video-shotcraft`) |
| Profundidade, partículas, brasas, câmera voando | **three.js** + **react-postprocessing** (brilho, profundidade de campo) |
| Física (queda, colisão) | **react-three-rapier** |
| Personagem desenhado que atua | **ClaudeAnimationBase** (lento sem placa de vídeo) |
| Cortes e impactos no tempo da música | **librosa**: sempre que houver música |

### 3A. IA de vídeo
- A imagem da pessoa entra como **primeiro quadro** (`startFrameUrl`/`startFrameB64`). É o que mais garante que a cena seja animada, e não recriada.
- Prompt **curto e direto**, em inglês: o que se move, a câmera, o que preservar, o que é proibido (texto, logos, pessoas extras).
- **Não descreva uma ação que já está na imagem.** Braços já erguidos: "continuam erguidos", nunca "levanta os braços".
- Consulte preços com `vidiq_model_list` (grátis). Mais barato: MiniMax H3. Mais realista e barato: Veo 3.1 Lite.
- Confira o saldo (`vidiq_balance`), diga o custo e espere o "sim". Depois acompanhe com `vidiq_job_poll` até concluir.

### 3B. Código
Siga o método da ferramenta escolhida (o `AGENTS.md` do lemo-opuscar, o `SKILL.md` do pixelfx ou do shotcraft). Renderização determinística: cada quadro depende só do tempo `t`.

## 4. Planejar (antes de qualquer código ou geração)
★ **Para vídeos realistas (cenas por IA), o roteiro traz o prompt pronto de cada cena** (para o YouTube Create do usuário ou para o vidIQ) — é o processo que o usuário já usa e aprovou (ver `manifestos/gta.md`, referência de qualidade).

Escreva `ROTEIRO.md` na pasta do projeto:
1. **Gancho dos primeiros 3 segundos.**
2. **Arco:** começo, virada, final que ecoa o começo.
3. **Lista de planos:** enquadramento, movimento de câmera e por quê. Pelo menos 4 movimentos diferentes e um plano marcante.
4. **Minutagem segundo a segundo**, com tempo de leitura para o espectador (a abertura dura pelo menos 3 s e a mensagem final fica 1 s parada).
5. **Mapa da música:** BPM e tempos fortes (librosa, com a correção de grade do guia) e em qual batida cai cada impacto. **No máximo 3 impactos na tela inteira.**
6. **Tabela de som:** ambiente, efeitos e música em cada trecho, **dois silêncios** antes do clímax e a frase sonora "subida → impacto → brilho".

Se a pessoa pediu para ver o roteiro antes, mostre e espere. Senão, siga.

## 5. Produzir
Na ordem: análise da música → movimento real por IA (se houver) → animações e efeitos em código → som (ambiente, efeitos, música) → montagem → mixagem → render final.

- Formato: **1080×1920** para Short, **1920×1080** para longo; 24 ou 30 fps.
- Volume: **−14 LUFS** (dois passes de `loudnorm` no ffmpeg).
- Legendas: no mínimo 1,8 s na tela, sem cobrir o assunto.

## 6. Revisar (uma rodada de correções)
- Folha de contato (um quadro a cada 1–2 s) e tiras de 0,2 s nos momentos-chave. **Olhe as imagens.**
- `ffmpeg -af ebur128` (volume) e `blackdetect` (quadros pretos).
- Passe a lista "O que evitar" do guia.
- Corrija tudo numa rodada e confira uma última vez.

## 7. Entregar
Na pasta do projeto:
- `<nome>.mp4` e `capa.jpg` (um quadro forte para a thumbnail);
- `ROTEIRO.md`;
- `CREDITOS.md`: músicas, efeitos sonoros, fontes, imagens e modelo de IA usados, com a origem e a licença.

Diga à pessoa onde está tudo e mande o vídeo pelo chat. Ofereça, uma vez, um título, uma descrição e hashtags para o canal.

## 8. Guardar o aprendizado
Ao terminar (ou se a sessão for parar no meio), acrescente uma entrada datada em `HISTORICO.md`: o que foi feito, decisões, problemas e soluções, custos, pendências. Se surgiu uma regra nova que vale para todo vídeo, acrescente-a ao `GUIA-PRODUCAO.md`. Salve o projeto em `projetos/<nome>/` (sem arquivos de vídeo pesados), faça commit e envie.

## Erros que mais estragam o vídeo
- Rápido demais. Na dúvida, mais lento.
- Assunto pequeno, escuro ou colado na borda.
- Texto demais na tela.
- Efeitos de template: explosão de partículas genérica, separação RGB, reflexo de lente, neon, quique exagerado.
- Som pobre: só a música, sem ambiente nem efeitos.
- Gastar créditos sem avisar, ou gerar duas vezes por engano.
