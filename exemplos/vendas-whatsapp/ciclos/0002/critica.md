# Crítica — Ciclo 0002 (v1 atual · experimento E0001 A vs B)

Fonte: `ciclos/0002/evidencia.md` (800 linhas, 2026-01-05 → 2026-04-26; 600 novas, 2026-02-02 → 2026-04-26, alocadas A/B). Versão atual: v1 (= variante A). Variante B: `versoes/candidata-vB` (H2, teto de 80 palavras).
Escala de força (n_minimo_para_padrao = 30): FORTE N ≥ 90 · MODERADA N ≥ 30 · FRACA N < 30. Força pela N do grupo; contagem de eventos anotada quando é pequena.
Populações: **A-exp** = v1 no período do experimento (N=300) · **B** = candidata-vB (N=300) · **v1 total** = 500 · **pré-exp** = 200 linhas do ciclo 0001 (derivadas: v1 total − A-exp).

## 1. Funciona

| Afirmação | Número | Força |
|---|---|---|
| B responde mais que A: +10,3 pp na métrica-sinal, e B chega ao `metrica_sinal.alvo` (0,30) | resposta B 29,67% (89/300) vs A 19,33% (58/300); z=2,94, p≈0,003 (derivado) | FORTE |
| B custa menos por proposta | custo B 0,9907 vs A 1,0066 (−1,6%) | FORTE |
| Guarda-corpo `optout` dentro da tolerância em B | optout B 0,33% (1/300) vs A 0,00% (0/300); delta +0,33 pp < 0,5 pp | FORTE (N) · 1 evento |
| A (v1, sem mudança) atinge a métrica-alvo no período do experimento | conversão A-exp 5,00% (15/300) vs alvo 0,05; resposta 19,33% | FORTE |
| Custo e tempo de v1 continuam estáveis | v1 total: custo 1,0153, tempo 5,448 min (N=500); faixa semanal custo 0,9528–1,0720, tempo 5,02–5,80 (N=50 cada) | FORTE (geral) · MODERADA (por semana) |
| Segmento `medio` responde na média geral nas linhas novas (no ciclo 0001 respondia pela metade) | resposta 25,60% (64/250) vs 24,5% geral (147/600, derivado) | FORTE |
| Segmento `pequeno` responde acima da média geral nas linhas novas | resposta 27,82% (74/266) vs 24,5% geral (147/600, derivado) | FORTE |

## 2. Falha

| Afirmação | Número | Força |
|---|---|---|
| **Guarda-corpo `reclamacoes` rompido em B** — tolerância 0,0 é regra determinística: qualquer excesso sobre A conta, independentemente de significância (Fisher p≈0,12, derivado) | reclamou B 2,00% (6/300) vs A 0,33% (1/300); delta +1,67 pp | FORTE (N) · 6 vs 1 eventos |
| A condição de parada antecipada declarada em `experimento.md` ("uma única reclamação em B acima da taxa de A encerra o teste") está satisfeita nos números acumulados | B 6/300 > A 1/300 | FORTE (N) |
| O ganho de resposta de B não aparece na conversão: +31 respostas em B geraram 0 conversões a mais | resultado B 4,67% (14/300) vs A 5,00% (15/300); z=−0,19, p≈0,85 (derivado). `experimento.md` já registra que conversão exige 1.506/variante — não potencializado | FORTE (N) · 14 vs 15 eventos |
| Tempo por proposta em B não caiu — H2 previa queda como efeito secundário | tempo B 5,537 vs A 5,437 min (+0,10) | FORTE |
| Desperdício de cadência: yaml diz `ciclo: semanal`; ciclo 0001 = 2026-02-02, ciclo 0002 = 2026-04-27 (12 semanas, 600 linhas). `veredito.md` previa primeiro veredito possível em 2026-03-23 (N≥166) — ~5 semanas / ~250 propostas rodaram além disso sob um teste cuja condição de parada pode já ter sido cruzada | 300/variante contra 166 exigidos (+81% de amostra); reclamações aparecem em W06, W07, W08, W09, W10, W11, W15 (1 cada) | FORTE |
| `evidencia.md` não traz `variante × semana` nem `segmento × variante` — não permite datar quando a condição de parada foi cruzada pela primeira vez, nem afirmar se a brevidade de B explica as 5 reclamações de `medio` | 7 reclamações no período em 7 semanas distintas; medio 5/250, pequeno 1/266, grande 1/84 | — (lacuna de dado) |
| Segmento `grande` responde pela metade dos demais nas linhas novas | resposta 10,71% (9/84) vs 27,82% (pequeno) e 25,60% (medio) | MODERADA |
| Volatilidade semanal da conversão em v1/AB: 11 das 16 semanas com ≤ 2 conversões | W02 0/50, W03 0/50, W09 1/50, W10 1/50, W12 1/50, W13 1/50 | MODERADA (cada) |

