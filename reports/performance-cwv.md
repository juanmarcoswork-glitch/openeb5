# Performance & Core Web Vitals — openeb5.com

**Date:** 2026-05-11
**Note:** Google PageSpeed Insights public API returned HTTP 429 (rate-limited without an API key) during this audit. Findings below are SYNTHETIC, derived from HTML inspection, header analysis, and known plugin/theme behavior. Re-run via Google PSI API with a key (set `PAGESPEED_API_KEY` and use `seo-google` skill) for field metrics.

---

## Synthetic CWV Estimate (Mobile, 4G/Slow 4G)

| Metric | Estimate | Status | Driver |
|---|---|---|---|
| LCP | **4.5–7.5 s** | ❌ Poor | Slider Revolution hero, 72 CSS files, no cache, no CDN |
| INP | **400–800 ms** | ❌ Poor | 148 script tags, multiple Elementor add-ons, GTM + Site Kit double tracking |
| CLS | **0.15–0.35** | ❌ Needs Improvement | Slider with reflow, late-loading social widgets, no explicit width/height on many images |
| FCP | **2.5–4.5 s** | ⚠️ Needs Improvement | Render-blocking CSS, no critical CSS inline |
| TTFB | **800–1500 ms** | ⚠️ Needs Improvement | No page cache (PHPSESSID set on every visit), no CDN |
| TBT | **600–1200 ms** | ❌ Poor | 17 render-blocking scripts in `<head>` |

**Performance score estimate: 25/100 mobile, 45/100 desktop.**

---

## Resource Inventory (from homepage HTML, 198 KB document)

| Asset class | Count | Notes |
|---|---|---|
| `<link rel="stylesheet">` total | **81** | Catastrophic for FCP; one of the worst counts I've seen on a marketing site |
| `<link rel="stylesheet">` in `<head>` | **72** | All render-blocking until parsed |
| `<script>` total | **148** | Includes inline and external; ~20+ are Elementor widget definitions |
| `<script src=>` in `<head>` | **17** | Render-blocking unless `async`/`defer` |
| `<link rel="preload">` | 3 | Some preload exists but probably not for LCP image |
| `<link rel="preconnect|dns-prefetch">` | 7 | Has some, but missing key origins |
| External domains loaded | **21** | See list below |

### External origins reached on homepage load
- fonts.googleapis.com, fonts.gstatic.com (Google Fonts)
- use.fontawesome.com (FontAwesome — heavy alternative to icon font subsetting)
- connect.facebook.net (Facebook Pixel)
- www.googletagmanager.com (GTM)
- www.monsterinsights.com (analytics — extra to GTM)
- yoast.com (Yoast metadata)
- ninjateam.org (WhatsApp plugin assets)
- s.w.org (WordPress emoji/CDN endpoint)
- api.w.org (WordPress API)
- api.whatsapp.com (WhatsApp click-to-chat)
- developers.google.com
- broaddususa.com (parent company)
- www.facebook.com, www.instagram.com, www.linkedin.com, www.youtube.com (social embeds)
- www.google.com.mx (Maps embed)
- schema.org, www.w3.org (markup references, not loaded)

> Each non-essential 3rd-party origin adds 100–400 ms TTFB risk + a TLS handshake. ~6 of these should be deferred to user interaction.

### WordPress plugin enqueue (23 plugins detected on the homepage)

| Plugin | Likely impact | Action |
|---|---|---|
| revslider (Slider Revolution) | Heavy — owns LCP element | Replace with native Elementor hero |
| elementor + elementor-pro | Large CSS/JS payload (~250 KB combined) | Keep but enable "Optimized Asset Loading" + "Improved CSS Loading" in Elementor → Settings → Features |
| woocommerce + yith-quick-view + yith-wishlist | Loads on every page despite no commerce | DEACTIVATE entirely |
| massive-cryptocurrency-widgets | Loads crypto API JS irrelevantly | DELETE |
| meks-simple-flickr-widget | Loads Flickr API JS | DELETE |
| instagram-feed | 3rd-party Instagram API | Lazy-load below the fold |
| mailchimp-for-wp | Form JS | Keep but defer |
| newsletter | Duplicate of mailchimp-for-wp | DEACTIVATE one |
| booked | Appointment booking | Audit usage; if unused, DEACTIVATE |
| google-analytics-for-wordpress (MonsterInsights) | Extra analytics layer | Consolidate via GTM only |
| google-site-kit | Pulls dashboard widgets | Limit dashboard role visibility; assess if double-firing gtag |
| whatsapp-for-wordpress (ninjateam) | JS loaded sitewide | Defer; load only on contact pages or by user interaction |
| case-theme-core + case-theme-user | Consultio theme support | Required by theme |
| elementskit + elementskit-lite | Elementor add-ons | Audit; remove if features unused |
| emage-hover-effects-for-elementor | Hover-effects add-on | DEACTIVATE; use CSS hover |
| country-phone-field-contact-form-7 | Phone field add-on | OK |
| contact-form-7 | Form plugin | Keep |
| openeb5-form-to-pdf | Custom form-to-PDF | Audit usage |

