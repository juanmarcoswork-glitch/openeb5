---
layout: page
title: Estrategia de keywords Q3 2026
permalink: /seo-audit/keyword-strategy/
nav_order: 6
---

# Estrategia de keywords Q3 2026

## 5.1 Contexto del nicho

**EB-5 es un nicho B2C/HNW (High Net Worth) con búsquedas concentradas en:**

- EE.UU. (usuarios buscando información sobre el programa)
- México (mercado emisor #1 actualmente)
- China, India, Vietnam, Taiwán (mercados históricos asiáticos)
- Brasil, Argentina, Colombia (mercados LATAM emergentes)

**Estacionalidad observada:**

- **Q1 (ene-mar):** Pico de búsquedas tras anuncios de cambios USCIS (renewals, deadlines)
- **Q3 (jul-sep):** Pico secundario por planificación fiscal de fin de año
- **Sep 30, 2027:** Deadline crítico de "grandfathering" — generará demanda en queries específicas

---

## 5.2 KWs Tier 1 (atacar primeros 30 días — KD ≤ 13)

> **Fuente:** Ahrefs Keywords Explorer US, consultado 13-may-2026

| Keyword | KD | Volumen | TP | Página propuesta | Prioridad |
|---|---|---|---|---|---|
| **i-526e processing time** | 0 | 150 | 170,000 | `/eb-5-visa/i-526e-processing-time/` | P0 |
| **i-829 petition** | 1 | 30 | 800 | `/eb-5-visa/i-829-petition/` | P0 |
| **eb-5 source of funds** | 0 | 10 | — | `/eb-5-visa/source-of-funds/` | P1 |
| **eb-5 minimum investment** | 6 | 30 | 20,000 | `/eb-5-visa/minimum-investment/` | P0 |
| **eb-5 reform and integrity act** | 13 | — | — | `/eb-5-visa/ria-2022/` | P1 |
| **eb-5 grandfathering** | 0 | 0 | — | `/eb-5-visa/grandfathering-deadline/` | P0 (urgencia 2027) |

**Estructura recomendada para cada página de KW Tier 1:**

```markdown
# H1 — Keyword exacta + año actual
## Resumen ejecutivo (150 palabras, answer box)
## ¿Qué es {keyword}? (definición clara)
## Proceso paso a paso
## Documentos requeridos
## Tiempos estimados (tabla con datos USCIS)
## Costos asociados
## Errores comunes a evitar
## FAQ (8-10 preguntas, formato FAQPage schema)
## CTA al cuestionario o contacto
```

Longitud objetivo: **2,500-3,000 palabras** por página.

---

## 5.3 KWs Tier 2 (atacar mes 2-3 — KD 31-43)

| Keyword | KD | Volumen | TP | Página propuesta |
|---|---|---|---|---|
| eb-5 priority date | 31 | 20 | 355,000 | `/eb-5-visa/priority-date/` |
| eb-5 investment | 40 | 100 | 20,000 | `/eb-5-visa/investment-overview/` |
| green card investment | 43 | 70 | 700 | `/eb-5-visa/green-card-investment/` |

---

## 5.4 KWs en español Tier 1 (México prioridad)

> **Fuente:** Ahrefs Keywords Explorer MX, consultado 13-may-2026

| Keyword | KD | Volumen MX | Página actual ES | Acción |
|---|---|---|---|---|
| visa de inversionista | 4 | 300 | (no existe página dedicada) | **Crear `/ES/visa-eb-5/inversionista/`** |
| visa eb5 | 9 | 200 | rankea pos ~12 | **Optimizar título + contenido + internal linking** |
| visa eb-5 | 2 | 150 | rankea pos ~10 | **Mejorar a top 5 con FAQ y schema** |
| visa inversionista estados unidos | — | 100 | (no existe) | **Crear página dedicada** |
| green card por inversion | — | 60 | (página enterrada depth 4) | **Mover a depth 2 + interconectar** |
| como obtener green card | 2 | 40 | 1 visita/mes | **Optimizar con KD bajo es la ganadora barata** |

---

## 5.5 Demanda creciente identificada para Q3 2026

Basado en análisis estacional y eventos políticos esperados:

1. **"i-526e processing time"** — esperado +30% por backlogs USCIS publicados Q2-2026
2. **"eb-5 grandfathering"** — crecerá fuerte al acercarse deadline sep-2027 (~12 meses)
3. **"eb-5 priority date"** — pico anticipado en China e India por retrogresión
4. **"visa eb-5 mexico"** — crecimiento sostenido por aumento de aplicantes mexicanos

---

## 5.6 Estrategia de internal linking para boost rápido

> Las 5 páginas que generen tráfico inicial deben recibir links desde 10+ páginas hub.

**Plan de internal links a `/eb-5-visa/i-526e-processing-time/` (página estrella):**

- Link desde Home (hero section + sidebar)
- Link desde `/eb-5-visa/` (hub principal, en H2)
- Link desde cada uno de los 19 blog posts EN (en CTAs contextuales)
- Link desde `/projects/midtown-pharr/` (porque incluye I-956F context)
- Link desde footer global
- Link desde `/about/team/` (citando expertise)

**Anchor text variado (importante para no parecer manipulativo):**

- "I-526E processing time"
- "tiempos de procesamiento USCIS"
- "cuánto tarda la I-526E"
- "EB-5 application timeline"
- "see latest USCIS data"

---

## 5.7 Schema markup obligatorio por tipo de página

| Tipo de página | Schemas obligatorios |
|---|---|
| Home | `Organization`, `LocalBusiness`, `FinancialService`, `WebSite` |
| Hubs (`/eb-5-visa/`) | `Article`, `BreadcrumbList` |
| Páginas Tier 1 KW | `Article`, `FAQPage`, `BreadcrumbList`, `HowTo` (donde aplique) |
| Blog posts | `BlogPosting`, `Author`, `BreadcrumbList` |
| Proyectos | `Place`, `RealEstateAgent`, `Investment` |
| Contact | `ContactPoint` |

---

## 5.8 Generative Engine Optimization (GEO)

Para que `openeb5.com` aparezca en respuestas de ChatGPT/Perplexity/Gemini:

1. **Estructura de Q&A explícita** en cada página (formato pregunta-respuesta)
2. **Atribuciones claras** (cita USCIS, cita el año, cita expertos nombrados)
3. **Datos concretos** (números, tablas, fechas)
4. **Schema FAQPage** en todas las páginas de información
5. **Mencionar entidades relacionadas** (USCIS, I-526E, I-829, Regional Center, RGV, McAllen)
