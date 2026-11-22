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
- ★ **Só o som do jogo, sem música** (pedido do usuário).
- Volume padrão do YouTube: **−14 LUFS**, pico −1,5 dB. Fade curto na entrada (0,1 s) e na saída (0,5 s).

## Transições
- Ao juntar trechos: fade de 0,3 s na imagem e no som.

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

## Entrega
- MP4 H.264 + AAC, sem marca d'água, mandado pelo chat.
- Ferramenta: `ferramentas/short-gameplay.sh`.

## Ainda não sabemos (perguntar quando surgir)
- Thumbnail/capa: estilo preferido.
- Título e descrição para o YouTube: tom e hashtags que o usuário usa.
- Vídeos longos: se terão música, narração, intro/outro.
