# openeb5.com + /ES — Auditoría SEO

> 📊 **Panel en vivo:** https://juanmarcoswork-glitch.github.io/openeb5/seo-audit/

Carpeta de trabajo de la auditoría SEO de **openeb5.com** y **openeb5.com/ES/** (Open EB5, Centro Regional EB-5 aprobado por USCIS, McAllen, Texas).

## Estado actual: 29 de octubre de 2026

| | |
|---|---|
| **Score** | **87/100** en vivo · 47 de 56 tareas cerradas |
| **Alcance** | 130 URLs de los dos sitemaps (69 EN + 61 ES) + 28 destinos de enlace interno |
| **Sector** | YMYL (inmigración + inversión) |
| **Stack** | Dos instalaciones de WordPress separadas, tema custom `openeb5` en ambas, Yoast, Elementor, NitroPack (solo EN) |
| **Visibilidad orgánica** | 17 keywords · 36 visitas/mes estimadas (28 Oct 2026). Eran 4 y 1 en agosto |

## Revisiones

| Documento | Fecha | Alcance | Score |
|---|---|---|---:|
| [`RE-AUDIT-2026-10-29.md`](RE-AUDIT-2026-10-29.md) | 29 Oct 2026 | **Vigente.** EN + ES, 130 URLs | 87 |
| [`RE-AUDIT-2026-10.md`](RE-AUDIT-2026-10.md) | 13 Oct 2026 | EN + ES, 138 URLs | 70 |
| [`RE-AUDIT-2026-09.md`](RE-AUDIT-2026-09.md) | 7 Sep 2026 | EN + ES, 130 URLs | 68 |
| [`AUDIT-2026-08-EN-ES.md`](AUDIT-2026-08-EN-ES.md) | 7 Ago 2026 | EN + ES, 215 URLs. Primera auditoría del sitio español | 58 |
| [`SCOPE-OF-WORK-2026-08.md`](SCOPE-OF-WORK-2026-08.md) | 7 Ago 2026 | Plan de 30 días + fases 2 y 3 | — |
| [`FULL-AUDIT-REPORT.md`](FULL-AUDIT-REPORT.md) | 11 May 2026 | Histórico. Solo inglés, tema Consultio | 29 |
| [`ACTION-PLAN.md`](ACTION-PLAN.md) | 11 May 2026 | Histórico. 47 acciones P0-P3 | — |

El score baja de 62 (junio, solo inglés) a 58 (agosto) porque cambia el **alcance de la medición**, no porque hubiera retroceso: en agosto se empieza a medir también `/ES/`, que nunca se había auditado.

## Los tres hallazgos que definen el trabajo

1. **El sitio español es el activo orgánico.** Cinco de las siete posiciones registradas apuntan a `/ES/` (#6 Argentina, #7 España, #8 Chile, #9 México para "eb5"), y es justo el que quedó fuera de las Fases 1-4.
2. **Son dos instalaciones de WordPress, no un sitio multiidioma.** Derivar URLs del otro idioma desde `home_url()` fue la causa del hreflang invertido y del árbol fantasma `/ES/ES/`, que sobrevivió tres auditorías porque en el sitio inglés el mismo código funciona.
3. **Sin enlaces entrantes no hay competencia posible.** 4 keywords orgánicas y 1 visita al mes. Lo técnico ya está casi resuelto; lo que falta es autoridad, y eso es la Fase 3 del SOW.

## Estructura

```
├── RE-AUDIT-2026-09.md          revisión vigente
├── AUDIT-2026-08-EN-ES.md       revisión anterior
├── SCOPE-OF-WORK-2026-08.md     alcance, fases y entregables
├── docs/
│   ├── index.html               landing de GitHub Pages
│   ├── seo-audit/index.html     panel interactivo (el entregable que ve el cliente)
│   └── theme-preview/           mockup del tema, ya en producción
├── data/                        scripts de crawl y verificación
└── reports/                     informes por área (mayo 2026)
```

## Scripts de verificación

En [`data/`](data/). Todos leen del sitio en vivo, no de snapshots.

| Script | Qué hace |
|---|---|
| `reaudit.py` | Crawl y extracción de `title`, `description`, `H1`, `canonical`, `hreflang`, `lang`, palabras, `alt`, scripts, hojas de estilo y bundles de plugin |
| `check_anchors.py` | Comprueba si cada ancla del plan de enlazado interno existe en la página de origen |
| `test_autolink_full.py` | Puerto del algoritmo de `inc/internal-links.php` a Python. Verifica contra el HTML real que ningún ancla genere un `<a>` anidado y que el número de enlaces crezca exactamente en el número de anclas aplicadas |
| `xlsx2csv.py` | Convierte a CSV los XLSX del plan de enlazado |

```bash
# Reunir las URLs de los dos sitemaps y recrawlear
cd data && python reaudit.py urls.json crawl.json

# Verificar el enlazado interno antes de desplegar
python test_autolink_full.py
```

**Advertencia:** con más de 6 hilos el servidor devuelve 503 esporádicos. Toda incidencia debe reverificarse en serie antes de reportarla.

## Condiciones de trabajo

El sitio se despliega **solo por FTP y sin staging**, y en julio de 2026 hubo un incidente de corrupción de archivos en una transferencia. Todo cambio de plantilla se entrega como ZIP con manifiesto MD5, se extrae desde cPanel File Manager y se verifica con `md5sum -c`. No se suben `.php` sueltos.

No hay binario `php` en la máquina de trabajo: el lint se hace con `php-parser` (npm) antes de cada entrega. Un manifiesto MD5 comprueba la transferencia, no la sintaxis.

---

**Preparado por:** Juan Marcos · SEO Specialist
**Última actualización:** 29 de octubre de 2026
