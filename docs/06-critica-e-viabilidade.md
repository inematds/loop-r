# 06 — Crítica e viabilidade: onde o LOOP-R quebra, e o que fazer a respeito

Este documento é deliberadamente duro. Ele existe para que a arquitetura ([02](./02-arquitetura.md)) e a medição ([05](./05-medicao-evals-guardrails.md)) sejam desenhadas **a partir dos problemas**, e para que nenhum outro documento — nem o curso — prometa mais do que o sistema entrega.

---

## 1. A tensão embutida no objetivo

> "instruções mínimas" **×** "garanta o resultado constante"

Essas duas metas puxam em direções opostas:

- Quanto **menos** a pessoa diz, **mais** o sistema tem que inferir — e o que ele infere sobre segurança, política e fonte de dados pode estar errado.
- Quanto **mais** garantia se quer, **mais** a pessoa precisa dizer (o que nunca muda, onde está a evidência, quanto pode gastar).

**Resolução adotada:** "mínimo" = as 5 respostas de [01 §2](./01-visao-produto.md). Não menos. Um sistema que aceita menos do que isso não é mais fácil — é mais perigoso, porque vai otimizar contra um objetivo que ninguém verificou.

---

## 2. O LOOP-R não garante melhoria. Ponto.

Nenhum loop de aprendizado garante que o número sobe. O que ele pode garantir:

| Garante | Não garante |
|---|---|
| Que uma versão **pior** não substitui a atual por decisão do sistema | Que a próxima versão será **melhor** |
| Que toda mudança tem registro e volta atrás em um comando | Que o registro terá alguma coisa útil (pode ser "sem evidência" 10 ciclos seguidos) |
| Que o ciclo roda toda vez, do mesmo jeito | Que cada ciclo produz uma hipótese boa |
| Que o custo não passa do teto | Que o custo compensa |

**Consequência para o produto:** o texto de venda, o curso e o guia falam em *não-regressão, auditabilidade e constância de processo*. A palavra "garantir" só aparece acompanhada de uma dessas três.

---

## 3. Amostra pequena: o problema que mata a maioria dos loops

O exemplo-âncora do framework é "conversão de 3% → 5%". Para **provar** que uma versão B converte 5% contra 3% da versão A, com o rigor mínimo usual (95% de confiança, 80% de poder), são necessárias cerca de **1.500 execuções por versão — 3.000 no total**.

Uma pequena empresa que manda 200 propostas por mês levaria **15 meses** para fechar um único experimento. Isso não é um detalhe; é a razão pela qual "loops de vendas com IA" em empresas pequenas viram *opinião com cara de dado*.

**Mitigações (todas entram no v0.1):**

1. **Métrica de sinal forte antes da métrica de dinheiro.** Taxa de resposta (20% → 30%) precisa de ~300 por versão, não 1.500. O loop otimiza primeiro o que dá para medir rápido, e vigia a conversão final como guarda-corpo.
2. **Regra dura: evidência insuficiente ⇒ não promove.** O Avaliador não escolhe "o que parece melhor". Ele responde uma de três coisas: *B ganhou com margem*, *A segue*, ou *amostra insuficiente — continue o teste*. A terceira resposta é a mais comum e tem que ser aceitável.
3. **Evals de artefato para o que não depende de cliente.** Qualidade de uma proposta, aderência a um roteiro, ausência de erro factual — isso se avalia sobre o próprio texto, com 20–50 casos, sem esperar o cliente responder. É onde o loop gira rápido.
4. **Tabela de amostra mínima no yaml**, calculada pelo Experimentador a partir da métrica-alvo, e mostrada à pessoa antes de iniciar o teste ("este teste precisa de ~300 envios por versão; no seu ritmo, 6 semanas").

---

## 4. Goodhart: o loop aprende a trapacear a métrica

Toda métrica isolada vira alvo e deixa de medir o que importava:

| Pedido | O que o loop aprende |
|---|---|
| maximizar cliques | clickbait |
| minimizar tempo de atendimento | encerrar rápido sem resolver |
| maximizar vendas | descontar até a margem sumir |
| maximizar taxa de resposta | mensagens que provocam "pare de me mandar isso" (que conta como resposta) |

**Mitigação (obrigatória, não opcional):** todo objetivo tem a forma **"maximizar X sem piorar Y, Z, W"**. O Guardião veta hipóteses que toquem Y/Z/W; o Avaliador reprova versões que melhoram X e pioram qualquer guarda-corpo, mesmo que X tenha subido muito. Ver [05 §2](./05-medicao-evals-guardrails.md).

O último exemplo da tabela mostra um risco extra: **a métrica pode ser mal definida no CSV**. "Resposta" tem que excluir "resposta negativa". A definição da métrica é parte do input, e o Observador confere a consistência antes de contar.

---

## 5. O juiz de IA deriva

Quando a métrica é subjetiva (qualidade de proposta, tom, clareza), o Avaliador usa um modelo como juiz com rubrica. Problemas conhecidos:

- **Viés de posição:** prefere a segunda opção, ou a mais longa.
- **Deriva:** a mesma rubrica dá notas diferentes em semanas diferentes (modelo atualizado, temperatura, ordem dos exemplos).
- **Concordância consigo mesmo:** o Otimizador e o Avaliador rodam no mesmo modelo — o modelo tende a aprovar o próprio estilo.

**Mitigações:**
- Rubrica com critérios binários (sim/não), não nota de 1 a 10.
- Sempre comparar em pares **com ordem embaralhada** e repetir 3× — desempate por maioria.
- **Conjunto de calibração humano**: 10–20 exemplos que a pessoa avaliou uma vez. O juiz é testado contra eles a cada ciclo; se a concordância cair abaixo de 80%, o Meta-agente sinaliza e o ciclo não promove.
- Avaliador pode rodar em modelo diferente do Otimizador, quando o custo permitir.

