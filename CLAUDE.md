# Memória do projeto (leia no início de toda sessão)

Converse em **português**, com frases curtas e sem jargão.

## Palavra-mestra de produção: `/produzir-video`
Para **qualquer pedido de vídeo, Short ou clipe** (FIRE & GRACE, GTA 6 ou outro), use a skill **`/produzir-video`** (`skills/produzir-video/SKILL.md`). Ela conduz tudo: perguntas, escolha das ferramentas, roteiro, produção, revisão, entrega e registro no histórico.

Se o comando `/produzir-video` não aparecer na lista de skills, a sessão é nova e nada está instalado. Rode, a partir da pasta que contém o repositório:
```bash
bash fluxo-de-edicao/scripts/setup-ambiente.sh
```
Depois diga à pessoa para recarregar a sessão, se a skill ainda não aparecer.

## Onde está o que já foi aprendido
| Arquivo | O que tem |
|---|---|
| `GUIA-PRODUCAO.md` | As regras de produção (ritmo, som, câmera, o que evitar) e os repositórios de motion graphics |
| `HISTORICO.md` | Diário das sessões: decisões, problemas já resolvidos, preços, **pendências** |
| `manifestos/` | **O jeito de fazer vídeo de cada canal** (GTA, FIRE & GRACE). Ler antes de qualquer vídeo |
| `projetos/<nome>/` | Projetos de vídeo em andamento (ex.: `elias-altar-fogo`) |
| `scripts/setup-ambiente.sh` | Reinstala todas as ferramentas |
| `SKILL.md` (raiz) | A skill original `/fluxo-de-edicao` (montar o fluxo de edição) |

**No início da sessão, leia as pendências em `HISTORICO.md`** e lembre a pessoa do que estiver em aberto.

## Regras que não mudam
- ★ **Padrão profissional, sempre.** O objetivo é **monetizar os dois canais** (FIRE & GRACE e Jogatina Fácil). Todo vídeo usa **as melhores ferramentas que temos**, nunca o atalho mais simples:
  - **3D e câmera de cinema com three.js** + pós-processamento (brilho, profundidade de campo), em vez de animação 2D simples;
  - **estilos e método de diretor do lemo-opuscar** (roteiro antes, gancho em 3 s, plano marcante, 4+ movimentos de câmera, som em 3 camadas);
  - **movimento real por IA** (vidIQ: Veo/MiniMax/Seedance) quando a cena pede pessoa/fogo/tecido realistas;
  - **cortes na batida** (librosa), **efeitos e transições** de qualidade (pixelfx, video-shotcraft quando couber);
  - **voz natural** (ElevenLabs) quando houver narração para publicar;
  - **revisão quadro a quadro** antes de entregar.
  - Se a ferramenta melhor gastar créditos, **mostrar o custo e esperar o "sim"**; se não der para usar, dizer qual seria e por quê.
- ★ **Enquanto os canais não monetizam: só créditos/tokens grátis, nada pago.** Quando os créditos grátis de uma ferramenta acabarem, **trocar por outra de qualidade excelente que ainda tenha créditos grátis** (rodízio). Antes de gerar, **conferir o saldo** de cada uma. A tabela de rodízio está no `GUIA-PRODUCAO.md` (seção 10).
- **Movimento real** (pessoa, fogo, tecido realistas) = IA de vídeo (vidIQ). **Acabamento** (som, títulos, ritmo, efeitos) = código.
- **Nunca gaste créditos** (vidIQ, ElevenLabs etc.) sem mostrar o custo e esperar o "sim". Nunca gere duas vezes por engano.
- Nada é publicado em rede social sem confirmação.
- Ao terminar um trabalho, **registre no `HISTORICO.md`**, faça commit e envie. Aprendizado novo que vale para todo vídeo vai para o `GUIA-PRODUCAO.md`.
