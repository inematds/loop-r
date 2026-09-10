VEREDITO: A_SEGUE
Métrica do teste: taxa_resposta  A=0,1933 (N=300)  B=0,2967 (N=300)  z=2,9426 p=0,0033 (bicaudal; unicaudal p=0,0016; z crítico 95% = 1,9600)
Vigiadas: margem_media A=0,3127 (N=15) vs B=0,3107 (N=14), Δ=−0,0020, tol 0,01 → DENTRO · reclamacoes A=0,0033 (1/300) vs B=0,0200 (6/300), Δ=+0,0167, tol 0,0 → FORA · optout A=0,0000 (0/300) vs B=0,0033 (1/300), Δ=+0,0033, tol 0,005 → DENTRO
Conclusão: B supera A com significância na taxa_resposta (N ≥ 166 em ambas), mas piora `reclamacoes` além da tolerância zero (6 vs 1) — guarda-corpo vetado, B não é promovida; A segue.

---

## Base do cálculo

- Experimento: E0001 (`ciclos/0001/experimento.md`), H2 — teto de 80 palavras. A = `versoes/atual` (v1), B = `versoes/candidata-vB`.
- Período: linhas de `dados/execucoes.csv` com `data ≥ 2026-02-02` até 2026-04-26 (600 linhas; 300 A / 300 B). Números recalculados do CSV e idênticos aos de `evidencia.md`.
- Amostra mínima 166/variante: atingida em ambas (300 ≥ 166). Veredito por amostra não se aplica.
- Teste z para duas proporções (pooled), nível `confianca: 0.95`:
  - p̂_A = 58/300 = 0,1933 · p̂_B = 89/300 = 0,2967 · p̄ = 147/600 = 0,2450
  - SE = √(0,2450·0,7550·(1/300+1/300)) = 0,03510 · z = (0,2967−0,1933)/0,03510 = 2,9426
  - p bicaudal = 0,0033 < 0,05 → B supera A com significância. Por si só, seria `B_GANHOU`.
- Guarda-corpos `sem_piorar` (B − A, piorar = margem cair / reclamacoes subir / optout subir):
  - `margem_media`: −0,0020 (queda ≤ 0,01) → dentro. Nota: margem só existe onde `resultado=sim`; N pequeno (15 vs 14).
  - `reclamacoes`: +0,0167 com tolerância 0,0 → **fora**. Este é o gatilho de parada antecipada previsto no próprio experimento ("uma única reclamação em B acima da taxa de A encerra o teste"). Informativo: z=1,90, p=0,057 — não significante a 95%, mas a regra do yaml é tolerância absoluta, não teste.
  - `optout`: +0,0033 (≤ 0,005) → dentro.
- Regra do contrato: `A_SEGUE` se B piora qualquer `sem_piorar` além da tolerância, mesmo com a métrica do teste subindo. Aplicada.
- Calibração do juiz (`dados/calibracao.csv`): não existe e não se aplica — a métrica do teste é objetiva (proporção no CSV), sem rubrica/juiz.
- `conversao` (métrica alvo, vigiada informativamente): A=5,00% (15/300) vs B=4,67% (14/300) — não testável neste ciclo (n=1.506/variante), sem conclusão.
