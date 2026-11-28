# Histórico de sessões

Diário do que foi feito, decidido e aprendido, para nada se perder entre uma sessão e outra.

---

## 21/11/2026: montagem do kit de produção

### O que foi feito
1. **Repositórios estudados e instalados** (lista do vídeo "10 GitHub Repos to 10x Your AI Motion Graphics", de Matt Penny):
   - Plugins ativos: **lemo-opuscar**, **pixelfx**. Skill ativa: **video-shotcraft**.
   - Bibliotecas no kit `~/motion-kit`: **librosa**, **three.js**, **react-three-rapier**, **react-postprocessing**.
   - Para consulta: **three.js** (repositório completo), **ClaudeAnimationBase**, **awesome-opus5-5-videos**, **opus-video-prompts**.
   - **Blender MCP: não instalado** (decisão do usuário: pesado e sensível).
2. **[`GUIA-PRODUCAO.md`](GUIA-PRODUCAO.md):** tudo o que foi aprendido, em português.
3. **Palavra-mestra `/produzir-video`** ([`skills/produzir-video/SKILL.md`](skills/produzir-video/SKILL.md)): conduz o vídeo do pedido à entrega.
4. **[`scripts/setup-ambiente.sh`](scripts/setup-ambiente.sh):** reinstala tudo numa sessão nova (testado em 21/11).
5. **Projeto do Elias** ([`projetos/elias-altar-fogo/`](projetos/elias-altar-fogo/PROJETO.md)): imagem, prompt corrigido e plano.
6. **Lembrete agendado:** 27/11/2026, 19h (Brasília), para gerar o vídeo do Elias quando os créditos do vidIQ renovarem.

### Decisões
- **Movimento real = IA de vídeo; acabamento = código.** Os repositórios em código não fazem vídeo realista.
- **Gerar vídeo sem gastar dinheiro por enquanto:** só com créditos de planos grátis.
- **Modelo do Elias:** MiniMax H3, 10 s (75 créditos). Alternativa: Veo 3.1 Lite, 8 s.
- **Não atualizar o three.js do lemo-opuscar** (0.170) para não quebrar; o 0.187 fica só para consulta.

### O que esbarrou e como foi resolvido
| Problema | Solução |
|---|---|
| O lemo-opuscar exige **ffmpeg 7+** e o Ubuntu tem 6.1 | Os sites de build estática são bloqueados pela rede. Funcionou: binário do pacote `imageio-ffmpeg` (PyPI), versão 9.0.2. O `ffprobe` 6.1 do sistema basta |
| **ElevenLabs** não gera vídeo | Só no plano pago; o plano grátis recusa |
| **vidIQ** cobra créditos | Saldo grátis: 150 créditos por mês (renova dia 27). Assistir um vídeo do YouTube inteiro: 25; transcrição: 5; dados do vídeo: 5 |
| **youtube.com** bloqueado pela rede | Ler vídeos do YouTube pelo vidIQ (transcrição ou dados) |
| Envio da imagem ao vidIQ pelo terminal bloqueado (`mcp.vidiq.com`) | Reanexar a imagem no chat no dia da geração |
| **YouTube Create** | Não há conexão com ele. O app do YouTube (Shorts) tem "foto para vídeo" grátis; dá para testar pelo celular |
| Envio ao GitHub falhou (403) | Voltou a funcionar depois de reconectar o GitHub |
| ClaudeAnimationBase sem placa de vídeo | `--soft-gl` e Chromium do Playwright; ≈7 s por quadro |
| **Google Drive** bloqueado pela rede | Liberar o Drive exige aprovar pelo **computador** (no celular não aparece a opção). Sem computador: anexar o arquivo no chat, ou usar ferramentas que baixam o link pelos servidores delas (OpusClip, Descript) |
| Aprovações de ambiente (rede, script) | **Só aparecem para aprovar no computador** (navegador em claude.ai/code). No celular a janela diz "revise no computador". Feito com notebook emprestado em 21/11 |
| Google Drive liberado | Link compartilhado baixa direto: `https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t` |
| Arquivo grande (gameplay de 2 h, 1,64 GB) | Não cabe como anexo. Melhor: cortar os melhores trechos no **CapCut** (20 s a 2 min, 1080p 30 fps) e anexar um por vez |

