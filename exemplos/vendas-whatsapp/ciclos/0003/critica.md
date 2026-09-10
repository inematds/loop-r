# Crítica — Ciclo 0003 (v1 atual · sem experimento em andamento)

Fonte: `ciclos/0003/evidencia.md` (850 linhas, 2026-01-05 → 2026-05-03; 50 novas, 2026-04-27 → 2026-05-03, todas v1/A). Versão atual: v1 (= variante A). E0001 encerrado no ciclo 0002 (`A_SEGUE`); nenhuma linha B após 2026-04-26.
Escala de força (n_minimo_para_padrao = 30): FORTE N ≥ 90 · MODERADA N ≥ 30 · FRACA N < 30. Força pela N do grupo; contagem de eventos anotada quando é pequena.
Populações: **v1/A total** = 550 (pré 200 + E0001-A 300 + pós 50) — linha de base desta crítica · **E0001-A** = 300 · **E0001-B** = 300 (candidata-vB, descartada) · **pós** = 50 linhas novas.
Aviso de leitura: as tabelas de segmento "todo o período" e "por período × segmento" em (c) misturam A e B dentro de E0001. Toda afirmação sobre v1/A por segmento abaixo usa só as linhas A de "segmento × variante dentro de E0001".

## 1. Funciona

| Afirmação | Número | Força |
|---|---|---|
| v1/A mantém reclamações e opt-outs raros em todo o período | reclamou 0,36% (2/550) · optout 0,36% (2/550); pós 0/50 e 0/50 | FORTE (N) · 2 + 2 eventos |
| Custo por proposta de v1/A estável, e menor na janela pós | pré 1,0283 (N=200) · E0001-A 1,0066 (N=300) · pós 0,9702 (N=50) · total 1,0112 (N=550) | FORTE (total) · MODERADA (pós) |
| Tempo por proposta de v1/A estável | pré 5,465 · E0001-A 5,437 · pós 5,660 min · total 5,467 (N=550) | FORTE (total) · MODERADA (pós) |
| Segmentos `pequeno` e `medio` respondem acima de `grande` em v1/A durante E0001 | pequeno/A 24,06% (32/133) · medio/A 17,97% (23/128) · grande/A 7,69% (3/39) | FORTE (pequeno, medio) · MODERADA (grande) |
| Cadência voltou ao contrato (`ciclo: semanal`) | ciclo 0002 = 2026-04-27, ciclo 0003 = 2026-05-04 (7 dias, 50 linhas = `volume_estimado_por_semana`) | — (fato de processo) |

## 2. Falha

| Afirmação | Número | Força |
|---|---|---|
| **Métrica-alvo não atingida na linha de base de todo o período**: conversão v1/A abaixo de `metrica_alvo.alvo` 0,05 | resultado 4,18% (23/550) | FORTE (N) · 23 eventos |
| A leitura "A atinge a meta" do ciclo 0002 dependia da janela: só E0001-A passa de 0,05; pré fica bem abaixo; o consolidado não chega | pré 2,50% (5/200) · E0001-A 5,00% (15/300) · pós 6,00% (3/50) · total 4,18% | FORTE (pré, E0001-A) · FRACA (pós, eventos 3) |
| **Métrica-sinal longe do alvo** (`metrica_sinal.alvo` 0,30) em v1/A; a única variante que chegou a 0,30 (B, 29,67%) está em `descartados.md` | resposta v1/A 18,36% (101/550) · pré 17,00% · E0001-A 19,33% · pós 18,00% (9/50) | FORTE (total, pré, E0001-A) · MODERADA (pós) |
| Segmento `grande` é o que menos responde em v1/A, em qualquer janela onde N permite ler | E0001 grande/A 7,69% (3/39) vs medio/A 17,97% e pequeno/A 24,06%; pré grande 20,00% (6/30, todas A) — a leitura vai contra a direção mas ambos têm N entre 30 e 45 | MODERADA · 3 e 6 eventos |
| **Capacidade ociosa do loop**: 50 propostas rodaram na janela pós sem nenhuma hipótese em teste, enquanto H3 está `AGUARDANDO` no ledger desde 2026-02-02 (13 semanas) sob `max_testes_simultaneos: 1` | 50 × 0,9702 ≈ 48,5 de custo e 50 × 5,660 min ≈ 4,7 h (derivado) sem informação experimental gerada | FORTE (fato) |
| Custo por conversão de v1/A continua alto | 550 × 1,0112 ≈ 556 de custo para 23 conversões ≈ 24,2 por conversão; pós: 48,5 / 3 ≈ 16,2 (derivado) | FORTE (total) · FRACA (pós, 3 eventos) |

## 3. Observado, não conclusivo (FRACA)

