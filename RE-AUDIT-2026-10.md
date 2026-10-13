# Re-auditoría SEO: openeb5.com + /ES

**Fecha:** 13 de octubre de 2026
**Revisión:** v6 (la anterior es `RE-AUDIT-2026-09.md`, del 7 de septiembre)
**Método:** re-crawl de las 138 URLs declaradas en los dos `sitemap_index.xml`, verificación serial del código de estado de los 27 destinos de enlace interno que no aparecen en ningún sitemap, comparación de la huella de los assets del tema en vivo contra el paquete v1.0.9.5, y métricas orgánicas y de enlaces al 12 de octubre
**Panel en vivo:** https://juanmarcoswork-glitch.github.io/openeb5/seo-audit/

---

## Resumen

**Score de la propiedad: 68 → 70/100.**

El mes trajo el primer movimiento orgánico real del proyecto y cerró cinco tareas. Pero el paquete v1.0.9.5 no se subió, y en el servidor hay una versión v1.1.x del tema que no coincide con él. Entraron además cuatro defectos nuevos al conteo, por eso cinco cierres valen solo dos puntos.

| Métrica | 7 Sep | 13 Oct | |
|---|---:|---:|---|
| Keywords orgánicas | 4 | 10 | ✅ |
| Visitas orgánicas estimadas/mes | 1 | 19 | ✅ |
| URLs en los dos sitemaps (todas 200) | 130 | 138 | ✅ |
| Páginas de país en 404 | 8 | 0 | ✅ |
| Páginas ES con dos H1 | 4 | 0 | ✅ |
| Cabeceras de seguridad | pendientes | 5 de 6 | ✅ |
| Destinos de enlace interno en 404 | 8 | 1 (desde 20 páginas) | ⚠️ nuevo |
| Páginas con hreflang invertido | 35 | 39 | ❌ |
| Canonicals hacia una URL que redirige | 21 | 26 | ❌ |
| Sitemap ES declarado | no | no | ❌ |
| Caché en `/ES/` | `no-store` | `no-store` | ❌ |
| Bundles de plugin, home ES | 23 | 23 | ❌ |
| `/ES/llms.txt` | 404 | 404 | ❌ |
| Dominios de referencia (no spam) | | 590 (22) | ⚠️ |

---

## 1. Lo que quedó cerrado

### 1.1 Páginas de país

Las 8 páginas que daban 404 existen: `/canada/`, `/france/`, `/turkey/`, `/venezuela/` y `/ES/canada/`, `/ES/francia/`, `/ES/turquia/`, `/ES/venezuela/`. Tienen entre 982 y 1.336 palabras, FAQ y meta description, y están en los sitemaps. `/ES/france/` y `/ES/turkey/` redirigen 301 a los slugs en español.

### 1.2 Slugs de país en español

`/ES/espana/`, `/ES/brasil/`, `/ES/corea-del-sur/` y `/ES/reino-unido/` ya usan la plantilla de país: un solo H1 en español y entre 1.097 y 1.241 palabras. Antes tenían dos H1 (uno en inglés o portugués) y entre 95 y 135 palabras. Ninguna página de los sitemaps tiene ya dos H1.

Las 20 páginas de país en español tienen título con keyword y meta description de 142 a 154 caracteres (tarea O3 cerrada).

### 1.3 Cabeceras de seguridad

Los dos sitios envían `Strict-Transport-Security` (un año, con subdominios), `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy` y `Permissions-Policy`. Falta `Content-Security-Policy`.

### 1.4 Visibilidad orgánica

| Keyword | País | Pos. | Vol. | URL |
|---|---|---:|---:|---|
| what is resident card | EE. UU. | 2 | 20 | blog EN, qué es la Green Card |
| green card eb5 | EE. UU. | 4 | 50 | blog EN, qué es la Green Card |
| green card usa que es | España | 5 | 30 | blog ES, qué es la Green Card |
| eb-5 visa cost | EE. UU. | 6 | 150 | blog EN, guía de requisitos y costes |
| eb5 | España | 6 | 30 | `/ES/` |
| eb5 china | EE. UU. | 8 | 20 | `/china/` |
| green card que es | Rep. Dominicana | 8 | 10 | blog ES, qué es la Green Card |
| eb5 india | EE. UU. | 9 | 90 | `/india/` |
| eb5 criteria | EE. UU. | 9 | 80 | blog EN, guía de requisitos y costes |
| eb5 | Perú | 9 | 70 | blog ES, requisitos 2025 |

