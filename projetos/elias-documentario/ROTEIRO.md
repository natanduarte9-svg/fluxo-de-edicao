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
O usuário gera no celular (grátis, Veo) e manda pelo Drive; eu troco as fotos pelos clipes mantendo voz, trilha, legendas e títulos. Alternativa: vidIQ em 27/11 (172 créditos → cenas 3 e 6).
1. Elijah keeps pointing at the king and speaks firmly, his robe and long hair moving in a light warm wind. The king stays seated, frowning. Guards stand still holding spears. Dust floats in the sunlight. Slow cinematic push-in toward Elijah. Keep all faces, clothes and the setting identical. No text, no new people.
2. The crows flap their wings and fly carrying bread in their beaks. The stream flows and splashes over the rocks. Light mist drifts through the canyon. Elijah keeps looking up calmly with open hands. Slow camera pull-back. Keep Elijah's face and clothes identical. No text, no new people.
3. The fire keeps roaring and rising from the altar, sparks and embers fly upward, thick smoke swirls in the dark stormy sky, the water around the altar boils and steams. Elijah keeps both arms raised. The people in the background bow down to the ground. Slow push-in toward the altar. Keep Elijah identical. No text.
4. The angel gently offers the bread and the clay jar. Elijah slowly reaches out his hand. The tree branches sway softly in the wind. Warm sun rays and dust float in the air. Slow, gentle push-in. Keep both faces and clothes identical. No text, no new people.
5. Elijah settles his red mantle over Elisha's shoulders. Elisha looks at him, surprised. The oxen move their heads slowly. Dust blows softly over the plowed field. Slow lateral camera move to the right. Keep both faces and clothes identical. No text, no new people.
6. The whirlwind spins in the sky, the horses of fire gallop with flaming manes, the chariot wheels burn, Elijah's mantle blows in the wind. Elisha keeps looking up with raised hands. Sparks swirl around them. Slow camera pull-back revealing the sky. Keep both faces identical. No text.
