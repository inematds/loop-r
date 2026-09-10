# Evidência — ciclo 0003

Dados consistentes: 0 ids duplicados, 0 obrigatórias vazias, 0 datas inválidas, `margem` presente sse `resultado=sim`, todos os valores sim/não válidos, `versao=v1` existe em `versoes/`.

## (a) Linhas novas desde 2026-04-27 (só v1/A)

Não coberto por `ciclos/0002/evidencia.md` (que ia até 2026-04-26).

| corte | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1/A, 2026-04-27→2026-05-03 | 50 | 3 | 6,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | 0,3233 (N=3) | 0,9702 | 5,660 |

Todas as 50 linhas novas são `v1`/`A` (sem outras versões/variantes no período).

## (b) Totais por versão × variante — todo o período, com período de E0001 separado

`versao` = v1 em 100% das 850 linhas. `variante` B só existe dentro da janela de E0001.

| período | versão | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pré-E0001 (2026-01-05→2026-02-01) | v1 | A | 200 | 5 | 2,50% | 34 | 17,00% | 1 | 0,50% | 2 | 1,00% | 0,3200 (N=5) | 1,0283 | 5,465 |
| E0001 (2026-02-02→2026-04-26) | v1 | A | 300 | 15 | 5,00% | 58 | 19,33% | 1 | 0,33% | 0 | 0,00% | 0,3127 (N=15) | 1,0066 | 5,437 |
| E0001 (2026-02-02→2026-04-26) | v1 | B | 300 | 14 | 4,67% | 89 | 29,67% | 6 | 2,00% | 1 | 0,33% | 0,3107 (N=14) | 0,9907 | 5,537 |
| pós-E0001 (2026-04-27→2026-05-03) | v1 | A | 50 | 3 | 6,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | 0,3233 (N=3) | 0,9702 | 5,660 |

Consolidado (todo o período, sem separar por janela):

| versão | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | A | 550 | 23 | 4,18% | 101 | 18,36% | 2 | 0,36% | 2 | 0,36% | 0,3157 (N=23) | 1,0112 | 5,467 |
| v1 | B | 300 | 14 | 4,67% | 89 | 29,67% | 6 | 2,00% | 1 | 0,33% | 0,3107 (N=14) | 0,9907 | 5,537 |

v1/A em todo o período (pré + E0001 + pós, excluindo B) — linha de base atual: N=550, resultado 4,18%, resposta 18,36%, reclamou 0,36%, optout 0,36%.

## (c) Segmentos com N ≥ 30

### Todo o período (todas as variantes)

| segmento | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pequeno | 378 | 14 | 3,70% | 96 | 25,40% | 2 | 0,53% | 3 | 0,79% | 0,3079 (N=14) | 1,0019 | 5,447 |
| medio | 351 | 18 | 5,13% | 77 | 21,94% | 5 | 1,42% | 0 | 0,00% | 0,3206 (N=18) | 1,0194 | 5,527 |
| grande | 121 | 5 | 4,13% | 17 | 14,05% | 1 | 0,83% | 0 | 0,00% | 0,3060 (N=5) | 0,9654 | 5,529 |

### Por período × segmento (N ≥ 30)

| período | segmento | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pré-E0001 | grande | 30 | 1 | 3,33% | 6 | 20,00% | 0 | 0,00% | 0 | 0,00% | 0,3500 (N=1) | 1,0043 | 5,767 |
| pré-E0001 | medio | 78 | 1 | 1,28% | 8 | 10,26% | 0 | 0,00% | 0 | 0,00% | 0,3200 (N=1) | 1,0472 | 5,577 |
| pré-E0001 | pequeno | 92 | 3 | 3,26% | 20 | 21,74% | 1 | 1,09% | 2 | 2,17% | 0,3100 (N=3) | 1,0201 | 5,272 |
| E0001 | grande | 84 | 3 | 3,57% | 9 | 10,71% | 1 | 1,19% | 0 | 0,00% | 0,2967 (N=3) | 0,9646 | 5,488 |
| E0001 | medio | 250 | 15 | 6,00% | 64 | 25,60% | 5 | 2,00% | 0 | 0,00% | 0,3180 (N=15) | 1,0098 | 5,472 |
| E0001 | pequeno | 266 | 11 | 4,14% | 74 | 27,82% | 1 | 0,38% | 1 | 0,38% | 0,3073 (N=11) | 0,9989 | 5,500 |
| pós-E0001 | grande | — | abaixo do N mínimo (N=7) | | | | | | | | | | |
| pós-E0001 | medio | — | abaixo do N mínimo (N=23) | | | | | | | | | | |
| pós-E0001 | pequeno | — | abaixo do N mínimo (N=20) | | | | | | | | | | |

### Segmento × variante dentro de E0001 (N ≥ 30)

| segmento | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| grande | A | 39 | 1 | 2,56% | 3 | 7,69% | 0 | 0,00% | 0 | 0,00% | 0,3100 (N=1) | 0,9754 | 5,282 |
| grande | B | 45 | 2 | 4,44% | 6 | 13,33% | 1 | 2,22% | 0 | 0,00% | 0,2900 (N=2) | 0,9553 | 5,667 |
| medio | A | 128 | 7 | 5,47% | 23 | 17,97% | 1 | 0,78% | 0 | 0,00% | 0,3214 (N=7) | 1,0249 | 5,383 |
| medio | B | 122 | 8 | 6,56% | 41 | 33,61% | 4 | 3,28% | 0 | 0,00% | 0,3150 (N=8) | 0,9939 | 5,566 |
| pequeno | A | 133 | 7 | 5,26% | 32 | 24,06% | 0 | 0,00% | 0 | 0,00% | 0,3043 (N=7) | 0,9980 | 5,534 |
| pequeno | B | 133 | 4 | 3,01% | 42 | 31,58% | 1 | 0,75% | 1 | 0,75% | 0,3125 (N=4) | 0,9997 | 5,466 |

Linhas novas (data ≥ 2026-04-27), por segmento — todas abaixo de N=30: grande N=7, medio N=23, pequeno N=20.

## Experimento em andamento

Nenhum. E0001 encerrado no ciclo 0002 (veredito `A_SEGUE`, `ciclos/0002/veredito.md`). Nenhuma linha com variante B no período pós-2026-04-26.

Linhas lidas: 850 · Período: 2026-01-05 → 2026-05-03
