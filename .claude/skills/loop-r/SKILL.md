---
name: loop-r
description: >-
  LOOP-R — roda um loop de melhoria contínua sobre um processo do negócio: /loop-r iniciar
  (5 perguntas → loop-r.yaml), ciclo (9 agentes → ciclos/NNNN/), decidir (cartão de decisão),
  promover, reverter, status. Use quando o usuário pedir para "iniciar/rodar/montar um loop",
  "rodar um ciclo", "promover/reverter versão", "status do loop", ou mencionar LOOP-R.
---

# /loop-r — runner v0.1 (Claude Code)

Todos os comandos aceitam `--dir <pasta>`; default é a raiz do repo. O diretório do loop é `LOOP_DIR`.
Cada agente é um subagente em `.claude/agents/`. **Sempre passe `LOOP_DIR` e `CICLO` no prompt do subagente.** Não execute o trabalho de um agente no seu lugar — a separação é o mecanismo.

Leia `docs/01-visao-produto.md` §2 e §6 antes do `iniciar` — é o contrato do que se promete.

---

## `iniciar` — 5 perguntas → `loop-r.yaml`

Pergunte **em texto livre, uma de cada vez**, e não avance sem resposta utilizável:

1. **Objetivo com número** — "Qual processo, e qual número quer mover de quanto para quanto?" (precisa de processo + métrica + atual + alvo)
2. **Onde nasce a evidência** — "Onde fica registrado o resultado de cada execução hoje?" (planilha/CSV no v0.1; pergunte volume por semana)
3. **O que nunca muda sozinho** — "O que a IA NUNCA pode mudar por conta própria?" (mínimo 1 invariável) e "O que não pode piorar enquanto melhoramos isso?" (mínimo 1 `sem_piorar`)
4. **Teto** — "Quanto pode gastar de IA por ciclo, e o ciclo é semanal ou mensal?"
5. **Quem aprova** — "Você aprova cada mudança (L1), ou só quer ver propostas (L0)?" (L2 não é permitido no `iniciar`)

Depois:

- **Proponha `metrica_sinal`** (tabela em `docs/05-medicao-evals-guardrails.md` §1–2) e **calcule a amostra mínima** (fórmula em `docs/05` §3). Diga a frase de honestidade: *"Com N/semana, provar X→Y leva ~K semanas. Vou otimizar primeiro <sinal> (~k semanas) e vigiar <alvo>. Confirma?"*
- Gere `LOOP_DIR/loop-r.yaml` conforme `docs/03-spec-loop-r-yaml.md` (§1 obrigatórios + §2 inferidos + §3 metadados) e **valide as 7 regras** de `docs/03` §4. Se falhar, mostre qual e corrija com a pessoa.
- Crie: `versoes/v1/executor.prompt.md` (o roteiro atual, pedido à pessoa ou rascunhado com ela) + `CHANGELOG.md`; `versoes/atual` → `v1` (symlink); `dados/esquema.md` (a partir do template em `templates/esquema.md`, com as colunas das métricas do yaml); `dados/execucoes.csv` só com cabeçalho; `evals/rubrica.md` (a partir de `templates/rubrica.md`, 5–7 critérios sim/não escritos com a pessoa); `memoria/{ledger,aprendizados,descartados,observado-nao-testado}.md` com cabeçalho; `ciclos/` vazio.
- `git add` + commit `loop-r: iniciar <processo>`.

---

## `ciclo` — um ciclo completo

`CICLO` = próximo número de 4 dígitos em `LOOP_DIR/ciclos/`. Crie a pasta e `manifesto.md` com a tabela abaixo. Rode **em sequência**, um subagente por linha; após cada um, anote no manifesto `[OK]`, `[PAROU: motivo]` ou `[PULADO: motivo]` e o arquivo gerado.

