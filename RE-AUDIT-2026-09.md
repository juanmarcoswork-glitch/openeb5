# Re-auditoría SEO — openeb5.com + /ES

**Fecha:** 7 de septiembre de 2026
**Revisión:** v5 (la anterior es `AUDIT-2026-08-EN-ES.md`, del 7 de agosto)
**Método:** re-crawl de las 130 URLs declaradas en los dos `sitemap_index.xml`, más verificación serial del código de estado de los 51 destinos de enlace interno que no aparecen en ningún sitemap
**Panel en vivo:** https://juanmarcoswork-glitch.github.io/openeb5/seo-audit/

---

## Resumen

**Score de la propiedad: 58 → 68/100.**

El mes cerró cuatro de las doce tareas del plan de 30 días, dejó seis a medias y no tocó dos. Aparecieron además dos defectos nuevos, uno de ellos causado por un cambio de configuración de agosto.

| Métrica | 7 Ago | 7 Sep | |
|---|---:|---:|---|
| URLs con respuesta 200 en sitemap | — | 130 / 130 | ✅ |
| Páginas ES con `lang` correcto | 0% | 100% | ✅ |
| URLs en español en sitemap | 0 | 61 | ⚠️ existe, sin declarar |
| Enlaces internos rotos | 27 | 8 | ⚠️ |
| Bloque de AI crawlers en `robots.txt` | ausente | presente | ✅ |
| Entradas del blog ES sin meta description | 13 | 0 | ✅ |
| Hojas de estilo, home EN | 28 | 7 | ✅ |
| Hojas de estilo, home ES | 64 | 64 | ❌ |
| Bundles de plugin, home ES | 24 | 23 | ❌ |
| Caché en `/ES/` | `no-store` | `no-store` | ❌ |
| Páginas con hreflang invertido | 35 | 35 | ❌ |
| Páginas ES con dos H1 | 4 | 4 | ❌ |
| Imágenes sin `alt` | 0 | 0 | ✅ |

---

## 1. Lo que quedó cerrado

### 1.1 Señal de idioma

Las 61 páginas del sitemap español declaran `<html lang="es">`. El 7 de agosto eran 0 de 122. Es el arreglo con más peso del mes: el sitio que concentra las cinco posiciones orgánicas del dominio ya se le presenta a Google en su idioma.

### 1.2 Enlaces rotos

De 27 quedan 8. Cerrados:

- Los 21 enlaces en español que apuntaban a `/ES/` + slug inglés. `/ES/contact-us/`, que rompía la conversión desde 22 páginas, ahora redirige a `/ES/contactanos/`.
- `/terms/`, enlazado desde el footer de 90 páginas, redirige a `/terms-of-service/`.
- `/ES/ES/` redirige a `/ES/`.

Siguen rotos los 8 de las cuatro páginas de país que nunca existieron, en los dos idiomas.

### 1.3 Regresión de `robots.txt`

El bloque de agentes de IA volvió al archivo en vivo, con cinco agentes. Se había perdido en algún momento entre junio y agosto.

### 1.4 Metadatos

- Las 13 entradas del blog en español tienen meta description. Ninguna entrada ES queda sin ella.
- El sufijo de título del blog ES pasó de ` - Open EB5 | Green Card` a ` | Open EB5`. De 12 títulos por encima de 60 caracteres quedan 3.
- Los títulos de una sola palabra en `/ES/chile/`, `/ES/china/`, `/ES/india/` y `/ES/peru/` ya usan el patrón trabajado.
- Las dos meta descriptions fuera de rango en español (341 y 178 caracteres) están corregidas.

### 1.5 Consolidación del blog en inglés

`/blog/` y `/category/blog/` redirigen 301 a `/eb-5-blog/`. `/lp-contact-us/` redirige a `/contact-us/`.

### 1.6 Peso del sitio en inglés

La home bajó de 28 hojas de estilo a 7, y de 10 bundles de plugin a 6. NitroPack la sirve cacheada (`X-Nitro-Cache: HIT`).

