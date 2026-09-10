# 05 — Medição, evals e guarda-corpos

"Evals são o coração do LOOP-R." Este documento diz como medir de um jeito que aguente a crítica de [06](./06-critica-e-viabilidade.md): amostra pequena, Goodhart, juiz que deriva, ruído.

---

## 1. Três tipos de métrica, três velocidades

| Tipo | Exemplo | Quem responde | Velocidade | Papel no loop |
|---|---|---|---|---|
| **Dinheiro** | conversão, ticket, margem | o cliente, semanas depois | lenta (meses para provar) | métrica-alvo de longo prazo; vira `sem_piorar` enquanto não há volume |
| **Sinal** | taxa de resposta, agendamento, clique útil | o cliente, em horas/dias | média (semanas) | o que o loop otimiza de verdade no começo |
| **Artefato** | proposta cumpre a rubrica? sem erro factual? tom certo? | o juiz + calibração humana | rápida (minutos) | onde o loop gira toda semana sem esperar ninguém |

**Regra:** o `/loop-r iniciar` sempre propõe uma métrica de cada tipo. O teste roda sobre a mais rápida que ainda tem relação causal plausível com a de dinheiro.

---

## 2. Guarda-corpos: "maximizar X sem piorar Y, Z, W"

Toda métrica-alvo vem acompanhada de pelo menos uma `sem_piorar`. Sugestões por domínio, que o gerador propõe:

| Domínio | Maximizar | Sem piorar |
|---|---|---|
| Vendas | taxa de resposta / conversão | margem média, reclamações, opt-out, desconto médio |
| Atendimento | resolução no 1º contato | satisfação (CSAT), reabertura em 7 dias, tempo do cliente |
| Conteúdo | cliques úteis | tempo na página, descadastro, denúncias |
| Software | bugs fechados por semana | bugs reabertos, cobertura de testes, tempo de build |

**Como o Avaliador aplica:** B só ganha se melhora X **e** nenhuma `sem_piorar` cai além da `tolerancia`. Se X sobe 40% e a margem cai 1% com tolerância 0 → `A_SEGUE`. Sem exceção.

**Tolerância em evento raro (aprendido no exemplo, ciclo 0002):** `tolerancia: 0` só faz sentido para métricas contínuas com N grande. Para eventos raros (reclamação ~1%, opt-out ~0,5%), com N=300 por variante, 6 vs 1 ocorrências **não é diferença** (p≈0,12) — é ruído, e tolerância zero descarta hipóteses boas por acaso. Regra do gerador: tolerância de evento raro ≥ **2 erros-padrão da taxa-base na amostra planejada** — `2·√(p(1−p)/N)`; a 1% e N=300 dá ≈0,011 → `tolerancia: 0.01`. Alternativa mais rigorosa (v0.2): o Avaliador testa "B não é significativamente pior" em vez de comparar com um número fixo.

---

## 3. Amostra mínima — a conta que o Experimentador mostra

Para duas proporções (A vs B), confiança 95%, poder 80%:

| De → para | Por variante | Total | Com 50/semana | Com 200/semana |
|---|---|---|---|---|
| 3% → 5% | ~1.500 | ~3.000 | 60 semanas | 15 semanas |
| 3% → 6% | ~700 | ~1.400 | 28 semanas | 7 semanas |
| 20% → 30% | ~300 | ~600 | 12 semanas | 3 semanas |
| 20% → 35% | ~140 | ~280 | 6 semanas | 1,5 semana |
| 50% → 65% | ~170 | ~340 | 7 semanas | 2 semanas |

(Fórmula padrão do teste z para duas proporções; o Experimentador recalcula para cada caso e grava em `evals/amostra-minima.md`.)

**Leitura:** métricas perto de 3% são quase impossíveis de otimizar diretamente em empresa pequena. Métricas perto de 20–50% (resposta, agendamento) são o terreno realista. O produto diz isso na primeira tela.

**Regra dura:** `N < mínimo ⇒ AMOSTRA_INSUFICIENTE`. Sem "mas está ganhando".

**Parada antecipada:** só por guarda-corpo caindo. Nunca por vantagem parcial — parar cedo quando "está ganhando" é a forma mais comum de promover ruído.

