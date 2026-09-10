# FALHAS — loop-r

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-09-10 | Crítico (ciclo 0004) flagrou: linhas `variante=B` de E0001 e E0002 indistinguíveis no CSV → tabelas 'todo o período' inválidas | coluna `experimento` no esquema (template + docs 02); Observador agrupa por ela | prompt |
| 2026-09-10 | CSV sintético (seed 42) saiu com A=24% vs desenho 20% → ciclo 2 daria A_SEGUE por variância, não por conteúdo | gerador com `--seed2` para as semanas ≥5 (mantém semanas 1–4 do ciclo 0001) + busca de seed cuja amostra reflete as taxas desenhadas; documentado no docstring | infra |
| 2026-09-10 | Otimizador estimou efeito pequeno (17→22%) → Experimentador calculou 40 semanas > teto e parou | não foi bug: escalou para o aprovador como previsto; runner sincronizou o yaml (300→166) após a decisão. Regra fixada no agente experimentador: dimensionar pelo `alvo` do yaml, não pela expectativa do Otimizador | prompt |
