# candidata-vB — H3: Abrir com algo específico da avaliação
- 2026-05-04 · derivada de `versoes/atual` (v1) com **apenas** a MUDANÇA de H3 (ciclo 0003, APROVADA pelo Guardião, FORÇA MODERADA). Substitui a candidata-vB anterior (H2 / E0001, encerrada com `A_SEGUE` no ciclo 0002). Nada de H4 (vetada).

## Hipótese testada (H3)
SE       o item 1 da Estrutura ("Saudação pelo nome e agradecimento pela visita") for substituído por uma abertura que, já na primeira frase, cite um ponto específico das observações da avaliação daquela cliente
ENTÃO    `taxa_resposta` deve ir de 18,36% (101/550, v1/A todo o período) para ≥ 30% (alvo do yaml)
PORQUE   81,6% das propostas v1/A não geram resposta em 48h, em todas as janelas — FORTE. A abertura v1 é idêntica para todas as clientes e não sinaliza que a proposta foi feita para ela. E0001 mostrou que uma mudança só de forma move `taxa_resposta` em +10 pp com significância — a métrica é sensível ao roteiro. Elo causal específico ainda indireto → MODERADA.
MUDANÇA  Substituir o item 1 da seção "Estrutura da mensagem" pelo texto abaixo (diff).
FORÇA    MODERADA

## Diff contra v1 (1 hunk, nada mais)
```
9c9
< 1. Saudação pelo nome e agradecimento pela visita.
---
> 1. Saudação pelo nome; a primeira frase já cita um ponto específico das observações da avaliação desta cliente (ex.: a queixa que ela trouxe ou a região avaliada). Sem agradecimento genérico pela visita.
```
