---
layout: page
title: Statement of Work
description: Alcance, fases, tareas, tiempos y entregables del proyecto SEO de openeb5.com
permalink: /sow/
nav_order: 3
---

# Statement of Work — SEO openeb5.com

> **Proyecto:** Auditoría SEO + plan de remediación
> **Duración:** 4 meses (14-may-2026 → 13-sep-2026)
> **Cliente:** Open EB5 Regional Center, McAllen, Texas

---

## 2.1 Resumen del SOW

**Objetivo del proyecto:** Llevar a `openeb5.com` desde su estado crítico actual (Health Score 29, DR 0.5, 1 visita orgánica/mes) hasta un sitio técnicamente saludable, indexado correctamente y posicionado para queries de la industria EB-5 en EE.UU. y México, en un horizonte de **4 meses**.

| Dato | Valor |
|---|---|
| Cliente | Open EB5 Regional Center |
| USCIS Status | Regional Center aprobado · proyectos I-956F activos (Midtown Pharr, Midtown Brownsville II) |
| Dirección | 3900 N. 10th St Suite 1080, McAllen, TX 78501 |
| Teléfono | +1 855 733 6325 |
| Mercados objetivo | EE.UU. · México · Latinoamérica (AR, CO, BO, GT, EC) |
| Modelo de inversión | Consultor SEO + cliente con acceso WP-admin |
| Inicio | 14 de mayo de 2026 |
| Fin estimado | 13 de septiembre de 2026 |

---

## 2.2 Alcance del trabajo · Fases mes a mes

El alcance se ejecuta en **4 fases mensuales**. Cada tabla detalla las tareas con su tiempo estimado y entregable asociado.

### Fase 1 · Mes 1 — Fundación + Performance

> **Periodo:** 14-may → 13-jun-2026
> **Horas estimadas:** 16 h
> **Objetivo:** Estabilizar la base técnica del sitio. Detener fuga de equity SEO (toxic backlinks, titles rotos, hreflang) y resolver Core Web Vitals.

| # | Tarea | Tiempo estimado | Entregable |
|---|---|---|---|
| 1.1 | Subir disavow file a GSC (94 dominios tóxicos) | 15 min | Screenshot GSC disavow upload confirmado |
| 1.2 | Fix title homepage (`USCIS-Approved EB-5 Regional Center \| Open EB5 — Texas`) | 15 min | Source HTML con title nuevo + screenshot SERP |
| 1.3 | Fix Yoast Site Representation (nombre, logo, dirección) | 30 min | Screenshot Yoast settings + verificación schema |
| 1.4 | Instalar plugin "HREFLANG Tags Lite" + cargar CSV 51 pares EN/ES | 1 h | View Source con `<link rel="alternate" hreflang>` activo |
| 1.5 | Submitar URLs `/ES/` actualizadas al sitemap | 30 min | URL sitemap_index.xml + screenshot GSC submission |
| 1.6 | Configurar 6 security headers en Cloudflare (HSTS, CSP, XFO, etc.) | 1 h | Grade A+ en securityheaders.com (screenshot) |
| 1.7 | Backup completo del sitio (UpdraftPlus) | 2 h | Archivo backup en Google Drive del cliente |
| 1.8 | Instalación + configuración WP Rocket + Cloudflare APO | 3 h | Screenshot config + PageSpeed before/after |
| 1.9 | Eliminar 7 plugins inútiles (WooCommerce, ct-mega-menu, etc.) | 2 h | Lista before/after + screenshot Plugins panel |
| 1.10 | Reemplazar Slider Revolution con Smart Slider 3 | 3 h | Comparativa LCP antes/después + sliders migrados |
| 1.11 | Fix 2 links internos rotos (`/collaborative-investments/`, `/home-onepage`) | 30 min | Crawl Screaming Frog: 0 internal 404s |
| 1.12 | Fix canonical roto `/author/user_open/` → `/author/eduardo-prato/` | 30 min | Verificación curl + screenshot Yoast author |
| 1.13 | Audit post-Fase 1 (Lighthouse + Health Score) | 1.5 h | Reporte `2026-06-13-post-fase-1.md` en `/reports/` |