---

## 4. Eval de artefato: rubrica binária

`evals/rubrica.md` — critérios que respondem **sim/não**. Nunca nota de 1 a 10.

Exemplo (proposta comercial por WhatsApp):

```text
R1  Tem no máximo 80 palavras?                                   sim/não
R2  A primeira frase menciona algo específico do cliente?         sim/não
R3  Tem exatamente UMA pergunta de fechamento?                    sim/não
R4  Não promete prazo? (invariável)                               sim/não
R5  Desconto, se houver, ≤ 10%? (invariável)                      sim/não
R6  Não contém erro factual sobre o produto (conferido na base)?  sim/não
R7  Tom: sem exclamação dupla, sem "imperdível", sem caps?        sim/não
```

Pontuação = quantidade de "sim". Versão B "ganha no artefato" se, nos `evals/casos/` (20–50 entradas), tem média ≥ A + 1 critério **e** não perde em R4–R6 (invariáveis) em nenhum caso.

---

## 5. O juiz: como impedir que ele derive

| Problema | Regra |
|---|---|
| Prefere o segundo / o mais longo | pares em **ordem embaralhada**, 3 repetições, maioria |
| Aprova o próprio estilo | Avaliador em modelo diferente do Otimizador quando o teto permitir; rubrica binária limita o gosto |
| Muda de opinião entre semanas | **calibração**: `dados/calibracao.csv` com 10–20 artefatos que a pessoa avaliou uma vez (0/1 por critério). A cada ciclo, o juiz avalia esses mesmos casos; concordância < 80% ⇒ `JUIZ DESCALIBRADO`, ciclo não promove, Meta-agente alerta |
| Rubrica ambígua | critério que dá < 80% de concordância humano×juiz na calibração é reescrito ou removido |

Custo da calibração para a pessoa: **20 minutos, uma vez** (marcar sim/não em 15 exemplos). É o único trabalho manual de medição que o produto pede.

---

## 6. Ruído × padrão

O Crítico rotula toda afirmação:

| Força | Condição | O que acontece |
|---|---|---|
| FORTE | N ≥ 3 × `n_minimo_para_padrao` (default 90) | vira hipótese prioritária |
| MODERADA | N ≥ `n_minimo_para_padrao` (default 30) | vira hipótese |
| FRACA | N < 30 | vai para `memoria/observado-nao-testado.md`; re-examinada quando N crescer |

Segmentação (por porte, canal, horário) só com N ≥ 30 **por segmento**. "Terça converte mais" com 12 propostas não existe.

---

## 7. Promoção e rollback — os limiares

**Promover (L1):** `veredito = B_GANHOU` **e** `decisao.md = aprovado` dentro de `prazo_decisao_dias`. Sem resposta ⇒ não promove; o ledger registra "pendente".

**Promover (L2):** `B_GANHOU` ⇒ promove sozinho. Pré-requisito: ≥5 promoções em L1 sem rollback.

**Rollback:** no primeiro ciclo após uma promoção, se a métrica do teste ou qualquer `sem_piorar` cair abaixo do valor da versão anterior além da tolerância ⇒ `atual` volta, commit, ledger com motivo. Em L1, o cartão de decisão avisa e pede confirmação; em L2, automático e notifica.

**Cartão de decisão** (o que o humano vê em L1 — 5 linhas, uma vez por semana no máximo):

```text
CICLO 0003 — hipótese: "mensagens com até 80 palavras"
Resultado:   taxa de resposta 20% → 29%  (N = 312 vs 310, margem ok)
Vigiado:     margem média igual · reclamações 0 · opt-out 1 vs 1
Custo:       R$ 41 neste ciclo (teto R$ 50)
Decisão:     [aprovar]  [rejeitar]  [esperar mais 2 semanas]
```

---

## 8. O que NÃO medir

- Nada que a pessoa não consiga explicar em uma frase.
- Nada que dependa de um sistema ao qual o loop não tem acesso.
- Nada com menos de 30 observações por período — vai para "observado, não testado".
- "Qualidade geral" sem rubrica. Se não dá para virar sim/não, ainda não é métrica.
