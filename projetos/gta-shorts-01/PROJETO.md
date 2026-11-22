# Shorts de GTA 6: parte 1 (21/11/2026)

**Fonte:** trecho de gameplay já editado no CapCut (4:45, 720×1280 vertical, fundo desfocado em cima e embaixo, legendas), baixado do Google Drive (link "qualquer pessoa com o link").

## Shorts entregues
| Arquivo | Trecho | Duração | Título (topo) |
|---|---|---|---|
| `short1-ponte.mp4` | 1:08–1:32 | 24 s | OS CARROS VOARAM / DA PONTE! |
| `short2-fuga.mp4` | 2:52–3:18 | 26 s | ELE NÃO ESPERAVA / POR ISSO... |
| `short3-cais.mp4` | 3:58–4:28 | 30 s | ACERTO DE CONTAS / NO CAIS |

## Versão juntada (pedido do usuário)
| `short-fuga-cais.mp4` | 2:52–3:18 + 3:58–4:38 | 1:06 | ELE NÃO ESPERAVA / POR ISSO... |

- Termina **1,5 s depois do tiro** no rapaz ajoelhado (tiro em 4:36,4 no original, achado pelo pico de som + quadros a cada 0,25 s), para dar tempo de ver a queda.
- Junção com fade de 0,3 s na imagem e no som (`xfade` + `acrossfade`).
- Com 1:06 passa de 1 minuto. O YouTube aceita Shorts de até 3 minutos, mas o ideal é até 60 s.

## Sticker "Inscreva-se" (pedido do usuário)
`short-fuga-cais-sticker.mp4`: sticker animado (cartão branco, joinha, botão vermelho INSCREVA-SE → clique → INSCRITO, sino balança), **5,6 s na tela (pedido do usuário: no mínimo 5 s)**, aos **0:04** e **0:40**. Fica no topo (overlay em x=160, y=110), acima do título. Gerado por `ferramentas/sticker-inscreva.py` (Pillow, PNGs com transparência a 30 fps).

## Como foi feito (`make.sh`)
- Escolha dos momentos: folha de contato a cada 5 s no vídeo todo, depois a cada 1 s nos candidatos.
- 1080×1920, 30 fps, H.264 CRF 18; **som do jogo** (sem música), dois passes de `loudnorm` para −14 LUFS, fade de 0,1 s na entrada e 0,5 s na saída.
- Título em duas linhas na faixa desfocada de cima, **abaixo do sticker de "se inscrever"** (linhas em y=410 e y=515 em 1080×1920; o sticker do CapCut fica em y≈180–375). **O sticker do canal nunca pode ser coberto** (pedido do usuário) (Inter Display Black, branco + amarelo, contorno preto), entrando com um pulo nos primeiros 0,25 s.
- Revisão: −14,0/−14,1 LUFS, nenhum quadro preto.

Uso: `SRC=<fonte> ./make.sh <saída.mp4> <início_s> <fim_s> "LINHA 1" "LINHA 2"` (com `parte-drive.mp4` na mesma pasta).

## Textos para publicar (22/11/2026)

### Short 1: ponte (`short1-ponte.mp4`)
- **Título:** OS CARROS VOARAM DA PONTE no GTA 6 😱 #shorts
- **Descrição:**
  > Eu só queria atravessar a ponte... e os carros saíram VOANDO! 😱🚗
  > A física do GTA 6 está insana: olha a altura que esses carros foram parar.
  > 👉 Inscreva-se e ative o sininho para mais momentos insanos de GTA 6!
  > #GTA6 #GTAVI #GTA6Brasil #Shorts #Gameplay #ViceCity #RockstarGames
- **Tags (397 caracteres):** gta 6, gta vi, gta 6 gameplay, gta 6 brasil, gta 6 pt br, gta 6 ponte, carros voando gta 6, gta 6 física, gta 6 momentos insanos, gta 6 cenas épicas, gta 6 shorts, gta 6 leonida, gta 6 vice city, grand theft auto 6, grand theft auto vi, rockstar games, gta 6 perseguição, gta 6 acidente, gta 6 legendado, gameplay gta 6 português, melhores momentos gta 6, gta 6 explosão, jogos 2026, gta 6 dublado

### Short 2: fuga + cais (`short-fuga-cais-sticker.mp4`)
- **Título:** ELE NÃO ESPERAVA POR ISSO... 😳 Acerto de contas no GTA 6 #shorts
- **Descrição:**
  > Primeiro a fuga... depois o acerto de contas no cais. Ele não esperava por esse final! 😳🔫
  > Uma das cenas mais pesadas do GTA 6 até agora.
  > 👉 Inscreva-se e ative o sininho para mais cenas de GTA 6!
  > #GTA6 #GTAVI #GTA6Brasil #Shorts #Gameplay #ViceCity #RockstarGames
- **Tags (385 caracteres):** gta 6, gta vi, gta 6 gameplay, gta 6 brasil, gta 6 pt br, gta 6 missão, gta 6 cena final, gta 6 acerto de contas, gta 6 traição, gta 6 cais, gta 6 fuga, gta 6 perseguição, gta 6 cutscene, gta 6 história, gta 6 shorts, gta 6 leonida, gta 6 vice city, grand theft auto 6, grand theft auto vi, rockstar games, gta 6 legendado, gameplay gta 6 português, melhores momentos gta 6, jogos 2026