---

## 2. Lo que sigue abierto

### 2.1 hreflang invertido — sin movimiento

35 páginas en español siguen emitiendo:

```
hreflang="en-US"     -> https://openeb5.com/ES/espana/      (es español)
hreflang="es"        -> https://openeb5.com/ES/ES/espana/   (no existe)
x-default            -> https://openeb5.com/ES/espana/
```

**Causa raíz identificada.** `inc/hreflang.php` construía las dos URLs a partir de `home_url()`. En la instalación inglesa eso vale `https://openeb5.com/`, así que funciona. Pero el sitio español es una instalación de WordPress separada cuyo `home_url()` ya es `https://openeb5.com/ES/`, y el mismo código antepone `/ES/` a una URL que ya lo tiene.

Además, **60 de las 130 páginas no emiten hreflang en absoluto**, incluidas todas las entradas del blog en los dos idiomas.

### 2.2 Rendimiento del sitio español — sin movimiento

| | Home EN | Home ES |
|---|---:|---:|
| Scripts | 18 | 29 |
| Hojas de estilo | 7 | 64 |
| Bundles de plugin | 6 | 23 |
| Caché | NitroPack `HIT` | `no-store, no-cache, must-revalidate` |

Los 17 bundles de diferencia son plugins activos en la instalación española que ya no existen en la inglesa: WooCommerce (sin tienda), YITH wishlist y quick-view, Slider Revolution (sin ningún slider en la página), Booked, Instagram Feed, un widget de criptomonedas, otro de Flickr, Newsletter, y los restos del tema Consultio.

El `no-store` viene de la sesión de WooCommerce. Impide guardar la página en el navegador, en NitroPack y en cualquier proxy: cada visita a la página que rankea en cuatro países regenera PHP entero.

### 2.3 Contenido corto en español — sin movimiento

`/ES/noticias/` 66 palabras · `/ES/comite-asesor/` 92 · `/ES/corea-del-sur/` 95 · `/ES/reino-unido/` 123 · `/ES/espana/` 133 · `/ES/brasil/` 135.

**Causa raíz identificada para las cuatro páginas de país.** Sus slugs están en español (`espana`, `brasil`, `corea-del-sur`, `reino-unido`) pero no figuraban como claves en `openeb5_countries_data()`, que sí usa los slugs ingleses. Por eso el filtro `template_include` nunca las enrutaba a `page-country.php` y seguían sirviendo contenido de Elementor: es la misma causa de los dos H1 del punto 2.4.

`/ES/noticias/` es un caso distinto: no es un artículo corto, es el contenedor del feed de la categoría *noticias*, y esa categoría está vacía.

### 2.4 H1 duplicados — sin movimiento

`/ES/brasil/`, `/ES/corea-del-sur/`, `/ES/espana/` y `/ES/reino-unido/` tienen dos H1, con el segundo en inglés o en portugués. Misma causa que 2.3.

### 2.5 `/es/` en minúsculas

`/ES/` responde 200, `/ES` redirige bien, `/es/` sigue devolviendo 404.

---

## 3. Defectos nuevos

### 3.1 Canonical hacia una URL que redirige — 21 entradas

En agosto la base de categoría de las entradas pasó de `blog` a `business`. El sitemap y las URLs servidas usan ya `/business/`, pero el canonical sigue apuntando a `/blog/`:

```
GET /business/strategic-investment-with-open-eb5/   -> 200
    <link rel="canonical" href=".../blog/strategic-investment-with-open-eb5/">
GET /blog/strategic-investment-with-open-eb5/       -> 301 a /business/...
```

Las 21 entradas del blog inglés se declaran canónicas de una URL que redirige de vuelta a ellas mismas. Google trata esa combinación como una señal contradictoria.

El mismo cambio dejó dos archivos equivalentes nuevos con respuesta 200: `/category/business/` y `/news/`.

### 3.2 El sitemap en español no está declarado en ninguna parte

