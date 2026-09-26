# LOOP-R — tradução PT/EN/ES

Data: 2026-09-26. Conteúdo autoral em português. As novas traduções foram feitas por agentes configurados como GPT-6 Luna pela assinatura do Codex. Nenhuma API, chave ou tradutor externo foi utilizado.

## Cobertura concluída

- README em PT, EN e ES.
- Guia em `guia/`, `guia/en/`, `guia/es/`.
- Landing do curso em `curso/`, `curso/en/`, `curso/es/`.
- 21 aulas nas cinco trilhas: 4 + 5 + 4 + 5 + 3, em EN e ES.
- Texto de leitura, metadados, atributos de apoio/glossário, feedbacks, legendas SVG e cartões JSON traduzidos.
- Interface compartilhada com progresso separado por `slug:en` e `slug:es`; PT preserva sua chave anterior. Os valores internos de temas permanecem `dark`, `papel`, `sepia`.
- Seletores recíprocos PT/EN/ES nas 21 páginas, alternates e canonical. A troca conserva query e a aula aberta no hash.

Comandos, caminhos, IDs, CSVs e registros de exemplo executáveis permanecem literais. Documentação técnica de referência em `docs/` continua no idioma original, indicado nos READMEs. Os arquivos PT receberam seletores de idioma e ajustes mínimos de responsividade; o conteúdo autoral das aulas foi preservado.

## Reprodução local

Os catálogos `i18n/translations/track-N-lesson-M.json` guardam as traduções. `i18n/scripts/apply_text_units.py` substitui cada seção a partir do PT com unidades completas, sem substituir partes de IDs ou de código. `check_translations.py` verifica estrutura, atributos executáveis, cartões e resíduos. Os mapas do guia, landing e UI estão em `i18n/scripts/`.

Após aplicação dos catálogos, `python3 i18n/scripts/finalize_languages.py` normaliza seletores, metadados e CSS compartilhado da trilha 4. É idempotente e não usa rede.

## Evidências

- Verificador reforçado: 42 combinações de aula/idioma passaram, incluindo front/back dos cartões e comparação de campos longos com PT.
- Checagem estática: 14 páginas EN/ES sem problemas de estrutura, IDs ou destinos locais. Os candidatos restantes de espanhol são cognatos válidos como “próxima”.
- Chromium local: 21 páginas PT/EN/ES em 360 e 1440 px, sem erros de página, assets ausentes, imagens quebradas ou rolagem horizontal.
- 15 trocas de idioma, nas cinco trilhas a partir dos três idiomas, conservaram aula e query.
- Temas, quiz e persistência conferidos; teste no mesmo contexto registrou progresso PT/EN/ES em três chaves distintas.
- `node --check`, compilação Python e `git diff --check` passaram.

Evidências da integração em `/home/nmaldaner/projetos/output/rsi-traducoes-2026-09-26/`. Falhas reais e correções mínimas estão em `FALHAS.md`. Publicação via git após verificações; sem consultar Vercel.
