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

### Contas e saldos (21/11/2026)
- **OpusClip:** plano de teste, **90 minutos** de processamento (~1 min de saldo por minuto de vídeo). Aceita link do Google Drive e pode limitar o trecho (`rangeStart`/`rangeEnd`). No teste, os cortes podem sair com marca d'água.
- **vidIQ:** 2 créditos (150 renovam em 27/11).
- **ElevenLabs:** plano grátis, sem geração de vídeo.

### Pendências
- [ ] **27/11, 19h:** gerar o vídeo do Elias (reanexar a imagem e confirmar o custo).
- [x] **Shorts de GTA, parte 1:** 3 Shorts entregues (ver `projetos/gta-shorts-01/`). Mandar as próximas partes quando houver.
- [ ] Completar o `manifestos/fire-grace.md` com o usuário (8 perguntas no fim do arquivo).
- [ ] Montar uma **biblioteca de efeitos sonoros com dicionário** (CC0, ex.: Freesound pelo `sfx-source.py` do video-shotcraft) para GTA e FIRE & GRACE.
- [x] Prints do Studio recebidos (21/11): **os dois canais ainda sem dados de horário**. Mantido o padrão do usuário. Rever em dezembro.
- [ ] Testar o react-three-rapier, o react-postprocessing e o video-shotcraft num projeto real.
- [x] Ambiente da nuvem **fluxo-de-edicao** criado com o script de instalação e o Google Drive liberado (aprovado pelo notebook em 21/11). Confirmar na próxima sessão nova que o script rodou sozinho.
- [x] Levar tudo para o `main` (PR #1, mesclado em 21/11).
