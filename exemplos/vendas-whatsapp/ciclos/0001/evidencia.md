# Evidência — Ciclo 0001

## Consistência
OK. 200 linhas, colunas obrigatórias preenchidas, sem ids duplicados, datas válidas, `versao` (v1) existe em `versoes/`, `variante` só `A` (sem experimento), valores sim/não válidos.

## Por versão × variante (todo o período)

| versão | variante | N | conversão (sim) | conversão % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | A | 200 | 5 | 2,50% | 34 | 17,00% | 1 | 0,50% | 2 | 1,00% | 0,32 (N=5) | 1,0283 | 5,465 |

Não há linhas de ciclos anteriores para excluir (ciclo 0001 é o primeiro).

## Por segmento (N ≥ 30 — n_minimo_para_padrao)

| segmento | N | conversão (sim) | conversão % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pequeno | 92 | 3 | 3,26% | 20 | 21,74% | 1 | 1,09% | 2 | 2,17% | 0,31 (N=3) | 1,0201 | 5,272 |
| medio | 78 | 1 | 1,28% | 8 | 10,26% | 0 | 0,00% | 0 | 0,00% | 0,32 (N=1) | 1,0472 | 5,577 |
| grande | 30 | 1 | 3,33% | 6 | 20,00% | 0 | 0,00% | 0 | 0,00% | 0,35 (N=1) | 1,0043 | 5,767 |

## Por semana ISO (N ≥ 30)

| semana | N | conversão (sim) | conversão % | resposta (sim) | resposta % | reclamou (sim) | reclamou % | optout (sim) | optout % | margem média | custo médio | tempo médio (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-W02 | 50 | 0 | 0,00% | 7 | 14,00% | 0 | 0,00% | 0 | 0,00% | — (N=0) | 1,0644 | 5,020 |
| 2026-W03 | 50 | 0 | 0,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | — (N=0) | 1,0172 | 5,800 |
| 2026-W04 | 50 | 2 | 4,00% | 9 | 18,00% | 0 | 0,00% | 0 | 0,00% | 0,30 (N=2) | 1,0350 | 5,380 |
| 2026-W05 | 50 | 3 | 6,00% | 9 | 18,00% | 1 | 2,00% | 2 | 4,00% | 0,33 (N=3) | 0,9966 | 5,660 |

## Por segmento × semana ISO

Todas as combinações abaixo do N mínimo (n_minimo_para_padrao=30):

| segmento | semana | N |
|---|---|---|
| grande | 2026-W02 | 8 |
| grande | 2026-W03 | 6 |
| grande | 2026-W04 | 7 |
| grande | 2026-W05 | 9 |
| medio | 2026-W02 | 15 |
| medio | 2026-W03 | 24 |
| medio | 2026-W04 | 24 |
| medio | 2026-W05 | 15 |
| pequeno | 2026-W02 | 27 |
| pequeno | 2026-W03 | 20 |
| pequeno | 2026-W04 | 19 |
| pequeno | 2026-W05 | 26 |

Abaixo do N mínimo (N=30) em todas as 12 combinações segmento × semana — nenhuma reportável individualmente.

## Experimento em andamento

Não há `ciclos/<anterior>/experimento.md` (ciclo 0001 é o primeiro do loop). Todas as 200 linhas são variante `A`; não há variante `B` no período. N/A.

Linhas lidas: 200 · Período: 2026-01-05 → 2026-02-01