### Pesquisa: ferramentas de foto para vídeo com movimento real (nov/2026)
- **Melhor qualidade (pagas):** Google Veo 3.1 (o mais realista), Kling 3.0 (melhor para pessoas; custo-benefício; 4K), Runway Gen-4.5 (uso profissional, controle de câmera).
- **Com plano grátis:** Hailuo (créditos diários), Dreamina/CapCut, PixVerse, Luma Dream Machine (rascunhos rápidos), Pika 2.5 (até 15 s).
- **Atenção:** o Sora (OpenAI) está sendo descontinuado. Planos grátis costumam ter marca d'água, resolução menor e restrição de uso comercial.

### Ferramentas próprias criadas
- `ferramentas/short-gameplay.sh`: corta um trecho, põe título em 2 linhas abaixo do sticker do canal, 1080×1920, −14 LUFS.
- `ferramentas/sticker-inscreva.py`: sticker animado "Inscreva-se" em PT-BR (5,6 s, transparente; o usuário quer **no mínimo 5 s na tela**). Aplicar com `overlay=160:110` no momento desejado.

### 22/11/2026: estudo do Fable 5.2
- Vídeo pedido: "Claude Fable 5.2 Just Changed Motion Graphics Forever" (Matt Penny). **YouTube liberado no ambiente, mas o YouTube bloqueia servidores na nuvem** ("confirme que não é robô"): só deu para ler o título. Para estudar um vídeo do YouTube: o usuário copia a transcrição ("Mostrar transcrição") e cola no chat, ou vidIQ (5 créditos).
- Estudado pelos guias do `sandbase-lab/awesome-fable-5-2` e pesquisa na web. Resultado na seção 7 do `GUIA-PRODUCAO.md`. **Conclusão: Fable é mais caro que o Opus; a reserva barata é o Sonnet 5.5.**
- Depois, o usuário colou a **transcrição** do vídeo. Lições na seção 7 do guia: Fable ~5x mais lento e ~3–4x mais caro; a maior economia é não refazer, usando um **manifesto de vídeo**; Fable planeja e Opus executa. Criados `manifestos/gta.md` (completo, a partir dos Shorts) e `manifestos/fire-grace.md` (rascunho com perguntas).

### 22/11/2026: Claude + CapCut
- Transcrição colada pelo usuário (vídeo do Matt Penny sobre editar no CapCut com o Claude). Lições na seção 8 do guia. **A "CapCut Bridge" precisa de CapCut no computador; o usuário só tem celular**, então seguimos editando na nuvem e entregando pronto (com versão sem legenda + .srt quando ajudar).

### 22/11/2026: publicação automática
- **GTA (JOGATINA FACIL):** já estava no vidIQ do Claude, com permissão de publicar.
- **FIRE & GRACE:** o vidIQ recusou (plano grátis = 1 canal; o canal já estava em outra conta vidIQ, a natanmusicagospel). **Conectado no Metricool** (marca 8216784) pelo notebook. Os horários do Metricool (16h/10h) eram média geral, não do canal (erro corrigido). Manter o padrão do usuário (longo 19h40, Shorts após 20h) até chegarem os prints do YouTube Studio.
- Liberado `mcp.vidiq.com` no ambiente (envio de arquivos ao vidIQ).
- **YouTube Create não tem conexão** (app de celular). Alternativa: Veo/MiniMax pelo vidIQ, ou o usuário gera no app e manda pelo Drive.

### 22/11/2026: teste do Short "mapa dos supercarros"
- Feito só para testar o aprendizado (não publicar). Ver `projetos/gta-mapa-exoticos/`. Sites de jogos são bloqueados pela rede; **miniaturas do YouTube (i.ytimg.com) e GitHub funcionam** para pegar imagens de referência.

