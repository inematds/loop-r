# Esquema de `dados/execucoes.csv`

Uma linha por execução do processo. Separador vírgula, codificação UTF-8, cabeçalho na 1ª linha. Datas `AAAA-MM-DD`. Sim/não escritos exatamente `sim` / `não`.

| coluna | tipo | obrigatória | definição |
|---|---|---|---|
| `id` | texto | sim | identificador único da execução (ex.: `P0001`) |
| `data` | AAAA-MM-DD | sim | data da execução |
| `versao` | `v1`, `v2`… | sim | versão do roteiro do Executor usada |
| `variante` | `A` \| `B` | sim | `A` = versão atual; `B` = candidata em teste. Fora de experimento, `A` |
| `experimento` | texto | sim quando `variante=B` | id do experimento (`E0001`, `E0002`…). Sem isto, linhas `B` de testes diferentes se misturam (achado do exemplo, ciclo 0004) |
| `segmento` | texto | não | recorte útil (porte, canal, origem…) — só é analisado com N ≥ `n_minimo_para_padrao` |
| `{{COLUNA_SINAL}}` | `sim` \| `não` | sim | **métrica de sinal** — `{{DEF_SINAL}}` |
| `{{COLUNA_ALVO}}` | `sim` \| `não` | sim | **métrica-alvo** — `{{DEF_ALVO}}` |
| `{{COLUNAS_SEM_PIORAR}}` | número ou sim/não | sim | uma coluna por item de `sem_piorar` |
| `custo` | número | não | custo direto da execução |
| `tempo_min` | número | não | minutos gastos |
| `nota_humana` | `0` \| `1` | não | avaliação da pessoa (usada em `calibracao.csv`) |
| `observacao` | texto | não | livre; o Executor grava `INVARIÁVEL BLOQUEOU: …` aqui quando for o caso |

Regras que o Observador confere: sem `id` duplicado; `versao` existe em `versoes/`; nenhuma coluna obrigatória vazia (exceto resultados ainda não conhecidos, que ficam vazios até o mundo responder).