Desperdício de custo/tempo, resumido: 600 propostas novas × ~1,0 ≈ 599 de custo (derivado: 300×1,0066 + 300×0,9907) e ≈ 54,9 h de tempo (600 × ~5,49 min) para 29 conversões — ≈ 20,7 por conversão (contra ≈ 41 no ciclo 0001). A metade B desse gasto gerou mais conversas (89 vs 58) sem gerar mais fechamentos; o tempo de atendimento dessas respostas extras não é medido no CSV.

## 3. Observado, não conclusivo (FRACA)

- **Margem média** (guarda-corpo `sem_piorar`, tolerância 0,01): A 0,3127 (N=15) vs B 0,3107 (N=14), delta −0,002 — dentro da tolerância na leitura literal, mas N de conversões < 30 em ambos: não dá para afirmar que a tolerância está respeitada. Idem margem por segmento: 0,31 (N=11) / 0,32 (N=15) / 0,30 (N=3).
- **Deriva da linha de base de A sem mudança de prompt**: pré-exp (derivado) resposta 17,00% (34/200) e conversão 2,50% (5/200); A-exp 19,33% e 5,00%. Por semana os N são 50 e a diferença de resposta não é significativa (z=0,66, derivado); conversão dobrou com 5→15 eventos (z=1,40). O experimento foi dimensionado sobre 0,17; o A real durante o teste ficou em 0,19.
- **W08 é um outlier**: 7/50 conversões (14%) = 24% das 29 conversões do experimento em uma só semana; resposta 40% (20/50). MODERADA pela N, mas sem `variante × semana` não é atribuível a A ou B — pode inflar qualquer uma das duas.
- **Contagens de eventos de guarda-corpo** (reclamou A 1 / B 6; optout A 0 / B 1) e por segmento (pequeno 2+3, medio 5+0, grande 1+0 em todo o período) — todas < 30 eventos.
- **Conversão por segmento** nas linhas novas: 4,14% / 6,00% / 3,57% vêm de 11 / 15 / 3 eventos — não distingue os segmentos entre si.
- **Segmento × semana**: 48 combinações, todas com N ≤ 27 — nada reportável.
- **Invariáveis** (desconto > 10%, promessa de resultado, contato pós-opt-out, concorrentes): sem colunas no CSV, como no ciclo 0001 — não há como confirmar nem negar. O texto de candidata-vB não contradiz nenhuma das quatro; o teto de 80 palavras não toca as invariáveis.
- **Unidade de custo vs. `teto.custo_por_ciclo_brl: 50`**: mesma ambiguidade do ciclo 0001; ≈ 50/semana de custo por proposta, comparação com o teto não afirmável.

## 4. Cruzamento com a memória

- `memoria/observado-nao-testado.md`, entrada 1 (**suavizar abordagem em `pequeno`**, 3 eventos de guarda-corpo em W05): nas 600 linhas novas, `pequeno` tem 1 reclamação + 1 opt-out (266) e `medio` tem 5 reclamações (250). A direção inverteu; continua FRACA (eventos < 30). Sem `segmento × variante`, não é possível dizer se as 5 de `medio` vêm de B.
- Entrada 3 (**variante específica para `medio`**, porque respondia 10,26%, N=78 — MODERADA no ciclo 0001): nas linhas novas `medio` responde 25,60% (N=250) e tem a melhor conversão (6,00%). A premissa MODERADA do ciclo 0001 não se sustentou com mais N; `grande` é o que responde menos agora (10,71%, N=84).
- Entrada 2 (**ajustar oferta por segmento para proteger margem**, `grande` 0,35 com N=1): agora `grande` 0,30 (N=3). Nenhum sinal; segue FRACA.
- `memoria/descartados.md`, H1: vetada por pressão prevista sobre `reclamacoes`/`optout`. A hipótese aprovada como "segura" (H2) é a que elevou reclamações de 1 para 6 em B. Registro diagnóstico: o veto de H1 não cobre H2, e nada em `descartados.md` resolve a falha de `reclamacoes` desta crítica.
- `memoria/ledger.md`: H2 EM TESTE (agora com N 300/300 ≥ 166); H3 AGUARDANDO (ainda não testada, um teste por vez). `memoria/aprendizados.md` vazio — nada promovido, nada a cruzar.
- `loop-r.yaml` segue com `metrica_sinal.atual: 0.20`, `amostra_minima_por_variante: 300` e `duracao_estimada_semanas: 12` desatualizados (já apontado em `experimento.md` e `amostra-minima.md`); `meta_info.ciclos_rodados: 1`. Não altera nenhuma afirmação acima — o Observador usou 166.
