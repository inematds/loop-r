# Relatório meta — ciclo 0001 (2026-02-02) · modo relatar · 1 ciclo rodado (sem série de 5 ainda)
- Custo do ciclo: ~391k tokens em 6 agentes (observador 66k, crítico 65k, otimizador 66k, guardião 60k, experimentador 71k, avaliador 63k); memória e meta ainda fora do custo.md. Custo por hipótese promovida: n/a (0 promovidas).
- Hipóteses acumulado: 3 geradas × 2 aprovadas pelo Guardião (H1 vetada: fechamento por escolha forçada, risco em reclamacoes/optout) × 0 promovidas. E0001 (H2, teto 80 palavras) em andamento.
- Retrabalho: nenhum ainda — Observador 0 interrupções; Avaliador AMOSTRA_INSUFICIENTE 1× (B N=0/166; primeiro veredito possível ~2026-03-23).
- Juiz: calibração pulada — `dados/calibracao.csv` (citado no yaml) não existe; sem tendência de concordância a relatar.
- Escalada de desenho: Experimentador pediu 985/variante = 40 semanas (> teto 16, per decisao-experimento.md) por causa da expectativa modesta do Otimizador (17→22%); aprovador redimensionou pelo `metrica_sinal.alvo` 0.30 → 166/variante, ~7 semanas.
- Deriva de configuração: yaml `experimento.amostra_minima_por_variante: 300` e `duracao_estimada_semanas: 12` já divergem do 166/7 efetivamente usado (o Avaliador também apontou).
- Alertas: ciclos_sem_promocao 1/5 → não; taxa de veto 0,33 < 0,5 → não; custo > 80% do teto → não avaliável (teto em R$50/ciclo, custo.md em tokens, sem conversão).
- Ledger: vazio (só cabeçalho) no momento deste relatório.
Se você quiser, sincronize o bloco `experimento` do loop-r.yaml com o dimensionamento aprovado (166/variante, ~7 semanas) para o Avaliador parar de ler um mínimo desatualizado.