### 22/11/2026: retorno do usuário sobre os testes do mapa
- "Ficou bom, mas pode melhorar. Nos próximos testes, usar os **melhores recursos**, algo **mais profissional**", citando o **three.js** (3D).
- ★ **Regra para os próximos testes:** não ficar só em 2D com PIL. Usar o que temos de melhor:
  1. **three.js** (cena 3D de verdade: mapa em relevo/inclinado, câmera voando, pinos 3D, carro em cartão 3D com reflexo) + **react-postprocessing**/`core/three/post.js` do lemo-opuscar (brilho, profundidade de campo, granulado).
  2. Um **estilo do lemo-opuscar** que combine (ex.: *3D Map Explainer*, *Satellite Briefing*, *Glass Product Render*), seguindo o `DIRECTOR.md` (roteiro antes, plano marcante, 4+ movimentos de câmera).
  3. **librosa** para cortes e impactos na batida da trilha.
  4. **Voz melhor** (ElevenLabs, com custo mostrado antes) quando for para valer.
  5. **Imagens reais do jogo** (prints do usuário) quando for para publicar.
- Sem placa de vídeo aqui, o 3D renderiza mais devagar (minutos por vídeo curto), mas funciona.

### 23/11/2026: voz substituta do ElevenLabs
- Pedido do usuário: substituto melhor que o Kokoro ("voz nada natural") para quando o ElevenLabs acabar. Pesquisado: XTTS v2 e Qwen3-TTS (bons, mas precisam baixar modelos do Hugging Face, bloqueado aqui, e são lentos sem placa de vídeo); **escolhido: vozes neurais da Microsoft (edge-tts)**, grátis e naturais. Liberado `speech.platform.bing.com` (aprovado pelo notebook). Ver seção 10 do guia.
- Orientado o usuário a sair das contas no notebook emprestado (Claude, Metricool, vidIQ, GitHub, Google) e conferir pelo celular.
- **Concluído (23/11):** saiu das contas no notebook e apagou os dados de 24 h. Pelo celular, desconectou as sessões do Windows nas duas contas Google (natanduarte9 e natanmusicagospel). GitHub sem sessão do Windows. vidIQ e Metricool seguem ligados aos canais (não dependem do notebook). Caminho no celular: Configurações → Google → Gerenciar sua Conta → Segurança e login → Seus dispositivos.

### 23/11/2026: documentário "A vida do profeta Elias" (Short FIRE & GRACE), versão 1
- Pedido: prompt mestre do usuário + 6 imagens. Decisões dele: **texto da narração inteiro, sem acelerar (~96 s)** e canal **FIRE & GRACE**. Projeto em `projetos/elias-documentario/` (roteiro, prompts da versão 2, scripts).
- Feito em código, sem gastar créditos: câmera diferente por cena, fogo que cintila e "respira" (cenas 3 e 6), água correndo e névoa (2), poeira na luz (1, 4, 5), brasas, brilho, granulado, vinheta, 2 impactos ("fogo" e "redemoinho"), títulos em Cinzel + referência em dourado, legenda palavra por palavra (tempo exato do edge-tts), sticker na palavra "inscrever", convite final com botões.
- ★ **Trilha com instrumentos reais gravados** (lemo-opuscar `sampler.py`: piano Salamander CC BY 3.0 — crédito obrigatório na descrição —, orquestra VSCO 2 CE/VCSL CC0). Os pacotes baixam do GitHub Releases (funciona). Ducking: trilha a 15% da voz na fala.
- Entrega: −14 LUFS, sem quadros pretos. Mestre 420 MB (granulado pesa) em `/home/user/elias-doc/`; cópia leve de 56 MB enviada no chat.
- Problemas: upscaler por IA (Real-ESRGAN) precisa de PyTorch, e `download.pytorch.org` é bloqueado → ampliação Lanczos (também preserva os rostos). OpenCV instalado no venv do lemo (entrou no script de instalação). Fontes Cinzel/Montserrat guardadas em `ferramentas/fontes/`.
- ★ **Regra nova do usuário:** créditos/tokens grátis podem ser usados para ter qualidade (avisando o que gastou); **dinheiro de verdade nunca** (CLAUDE.md e skill atualizados).
- Saldos: vidIQ 22 créditos avulsos (150 renovam 27/11); ElevenLabs 8.044 caracteres (o plano grátis não permite uso comercial da voz, pelo que sei → manter Antonio).
- **Versão 2 (pendente):** movimento real nas 6 cenas: o usuário gera no YouTube Create com os prompts do `ROTEIRO.md` e manda pelo Drive, ou eu gero as cenas 3 e 6 no vidIQ em 27/11.

