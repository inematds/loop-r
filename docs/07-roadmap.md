# 07 — Roadmap

Começa pelo gargalo ([06 §8](./06-critica-e-viabilidade.md)): dados e medição antes de agentes. Cada fase entrega algo que funciona sozinho.

---

## v0.1 — "Um loop, uma planilha, um ciclo" *(construível agora)*

**Entrega:** alguém clona o repo, responde 5 perguntas, e roda um ciclo completo em L0/L1 sobre um CSV.

| # | Item | Arquivo(s) | Pronto quando |
|---|---|---|---|
| 1 | Esquema do CSV + validador | `dados/esquema.md`, Observador | Observador rejeita CSV inválido com motivo em 1 linha |
| 2 | Gerador de yaml (5 perguntas → `loop-r.yaml`) | `.claude/skills/loop-r/` (`iniciar`) | yaml passa nas 7 regras de validação de [03 §4](./03-spec-loop-r-yaml.md) |
| 3 | Cálculo de amostra mínima + frase de honestidade | Experimentador, `evals/amostra-minima.md` | mostra a tabela de [05 §3](./05-medicao-evals-guardrails.md) para o caso da pessoa |
| 4 | 9 agentes como subagentes, prompts gerados do yaml | `.claude/agents/*.md` | cada um lê/escreve só o que o contrato de [04](./04-agentes.md) diz |
| 5 | `/loop-r ciclo` — orquestra os 9 em sequência, grava `ciclos/NNNN/` | skill | manifesto 100% preenchido |
| 6 | Cartão de decisão + `decisao.md` | `/loop-r decidir` | 5 linhas, 3 botões |
| 7 | Promover / reverter via git | `/loop-r promover`, `/loop-r reverter` | `versoes/atual` muda + commit + ledger |
| 8 | Memória (ledger + 3 arquivos) | Memória | nunca apaga; 1 linha por evento |
| 9 | Meta-agente em modo `relatar` | `relatorio-meta.md` | ≤10 linhas, zero ação |
| 10 | Exemplo completo rodando: vendas WhatsApp com CSV sintético de 1.500 linhas (baseline + 2 testes completos a 300/variante + 1 semana pós-promoção) | `exemplos/vendas-whatsapp/` | 4 ciclos gravados: 1 amostra insuficiente, 1 descarte por guarda-corpo, 1 desenho de experimento, 1 promoção |
| 11 | README + `guia/index.html` (skill `projetos-landing-guia`) | raiz, `guia/` | página no GitHub Pages |

**Fora do v0.1:** cron, conectores, CLI Python, L2, juiz calibrado (só rubrica simples).

---

## v0.2 — "Medir de verdade"

| # | Item | Pronto quando |
|---|---|---|
| 1 | Rubrica binária + `evals/casos/` (20–50) | Avaliador pontua A vs B no artefato sem esperar cliente |
| 2 | Juiz em pares embaralhados, 3×, maioria | resultado estável em 3 rodadas consecutivas |
| 3 | `dados/calibracao.csv` + checagem de concordância ≥ 80% | `JUIZ DESCALIBRADO` dispara quando a rubrica é sabotada de propósito (teste) |
| 4 | Métrica de sinal proposta automaticamente por domínio | tabela de [05 §2](./05-medicao-evals-guardrails.md) embutida no gerador |
| 5 | Curso v5 (5 trilhas) publicado + card no portal | `/formato-curso-v5` + `/atualiza-portal` |

---

## v1 — "Roda sem mim"

| # | Item | Dependência |
|---|---|---|
| 1 | CLI Python `loopr` (mesmos comandos, mesmo yaml, API Anthropic) | — |
| 2 | Modelos por agente (leitura pequeno / raciocínio grande) | CLI |
| 3 | Cron / agendamento do ciclo + gatilho "rodar Avaliador quando N ≥ mínimo por variante" (sugestão do meta-agente no exemplo, ciclo 0002: 5 de 12 semanas foram espera sem veredito) | CLI |
| 4 | Conector 1: Google Sheets → CSV | um usuário piloto com dados reais |
| 5 | Conector 2: exportação do WhatsApp Business → CSV | idem |
| 6 | L2: auto-promoção + rollback automático | ≥5 promoções corretas em L1 no piloto |
| 7 | Notificação do cartão de decisão (Telegram/e-mail) | CLI |

---

## v2 — "Vários loops" *(pesquisa)*

| # | Item | Dependência |
|---|---|---|
| 1 | Múltiplos `loop-r.yaml` no mesmo repo (vendas, atendimento…) | v1 estável |
| 2 | Meta-loop: Meta-agente lê todos os ledgers | meses de ledger real de ≥2 loops |
| 3 | Meta-agente em modo `propor` (L3 supervisionado) | idem + aprovação humana obrigatória |
| 4 | Conectores adicionais (CRM) | demanda real |

---

## Critério para avançar de fase

Nenhuma fase começa antes que a anterior tenha **um usuário real** (nem que seja o próprio Nei, num processo do INEMA) com **≥3 ciclos no ledger**. O framework se aplica a si mesmo: sem evidência, não promove.

---

## Primeiro loop real sugerido (dogfooding)

Processo do INEMA com dados já existentes e volume semanal ≥ 50: ex.: **roteiros de Reels** (métrica de sinal: retenção nos 3s; sem piorar: tempo de produção, CTR do CTA) ou **respostas a leads do portal**. Escolher o que já tem CSV/planilha hoje.
