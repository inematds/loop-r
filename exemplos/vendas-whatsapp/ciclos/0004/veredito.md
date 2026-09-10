VEREDITO: B_GANHOU
Métrica do teste: taxa_resposta  A=0,1933 (N=300)  B=0,2933 (N=300)  z=2,8543 p=0,0043 (bicaudal; unicaudal p=0,0022; z crítico 95% = 1,9600)
Vigiadas: margem_media A=0,3178 (N=9) vs B=0,3245 (N=11), Δ=+0,0068, tol 0,01 → DENTRO (B não piorou) · reclamacoes A=0,0067 (2/300) vs B=0,0133 (4/300), Δ=+0,0067, tol 0,01 → DENTRO · optout A=0,0100 (3/300) vs B=0,0033 (1/300), Δ=−0,0067, tol 0,005 → DENTRO (B melhorou)
Conclusão: B supera A em taxa_resposta com significância (z=2,85 > 1,96; p=0,0043 < 0,05), N ≥ 212 nas duas variantes, e nenhuma sem_piorar excedeu a tolerância → promover candidata-vB.

---

Ciclo 0004 (2026-07-27). Experimento: E0002 (H3 — abrir com algo específico da avaliação), `ciclos/0003/experimento.md`. Em andamento desde 2026-05-04. Amostra mínima: 212/variante. Confiança: 0,95.

Fonte: `dados/execucoes.csv`, só período do experimento (data ≥ 2026-05-04), recalculado direto do CSV — bate com `ciclos/0004/evidencia.md` §b em todas as contagens.

## Conta (Python, teste z para duas proporções, variância agrupada)

```
p_A = 58/300 = 0,1933      p_B = 88/300 = 0,2933
p̄  = (58+88)/600 = 0,2433
SE  = √[p̄(1−p̄)(1/300 + 1/300)] = √[0,2433·0,7567·0,006667] = 0,0350
z   = (0,2933 − 0,1933) / 0,0350 = 2,8543
p bilateral = 2·(1 − Φ(2,8543)) = 0,0043      p unilateral = 0,0022
z_crit (α=0,05 bilateral) = 1,9600 → rejeita H0
```

Diferença observada: +10,00 pp (esperado no dimensionamento: +11,64 pp, 0,1836 → 0,30). B ficou em 0,2933, abaixo do alvo de 0,30 da `metrica_sinal`, mas o teste é de superioridade sobre A, não de atingir o alvo — e a superioridade é significativa.

## Vigiadas (`guarda_corpos.sem_piorar` do yaml atual), A vs B no período do experimento

| vigiada | tolerância | A | B | B − A | piorou além da tol.? |
|---|---|---|---|---|---|
| margem_media (`margem`, só resultado=sim) | 0,01 | 0,3178 (N=9) | 0,3245 (N=11) | +0,0068 | não (subiu) |
| reclamacoes (`reclamou`) | 0,01 | 0,0067 (2/300) | 0,0133 (4/300) | +0,0067 | não (0,0067 < 0,01) |
| optout (`optout`) | 0,005 | 0,0100 (3/300) | 0,0033 (1/300) | −0,0067 | não (caiu) |

Observações de registro (não alteram o veredito):
- `reclamacoes` em B está +0,0067 acima de A — dentro da tolerância de 0,01, mas com 2/3 dela consumida; 4 vs 2 eventos em 300 é ruído de evento raro (a tolerância foi ajustada no ciclo 0002 exatamente por isso). Item a vigiar no 1º ciclo pós-promoção (gatilho de rollback do yaml). Também não disparou a parada antecipada do experimento (+0,01).
- `margem_media` compara N=9 vs N=11 pacotes pagos — base pequena; sinal fraco em qualquer direção.
- `conversao` (métrica alvo): A 3,00% (9/300) vs B 3,67% (11/300) — não testável neste N (ver experimento.md); só registro.

Sem `dados/calibracao.csv` e sem rubrica aplicável: métrica objetiva (coluna `resposta`), sem julgamento subjetivo — calibração não se aplica.
