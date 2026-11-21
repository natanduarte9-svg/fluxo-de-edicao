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

As instalações não sobrevivem ao fim de uma sessão na nuvem. Para refazer:

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