Tráfico estimado mensual: 1 (mayo), 4, 14, 5, 7, 16 (octubre). Por primera vez rankean el blog inglés y páginas de país en inglés.

**Todas las URLs del blog inglés que rankean están indexadas bajo `/blog/`**, no bajo `/business/`. Ver 2.1.

---

## 2. Lo que sigue abierto

### 2.1 Canonical del blog EN: ahora con tráfico en juego

Sin cambios en el mecanismo: las entradas se sirven en `/business/`, declaran canonical a `/blog/`, y `/blog/` redirige 301 a `/business/`. Ya son 26 entradas.

Lo que cambió es que Google eligió `/blog/` como URL indexada, y esas son las URLs que rankean. **Cambio de criterio respecto al paquete:** v1.0.9.5 forzaba el canonical a `/business/`. Con las posiciones ya ganadas bajo `/blog/`, lo correcto es devolver la base de categoría a `blog` (Ajustes → Enlaces permanentes) y redirigir `/business/*` a `/blog/*`. Así la URL servida, la canónica y la indexada vuelven a ser la misma, sin mover nada de lo que ya posiciona.

### 2.2 hreflang invertido: empeora

39 páginas en español se declaran `en-US` y apuntan a `/ES/ES/...` como versión española. Eran 35: las 4 páginas de país nuevas heredaron el error. 60 páginas siguen sin hreflang.

### 2.3 Sitemap ES sin declarar

`/ES/sitemap_index.xml` responde 200 con 65 URLs, pero `robots.txt` sigue declarando solo el índice inglés. El `robots.txt` en vivo es idéntico al de septiembre (5 agentes de IA + bloque de Yoast). Sigue también el `portfolio-category-sitemap.xml` de 2019.

### 2.4 Rendimiento de `/ES/`

| | Home EN | Home ES |
|---|---:|---:|
| Scripts | 18 | 29 |
| Hojas de estilo | 7 | 65 |
| Bundles de plugin | 6 | 23 |
| Caché | NitroPack `HIT` | `no-store, no-cache, must-revalidate` |

### 2.5 Otros

- `/es/` en minúsculas: 404.
- `/category/business/` y `/news/`: 200, duplican el archivo del blog.
- 15 títulos por encima de 60 caracteres (12 EN, 3 ES; el peor, 121).
- 8 páginas ES sin meta description (eran 33 en agosto).
- Páginas de continente en 175 a 206 palabras.
- Home ES sin nodo `Organization`.
- `/ES/llms.txt`: 404.

---

## 3. Defectos nuevos

### 3.1 Política de privacidad en 404 desde el formulario de país ES (crítico)

El aviso bajo el botón "Solicitar evaluación gratuita" de las **20 páginas de país en español** enlaza a `/ES/politica-de-privacidad/`, que da 404. La política real está en `/ES/privacy-policy/`. Es el punto de conversión de un sitio YMYL que pide datos financieros.

Arreglo: corregir la URL en la plantilla del formulario de país del tema ES y añadir un 301 de respaldo. El enlace no viene del paquete v1.0.9.5: llegó con la versión v1.1.x.

### 3.2 El tema en vivo diverge del paquete (alto, proceso)

`components.css` en vivo no coincide con el del paquete: contiene bloques marcados `v1.1.1` (enlaces en prosa) y `v1.1.2` (enlaces en contenido de Elementor) que el paquete no tiene, y le faltan bloques de módulos de país que el paquete sí trae. `llms.txt` en vivo tampoco es el del paquete.

