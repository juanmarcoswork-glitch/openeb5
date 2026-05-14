# Action Plan — openeb5.com SEO

**Audit date:** 2026-05-11
**Total prioritized actions:** 47
**Priority legend:** P0 = fix this week · P1 = fix this month · P2 = next quarter · P3 = backlog

---

## P0 — CRITICAL (Fix in week 1)

| # | Action | Owner | Effort | Where |
|---|---|---|---|---|
| 1 | Set Yoast Organization name to `Open EB5` (proper case) + add phone (+1-855-OPENEB5) + address (3900 N. 10th St, Suite 1080, McAllen, TX 78501) | Web dev | 30 min | Yoast → General → Site Representation |
| 2 | Rewrite homepage `<title>` and meta description | Marketing | 30 min | Yoast → Search Appearance → Homepage. Title: `USCIS-Approved EB-5 Regional Center \| Open EB5 — Texas`. Meta: see `reports/content-eeat.md` |
| 3 | Strip `Cache-Control: no-store` from homepage; install WP Rocket; put Cloudflare in front | Web dev / Host | 2 h | Hosting + plugin install |
| 4 | Identify which plugin sets `PHPSESSID` on every visit; restrict to cart/booking flows | Web dev | 2 h | Trace via incognito + plugin disable bisection |
| 5 | Add HTTP security headers (HSTS, XCTO, XFO, CSP, Referrer-Policy, Permissions-Policy) | Web dev / Sysadmin | 1 h | nginx config — snippets in `reports/technical-seo.md` |
| 6 | Strip `<meta name="generator">` from all pages (6 generator tags currently expose plugin versions) | Web dev | 30 min | functions.php / mu-plugin snippet in technical-seo.md |
| 7 | Replace the broken 1-item BreadcrumbList schema with valid breadcrumbs site-wide | Web dev | 1 h | Yoast → General → Breadcrumbs |
| 8 | Delete unused plugins: WooCommerce, YITH ×2 (quick-view, wishlist), `massive-cryptocurrency-widgets`, `meks-simple-flickr-widget`, `emage-hover-effects-for-elementor`, one of two newsletter plugins | Web dev | 2 h | Deactivate → test → delete |
| 9 | Add FinancialService / LocalBusiness JSON-LD on the homepage (replace shell Organization) | Web dev | 1 h | WPCode snippet; full block in `reports/schema-markup.md` |
| 10 | Publish `/llms.txt` per template in `reports/geo-ai-readiness.md` | Marketing | 30 min | Upload to `wp-content/uploads/` and add nginx alias OR use a plugin like "llms.txt" |
| 11 | Audit /about-us/ content — find and remove "Dunkin Donuts Harlingen TX" off-topic text (causing irrelevant SEMrush ranking) | Marketing | 30 min | Manual review |
| 12 | Set `noindex` on /confirmation/, /success/, /lp-contact-us/, /elementor-7790/ | Web dev | 30 min | Yoast on each page |

---

## P1 — HIGH (Fix in weeks 2-4)

