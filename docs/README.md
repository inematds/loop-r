# docs/ — LOOP-R

Documentação do framework, do produto (repo `loop-r`) e do curso. Ordem de leitura sugerida:

| # | Arquivo | O que é |
|---|---|---|
| — | [loop-r-framework.md](./loop-r-framework.md) | O framework conceitual completo (texto-fonte, 19 seções) |
| 01 | [01-visao-produto.md](./01-visao-produto.md) | Contrato de produto: as 5 respostas mínimas, o que o sistema constrói e mantém, níveis de autonomia L0–L3, o que "garantir" significa |
| 06 | [06-critica-e-viabilidade.md](./06-critica-e-viabilidade.md) | **Leia antes de 02–05.** Onde o LOOP-R quebra (amostra pequena, Goodhart, juiz que deriva, custo, ruído, dados) e o veredito de viabilidade por fase |
| 02 | [02-arquitetura.md](./02-arquitetura.md) | Estrutura do repo, git como promoção/rollback, fluxo do ciclo, adaptador CSV, onde roda (Claude Code → CLI) |
| 03 | [03-spec-loop-r-yaml.md](./03-spec-loop-r-yaml.md) | Spec do `loop-r.yaml`: obrigatórios × inferidos, validação, exemplo gerado de 5 frases |
| 04 | [04-agentes.md](./04-agentes.md) | Os 9 agentes: o que lê, escreve, decide, nunca faz — com esqueleto de prompt |
| 05 | [05-medicao-evals-guardrails.md](./05-medicao-evals-guardrails.md) | Três tipos de métrica, "sem piorar", tabela de amostra mínima, rubrica binária, calibração do juiz, cartão de decisão |
| 07 | [07-roadmap.md](./07-roadmap.md) | v0.1 (agora) → v0.2 → v1 → v2, com critério para avançar |
| — | [plano-curso-loop-r.md](./plano-curso-loop-r.md) | Plano do curso v5: 5 trilhas / 21 aulas, tradução de jargão, mapa aula → artefato do produto |

**Uma frase:** o LOOP-R como *disciplina de processo com registro e não-regressão* é viável hoje; como *sistema que aprende sozinho* depende de volume de dados — e o produto diz isso na primeira tela.
