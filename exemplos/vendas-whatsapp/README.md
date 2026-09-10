# Exemplo de referência — vendas por WhatsApp (clínica de estética)

Leia isto antes de abrir `memoria/ledger.md` ou os `ciclos/*/`. O produto promete honestidade; este exemplo tem que começar por ela.

## O que é real

- **Os 9 agentes rodaram de verdade.** Cada arquivo em `ciclos/000N/` (evidência, crítica, hipóteses, veto, experimento, veredito, relatório-meta) é a saída **não editada** do agente correspondente, rodando com o contrato de `.claude/agents/*.md`. Os achados — o Guardião vetando duas hipóteses, o Experimentador escalando um desenho de 40 semanas, o Avaliador reprovando um ganho de 10 pontos por um guarda-corpo, o Crítico apontando a coluna `experimento` que faltava — aconteceram, não foram roteirizados.
- **Os manifestos e o ledger** refletem o que cada ciclo fez, na ordem em que fez.

## O que é simulado

- **Os dados são sintéticos.** `dados/execucoes.csv` (1.500 linhas) vem de `../../ferramentas/gerar_csv_sintetico.py`, com três seeds fixos. **Os seeds foram escolhidos para que a amostra refletisse os efeitos desenhados** (v1 ≈ 20% de resposta, candidatas ≈ 29%, guarda-corpos dentro da tolerância). Ou seja: este exemplo ilustra *como o loop se comporta diante de um efeito verdadeiro* — ele não descobriu um efeito. Numa operação real não existe essa escolha; o que aparece é o que os dados disserem.
- **As decisões humanas (nível L1)** — `ciclos/0001/decisao-experimento.md`, `ciclos/0002/decisao.md`, `ciclos/0004/decisao.md` — foram escritas pelo runner, para o exemplo avançar, e estão marcadas como **simuladas**. No uso real, quem responde ao cartão é o aprovador.
- **O Executor não produziu artefatos.** O CSV faz o papel do mundo (as propostas "foram enviadas" e "responderam" segundo o gerador). Numa operação real, o Executor escreve a proposta e a pessoa/conector registra o resultado.
- **`metrica_alvo.atual: 0.03`** no yaml é o número *declarado* pela pessoa fictícia; o observado no CSV foi 2,5% — o Crítico apontou a divergência no ciclo 0001, como deve.

## O que os quatro ciclos mostram

| Ciclo | Data (no loop) | O que aconteceu |
|---|---|---|
| 0001 | 2026-02-02 | 3 hipóteses; H1 vetada (escolha forçada pressiona reclamações); H2 (≤80 palavras) desenhada — depois de o Experimentador escalar que, pela expectativa do Otimizador, o teste levaria 40 semanas; humano redimensionou pelo alvo do yaml |
| 0002 | 2026-04-27 | H2: resposta 19,3% → 29,7% (N=300/300, p=0,003) **mas** reclamações 6 vs 1 com tolerância 0 → `A_SEGUE`, descartada. Lição: tolerância zero em evento raro é ruído — ajustada para 0,01 nos próximos testes |
| 0003 | 2026-05-04 | H3 (abrir citando a avaliação) reapresentada e desenhada (212/variante); H4 vetada (antecipar preço) |
| 0004 | 2026-07-27 | H3: resposta 19,3% → 29,3% (N=300/300, p=0,004), guarda-corpos dentro → `B_GANHOU`, aprovada, **promovida v2**. Conversão não se moveu (3,7% vs 3,0%, n.s.): o elo sinal→alvo segue não provado |

Custo total dos quatro ciclos: ≈ 1,7 milhão de tokens (em `ciclos/*/custo.md`).

## Como reproduzir a linha do tempo

```bash
python3 ../../ferramentas/gerar_csv_sintetico.py --ate 2026-02-01 --out dados/execucoes.csv   # ciclo 0001
python3 ../../ferramentas/gerar_csv_sintetico.py --ate 2026-04-26 --out dados/execucoes.csv   # ciclo 0002
python3 ../../ferramentas/gerar_csv_sintetico.py --ate 2026-05-03 --out dados/execucoes.csv   # ciclo 0003
python3 ../../ferramentas/gerar_csv_sintetico.py --ate 2026-07-26 --out dados/execucoes.csv   # ciclo 0004
```

Depois, `/loop-r ciclo --dir exemplos/vendas-whatsapp` a cada passo. Os agentes vão produzir saídas diferentes das que estão aqui (são modelos, não scripts) — e é esse o ponto.
