---
layout: page
title: Plan de arquitectura y limpieza
permalink: /architecture-fix/
nav_order: 5
---

# Plan de arquitectura y limpieza

## 4.1 Estado actual de la arquitectura (problema)

**161 URLs HTML rastreadas** distribuidas en una estructura desorganizada:

- 110 URLs en el árbol "activo" (con función SEO clara)
- 51 URLs "basura" (theme demos, plugins demos, categorías vacías, orphan pages, 404s)

Ver organigrama visual completo en: [https://miro.com/app/board/uXjVHT7ICPE=/](https://miro.com/app/board/uXjVHT7ICPE=/) (zona Y=5800+)

---

## 4.2 Estructura propuesta (target)

```
openeb5.com/
├── /                              [Home EN]
├── /ES/                           [Home ES]
│
├── /eb-5-visa/                    [Hub principal EN — renombrar de /eb-5/]
│   ├── /eb-5-visa/process/        [TOFU]
│   ├── /eb-5-visa/requirements/   [MOFU]
│   ├── /eb-5-visa/timeline/       [MOFU]
│   ├── /eb-5-visa/source-of-funds/  [BOFU]
│   └── /eb-5-visa/i-526e-processing-time/  [TOFU — KW alta demanda]
│
├── /ES/visa-eb-5/                 [Hub principal ES]
│   ├── /ES/visa-eb-5/proceso/
│   ├── /ES/visa-eb-5/requisitos/
│   └── ...
│
├── /projects/                     [Hub proyectos]
│   ├── /projects/midtown-pharr/
│   ├── /projects/midtown-brownsville-ii/
│   ├── /projects/past/
│   └── /projects/collaborative/
│
├── /investors/                    [Hub inversores]
│   ├── /investors/by-country/mexico/
│   ├── /investors/by-country/china/
│   ├── /investors/by-country/vietnam/
│   └── ...
│
├── /blog/                         [Blog sin fechas en URL]
│   ├── /blog/{slug}/
│   └── ...
│
├── /about/
│   ├── /about/team/
│   └── /about/contact/
│
└── /resources/                    [Legal y misc]
    ├── /resources/news/
    ├── /resources/privacy/
    └── /resources/terms/
```

---

## 4.3 Mapping de redirects 301

> **Crítico:** sin un mapping de 301 perfecto se pierde toda la equity de backlinks (los pocos legítimos que hay).

| URL antigua | URL nueva | Razón |
|---|---|---|
| `/eb-5/` | `/eb-5-visa/` | Mejor matching de keyword |
| `/current-projects/` | `/projects/` | Hub más limpio |
| `/past-projects/` | `/projects/past/` | Anidamiento jerárquico |
| `/collaborative-projects/` | `/projects/collaborative/` | Anidamiento |
| `/midtown-pharr/` | `/projects/midtown-pharr/` | Bajo hub |
| `/midtown-brownsville/` | `/projects/midtown-brownsville-ii/` | Nombre real proyecto |
| `/mexico/` | `/investors/by-country/mexico/` | Anidamiento |
| `/2026/04/06/what-happens-after-...` | `/blog/green-card-stages-after-eb5/` | URLs sin fecha + slug corto |
| `/author/user_open/` | `/author/eduardo-prato/` | Canonical fix |
| `/collaborative-investments/` | `/projects/collaborative/` | Era 404 |
| `/home-onepage` | `/` | Era 404 |
| `/category/business/` | (410 Gone) | Categoría vacía |
| `/tag/builder/` | (410 Gone) | Tag basura |
| `/portfolio-category/*` | (410 Gone) | Theme inheritance basura |
| `/case-study-category/*` | (410 Gone) | Theme inheritance basura |
| `/service-category/*` | (410 Gone) | Theme inheritance basura |
| `/ct-mega-menu/*` | (410 Gone) | Plugin demo en prod |
| `/footer/*` | (410 Gone) | Theme demo |
| `/page-title/*` | (410 Gone) | Theme demo |

---

## 4.4 Implementación de redirects

### Opción A — Plugin "Redirection" para WordPress (recomendado)

```
1. Instalar plugin "Redirection" by John Godley
2. Importar CSV con todos los pares URL_antigua,URL_nueva,tipo (301)
3. Verificar con Screaming Frog que todos los 301 funcionan
4. Monitorear "Redirection Log" durante 30 días para capturar URLs no contempladas
```

### Opción B — Modificar `.htaccess` directamente (avanzado, requiere SSH)

```apache
RewriteEngine On

# Hub renames
RedirectMatch 301 ^/eb-5/?$ /eb-5-visa/
RedirectMatch 301 ^/current-projects/?$ /projects/
RedirectMatch 301 ^/past-projects/?$ /projects/past/
# ... (continuar con resto del mapping)

# 410 Gone para basura
RedirectMatch 410 ^/category/
RedirectMatch 410 ^/tag/
RedirectMatch 410 ^/portfolio-category/
RedirectMatch 410 ^/case-study-category/
RedirectMatch 410 ^/service-category/
RedirectMatch 410 ^/ct-mega-menu/
RedirectMatch 410 ^/footer/
RedirectMatch 410 ^/page-title/
```

---

## 4.5 Sitemap regenerado

Después de los redirects, regenerar `sitemap_index.xml` con:

- Yoast → Settings → Site features → XML sitemaps → ON
- Verificar que incluya las 51 URLs `/ES/` que faltaban
- Submitar la nueva URL del sitemap a GSC

---

## 4.6 Robots.txt actualizado

```
User-agent: *
Allow: /

# Bloquear basura legacy (después de 30 días post-redirect)
Disallow: /category/
Disallow: /tag/
Disallow: /portfolio-category/
Disallow: /case-study-category/
Disallow: /service-category/
Disallow: /ct-mega-menu/
Disallow: /footer/
Disallow: /page-title/
Disallow: /author/yarrdo/

# Sitemaps
Sitemap: https://openeb5.com/sitemap_index.xml
```

---

## 4.7 Cleanup de plugins

Eliminar estos 7 plugins del WordPress:

1. **WooCommerce** (sitio no es ecommerce, plugin pesa 60+ MB)
2. **WooCommerce Payments** (causa de las URLs con doble slash)
3. **ct-mega-menu** (deja `demo.casethemes.net` en producción)
4. **Booked** (causa doble slash, no se usa)
5. **Slider Revolution** (reemplazar con Smart Slider 3, más rápido)
6. **Crypto widget** (no relacionado al negocio)
7. **Cualquier plugin "demo importer"** (revisar lista)

**Antes de eliminar:** backup completo del sitio (UpdraftPlus o similar).

---

## 4.8 Estructura de internal linking propuesta

- **Home → Hubs:** 10 links principales (uno por hub)
- **Hub → Sub-páginas:** 4-7 links según hub
- **Sub-páginas → Hub padre:** breadcrumb obligatorio
- **Cross-hub links:** entre blog posts y hubs relevantes (regla: cada post linkea a 2-3 hubs)
- **Footer:** links a Legal, Sitemap, Contact (sin duplicar el menú principal)
