# Technical SEO Audit — openeb5.com

**Date:** 2026-05-11
**Target:** https://openeb5.com/
**Stack detected:** WordPress 6.9.4 · Yoast SEO · Elementor 3.34.4 Pro · Slider Revolution 6.7.20 · WooCommerce 10.4.3 · Consultio theme · nginx · 23 plugins identified
**Crawl scope:** 67 indexable URLs in sitemap_index.xml + sampled headers across 8 pages

---

## Severity Summary

| Severity | Count | Categories |
|---|---|---|
| Critical | 8 | Caching broken, no hreflang, exposed generators, vulnerable plugin versions, /ES/ blog not in sitemap, page-level Cache-Control: no-store, PHPSESSID cookie on every visit, missing security headers |
| High | 11 | Title/meta absent, schema gaps, orphan pages in sitemap, image alt missing, redundant plugins, no CDN, no WP cache plugin, hosting-level performance, broken breadcrumb, weak Organization data, duplicate `/contact-us-2/` |
| Medium | 9 | URL pattern legacy /YYYY/MM/DD/, empty taxonomies, WooCommerce installed but unused, deprecated sitemap leftovers, no XML image sitemap, no preload for LCP image, multiple favicons missing, no IndexNow ping, missing `<noscript>` fallback |
| Low | 6 | Cookie not SameSite=Strict, RSS feeds exposed, oEmbed/wp-json fingerprinting, missing security.txt, missing humans.txt, missing PWA manifest |

---

## 1. CRITICAL ISSUES

### 1.1 Page caching is effectively disabled
Homepage and most authenticated/dynamic pages return:
```
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Set-Cookie: PHPSESSID=...; path=/; secure; HttpOnly
```
**Impact:** Every visitor — including Googlebot — gets an uncached server-rendered response. CDN page caching is broken because PHPSESSID is set on every visit, so any CDN keyed on cookies will bypass the cache entirely. This destroys TTFB, drives up server cost, and degrades Core Web Vitals (LCP/TBT).
**Fix:**
1. Audit which plugin starts PHPSESSID (likely WooCommerce, Booked, or one of the Elementor add-ons). Disable session-starting on non-cart pages.
2. Install **WP Rocket** or **LiteSpeed Cache** or **W3 Total Cache**, configure full-page cache, exclude only WooCommerce cart/checkout/account.
3. Add Cloudflare in front (or any CDN). Configure "Cache Everything" page rule for `/wp-content/uploads/`, theme assets, and pages.
4. Strip `no-store, no-cache, must-revalidate` from the default response. Replace with `Cache-Control: public, max-age=3600, s-maxage=86400` for cacheable HTML.

### 1.2 Hreflang is missing across all EN/ES page pairs
Site has English (`/`) and Spanish (`/ES/`) versions, plus 18 country pages. `<link rel="alternate" hreflang="...">` is absent on every page tested. `<html lang="en-US">` is set on EN but no x-default and no hreflang annotation.
**Impact:** Google can't reliably swap the correct language version in SERPs. Spanish search results from LatAm investors may serve the English page; Brazilian/Portuguese searches see nothing relevant. Risk of self-cannibalization between `/eb-5/` and `/ES/eb-5/`.
**Fix:** Configure Yoast's WPML or Polylang integration. Minimum required pairs per page:
```html
<link rel="alternate" hreflang="en-us" href="https://openeb5.com/eb-5/" />
<link rel="alternate" hreflang="es"    href="https://openeb5.com/ES/eb-5/" />
<link rel="alternate" hreflang="x-default" href="https://openeb5.com/eb-5/" />
```

### 1.3 Spanish blog posts are NOT in the sitemap
SEMrush shows ranked URLs at `/ES/2025/05/23/que-es-la-visa-eb-5-y-como-funciona-guia-completa-paso-a-paso/` and `/ES/2025/08/04/3-senales-claras-de-que-estas-listo-para-aplicar-a-la-visa-eb-5/` and `/ES/2025/07/03/que-es-la-green-card-y-que-beneficios-ofrece-en-estados-unidos/`. None of these appear in https://openeb5.com/post-sitemap.xml (which only lists EN posts).
**Impact:** Google may be relying on internal links alone to discover ES content; many ES posts may go undiscovered or be slow to refresh. The handful that rank are likely the lucky ones with cross-language links.
**Fix:** Configure Yoast to include all post types and translations. If running WPML, ensure "Translations included in sitemap" is enabled. If pages are under a directory-based locale, configure a `post-sitemap-es.xml` and add it to `sitemap_index.xml`.