---

## Top 10 Performance Wins (Ranked by impact)

1. **Install a page cache + CDN.** Single highest-impact change. WP Rocket + Cloudflare. Expected gain: TTFB 1000 ms → 100 ms; LCP −1.5 s.
2. **Stop setting PHPSESSID on every page.** Audit cookie-starting plugins; restrict to cart/booking flows. Without this, no CDN page cache will hit.
3. **Remove WooCommerce, Slider Revolution, massive-cryptocurrency-widgets, meks-simple-flickr-widget, emage-hover-effects, yith-quick-view, yith-wishlist.** Expected gain: −40 enqueued assets, −600 ms TBT.
4. **Replace the homepage Slider Revolution with a single static hero image + LCP `preload`.** Expected gain: LCP −1.5 to −2.5 s.
5. **Enable Elementor "Optimized CSS Loading" + "Optimized Asset Loading"** in Settings → Features. Reduces enqueued asset count ~30–50%.
6. **Concatenate / minify CSS & JS** via WP Rocket or Autoptimize. Targeting <20 final CSS files and <30 JS files.
7. **Self-host Google Fonts** (or remove FontAwesome if a subset would do). One less origin handshake + GDPR cleaner.
8. **Lazy-load Instagram feed, WhatsApp widget, Facebook Pixel,** until user interaction or scroll past 50%. Use a consent-manager-driven loader.
9. **Convert images to WebP/AVIF.** Install ShortPixel or Imagify; serve via `<picture>` element. Logos (OpenEB5_logo.jpg) should also be SVG where possible.
10. **Add explicit `width` and `height` on every `<img>`** to prevent CLS. Most likely missing on Elementor-rendered images.

---

## CWV Per-Page Estimate

| URL | LCP est. (mobile) | INP est. | CLS est. | Priority |
|---|---|---|---|---|
| `/` | 5.5–7.5 s | 600 ms | 0.20 | P0 |
| `/the-complete-guide-to-eb-5-investment/` | 4.0–6.0 s | 400 ms | 0.10 | P0 |
| `/eb-5/` | 4.0–5.5 s | 400 ms | 0.10 | P0 |
| `/midtown-pharr/` | 4.0–6.0 s | 400 ms | 0.15 | P1 |
| Blog post (any) | 3.5–5.0 s | 300 ms | 0.10 | P1 |

---

## Server / Hosting Findings

- `Server: nginx` (version not exposed — good)
- `Set-Cookie: PHPSESSID=...; secure; HttpOnly` (HttpOnly is correct; missing `SameSite=Lax/Strict`)
- No `cf-cache-status`, `x-cache`, or other CDN-cache headers — site is **NOT** behind a CDN
- `Transfer-Encoding: chunked` (OK)
- `Cache-Control: no-store, no-cache, must-revalidate` on the homepage — disables every caching layer

**Recommended hosting/CDN stack:**
- **WP Engine, Kinsta, Cloudways, or RunCloud** for managed WordPress with server-level caching
- **Cloudflare (free tier minimum)** in front for CDN + DDoS + WAF
- **Cloudflare APO ($5/mo)** if staying on Cloudflare — provides full-page caching for WordPress including HTML

---

## Action Validation

After implementing fixes, re-test with:
- https://pagespeed.web.dev/report?url=https%3A%2F%2Fopeneb5.com%2F
- https://www.webpagetest.org/ — Mobile / Slow 4G / Pixel device
- Chrome DevTools Lighthouse (incognito)
- `seo-google` skill with PSI API key for CrUX field data over 28 days

**Target metrics post-fix:**
- LCP ≤ 2.5 s mobile
- INP ≤ 200 ms
- CLS ≤ 0.10
- Lighthouse Performance ≥ 75 mobile, ≥ 90 desktop

**Performance score (synthetic, current): 25/100** → **target: 80/100**
