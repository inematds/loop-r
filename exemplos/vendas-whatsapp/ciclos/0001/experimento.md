EXPERIMENTO E0001 — H2: Teto de 80 palavras na mensagem
Variante A: versoes/atual (v1)      Variante B: versoes/candidata-vB
Métrica do teste: taxa_resposta  0,17 → 0,30 (efeito mínimo que vale detectar = `metrica_sinal.alvo` do yaml; ver decisão abaixo)       Vigiadas: margem_media (tol. 0,01) · reclamacoes (tol. 0,0) · optout (tol. 0,005) · conversao (métrica alvo, 0,03 → 0,05, não testável em um ciclo: n=1.506/variante = 61 semanas)
Amostra mínima: 166/variante  (conta: z_{α/2}=1,9600, z_β=0,8416, p̄=0,235; n = [1,9600·√(2·0,235·0,765) + 0,8416·√(0,17·0,83 + 0,30·0,70)]² / 0,13² = 165,8 → 166; tabela completa em evals/amostra-minima.md)
Duração estimada: 7 semanas a 50/semana  (166 × 2 / 50 = 6,64 → 7)
Alocação: 50/50 por id (ímpar → A, par → B, ordem de chegada; nunca por escolha do Executor)      Parada antecipada: só por guarda-corpo — `reclamacoes` tem tolerância 0,0: uma única reclamação em B acima da taxa de A encerra o teste; idem `optout` acima de +0,005 e `margem_media` abaixo de −0,01. Nunca por "já está ganhando".
Status: EM ANDAMENTO desde 2026-02-02

## Escolha da hipótese
Guardião: H1 VETADA, H2 APROVADA (FORTE), H3 APROVADA (MODERADA). Escolhida H2 — aprovada de maior força. H3 fica na fila para o próximo ciclo (um teste por vez; nada de H3 na candidata-vB). `versoes/candidata-vB` inalterada pela decisão abaixo (só o dimensionamento mudou).

## Leitura do veredito com esta base
O teste está dimensionado para detectar 17% → 30%. Se B entregar só os 22% esperados pelo Otimizador, o teste provavelmente não distingue de A e o veredito será `A_SEGUE` — aceito pelo aprovador: efeito menor que 30% não paga o ciclo.

## Histórico do desenho — por que mudou (registro mantido)
**Desenho anterior (2026-02-02, 1ª versão deste arquivo):** teste dimensionado pelo ENTÃO literal de H2 (0,17 → 0,22): 985/variante, 40 semanas — acima do teto de 16 semanas. A regra "refaça sobre `metrica_sinal`" não tinha para onde cair (o teste já era sobre `taxa_resposta`; `conversao` já vigiada). O Experimentador não trocou o `esperado` por conta própria e escalou ao aprovador com três opções na mesa (manter 40 sem; teto de 16 sem = 400/variante, MDE ≈ 0,251; ou reescrever o ENTÃO).

**Decisão do aprovador (`ciclos/0001/decisao-experimento.md`, 2026-02-02, Nei — simulado no exemplo):** dimensionar pelo **efeito mínimo que vale detectar**, já declarado no yaml (`metrica_sinal.alvo: 0.30`), não pela expectativa do Otimizador. Resultado: 0,17 → 0,30, **166/variante, 7 semanas** — dentro do teto. O ENTÃO de H2 em `hipoteses.md` não foi reescrito; o que mudou foi a base de dimensionamento do teste.

## Discrepâncias com o yaml (não alteradas — fora da atribuição)
`metrica_sinal.atual: 0.20` está desatualizado (observado 0,17 = 34/200); `experimento.amostra_minima_por_variante: 300` e `duracao_estimada_semanas: 12` correspondem a 0,20 → 0,30, não ao cenário real (0,17 → 0,30 = 166 / 7 sem).

## Veredito do ciclo
A cada ciclo semanal, o Avaliador compara A vs B só quando N ≥ 166 em cada variante; antes disso o veredito é AMOSTRA_INSUFICIENTE com o N acumulado.