### 23/11/2026: documentário de Elias, versão 2 (movimento real)
- O usuário gerou as 6 cenas no **YouTube Create** com os prompts curtos (≤900 caracteres, "Main movement" primeiro, sem som) e mandou com um novo prompt mestre. Resultado aprovado na conferência: rosto de Elias igual nas 6, a carruagem voa de verdade.
- ★ **Técnica nova: câmera lenta com quadros intermediários** (`ffmpeg minterpolate=mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1`) para clipes de 10 s cobrirem a narração (até 1,7×) sem "travar". Sem artefatos visíveis. ~25 min para 6 clipes (4 núcleos).
- Prompt mestre pediu 60–70 s; com o texto inteiro deu **86,7 s** (voz +8%). Música refeita para o novo tempo (o `musica.py` agora calcula os acordes pela duração das cenas).
- Entregue: cópia leve no chat; mestre (278 MB), `.srt` e pacote de publicação em `/home/user/projeto_elias/exportacao/`. Detalhes: `projetos/elias-documentario/v2/RELATORIO.md`.
- Correção pedida pelo usuário: "seca" saiu com "e" aberto (séca). Voz refeita só na cena 2 com "sêca" no texto da voz (legenda inalterada), mesmo tempo de cena; só os quadros da cena 2 renderizados de novo.
- **Versão com voz feminina (Thalita)**, a pedido do usuário (preferiu a Thalita à Francisca). As duas versões ficam guardadas: `/home/user/projeto_elias/exportacao/documentario_historia_de_elias.mp4` (Antonio) e `/home/user/projeto_elias_thalita/exportacao/documentario_historia_de_elias_thalita.mp4` (Thalita, ritmo +3%, cada cena termina no mesmo instante da versão Antonio → reaproveitou as câmeras lentas). Scripts em `projetos/elias-documentario/v2-thalita/`.
- ★ **Publicado (agendado) com a voz da Thalita:** Metricool post 439175771, YouTube Short, **23/11/2026 20h00** (Brasília), público, IA = sim, não infantil, categoria Educação, título "A HISTÓRIA DE ELIAS: o profeta que viu o fogo cair do céu 🔥". Arquivo enviado pelo `vidiq_video_upload` (localFile, grátis; o Metricool copiou para o servidor dele). Conferido às 20h15: **PUBLICADO** sem erro → https://www.youtube.com/shorts/AzTanu9SXWw Usuário vai criar a playlist pública **"Mini Documentários"** pelo app (não há ferramenta para isso). (Metricool precisa de link público do arquivo; mostrar tudo e esperar o "sim").

### 25/11/2026: estilo "Painel de controle" (referência do usuário)
- O usuário mandou a gravação de um story (criador de cortes de GTA) para aprender o estilo. Analisado quadro a quadro (guia, seção 14) e feito um **teste** com o trecho da explosão no pântano: `entregas/gta-cortes/teste-estilo-painel.mp4` (26 s, só som do jogo).
- O usuário citou "a voz do Will" para o GTA — **não havia registro** disso (o combinado era vozes do jogo; narração Antonio/Thalita). Provável: voz "Will" do ElevenLabs. **Perguntar e confirmar** antes de usar.
- Voz do GTA confirmada: **Will Brian (ElevenLabs)**. Narração do teste gerada (269 caracteres; sobram ~7.775). O download do ElevenLabs é bloqueado aqui → o usuário baixou e mandou pelo Drive. Teste com narração: `entregas/gta-cortes/teste-painel-will.mp4` (27 s).
- ★★ O usuário aprovou o teste com narração: **todos os Shorts de GTA agora no estilo Painel** (manifesto do GTA atualizado).
- Pergunta do usuário sobre vozes grátis para monetizar: pesquisado (guia, seção 15). Resposta: só a voz dele e o Kokoro são 100% liberados; Microsoft pelo edge-tts não é liberado oficialmente (risco baixo); ElevenLabs grátis não.
- Kokoro melhorado testado (Alex e Santa, com tratamento): **o usuário achou ruim**. Decisão: **ele vai gravar a própria voz** para os vídeos monetizados. Gravação recebida pelo Drive (29 s, boa qualidade) → tratamento de rádio + encaixe na cena: `entregas/gta-cortes/teste-painel-natan.mp4` (28 s). **O usuário não gostou da própria voz.** Não insistir nessa opção.
- **Voz do Suno**: depois de 4 ajustes no prompt (séria → forçada → natural de streamer → "parecida com o Will"), o usuário mandou a narração. Montada com tempo exato das palavras (Scribe): `entregas/gta-cortes/teste-painel-suno.mp4`. Liberada para monetizar (Suno pago). ★★★ **Aprovado como MODELO DEFINITIVO dos vídeos de gameplay de GTA** (manifesto atualizado). O usuário vai postar esse teste **hoje (25/11) às 18h manualmente**; o Short 4 antigo de sexta (mesma cena) foi cancelado.
- Shorts 4, 5 e 6 de GTA programados (25/11 6h).

