# candidata-vB — H2: Teto de 80 palavras na mensagem
- 2026-02-02 · derivada de `versoes/atual` (v1) com **apenas** a MUDANÇA de H2 (ciclo 0001, APROVADA pelo Guardião, FORÇA FORTE). Nada de H3.

## Hipótese testada (H2)
SE       for acrescentada em Regras a exigência de no máximo 80 palavras no total (e, no item 2 da Estrutura, "2–3 frases" virar "1 frase")
ENTÃO    `taxa_resposta` deve ir de 17,00% (N=200) para ≥ 22%
PORQUE   83% das propostas não geram resposta e o grosso do custo/tempo (≈ 205,7 para 5 conversões; 5,465 min por proposta) é gasto em mensagens sem retorno — FORTE. A estrutura v1 em 5 blocos produz uma mensagem longa para WhatsApp; encurtar reduz o custo de leitura antes do preço e da resposta. Efeito secundário esperado: queda em `custo` e `tempo_min`.
MUDANÇA  Em "Estrutura da mensagem", item 2, trocar "(2–3 frases)" por "(1 frase)". Em "Regras", acrescentar a linha `- Máximo de 80 palavras no total da mensagem.`
FORÇA    FORTE

## Diff contra v1 (2 hunks, nada mais)
```
10c10
< 2. Resumo do que foi avaliado e do procedimento indicado (2–3 frases).
---
> 2. Resumo do que foi avaliado e do procedimento indicado (1 frase).
20a21
> - Máximo de 80 palavras no total da mensagem.
```
