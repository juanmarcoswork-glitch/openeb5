---
layout: page
title: Plan técnico — Próximos 5 días
permalink: /technical-fixes-5days/
nav_order: 7
---

# Plan técnico — Próximos 5 días

## 6.1 Resumen

Tras los 5 días de auditoría exhaustiva (10-14 mayo 2026), se han identificado **8 errores técnicos críticos** que deben corregirse en los próximos 5 días de trabajo: **viernes 15 a martes 19 de mayo de 2026**.

Estos cambios desbloquean todas las acciones posteriores y deben ejecutarse en estricto orden de dependencias.

---

## 6.2 Día 1 — Viernes 15 de mayo 2026 (3 horas)

### Tarea 1.1 — Subir disavow file (15 min) — **P0 CRÍTICO**

**Quién:** Consultor con acceso GSC
**Qué hacer:**

1. Abrir [https://search.google.com/search-console/disavow-links](https://search.google.com/search-console/disavow-links)
2. Seleccionar propiedad `openeb5.com`
3. Subir `disavow-openeb5.txt` (94 dominios tóxicos)
4. Click "Subir"
5. Captura de pantalla para reporte

**Resultado esperado:** Google deja de considerar los 94 dominios para ranking. Efecto medible en 30-60 días.

### Tarea 1.2 — Fix title homepage (15 min) — **P0 CRÍTICO**

**Quién:** Cliente con WP-admin
**Qué hacer:**

1. WP Admin → Pages → Home → Edit
2. Bajar a "Yoast SEO" section
3. SEO title: `USCIS-Approved EB-5 Regional Center | Open EB5 — Texas`
4. Meta description: `Open EB5 is a USCIS-approved Regional Center in McAllen, Texas offering EB-5 investment opportunities in the Rio Grande Valley. I-956F approved projects. Learn how to obtain your green card through investment.`
5. Save & Update

**Resultado esperado:** Title aparece correctamente en SERPs en 24-72 hrs.

### Tarea 1.3 — Fix Yoast Site Representation (30 min)

**Quién:** Cliente con WP-admin
**Qué hacer:**

1. WP Admin → Yoast SEO → Settings → Site basics
2. **Website name:** `Open EB5` (con espacio, mayúsculas correctas)
3. **Tagline:** `USCIS-Approved EB-5 Regional Center in Texas`
4. **Site representation:** `Organization`
5. **Organization name:** `Open EB5 Regional Center`
6. **Logo:** subir versión cuadrada 512x512 mínimo (PNG con transparencia)
7. **Phone:** `+1-855-733-6325`
8. **Address:** `3900 N. 10th St Suite 1080, McAllen, TX 78501`
9. Save changes

**Resultado esperado:** Los 94 titles con patrón `X - openeb5` ahora muestran `X | Open EB5`.

### Tarea 1.4 — Backup completo del sitio (2 hrs)

**Quién:** Cliente o consultor (UpdraftPlus o BackupBuddy)
**Qué hacer:** Backup full antes de cualquier otro cambio. Guardar en Google Drive o Dropbox.

**Resultado esperado:** Punto de restauración disponible si algo falla.

---

## 6.3 Día 2 — Sábado 16 de mayo 2026 (2 horas)

### Tarea 2.1 — Instalar plugin Hreflang (1 h)

**Quién:** Cliente con WP-admin
**Qué hacer:**

1. WP Admin → Plugins → Add new → buscar `HREFLANG Tags Lite`
2. Instalar y activar (autor: HREFLANG.org)
3. Settings → HREFLANG → cargar `hreflang-mapping-openeb5.csv` (51 pares)
4. Verificar con View Source en una página /ES/ que aparezca:

   ```html
   <link rel="alternate" hreflang="en" href="https://openeb5.com/..." />
   <link rel="alternate" hreflang="es" href="https://openeb5.com/ES/..." />
   <link rel="alternate" hreflang="x-default" href="https://openeb5.com/..." />
   ```

**Resultado esperado:** Google indexa correctamente versiones EN/ES sin confundirlas con contenido duplicado.

### Tarea 2.2 — Submitar sitemap actualizado a GSC (1 h)

**Quién:** Consultor
**Qué hacer:**

1. GSC → Sitemaps → eliminar sitemap viejo si existe
2. Agregar nuevo: `https://openeb5.com/sitemap_index.xml`
3. Submit
4. Verificar manualmente que las 51 URLs `/ES/` aparezcan
5. Si no aparecen: WP Admin → Yoast → re-toggle XML sitemaps off/on para forzar regeneración

**Resultado esperado:** Sitemap completo enviado, GSC empieza a crawlear URLs ES faltantes.

---

## 6.4 Día 3 — Domingo 17 de mayo 2026 (2 horas)

### Tarea 3.1 — Configurar headers de seguridad en Cloudflare (1 h)

**Quién:** Consultor con acceso Cloudflare
**Qué hacer:**

1. Cloudflare Dashboard → openeb5.com → Rules → Transform Rules → Modify Response Header
2. Crear regla "Security Headers":
   - **HSTS:** `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`
   - **CSP:** `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://*.googletagmanager.com https://*.google-analytics.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:`
   - **X-Frame-Options:** `X-Frame-Options: SAMEORIGIN`
   - **X-Content-Type-Options:** `X-Content-Type-Options: nosniff`
   - **Referrer-Policy:** `Referrer-Policy: strict-origin-when-cross-origin`
   - **COOP:** `Cross-Origin-Opener-Policy: same-origin`
3. Deploy
4. Verificar con [https://securityheaders.com/?q=openeb5.com](https://securityheaders.com/?q=openeb5.com) (target: grade A+)

**Resultado esperado:** Sitio gana puntos en signals técnicos. Mejor seguridad para usuarios.

### Tarea 3.2 — Identificar y listar las 7 plugins a eliminar (1 h)

**Quién:** Consultor
**Qué hacer:**

1. WP Admin → Plugins → exportar lista (CSV manual o screenshot)
2. Identificar:
   - WooCommerce
   - WooCommerce Payments
   - ct-mega-menu
   - Booked
   - Slider Revolution
   - Cualquier "crypto widget"
   - Cualquier "demo importer"
3. NO ELIMINAR aún. Solo documentar dependencias.

**Resultado esperado:** Lista finalizada de plugins a remover en Día 8 (semana 2).

---

## 6.5 Día 4 — Lunes 18 de mayo 2026 (3 horas)

### Tarea 4.1 — Crear plan de redirects 301 (2 h)

**Quién:** Consultor
**Qué hacer:**

1. Construir CSV completo de redirects (ver Sección 4.3 de `architecture-fix.md`)
2. Validar cada URL antigua con curl que retorne 200 actualmente
3. Validar que cada URL nueva esté disponible
4. Preparar para implementación con plugin Redirection

**Resultado esperado:** `redirects-301.csv` listo para deploy en semana 2.

### Tarea 4.2 — Fix los 2 links internos rotos (1 h)

**Quién:** Cliente con WP-admin
**Qué hacer:**

1. Buscar en el contenido WordPress los links:
   - `/collaborative-investments/` (404)
   - `/home-onepage` (404)
2. Reemplazarlos con:
   - `/collaborative-projects/` (existe)
   - `/` (home)
3. Save & Update todas las páginas modificadas

**Resultado esperado:** 0 links internos rotos en el sitio.

---

## 6.6 Día 5 — Martes 19 de mayo 2026 (3 horas)

### Tarea 5.1 — Fix canonical roto (30 min)

**Quién:** Cliente con WP-admin
**Qué hacer:**

1. WP Admin → Users → buscar `user_open`
2. Verificar si tiene posts atribuidos
3. Si sí: reasignar todos los posts a `eduardo-prato`
4. Eliminar usuario `user_open`
5. Eliminar usuario `yarrdo` también
6. Verificar que `/author/user_open/` y `/author/yarrdo/` retornen 404 (luego se 410 en cleanup phase)

**Resultado esperado:** Canonical roto eliminado.

### Tarea 5.2 — Audit final post-fixes técnicos (2 h 30 min)

**Quién:** Consultor
**Qué hacer:**

1. Run Screaming Frog crawl completo
2. Comparar con baseline del 10-may-2026
3. Verificar:
   - 0 títulos con patrón `X - openeb5`
   - Hreflang presente en TODAS las páginas /ES/
   - 0 links internos rotos
   - Security headers grade A+ en securityheaders.com
   - Sitemap incluye las 51 URLs /ES/
4. Generar reporte HTML con before/after
5. Subir reporte a `/docs/reports/2026-05-19-post-fase-0.md`

**Resultado esperado:** Validación documentada de Fase 0 completada exitosamente.

---

## 6.7 Checklist visual de los 5 días

```
DÍA 1 (Vie 15-may) — 3 hrs
[ ] Disavow file subido a GSC
[ ] Title homepage corregido
[ ] Yoast Site Representation arreglado
[ ] Backup completo del sitio

DÍA 2 (Sáb 16-may) — 2 hrs
[ ] Plugin hreflang instalado y configurado
[ ] Sitemap actualizado submitido a GSC

DÍA 3 (Dom 17-may) — 2 hrs
[ ] Security headers en Cloudflare (grade A+)
[ ] Lista de 7 plugins a remover documentada

DÍA 4 (Lun 18-may) — 3 hrs
[ ] Plan de redirects 301 completo en CSV
[ ] 2 links internos rotos corregidos

DÍA 5 (Mar 19-may) — 3 hrs
[ ] Canonical /author/user_open/ arreglado
[ ] Audit post-Fase 0 documentado en /docs/reports/
```

**Total tiempo invertido en Fase 0:** ~13 horas distribuidas en 5 días.
