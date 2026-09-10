#!/usr/bin/env python3
"""Gera dados/execucoes.csv sintético para o exemplo vendas-whatsapp.
Determinístico. --seed governa as semanas 1-4, --seed2 as demais (escolhido para que a amostra reflita as taxas desenhadas — é ilustração de um efeito real, não dado real). --ate AAAA-MM-DD corta a linha do tempo (simula 'até hoje').

Linha do tempo (50 propostas/semana, seg→dom):
  sem 1–4   2026-01-05..02-01  v1 A            resposta 20%  conv 3%
  sem 5–16  2026-02-02..04-26  v1 A vs B(H1)   A 20% / B 29% ; conv 3% / 4%
  sem 17      2026-04-27..05-03  v1 A            20%   (E0001 descartado no ciclo 0002 por guarda-corpo; ciclo 0003 desenha E0002 em 05-04)
  sem 18–29   2026-05-04..07-26  v1 A vs B(H3)   A 20% / B 29% ; conv 3% / 4%
  sem 30      2026-07-27..08-02  v2 A            29%   (H3 promovida no ciclo 0004, 07-27)
Total: 1.500 linhas. Segmento 'grande' responde ~5 p.p. menos (padrão real, MODERADO).
"""
import csv, random, argparse, datetime as dt
ap = argparse.ArgumentParser(); ap.add_argument("--ate", default="2026-08-02"); ap.add_argument("--out", required=True); ap.add_argument("--seed", type=int, default=42); ap.add_argument("--seed2", type=int, default=99); ap.add_argument("--seed3", type=int, default=3)
a = ap.parse_args(); ate = dt.date.fromisoformat(a.ate)
rng0 = random.Random(a.seed); rng2 = random.Random(a.seed2); rng3 = random.Random(a.seed3); ini = dt.date(2026, 1, 5)
rows = []; pid = 0
for sem in range(1, 31):
    rng = rng0 if sem <= 4 else (rng2 if sem <= 17 else rng3)   # 1-4: seed (ciclo 0001); 5-17: seed2 (E0001); 18+: seed3 (E0002)
    for k in range(50):
        pid += 1
        d = ini + dt.timedelta(days=(sem - 1) * 7 + rng.randrange(7))
        if d > ate: continue
        if sem <= 4:   ver, var, p_resp, p_conv = "v1", "A", 0.20, 0.03
        elif sem <= 16:
            var = "A" if pid % 2 else "B"; ver = "v1"
            p_resp, p_conv = (0.20, 0.03) if var == "A" else (0.29, 0.04)
        elif sem == 17:  ver, var, p_resp, p_conv = "v1", "A", 0.20, 0.03   # semana entre E0001 e E0002
        elif sem <= 29:   # E0002: v1 A vs B(H3)
            var = "A" if pid % 2 else "B"; ver = "v1"
            p_resp, p_conv = (0.20, 0.03) if var == "A" else (0.29, 0.04)
        else:          ver, var, p_resp, p_conv = "v2", "A", 0.29, 0.04
        seg = rng.choices(["pequeno", "medio", "grande"], [0.45, 0.4, 0.15])[0]
        if seg == "grande": p_resp -= 0.05
        resp = rng.random() < p_resp
        conv = resp and rng.random() < (p_conv / p_resp)
        margem = f"{rng.uniform(0.28, 0.36):.2f}" if conv else ""
        recl = rng.random() < 0.01
        opt = rng.random() < 0.008
        rows.append([f"P{pid:04d}", d.isoformat(), ver, var, seg,
                     "sim" if resp else "não", "sim" if conv else "não", margem,
                     "sim" if recl else "não", "sim" if opt else "não",
                     f"{rng.uniform(0.6, 1.4):.2f}", rng.randrange(3, 9), ""])
rows.sort(key=lambda r: (r[1], r[0]))
with open(a.out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","data","versao","variante","segmento","resposta","resultado","margem","reclamou","optout","custo","tempo_min","observacao"])
    w.writerows(rows)
print(f"{len(rows)} linhas até {ate}")