### 24/11/2026: resumo do dia (o que aprendemos)
- **GTA:** achar os melhores momentos de uma gameplay longa (som + movimento), falas do jogo em legenda grande, títulos com palavras simples, limite de 3 envios/dia do vidIQ, conferir a agenda do canal antes de programar.
- **FIRE & GRACE:** 2º mini documentário (Paulo e Silas) com pausas dramáticas, voz limpa (sem chiado), convite final narrado, trilha emocional contínua e, por fim, a **música do usuário (Suno)** como trilha; aprovado ("ficou excelente") e agendado.
- **Atendimento:** sempre em português; só mandar vídeo depois que a exportação terminar; conferir a visibilidade no Studio depois de publicar pelo Metricool.
- O lembrete do Elias no altar (27/11) foi cancelado pelo usuário.

### 24/11/2026: 2º mini documentário — Paulo e Silas na prisão (FIRE & GRACE)
- Prompt mestre + 6 clipes do YouTube Create. Montado pela receita da seção 12 (voz Antonio, câmera lenta, trilha real, legenda, referências, cartão final ATOS 16:25–34). 88,8 s. Projeto: `projetos/paulo-silas-prisao/`.
- ★ Novo: **pausas dramáticas dentro da fala** (`voz.py` com partes por cena) e checagem automática de fala cortada.
- ⚠️ Respondi em inglês de novo durante o trabalho; o usuário pediu português. Regra reforçada no CLAUDE.md.
- Pedidos do usuário: **voz da Thalita** (versão Antonio guardada), **tirar o chiado** (vinha da voz do edge-tts, não do som dos clipes; resolvido com `ferramentas/limpar_voz.py` e sem ambiente de ruído) e **convite no final** narrado ("se inscreva, deixe o like e comente qual outra história…") com pergunta e botões. Final: 97,7 s, −14,4 LUFS, `/home/user/projeto_paulo_thalita/exportacao/PAULO_E_SILAS_NA_PRISAO_DOCUMENTARIO_THALITA.mp4`.
- Trilha refeita a pedido: contínua, emocional e acolhedora (Bm–G–D–A, piano + cordas, crescendo), ~18% da voz na fala. Guia seção 13.
- Trilha mais alta a pedido (24% da voz + corte de médios na fala). Depois o usuário mandou a música dele do Suno, **"Prayer at Midnight"** (2:53): virou a trilha (início até 81 s + clímax final 155,75–173,2 s).
- ★ **Aprovado ("ficou excelente") e agendado:** Metricool post 440845916, YouTube Short, **24/11/2026 20h00**, título "PAULO E SILAS NA PRISÃO: o louvor que abriu as portas 🔥", público, IA = sim, Educação. Conferido às 20h15: **PUBLICADO** pelo Metricool → https://www.youtube.com/shorts/OYrADG-GB_I (usuário confere a visibilidade no Studio e põe na playlist).

### 24/11/2026: retorno do usuário sobre o mini documentário
- ★ O usuário disse que o Short do Elias (mini documentário) **"deu super certo, foi muito bom"** e que vão **produzir mais vídeos como aquele logo**. Formato aprovado: seguir a receita da seção 12 do guia. Ideia: usar os comentários ("qual história você quer ver?") para escolher a próxima.

