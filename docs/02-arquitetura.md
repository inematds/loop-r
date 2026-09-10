# 02 — Arquitetura do repo `loop-r`

Como o LOOP-R vira software que "funciona direto". Decisões tomadas a partir da crítica em [06](./06-critica-e-viabilidade.md).

---

## 1. Princípios de desenho

1. **Arquivos, não banco.** Tudo é texto versionado em git: yaml, prompts, CSV, ledger. Qualquer pessoa abre, lê e edita. Sem servidor, sem infra.
2. **Git é o mecanismo de promoção e rollback.** Cada versão do processo é um commit em `versoes/`. Promover = a nova pasta vira `versoes/atual` (symlink ou cópia + commit). Reverter = `git revert`. Não construímos versionamento — usamos o que existe há 20 anos.
3. **O ciclo é um manifesto, não um script mágico.** Cada ciclo gera `ciclos/NNNN/manifesto.md` com o que cada agente leu, decidiu, e por quê. Ciclo sem manifesto completo não conta.
4. **Um adaptador de dados primeiro.** CSV com colunas contratuais. Conectores depois.
5. **O runner é substituível.** v0.1 = Claude Code (skill + subagentes). v1 = CLI Python. Ambos obedecem ao mesmo yaml e à mesma estrutura de pastas.

---

## 2. Estrutura do repositório

```text
loop-r/
├── README.md                    # o que é, 5 perguntas, como rodar
├── loop-r.yaml                  # contrato do loop (gerado das 5 perguntas)  → 03
├── .claude/
│   ├── skills/loop-r/SKILL.md   # /loop-r iniciar | ciclo | promover | reverter | status
│   └── agents/                  # 9 subagentes, um .md cada                  → 04
│       ├── executor.md
│       ├── observador.md
│       ├── critico.md
│       ├── otimizador.md
│       ├── experimentador.md
│       ├── avaliador.md
│       ├── guardiao.md
│       ├── memoria.md
│       └── meta-agente.md
├── versoes/
│   ├── v1/                      # linha de base: prompt/roteiro do Executor
│   │   ├── executor.prompt.md
│   │   └── CHANGELOG.md
│   ├── v2/ ...
│   ├── candidata-vB/            # variante em teste (criada pelo Experimentador)
│   └── atual -> v1              # ponteiro para a versão em produção
├── dados/
│   ├── esquema.md               # colunas do CSV, definição exata de cada métrica
│   ├── execucoes.csv            # 1 linha por execução (o adaptador universal)
│   └── calibracao.csv           # 10–20 exemplos avaliados pela pessoa (juiz)
├── evals/
│   ├── rubrica.md               # critérios binários de qualidade do artefato
│   ├── amostra-minima.md        # tabela calculada pelo Experimentador
│   └── casos/                   # casos de teste do artefato (20–50)
├── ciclos/
│   ├── 0001/
│   │   ├── manifesto.md         # o que aconteceu no ciclo, agente por agente
│   │   ├── evidencia.md         # saída do Observador
│   │   ├── critica.md
│   │   ├── hipoteses.md
│   │   ├── experimento.md
│   │   ├── veredito.md          # saída do Avaliador (3 respostas possíveis)
│   │   └── decisao.md           # humano: aprovado / rejeitado / esperar
│   └── 0002/ ...
├── memoria/
│   ├── ledger.md                # cronológico: toda decisão, 1 linha cada
│   ├── aprendizados.md          # o que ficou provado (promovido)
│   ├── descartados.md           # o que foi testado e perdeu (não re-testar)
│   └── observado-nao-testado.md # hipóteses fracas, aguardando volume
├── exemplos/
│   └── vendas-whatsapp/         # loop completo de referência: yaml + CSV sintético + 3 ciclos
├── guia/                        # landing + guia de uso (GitHub Pages)     → skill projetos-landing-guia
├── curso/                       # curso v5 (1 curso.html por trilha)       → plano-curso
├── docs/                        # estes documentos
└── cli/                         # v1: runner Python independente (loopr)
```

---

## 3. Fluxo de um ciclo

