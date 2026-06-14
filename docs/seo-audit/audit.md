---
layout: page
title: Auditoría SEO completa
permalink: /seo-audit/audit/
nav_order: 2
---

# Auditoría SEO completa — openeb5.com

> **Fecha:** 14 de mayo de 2026
> **Cliente:** Open EB5 Regional Center — McAllen, Texas
> **Site:** [https://openeb5.com](https://openeb5.com)
> **Validación cruzada:** Claude Code audit (10-may-2026) + Ahrefs Site Audit CSV (11-may-2026) + Ahrefs API live (13-may-2026) + PageSpeed Insights CrUX (11-may-2026)

---

## 1.1 Resumen ejecutivo

> **Fuente:** Validación cruzada Ahrefs API en vivo (13-may-2026) vs audit Claude Code (10-may-2026)

| Métrica | Audit Claude Code (10-may) | Realidad Ahrefs API (13-may) | Delta |
|---|---|---|---|
| Domain Rating | "2" | **0.5** | Sobreestimado |
| Referring domains vivos | "93" | **38** (90/96 marcados spam) | -55 |
| Backlinks vivos | "154" | **47** | -107 |
| Keywords orgánicas | "20 US" | **4 globales** (todas ES, pos 9-12) | -16 |
| Competidores orgánicos | varios | **0** en US/MX/ES | crítico |
| Tráfico orgánico/mes | "0" | **1 visita** (mayo 2026) | confirmado |

**Conclusión:** El audit inicial sobreestimó la salud SEO del sitio. La realidad es que `openeb5.com` está en estado crítico: 17 meses estancado en DR 0.5, 0 competidores orgánicos identificados (señal de invisibilidad), y un perfil de backlinks con 94% de toxicidad.

---

## 1.2 Hallazgos críticos validados

### 1.2.1 Título de homepage roto

> **Fuente:** Crawl Ahrefs 11-may-2026 + Yoast HTML inspeccionado

- Title actual: literalmente `OpenEB5 - openeb5` (17 caracteres, sin keywords)
- **94 de 154 URLs** tienen el patrón `[Page] - openeb5` con minúscula
- Causa raíz: Yoast → Site Representation mal configurado (nombre del sitio = "openeb5" minúscula)

### 1.2.2 Hreflang inexistente

> **Fuente:** Análisis Ahrefs Site Audit + verificación manual

- 0 hreflang tags en 30,151 links analizados
- 51 pairs EN ⇄ ES sin declarar
- 57 URLs `/ES/` NO están incluidas en `sitemap_index.xml`

### 1.2.3 Core Web Vitals destruidos

> **Fuente:** PageSpeed Insights (CrUX real, 11-may-2026)

| Métrica | Valor | Umbral aprobación | Estado |
|---|---|---|---|
| LCP (Largest Contentful Paint) | 7.0 s | < 2.5 s | 🔴 Crítico |
| TTFB (Time to First Byte) | 2.5 s | < 0.8 s | 🔴 Crítico |
| FCP (First Contentful Paint) | 6.4 s | < 1.8 s | 🔴 Crítico |
| Mobile Web Vitals Assessment | "No aprobada" | "Aprobada" | 🔴 Crítico |
| Performance Score Lighthouse Mobile | 38/100 | 90+ | 🔴 Crítico |
| Performance Score Lighthouse Desktop | 17/100 | 90+ | 🔴 Crítico |

### 1.2.4 Headers de seguridad ausentes

> **Fuente:** curl headers test 13-may-2026

- HSTS: No presente
- Content-Security-Policy: No presente
- X-Frame-Options: No presente
- Cross-Origin-Opener-Policy: No presente

### 1.2.5 Otros issues técnicos críticos

> **Fuente:** Ahrefs Site Audit + Claude Code audit

- **138 de 154 páginas** sin meta description
- **18 orphan pages** (sin enlaces internos entrantes)
- **23 categorías vacías** (theme inheritance: `/category/business/`, `/tag/builder/`, `/portfolio-category/*`, etc.)
- **75 enlaces internos** apuntando a `demo.casethemes.net` (plugin `ct-mega-menu` con demo en producción)
- **308 URLs con doble slash** (causadas por plugins Booked + WooCommerce-payments)
- **2 links internos a 404s:** `/collaborative-investments/`, `/home-onepage`
- **Canonical roto:** `/author/user_open/` → `/author/yarrdo/` (404)

---

## 1.3 Perfil de backlinks tóxicos

> **Fuente:** Ahrefs Site Explorer API 13-may-2026

**90 de 96 referring domains marcados como spam por Ahrefs.** Anchors literales encontrados:

- "Boost openeb5.com For Ahrefs DR with Quality Dofollow Backlinks"
- "Premium SEO Backlinks openeb5.com Gambling/Casino/Crypto"
- "Skyrocket openeb5.com SEO Using SeoZumi.com"

**TLDs problemáticos predominantes:** `.shop`, `.click`, `.agency`, PBN marketplaces.

**6 dominios legítimos identificados (a preservar en disavow):**

| Dominio | DR | Tipo |
|---|---|---|
| riograndeguardian.com | 61 | Medio local |
| seoexpress.org | 74 | Directorio SEO |
| host.io | — | Hosting info |
| rgvbusinessjournal.com | 32 | Medio local |
| rgv.news | — | Medio local |
| tpvinh.vn | — | Asiático legítimo |

**Acción crítica P0:** subir `disavow-openeb5.txt` (94 dominios) a Google Search Console **antes que cualquier otra acción**.

---

## 1.4 Keywords actuales y oportunidades

> **Fuente:** Ahrefs Keywords Explorer + Site Explorer 13-may-2026

### Keywords donde openeb5.com YA rankea (todas ES, posiciones 9-12)

| Keyword | País | KD | Volumen | Pos actual |
|---|---|---|---|---|
| que es green card | BO/GT/EC | 4-5 | 40-100 | 9-12 |
| visa eb-5 | MX | 2 | 150 | ~10 |
| visa de inversionista | MX | 4 | 300 | ~11 |
| visa eb5 | MX | 9 | 200 | ~12 |

### Tier 1 oportunidades (KD ≤ 13, atacar primero)

| Keyword | KD | Volumen US | Traffic Potential | Intent |
|---|---|---|---|---|
| i-526e processing time | **0** | 150 | **170,000** | Informational |
| i-829 petition | 1 | 30 | 800 | Informational |
| eb-5 source of funds | 0 | 10 | — | Informational |
| eb-5 minimum investment | 6 | 30 | **20,000** | Informational |
| eb-5 reform and integrity act | 13 | — | — | Informational |
| eb-5 grandfathering | 0 | 0 | — | Informational |

### Tier 2 oportunidades (KD intermedio, atacar en mes 2-3)

| Keyword | KD | Volumen US | Traffic Potential |
|---|---|---|---|
| eb-5 priority date | 31 | 20 | **355,000** |
| eb-5 investment | 40 | 100 | 20,000 |
| green card investment | 43 | 70 | 700 |

---

## 1.5 Comparativa de auditorías (3 ángulos)

> **Fuente:** Triangulación entre Claude Code HTML audit + Ahrefs Site Audit CSV + Ahrefs API live

| Ángulo | Hallazgo único | Coincidencia con otros |
|---|---|---|
| Claude Code HTML | Detectó plugins demo + estructura WP | ✓ Confirmado por Ahrefs |
| Ahrefs Site Audit | Tóxicos + CWV + hreflang | ✓ Confirmado por API |
| Ahrefs API live | DR real 0.5 + 0 competidores | Único, no detectable en otros |
| PageSpeed CrUX | LCP/TTFB real-user data | Único, no detectable en otros |

**Lección clave:** los audits estáticos del HTML no detectan el problema más grave (toxicidad de backlinks). Sin la verificación API, la auditoría Claude Code estaba diagnosticando un problema técnico cuando el problema principal es de autoridad/reputación.

---

## 1.6 Estado de visualizaciones generadas

> Referencia para handoff. Estos artefactos viven en Miro/local, no necesariamente en el repo.

- ✅ Board Miro "openeb5.com — Arquitectura jerárquica (Tree)": [https://miro.com/app/board/uXjVHT7ICPE=/](https://miro.com/app/board/uXjVHT7ICPE=/)
- ✅ Organigrama vertical clásico (mismo board, zona Y=5800+)
- ⚠️ Board confuso por categoría (a borrar manualmente): [https://miro.com/app/board/uXjVHT3U_Y4=/](https://miro.com/app/board/uXjVHT3U_Y4=/)
- ✅ `disavow-openeb5.txt` (94 dominios)
- ✅ `hreflang-mapping-openeb5.csv` (51 pairs EN/ES)