### 1.4 No HTTP security headers
Response headers from `/` show NONE of the following:
- `Strict-Transport-Security` (HSTS)
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options` or CSP `frame-ancestors`
- `Content-Security-Policy`
- `Referrer-Policy`
- `Permissions-Policy`

**Impact:** Loss of HSTS preload eligibility, clickjacking risk, MIME confusion attacks, no defense-in-depth for XSS. For a YMYL financial advisory site, this fails baseline trust expectations and is a Best Practices ding in Lighthouse.
**Fix (nginx):**
```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;
add_header Content-Security-Policy "default-src 'self' https:; img-src 'self' data: https:; style-src 'self' 'unsafe-inline' https:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https:; frame-src https:; connect-src 'self' https:;" always;
```
Once stable, submit to https://hstspreload.org/.

### 1.5 WordPress + plugin versions are exposed
The homepage emits 6 generator meta tags revealing exact versions:
```
<meta name="generator" content="WordPress 6.9.4" />
<meta name="generator" content="WooCommerce 10.4.3" />
<meta name="generator" content="Redux 4.5.10" />
<meta name="generator" content="Site Kit by Google 1.159.0" />
<meta name="generator" content="Elementor 3.34.4; ..." />
<meta name="generator" content="Powered by Slider Revolution 6.7.20 ..." />
```
**Impact:** Attackers can target known CVEs immediately. **Slider Revolution has a long CVE history**; running a publicly fingerprinted instance is a measurable security risk. This is also a tiny SEO Best Practices penalty in Lighthouse.
**Fix:** In `functions.php` or via a small mu-plugin:
```php
remove_action('wp_head', 'wp_generator');
add_filter('the_generator', '__return_empty_string');
// Per-plugin (paste in mu-plugin):
add_action('wp_head', function() { ob_start(function($b) { return preg_replace('/<meta name="generator"[^>]+>\\s*/i', '', $b); }); }, 0);
add_action('wp_footer', function() { ob_end_flush(); }, PHP_INT_MAX);
```

### 1.6 Plugin bloat & off-topic plugins active
23 active plugins detected on a single page load, including:
- **massive-cryptocurrency-widgets** — totally irrelevant for an EB-5 advisory site; off-topic content + abandoned plugins are common attack vectors.
- **meks-simple-flickr-widget** — Flickr widget; likely unused, abandoned-ish.
- **yith-woocommerce-quick-view** + **yith-woocommerce-wishlist** + **woocommerce** — full e-commerce stack on a site with no products; pure overhead.
- **mailchimp-for-wp** + **newsletter** — two newsletter plugins doing the same job.
- **booked** — appointment booking; may not be in use.
- **instagram-feed** — heavy 3rd-party JS for a small embed.
- **revslider** (Slider Revolution) — heavyweight slider, known CVE history.
- **emage-hover-effects-for-elementor** — Elementor add-on.

**Impact:** Each plugin enqueues CSS/JS. Cumulative effect: 72 stylesheets and 148 `<script>` tags on the homepage (see Performance report).
**Fix:** Deactivate then DELETE all unused plugins. Specifically remove: massive-cryptocurrency-widgets, meks-simple-flickr-widget, yith-woocommerce-quick-view, yith-woocommerce-wishlist, woocommerce (unless e-commerce is planned). Consolidate newsletter functionality on one plugin.

### 1.7 Vulnerable / dated plugins
Slider Revolution 6.7.20 — current branch is 6.7.x, but Slider Revolution has had RCE and arbitrary-file-upload CVEs across versions; running it on a marketing page is unnecessary risk. Replace with **Elementor's native slider** or a static hero image.
Elementor 3.34.4 — current stable as of audit date; OK if kept updated.
**Fix:** Replace Slider Revolution; enable auto-updates for core, themes, and plugins; subscribe to Patchstack or Wordfence alerts.

### 1.8 Multiple orphan / debug pages in production sitemap
The `page-sitemap.xml` includes:
- `/elementor-7790/` — Elementor working draft
- `/contact-us-2/` — duplicate contact page (cannibalizes `/contact-us/`)
- `/welcome-to-open-eb5/` — likely a dev landing page
- `/confirmation/` — form thank-you (should be noindex)
- `/success/` — form thank-you (should be noindex)
- `/lp-contact-us/` — alternate contact landing
- `/lp-guide/` — guide landing (intentional, but lp/lps should be flagged)

**Impact:** Bloats crawl budget, may rank instead of canonical pages, leaks marketing/funnel pages to Google.
**Fix:**
1. Delete `/elementor-7790/`.
2. Set `noindex` on `/confirmation/`, `/success/`, `/lp-contact-us/` via Yoast post-edit screen.
3. Pick one canonical contact page; redirect the duplicate via 301.
4. Exclude landing pages (`/lp-*`) from the sitemap or noindex them depending on intent.

---

## 2. HIGH-PRIORITY ISSUES

### 2.1 Homepage title is brand-only and lowercase
```html
<title>OpenEB5 - openeb5</title>
```
**Impact:** No keywords (`EB-5 visa`, `green card investment`, `regional center`, `Texas EB-5`), no value proposition, no CTR hook. Yoast's organization name was also stored as lowercase `openeb5`, which propagates into the JSON-LD Organization entity, OG title, and most page titles. This is one of the most damaging single fixes available.
**Fix:** In Yoast → Search Appearance → Homepage:
```
Title: USCIS-Approved EB-5 Regional Center | OpenEB5 — Texas
Meta Description: Invest from $800K in USCIS-approved Texas projects to obtain U.S. permanent residency through the EB-5 program. Bilingual EN/ES advisory team in McAllen. Schedule a consultation today.
```
Update the Organization name to `Open EB5` (proper capitalization) in Yoast → General → Site Representation. This corrects schema and OG output globally.

### 2.2 Homepage meta description is missing
Source has no `<meta name="description">`; Yoast emits an OG description that is raw page text truncated with `[…]`. Google may either auto-generate from page content or use a snippet that fails to convert.
**Fix:** Add a Yoast-managed meta description (110-155 chars) on the homepage and every money page.

### 2.3 Canonical for `/ES/` not verified
Need to verify that `/ES/` pages do not canonicalize to the EN equivalent (a common WPML misconfiguration). Sampling required during implementation.
**Fix:** After running tests on a sample of ES pages, confirm each has a self-referential canonical, not the EN canonical.

### 2.4 Empty sitemap shards left in the index
`portfolio-category-sitemap.xml` (lastmod 2019), `service-category-sitemap.xml`, `case-study-category-sitemap.xml` are referenced but empty. `page-title-sitemap.xml` and `ct-mega-menu-sitemap.xml` are deprecated.
**Impact:** Wastes crawl budget hitting empty XML files, weakens sitemap quality signal.
**Fix:** Disable the Consultio theme's custom sitemap providers or filter them out via Yoast:
```php
add_filter('wpseo_sitemap_index', function($index) {
  return preg_replace('#<sitemap>.*?(portfolio-category|service-category|case-study-category|page-title|ct-mega-menu)-sitemap.xml.*?</sitemap>#s', '', $index);
});
```

### 2.5 Breadcrumb schema invalid
Yoast outputs:
```json
"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home"}]
```
Google requires a minimum of 2 ListItems for a Breadcrumb rich result. A 1-item breadcrumb is essentially noise and will be ignored.
**Fix:** Configure Yoast Breadcrumbs (Yoast → General → Breadcrumbs → Enable). Output proper paths on deep pages: `Home > EB-5 > The Complete Guide`. On the homepage itself, breadcrumb should be suppressed entirely rather than emitting a 1-item list.

### 2.6 Organization schema is weak
```json
{
  "@type":"Organization","name":"openeb5","description":"",
  "url":"https://openeb5.com/",
  "logo":{"width":674,"height":150},
  // missing: telephone, address, contactPoint, sameAs, founder, foundingDate, areaServed
}
```
Logo dimensions in schema (674×150) don't match the `og:image` of `OpenEB5-green-stars.png` (308×45). Brand name is lowercase.
**Fix:** See `schema-markup.md` for the full corrected JSON-LD with `LocalBusiness`/`FinancialService` typing, full address, phone, languages, social profiles via `sameAs`.

### 2.7 Image alt text is missing or empty
11 of 16 `<img>` tags on the homepage have `alt=""`. The decorative-image convention (`alt=""`) is acceptable for purely ornamental icons but is being applied to logos and content imagery. No descriptive alt text means image SEO and accessibility are both broken.
**Fix:** Audit every content image and write a descriptive alt. Reserve `alt=""` for actual decorative ornaments only.

### 2.8 No XML image sitemap
Yoast does not emit `<image:image>` tags in the post sitemap by default for this Yoast config.
**Fix:** Yoast → Search Appearance → enable image sitemap, or add `image_sitemap_enabled` filter via WPCode. For 19 blog posts × ~3 images = ~57 images to surface for Google Image search.

### 2.9 Legacy URL pattern for blog posts
Blog posts use `/YYYY/MM/DD/slug/` (the WordPress legacy "Day and Name" permalink structure). This pattern is:
- Longer URLs (lower CTR)
- Dates visible to Google, signaling article age (bad if you don't update)
- Harder to rewrite/repurpose without 301s
- Misaligned with current SEO best practice (flat `/slug/` or `/category/slug/`)

**Fix:** Migrate permalink structure to `/blog/%postname%/` or `/eb-5-blog/%postname%/`. Run a full 301 redirect map old→new on cutover (every legacy URL must redirect or risk losing the ~20 rankings). Test with one post first.

### 2.10 No WordPress object cache or page cache plugin detected
Headers reveal no `X-Cache`, `X-LiteSpeed-Cache`, `cf-cache-status`, or similar CDN/cache indicators.
**Fix:** Same as 1.1. Recommended stack:
- **WP Rocket** (paid) or **LiteSpeed Cache** (free if on LiteSpeed host) or **W3 Total Cache**
- **Cloudflare** in front (free tier acceptable)
- Object cache: **Redis Object Cache** plugin if host supports it

### 2.11 Duplicate /contact-us/ and /contact-us-2/
Both URLs exist in the sitemap.
**Fix:** Pick the canonical. Set 301 from the duplicate.

---

## 3. MEDIUM-PRIORITY

### 3.1 WooCommerce active but unused
Adds session cookies, AJAX endpoints, and ~15 enqueued assets site-wide. Either deactivate or use the "Disable WooCommerce on non-WC pages" pattern (custom snippet that dequeues WC scripts outside `/shop/`, `/cart/`, `/checkout/`, `/my-account/`).

### 3.2 No preload for LCP image
Slider Revolution likely owns the LCP element. No `<link rel="preload" as="image">` for it.
**Fix:** Identify LCP image via Lighthouse, then add a manual `wp_head` preload hint.

### 3.3 `/wp-json/` REST API is publicly exposed
Anyone can query user enumeration endpoints (`/wp-json/wp/v2/users`). For a security-sensitive site, restrict.
**Fix:** Use a plugin like "Disable WP REST API" or filter `rest_authentication_errors` to require auth on user endpoints.

### 3.4 No `<link rel="preconnect">` for fonts.gstatic.com
Google Fonts is loaded; missing preconnect costs ~200ms on cold connections.
**Fix:** Yoast or theme can add the preconnect; or self-host Google Fonts (recommended for GDPR + performance).

### 3.5 Two analytics pipelines
Both Google Tag Manager and Google Site Kit (which can add its own gtag) detected. Likely double-firing.
**Fix:** Audit tags in GTM Preview Mode; remove duplicate gtag from Site Kit or remove redundant tracking from GTM.

### 3.6 Multiple Elementor add-on plugins
`elementskit`, `elementskit-lite`, `emage-hover-effects-for-elementor`, `case-theme-core`, `case-theme-user` — at least 5 Elementor extensions, each enqueueing CSS/JS.
**Fix:** Audit what features are actually used. Consolidate or remove.

### 3.7 No IndexNow submission detected
Bing/Yandex prefer IndexNow for instant indexing. Yoast supports this in newer versions.
**Fix:** Yoast → Site Connections → enable IndexNow (or install "IndexNow for WordPress" by Bing).

### 3.8 RSS feeds exposed
`/feed/`, `/comments/feed/` discoverable via `<link rel="alternate" type="application/rss+xml">`. Not a security issue but creates duplicate-content risk if scraped.
**Fix:** Optional — disable comments feed (`/comments/feed/`) since there are likely no public comments.

### 3.9 oEmbed and wp-json discovery leaks
`<link rel="alternate" type="application/json" href=".../wp-json/wp/v2/pages/5745" />` reveals WordPress post IDs.
**Fix:** Remove via:
```php
remove_action('wp_head', 'rest_output_link_wp_head');
remove_action('wp_head', 'wp_oembed_add_discovery_links');
remove_action('template_redirect', 'rest_output_link_header', 11);
```

---

## 4. LOW-PRIORITY

- Missing `security.txt` at `/.well-known/security.txt` — recommended for any site collecting investor data.
- Missing `humans.txt` — minor nice-to-have for transparency.
- No PWA manifest — not critical for advisory site.
- Cookie SameSite not set to Strict — review PHPSESSID and analytics cookies.
- No favicon at multiple sizes (192px, 512px) — verify `/wp-content/themes/consultio/` favicon set.

---

## 5. Verification commands

```bash
# Verify headers improvements
curl -I https://openeb5.com/

# Verify hreflang after fix
curl -s https://openeb5.com/eb-5/ | grep -i 'hreflang'

# Verify generator suppression
curl -s https://openeb5.com/ | grep -i '<meta name="generator"'

# Verify breadcrumb fix
curl -s https://openeb5.com/eb-5/ | grep -oE '"@type":"BreadcrumbList".*?\]' | head -1

# Verify sitemap cleanup
curl -s https://openeb5.com/sitemap_index.xml | grep -E '(portfolio|case-study|service|page-title|ct-mega)-sitemap'
```

---

**Technical SEO score: 30/100** — Critical issues across caching, hreflang, security headers, and sitemap hygiene. A YMYL site with this baseline is leaking trust at every level.
