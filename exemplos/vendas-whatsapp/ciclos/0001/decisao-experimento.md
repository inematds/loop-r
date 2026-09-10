# Decisão sobre o desenho do experimento — ciclo 0001

**[DECISÃO SIMULADA pelo runner para o exemplo de referência — no uso real quem responde é o aprovador (L1).]**

O Experimentador escalou: a expectativa do Otimizador (17% → 22%) exige 985/variante = 40 semanas, acima do teto de 16.

Decisão: dimensionar o teste pelo **efeito mínimo que vale detectar**, já declarado no yaml (`metrica_sinal.alvo: 0.30`, i.e. 17% → 30%), não pelo palpite do Otimizador. Se B entregar só 22%, o veredito será `A_SEGUE` — aceitável: efeito menor que isso não paga o ciclo. Recalcular amostra e duração com essa base.

— 2026-02-02 · Nei (simulado)
