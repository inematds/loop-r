# 01 — Visão de produto: o LOOP-R como ferramenta que "funciona direto"

> Objetivo declarado (Nei, 2026-09-10): *"um framework que funcione direto, onde o usuário dá instruções mínimas, a solução é construída e mantida de forma que o LOOP-R garanta o resultado constante."*

Este documento traduz esse objetivo em um **contrato de produto** — o que a pessoa fornece, o que o sistema constrói, o que ele mantém, e o que ele **garante de verdade** (ver [06-critica-e-viabilidade.md](./06-critica-e-viabilidade.md) para o que ele **não** garante).

---

## 1. A promessa, escrita com cuidado

**Promessa honesta:**

> Você descreve **um processo** e **um número** que quer melhorar. O LOOP-R monta o time de agentes, roda o ciclo *executar → medir → criticar → propor → testar → validar → promover*, guarda tudo o que aprendeu, e **nunca deixa uma versão pior substituir a atual**.

**O que a promessa NÃO diz** (de propósito): "vai melhorar X%". Nenhum sistema honesto promete isso. O que se garante é o **processo** e a **não-regressão** — ver §5.

---

## 2. "Instruções mínimas" — definição exata

Há cinco coisas que **nenhum sistema pode inferir com segurança** e que a pessoa precisa dizer. São o **input mínimo obrigatório**:

| # | Campo | Por que não dá para inferir | Exemplo |
|---|---|---|---|
| 1 | **Objetivo com número** | "Melhorar vendas" não é otimizável. Precisa de métrica + valor atual + valor-alvo | "Conversão de propostas no WhatsApp: 3% → 5%" |
| 2 | **Onde nasce a evidência** | O sistema não adivinha onde o resultado é registrado | "Planilha `vendas.csv`, uma linha por proposta, coluna `fechou` sim/não" |
| 3 | **O que nunca muda sozinho** (guarda-corpos) | Segurança e política são decisões humanas | "Nunca oferecer desconto acima de 10%. Nunca prometer prazo. Nunca contatar quem pediu para sair." |
| 4 | **Teto de custo e tempo** | Quanto se aceita gastar por ciclo é decisão de negócio | "Até R$ 50/semana em IA; ciclo semanal" |
| 5 | **Quem aprova** | Nível de autonomia é escolha humana | "Eu aprovo cada promoção" (L1) |

**Tudo o resto o sistema propõe e a pessoa só confirma:** quais agentes existem, quais métricas secundárias vigiar ("sem piorar"), como comparar versões, cadência do ciclo, formato da memória.

Cinco respostas em linguagem natural. É isso que "mínimo" significa aqui. Menos que isso não é mínimo — é inseguro.

---

## 3. O que o sistema constrói a partir disso

Da resposta às 5 perguntas, o LOOP-R gera automaticamente:

1. **`loop-r.yaml`** — o contrato do loop (spec em [03-spec-loop-r-yaml.md](./03-spec-loop-r-yaml.md)).
2. **9 agentes instanciados** para *este* objetivo — Executor, Observador, Crítico, Otimizador, Experimentador, Avaliador, Guardião, Memória, Meta-agente — cada um com prompt derivado do yaml ([04-agentes.md](./04-agentes.md)).
3. **Versão 1 do processo** (`versoes/v1/`) — o prompt/roteiro/checklist atual do Executor, congelado como linha de base.
4. **Adaptador de dados** — no v0.1, uma planilha/CSV com colunas fixas; a pessoa só preenche ou exporta do sistema que já usa.
5. **Eval inicial** — os critérios de comparação e a regra de amostra mínima ([05-medicao-evals-guardrails.md](./05-medicao-evals-guardrails.md)).
6. **Memória vazia com estrutura** — `memoria/ledger.md` + `memoria/hipoteses/`.

---

## 4. O que o sistema mantém (o "e mantida")

A cada ciclo (diário/semanal, conforme o yaml):

