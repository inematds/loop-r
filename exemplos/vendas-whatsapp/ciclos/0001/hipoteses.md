# Hipóteses — Ciclo 0001 (sobre v1)

Fonte: `ciclos/0001/critica.md`. Métrica de teste: `taxa_resposta` (sinal), atual observado **17,00% (34/200)** — o `atual: 0.20` do `loop-r.yaml` está desatualizado. Conversão (5 eventos em 200) não é testável em um ciclo; fica como métrica de acompanhamento.
Memória (`descartados.md`, `observado-nao-testado.md`) vazia — nenhuma colisão. Nenhuma hipótese toca `guarda_corpos.invariaveis`.

## H1 — Encerrar com uma única pergunta de fechamento
SE       o item 5 da Estrutura ("Encerramento cordial, colocando-se à disposição para dúvidas") for substituído por uma única pergunta de fechamento, neutra, que peça uma resposta concreta da cliente
ENTÃO    `taxa_resposta` deve ir de 17,00% (N=200) para ≥ 25%
PORQUE   166/200 propostas (83%) não geram resposta em 48h — FORTE. O roteiro v1 termina sem pedir nada à cliente ("à disposição para dúvidas"): a mensagem não cria um motivo para responder. A pergunta é sem urgência e sem exclamação para não pressionar a folga zero em `reclamacoes` (tolerância 0,0 — FORTE).
MUDANÇA  Substituir o item 5 da seção "Estrutura da mensagem" por:
         `5. Encerrar com UMA única pergunta de fechamento, neutra e sem urgência, que peça uma escolha concreta — por exemplo: "Prefere começar ainda esta semana ou na próxima?". Nenhuma outra pergunta na mensagem.`
FORÇA    FORTE

## H2 — Teto de 80 palavras na mensagem
SE       for acrescentada em Regras a exigência de no máximo 80 palavras no total (e, no item 2 da Estrutura, "2–3 frases" virar "1 frase")
ENTÃO    `taxa_resposta` deve ir de 17,00% (N=200) para ≥ 22%
PORQUE   83% das propostas não geram resposta e o grosso do custo/tempo (≈ 205,7 para 5 conversões; 5,465 min por proposta) é gasto em mensagens sem retorno — FORTE. A estrutura v1 em 5 blocos (resumo em 2–3 frases + explicação do pacote + valor + formas de pagamento) produz uma mensagem longa para WhatsApp; encurtar reduz o custo de leitura antes do preço e da resposta. Efeito secundário esperado: queda em `custo` e `tempo_min` (estáveis em 1,0283 e 5,465 — FORTE).
MUDANÇA  Em "Estrutura da mensagem", item 2, trocar "(2–3 frases)" por "(1 frase)". Em "Regras", acrescentar a linha:
         `- Máximo de 80 palavras no total da mensagem.`
FORÇA    FORTE

## H3 — Abrir com algo específico da avaliação
SE       o item 1 da Estrutura ("Saudação pelo nome e agradecimento pela visita") for substituído por uma abertura que, já na primeira frase, cite um ponto específico das observações da avaliação daquela cliente
ENTÃO    `taxa_resposta` deve ir de 17,00% (N=200) para ≥ 22%
PORQUE   166/200 sem resposta — FORTE — mas o elo causal é indireto: a crítica mostra que a mensagem não é lida/respondida, não que a abertura genérica seja a causa. A abertura v1 (saudação + agradecimento) é idêntica para todas as clientes e não sinaliza que a proposta foi feita para ela. Marcada MODERADA por isso.
MUDANÇA  Substituir o item 1 da seção "Estrutura da mensagem" por:
         `1. Saudação pelo nome; a primeira frase já cita um ponto específico das observações da avaliação desta cliente (ex.: a queixa que ela trouxe ou a região avaliada). Sem agradecimento genérico pela visita.`
FORÇA    MODERADA

---
Não entram aqui (base só FRACA): ver `memoria/observado-nao-testado.md`, linhas de 2026-02-02.
