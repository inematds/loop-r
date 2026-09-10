# Aprendizados (provado e promovido)

## Processo

- 2026-04-27 · ciclo 0002 · Tolerância zero em guarda-corpo de evento raro não distingue efeito de ruído. No E0001 (H2, teto de 80 palavras), `reclamacoes` tem tolerância 0,0 no `loop-r.yaml`; B registrou 6/300 (2,00%) vs A 1/300 (0,33%) — viola a tolerância literal, mas com N=300 essa diferença não é estatisticamente significativa (Fisher p≈0,12). O veredito seguiu a regra escrita (`A_SEGUE`, H2 descartada) porque o contrato não permite contorná-la — mas o próprio ajuste registra a falha de desenho. Correção: `loop-r.yaml` → `reclamacoes.tolerancia: 0,0 → 0,01` (≈ 2 erros-padrão de uma taxa de ~1% com N=300), para eventos raros terem piso ≥ ruído esperado na amostra planejada, ou usar teste estatístico ("B não é significativamente pior") em vez de tolerância absoluta. Vale só para os próximos experimentos — E0001 não é reavaliado com a regra nova.

