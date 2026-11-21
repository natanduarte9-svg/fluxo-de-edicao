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
| `projetos/<nome>/` | Projetos de vídeo em andamento (ex.: `elias-altar-fogo`) |
| `scripts/setup-ambiente.sh` | Reinstala todas as ferramentas |
| `SKILL.md` (raiz) | A skill original `/fluxo-de-edicao` (montar o fluxo de edição) |

**No início da sessão, leia as pendências em `HISTORICO.md`** e lembre a pessoa do que estiver em aberto.

## Regras que não mudam
- **Movimento real** (pessoa, fogo, tecido realistas) = IA de vídeo (vidIQ). **Acabamento** (som, títulos, ritmo, efeitos) = código.
- **Nunca gaste créditos** (vidIQ, ElevenLabs etc.) sem mostrar o custo e esperar o "sim". Nunca gere duas vezes por engano.
- Nada é publicado em rede social sem confirmação.
- Ao terminar um trabalho, **registre no `HISTORICO.md`**, faça commit e envie. Aprendizado novo que vale para todo vídeo vai para o `GUIA-PRODUCAO.md`.