| # | Action | Effort | Notes |
|---|---|---|---|
| 13 | Add hreflang tags across all EN/ES page pairs and country pages | 4 h | Configure WPML or Polylang; if neither is installed, install Polylang free + Yoast Polylang glue |
| 14 | Add Spanish blog posts to the post-sitemap | 2 h | Yoast WPML/Polylang configuration |
| 15 | Replace Slider Revolution on the homepage with a static hero image + LCP `preload` | 3 h | Designer + dev |
| 16 | Rewrite homepage hero copy: value prop ("USCIS-approved EB-5 Regional Center — invest $800,000 in Texas TEA projects for U.S. permanent residency"), 3 trust strip metrics (years operating / projects approved / capital deployed) | 4 h | Copywriter + Elementor |
| 17 | Write meta descriptions (130-155 chars) for the 15 most important pages | 3 h | Yoast UI |
| 18 | Rewrite the pillar: `/the-complete-guide-to-eb-5-investment/` — 3× word count, define TEA, add EB-5 Reform Act 2022 section, add USCIS.gov citations, add comparison tables (Regional Center vs Direct, $800K vs $1.05M, processing times by country), add FAQ block | 16 h | Senior writer + immigration counsel review |
| 19 | Add FAQPage schema to /eb-5/ and pillar guide | 1 h | WPCode; blocks ready in schema report |
| 20 | Add HowTo schema to pillar guide | 1 h | Block ready |
| 21 | Add Article schema to all 19 blog posts (replace generic WebPage) | 2 h | Yoast → Search Appearance → Posts → set schema piece type to "Article" |
| 22 | Add named author + photo + Person schema for each named author | 4 h | Bios + photos + WP user profile setup |
| 23 | Write bios for the 8 administrative team members; add named immigration attorney + securities counsel to /the-team/ | 8 h | Content + photos |
| 24 | Add visible "Last updated" date + author byline to every blog post and key page | 2 h | Theme template edit |
| 25 | Convert all images to WebP via ShortPixel or Imagify; serve via `<picture>` | 4 h | Bulk-process existing media library |
| 26 | Audit and fix `<img alt="">` on the 11 affected homepage images and across the site | 4 h | Manual content review |
| 27 | Set OG image to a proper 1200×630 social card (currently the 308×45 logo) | 1 h | Designer + Yoast |
| 28 | Add Service schema to /eb-5/ and InvestmentOrDeposit schema to /midtown-pharr/, /midtown-brownsville/, /brownsville-parkside/ | 2 h | WPCode |
| 29 | Migrate blog permalink from `/YYYY/MM/DD/slug/` to `/blog/slug/` with 301 redirects | 4 h | Permalinks change + Redirection plugin; backup first |
| 30 | Submit site to Google Business Profile (McAllen office) | 1 h | Google account |
| 31 | Submit Crunchbase profile | 2 h | Marketing |
| 32 | Verify and claim USCIS Regional Center directory listing (if designated) | 1 h | Compliance |
| 33 | Join / verify IIUSA member directory listing | 1 h | Membership |
| 34 | Enable IndexNow in Yoast → Site Connections | 5 min | One toggle |

---

## P2 — MEDIUM (Fix in weeks 5-12)

| # | Action | Effort | Notes |
|---|---|---|---|
| 35 | Rewrite top 5 country pages (China, India, Vietnam, Brazil, Mexico) with country-specific source-of-funds, retrogression, attorney/consulate context (1,200+ words each, original research where possible) | 30 h | Senior writer + research |
| 36 | Noindex (or rewrite) the remaining 13 country pages until they meet quality bar | 2 h | Yoast |
| 37 | Publish 12 new keyword-gap blog posts (EB-5 vs E-2 visa, Reform Act explained, Reserved Visa categories, source of funds, I-526E denial reasons, I-829 walkthrough, children aging-out, U.S. tax post-green card, processing times by country, etc.) | 48 h | Editorial calendar |
| 38 | Press release on each I-956F approval; submit to PRNewswire + targeted EB-5 trade publications | 6 h per release | Comms |
| 39 | Pitch 4 guest articles to eb5investors.com and EB5Insights | 16 h | Editorial relationships |
| 40 | Launch original-research piece: "State of EB-5 from LatAm investors 2026" — survey, infographic, distribution | 40 h | Big project |
| 41 | Audit and consolidate analytics: GTM only (remove duplicate gtag from Site Kit and MonsterInsights) | 2 h | Web dev |
| 42 | Configure object cache (Redis) on host | 2 h | DevOps |
| 43 | Disable `/wp-json/wp/v2/users` user-enumeration endpoint | 30 min | Security plugin or custom filter |
| 44 | Disable XML-RPC | 15 min | Security plugin |
| 45 | Add `<link rel="preconnect">` to fonts.gstatic.com, www.googletagmanager.com | 30 min | Theme functions.php |
| 46 | Submit `/.well-known/security.txt` with security contact + PGP key (if available) | 30 min | Static file |
| 47 | Migrate Google Fonts to self-hosted | 2 h | Caos plugin or manual |

