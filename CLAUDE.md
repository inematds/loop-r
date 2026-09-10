# loop-r — instruções do projeto

- **Conta/autor git:** `inematds <inematds@gmail.com>` (repo `inematds/loop-r`). Publicar = commit + push; GitHub Pages serve a raiz (`guia/` e `curso/`).
- **O que é:** framework LOOP-R + runner v0.1 em Claude Code (`/loop-r`), 9 agentes em `.claude/agents/`, exemplo em `exemplos/vendas-whatsapp/`. Leia `docs/README.md` (visão 01, crítica 06) antes de mexer em agente ou skill.
- **Invariantes do runner** (não quebrar): nunca escrever no arquivo de um agente no lugar dele; nunca promover sem `B_GANHOU` + aprovação; nunca apagar ciclo/versão/linha de memória; um experimento por vez.
- **Agentes novos nesta sessão não aparecem como `subagent_type`** — rode via `general-purpose` passando o caminho do `.md` do agente no prompt (comportamento idêntico).
- **Dados do exemplo são sintéticos** (`ferramentas/gerar_csv_sintetico.py`, seeds fixos). Regenerar com `--ate <data>` para simular a linha do tempo. Não editar `execucoes.csv` à mão.
- **Curso:** `/formato-curso-v5` (invocação manual) com `docs/plano-curso-loop-r.md`; saída em `curso/`. Guia: `guia/index.html` (skill `projetos-landing-guia`).
- **Versão:** `0.1.0` (README). Semver do CLAUDE.md global.
