# Plano de Curso — LOOP-R: Sua Empresa que Aprende Sozinha

**Revisão 2 (2026-09-10)** — alinhada ao produto ([01](./01-visao-produto.md)), à crítica ([06](./06-critica-e-viabilidade.md)) e ao contrato do `/formato-curso-v5` (1 `curso.html` por trilha, até 9 aulas/trilha, 15–25 min/aula, 3–5 passos/aula, prática sem terminal, jargão de computação traduzido ou eliminado).

**Fonte conceitual:** [loop-r-framework.md](./loop-r-framework.md)
**Ferramenta que o curso ensina a usar:** o repo `loop-r` ([02](./02-arquitetura.md)) — o curso não ensina abstrações; ensina a preencher, ler e decidir sobre os artefatos reais do produto.
**Saída:** `curso/trilha-N/curso.html` (5 trilhas) + `curso/index.html` (landing). O `guia/` é a landing+guia do repo (outra skill) e **aponta** para o curso.

---

## 0. Descoberta (Passo 0 do v5 — respostas propostas, a confirmar quando rodar a skill)

| Pergunta do v5 | Resposta proposta |
|---|---|
| Público específico | Donos e gestores de negócios pequenos/médios, 40+, que já usam IA para "fazer coisas" (propostas, respostas, posts) e sentem que nada melhora com o tempo |
| ≥2 profissões-alvo | **(1) dona de clínica de estética** que manda propostas por WhatsApp; **(2) corretor de imóveis** que responde leads de portal; **(3) gestor de suporte** de uma empresa de software pequena |
| Familiaridade com tecnologia | Usa WhatsApp, planilha e um chat de IA. Não usa terminal, não programa, nunca ouviu "Git" |
| Resultado prático | Sair com **um loop montado** no próprio negócio: 5 respostas dadas, planilha preenchida, 1 experimento desenhado, 1 decisão tomada com o cartão |
| Tempo por sessão | 20 min |

---

## 1. Posicionamento

O aluno não vem aprender prompt. Vem descobrir por que a empresa dele usa IA mil vezes e **continua igual** — e sair com um sistema que faz cada tarefa alimentar a próxima.

**Frase-âncora do curso:**
> Não peça para a IA melhorar. Faça cada execução produzir evidência, cada evidência gerar uma hipótese, cada hipótese virar um experimento — e só o que for comprovado entra na próxima versão.

**Promessa (verificável, na linguagem do v5):**
> Ao final, você terá um loop de melhoria rodando em um processo do seu negócio, com registro do que foi testado e um botão de voltar atrás.

**Antipromessa (dita na primeira aula, não escondida):** não promete que o número sobe. Promete que ele **não cai por decisão do sistema**, que tudo fica registrado, e que o ciclo roda toda semana do mesmo jeito. Fonte: [06 §2](./06-critica-e-viabilidade.md).

---

## 2. Tradução obrigatória de jargão (lista-sentinela do v5)

O produto usa git, yaml, csv, CLI. O curso **nunca** usa essas palavras sem tradução — e na maioria das aulas, usa só a tradução:

| Termo do produto | Como o curso chama | Analogia |
|---|---|---|
| `loop-r.yaml` | **ficha do loop** | a ficha de anamnese que a clínica preenche uma vez |
| CSV / `execucoes.csv` | **planilha de registro** | o caderno onde cada proposta vira uma linha |
| git / commit / versões | **histórico com botão de voltar** | o "desfazer" do Word, só que para o processo inteiro |
| promover | **virar a versão oficial** | o roteiro novo vira o roteiro da equipe |
| rollback | **voltar atrás** | — |
| agente | **assistente com uma função só** | o funcionário que só faz uma coisa e faz bem |
| eval / rubrica | **lista de conferência** | o checklist do inspetor antes de liberar o carro |
| amostra mínima | **quantidade que prova** | quantas vezes precisa acontecer para não ser sorte |
| Claude Code / CLI | **o programa que roda o loop** | — (aparece só no guia, não no curso) |
| repositório | **a pasta do loop** | — |

---

## 3. Estrutura — 5 trilhas, 21 aulas (~7h)

Cada trilha = 1 `curso.html`. Tipo de cada aula: `fundamento` (ideia) ou `ferramenta` (fazer no produto). Prática sempre em modo `prompt`, `tarefa` ou `analise` — nunca `codigo`.