`https://openeb5.com/ES/sitemap_index.xml` responde 200 y lista 61 URLs en cuatro sub-sitemaps. Es correcto y está al día.

Pero **nada lo menciona**: `robots.txt` solo declara el índice del sitio inglés, y ese índice no lo referencia. Como son instalaciones separadas, Yoast no puede saber de la otra. Google solo puede llegar a esas 61 URLs siguiendo enlaces internos.

Es el hallazgo con mejor relación entre esfuerzo y efecto de toda esta revisión: una línea en `robots.txt`.

El índice español arrastra además un `portfolio-category-sitemap.xml` con `lastmod` de diciembre de 2019, del tema Consultio.

### 3.3 Duplicado del consejo asesor en español

| URL | Palabras | H1 |
|---|---:|---|
| `/ES/advisory-board/` | 407 | Junta Asesora |
| `/ES/comite-asesor/` | 92 | Comité Asesor |

Las dos están en el sitemap y las dos se canonicalizan a sí mismas.

---

## 4. Estado de las 12 tareas del plan de 30 días

| Tarea | Estado | Detalle |
|---|---|---|
| **T1** · Sitemap ES + `lang` | A medias | `lang` cerrado. El sitemap existe pero no está declarado. |
| **O1** · Meta descriptions blog ES | **Cerrado** | 13 de 13. |
| **O2** · Plantilla de títulos blog ES | A medias &rarr; **en el paquete** | Sufijo corregido en vivo. Los 3 títulos largos y la redacción rota entran en el mapa curado. |
| **T2** · 27 enlaces rotos + 301 | A medias | Quedan 8: las 4 páginas de país en dos idiomas. |
| **O3** · Títulos y metas de países ES | A medias &rarr; **en el paquete** | Títulos hechos en vivo. Las 4 meta descriptions que faltaban entran en el mapa curado. |
| **O4** · H1 duplicados | Sin empezar | Causa raíz identificada en esta revisión. |
| **T3** · hreflang + `/ES/ES/` | A medias | `/ES/ES/` redirige. El hreflang sigue invertido. |
| **O5** · Ampliar 5 páginas ES cortas | **En el paquete** | Cubierto por `country-content.php` y `hub-content.php`. |
| **O6** · Meta descriptions fuera de rango | A medias &rarr; **en el paquete** | 2 de 3 corregidas en vivo. La tercera y las 2 páginas EN sin descripción entran en el mapa curado. |
| **T4** · Caché y dequeues en `/ES/` | Sin empezar | Sin ningún movimiento medible. |
| **O7** · Consolidar duplicados EN | A medias &rarr; **en el paquete** | `/blog/` resuelto en vivo. Los dos archivos nuevos los cierra `archive-policy.php`. |
| **O8** · `llms.txt` + robots + schema | A medias | Robots cerrado. `llms.txt` sin actualizar, sin `Organization` en la home ES. |

---

## 5. Qué resuelve el paquete v1.0.9.5

Entregado junto a esta revisión. Instrucciones en `INSTRUCCIONES-FTP-v1.0.9.5.md`.

