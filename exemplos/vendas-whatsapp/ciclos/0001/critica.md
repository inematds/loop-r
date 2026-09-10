# Crítica — Ciclo 0001 (v1, linha de base)

Fonte: `ciclos/0001/evidencia.md` (200 linhas, 2026-01-05 → 2026-02-01, só variante A).
Escala de força (n_minimo_para_padrao = 30): FORTE N ≥ 90 · MODERADA N ≥ 30 · FRACA N < 30.

## 1. Funciona

| Afirmação | Número | Força |
|---|---|---|
| Guarda-corpo `reclamacoes` quase intacto no período: 1 reclamação em 200 propostas | reclamou 0,50% (N=200) | FORTE |
| Guarda-corpo `optout` baixo no período: 2 opt-outs em 200 | optout 1,00% (N=200) | FORTE |
| Segmentos `medio` e `grande` sem nenhuma reclamação nem opt-out | 0/78 e 0/30 | MODERADA (medio) · MODERADA (grande) |
| Tempo por proposta estável | 5,465 min (N=200); faixa semanal 5,02–5,80 (N=50 cada) | FORTE (geral) · MODERADA (por semana) |
| Custo por proposta estável | 1,0283 (N=200); faixa semanal 0,9966–1,0644 (N=50 cada) | FORTE (geral) · MODERADA (por semana) |
| Segmento `pequeno` responde acima da média geral | resposta 21,74% (N=92) vs 17,00% (N=200) | FORTE |

## 2. Falha

| Afirmação | Número | Força |
|---|---|---|
| Conversão abaixo do declarado como "atual" no `loop-r.yaml` (0,03) e metade do alvo (0,05) | 2,50% (5/200) | FORTE |
| Taxa de resposta (métrica-sinal) abaixo do declarado como "atual" (0,20) e bem abaixo do alvo (0,30) | 17,00% (34/200) | FORTE |
| 83% das propostas não geram resposta em 48h — o grosso do custo e do tempo é gasto em mensagens sem retorno | 166/200 sem resposta; custo 1,0283 × 200 ≈ 205,7 gasto para 5 conversões (≈ 41 por conversão, derivado) | FORTE |
| Segmento `medio` responde pela metade dos outros | resposta 10,26% (N=78) vs 21,74% (pequeno, N=92) e 20,00% (grande, N=30) | MODERADA |
| Segmento `medio` é o mais caro por proposta e o que menos responde | custo 1,0472 (N=78) vs 1,0201 (pequeno) e 1,0043 (grande) | MODERADA |
| Duas semanas inteiras sem nenhuma conversão | W02 0/50, W03 0/50 | MODERADA (cada) |
| Todos os eventos de guarda-corpo do período concentram-se na semana W05 e no segmento `pequeno` | W05: 1 reclamação + 2 opt-outs (N=50); pequeno: 1 + 2 (N=92); demais semanas/segmentos: 0 | MODERADA (W05) · FORTE (pequeno) |
| Folga zero nos guarda-corpos `sem_piorar`: as tolerâncias são deltas contra a versão anterior (ver `rollback.gatilho`), então qualquer sucessora de v1 não pode ter nem uma reclamação a mais (tolerância 0,0) e tem só 0,5 pp de folga em opt-out (tolerância 0,005) | reclamou 0,50%, optout 1,00% (N=200) | FORTE |

Desperdício de custo/tempo, resumido: cada semana consome ≈ 51 de custo e ≈ 4,6 h de tempo (50 × 5,465 min) para 0–3 conversões.

## 3. Observado, não conclusivo (FRACA)

- **Margem média** por conversão: 0,32 geral (N=5); 0,31 pequeno (N=3), 0,32 medio (N=1), 0,35 grande (N=1). N de conversões é minúsculo — não dá para afirmar nada sobre margem por segmento, nem se a tolerância `margem_media` (0,01) está sendo respeitada.
- **Tendência de alta na conversão**: 0% → 0% → 4% → 6% (W02→W05). Cada semana tem N=50, mas os eventos são 0, 0, 2, 3 — cinco conversões no total; pode ser ruído.
- **Tendência de alta em reclamação/opt-out** na última semana (W05): 1 + 2 eventos. Três eventos, não conclusivo.
- **Segmento × semana**: todas as 12 combinações têm N entre 6 e 27 — nada reportável individualmente.
- **Conversão por segmento**: os percentuais (3,26% / 1,28% / 3,33%) vêm de 3, 1 e 1 eventos. O N do segmento é ≥ 30, mas a contagem de sucessos é pequena demais para distinguir os segmentos entre si.
- **Invariáveis** (desconto > 10%, promessa de resultado, contato pós-opt-out, concorrentes): `evidencia.md` não traz colunas sobre isso — não há como confirmar nem negar violação a partir dos dados deste ciclo. O texto do roteiro v1, por si, não contradiz nenhuma das quatro.
- **Custo vs. teto**: `teto.custo_por_ciclo_brl: 50` está no bloco do loop (junto de `max_hipoteses_por_ciclo`), e a coluna `custo` da evidência é custo por proposta sem unidade declarada. Custo médio × N dá ≈ 205,7 em 4 semanas (≈ 51,4/semana), mas não é possível afirmar que compara com o teto — categoria e unidade ambíguas.

## 4. Cruzamento com a memória

`memoria/aprendizados.md` e `memoria/descartados.md` estão vazios (primeiro ciclo). Nenhuma falha acima já foi resolvida ou descartada antes — nada a cruzar.
