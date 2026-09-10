# Decisão — ciclo 0002

**[DECISÃO SIMULADA pelo runner para o exemplo de referência — no uso real quem responde é o aprovador (L1).]**

Veredito do Avaliador: `A_SEGUE` — H2 (teto de 80 palavras) subiu `taxa_resposta` 19,3% → 29,7% (N=300/300, significativo), mas `reclamacoes` ficou fora da tolerância: B 6/300 vs A 1/300, tolerância 0,0.

Decisão: **aceito o veredito. H2 é descartada como testada** — a regra estava escrita assim e o sistema não a contorna.

Aprendizado de processo (fica na memória e nos docs): tolerância **zero** num evento raro (~1%) com N=300 não distingue efeito de ruído — 6 vs 1 em 300 não é estatisticamente diferente (p≈0,12). Guarda-corpo de evento raro precisa de tolerância ≥ piso de ruído na amostra planejada, ou de teste estatístico ("B não é significativamente pior"). Ajuste no `loop-r.yaml`: `reclamacoes.tolerancia: 0.0 → 0.01` (≈ 2 erros-padrão de 1% com N=300). Vale para os próximos experimentos; **não** se reavalia E0001 com a regra nova.

Próximo ciclo: Otimizador pode propor de novo (H3 já aprovada pelo Guardião aguarda teste).

— 2026-04-27 · Nei (simulado)
