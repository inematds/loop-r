# 🔁 LOOP-R — Marco para sistemas y empresas que se mejoran

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

> No le pidas a la IA que mejore. Haz que cada ejecución produzca evidencia, que cada evidencia genere una hipótesis y que cada hipótesis se convierta en un experimento. Solo lo comprobado entra en la siguiente versión.

LOOP-R convierte un proceso de tu negocio (propuestas, atención al cliente, contenido…) en un **ciclo de mejora con registro y botón para volver atrás**: nueve asistentes de IA con funciones separadas ejecutan, miden, critican, proponen, prueban, evalúan, conservan la memoria y vigilan su propio costo. **El sistema nunca sustituye la versión actual por otra peor.**

## 📖 Guía de uso

Guía completa (presentación + paso a paso): **https://inematds.github.io/loop-r/guia/es/**

## 🎓 Curso

**LOOP-R: Tu empresa aprende por sí sola** — 5 rutas, 21 clases (~7,5 h), para propietarios y gestores de 40 años o más sin conocimientos técnicos: **https://inematds.github.io/loop-r/curso/es/**

## Qué garantiza (y qué no)

| Garantiza | No garantiza |
|---|---|
| **Sin regresiones** — una versión peor nunca entra en producción | que el número aumente |
| **Auditabilidad** — cada versión, prueba y decisión queda registrada; `reverter` vuelve atrás con un comando | que cada ciclo genere una buena hipótesis |
| **Constancia del proceso** — el ciclo se ejecuta siempre de la misma manera | que el costo compense sin que lo revises |
| **Límite de costo** — se detiene al alcanzarlo | — |

Lee [docs/06-critica-e-viabilidade.md](docs/06-critica-e-viabilidade.md) antes de esperar algo más (documento en portugués).

## Empezar (Claude Code)

```bash
git clone https://github.com/inematds/loop-r && cd loop-r
claude
> /loop-r iniciar
```

El comando `iniciar` hace **5 preguntas** y lo prepara todo:

1. ¿Qué proceso y qué número quieres mover, de qué valor a cuál?
2. ¿Dónde se registra el resultado de cada ejecución? (hoja de cálculo)
3. ¿Qué no puede cambiar nunca la IA por su cuenta? ¿Qué no debe empeorar?
4. ¿Cuánto puede gastar cada ciclo? ¿Por semana o por mes?
5. ¿Apruebas cada cambio (L1) o solo quieres ver propuestas (L0)?

Después:

```
/loop-r ciclo      # ejecuta los 9 agentes → ciclos/NNNN/
/loop-r decidir    # tarjeta de cinco líneas: aprobar / rechazar / esperar
/loop-r promover   # la candidata pasa a ser la versión oficial (commit)
/loop-r reverter   # restaura la versión anterior (commit)
/loop-r status
```

## Estructura

```
loop-r.yaml             ficha del ciclo (5 respuestas + valores inferidos) docs/03
.claude/agents/         9 agentes: qué lee, escribe, decide y evita        docs/04
.claude/skills/loop-r/  el runner (/loop-r ...)
versoes/                v1, v2… + atual → vN (git = promoción/rollback)
dados/                  execucoes.csv (adaptador universal) + esquema
evals/                  rúbrica sí/no, muestra mínima y casos
ciclos/NNNN/            manifiesto + salida de cada agente + decisión
memoria/                ledger, aprendizajes, descartados, observado-no-probado
exemplos/vendas-whatsapp/ ciclo de referencia completo (4 ciclos ejecutados)
docs/                   visión, crítica, arquitectura, especificación, agentes, medición, roadmap, curso
```

## Ejemplo ejecutado

[`exemplos/vendas-whatsapp/`](exemplos/vendas-whatsapp/) — clínica estética, propuestas por WhatsApp, 1.500 filas sintéticas y 4 ciclos ejecutados de verdad por los agentes: muestra insuficiente (0001), descarte por una barrera —y la corrección de tolerancia que nos enseñó (0002)—, nuevo experimento (0003) y promoción a v2 (0004). **Lee primero el [README del ejemplo](exemplos/vendas-whatsapp/README.md)** (en portugués): explica qué es real (los agentes) y qué es simulado (datos y decisiones). Después, `memoria/ledger.md` y `ciclos/*/manifesto.md`.

## Documentación

[docs/README.md](docs/README.md): empieza por la **visión** (01) y la **crítica** (06). Los documentos están en portugués.

## Versión

`0.1.0` — runner de Claude Code, adaptador CSV, L0/L1 y metaagente en modo de informe. Consulta la [hoja de ruta](docs/07-roadmap.md) (en portugués).

---

INEMA · [inema.club](https://inema.club) · [inema.pro](https://inema.pro)

## Videos

[Mira las 5 rutas en video](https://inematds.github.io/loop-r/videos/es.html) (PT/EN/ES), con capítulos y subtítulos.
