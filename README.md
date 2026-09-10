# 🔁 LOOP-R — Framework para Sistemas e Empresas Autoaperfeiçoáveis

> Não peça para a IA melhorar. Faça cada execução produzir evidência, cada evidência gerar uma hipótese, cada hipótese virar um experimento — e só o que for comprovado entrar na próxima versão.

O LOOP-R transforma um processo do seu negócio (propostas, atendimento, conteúdo…) em um **loop de melhoria com registro e botão de voltar**: 9 assistentes de IA com funções separadas executam, medem, criticam, propõem, testam, julgam, guardam a memória e vigiam o próprio custo — e **nenhuma versão pior substitui a atual por decisão do sistema**.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/loop-r/guia/**

## O que ele garante (e o que não)

| Garante | Não garante |
|---|---|
| **Não-regressão** — versão pior nunca entra | que o número sobe |
| **Auditabilidade** — toda versão, teste e decisão registrados; `reverter` em um comando | que cada ciclo gere uma hipótese boa |
| **Constância de processo** — o ciclo roda toda vez, do mesmo jeito | que o custo compense sem você olhar |
| **Teto de custo** — para quando atinge | — |

Leia [docs/06-critica-e-viabilidade.md](docs/06-critica-e-viabilidade.md) antes de esperar mais que isso.

## Começar (Claude Code)

```bash
git clone https://github.com/inematds/loop-r && cd loop-r
claude
> /loop-r iniciar
```

O `iniciar` faz **5 perguntas** e monta tudo:

1. Qual processo, e qual número mover de quanto para quanto?
2. Onde fica registrado o resultado de cada execução? (planilha)
3. O que a IA nunca pode mudar sozinha? O que não pode piorar?
4. Quanto pode gastar por ciclo? Semanal ou mensal?
5. Você aprova cada mudança (L1) ou só quer ver propostas (L0)?

Depois:

```
/loop-r ciclo      # roda os 9 agentes → ciclos/NNNN/
/loop-r decidir    # cartão de 5 linhas: aprovar / rejeitar / esperar
/loop-r promover   # a candidata vira a versão oficial (commit)
/loop-r reverter   # volta a anterior (commit)
/loop-r status
```

## Estrutura

```
loop-r.yaml          ficha do loop (5 respostas + inferidos)         docs/03
.claude/agents/      9 agentes: o que lê, escreve, decide, nunca faz  docs/04
.claude/skills/loop-r/  o runner (/loop-r ...)
versoes/             v1, v2… + atual → vN  (git = promoção/rollback)
dados/               execucoes.csv (adaptador universal) + esquema
evals/               rubrica sim/não, amostra mínima, casos
ciclos/NNNN/         manifesto + saída de cada agente + decisão
memoria/             ledger, aprendizados, descartados, observado-não-testado
exemplos/vendas-whatsapp/   loop completo de referência (3 ciclos rodados)
docs/                visão, crítica, arquitetura, spec, agentes, medição, roadmap, curso
```

## Exemplo que já rodou

[`exemplos/vendas-whatsapp/`](exemplos/vendas-whatsapp/) — clínica de estética, propostas por WhatsApp, 1.500 linhas sintéticas, 3 ciclos: uma hipótese promovida (v2), uma descartada, uma com amostra insuficiente. Leia `memoria/ledger.md` e os `ciclos/*/manifesto.md`.

## Documentação

[docs/README.md](docs/README.md) — comece pela **visão** (01) e pela **crítica** (06).

## Versão

`0.1.0` — runner Claude Code, adaptador CSV, L0/L1, meta-agente em modo relatar. Roadmap em [docs/07-roadmap.md](docs/07-roadmap.md).

---

INEMA · [inema.club](https://inema.club) · [inema.pro](https://inema.pro)
