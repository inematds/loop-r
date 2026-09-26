# 🔁 LOOP-R — A Framework for Self-Improving Systems and Businesses

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

> Don't ask AI to improve. Make every run produce evidence, every piece of evidence generate a hypothesis, and every hypothesis become an experiment. Only what is proven enters the next version.

LOOP-R turns a business process (proposals, customer support, content…) into an **improvement loop with a record and a rollback button**: nine AI assistants with separate roles execute, measure, critique, propose, test, judge, preserve memory, and watch their own cost. **The system never replaces the current version with a worse one.**

## 📖 User guide

Full guide (overview + step-by-step): **https://inematds.github.io/loop-r/guia/en/**

## 🎓 Course

**LOOP-R: The Business That Learns on Its Own** — 5 tracks, 21 lessons (~7.5 h), for non-technical owners and managers aged 40+: **https://inematds.github.io/loop-r/curso/en/**

## What it guarantees (and what it does not)

| Guarantees | Does not guarantee |
|---|---|
| **No regression** — a worse version never enters production | that the number will go up |
| **Auditability** — every version, test, and decision is recorded; `reverter` rolls back in one command | that every cycle will produce a good hypothesis |
| **Process consistency** — every cycle runs the same way | that the cost is worthwhile without your review |
| **Cost ceiling** — it stops when the limit is reached | — |

Read [docs/06-critica-e-viabilidade.md](docs/06-critica-e-viabilidade.md) before expecting more than this (document in Portuguese).

## Get started (Claude Code)

```bash
git clone https://github.com/inematds/loop-r && cd loop-r
claude
> /loop-r iniciar
```

The `iniciar` command asks **5 questions** and sets everything up:

1. Which process, and what number should move from what value to what value?
2. Where is each run's result recorded? (spreadsheet)
3. What must AI never change on its own? What must not get worse?
4. How much can each cycle spend? Weekly or monthly?
5. Do you approve every change (L1), or only want to review proposals (L0)?

Then:

```
/loop-r ciclo      # runs the 9 agents → ciclos/NNNN/
/loop-r decidir    # five-line decision card: approve / reject / wait
/loop-r promover   # candidate becomes the official version (commit)
/loop-r reverter   # restore the previous version (commit)
/loop-r status
```

## Structure

```
loop-r.yaml             loop profile (5 answers + inferred values)       docs/03
.claude/agents/         9 agents: what each reads, writes, decides, avoids docs/04
.claude/skills/loop-r/  the runner (/loop-r ...)
versoes/                v1, v2… + atual → vN (git = promote/rollback)
dados/                  execucoes.csv (universal adapter) + schema
evals/                  yes/no rubric, minimum sample, cases
ciclos/NNNN/            manifest + each agent's output + decision
memoria/                ledger, learnings, discarded, observed-not-tested
exemplos/vendas-whatsapp/ complete reference loop (4 cycles run)
docs/                   overview, critique, architecture, spec, agents, measurement, roadmap, course
```

## A completed example

[`exemplos/vendas-whatsapp/`](exemplos/vendas-whatsapp/) — an aesthetics clinic, WhatsApp proposals, 1,500 synthetic rows, and 4 cycles actually run by the agents: insufficient sample (0001), rejected by a guardrail — and the tolerance correction that taught us (0002), a new experiment (0003), promotion to v2 (0004). **Read the [example README](exemplos/vendas-whatsapp/README.md) first** (in Portuguese): it explains what is real (the agents) and what is simulated (data and decisions). Then read `memoria/ledger.md` and `ciclos/*/manifesto.md`.

## Documentation

[docs/README.md](docs/README.md) — start with the **overview** (01) and the **critique** (06). Documents are in Portuguese.

## Version

`0.1.0` — Claude Code runner, CSV adapter, L0/L1, meta-agent in reporting mode. See the [roadmap](docs/07-roadmap.md) (in Portuguese).

---

INEMA · [inema.club](https://inema.club) · [inema.pro](https://inema.pro)
