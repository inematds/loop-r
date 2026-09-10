# Hipóteses — Ciclo 0003 (sobre v1) · 2026-05-04

Fonte: `ciclos/0003/critica.md`. Métrica de teste: `taxa_resposta` (sinal), atual observado em v1/A todo o período **18,36% (101/550)** — o `atual: 0.20` do `loop-r.yaml` está desatualizado (crítica, §4). Alvo do yaml: **0,30**. Conversão (23 eventos em 550, 4,18%) segue como métrica de acompanhamento — não é testável em um experimento de 166/variante.
Memória: `descartados.md` tem H1 (pergunta de fechamento, VETADA) e H2 (teto de 80 palavras, A_SEGUE por `reclamacoes`). **Nenhuma hipótese abaixo toca o encerramento da mensagem, impõe limite de tamanho ou reformula qualquer das duas.** Nenhuma toca `guarda_corpos.invariaveis` (Regras 2–5 do roteiro ficam intactas). Rótulos H1/H2 estão ocupados no ledger — novas hipóteses começam em H4.

## H3 — Abrir com algo específico da avaliação (reapresentada; aprovada pelo Guardião no ciclo 0001, AGUARDANDO desde 2026-02-02)
SE       o item 1 da Estrutura ("Saudação pelo nome e agradecimento pela visita") for substituído por uma abertura que, já na primeira frase, cite um ponto específico das observações da avaliação daquela cliente
ENTÃO    `taxa_resposta` deve ir de 18,36% (101/550, v1/A todo o período) para ≥ 30% (alvo do yaml); leitura no experimento contra a linha A concorrente, 166/variante
PORQUE   449/550 propostas (81,6%) não geram resposta em 48h em v1/A, em todas as janelas (pré 17,00% · E0001-A 19,33% · pós 18,00%) — FORTE. A abertura v1 é idêntica para todas as clientes desde o início do loop (`aprendizados.md`: nenhum conteúdo de prompt promovido; v1 é o mesmo texto) e não sinaliza que a proposta foi feita para ela. E0001 mostrou que uma mudança só de forma move `taxa_resposta` em +10 pp com significância (B 29,67% vs A 19,33%, z=2,94) — a métrica é sensível ao roteiro. O elo causal específico (abertura genérica → não-resposta) continua indireto: a crítica não traz dado sobre a abertura em si, por isso segue MODERADA. Contexto de processo: a janela pós rodou 50 propostas sem hipótese em teste enquanto esta esperava (capacidade ociosa — FORTE, fato); com E0001 encerrado, não há bloqueio de `max_testes_simultaneos: 1`.
MUDANÇA  Substituir o item 1 da seção "Estrutura da mensagem" por:
         `1. Saudação pelo nome; a primeira frase já cita um ponto específico das observações da avaliação desta cliente (ex.: a queixa que ela trouxe ou a região avaliada). Sem agradecimento genérico pela visita.`
FORÇA    MODERADA

## H4 — Valor e formas de pagamento logo após a saudação (reordenar blocos, sem cortar nada)
SE       o item 4 da Estrutura ("Valor do pacote e formas de pagamento") passar a ser o item 2, e os atuais itens 2 e 3 (resumo da avaliação; como funciona o pacote) descerem para 3 e 4 — os cinco blocos permanecem, com o mesmo texto; só a ordem muda
ENTÃO    `taxa_resposta` deve ir de 18,36% (101/550) para ≥ 30% (alvo do yaml); leitura no experimento contra a linha A concorrente, 166/variante
PORQUE   81,6% sem resposta — FORTE. Em v1 a cliente só chega ao valor depois de dois blocos de explicação (resumo em 2–3 frases + funcionamento do pacote); o diagnóstico de E0001 é que reduzir o custo de leitura antes do preço eleva a resposta (B +10 pp, z=2,94, N=300/300 — FORTE), mas a via testada (teto de 80 palavras) rompeu `reclamacoes` e está descartada. H4 ataca o mesmo custo de leitura por outra via — posição, não tamanho: nada é cortado, o roteiro não ganha limite de palavras e o fechamento (item 5) fica como está. Não há dado direto sobre posição do preço na crítica, por isso MODERADA. Guarda-corpos: `reclamacoes` agora com tolerância 0,01; as reclamações de B vieram de uma mensagem seca (item 2 reduzido a 1 frase) — aqui a explicação continua completa, só depois do valor. Risco a vigiar: `optout` (tol 0,005) se o preço cedo soar abrupto.
MUDANÇA  Substituir a seção "Estrutura da mensagem" por:
         `1. Saudação pelo nome e agradecimento pela visita.`
         `2. Valor do pacote e formas de pagamento (à vista com 5% de desconto, ou em até 6×).`
         `3. Resumo do que foi avaliado e do procedimento indicado (2–3 frases).`
         `4. Explicação de como funciona o pacote: número de sessões, intervalo, o que está incluso.`
         `5. Encerramento cordial, colocando-se à disposição para dúvidas.`
FORÇA    MODERADA

---
Ordem: ambas MODERADA; H3 primeiro por já ter aprovação do Guardião e por ser o objeto direto da "capacidade ociosa" apontada na crítica. Sob `max_testes_simultaneos: 1`, H4 entra na fila.
Não proposta: variante para o segmento `grande` (7,69%, 3/39 — MODERADA por N, mas 3 eventos e pré contradiz com 20,00%, 6/30). Não mira 0,30 (`grande` ≈ 7% da população) e o roteiro não recebe `segmento` na Entrada. Fica como diagnóstico da crítica, não como hipótese.
Nenhuma hipótese nova com base só FRACA neste ciclo — `memoria/observado-nao-testado.md` não recebe linha.
