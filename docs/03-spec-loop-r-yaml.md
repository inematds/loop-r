# 03 — Spec do `loop-r.yaml`

O contrato do loop. Gerado pelo `/loop-r iniciar` a partir das 5 respostas ([01 §2](./01-visao-produto.md)); o resto é preenchido com defaults que a pessoa confirma. Lido por todos os agentes e pelo runner.

---

## 1. Campos obrigatórios (vêm da pessoa — não inferíveis)

```yaml
# ── 1. OBJETIVO COM NÚMERO ─────────────────────────────────────────
objetivo:
  processo: "Proposta comercial por WhatsApp"
  metrica_alvo:
    nome: "conversao"
    definicao: "proposta enviada que virou pedido pago em até 15 dias"
    coluna_csv: "resultado"
    atual: 0.03
    alvo: 0.05
    direcao: maximizar            # maximizar | minimizar

# ── 2. ONDE NASCE A EVIDÊNCIA ──────────────────────────────────────
evidencia:
  fonte: csv                      # v0.1: só csv. v1+: sheets | whatsapp | hubspot ...
  arquivo: dados/execucoes.csv
  unidade: "uma linha por proposta enviada"
  volume_estimado_por_semana: 50  # usado para calcular duração de testes

# ── 3. O QUE NUNCA MUDA SOZINHO ────────────────────────────────────
guarda_corpos:
  invariaveis:                    # o Guardião veta qualquer hipótese que toque nisso
    - "desconto acima de 10%"
    - "prometer prazo de entrega"
    - "contatar quem pediu para não receber mensagens"
    - "mencionar concorrentes pelo nome"
  sem_piorar:                     # métricas que a nova versão NÃO pode piorar
    - nome: "margem_media"
      coluna_csv: "margem"
      tolerancia: 0.0             # 0 = nem um pouco
    - nome: "reclamacoes"
      coluna_csv: "reclamou"
      tolerancia: 0.0

# ── 4. TETO ────────────────────────────────────────────────────────
teto:
  custo_por_ciclo_brl: 50
  ciclo: semanal                  # diario | semanal | quinzenal | mensal
  max_hipoteses_por_ciclo: 3
  max_testes_simultaneos: 1

# ── 5. QUEM APROVA ─────────────────────────────────────────────────
autonomia:
  nivel: L1                       # L0 propõe | L1 humano aprova promoção | L2 auto-promove c/ rollback
  aprovador: "Nei"
  prazo_decisao_dias: 7           # sem resposta ⇒ NÃO promove
```

---

## 2. Campos inferidos (o sistema propõe, a pessoa confirma)

```yaml
# ── SINAL FORTE (métrica rápida, antes da métrica de dinheiro) ─────
metrica_sinal:
  nome: "taxa_resposta"
  definicao: "cliente respondeu qualquer coisa que não seja recusa em 48h"
  coluna_csv: "resposta"
  atual: 0.20
  alvo: 0.30                      # proposto pelo gerador; a pessoa confirma
  # Loop otimiza esta primeiro; conversao vira sem_piorar até ter volume

# ── EXPERIMENTO ────────────────────────────────────────────────────
experimento:
  confianca: 0.95
  poder: 0.80
  amostra_minima_por_variante: 300   # calculado pelo Experimentador → evals/amostra-minima.md
  duracao_estimada_semanas: 12       # = amostra*2 / volume_semanal, arredondado p/ cima
  n_minimo_para_padrao: 30           # Crítico só afirma padrão de segmento com N ≥ isto

# ── EVAL DE ARTEFATO (gira rápido, sem esperar cliente) ────────────
eval_artefato:
  rubrica: evals/rubrica.md          # critérios binários
  casos: evals/casos/                # 20–50 entradas de teste
  juiz:
    modo: pares_embaralhados         # A/B em ordem aleatória, 3 repetições, maioria
    repeticoes: 3
    calibracao: dados/calibracao.csv # 10–20 exemplos com nota humana
    concordancia_minima: 0.80        # abaixo disto ⇒ juiz suspenso, ciclo não promove

# ── ROLLBACK ───────────────────────────────────────────────────────
rollback:
  gatilho: "metrica_alvo ou qualquer sem_piorar abaixo do limiar por 1 ciclo após promoção"
  acao: "atual → versão anterior; commit; linha no ledger"
  automatico: false                  # true só em L2

# ── MODELOS POR AGENTE (v1 CLI; no v0.1 Claude Code decide) ────────
modelos:
  leitura:    { agentes: [observador, memoria], modelo: pequeno }
  raciocinio: { agentes: [critico, otimizador, experimentador, avaliador, meta-agente], modelo: grande }
  guardiao:   { modelo: grande, temperatura: 0 }

# ── META-AGENTE ────────────────────────────────────────────────────
meta:
  modo: relatar                      # relatar (v0.1/v1) | propor (v2) — nunca "agir"
  alertas:
    ciclos_sem_promocao: 5           # ⇒ sugerir reduzir cadência / custo
    taxa_veto_guardiao: 0.5          # ⇒ Otimizador desalinhado com guarda-corpos (conta hipóteses DISTINTAS, não reapresentações)
```

---

## 3. Metadados (gerados)

```yaml
meta_info:
  criado_em: 2026-09-10
  versao_spec: 0.1
  versao_atual: v1
  ciclos_rodados: 0
  ultima_promocao: null
```

---

## 4. Regras de validação (o runner recusa o yaml se…)

1. `metrica_alvo.atual` e `alvo` ausentes ou iguais.
2. `guarda_corpos.invariaveis` vazio — **não é permitido rodar sem invariáveis**. Mínimo 1.
3. `guarda_corpos.sem_piorar` vazio — mínimo 1 (Goodhart, [06 §4](./06-critica-e-viabilidade.md)).
4. `teto.custo_por_ciclo_brl` ausente.
5. `autonomia.nivel: L2` com `meta_info.ciclos_rodados < 5` ou sem 5 promoções corretas no ledger.
6. `evidencia.arquivo` não existe ou não bate com `dados/esquema.md`.
7. `eval_artefato.juiz.calibracao` ausente quando a métrica-alvo é subjetiva.

---

## 5. Exemplo completo mínimo (o que `/loop-r iniciar` gera de 5 frases)

Entrada da pessoa, em texto:

> 1. "Quero que minhas propostas no WhatsApp fechem mais: hoje 3 em 100 fecham, quero 5."
> 2. "Anoto tudo numa planilha, uma linha por proposta, tem uma coluna 'fechou'."
> 3. "Nunca dar mais de 10% de desconto, nunca prometer prazo, não mandar pra quem pediu pra parar."
> 4. "Uns 50 reais por semana de IA tá bom. Roda uma vez por semana."
> 5. "Eu aprovo cada mudança."

Saída: o yaml das §1 + §2 acima, com `metrica_sinal` proposta ("taxa de resposta") e a frase ao final:

> *"Com 50 propostas por semana, provar 3% → 5% leva ~60 semanas. Vou otimizar primeiro a **taxa de resposta** (precisa de ~12 semanas) e vigiar a conversão. Confirma?"*

Essa frase é o produto dizendo a verdade na primeira tela ([06 §3](./06-critica-e-viabilidade.md)).