Parte del paquete está en vivo (páginas de país, alias de slug ES) y parte no (hreflang, robots virtual, mapa de metas, archive policy, asset diet, noticias policy, schema ES, llms ES). **Subir v1.0.9.5 tal cual pisaría v1.1.x.** Hace falta la copia del tema en el servidor (EN y ES) para rehacer el paquete encima.

### 3.3 Ola de enlaces spam (medio)

Los dominios de referencia pasaron de 184 (1 de agosto) a 590. 568 están clasificados como spam: granjas `.shop`, `.top`, `.site`, un dominio de casinos. Los enlaces editoriales reales son 4: theorg.com, rgvbusinessjournal.com, rgvmonthly.com y eb5visainvestments.com (nuevo, 6 de octubre, el primero temático de la industria EB-5).

Google ignora este tipo de enlaces de forma automática. Recomendación: desautorizar a nivel de dominio solo el de casinos y los de anclas tipo "comprar backlinks", y seguir el perfil mes a mes.

### 3.4 Brownsville Parkside sin contenido (medio)

`/brownsville-parkside/` (72 palabras) y `/ES/brownsville-parkside/` (68), en los dos sitemaps, sin meta description y con títulos genéricos. La ES no emite hreflang. Hace falta del cliente la información pública del proyecto; cualquier estado USCIS se confirma antes de publicarlo.

Además: `/ES/lp-guia/` está indexable con 125 palabras y sin descripción. Si es landing de campañas, `noindex`.

---

## 4. Estado de las 12 tareas del plan de 30 días

| Tarea | Sep | Oct |
|---|---|---|
| **T1** · Sitemap ES + `lang` | A medias | A medias. `lang` cerrado, sitemap sin declarar |
| **O1** · Meta descriptions blog ES | Cerrado | Cerrado |
| **O2** · Títulos blog ES | En el paquete | En el paquete. 3 títulos ES largos |
| **T2** · Enlaces rotos + 301 | A medias | A medias. Países cerrados, entra privacidad ES |
| **O3** · Títulos y metas de países ES | En el paquete | **Cerrado en vivo** |
| **O4** · H1 duplicados | En el paquete | **Cerrado en vivo** |
| **T3** · hreflang + `/ES/ES/` | En el paquete | En el paquete. 39 páginas |
| **O5** · Ampliar páginas ES cortas | En el paquete | A medias. Países cerrados, faltan hubs |
| **O6** · Meta descriptions fuera de rango | En el paquete | En el paquete |
| **T4** · Caché y dequeues en `/ES/` | En el paquete | En el paquete. Sin movimiento |
| **O7** · Consolidar duplicados EN | En el paquete | En el paquete. Cambia el criterio del canonical (2.1) |
| **O8** · `llms.txt` + robots + schema | En el paquete | En el paquete |

---

## 5. Siguientes pasos

1. Corregir el enlace de privacidad del formulario de país ES (15 minutos, independiente de todo lo demás).
2. Conseguir la copia del tema en vivo, EN y ES.
3. Rehacer el paquete sobre esa copia: hreflang, robots virtual con los dos sitemaps, mapa de metas, archive policy, asset diet ES, noticias policy, schema ES, `llms.txt` ES. Cambiar el criterio del canonical del blog a `/blog/`.
4. Del cliente: datos de Brownsville Parkside, decisión sobre `/ES/lp-guia/`, desactivar los plugins sin uso de ES, NitroPack en `/ES/`.
5. Disavow puntual del dominio de casinos y de las granjas con anclas de compra de enlaces.

**Proyección:** 70 → 84 con el paquete reconciliado, desplegado y verificado.

---

## 6. Reproducir esta revisión

Mismo procedimiento que `RE-AUDIT-2026-09.md` §7 (`data/reaudit.py`). Para la divergencia del tema:

```bash
curl -s https://openeb5.com/wp-content/themes/openeb5/assets/css/components.css | md5sum
# paquete v1.0.9.5: 6608a091bb6fd6162aaa95e6f1e48e4a · en vivo 13 Oct: 4e1ed806abdc536783baaa08f0db139b
```
