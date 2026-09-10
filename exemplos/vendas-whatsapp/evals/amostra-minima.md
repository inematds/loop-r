# Amostra mínima por variante — teste z para duas proporções

Calculado em 2026-02-02 (ciclo 0001) pelo Experimentador. Parâmetros do `loop-r.yaml`: `confianca = 0.95`, `poder = 0.80`, `volume_estimado_por_semana = 50`.

## Fórmula

```
n = [ z_{α/2} · √(2·p̄·(1−p̄)) + z_β · √(p₁(1−p₁) + p₂(1−p₂)) ]² / (p₂ − p₁)²
p̄ = (p₁ + p₂) / 2       z_{α/2} = 1,9600 (95%, bilateral)       z_β = 0,8416 (poder 80%)
duração (semanas) = ⌈ n × 2 / 50 ⌉
```

## Conta do experimento E0001 (H2) — `taxa_resposta` 0,17 → 0,30 (base: `metrica_sinal.alvo`, decisão do aprovador)

```python
from math import sqrt, ceil
from statistics import NormalDist
p1, p2 = 0.17, 0.30
za = NormalDist().inv_cdf(1 - 0.05/2)   # 1.9600
zb = NormalDist().inv_cdf(0.80)         # 0.8416
pbar = (p1 + p2) / 2                    # 0.235
n = ((za*sqrt(2*pbar*(1-pbar)) + zb*sqrt(p1*(1-p1) + p2*(1-p2)))**2) / (p2-p1)**2
# n bruto = 165.80  ->  166 por variante
# duração = 166 × 2 / 50 = 6,64  ->  7 semanas
```

Desenho anterior (mesmo dia, substituído por `ciclos/0001/decisao-experimento.md`): 0,17 → 0,22 (ENTÃO literal de H2) → 985/variante, 40 semanas — acima do teto de 16. O aprovador decidiu dimensionar pelo efeito mínimo que vale detectar (alvo do yaml), não pela expectativa do Otimizador.

## Tabela

| p₁ → p₂ | métrica | n / variante | total (A+B) | semanas a 50/sem | observação |
|---|---|---|---|---|---|
| **0,17 → 0,30** | `taxa_resposta` (alvo do yaml — **E0001 vigente**) | **166** | 332 | **7** | base escolhida pelo aprovador |
| 0,17 → 0,22 | `taxa_resposta` (ENTÃO literal de H2 — desenho anterior) | 985 | 1.970 | 40 | acima do teto de 16 sem; substituído |
| 0,17 → 0,25 | `taxa_resposta` (ENTÃO de H1, vetada) | 406 | 812 | 17 | referência |
| 0,17 → 0,2506 | `taxa_resposta` (MDE que cabe em 16 sem) | 400 | 800 | 16 | efeito mínimo detectável com o teto de 16 semanas |
| 0,20 → 0,30 | `taxa_resposta` (valores do yaml, desatualizados) | 294 | 588 | 12 | é de onde saiu o `amostra_minima_por_variante: 300` do yaml |
| 0,03 → 0,05 | `conversao` (métrica alvo) | 1.506 | 3.012 | 61 | não testável em um ciclo — fica como vigiada |

Notas:
- O `metrica_sinal.atual: 0.20` do yaml está desatualizado; o observado no ciclo 0001 é 0,17 (34/200). Os valores desatualizados do yaml (`amostra_minima_por_variante: 300`, `duracao_estimada_semanas: 12`) não foram alterados aqui — não é atribuição do Experimentador.
- Cada variante recebe 25/semana (alocação 50/50 sobre 50/semana), daí a duração = n × 2 / 50.

---

## Conta do experimento E0002 (H3) — `taxa_resposta` 0,1836 → 0,30 (base: `metrica_sinal.alvo`)

Calculado em 2026-05-04 (ciclo 0003) pelo Experimentador. Mesma fórmula e parâmetros acima. Taxa atual = v1/A em **todo o período** (pré + E0001-A + pós), 101/550 = 0,18364 (`ciclos/0003/evidencia.md` §b).

```python
from math import sqrt, ceil
from statistics import NormalDist
p1, p2 = 101/550, 0.30                  # 0.18364 -> alvo do yaml
za = NormalDist().inv_cdf(1 - 0.05/2)   # 1.9600
zb = NormalDist().inv_cdf(0.80)         # 0.8416
pbar = (p1 + p2) / 2                    # 0.24182
n = ((za*sqrt(2*pbar*(1-pbar)) + zb*sqrt(p1*(1-p1) + p2*(1-p2)))**2) / (p2-p1)**2
# √(2·p̄·(1−p̄)) = 0.6055 ; √(p₁(1−p₁)+p₂(1−p₂)) = 0.5999
# numerador = (1.9600·0.6055 + 0.8416·0.5999)² = 1.6918² = 2.8621 ; denominador = 0.11636² = 0.013540
# n bruto = 211.37  ->  212 por variante
# duração = 212 × 2 / 50 = 8.48  ->  9 semanas
```

| p₁ → p₂ | métrica | n / variante | total (A+B) | semanas a 50/sem | observação |
|---|---|---|---|---|---|
| **0,1836 → 0,30** | `taxa_resposta` (alvo do yaml — **E0002 vigente**) | **212** | 424 | **9** | base v1/A todo o período (101/550) |
| 0,1836 → 0,2662 | `taxa_resposta` (MDE que cabe em 16 sem) | 400 | 800 | 16 | efeito mínimo detectável com o teto de 16 semanas |
| 0,0418 → 0,05 | `conversao` (métrica alvo, 23/550) | 10.271 | 20.542 | 411 | não testável — segue vigiada |

Notas:
- 212 > 166 (E0001) porque a base subiu de 0,17 para 0,1836 e o alvo ficou em 0,30: diferença menor (11,64 pp vs 13 pp) exige mais amostra.
- O `experimento.amostra_minima_por_variante: 166` e `duracao_estimada_semanas: 7` do yaml correspondem a E0001; para E0002 são 212 / 9. Não alterados aqui — fora da atribuição do Experimentador.