```text
                ┌──────────────────────────────────────────────┐
                │  loop-r.yaml  +  versoes/atual  +  memoria/  │  (contexto de todo agente)
                └──────────────────────────────────────────────┘
                                      │
 dados/execucoes.csv ──► OBSERVADOR ──► evidencia.md
                                      │
                          CRÍTICO ────► critica.md  (funcionou / falhou / N suficiente?)
                                      │
                        OTIMIZADOR ───► hipoteses.md (1–3, com força da evidência)
                                      │
                          GUARDIÃO ───► veta / aprova cada hipótese (guarda-corpos, teto)
                                      │
                     EXPERIMENTADOR ──► experimento.md (A vs B, amostra mínima, duração)
                                      │
                          EXECUTOR ───► roda A e B  →  novas linhas em execucoes.csv
                                      │
                         AVALIADOR ───► veredito.md ∈ { B_GANHOU, A_SEGUE, AMOSTRA_INSUFICIENTE }
                                      │
              ┌───────────────────────┼─────────────────────────┐
         B_GANHOU               A_SEGUE               AMOSTRA_INSUFICIENTE
              │                       │                         │
    L1: humano decide        memoria/descartados      continua o teste
    L2: promove sozinho               │               (próximo ciclo)
              │                       │
      versoes/vN+1 + atual→vN+1       │
      git commit "promote vN+1"       │
              └───────────┬───────────┘
                       MEMÓRIA ───► ledger.md, aprendizados.md
                          │
                     META-AGENTE ──► relatório: custo, taxa de promoção, vetos, deriva do juiz
                                    (v0.1/v1: só relata; nunca age)
```

**Rollback** (manual em L1, automático em L2): se a métrica-alvo ou qualquer guarda-corpo cair abaixo do limiar por 1 ciclo após uma promoção → `atual` volta para a versão anterior, commit `rollback vN+1 → vN`, linha no ledger com o motivo.

---

## 4. Contratos entre agentes (resumo; detalhe em [04](./04-agentes.md))

| Agente | Lê | Escreve | Decide | Nunca faz |
|---|---|---|---|---|
| Executor | `versoes/atual`, entrada da tarefa | artefato + linha no CSV | nada | mudar o próprio prompt |
| Observador | CSV, esquema | `evidencia.md` | nada | interpretar causa |
| Crítico | evidência, versão atual, memória | `critica.md` | se há padrão com N suficiente | propor solução |
| Otimizador | crítica, memória (descartados!) | `hipoteses.md` | nada | repetir hipótese descartada |
| Guardião | hipóteses, yaml (guarda-corpos, teto) | veto/aprovação por hipótese | **veto é final** | ser convencido |
| Experimentador | hipóteses aprovadas, amostra mínima | `experimento.md` | desenho do teste | rodar sem N calculado |
| Avaliador | resultados A/B, rubrica, calibração | `veredito.md` | uma das 3 respostas | "parece melhor" |
| Memória | tudo do ciclo | ledger + 3 arquivos | nada | apagar registro |
| Meta-agente | manifestos de todos os ciclos | `relatorio-meta.md` | nada (v0.1/v1) | alterar agentes |

---

## 5. Onde roda

### v0.1 — Claude Code (skill + subagentes)

```text
/loop-r iniciar    → faz as 5 perguntas, gera loop-r.yaml, versoes/v1, dados/esquema.md, agentes
/loop-r ciclo      → executa o fluxo §3, um agente por subagente, grava ciclos/NNNN/
/loop-r decidir    → mostra o cartão de decisão (5 linhas), registra decisao.md
/loop-r promover   → cria versoes/vN+1, move atual, commit
/loop-r reverter   → git revert da última promoção, ledger
/loop-r status     → última versão, ciclos rodados, taxa de promoção, custo acumulado
```

Vantagem: zero código para funcionar; os agentes são markdown. Quem tem Claude Code clona e roda.
Limite: precisa de Claude Code; ciclo é disparado por pessoa (sem cron no v0.1).

### v1 — CLI Python (`cli/loopr`)

Mesmos comandos, mesmo yaml, mesma pasta. Usa a API da Anthropic; pode rodar em cron. Modelos por agente configuráveis no yaml (leitura em modelo pequeno, raciocínio em modelo maior — ver [06 §6](./06-critica-e-viabilidade.md)).

---

## 6. Adaptador de dados (v0.1: CSV)

`dados/esquema.md` é gerado do yaml e diz exatamente:

```text
coluna          tipo       obrigatória   definição
id              texto      sim           identificador único da execução
data            AAAA-MM-DD sim
versao          v1|v2...   sim           qual versão do Executor gerou
variante        A|B        sim           quando em experimento
experimento     E0001…     sim se B      qual teste gerou a linha (B de testes diferentes nunca se misturam)
segmento        texto      não           ex.: porte do cliente, canal
resultado       sim|não    sim           métrica-alvo (definida no yaml — ex.: "fechou proposta")
resposta        sim|não    não           métrica de sinal forte (ex.: "cliente respondeu")
custo           número     não
tempo_min       número     não
nota_humana     0|1        não           usado em calibração
observacao      texto      não
```

A pessoa preenche na planilha que já usa e exporta CSV, ou o Executor grava direto quando ele mesmo produz o artefato. **Conectores (v1+) só traduzem uma fonte para este mesmo CSV** — a arquitetura não muda.

---

## 7. O que fica fora (de propósito)

- Banco de dados, dashboard web, fila, servidor — não no v0.1/v1.
- Meta-agente que altera agentes — não antes do v2.
- Múltiplos loops + meta-loop — v2 ([07](./07-roadmap.md)).
