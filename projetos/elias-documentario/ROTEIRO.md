# Documentário: a vida do profeta Elias (Short 9:16, FIRE & GRACE)

Feito a partir do **prompt mestre do usuário** (23/11/2026) e das **6 imagens** dele (`img/` não vai para o Git; ficam em `/home/user/elias-doc/img`).
Decisões do usuário: **texto da narração inteiro, sem acelerar (~96 s)**; canal **FIRE & GRACE**.

## Linha do tempo (gerada por `linha.py` a partir do tempo real de cada palavra)
| Cena | Tempo | Imagem | Câmera | Título / referência |
|---|---|---|---|---|
| 1 | 0,0–10,8 | Elias diante de Acabe | aproximação lenta até Elias + poeira na luz | ELIAS: UM PROFETA DE CORAGEM · 1 Reis 17:1 |
| 2 | 10,8–22,6 | Ribeiro de Querite, corvos | abre revelando riacho e corvos; água correndo, névoa | DEUS CUIDA DOS SEUS · 1 Reis 17:2–7 |
| 3 | 22,6–40,6 | Fogo no monte Carmelo | aproxima do altar; fogo cintila e "respira"; brasas; **impacto 1** em "fogo" (32,1 s): tremor curto, brilho, tímpanos e trompas | O FOGO DO SENHOR CAIU! · 1 Reis 18:20–39 |
| 4 | 40,6–53,9 | Anjo alimenta Elias | aproximação delicada com deriva lateral; poeira na luz | DEUS TAMBÉM CUIDA DE QUEM ESTÁ CANSADO · 1 Reis 19:1–8 |
| 5 | 53,9–65,7 | Manto sobre Eliseu | movimento lateral até o manto | UMA MISSÃO QUE CONTINUA · 1 Reis 19:19–21 |
| 6 | 65,7–81,6 | Redemoinho e carruagem de fogo | afasta revelando o céu; **impacto 2** em "redemoinho" (72,7 s): brilho e orquestra cheia | UMA HISTÓRIA EXTRAORDINÁRIA DE FÉ · 2 Reis 2:1–12 |
| 7 | 81,6–96,1 | Mesma imagem, escurecida e desfocada | leve afastamento final | QUAL HISTÓRIA VOCÊ QUER VER AQUI? + COMENTE / DEIXE SEU LIKE / INSCREVA-SE (cada botão entra na palavra falada) + sticker "Inscreva-se" na palavra "inscrever" |

- Transições: dissolve de 0,9 s; luz quente que "vira" a cena seguinte em 3→4 e 5→6. Fade final.
- Legendas: Montserrat ExtraBold, branco com contorno, palavras-chave em dourado, 1–3 palavras, sincronizadas pelo tempo exato de cada palavra (edge-tts). Títulos em Cinzel; referência em dourado.

## Som
- Voz: Antonio (Microsoft edge-tts), ritmo natural.
- Trilha original com instrumentos reais gravados (piano Salamander, orquestra VSCO 2 CE/VCSL): ré menor → cresce até o fogo (silêncio de 0,75 s antes) → delicada no deserto → esperança (fá maior) → grandiosa na subida (ré maior) → suave no convite.
- Ducking: trilha a ~15% da voz durante a fala (pedido: 10–18%); sobe nos intervalos.
- Ambiente bem baixo: riacho (cena 2), rugido do fogo (cena 3), vento e fogo (cena 6).

## Precisão bíblica
Ordem e referências conferidas. Narração diz que Elias foi levado **pelo redemoinho** e que a carruagem **separou** Elias de Eliseu (2 Rs 2:11). A imagem 6 mostra Elias junto à carruagem; o texto falado segue a Bíblia.

## Como refazer
`python linha.py` (tempos) → `bash render_all.sh` (quadros) → `python musica.py` → `python mix.py` → ffmpeg (ver HISTORICO).

## Versão 2 (movimento real): prompts para o YouTube Create (foto para vídeo, vertical)
O usuário anexa a imagem da cena, cola o prompt e gera (grátis, Veo); manda os 6 clipes pelo Drive. Eu troco as fotos pelos clipes mantendo voz, trilha, legendas e títulos (e removo qualquer som). ★ **Limite do YouTube Create: 900 caracteres por prompt** → manter cada um entre 400 e 650. Ação principal primeiro ("Main movement"), depois "Also", câmera, proibições e "Silent video".

### Cena 1 (461 caracteres)
```
Animate this exact image. Keep the same faces, beards, clothes and background.
Main movement: the man in the red cloak keeps pointing at the king and speaks. His hair and cloak move gently in the wind.
Also: the king stays seated and frowns, the guards stand still, dust floats in the sunlight.
Camera: very slow zoom in toward the man in the red cloak.
No new people, no text. Silent video: no sound, no music, no voices.
Realistic, cinematic, slow and smooth.
```
### Cena 2 (417 caracteres)
```
Animate this exact image. Keep the same man, face, clothes, crows and landscape.
Main movement: the crows flap their wings and fly holding bread in their beaks. The stream water flows over the rocks.
Also: light mist moves slowly. The man stays seated, looking up, with open hands.
Camera: very slow zoom out.
No new people, no text. Silent video: no sound, no music, no voices.
Realistic, cinematic, slow and smooth.
```
### Cena 3 (469 caracteres)
```
Animate this exact image. Keep the same man, cloak, altar, people and sky.
Main movement: the big fire on the altar burns strongly and rises upward. Sparks and embers fly up.
Also: smoke turns slowly in the dark sky, the water around the altar steams. The man keeps both arms raised. The people in the back stay bowed.
Camera: very slow zoom in toward the fire.
No new people, no text. Silent video: no sound, no music, no voices.
Realistic, cinematic, slow and smooth.
```
### Cena 4 (434 caracteres)
```
Animate this exact image. Keep the same two people, faces, clothes, tree and desert.
Main movement: the young man in white gently holds out the bread and the clay jar. The old man slowly lifts his hand to receive it.
Also: the tree branches move softly in the wind, dust floats in the warm sunlight.
Camera: very slow zoom in.
No new people, no text. Silent video: no sound, no music, no voices.
Realistic, cinematic, slow and smooth.
```
### Cena 5 (442 caracteres)
```
Animate this exact image. Keep the same two men, faces, clothes, red cloak, oxen and field.
Main movement: the older man gently places the red cloak on the young man's shoulders. The young man looks at him, surprised.
Also: the oxen move their heads a little, dust moves softly over the field.
Camera: very slow movement to the right.
No new people, no text. Silent video: no sound, no music, no voices.
Realistic, cinematic, slow and smooth.
```
### Cena 6 (607 caracteres)
```
Animate this exact image. Keep the same faces, clothes, fire horses, chariot and sky.
Main movement: the fire horses gallop through the air and pull the fire chariot up into the sky. The man in the red cloak rides the chariot and flies up with it into the whirlwind, getting smaller as they rise into the clouds.
Also: the whirlwind spins, flames move on the horses, the red cloak waves, sparks fly.
The young man stays on the ground, looking up with raised hands.
Camera: slow tilt up following the chariot.
No new people, no text. Silent video: no sound, no music, no voices.
Realistic, cinematic, smooth.
```