- **Margem média** (guarda-corpo `sem_piorar`, tolerância 0,01): v1/A 0,3157 com N=23 conversões; pós 0,3233 com N=3; pré 0,3200 (N=5); E0001-A 0,3127 (N=15). Nenhuma janela chega a 30 conversões — a tolerância não é verificável em nenhuma comparação.
- **Deriva da conversão de A sem mudança de prompt**: 2,50% → 5,00% → 6,00% (pré → E0001-A → pós) com 5 → 15 → 3 eventos. A crítica do 0002 já registrava pré vs E0001-A como z≈1,40 (derivado, não significativo); a janela pós tem 3 eventos. Não dá para dizer se a linha de base subiu ou se é ruído.
- **Janela pós por segmento**: grande N=7, medio N=23, pequeno N=20 — nada reportável (a evidência já as marca abaixo do mínimo).
- **Eventos de guarda-corpo por segmento, todo o período (A+B misturados)**: reclamou pequeno 2 / medio 5 / grande 1; optout pequeno 3 / medio 0 / grande 0 — todos < 30 eventos. Dentro de E0001, as linhas A têm reclamou 0/133, 1/128, 0/39 e optout 0/133, 0/128, 0/39.
- **Conversão por segmento em v1/A (E0001)**: pequeno 5,26% (7/133), medio 5,47% (7/128), grande 2,56% (1/39) — 7, 7 e 1 eventos; não distingue os segmentos.
- **Invariáveis** (desconto > 10%, promessa de resultado, contato pós-opt-out, concorrentes): sem colunas no CSV, como nos ciclos 0001 e 0002 — não há como confirmar nem negar. `versoes/atual/executor.prompt.md` (v1) declara as quatro regras em texto; a evidência não mede cumprimento.

## Lacunas de dado (não são afirmações; limitam o que se pode afirmar)

- `evidencia.md` deste ciclo não traz série semanal (o 0002 trazia W01–W16). Volatilidade semanal da conversão e outliers (W08 no 0002) não são verificáveis aqui; a janela pós é uma semana só.
- Unidade de `custo` vs `teto.custo_por_ciclo_brl: 50`: mesma ambiguidade dos ciclos anteriores. Se o custo do CSV for em BRL, a janela pós (≈ 48,5) fica dentro do teto — não afirmável.

## 4. Cruzamento com a memória

- **`descartados.md`, H2 (teto de 80 palavras, E0001, A_SEGUE)** — descartada por romper `reclamacoes` com tolerância 0,0. `aprendizados.md` (seção Processo) registra a tolerância ajustada para 0,01 no ciclo 0002 e que E0001 **não** é reavaliado. Só como diagnóstico: o Δ observado (+1,67 pp, 6/300 vs 1/300) também excede 0,01 — a regra nova, aplicada aos mesmos números, daria o mesmo resultado de guarda-corpo. Nada nesta crítica reabre H2; o que a evidência mostra é que a métrica-sinal de v1/A (18,36%) ficou onde estava e que a única variante que a moveu está descartada.
- **`descartados.md`, H1 (fechamento por escolha forçada)** — vetada pelo Guardião no 0001; nenhum número deste ciclo toca a hipótese.
- **`ledger.md`, H3 (abrir citando ponto específico da avaliação)** — `AGUARDANDO` desde 2026-02-02, aprovada pelo Guardião no 0001, nunca testada. Com E0001 encerrado, não há mais o bloqueio "um teste por vez"; a janela pós rodou vazia (ver "Capacidade ociosa" em Falha). Diagnóstico de estado, não proposta.
- **`observado-nao-testado.md`, entrada 3 (variante para `medio`, que respondia 10,26% no 0001)** — premissa não se sustenta: medio/A responde 17,97% (N=128) em E0001 e 21,94% (N=351, A+B) no consolidado. `grande` é o segmento fraco em v1/A (7,69%, N=39 — MODERADA).
- **Entrada 1 (suavizar `pequeno`, 3 eventos de guarda-corpo)** — direção segue invertida: no consolidado `medio` tem 5 reclamações e `pequeno` 2 (com 3 opt-outs). Em v1/A puro (E0001) `pequeno` tem 0 eventos. Segue FRACA (eventos < 30).
- **Entrada 2 (oferta por segmento para proteger margem)** — margem por segmento no consolidado 0,3079 (N=14) / 0,3206 (N=18) / 0,3060 (N=5). Sem sinal; FRACA.
- **`aprendizados.md`** — única entrada é de processo (tolerância de evento raro). Nenhum aprendizado de conteúdo do prompt promovido; v1 é o mesmo texto desde o início.
- **`loop-r.yaml`** — `metrica_alvo.atual: 0.03` e `metrica_sinal.atual: 0.20` estão desatualizados frente à linha de base de todo o período (4,18% e 18,36%, N=550); `meta_info.ciclos_rodados: 2` e `ultima_promocao: null` conferem. Registro diagnóstico; não altera nenhuma afirmação acima.