### TRILHA 1 — Por que sua empresa não melhora *(diagnóstico)* — 4 aulas

| # | Aula | Tipo | Prática (modo) | Artefato do produto |
|---|---|---|---|---|
| 1.1 | A IA que termina ali: humano → pedido → resposta → fim | fundamento | *análise*: listar 5 tarefas que sua IA faz e que "terminam ali" | — |
| 1.2 | Dez mil execuções e nenhum aprendizado | fundamento | *tarefa*: contar quantas vezes por mês a mesma tarefa é refeita do zero | — |
| 1.3 | Os 5 níveis: de "responde" a "empresa que aprende" | fundamento | *análise*: marcar em que nível está (1–5) com gabarito | autoavaliação de maturidade |
| 1.4 | "IA, fique melhor" — o erro que parece inteligente | fundamento | *prompt*: reescrever uma instrução vaga com evidência + métrica + hipótese | — |

### TRILHA 2 — O LOOP-R *(o método)* — 5 aulas

| # | Aula | Tipo | Prática | Artefato |
|---|---|---|---|---|
| 2.1 | **L — Localizar**: um processo, um número | ferramenta | *tarefa*: escrever o objetivo com número (de X para Y) | ficha do loop — pergunta 1 |
| 2.2 | **O — Operar**: não existe aprendizado sem execução | fundamento | *análise*: mapear os passos atuais do processo | — |
| 2.3 | **O — Observar**: onde nasce a evidência | ferramenta | *tarefa*: preencher 10 linhas da planilha de registro | planilha de registro — pergunta 2 |
| 2.4 | **P — Propor**: da evidência à hipótese (SE… ENTÃO… PORQUE…) | fundamento | *prompt*: escrever 3 hipóteses no formato | — |
| 2.5 | **R — Reforçar**: testar, validar, virar oficial | fundamento | *análise*: dado um resultado A×B, dizer qual das 3 respostas cabe | — |

### TRILHA 3 — Os assistentes do loop *(a arquitetura)* — 4 aulas

| # | Aula | Tipo | Prática | Artefato |
|---|---|---|---|---|
| 3.1 | Um assistente para cada função: Executor, Observador, Crítico | fundamento | *prompt*: rodar o Crítico em uma proposta sua | — |
| 3.2 | Quem propõe, quem testa, quem julga: Otimizador, Experimentador, Avaliador | fundamento | *análise*: identificar quem "se convenceu sozinho" num caso | — |
| 3.3 | **O Guardião**: o que nunca muda sozinho | ferramenta | *tarefa*: escrever 3 invariáveis + 2 "sem piorar" | ficha do loop — pergunta 3 |
| 3.4 | **A Memória**: o ativo que a concorrência não copia | ferramenta | *tarefa*: escrever a 1ª linha do histórico (o que já tentou e falhou) | histórico / memória |

### TRILHA 4 — Medir de verdade *(evals, decisão e limites)* — 5 aulas

| # | Aula | Tipo | Prática | Artefato |
|---|---|---|---|---|
| 4.1 | O loop que aprende a trapacear: cliques, atendimento curto, desconto | fundamento | *análise*: para cada meta, achar a trapaça | — |
| 4.2 | A quantidade que prova: por que 12 propostas não dizem nada | fundamento | *análise*: ler a tabela de amostra e escolher a métrica realista | quantidade que prova |
| 4.3 | A lista de conferência: sim ou não, nunca nota de 1 a 10 | ferramenta | *tarefa*: escrever 6 critérios sim/não para o seu artefato | lista de conferência (rubrica) |
| 4.4 | O cartão de decisão: aprovar, rejeitar, esperar — e o botão de voltar | ferramenta | *análise*: decidir sobre 3 cartões reais (gabarito) | cartão de decisão — perguntas 4 e 5 |
| 4.5 | **O que o LOOP-R não garante** | fundamento | *análise*: marcar V/F em 8 afirmações sobre garantias | — |

### TRILHA 5 — Da tarefa à empresa *(aplicação)* — 3 aulas

