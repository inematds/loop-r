Custo por ciclo (custo.md): 0001 ~391k · 0002 ~366k · 0003 ~565k · 0004 ~306k (parcial, sem meta-agente) · média ~407k tokens · total ~1,63M → **custo por hipótese promovida: ~1,63M tokens (1 promoção, v2)**.
Hipóteses: 5 apresentadas / 4 distintas (H1–H4; H3 reapresentada no 0003) × 3 aprovações do Guardião (H2, H3, H3) × 1 promovida (H3 → v2). Vetadas 2 (H1, H4) · descartada por guarda-corpo 1 (H2).
Retrabalho: Avaliador AMOSTRA_INSUFICIENTE 2× (0001, 0003, não consecutivas); Crítico apontou cadência fora do contrato em 3 ciclos seguidos (intervalos 12/1/12 semanas) e é o agente mais caro (82–83k); Guardião rejulgou H3; Observador 0 interrupções; esquema ganhou coluna `experimento` só no 0004 (rótulo B misturava H2 e H3).
Juiz/calibração: não se aplica — `dados/calibracao.csv` não existe e a métrica é objetiva; sem tendência a reportar.
Elo sinal→alvo não provado: dois B independentes (E0001-B 29,67%, E0002-B 29,33%) subiram `resposta` +10 pp e nenhum moveu `conversao` (p=0,85 e p=0,65) — duas observações contra, zero a favor; a versão promovida (v2) foi aprovada só pelo sinal.
ALERTA taxa de veto: 2/4 distintas = 0,50 ≥ `taxa_veto_guardiao` 0,5 (mesmo estado do 0003).
ALERTA custo: pela única conversão disponível (decisao.md 0004: ~430k ≈ R$45), o ciclo ficou em 90% do teto de R$50 (> 80%); o 0003 (565k) provavelmente estourou o teto.
ciclos_sem_promocao: 0 (promoção neste ciclo) — sem alerta.
Se você quiser, antes de gerar hipóteses novas, troque ou complemente a métrica-sinal por algo mais próximo do fechamento (ex.: "respondeu e pediu agendamento/valor"), porque `taxa_resposta` já provou duas vezes que sobe sem mover `conversao`.
