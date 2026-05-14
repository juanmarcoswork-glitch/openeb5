---
layout: page
title: Statement of Work — SEO openeb5.com
permalink: /sow/
nav_order: 3
---

# Statement of Work — SEO openeb5.com

## 2.1 Resumen del SOW

**Objetivo del proyecto:** Llevar a `openeb5.com` de DR 0.5 / 1 visita orgánica mensual a un sitio que rankee top 10 en EE.UU. y México para queries comerciales de la industria EB-5, en horizonte de 12 meses.

**Cliente:** Open EB5 Regional Center, McAllen, Texas
**USCIS Status:** Regional Center aprobado, proyectos I-956F activos (Midtown Pharr, Midtown Brownsville II)
**Dirección oficina:** 3900 N. 10th St Suite 1080, McAllen, TX 78501
**Teléfono:** +1 855 733 6325

**Mercados objetivo:**

1. EE.UU. (inversionistas internacionales que buscan inglés)
2. México (mercado primario LATAM, búsquedas en español)
3. Latinoamérica (Argentina, Colombia, Bolivia, Guatemala, Ecuador)

**Modelo de inversión:** Tiempo estimado del consultor SEO + tiempo del cliente con acceso WP-admin.

---

## 2.2 Alcance del trabajo (12 semanas, 30+ horas)

### Fase 0 — Quick wins de emergencia (Días 1-5, 8 horas)

Ver detalle completo en [`technical-fixes-5days.md`](./technical-fixes-5days/). Resumen:

1. Subir disavow file a GSC (15 min) — **P0 CRÍTICO**
2. Fix title homepage (15 min) — **P0 CRÍTICO**
3. Fix Yoast Site Representation (30 min)
4. Implementar hreflang con plugin "HREFLANG Tags Lite" (1 h)
5. Submitar URLs /ES/ al sitemap (15 min)
6. Headers de seguridad vía Cloudflare (30 min)

### Fase 1 — Performance (Semana 2, 8 horas)

7. WP Rocket + Cloudflare APO ($59 + $5/mes) — instalación y configuración (3 h)
8. Eliminar 7 plugins innecesarios (WooCommerce, ct-mega-menu, crypto widget, etc.) (2 h)
9. Reemplazar Slider Revolution con Smart Slider 3 (3 h)

### Fase 2 — On-page y contenido (Semanas 3-6, 18 horas)

10. Reescribir titles de 10 páginas hub (2 h)
11. Crear 6 páginas nuevas atacando KD≤13 (16 h):
    - `/i-526e-processing-time/`
    - `/i-829-petition/`
    - `/eb-5-source-of-funds/`
    - `/eb-5-minimum-investment/`
    - `/eb-5-reform-and-integrity-act/`
    - `/eb-5-grandfathering/`
12. Schema FinancialService + LocalBusiness en homepage (2 h)

### Fase 3 — Cleanup arquitectónico (Semanas 7-9, 10 horas)

13. Eliminar 18 orphan pages
14. Eliminar 23 categorías vacías del theme
15. Eliminar 16 URLs basura (`/ct-mega-menu/*`, `/footer/*`, etc.)
16. Fix 308 URLs con doble slash
17. Fix canonical roto `/author/user_open/`
18. Alt text en 154 imágenes

### Fase 4 — Link building y outreach (Semanas 10-12, 6 horas)

19. Outreach a EB5Investors Magazine
20. Outreach a IIUSA
21. Outreach a Rio Grande Guardian (DR 61 — already linking)
22. Outreach a RGV Business Journal (DR 32)
23. Press release I-956F Midtown Pharr para distribución

---

## 2.3 Entregables

| Entregable | Formato | Semana |
|---|---|---|
| Disavow file aplicado | GSC screenshot | 1 |
| Yoast config fix | WP screenshot | 1 |
| Hreflang activo | Source code + Screaming Frog export | 1 |
| Sitemap actualizado | URL + GSC submission proof | 1 |
| Performance audit post-WP Rocket | PageSpeed Insights screenshot | 2 |
| 6 páginas nuevas publicadas | URLs + screenshots Yoast | 3-6 |
| Schema validator pass | Google Rich Results Test screenshots | 6 |
| Cleanup completado | URL list de elementos eliminados | 9 |
| Outreach pipeline | Spreadsheet con 50+ contactos | 12 |

---

## 2.4 Out of scope (NO incluye)

- Diseño UI/UX nuevo (sitio mantiene diseño actual)
- Migración de hosting
- Cambios de plataforma (sigue WordPress)
- Content writing en idiomas distintos a EN/ES
- Campañas de pago (Google Ads, Meta Ads)
- Email marketing automation
- CRM integration

---

## 2.5 Supuestos y dependencias

- Acceso WP-admin del cliente disponible y funcional
- Acceso a Google Search Console y Google Analytics
- Cliente acepta gasto recurrente de $64/mes (WP Rocket $59 anual + Cloudflare APO $5/mes)
- Cliente puede revisar y aprobar contenido nuevo en 48 hrs
- USCIS no cambia normativa EB-5 durante el proyecto (riesgo bajo, programa estable hasta 30-sep-2027)

---

## 2.6 Riesgos identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Disavow no surte efecto en 60 días | Media | Alto | Combinar con link building activo para diluir |
| Cliente retrasa publicación de contenido nuevo | Media | Medio | Calendar invites + Slack channel |
| Plugin removal rompe layout actual | Baja | Alto | Backup completo previo + staging environment |
| Cambio algorítmico de Google | Baja | Alto | Diversificar a search engines + GEO (ChatGPT/Perplexity) |
| Competidor agresivo entra al nicho | Baja | Medio | Monitorear con rank tracker semanal |

---

## 2.7 KPIs de éxito

| KPI | Baseline (mayo 2026) | Meta mes 3 | Meta mes 6 | Meta mes 12 |
|---|---|---|---|---|
| Domain Rating | 0.5 | 8 | 15 | 25 |
| Tráfico orgánico/mes | 1 | 50 | 500 | 5,000 |
| Keywords rankeando top 10 | 0 | 5 | 25 | 100 |
| Referring domains legítimos | 6 | 15 | 35 | 80 |
| Core Web Vitals (mobile) | "No aprobada" | "Aprobada" | "Aprobada" | "Aprobada" |
| Lighthouse Mobile Score | 38 | 75 | 85 | 90+ |
| Leads orgánicos cualificados/mes | 0 | 2 | 10 | 30 |
