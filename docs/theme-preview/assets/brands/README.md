# Brand & media logos — Open EB5 trust carousel

Esta carpeta contiene los logos que aparecen en el carrusel de autoridad del home (sección `.logo-marquee` justo debajo del hero).

Los logos representan **marcas con las que han trabajado los miembros del team de Open EB5** y **medios donde el team ha sido mencionado** — son señales de autoridad y credibilidad para los visitantes.

## ✅ Estado actual (2026-06-25)

**Logos oficiales del cliente subidos.** Los placeholders SVG monochrome fueron reemplazados por los archivos originales que el cliente entregó. El carrusel ya muestra los logos reales.

## 📁 Archivos actuales (15 totales)

### Medios (de bio de Emilio Guzmán)

| Archivo | Marca | Formato origen |
|---|---|---|
| `bloomberg.jpg` | Bloomberg | JPG color |
| `cnn.svg` | CNN | SVG vector (rojo oficial) |
| `forbes.jpeg` | Forbes | JPEG |
| `reforma.png` | Reforma | PNG |
| `adn40.png` | ADN40 | PNG |

### Brands (de bio de Ricardo Rubiano)

| Archivo | Marca | Formato origen |
|---|---|---|
| `dunkin.png` | Dunkin' | PNG |
| `olive-garden.png` | Olive Garden | PNG |
| `sleep-number.png` | Sleep Number | PNG |
| `sprint.svg` | Sprint | SVG vector |
| `verizon.png` | Verizon | PNG |
| `longhorn.png` | LongHorn Steakhouse | PNG |
| `take-5.png` | Take 5 Oil Change | PNG |
| `anytime-fitness.png` | Anytime Fitness | PNG |
| `mcalisters.png` | McAlister's Deli | PNG |
| `black-bear-diner.png` | Black Bear Diner | PNG |

### Cómo se ven en el carrusel

El CSS aplica `filter: grayscale(1) opacity: 0.55 + mix-blend-mode: multiply` por default → logos en B/N tenues sobre fondo blanco. En **hover** quita el filter → vuelven a su color original con `opacity: 1`. Efecto premium "muted strip → live brand".

Para logos con **fondo blanco/JPG** (Bloomberg, Forbes, etc.), el `mix-blend-mode: multiply` funde el blanco con el fondo del marquee → sin bordes visibles.

### Si querés reemplazar un logo

1. Reemplazar el archivo en esta carpeta manteniendo el filename
2. Si cambiás de extensión (ej PNG → SVG), actualizar también [`../../index.html`](../../index.html) en la sección `<section class="logo-marquee">` para apuntar al nuevo path

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