**Meta de salida Fase 1:** Health Score 55 · Lighthouse Mobile 65 · CWV mobile "mejorando" · 0 links internos rotos.

---

### Fase 2 · Mes 2 — Contenido + Schema

> **Periodo:** 14-jun → 13-jul-2026
> **Horas estimadas:** 20 h
> **Objetivo:** Capturar las 6 oportunidades de keywords con KD ≤ 13 mediante páginas dedicadas + dar contexto E-E-A-T YMYL adecuado al nicho.

| # | Tarea | Tiempo estimado | Entregable |
|---|---|---|---|
| 2.1 | Rewrite titles + meta descriptions de 10 páginas hub | 2 h | CSV con before/after + screenshots Yoast |
| 2.2 | Crear página `/eb-5-visa/i-526e-processing-time/` (2,500-3,000 palabras) | 3 h | URL publicada + screenshot Yoast + FAQ schema validado |
| 2.3 | Crear página `/eb-5-visa/i-829-petition/` | 2.5 h | URL publicada + schema valid en Rich Results Test |
| 2.4 | Crear página `/eb-5-visa/source-of-funds/` | 2.5 h | URL publicada + schema valid |
| 2.5 | Crear página `/eb-5-visa/minimum-investment/` | 2.5 h | URL publicada + schema valid |
| 2.6 | Crear página `/eb-5-visa/reform-and-integrity-act-2022/` | 2.5 h | URL publicada + schema valid |
| 2.7 | Crear página `/eb-5-visa/grandfathering-deadline/` (urgencia 2027) | 2.5 h | URL publicada + schema valid |
| 2.8 | Schema FinancialService + LocalBusiness en homepage | 1.5 h | JSON-LD validado en Schema.org Validator |
| 2.9 | Schema FAQPage en las 6 páginas nuevas | 1 h | 6 validaciones pass en Rich Results Test |

**Meta de salida Fase 2:** Health Score 75 · Lighthouse Mobile 80 · CWV mobile "aprobada" · 6 páginas nuevas indexadas · +10% impresiones GSC.

---

### Fase 3 · Mes 3 — Arquitectura + Cleanup

> **Periodo:** 14-jul → 13-ago-2026
> **Horas estimadas:** 14 h
> **Objetivo:** Limpiar la herencia técnica del theme (orphans, categorías vacías, doble slash) y consolidar la arquitectura.

| # | Tarea | Tiempo estimado | Entregable |
|---|---|---|---|
| 3.1 | Construir CSV de 301 redirects (legacy → nuevas URLs) | 2 h | Archivo `redirects-301.csv` validado URL por URL |
| 3.2 | Implementar 301 redirects vía plugin Redirection | 1.5 h | Screenshot Redirection plugin + test curl 5 URLs |
| 3.3 | Eliminar 18 orphan pages identificadas | 1 h | Lista URLs + screenshot Pages panel before/after |
| 3.4 | Eliminar 23 categorías vacías del theme (heredadas) | 1.5 h | Screenshot Categories panel + verificación 410 |
| 3.5 | Eliminar 16 URLs basura (`/ct-mega-menu/*`, `/footer/*`, `/page-title/*`) | 1.5 h | Robots.txt actualizado + 410 Gone verificado |
| 3.6 | Fix 308 URLs con doble slash (causadas por Booked + WC Payments) | 2 h | Crawl Screaming Frog: 0 dobles slash |
| 3.7 | Alt text descriptivo en 154 imágenes de homepage + hubs | 3 h | CSV alt-texts + screenshot Media Library |
| 3.8 | Robots.txt actualizado con Disallow para legacy paths | 30 min | Diff robots.txt + verificación GSC |
| 3.9 | Audit post-Fase 3 (Screaming Frog full crawl) | 1 h | Reporte `2026-08-13-post-fase-3.md` |

