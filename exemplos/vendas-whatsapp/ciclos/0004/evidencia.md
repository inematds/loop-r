# Evidência — ciclo 0004

Dados consistentes: 0 ids duplicados, 0 obrigatórias vazias, 0 datas inválidas, `margem` presente sse `resultado=sim`, todos os valores sim/não válidos, `versao` existe em `versoes/`, `variante` ∈ {A,B}. Total de linhas no CSV: 1450 (era 850 em `ciclos/0003/evidencia.md`).

## (a) Linhas novas desde 2026-05-04 (não cobertas por `ciclos/0003/evidencia.md`, que ia até 2026-05-03)

600 linhas novas, todas dentro da janela do experimento E0002 (`versao=v1`, variante A ou B).

| corte | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1/A, 2026-05-04→2026-07-26 | 300 | 9 | 3,00% | 58 | 19,33% | 2 | 0,67% | 3 | 1,00% | 0,3178 (N=9) | 1,0028 | 5,380 |
| v1/B, 2026-05-04→2026-07-26 | 300 | 11 | 3,67% | 88 | 29,33% | 4 | 1,33% | 1 | 0,33% | 0,3245 (N=11) | 0,9821 | 5,550 |

## (b) Experimento E0002 — N acumulado vs. amostra mínima

Amostra mínima: 212/variante (`ciclos/0003/experimento.md`). Em andamento desde 2026-05-04.

| variante | N acumulado | mínimo | atingiu mínimo? |
|---|---|---|---|
| A | 300 | 212 | sim (+88) |
| B | 300 | 212 | sim (+88) |

### Todas as métricas por variante, só período do experimento (data ≥ 2026-05-04)

| variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 300 | 9 | 3,00% | 58 | 19,33% | 2 | 0,67% | 3 | 1,00% | 0,3178 (N=9) | 1,0028 | 5,380 |
| B | 300 | 11 | 3,67% | 88 | 29,33% | 4 | 1,33% | 1 | 0,33% | 0,3245 (N=11) | 0,9821 | 5,550 |

Diferença B−A (só como contagem, sem interpretação): resultado +0,67pp · resposta +10,00pp · reclamou +0,67pp · optout −0,67pp · margem +0,0067 · custo −0,0207 · tempo +0,170min.

## (c) Totais por versão × variante — todo o período, com janela do experimento separada

`versao` = v1 em 100% das 1450 linhas.

| período | versão | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pré-E0002 (2026-01-05→2026-05-03) | v1 | A | 550 | 23 | 4,18% | 101 | 18,36% | 2 | 0,36% | 2 | 0,36% | 0,3157 (N=23) | 1,0112 | 5,467 |
| E0002 (2026-05-04→2026-07-26) | v1 | A | 300 | 9 | 3,00% | 58 | 19,33% | 2 | 0,67% | 3 | 1,00% | 0,3178 (N=9) | 1,0028 | 5,380 |
| E0002 (2026-05-04→2026-07-26) | v1 | B | 300 | 11 | 3,67% | 88 | 29,33% | 4 | 1,33% | 1 | 0,33% | 0,3245 (N=11) | 0,9821 | 5,550 |

Nenhuma linha `variante=B` fora da janela do experimento.

### Consolidado (todo o período, sem separar por janela)

| versão | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | A | 850 | 32 | 3,76% | 159 | 18,71% | 4 | 0,47% | 5 | 0,59% | 0,3163 (N=32) | 1,0082 | 5,437 |
| v1 | B | 600 | 25 | 4,17% | 177 | 29,50% | 10 | 1,67% | 2 | 0,33% | 0,3168 (N=25) | 0,9864 | 5,543 |

## (d) Segmentos com N ≥ 30

### Todo o período, todas as variantes juntas

| segmento | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| grande | 214 | 7 | 3,27% | 35 | 16,36% | 1 | 0,47% | 2 | 0,93% | 0,3114 (N=7) | 0,9779 | 5,439 |
| medio | 603 | 27 | 4,48% | 141 | 23,38% | 6 | 1,00% | 1 | 0,17% | 0,3196 (N=27) | 1,0099 | 5,551 |
| pequeno | 633 | 23 | 3,63% | 160 | 25,28% | 7 | 1,11% | 4 | 0,63% | 0,3143 (N=23) | 0,9961 | 5,428 |

### Segmento × variante, todo o período (N ≥ 30)

| segmento | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| grande | A | 119 | 5 | 4,20% | 20 | 16,81% | 0 | 0,00% | 2 | 1,68% | 0,3200 (N=5) | 0,9949 | 5,378 |
| grande | B | 95 | 2 | 2,11% | 15 | 15,79% | 1 | 1,05% | 0 | 0,00% | 0,2900 (N=2) | 0,9567 | 5,516 |
| medio | A | 359 | 14 | 3,90% | 61 | 16,99% | 2 | 0,56% | 1 | 0,28% | 0,3229 (N=14) | 1,0187 | 5,496 |
| medio | B | 244 | 13 | 5,33% | 80 | 32,79% | 4 | 1,64% | 0 | 0,00% | 0,3162 (N=13) | 0,9970 | 5,631 |
| pequeno | A | 372 | 13 | 3,49% | 78 | 20,97% | 2 | 0,54% | 2 | 0,54% | 0,3077 (N=13) | 1,0024 | 5,398 |
| pequeno | B | 261 | 10 | 3,83% | 82 | 31,42% | 5 | 1,92% | 2 | 0,77% | 0,3230 (N=10) | 0,9872 | 5,471 |

### Segmento × variante, só período do experimento (data ≥ 2026-05-04, N ≥ 30)

| segmento | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| grande | A | 43 | 2 | 4,65% | 9 | 20,93% | 0 | 0,00% | 2 | 4,65% | 0,3250 (N=2) | 1,0365 | 5,256 |
| grande | B | 50 | 0 | 0,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | — (N=0) | 0,9580 | 5,380 |
| medio | A | 130 | 4 | 3,08% | 25 | 19,23% | 1 | 0,77% | 1 | 0,77% | 0,3175 (N=4) | 0,9935 | 5,477 |
| medio | B | 122 | 5 | 4,10% | 39 | 31,97% | 0 | 0,00% | 0 | 0,00% | 0,3180 (N=5) | 1,0001 | 5,697 |
| pequeno | A | 127 | 3 | 2,36% | 24 | 18,90% | 1 | 0,79% | 0 | 0,00% | 0,3133 (N=3) | 1,0009 | 5,323 |
| pequeno | B | 128 | 6 | 4,69% | 40 | 31,25% | 4 | 3,12% | 1 | 0,78% | 0,3300 (N=6) | 0,9743 | 5,477 |

### Semana ISO × segmento

Nenhuma combinação semana×segmento isolada atinge N ≥ 30 (volume semanal ≈ 50 linhas dividido entre 3 segmentos e, na janela do experimento, entre 2 variantes) — abaixo do N mínimo em todas.

Linhas lidas: 1450 · Período: 2026-01-05 → 2026-07-26
