# Brand & media logos — Open EB5 trust carousel

Esta carpeta contiene los logos que aparecen en el carrusel de autoridad del home (sección `.logo-marquee` justo debajo del hero).

Los logos representan **marcas con las que han trabajado los miembros del team de Open EB5** y **medios donde el team ha sido mencionado** — son señales de autoridad y credibilidad para los visitantes.

## 📋 Estado actual

Cada archivo `.svg` en esta carpeta es un **placeholder gris con el wordmark** de cada marca. Esto asegura que el carrusel se vea bien aunque los logos oficiales no estén subidos todavía.

Cuando subas el logo oficial con el **mismo nombre de archivo**, automáticamente reemplaza el placeholder. No hay que tocar HTML ni CSS.

## 📁 Archivos esperados (15 totales)

### Medios (de bio de Emilio Guzmán)

| Archivo | Marca |
|---|---|
| `bloomberg.svg` | Bloomberg |
| `cnn.svg` | CNN |
| `forbes.svg` | Forbes |
| `reforma.svg` | Reforma |
| `adn40.svg` | ADN40 |

### Brands (de bio de Ricardo Rubiano)

| Archivo | Marca |
|---|---|
| `dunkin.svg` | Dunkin' |
| `olive-garden.svg` | Olive Garden |
| `sleep-number.svg` | Sleep Number |
| `sprint.svg` | Sprint |
| `verizon.svg` | Verizon |
| `longhorn.svg` | LongHorn Steakhouse |
| `take-5.svg` | Take 5 Oil Change |
| `anytime-fitness.svg` | Anytime Fitness |
| `mcalisters.svg` | McAlister's Deli |
| `black-bear-diner.svg` | Black Bear Diner |

## 🎨 Specs de los archivos

| Atributo | Valor recomendado |
|---|---|
| Formato | **SVG** preferido (escala perfecta, peso mínimo). PNG transparente acepta como fallback. |
| viewBox | `0 0 240 80` (ratio ~3:1, queda holgado para wordmarks) |
| Altura visual | Logo ocupa ~70% del alto disponible (margin interno ~10%) |
| Color | **Color oficial** del logo (full color). El CSS aplica `filter: grayscale(1)` para uniformar y `grayscale(0)` en hover. |
| Fondo | **Transparente** siempre |
| Peso | < 10 KB por archivo (los placeholders pesan ~400 bytes) |
| PNG | Si SVG no es posible: PNG transparente, mínimo 480×160px (2x para retina), max 50 KB |

## 🔄 Cómo reemplazar un logo

1. Obtener el logo oficial (SVG preferido) del press kit / web oficial de la marca
2. Renombrarlo al filename exacto de la tabla de arriba (kebab-case)
3. Reemplazar el archivo placeholder en esta carpeta
4. Commit + push → GitHub Pages reconstruye en ~1 min
5. Para producción WP: copiar a `/wp-content/uploads/brands/` (mismo naming)

## ⚖️ Nota legal

Los logos son propiedad de sus respectivos titulares. Su uso en este carrusel se justifica como **referencia a relaciones comerciales o menciones editoriales reales** del team de Open EB5. Antes de publicar en producción:

- Confirmar que cada relación es **verificable** (hay un trabajo real, una mención editorial real)
- Considerar agregar un disclaimer pequeño debajo del carrusel del tipo: *"Logos representing past professional engagements and editorial mentions of Open EB5 team members. All trademarks are property of their respective owners."*
- Si una marca solicita remover su logo, hacerlo inmediatamente (borrar el archivo + el `<img>` correspondiente en `index.html`)

## 🔧 Markup en el HTML

Los logos se referencian desde [`index.html`](../../index.html) en la sección `<section class="logo-marquee">`:

```html
<img class="logo-mark" src="assets/brands/bloomberg.svg" alt="Bloomberg" loading="lazy" />
```

El CSS está en [`../css/components.css`](../css/components.css) bajo el bloque `LOGO MARQUEE`.
