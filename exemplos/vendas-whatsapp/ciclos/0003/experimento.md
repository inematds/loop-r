EXPERIMENTO E0002 — H3: Abrir com algo específico da avaliação
Variante A: versoes/atual (v1)      Variante B: versoes/candidata-vB
Métrica do teste: taxa_resposta  0,1836 → 0,30 (atual = v1/A todo o período, 101/550, `ciclos/0003/evidencia.md` §b; esperado = `metrica_sinal.alvo` do yaml — efeito mínimo que vale detectar, não a expectativa do Otimizador)       Vigiadas: margem_media (tol. 0,01) · reclamacoes (tol. 0,01) · optout (tol. 0,005) · conversao (métrica alvo, 0,0418 → 0,05, não testável em um ciclo: n=10.271/variante = 411 semanas)
Amostra mínima: 212/variante  (conta: z_{α/2}=1,9600, z_β=0,8416, p̄=0,2418; n = [1,9600·√(2·0,2418·0,7582) + 0,8416·√(0,1836·0,8164 + 0,30·0,70)]² / (0,30 − 0,1836)² = [1,9600·0,6055 + 0,8416·0,5999]² / 0,013540 = 1,6918² / 0,013540 = 2,8621 / 0,013540 = 211,37 → 212; tabela completa em evals/amostra-minima.md)
Duração estimada: 9 semanas a 50/semana  (212 × 2 / 50 = 8,48 → 9; dentro do teto de 16 — não há necessidade de trocar métrica)
Alocação: 50/50 por id (ímpar → A, par → B, ordem de chegada; nunca por escolha do Executor)      Parada antecipada: só por guarda-corpo — B encerra o teste se `reclamacoes` ficar acima da taxa de A além de +0,01, `optout` além de +0,005 ou `margem_media` abaixo de −0,01. Nunca por "já está ganhando".
Status: EM ANDAMENTO desde 2026-05-04

## Escolha da hipótese
Guardião (ciclo 0003): H3 APROVADA, H4 VETADA. Única aprovada → H3 (MODERADA; já aprovada também no ciclo 0001, aguardando desde 2026-02-02). Nenhum experimento em andamento (E0001 encerrado com `A_SEGUE` no ciclo 0002) — `max_testes_simultaneos: 1` respeitado. `versoes/candidata-vB` antiga (H2/E0001) substituída; a nova contém **só** a MUDANÇA de H3 (diff de 1 hunk em `versoes/candidata-vB/CHANGELOG.md`). `versoes/atual` (→ v1) inalterada.

## Por que 212 e não 166
`hipoteses.md` cita "166/variante" — esse número vem de E0001 (0,17 → 0,30). A base agora é 0,1836 (v1/A em todo o período, N=550), mais perto do alvo: o mesmo alvo de 0,30 dá uma diferença menor (11,64 pp em vez de 13 pp), logo mais amostra: **212/variante, 9 semanas**. O `experimento.amostra_minima_por_variante: 166` do yaml fica desatualizado para E0002 (não alterado — fora da atribuição).

## Leitura do veredito com esta base
O teste detecta efeitos ≥ 0,30 (≈ +11,6 pp). H3 prevê exatamente o alvo (≥ 30%), então dimensionamento e ENTÃO coincidem. Efeitos abaixo de 0,30 têm poder < 80% com 212/variante — quanto menor o efeito real, mais provável `A_SEGUE`; efeito menor que o alvo não paga o ciclo.

## Veredito do ciclo
A cada ciclo semanal, o Avaliador compara A vs B só quando N ≥ 212 em cada variante; antes disso o veredito é AMOSTRA_INSUFICIENTE com o N acumulado.
