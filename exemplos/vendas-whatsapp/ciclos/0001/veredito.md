# Veredito — Ciclo 0001 (2026-02-02)

Experimento em andamento: E0001 (H2, teto de 80 palavras) — `ciclos/0001/experimento.md`, EM ANDAMENTO desde 2026-02-02.
Calibração do juiz: pulada — `dados/calibracao.csv` não existe (e a métrica do teste é objetiva, coluna `resposta`; a rubrica não entra neste veredito).

```
VEREDITO: AMOSTRA_INSUFICIENTE
Métrica do teste: taxa_resposta  A=0,17 (N=0 no experimento; 200 linhas pré-experimento, v1, 2026-01-05→02-01)  B=— (N=0)  z=n/a p=n/a
Vigiadas: margem_media A=0,32 vs B=—; reclamacoes A=0,50% vs B=—; optout A=1,00% vs B=—; conversao (alvo) A=2,50% vs B=—  — não avaliáveis (B sem linhas)
Conclusão: dados/execucoes.csv tem 0 linhas de variante B (201 linhas, todas A); faltam 166 em B e 166 em A alocadas pelo experimento (mínimo 166/variante do E0001) — a 50/semana em 50/50 = 25/variante/semana, 7 semanas (166/25 = 6,64 → 7); primeiro veredito com N ≥ 166 possível no ciclo de 2026-03-23.
```

Notas:
- As 200 linhas de A são anteriores ao início do experimento (alocação 50/50 por id começa em 2026-02-02) e não contam como N experimental; servem só como baseline (0,17 = 34/200).
- Mínimo usado: 166/variante (dimensionamento aprovado em `decisao-experimento.md`, 0,17 → 0,30). O `experimento.amostra_minima_por_variante: 300` do yaml está desatualizado e não foi usado.
- Nenhuma parada antecipada por guarda-corpo: sem linhas de B, nada a comparar.