| # | Agente | Gera | Para o ciclo se |
|---|---|---|---|
| 1 | observador | `evidencia.md` | `DADOS INCONSISTENTES` |
| 2 | critico | `critica.md` | `CICLO INTERROMPIDO` |
| 3 | otimizador | `hipoteses.md` (+ `memoria/observado-nao-testado.md`) | — |
| 4 | guardiao | `guardiao.md` | — (zero aprovadas ⇒ 5 escreve `SEM EXPERIMENTO`) |
| 5 | experimentador | `experimento.md`, `evals/amostra-minima.md`, `versoes/candidata-vB/` | — |
| 6 | *(mundo real)* | linhas novas em `dados/execucoes.csv` | o Executor roda quando há tarefa; no ciclo, só registre quantas linhas entraram |
| 7 | avaliador | `veredito.md` | `JUIZ DESCALIBRADO` |
| 8 | *(humano, se L1 e `B_GANHOU`)* | `decisao.md` via `decidir` | — |
| 9 | memoria | `memoria/*.md` | — |
| 10 | meta-agente | `relatorio-meta.md` | — |

Regras do orquestrador:
- Se há experimento em andamento (veredito anterior `AMOSTRA_INSUFICIENTE`), 3–5 são pulados (`[PULADO: experimento em andamento]`) — um teste por vez — e vai direto ao 7.
- Custo: estime tokens de cada subagente e registre em `ciclos/CICLO/custo.md`; se passar de `teto.custo_por_ciclo_brl`, pare e registre `[PAROU: teto]`.
- `B_GANHOU` em L1 ⇒ mostre o cartão (`decidir`) e **não promova sem `decisao.md = aprovado`**. Sem resposta em `prazo_decisao_dias` ⇒ `PENDENTE`, não promove.
- `B_GANHOU` em L2 ⇒ `promover` automático (só se o yaml passou na regra 5 de validação).
- Atualize `meta_info.ciclos_rodados` no yaml. Commit `loop-r: ciclo CICLO — <veredito>`.
- Ciclo sem manifesto 100% preenchido **não conta**.

---

## `decidir` — cartão de decisão (5 linhas)

Leia `experimento.md` + `veredito.md` + `custo.md` do ciclo e mostre:

```
CICLO <n> — hipótese: "<título>"
Resultado:   <métrica> <A> → <B>  (N = <a> vs <b>, z=<..>, p=<..>)
Vigiado:     <cada sem_piorar: ok / caiu>
Custo:       R$ <x> neste ciclo (teto R$ <t>)
Decisão:     aprovar / rejeitar / esperar mais dados
```

Registre a resposta da pessoa em `ciclos/CICLO/decisao.md` (`aprovado | rejeitado | esperar — <data> — <nome>`). `aprovado` ⇒ rode `promover`. `rejeitado` ⇒ Memória classifica como descartada.

---

## `promover` — nova versão oficial

Pré-condições: `veredito = B_GANHOU` **e** (`decisao = aprovado` ou L2). Senão, recuse dizendo qual falta.

1. `N+1` = próximo número em `versoes/`. `cp -r versoes/candidata-vB versoes/vN+1`; `CHANGELOG.md` com hipótese, números, ciclo.
2. `ln -sfn vN+1 versoes/atual`. Remova `candidata-vB`.
3. `meta_info.versao_atual`, `ultima_promocao` no yaml. Linha no ledger `PROMOVIDA vN+1`.
4. Commit `loop-r: promote vN+1 — <hipótese>`.

---

## `reverter` — rollback

1. Descubra a versão anterior pelo ledger (última `PROMOVIDA` antes da atual). `ln -sfn vN-1 versoes/atual`.
2. Linha no ledger `ROLLBACK vN → vN-1 — <motivo>` (peça o motivo se não vier).
3. Commit `loop-r: rollback vN → vN-1`. A pasta `vN` **fica** — memória.

Gatilho automático (só L2): no primeiro ciclo após promoção, se métrica do teste ou qualquer `sem_piorar` cair abaixo da versão anterior além da tolerância.

---

## `status`

Uma tela: versão atual, ciclos rodados, experimento em andamento (N acumulado / mínimo, semanas restantes), promoções × descartes, custo acumulado, último alerta do meta-agente, decisão pendente se houver.

---

## Invariantes do runner

- Nunca escrever nos arquivos de um agente no lugar dele.
- Nunca promover sem `B_GANHOU` + aprovação.
- Nunca apagar ciclo, versão ou linha de memória.
- Nunca dois experimentos ao mesmo tempo.
- Toda ação que muda `versoes/atual` gera commit.
