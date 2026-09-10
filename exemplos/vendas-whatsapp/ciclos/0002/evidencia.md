# Evidência — Ciclo 0002

## Consistência
OK. 800 linhas, colunas obrigatórias preenchidas, sem `id` duplicados, datas AAAA-MM-DD válidas, `versao` (v1) existe em `versoes/`, `variante` só `A`/`B`, valores sim/não válidos, `margem` preenchida sse `resultado=sim` e sempre em 0–1.

## Por versão × variante (todo o período)

| versão | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | A | 500 | 20 | 4,00% | 92 | 18,40% | 2 | 0,40% | 2 | 0,40% | 0,31 (N=20) | 1,0153 | 5,448 |
| v1 | B | 300 | 14 | 4,67% | 89 | 29,67% | 6 | 2,00% | 1 | 0,33% | 0,31 (N=14) | 0,9907 | 5,537 |

## Por versão × variante (linhas não cobertas por ciclo anterior — data > 2026-02-01)

| versão | variante | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | A | 300 | 15 | 5,00% | 58 | 19,33% | 1 | 0,33% | 0 | 0,00% | 0,31 (N=15) | 1,0066 | 5,437 |
| v1 | B | 300 | 14 | 4,67% | 89 | 29,67% | 6 | 2,00% | 1 | 0,33% | 0,31 (N=14) | 0,9907 | 5,537 |

Novas: 600 linhas (2026-02-02 → 2026-04-26). Ciclo 0001 já cobria até 2026-02-01 (200 linhas, todas variante A).

## Por segmento (N ≥ 30 — n_minimo_para_padrao), todo o período

| segmento | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pequeno | 358 | 14 | 3,91% | 94 | 26,26% | 2 | 0,56% | 3 | 0,84% | 0,31 (N=14) | 1,0043 | 5,441 |
| medio | 328 | 16 | 4,88% | 72 | 21,95% | 5 | 1,52% | 0 | 0,00% | 0,32 (N=16) | 1,0187 | 5,497 |
| grande | 114 | 4 | 3,51% | 15 | 13,16% | 1 | 0,88% | 0 | 0,00% | 0,31 (N=4) | 0,9751 | 5,561 |

## Por segmento (N ≥ 30), apenas linhas novas (data > 2026-02-01)

| segmento | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pequeno | 266 | 11 | 4,14% | 74 | 27,82% | 1 | 0,38% | 1 | 0,38% | 0,31 (N=11) | 0,9989 | 5,500 |
| medio | 250 | 15 | 6,00% | 64 | 25,60% | 5 | 2,00% | 0 | 0,00% | 0,32 (N=15) | 1,0098 | 5,472 |
| grande | 84 | 3 | 3,57% | 9 | 10,71% | 1 | 1,19% | 0 | 0,00% | 0,30 (N=3) | 0,9646 | 5,488 |

## Por semana ISO (N ≥ 30), todo o período

| semana | N | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-W02 | 50 | 0 | 0,00% | 7 | 14,00% | 0 | 0,00% | 0 | 0,00% | — (N=0) | 1,0644 | 5,020 |
| 2026-W03 | 50 | 0 | 0,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | — (N=0) | 1,0172 | 5,800 |
| 2026-W04 | 50 | 2 | 4,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | 0,30 (N=2) | 1,0350 | 5,380 |
| 2026-W05 | 50 | 3 | 6,00% | 9 | 18,00% | 1 | 2,00% | 2 | 4,00% | 0,33 (N=3) | 0,9966 | 5,660 |
| 2026-W06 | 50 | 2 | 4,00% | 13 | 26,00% | 1 | 2,00% | 0 | 0,00% | 0,34 (N=2) | 1,0720 | 5,400 |
| 2026-W07 | 50 | 2 | 4,00% | 14 | 28,00% | 1 | 2,00% | 0 | 0,00% | 0,32 (N=2) | 0,9528 | 5,120 |
| 2026-W08 | 50 | 7 | 14,00% | 20 | 40,00% | 1 | 2,00% | 0 | 0,00% | 0,31 (N=7) | 1,0026 | 5,380 |
| 2026-W09 | 50 | 1 | 2,00% | 9 | 18,00% | 1 | 2,00% | 0 | 0,00% | 0,29 (N=1) | 1,0538 | 5,300 |
| 2026-W10 | 50 | 1 | 2,00% | 16 | 32,00% | 1 | 2,00% | 0 | 0,00% | 0,31 (N=1) | 0,9996 | 5,360 |
| 2026-W11 | 50 | 3 | 6,00% | 10 | 20,00% | 1 | 2,00% | 0 | 0,00% | 0,30 (N=3) | 0,9882 | 5,200 |
| 2026-W12 | 50 | 1 | 2,00% | 12 | 24,00% | 0 | 0,00% | 0 | 0,00% | 0,36 (N=1) | 1,0034 | 5,720 |
| 2026-W13 | 50 | 1 | 2,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | 0,34 (N=1) | 0,9714 | 5,760 |
| 2026-W14 | 50 | 2 | 4,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | 0,30 (N=2) | 0,9940 | 5,780 |
| 2026-W15 | 50 | 2 | 4,00% | 13 | 26,00% | 1 | 2,00% | 0 | 0,00% | 0,29 (N=2) | 0,9920 | 5,460 |
| 2026-W16 | 50 | 3 | 6,00% | 12 | 24,00% | 0 | 0,00% | 1 | 2,00% | 0,32 (N=3) | 0,9964 | 5,720 |
| 2026-W17 | 50 | 4 | 8,00% | 10 | 20,00% | 0 | 0,00% | 0 | 0,00% | 0,31 (N=4) | 0,9572 | 5,640 |

Semanas novas (não cobertas por ciclo 0001): W06 a W17 (12 semanas, 600 linhas), todas com N=50 — reportadas na mesma tabela acima (idênticas às linhas "todo o período" para essas semanas, já que W02–W05 são as únicas do ciclo anterior).

## Por segmento × semana ISO

Todas as combinações abaixo do N mínimo (n_minimo_para_padrao=30) em todo o período — máximo observado: 27 (pequeno, W02 e W16). Nenhuma reportável individualmente (48 combinações no total, incluindo as 12 novas semanas × 3 segmentos).

## Experimento em andamento (E0001, `ciclos/0001/experimento.md`)

Variante A = `versoes/atual` (v1) · Variante B = `versoes/candidata-vB` · Amostra mínima: 166/variante · Início: 2026-02-02.

| variante | N acumulado (desde 2026-02-02) | mínimo exigido | atingiu mínimo? | resultado (sim) | resultado % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 300 | 166 | sim | 15 | 5,00% | 58 | 19,33% | 1 | 0,33% | 0 | 0,00% | 0,3127 (N=15) | 1,0066 | 5,437 |
| B | 300 | 166 | sim | 14 | 4,67% | 89 | 29,67% | 6 | 2,00% | 1 | 0,33% | 0,3107 (N=14) | 0,9907 | 5,537 |

Período do experimento: 2026-02-02 → 2026-04-26 (600 linhas). Ambas as variantes ultrapassaram a amostra mínima de 166.

Linhas lidas: 800 · Período: 2026-01-05 → 2026-04-26