### 24/11/2026: 5 Shorts do Jogatina Fácil a partir da gameplay de 2h25
- Pedido: exatamente 5 Shorts de 20–28 s (máx. 30). Baixada a gameplay inteira do Drive (1,6 GB) — **o Drive liberado no ambiente resolve arquivos grandes, sem precisar cortar no CapCut**.
- ★ Técnica nova: **achar os melhores momentos por análise de som + movimento** (`projetos/gta-cortes-pantano/analisar.py`), depois folhas de contato para escolher. Mostrada ao usuário uma imagem com 5 escolhidos + 2 reservas; aprovou os 5.
- Entregues 5 Shorts (25–26 s, −14 LUFS, 1080×1920, som do jogo, sticker 5,6 s). Detalhes em `projetos/gta-cortes-pantano/PROJETO.md`.
- Correções do usuário: **falas do jogo em legenda grande na faixa de baixo** (lidas quadro a quadro da legenda do jogo, palavrões com asterisco) e **Short 5 trocado** pela briga no aerobarco (0:48:00–0:48:26, cabeça na hélice). Regra nova no manifesto do GTA.
- Short 6 a pedido: "ELES CHEGARAM NA HORA ERRADA!" (0:04:30–0:05:04 + explosão do avião, 37,7 s).
- Publicação aprovada: 6 Shorts, um por dia às 20h (24 a 29/11), vídeo relacionado = live "Primeiras horas de gta6 parte 4". Shorts 1–3 programados e conferidos (20h certinho); 4–6 esperam o limite diário do vidIQ (**feito em 25/11: 4, 5 e 6 programados; o usuário conferiu no Studio: "a programação deu certo"**). Short 1 (Tiroteio) movido para 30/11 20h a pedido (não lotar o dia 24). vidIQ: 7 créditos (150 renovam 27/11).

### Contas e saldos (21/11/2026)
- **OpusClip:** plano de teste, **90 minutos** de processamento (~1 min de saldo por minuto de vídeo). Aceita link do Google Drive e pode limitar o trecho (`rangeStart`/`rangeEnd`). No teste, os cortes podem sair com marca d'água.
- **vidIQ:** 2 créditos (150 renovam em 27/11).
- **ElevenLabs:** plano grátis, sem geração de vídeo.