---

## 6. Custo por ciclo — o primeiro trabalho real do Meta-agente

Um ciclo com 9 agentes lendo dados, memória e versões consome dezenas a centenas de milhares de tokens, dependendo do volume. Sem teto, o loop pode custar mais do que o ganho que persegue.

**Mitigações:**
- Teto de custo por ciclo no yaml (input obrigatório #4). O Guardião interrompe o ciclo ao atingir.
- **A primeira métrica que o Meta-agente vigia é custo por hipótese promovida.** Se em 5 ciclos nada foi promovido, ele propõe: reduzir cadência, trocar por modelo mais barato nos agentes de leitura, ou encolher a memória que os agentes carregam.
- Agentes de leitura (Observador, Memória) em modelo pequeno; raciocínio (Crítico, Otimizador, Avaliador) em modelo maior.

---

## 7. Aprender com ruído

Com poucos dados, o Crítico vai "encontrar padrões" que são acaso: *"propostas enviadas na terça convertem mais"* com 12 propostas. O loop então gasta um ciclo testando ruído.

**Mitigações:**
- O Crítico só pode afirmar padrão com N mínimo (definido no yaml; default 30 por segmento).
- Toda hipótese carrega **força da evidência** (fraca / moderada / forte). O Experimentador prioriza fortes; fracas vão para a memória como "observado, não testado".
- Memória de hipóteses **descartadas** é tão importante quanto a das promovidas — impede re-testar a mesma ideia ruim.

---

## 8. A fonte de dados é o gargalo, não os agentes

Todo o framework depende do passo **Observe**. Sem evidência, o resto é teatro. E o mundo real guarda dados em CRM, WhatsApp, e-mail, planilha do sócio, cabeça do vendedor.

**"Construir a solução a partir de instruções mínimas" não constrói integrações.** Não há como o sistema, a partir de 5 frases, se conectar ao CRM da pessoa.

**Decisão:** o v0.1 tem **um** adaptador universal: planilha/CSV com colunas definidas pelo yaml. Quem quer usar, exporta ou preenche. Conectores (WhatsApp Business, Sheets, HubSpot…) são v1+, um por vez, e cada um é um projeto próprio. O roadmap ([07](./07-roadmap.md)) começa pelo adaptador, não pelos agentes.

---

## 9. O Meta-agente é pesquisa, não produto

"O sistema que melhora o sistema" é a ideia mais sedutora do framework e a menos madura. Um agente que redesenha outros agentes, sem supervisão, com dados escassos, é um multiplicador de todos os problemas acima.

**No produto:**
- **v0.1/v1:** o Meta-agente **só relata**: custo por ciclo, hipóteses geradas × promovidas, agente que mais gera veto do Guardião, concordância do juiz. Zero ação.
- **v2:** propõe mudanças estruturais para aprovação humana (L3 supervisionado).
- Redesign autônomo fica fora do horizonte deste repo.

---

## 10. Humano no loop custa atenção — e atenção acaba

L1 exige que a pessoa aprove cada promoção. Nas primeiras semanas, ela aprova. No mês 3, aprova sem ler. No mês 4, para de abrir. O loop vira ruído de notificação.

**Mitigações:**
- **Uma decisão por semana, no máximo**, apresentada em um cartão de 5 linhas: o que mudou, quanto melhorou, o que foi vigiado, custo, "aprovar / rejeitar / esperar mais dados".
- Se não houver resposta em N dias, o padrão é **não promover** (seguro), e o Meta-agente registra "decisão pendente".
- L2 (auto-promoção com rollback) existe justamente para quando a pessoa já confia — mas só se desbloqueia depois de 5 promoções corretas em L1.

---

## 11. Veredito de viabilidade, por fase

| Fase | O quê | Viabilidade | Depende de |
|---|---|---|---|
| **v0.1** | 5 perguntas → yaml → 9 agentes → 1 ciclo em L0/L1 sobre CSV, com git como histórico | **Alta — construível agora com certeza** | Nada externo. Claude Code + repo |
| **v0.2** | Evals de artefato + juiz calibrado + regra de amostra mínima | **Alta** | 10–20 exemplos rotulados pela pessoa |
| **v1** | CLI independente + 1–2 conectores de dados + L2 com rollback automático | **Média** — cada conector é um projeto; L2 precisa de volume | Volume de dados real de um usuário piloto |
| **v2** | Meta-loop entre vários loops; meta-agente propõe redesign | **Baixa/pesquisa** | Meses de ledger de ≥2 loops reais |

**Resumo em uma frase:** o LOOP-R como *disciplina de processo com registro e não-regressão* é viável hoje e vale sozinho; o LOOP-R como *sistema que aprende sozinho* depende de volume de dados que a maioria das empresas pequenas não tem — e o produto tem que ser honesto sobre isso na primeira tela.

---

## 12. O que este documento muda nos outros

- [01 §5–6](./01-visao-produto.md): garantias reescritas como não-regressão / auditabilidade / constância.
- [02](./02-arquitetura.md): git como mecanismo de promoção/rollback; Meta-agente só relata; adaptador CSV primeiro.
- [03](./03-spec-loop-r-yaml.md): campos `guarda_corpos`, `teto`, `amostra_minima`, `calibracao` obrigatórios.
- [05](./05-medicao-evals-guardrails.md): três respostas do Avaliador; métrica de sinal forte; rubrica binária; embaralhar pares.
- [07](./07-roadmap.md): começa pelo adaptador de dados.
- [plano-curso](./plano-curso-loop-r.md): aula "O que o LOOP-R não garante".
