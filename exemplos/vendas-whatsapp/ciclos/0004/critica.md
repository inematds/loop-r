# Crítica — Ciclo 0004 (v1 atual · E0002 em andamento, N ≥ mínimo nas duas variantes)

Fonte: `ciclos/0004/evidencia.md` (1450 linhas, 2026-01-05 → 2026-07-26; 600 novas, 2026-05-04 → 2026-07-26, todas dentro de E0002). Versão atual: v1 (= variante A). Candidata: `versoes/candidata-vB` (H3, só o item 1 da Estrutura alterado — diff de 1 hunk). Data do ciclo: 2026-07-27.
Escala de força (n_minimo_para_padrao = 30): FORTE N ≥ 90 · MODERADA N ≥ 30 · FRACA N < 30. Força pela N do grupo; contagem de eventos anotada quando é pequena. Estatísticas marcadas "(derivado)" são calculadas só a partir das contagens da evidência.
Populações desta crítica: **E0002-A** = 300 (v1, 2026-05-04→) · **E0002-B** = 300 (candidata-vB, 2026-05-04→) · **v1/A pré-E0002** = 550 (2026-01-05 → 2026-05-03).

**Aviso de leitura (lacuna da evidência, não inconsistência de dados):** a evidência afirma "nenhuma linha `variante=B` fora da janela do experimento", mas o consolidado em (c) mostra v1/B com N=600 — 300 são E0002-B e as outras 300 são E0001-B (H2, teto de 80 palavras, descartada no ciclo 0002; 850 linhas pré-E0002 − 550 A = 300 B). Como `versao` = v1 em 100% das linhas, o rótulo B agrupa **dois prompts diferentes** e só a data os separa. Consequência: as tabelas "todo o período" com B em (c) consolidado e (d) segmento × variante misturam H2 e H3. Toda afirmação sobre B abaixo usa **só** as tabelas com data ≥ 2026-05-04. Toda afirmação sobre A por segmento fora da janela usa só a linha v1/A pré-E0002 (550), que é pura.

## 1. Funciona

| Afirmação | Número | Força |
|---|---|---|
| **B moveu a métrica-sinal contra A concorrente** — a única coisa que H3 prometeu mover | resposta E0002-B 29,33% (88/300) vs E0002-A 19,33% (58/300) · Δ = +10,00 pp · z = 2,85, p = 0,004 (derivado) | FORTE (N=300/300) |
| Linha de base de A não se mexeu entre janelas — a comparação concorrente é válida | resposta v1/A pré 18,36% (101/550) vs E0002-A 19,33% (58/300) · z = 0,35, p = 0,73 (derivado) | FORTE (N=550/300) |
| B responde mais em `pequeno` e `medio` (janela E0002) | pequeno: A 18,90% (24/127) → B 31,25% (40/128) · medio: A 19,23% (25/130) → B 31,97% (39/122) | FORTE (N ≥ 122 em cada célula) |
| Custo por proposta de B menor que A | E0002-B 0,9821 vs E0002-A 1,0028 · Δ = −0,0207 (N=300/300) | FORTE |
| Guarda-corpo `optout` não piora em B | E0002-B 0,33% (1/300) vs E0002-A 1,00% (3/300) · Δ = −0,67 pp, tolerância +0,005 → dentro · Fisher p = 0,62 (derivado) | FORTE (N) · 1 + 3 eventos |
| Guarda-corpo `reclamacoes` dentro da tolerância vigente | E0002-B 1,33% (4/300) vs E0002-A 0,67% (2/300) · Δ = +0,0067 < 0,01 · Fisher p = 0,69 (derivado) | FORTE (N) · 4 + 2 eventos — ver §2 e §4: passa só pela tolerância ajustada no 0002 |
| Amostra mínima atingida nas duas variantes (segundo experimento do loop a chegar ao N de desenho; E0001 chegou a 300/300 ≥ 166) | A 300 / B 300 ≥ 212 (+88 cada) | — (fato de processo) |
| Volume real bateu o estimado | 600 linhas em 12 semanas = 50/semana = `volume_estimado_por_semana` | — (fato de processo) |

## 2. Falha