### Pendências
- [x] ~~27/11, 19h: gerar o vídeo do Elias no altar~~ — **cancelado pelo usuário em 24/11**: o mini documentário de Elias (publicado) ocupou o lugar. Lembrete apagado.
- [x] Short do Elias: o usuário pôs na playlist "MINI DOCUMENTÁRIO" e o relacionado "DEUS AINDA RESPONDE COM FOGO". ⚠️ Estava "Programado 24/11 00:00" (erro de fuso do Metricool) → orientado a mudar para Público.
- [x] **Documentário de Elias, versão 2 (entregue 23/11):** clipes do YouTube Create do usuário (ou vidIQ em 27/11, cenas 3 e 6) → trocar as fotos e reexportar. Depois: título, descrição (com crédito do piano) e agendamento.
- [x] **Shorts de GTA, parte 1:** 3 Shorts entregues (ver `projetos/gta-shorts-01/`). Mandar as próximas partes quando houver.
- [ ] Completar o `manifestos/fire-grace.md` com o usuário (8 perguntas no fim do arquivo).
- [ ] Montar uma **biblioteca de efeitos sonoros com dicionário** (CC0, ex.: Freesound pelo `sfx-source.py` do video-shotcraft) para GTA e FIRE & GRACE.
- [x] Prints do Studio recebidos (21/11): **os dois canais ainda sem dados de horário**. Mantido o padrão do usuário. Rever em dezembro.
- [ ] Testar o react-three-rapier, o react-postprocessing e o video-shotcraft num projeto real.
- [x] Ambiente da nuvem **fluxo-de-edicao** criado com o script de instalação e o Google Drive liberado (aprovado pelo notebook em 21/11). Confirmar na próxima sessão nova que o script rodou sozinho.
- [x] Levar tudo para o `main` (PR #1, mesclado em 21/11).
- [x] Clipe "NO DESERTO, ELE VENCEU": agendado 27–29/11 (ver registro de 27/11).
- [ ] Conferir a publicação do clipe e dos Shorts (miniatura, vídeo relacionado, visibilidade).

## 27/11/2026: clipe "NO DESERTO, ELE VENCEU" (FIRE & GRACE)
- Música do Natan no Suno (plano pago, monetizável), 4min42. Imagem estática 16:9 dele com o título na arte. Projeto: `projetos/clipe-no-deserto/`.
- **Tempo de cada palavra:** transcrição ElevenLabs Scribe (2.585 créditos grátis; sobram ~4.800). A letra oficial que ele colou bateu 369/369 palavras com a transcrição → texto da letra + tempos da transcrição (`palavras_letra.json`).
- **Movimento:** câmera de cinema lenta (aproxima nos versos, abre nos refrões, nunca corta o título), sol que respira, raios no céu, poeira dourada com bokeh, pulso de luz na batida só no refrão, vinheta e grão.
- **Karaokê** em ASS (`\kf`), Cinzel peso 800 ("Cinzel Deserto"): a palavra enche de dourado só enquanto é cantada; um verso por linha, dois versos por vez, como na letra.
- **Sticker** Inscreva-se/Like 3x de 10 s (começo, meio, fim), no céu à esquerda. -14 LUFS.
- Vídeo de 410 MB passou do limite de envio (400 MB) → cópia CRF 20 para mandar.
- Próximo: o usuário aprova → 3 Shorts 9:16 de até 35 s (refrão, verso 2, ponte) e publicação pelo manifesto (título com **VENCEU**, a tag do Suno diz "VENDEU").
- **27/11 (tarde):** o usuário mandou o **sticker do canal** (CapCut, fundo verde, logo do leão) → recortado e com o nome
  "FIRE & GRACE" reescrito inteiro (`ferramentas/sticker-fire-grace/`). Mandou um modelo do CapCut ("Back to HOME") para
  aprender **só a animação do título** → `ferramentas/titulo_animado.py`. Mandou a **imagem sem título** → título agora
  aparece no meio, sobe e fica fixo no céu. Prévia aprovada: **"Ficou muito bom, excelente trabalho"**. Clipe completo:
  aguardando o usuário liberar a geração.
- 3 vídeos de referência (Reels) analisados → técnicas guardadas como **opção** (guia seção 16), não viram padrão.
- ★ **27/11, 19h16 — "NO DESERTO, ELE VENCEU" agendado no Metricool (aprovado: "Pode sim"):**
  | Quando | Post Metricool | Vídeo |
  |---|---|---|
  | 27/11 19h40 | 444926552 | Clipe 16:9 4:42 (qualidade máxima, 552 MB), categoria Música, IA = sim |
  | 27/11 20h00 | 444927337 | Short 1 refrão final (33 s) |
  | 28/11 20h00 | 444927491 | Short 2 subida até o refrão (33 s) |
  | 29/11 20h00 | 444927681 | Short 3 ponte (34,5 s) |
  Arquivos pelo `vidiq_video_upload` (localFile, grátis). Tags 500 caracteres + 15 hashtags em cada. Shorts com o
  encerramento oficial (logo agora com o nome inteiro). **Pendente com o usuário:** miniatura do longo (`capa.png`) no Studio,
  "Vídeo relacionado" dos Shorts = o longo, comentário fixado, conferir a Visibilidade depois das 20h.
- ✅ **Publicados 27/11:** clipe longo https://www.youtube.com/watch?v=_LwvZMhdWgc (19h40) e Short 1 https://www.youtube.com/shorts/q3eh6noTDOM (20h; ficou alguns minutos em "publicando" no Metricool — normal, é o envio ao YouTube). Usuário conferiu.


## 28/11/2026: 5 Shorts de GTA com as técnicas do canal Desbugando
- Analisado o canal **Desbugando** (monetizado; 709 mil views no melhor Short) → manifesto GTA. Limite do usuário: **até 40 s**.
- Gameplay de 2h52 analisada (som + movimento + detecção de cutscene). 5 Shorts: 2 mini-listas ("3 coisas…", com número gigante
  e som de impacto) + 3 de ação (assalto com cutscene, fuga, tiroteio). Projeto: `projetos/gta-assalto-listas/`.
- Narração do Suno: o modo **Discurso** sempre vem com música → voltamos ao modo Música a cappella (funcionou).
- Gastos grátis: vidIQ 21 créditos (sobram ~131), ElevenLabs 1.127 créditos (sobram ~3.700).
- Pendente: aprovação do usuário → títulos, descrição, tags e agendamento (vidIQ, 20h, um por dia, máx. 3 envios/dia).