**Meta de salida Fase 3:** Health Score 85 · Lighthouse Mobile 88 · Sitio estructuralmente limpio · 0 orphans · +13% impresiones GSC.

---

### Fase 4 · Mes 4 — Autoridad + Reporte Final

> **Periodo:** 14-ago → 13-sep-2026
> **Horas estimadas:** 10 h
> **Objetivo:** Construir señales de autoridad mediante outreach a medios legítimos del nicho (RGV + EB-5 industry) y entregar reporte ejecutivo de cierre.

| # | Tarea | Tiempo estimado | Entregable |
|---|---|---|---|
| 4.1 | Pitch + envío a EB5Investors Magazine (artículo experto) | 1.5 h | Email enviado + tracking en spreadsheet outreach |
| 4.2 | Pitch + envío a IIUSA (asociación de la industria) | 1 h | Email enviado + propuesta de colaboración |
| 4.3 | Outreach a Rio Grande Guardian (DR 61 · ya linkea) | 1 h | Email enviado · pitch press release I-956F |
| 4.4 | Outreach a RGV Business Journal (DR 32) | 1 h | Email enviado · pitch proyectos Midtown Pharr |
| 4.5 | Distribución press release I-956F Midtown Pharr | 1.5 h | Press release publicado + 5+ pickups documentados |
| 4.6 | Distribución press release Midtown Brownsville II | 1 h | Press release publicado |
| 4.7 | Compilar reporte ejecutivo final + before/after | 2 h | PDF + presentación cliente con 4 meses de data |
| 4.8 | Handoff técnico al equipo del cliente (WP-admin, GSC, Cloudflare) | 1 h | Documento handoff + sesión videocall grabada |

**Meta de salida Fase 4:** Health Score 90+ · Lighthouse Mobile 90+ · CWV aprobada · +15% impresiones/clicks orgánicos · 15 ref. domains legítimos · 8 keywords ranking top 10.

---

## 2.3 Resumen consolidado de fases

| Fase | Mes | Periodo | Foco | Horas | Tareas | Salida clave |
|---|---|---|---|---|---|---|
| **1** | Mes 1 | 14-may → 13-jun | Fundación + Performance | 16 h | 13 | Health 55 · Lighthouse 65 |
| **2** | Mes 2 | 14-jun → 13-jul | Contenido + Schema | 20 h | 9 | Health 75 · CWV aprobada · 6 páginas nuevas |
| **3** | Mes 3 | 14-jul → 13-ago | Arquitectura + Cleanup | 14 h | 9 | Health 85 · Sitio limpio · 0 orphans |
| **4** | Mes 4 | 14-ago → 13-sep | Autoridad + Reporte | 10 h | 8 | Health 90+ · +15% tráfico · 15 ref. domains |
| **TOTAL** | — | 4 meses | — | **60 h** | **39 tareas** | **Health Score 29 → 90+** |

---

## 2.4 Entregables ejecutivos por mes

| Mes | Entregable principal | Formato |
|---|---|---|
| Mes 1 | Reporte Post-Fase 1 (Fundación + Performance) | Markdown en `/reports/` + screenshots before/after |
| Mes 2 | 6 páginas SEO nuevas publicadas + reporte schema | URLs en vivo + Rich Results Test pass screenshots |
| Mes 3 | Reporte Post-Fase 3 (Arquitectura limpia) | Screaming Frog crawl comparativo + CSV cleanup |
| Mes 4 | **Reporte Ejecutivo Final + presentación cliente** | PDF ~25 páginas + deck + videocall handoff |

---

## 2.5 Out of scope (NO incluye)