---

## P3 — LOW / BACKLOG

- Implement schema for Event when webinars are scheduled
- Add VideoObject schema for embedded YouTube videos
- Implement breadcrumb visible UI on every page (currently hidden / not displayed)
- Add a structured data testing routine to the CI pipeline (validator.schema.org)
- Generate an XML image sitemap via Yoast
- Add PWA manifest + service worker (low priority for advisory firm)
- Audit cookie SameSite attributes
- Audit form-to-PDF custom plugin for security
- Refresh /privacy-policy/ and /terms-of-service/ for current US/TX disclosures
- Consider building a public "ROI calculator" / "EB-5 cost estimator" interactive (info-gain for SEO + AI citations)

---

## Acceptance Criteria & Validation

| Action # | Validation command |
|---|---|
| 1, 9 | `curl -s https://openeb5.com/ \| grep -oE '"@type":"[^"]+"' \| sort -u` should show `FinancialService` and `Open EB5` name (not lowercase) |
| 2 | `curl -s https://openeb5.com/ \| grep -i '<title>' \| head -1` should not return `OpenEB5 - openeb5` |
| 3, 4 | `curl -I https://openeb5.com/` should show `cf-cache-status: HIT` and no `Set-Cookie: PHPSESSID` on first visit |
| 5 | `curl -I https://openeb5.com/` should show `strict-transport-security`, `x-content-type-options`, `x-frame-options` |
| 6 | `curl -s https://openeb5.com/ \| grep -i 'meta name="generator"' \| wc -l` should return 0 |
| 7 | Schema validator on https://search.google.com/test/rich-results should show valid Breadcrumb |
| 8 | `curl -s https://openeb5.com/ \| grep -oE '/wp-content/plugins/[a-z0-9-]+' \| sort -u \| wc -l` should drop from 23 → ≤ 15 |
| 10 | `curl -I https://openeb5.com/llms.txt` should return 200 |
| 13 | `curl -s https://openeb5.com/eb-5/ \| grep -i 'hreflang' \| wc -l` should be ≥ 2 |
| 14 | `curl -s https://openeb5.com/post-sitemap.xml \| grep -c '/ES/'` should be > 0 |
| 19, 20, 21 | All money pages return valid Schema in https://validator.schema.org/ |
| 24 | Every blog post should show a visible "Last updated" line near the H1 |
| 25 | `curl -sI https://openeb5.com/wp-content/uploads/...` for a converted image should show `Content-Type: image/webp` |
| 27 | Sharing the homepage on LinkedIn should preview a 1200×630 card, not the 308×45 logo |
| 33 | Open EB5 listed on https://iiusa.org/members/ |
| 34 | Bing Webmaster Tools shows IndexNow submissions |

---

## What I delivered in this audit

- 6 specialist reports under `reports/`
- 1 executive summary (`FULL-AUDIT-REPORT.md`)
- 1 prioritized action plan (this file)
- Raw HTML and header snapshots under `data/`
- Complete ready-to-paste JSON-LD blocks for 6 page types in `reports/schema-markup.md`
- Complete `/llms.txt` template in `reports/geo-ai-readiness.md`
- Competitor benchmark table for 5 EB-5 industry sites
- Keyword gap list (15 high-priority targets)
- 90-day strategic roadmap

## What's next

When you attach openeb5.com to Ahrefs, share access (or paste the Site Explorer + Site Audit summaries) and I will:
1. Cross-validate the SEMrush findings against Ahrefs DR/RD
2. Run Ahrefs Content Gap with the 5 competitor seeds
3. Refine the keyword target list with Ahrefs's broader EB-5 keyword index
4. Validate or relax the "do not disavow" recommendation based on Ahrefs toxicity scoring
5. Build an Ahrefs-tracked keyword set (15-25 keywords) and a referring-domains alert for new authentic links