```text
1. Observador lê os dados novos → resumo de evidência
2. Crítico compara com a versão vigente → o que funcionou / falhou
3. Otimizador escreve 1–3 hipóteses testáveis
4. Guardião veta o que fere guarda-corpos ou teto
5. Experimentador desenha o teste (A vs B, amostra mínima)
6. Executor roda A e B pelo período
7. Avaliador decide: B ganhou? por métrica, com margem
8. Se ganhou E humano aprovou (L1) → PROMOVE (vira v2)
   Se empatou ou perdeu → DESCARTA, registra na memória
9. Memória registra tudo. Meta-agente revisa custo e desperdício do ciclo.
```

A manutenção é o próprio loop rodando. Não existe "manutenção" separada do ciclo.

---

## 5. Níveis de autonomia (o que "garante" significa em cada um)

Como nos carros autônomos, a autonomia é gradual e a pessoa escolhe o nível:

| Nível | O que o sistema faz sozinho | O que o humano faz | Quando usar |
|---|---|---|---|
| **L0 — Propõe** | Observa, critica, propõe hipóteses | Decide tudo; roda testes manualmente | Primeiros 2 ciclos, para ganhar confiança |
| **L1 — Testa** *(padrão v1)* | Tudo do L0 + desenha e roda o teste A/B + avalia | **Aprova ou rejeita cada promoção** | Operação normal |
| **L2 — Promove** | Tudo do L1 + promove sozinho quando eval passa; **rollback automático** se métrica cair | Revisa o ledger semanalmente; ajusta guarda-corpos | Só após ≥5 promoções corretas em L1 |
| **L3 — Redesenha** | Meta-agente muda agentes, workflow, modelo | Aprova mudanças estruturais | Pesquisa. Não está no v1. |

**O produto entrega L0 e L1 com certeza. L2 depende de dados em volume. L3 é pesquisa** — detalhes em [06](./06-critica-e-viabilidade.md) e [07-roadmap.md](./07-roadmap.md).

---

## 6. O que "resultado constante" passa a significar

Reescrevendo o objetivo para algo que dá para cumprir:

| Pedido original | O que o LOOP-R garante de fato | Mecanismo |
|---|---|---|
| "resultado constante" | **Não-regressão**: a versão em produção nunca é pior que a anterior por decisão do sistema | Eval + regra de promoção + rollback |
| "garanta" | **Auditabilidade**: toda versão, todo teste, toda decisão tem registro e pode ser revertida | Git como histórico de versões; ledger |
| "mantida" | **Constância de processo**: o ciclo roda toda vez, com os mesmos passos, mesmo que a resposta seja "sem evidência suficiente, não mudo nada" | Runner + manifesto de ciclo |
| "funcione direto" | **Zero configuração além das 5 respostas** | Gerador de yaml + agentes |

A melhoria é **provável** com o tempo (é para isso que o loop existe), mas o que se **garante** é: o sistema não piora por conta própria, não gasta acima do teto, e você sempre sabe por que ele fez o que fez.

---

## 7. Onde roda (decisão assumida)

Você pediu um repo "onde as pessoas apenas informam os dados e ele constrói". Decisão assumida (não bloqueio nela; corrija se quiser outra):

- **v0.1:** o runner é o **Claude Code** — o repo traz uma skill `/loop-r` + os 9 agentes como subagentes. Quem tem Claude Code clona, responde as 5 perguntas, e o loop roda. É o caminho mais curto até "funciona direto" no seu ecossistema.
- **v1:** CLI Python independente (`loopr iniciar` / `loopr ciclo` / `loopr promover` / `loopr reverter`) usando a API da Anthropic — para quem não usa Claude Code.
- **Ambos leem o mesmo `loop-r.yaml` e a mesma pasta `memoria/`.** Detalhes em [02-arquitetura.md](./02-arquitetura.md).

Na apresentação para leigos (curso e guia), nada disso aparece com esses nomes — ver as regras de linguagem em [plano-curso-loop-r.md](./plano-curso-loop-r.md).

---

## 8. Decisões em aberto (respostas em texto, quando quiser)

1. **Interface das 5 perguntas:** conversa no Claude Code (assumido), ou também um formulário web simples que gera o `loop-r.yaml` para baixar?
2. **Primeiro domínio de referência:** vendas por WhatsApp (assumido nos exemplos) — ou atendimento?
3. **Conta GitHub do repo:** `inematds/loop-r` (default do CLAUDE.md), salvo instrução contrária.