| ❌ Excluido | Razón |
|---|---|
| Diseño UI/UX nuevo del sitio | Sitio mantiene diseño actual · no es rebuild |
| Migración de hosting | Stack WordPress se mantiene |
| Cambios de plataforma | Sigue WordPress (no migración a Webflow/Next.js) |
| Content writing en idiomas ≠ EN/ES | Solo inglés y español (mercado MX) |
| Campañas de pago (Google Ads, Meta Ads) | Sin presupuesto media en este SOW |
| Email marketing automation | Stack actual no requiere intervención |
| CRM integration | Fuera del scope SEO |

---

## 2.6 Supuestos y dependencias

| Supuesto | Tipo |
|---|---|
| Acceso WP-admin del cliente disponible y funcional | Crítico |
| Acceso a Google Search Console y Google Analytics | Crítico |
| Cliente acepta gasto recurrente de **$64/mes** (WP Rocket $59 anual + Cloudflare APO $5/mes) | Comercial |
| Cliente puede revisar y aprobar contenido nuevo en 48 hrs | Operativo |
| USCIS no cambia normativa EB-5 durante el proyecto | Externo (programa estable hasta 30-sep-2027) |
| Cliente provee bios + headshots del equipo para schema Person | Operativo |

---

## 2.7 Riesgos identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Disavow no surte efecto en 60 días | Media | Alto | Combinar con link building activo para diluir |
| Cliente retrasa publicación de contenido nuevo | Media | Medio | Calendar invites + canal Slack dedicado |
| Plugin removal rompe layout actual | Baja | Alto | Backup completo + staging environment previo |
| Cambio algorítmico de Google durante proyecto | Baja | Alto | Diversificar a GEO (ChatGPT/Perplexity) |
| Competidor agresivo entra al nicho | Baja | Medio | Rank tracker semanal + alertas Ahrefs |
| Outreach de Fase 4 sin respuesta | Media | Medio | Pipeline de 15+ contactos para asegurar 3-5 pickups |

---

## 2.8 KPIs de éxito · 4 meses

> **Filosofía:** Las métricas técnicas (Health Score, Lighthouse, CWV) son **alcanzables al 100%** dado el control directo sobre el código y plugins. Las métricas orgánicas (tráfico, impresiones, keywords) se proyectan **conservadoramente al +10-15% mes a mes** dada la baja autoridad inicial y el ciclo natural de indexación de Google (60-120 días).

| KPI | Baseline · 14-may | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|---|---|---|---|---|---|
| **Health Score** (auditoría) | 29 | 55 | 75 | 85 | **90+** |
| **Lighthouse Mobile** | 38 | 65 | 80 | 88 | **90+** |
| **Lighthouse Desktop** | 17 | 55 | 78 | 88 | **90+** |
| **Core Web Vitals mobile** | No aprobada | Mejorando | Aprobada | Aprobada | **Aprobada** |
| **LCP** | 7.0 s | 3.8 s | 2.4 s | 2.0 s | **< 2.0 s** |
| **Impresiones GSC** (vs baseline) | baseline | +5% | +10% | +13% | **+15%** |
| **Clicks orgánicos** (vs baseline) | baseline | +5% | +10% | +12% | **+15%** |
| **Visibility Score** (Ahrefs) | baseline | +8% | +11% | +13% | **+15%** |
| Keywords ranking top 30 | 4 | 8 | 14 | 20 | 25 |
| Keywords ranking top 10 | 0 | 1 | 3 | 5 | **8** |
| Ref. domains legítimos | 6 | 8 | 11 | 13 | **15** |
| Páginas con meta description | 16/154 | 60/154 | 120/154 | 154/154 | **100%** |

**Compromisos de cierre Mes 4:**

- Health Score y Lighthouse **superan 90/100** ✓
- Core Web Vitals **"Aprobada"** en mobile y desktop ✓
- Crecimiento orgánico **realista de +10-15%** en impresiones, clicks y visibilidad ✓
- **15 ref. domains legítimos** adicionales (vs 6 baseline) ✓
- **Reporte ejecutivo final** con before/after documentado ✓