| # | Aula | Tipo | Prática | Artefato |
|---|---|---|---|---|
| 5.1 | Um loop de vendas, do começo ao fim (caso da clínica) | ferramenta | *análise*: acompanhar 3 ciclos reais do exemplo e prever o 4º | exemplo `vendas-whatsapp` |
| 5.2 | Um loop de atendimento: dos 10.000 chamados ao produto melhor (caso do suporte) | fundamento | *prompt*: rodar o Observador sobre 20 chamados fictícios | — |
| 5.3 | Seu loop, montado: as 5 respostas + primeiro ciclo | ferramenta | *tarefa*: entregar a ficha do loop completa e o 1º cartão de decisão | ficha do loop completa (entrega final) |

**Fórmula que fecha o curso** (âncora da 5.3): **EXECUÇÃO × EVIDÊNCIA × EXPERIMENTAÇÃO × MEMÓRIA = EVOLUÇÃO** — qualquer fator zero, resultado zero. Cada trilha alimentou um fator.

---

## 4. Mapa aula → input mínimo do produto

As 5 respostas obrigatórias do [01 §2](./01-visao-produto.md) são construídas ao longo do curso, uma por vez:

| Resposta | Aula que a produz |
|---|---|
| 1. Objetivo com número | 2.1 |
| 2. Onde nasce a evidência | 2.3 |
| 3. O que nunca muda sozinho | 3.3 |
| 4. Teto de custo e tempo | 4.4 |
| 5. Quem aprova (nível L0/L1) | 4.4 |
| → ficha completa | 5.3 |

Os níveis de autonomia (L0–L2) aparecem na 1.3 (maturidade) e na 4.4 (decisão). L3 é citado só na 4.5 como "o que ainda é pesquisa".

---

## 5. Regras de conteúdo por aula (herdadas do v5, com o que muda aqui)

- **Abertura:** promessa verificável + tempo + "por que importa" + metáfora do mundo real (clínica, imobiliária, suporte — nunca robô/cérebro-circuito).
- **Núcleo:** 3–5 passos, cada um com exemplo de uma das 3 profissões da descoberta e um diagrama-de-mecanismo (os diagramas em texto do framework viram figuras).
- **Prática:** 1 por aula, 5–15 min, com `.psafe` ("é seguro porque nada muda no seu negócio até você aprovar").
- **Fecho:** resumo autoral ≤5 linhas + microação ≤15 min + gancho.
- **Erro comum** (`.qerr`, máx. 2/aula): puxados de [06](./06-critica-e-viabilidade.md) — "promover porque parece melhor", "parar o teste porque está ganhando", "12 propostas viraram regra", "meta sem 'sem piorar'".
- **Antes/Depois** (máx. 1/aula): sempre com número (ex.: taxa de resposta 20% → 29%, N = 312).

---

## 6. Recursos de apoio (entram como downloads/quadros no curso)

- **Ficha do loop** — as 5 perguntas em uma página (versão leiga do `loop-r.yaml`)
- **Planilha de registro** — colunas do [02 §6](./02-arquitetura.md), com 5 linhas de exemplo
- **Tabela "quantidade que prova"** — [05 §3](./05-medicao-evals-guardrails.md)
- **Cartão de decisão** em branco — [05 §7](./05-medicao-evals-guardrails.md)
- **Lista de conferência** modelo — 7 critérios sim/não
- **Os 9 assistentes em uma página** — função, o que lê, o que escreve, o que nunca faz
- **Canvas LOOP-R (13 perguntas)** — impresso, como fecho da 5.3

---

## 7. Avaliação

- Checkpoint por trilha: 5 perguntas de **decisão** (não de memória) — "dado isto, você promove, descarta ou espera?".
- Entrega final (5.3): ficha do loop completa + 1 cartão de decisão preenchido sobre o exemplo.
- Critério de aprovação: o aluno consegue dizer **qual evidência o faria descartar a própria ideia** e **qual guarda-corpo nunca deixaria a IA tocar**.

---

## 8. Produção

1. Rodar `/formato-curso-v5` (invocação manual, a skill bloqueia chamada automática) com este plano; confirmar as respostas da descoberta (§0).
2. Saída em `curso/` do repo `loop-r` (uma pasta por trilha + landing). **Não** em `guia/` — `guia/index.html` é a landing+guia do produto e linka para `curso/`.
3. Publicar: commit + push em `inematds/loop-r` (GitHub Pages da raiz). Card no portal via `/atualiza-portal` apontando para `https://inematds.github.io/loop-r/curso/`.
4. Revisar com `/revisar-curso` antes de publicar.