| Afirmação | Número | Força |
|---|---|---|
| **B ficou abaixo do ENTÃO de H3 e do `metrica_sinal.alvo` (≥ 30%)** | 29,33% (88/300); 30% exigiria 90/300 — faltaram 2 respostas. Δ observado +10,00 pp vs. efeito de desenho +11,64 pp (0,1836 → 0,30, `ciclos/0003/experimento.md`), que o próprio experimento declara como "efeito menor que isso não paga o ciclo" | FORTE (N=300) — registro dos dois lados; o veredito é do Avaliador |
| **Sinal moveu, alvo não — pela segunda vez no loop** | resultado E0002-B 3,67% (11/300) vs E0002-A 3,00% (9/300) · Δ = +0,67 pp · z = 0,45, p = 0,65 / Fisher p = 0,82 (derivado). `metrica_alvo.alvo` = 0,05; nenhuma variante chega | FORTE (N) · 9 + 11 eventos |
| B em `grande` não responde mais que A | grande: A 20,93% (9/43) vs B 18,00% (9/50) · Δ = −2,93 pp — `grande` é o único segmento onde a abertura específica não levanta a resposta | MODERADA (N 43/50) · 9 + 9 eventos |
| Conversão de v1/A na janela caiu contra a linha de base pré-E0002 | E0002-A 3,00% (9/300) vs pré 4,18% (23/550) · z = −0,87, p = 0,39 (derivado) — não significativo; `metrica_alvo.atual: 0.03` do yaml coincide com a janela e está abaixo do consolidado 3,76% (32/850) | FORTE (N) · 9 + 23 eventos — direção contra o alvo, sem significância |
| **Cadência saiu do contrato (`ciclo: semanal`) de novo** | ciclo 0003 = 2026-05-04, ciclo 0004 = 2026-07-27: 84 dias = 12 semanas sem ciclo. O 0003 registrou "cadência voltou ao contrato"; durou um ciclo. Sequência de intervalos 0001→0002→0003→0004: 12 / 1 / 12 semanas — o semanal foi a exceção | — (fato de processo) |
| **Sobreamostragem sem veredito**: o mínimo de 424 linhas (212×2) foi atingido em ~8,5 semanas; ~176 linhas / ~3,5 semanas rodaram além do desenho sem que nenhum Avaliador lesse | 600 − 424 = 176 linhas · 176 × ≈0,99 ≈ 175 de custo e 176 × ≈5,5 min ≈ 16 h (derivado) além do necessário para o veredito. Não é inédito: E0001 rodou 300/300 contra mínimo de 166 | FORTE (fato) |
| **Parada antecipada por guarda-corpo ficou sem observador por 12 semanas**: `experimento.md` prevê "B encerra o teste se `reclamacoes` ficar acima de +0,01 …", mas os 11 vereditos semanais intermediários (AMOSTRA_INSUFICIENTE com N acumulado) não existem — a cláusula nunca pôde disparar | 0 ciclos entre 2026-05-04 e 2026-07-27; 600 linhas sem leitura | — (fato de processo) |
| Custo por conversão continua alto nas duas variantes | E0002-A 300 × 1,0028 ≈ 301 / 9 ≈ 33,4 por conversão · E0002-B 300 × 0,9821 ≈ 295 / 11 ≈ 26,8 (derivado) — vs 24,2 de v1/A todo o período no 0003 | FORTE (N) · 9 + 11 eventos |
| Tempo por proposta de B ligeiramente maior | E0002-B 5,550 vs E0002-A 5,380 min · Δ = +0,170 min (N=300/300) | FORTE (N) — sem guarda-corpo para tempo; registro |

## 3. Observado, não conclusivo (FRACA)

- **Margem média** (guarda-corpo `sem_piorar`, tolerância 0,01): E0002-A 0,3178 (N=9) vs E0002-B 0,3245 (N=11), Δ = +0,0067. Nenhuma das duas chega a 30 conversões — a tolerância **não é verificável** neste experimento, mesma lacuna do 0003. Só como registro: a direção não é de piora.
- **As 4 reclamações de B estão todas em `pequeno`**: pequeno/B 3,12% (4/128) vs pequeno/A 0,79% (1/127), Fisher p = 0,37 (derivado); medio/B 0/122, grande/B 0/50. 4 eventos. Se fosse padrão, a abertura específica incomodaria justamente no segmento onde mais levanta resposta — mas não passa de 4 eventos.
- **`grande` na janela**: B 0/50 conversões vs A 2/43; A com 2/43 opt-outs (4,65%) vs B 0/50. Eventos ≤ 2 em cada célula.
- **Conversão por segmento na janela**: pequeno A 3/127 vs B 6/128; medio A 4/130 vs B 5/122; grande A 2/43 vs B 0/50 — todos < 30 eventos; nada distingue segmentos.
- **Margem por segmento**: N entre 0 e 6 conversões por célula na janela — nada reportável.
- **Semana ISO × segmento**: nenhuma célula ≥ 30 (a evidência já marca). A evidência do 0004 também não traz série semanal simples (A vs B por semana) — a estabilidade do Δ de resposta ao longo das 12 semanas não é verificável.
- **Invariáveis** (desconto > 10%, promessa de resultado, contato pós-opt-out, concorrentes): sem colunas no CSV, como nos ciclos 0001–0003. Não há como confirmar nem negar cumprimento em nenhuma variante — e a candidata-vB introduz texto novo (citar a queixa da cliente) sem nenhuma medida de que não escorrega para promessa de resultado.

