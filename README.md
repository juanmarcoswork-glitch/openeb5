# openeb5.com — SEO Audit (May 2026)

> 🔍 Ver la auditoría SEO completa en [GitHub Pages](https://juanmarcoswork-glitch.github.io/openeb5-seo-audit/) o `/docs/`.

Carpeta de trabajo para la auditoría SEO completa de **https://openeb5.com/** (Open EB5 — USCIS-approved EB-5 Regional Center, McAllen, TX).

## Resumen rápido

- **Health Score: 29/100 (Critical)**
- **Stack:** WordPress 6.9.4 + Yoast + Elementor Pro + Slider Revolution + WooCommerce + 23 plugins activos
- **Visibilidad orgánica (US, SEMrush):** 20 keywords · 0 tráfico estimado · Authority Score 2/100
- **Industria:** YMYL (Your Money or Your Life) — inversión + inmigración

## Archivos clave

| Archivo | Propósito |
|---|---|
| [`FULL-AUDIT-REPORT.md`](FULL-AUDIT-REPORT.md) | Reporte ejecutivo + scoring completo |
| [`ACTION-PLAN.md`](ACTION-PLAN.md) | 47 acciones priorizadas (P0–P3) |
| [`reports/technical-seo.md`](reports/technical-seo.md) | Caching, hreflang, seguridad, plugins, sitemap |
| [`reports/content-eeat.md`](reports/content-eeat.md) | YMYL, E-E-A-T, gaps de contenido, country pages |
| [`reports/schema-markup.md`](reports/schema-markup.md) | JSON-LD listo para pegar (Org, FAQ, Article, Person…) |
| [`reports/performance-cwv.md`](reports/performance-cwv.md) | Core Web Vitals (sintético) + plugin bloat |
| [`reports/geo-ai-readiness.md`](reports/geo-ai-readiness.md) | AI Overviews, ChatGPT, Perplexity, plantilla llms.txt |
| [`reports/backlinks-competitive.md`](reports/backlinks-competitive.md) | Backlinks, anchor texts, gap competitivo, keyword targets |
| [`data/`](data/) | Snapshots crudos (HTML, headers, sitemaps, robots.txt) |

## Top-5 hallazgos críticos

1. Homepage `<title>` = "OpenEB5 - openeb5" (sin keywords, marca en minúscula)
2. `Cache-Control: no-store` + PHPSESSID por visita → caché y CDN rotos
3. Sin hreflang en sitio EN/ES + 18 páginas de país; blog ES no está en sitemap
4. Cero menciones de USCIS.gov en pillar guide; sin abogado nombrado, sin disclaimers SEC, sin número de Regional Center visible
5. Schema mínimo y roto (Organization en minúsculas, BreadcrumbList con 1 item, sin LocalBusiness, sin FAQ, sin Article en blog)

## Top-5 quick wins (≤4h cada uno)

1. Corregir nombre "Open EB5" en Yoast (cascada global)
2. Reescribir title + meta de homepage
3. Instalar WP Rocket + Cloudflare
4. Eliminar plugins inútiles (WooCommerce, YITH ×2, crypto-widgets, Flickr, etc.)
5. Publicar `/llms.txt`

## Métricas competitivas (US, SEMrush)

| Dominio | Authority | Keywords | Tráfico |
|---|---|---|---|
| **openeb5.com** | **2** | **20** | **0** |
| eb5investors.com | 35 | 9,174 | 6,333 |
| iiusa.org | 34 | 2,121 | 5,486 |
| eb5affiliatenetwork.com | — | 2,862 | 1,288 |
| civitascapital.com | — | 609 | 2,755 |

## Siguiente paso — Ahrefs cross-check

Cuando adjuntes openeb5.com a Ahrefs:
- Validar DR/RD vs SEMrush AS 2
- Ahrefs Content Gap con seeds: eb5investors.com, iiusa.org, civitascapital.com, eb5capital.com
- Ahrefs Site Audit para validar issues técnicos
- Brand Radar para SOV de "Open EB5" en LLMs
- Setear keyword tracking con 15-25 targets (lista en `backlinks-competitive.md` §5)

Comparte la data y se cruza con esta auditoría para refinar el plan de 90 días.

---

**Fecha de auditoría:** 2026-05-11
**Herramientas:** WebFetch, curl, SEMrush MCP, análisis sintético de HTML/headers
