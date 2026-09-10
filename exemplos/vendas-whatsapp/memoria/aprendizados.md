# Aprendizados (provado e promovido)

## Hipóteses

- 2026-07-27 · ciclo 0004 · H3 (abrir citando ponto específico da avaliação da cliente, `versoes/v2`) — E0002, B_GANHOU. B elevou taxa_resposta de 19,33% (58/300) para 29,33% (88/300) — z=2,8543, p=0,0043, significativo (N=300/300). Guarda-corpos dentro da tolerância: margem_media Δ=+0,0068 (tol 0,01) · reclamacoes Δ=+0,0067, 4/300 vs 2/300 (tol 0,01) · optout Δ=−0,0067, 1/300 vs 3/300 (tol 0,005). Decisão humana (2026-07-27, Nei simulado): aprovado. PROMOVIDA v2 (`versoes/v2`, atual → v2).

## Processo

- 2026-04-27 · ciclo 0002 · Tolerância zero em guarda-corpo de evento raro não distingue efeito de ruído. No E0001 (H2, teto de 80 palavras), `reclamacoes` tem tolerância 0,0 no `loop-r.yaml`; B registrou 6/300 (2,00%) vs A 1/300 (0,33%) — viola a tolerância literal, mas com N=300 essa diferença não é estatisticamente significativa (Fisher p≈0,12). O veredito seguiu a regra escrita (`A_SEGUE`, H2 descartada) porque o contrato não permite contorná-la — mas o próprio ajuste registra a falha de desenho. Correção: `loop-r.yaml` → `reclamacoes.tolerancia: 0,0 → 0,01` (≈ 2 erros-padrão de uma taxa de ~1% com N=300), para eventos raros terem piso ≥ ruído esperado na amostra planejada, ou usar teste estatístico ("B não é significativamente pior") em vez de tolerância absoluta. Vale só para os próximos experimentos — E0001 não é reavaliado com a regra nova.

- 2026-07-27 · ciclo 0004 · Sinal move, alvo não se move — pela segunda vez no loop. E0002 (H3): resultado (conversão) A=3,00% (9/300) vs B=3,67% (11/300), Δ=+0,67pp, z=0,45 p=0,65 (Fisher p=0,82, derivado) — não significativo, `metrica_alvo.alvo`=0,05 e nenhuma variante chega perto. Igual padrão de H2/E0001 (resposta subiu ~+10pp, conversão ficou parada). Depois de duas hipóteses testadas, o elo sinal (taxa_resposta) → alvo (conversão) segue não provado — mover o sinal não é evidência de que o alvo se move junto.

- 2026-07-27 · ciclo 0004 · A coluna `variante` (A/B) não identifica o experimento — só a janela de datas separa. `versao`=v1 em 100% das 1450 linhas do CSV, inclusive nas 600 linhas rotuladas `B`, que juntam E0001-B (H2, descartada no ciclo 0002) e E0002-B (H3, promovida neste ciclo) sob o mesmo rótulo. Qualquer tabela "todo o período" agrupada só por variante mistura dois prompts diferentes sem aviso (ver `ciclos/0004/critica.md`, aviso de leitura). Correção necessária: `dados/esquema.md` precisa de uma coluna `experimento` (ex.: E0001, E0002) — a separação não pode depender só de datas.

