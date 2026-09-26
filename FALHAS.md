| 2026-09-26 | Aplicação de traduções por fragmentos exigiu reparos em cartões JSON e atributos e não era segura para chaves curtas | Aplicar unidades completas a partir da seção PT original; tratar atributos e cartões com parsers próprios | prompt |
# FALHAS — loop-r

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-09-26 | Checagem staged detectou espaços em linhas vazias de guias novos, fora do diff rastreado anterior | Limpar linhas vazias e validar também git diff --cached --check | infra |
| 2026-09-26 | Link de idioma na barra fixa não recebia clique porque herdava pointer-events:none | Habilitar pointer-events somente no seletor de idiomas | infra |
| 2026-09-26 | Trilha 4 EN/ES referenciava aula.css ausente e guia PT excedia largura móvel | Apontar CSS compartilhado e aplicar min-width:0 nas células do guia | infra |
| 2026-09-26 | Verificador de tradução não detectava feedbacks, legendas e cartões de revisão literais em PT nos catálogos | Incluir esses campos pelos textos exatos da fonte e reaplicar cada aula; auditar todos os campos JSON/atributos | infra |
| 2026-09-26 | Builder da UI compartilhada gravava a cópia T4 em assets/curso.js e reutilizava a chave de progresso entre idiomas | Destinar T4 ao curso.js referenciado e acrescentar o locale ao CK, testando PT/EN/ES no mesmo contexto | prompt |
| 2026-09-26 | Checker validava estrutura dos cartões mas deixava passar texto PT e atributos sem palavras do filtro | Comparar campos longos com a fonte e verificar conteúdo front/back, além de estrutura | infra |
| 2026-09-26 | Catálogos das aulas 1 e 2 continham entradas fora do esquema de pares EN/ES e o aplicador interrompeu / selecionou caractere isolado | Remover entradas auxiliares e validar todas as chaves e pares antes de aplicar | prompt |
| 2026-09-26 | Catálogo da aula 4 deixou vazia a tradução ES de um rótulo de diagrama e o verificador rejeitou a unidade | Exigir valor não vazio nos dois idiomas antes de aplicar; preencher o rótulo e reaplicar | prompt |
| 2026-09-26 | Catálogo da aula 5 da trilha 4 tinha escape inválido e impedia leitura JSON | Remover a barra indevida antes do ponto e validar com `python -m json.tool` | prompt |
| 2026-09-26 | Fragmentos de comentários da substituição antiga apareciam entre aulas da trilha 1 EN/ES | Restaurar separadores entre seções a partir do PT e conferir texto fora das aulas | infra |
| 2026-09-10 | Crítico (ciclo 0004) flagrou: linhas `variante=B` de E0001 e E0002 indistinguíveis no CSV → tabelas 'todo o período' inválidas | coluna `experimento` no esquema (template + docs 02); Observador agrupa por ela | prompt |
| 2026-09-10 | CSV sintético (seed 42) saiu com A=24% vs desenho 20% → ciclo 2 daria A_SEGUE por variância, não por conteúdo | gerador com `--seed2` para as semanas ≥5 (mantém semanas 1–4 do ciclo 0001) + busca de seed cuja amostra reflete as taxas desenhadas; documentado no docstring | infra |
| 2026-09-10 | Otimizador estimou efeito pequeno (17→22%) → Experimentador calculou 40 semanas > teto e parou | não foi bug: escalou para o aprovador como previsto; runner sincronizou o yaml (300→166) após a decisão. Regra fixada no agente experimentador: dimensionar pelo `alvo` do yaml, não pela expectativa do Otimizador | prompt |
