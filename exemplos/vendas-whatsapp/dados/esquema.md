# Esquema de `dados/execucoes.csv`

Uma linha por proposta enviada. Vírgula, UTF-8, datas `AAAA-MM-DD`, sim/não exatamente `sim`/`não`.

| coluna | tipo | obrigatória | definição |
|---|---|---|---|
| `id` | texto | sim | `P0001`, `P0002`… |
| `data` | AAAA-MM-DD | sim | data do envio |
| `versao` | `v1`, `v2`… | sim | versão do roteiro usada |
| `variante` | `A` \| `B` | sim | `A` = atual; `B` = candidata em teste; fora de experimento, `A` |
| `segmento` | `pequeno` \| `medio` \| `grande` | não | valor do pacote: <R$1.500 / 1.500–4.000 / >4.000 |
| `resposta` | sim/não | sim | **sinal** — cliente respondeu em 48h com algo que não seja recusa |
| `resultado` | sim/não | sim | **alvo** — virou pacote pago em até 15 dias |
| `margem` | número 0–1 | sim | margem do pacote fechado (vazio se não fechou) |
| `reclamou` | sim/não | sim | cliente reclamou da abordagem |
| `optout` | sim/não | sim | cliente pediu para não receber mais mensagens |
| `custo` | número | não | custo de IA + envio (R$) |
| `tempo_min` | número | não | minutos até enviar |
| `nota_humana` | 0/1 | não | usado só em `calibracao.csv` |
| `observacao` | texto | não | livre |

Observador confere: `id` único; `versao` existe em `versoes/`; obrigatórias preenchidas.