## Lacunas de dado (limitam o que se pode afirmar)

- Rótulo `versao` = v1 em 100% das linhas, inclusive nas 600 de B (E0001-B e E0002-B): o CSV não distingue os prompts testados; a separação depende inteiramente da data. Ver aviso de leitura no topo.
- Unidade de `custo` vs `teto.custo_por_ciclo_brl: 50`: mesma ambiguidade dos ciclos anteriores. Se o custo do CSV for BRL, as 600 linhas do "ciclo" 0004 somam ≈ 596 — 12× o teto semanal, coerente com 12 semanas, mas não afirmável.
- `loop-r.yaml`: `experimento.amostra_minima_por_variante: 212` e `duracao_estimada_semanas: 9` já refletem E0002 (resolve a nota do 0003 sobre 166). `metrica_sinal.atual: 0.20` continua desatualizado (A: 18,36% pré / 19,33% janela). `meta_info.ciclos_rodados: 3` e `ultima_promocao: null` conferem.

## 4. Cruzamento com a memória

- **`aprendizados.md`, seção Processo (tolerância de `reclamacoes` 0,0 → 0,01)** — é a primeira vez que a entrada faz trabalho. Com a tolerância antiga, B (4/300 vs 2/300, Δ = +0,0067 > 0) teria rompido o guarda-corpo e a cláusula de parada antecipada teria encerrado E0002 como encerrou E0001. Com 0,01, passa, e o Fisher p = 0,69 (derivado) confirma que a diferença está no piso de ruído que a entrada previa (~2 e.p. a 1%, N=300). O aprendizado se sustenta nos números deste ciclo. A entrada também diz "ou usar teste estatístico" — a evidência deste ciclo não aplica nenhum; a tolerância absoluta continua sendo a regra em uso.
- **`descartados.md`, H2 (teto de 80 palavras, E0001, A_SEGUE)** — E0001-B fez 29,67% (89/300) de resposta e 4,67% (14/300) de conversão; E0002-B faz 29,33% (88/300) e 3,67% (11/300). Duas mudanças só de forma, independentes, param no mesmo lugar (~29,5% de resposta, +10 pp) e nenhuma move `resultado`. Diagnóstico: a métrica-sinal é sensível ao roteiro, como a hipótese H3 dizia; o elo sinal → alvo, que `experimento.md` já declarava não testável em um ciclo (10.271/variante), agora tem duas observações contra e nenhuma a favor. Nada aqui reabre H2.
- **`descartados.md`, H1 e H4 (vetadas)** — nenhum número deste ciclo toca as duas.
- **`ledger.md`, H3** — `AGUARDANDO` de 2026-02-02 a 2026-05-04 (13 semanas), `EM TESTE` desde 2026-05-04 (12 semanas até este ciclo). Da aprovação pelo Guardião no 0001 até o primeiro veredito com amostra: 25 semanas. O `experimento.md` estimava 9 semanas de coleta.
- **`observado-nao-testado.md`, entrada 1 (suavizar `pequeno`; 3 eventos no 0001)** — reaparece com a mesma direção em B: 4/4 reclamações de E0002-B em `pequeno`. Ainda 4 eventos; segue FRACA. Em A, na janela, `pequeno` tem 1 reclamação e 0 opt-out em 127.
- **Entrada 2 (oferta por segmento para proteger margem)** — N de conversões por célula entre 0 e 6 na janela. Sem sinal; FRACA.
- **Entrada 3 (variante para `medio`, que respondia 10,26% no 0001)** — premissa segue derrubada: medio/A responde 19,23% (25/130) na janela, e medio/B 31,97% (39/122). `grande` continua o segmento que menos responde (A 20,93%, B 18,00%) e o único onde H3 não levanta nada — MODERADA (N 43/50). O 0003 já apontava `grande` como o fraco em v1/A (7,69%, N=39); na janela A subiu para 20,93% (9/43) — 3 vs 9 eventos, não distingue deriva de ruído.
- **`ciclos/0003/critica.md`, "Capacidade ociosa do loop"** — no 0003 eram 50 linhas sem hipótese em teste. No 0004 são 176 linhas além do desenho sem veredito, e 12 semanas sem nenhum ciclo lendo os guarda-corpos. A falha de processo mudou de forma (de "sem teste" para "teste sem observador"), não de natureza.