| Módulo | Resuelve |
|---|---|
| `inc/hreflang.php` reescrito | T3. Raíces absolutas en vez de `home_url()`. Suma los 18 pares de entradas del blog. |
| `inc/robots-txt.php` nuevo | T1 y O8. `robots.txt` virtual con los dos sitemaps y 12 agentes de IA. |
| `inc/country-content.php` nuevo | O5. 400 a 700 palabras por país en 11 páginas EN y 14 ES, con FAQ y `FAQPage` JSON-LD. |
| `inc/country-pages-installer.php` nuevo | T2. Crea las 8 páginas de país que faltaban en la base de datos. |
| `inc/internal-links.php` nuevo | Aplica el plan de enlazado interno: 91 anclas en los dos idiomas. |
| `inc/asset-diet.php` nuevo (ES) | T4. Retira los assets de 8 plugins y levanta el `no-store`. |
| `inc/noticias-policy.php` nuevo (ES) | `/ES/noticias/`: `noindex` mientras el feed esté vacío, con la redirección al blog preparada. |
| `inc/url-redirects.php` | T2. 301 de `/es/*` y de `/blog/page/N/`. Canonical auto-referencial en las entradas (defecto 3.1). |
| `inc/sitemap-tuning.php` | O7. Las URLs que redirigen se declaran por su ruta canónica. Consolidación del duplicado 3.3. Fuera el CPT `portfolio` de 2019. |
| `inc/country-data.php` + `inc/compat.php` (ES) | O4 y O5. Los 4 slugs en español ya enrutan a la plantilla de país. |
| `inc/schema.php` (ES) | O8. Nodo `Organization` en la home española. |
| `inc/hub-content.php` nuevo | O5 y contenido corto EN. Lleva las 8 páginas de continente y hub de cada idioma de 68-297 palabras a 404-609, sin editar ninguna plantilla. |
| `inc/meta-overrides.php` nuevo | O1, O2, O3 y O6. Mapa curado de 20 títulos y 21 meta descriptions, versionado con el tema. Cubre las 15 páginas sin descripción, las 10 con título largo y la redacción rota del blog ES. |
| `inc/archive-policy.php` nuevo (EN) | O7 y defecto 3.1. `/category/business/` redirige 301 a `/eb-5-blog/` conservando la paginación; `/news/` se canonicaliza al blog mientras lo duplique. |
| `llms.txt` EN + ES | O8. Actualizado y con versión en español. Se corrigieron 3 URLs del borrador que devolvían 404 o 301. |

**Proyección: 68 → 84/100** una vez desplegado y verificado.

Con esto las 12 tareas del plan de 30 días quedan cerradas o resueltas en el paquete. Lo que sigue abierto no es trabajo de código.

---

## 6. Lo que no se puede resolver desde el código

Son las cuatro cosas que separan el 84 proyectado del 92 objetivo:

1. **Desactivar los 8 plugins sin uso del sitio ES.** El tema ya impide que envíen assets, pero siguen ejecutando PHP en cada request.
2. **Activar NitroPack en `/ES/`.**
3. **Borrar el `robots.txt` físico** de la raíz. Mientras exista, WordPress lo sirve tal cual y el módulo nuevo queda inerte.
4. **Cabeceras de seguridad** (HSTS, CSP, X-Frame-Options) y los 11 datos de schema pendientes del cliente.

Y por encima de todo eso sigue el problema de fondo que ya señalaba el SOW: **4 keywords orgánicas y 1 visita estimada al mes**. El sitio está cada vez más sano técnicamente, pero sin enlaces entrantes no hay competencia posible en EB-5. Eso es la Fase 3.

---

## 7. Reproducir esta revisión

```bash
# 1. Reunir las URLs de los dos sitemaps
python - <<'PY'
import urllib.request, re, json
UA={'User-Agent':'Mozilla/5.0'}
get=lambda u: urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=40).read().decode('utf-8','replace')
urls=set()
for base in ['https://openeb5.com/sitemap_index.xml','https://openeb5.com/ES/sitemap_index.xml']:
    for sm in re.findall(r'<loc>([^<]+)</loc>', get(base)):
        if 'portfolio' in sm: continue
        urls |= set(re.findall(r'<loc>([^<]+)</loc>', get(sm)))
json.dump(sorted(urls), open('urls.json','w'), indent=1)
PY

# 2. Crawl y analisis (scripts en data/)
python reaudit.py urls.json crawl.json
```

Los scripts `reaudit.py`, `check_anchors.py` y `test_autolink_full.py` están en `data/`. El último es el que verifica el enlazado interno contra el HTML en vivo antes de desplegar: comprueba que ningún ancla genere un `<a>` anidado y que el número de enlaces crezca exactamente en el número de anclas aplicadas.

**Advertencia:** con más de 6 hilos el servidor devuelve 503 esporádicos. Toda incidencia debe reverificarse en serie antes de reportarla.
