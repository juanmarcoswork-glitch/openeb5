# SEO Audit Report — openeb5.com

**Audit date:** May 11, 2026
**Site:** https://openeb5.com/
**Business:** Open EB5 — USCIS-approved EB-5 Regional Center & investment advisory, McAllen, Texas
**Industry category:** YMYL (Your Money or Your Life) — Immigration + Investment
**Stack:** WordPress 6.9.4 + Yoast SEO + Elementor 3.34.4 Pro + Slider Revolution + WooCommerce + 23 active plugins
**Audit tools used:** WebFetch, curl, SEMrush MCP, sitemap parsing, schema validation, synthetic CWV analysis

---

## Executive Summary

### SEO Health Score: **29/100 — Critical**

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 30 | 6.6 |
| Content Quality & E-E-A-T | 23% | 35 | 8.05 |
| On-Page SEO | 20% | 25 | 5.0 |
| Schema / Structured Data | 10% | 25 | 2.5 |
| Performance (CWV) | 10% | 25 | 2.5 |
| AI Search Readiness | 10% | 28 | 2.8 |
| Images | 5% | 30 | 1.5 |
| **TOTAL** | **100%** | | **~29/100** |

**Verdict:** OpenEB5 has a healthy business shape (clear service offering, named projects, multilingual support, physical office, parent-company backing) but is **structurally invisible to search engines and AI engines.** With Authority Score 2/100, 20 organic keywords, 0 estimated organic traffic, and a homepage `<title>` of "OpenEB5 - openeb5", the site is currently behaving like a private brochure rather than a digital asset.

### Top 5 Critical issues

1. **Homepage title and meta description are missing or branded-only** — "OpenEB5 - openeb5" (17 chars, lowercase brand, no keywords). Single largest CTR leak.
2. **Page caching is effectively disabled** — `Cache-Control: no-store, no-cache, must-revalidate` + PHPSESSID cookie set on every visit. No CDN. TTFB + LCP destroyed sitewide.
3. **No hreflang** despite EN/ES versions and 18 country pages. Search engines cannot reliably serve the right language. Spanish blog posts are not even in the sitemap.
4. **YMYL E-E-A-T baseline missing** — No USCIS Regional Center number visible, no named immigration attorney, no SEC Reg D / risk disclosures, no government source citations on the pillar guide.
5. **Schema is broken or absent for every meaningful entity** — Organization name is lowercase, no LocalBusiness, no FAQPage, no Article on blog posts, BreadcrumbList has 1 item (invalid).

### Top 5 Quick Wins (high impact, ≤ 4 hours each)

1. **Fix Yoast Organization settings** — Set Organization name to `Open EB5` (proper case) and add phone, address. Cascades to schema, OG, titles globally. (1 h)
2. **Write homepage title + meta** — `USCIS-Approved EB-5 Regional Center | Open EB5 — Texas` + 155-char meta description. (30 min)
3. **Install WP Rocket + Cloudflare** — Single biggest performance win. (2 h)
4. **Delete unused plugins** — WooCommerce, YITH ×2, massive-cryptocurrency-widgets, meks-simple-flickr-widget, emage-hover-effects, one of two newsletter plugins. (2 h)
5. **Publish `/llms.txt`** — Template provided in `reports/geo-ai-readiness.md`. (30 min)

### Competitive position (US market, EB-5 niche)

| Domain | Authority Score | Organic Keywords | Est. Traffic |
|---|---|---|---|
| **openeb5.com** | **2** | **20** | **0** |
| eb5investors.com | 35 | 9,174 | 6,333 |
| iiusa.org | 34 | 2,121 | 5,486 |
| eb5affiliatenetwork.com | — | 2,862 | 1,288 |
| civitascapital.com | — | 609 | 2,755 |
| eb5capital.com | — | 462 | 1,085 |

**Gap:** 458× fewer keywords and 3,166× lower-traffic than category leader. No organic competitive overlap with any real EB-5 competitor — the keywords openeb5.com ranks for are accidental real-estate or random terms (`midtown brownsville`, `dunkin donuts harlingen tx`).

---

## 1. Site Inventory

| Asset | Count | Notes |
|---|---|---|
| Blog posts (EN, sitemap) | 19 | URL pattern `/YYYY/MM/DD/slug/` (legacy) |
| Pages (sitemap) | 48 | Includes 18 country pages + 4 regional pages |
| Country pages | 18 | argentina, australia, brazil, chile, china, colombia, india, iran, israel, lebanon, mexico, pakistan, peru, south-korea, spain, taiwan, united-kingdom, vietnam |
| Regional pages | 4 | america, asia, europe, oceania |
| Project pages | 3 | midtown-pharr, midtown-brownsville, brownsville-parkside |
| ES blog posts | Unknown — NOT in sitemap | At least 3 ES posts are ranked in SEMrush but absent from `/post-sitemap.xml` |
| Categories | 2 | business, strategy |
| Empty taxonomies referenced | 3 | portfolio-category, service-category, case-study-category (all last-modified 2019) |
| Active WordPress plugins (detected) | 23 | See performance report |
| Tracking | Google Tag Manager + Site Kit + MonsterInsights + Facebook Pixel | Likely double-firing |

---

## 2. Critical Findings by Category

### 2.1 Technical SEO — score 30/100
See `reports/technical-seo.md`. Headlines:
- `Cache-Control: no-store` + `Expires: 1981` on the homepage breaks every cache layer
- No HSTS, X-Content-Type-Options, X-Frame-Options, Content-Security-Policy, Referrer-Policy, Permissions-Policy
- 6 `<meta name="generator">` tags publicly expose exact versions of WP, WC, Elementor, Slider Revolution, Site Kit, Redux — measurable CVE-targeting risk
- No hreflang anywhere — EN/ES self-cannibalization risk
- Spanish blog content is not in the sitemap
- Empty sitemap shards (portfolio/service/case-study) still indexed
- `/elementor-7790/`, `/contact-us-2/`, `/welcome-to-open-eb5/`, `/confirmation/`, `/success/` are publicly indexable in the sitemap

### 2.2 Content Quality & E-E-A-T — score 35/100
See `reports/content-eeat.md`. Headlines:
- Pillar guide `/the-complete-guide-to-eb-5-investment/` is ~1,300 words (should be 3,500-5,000 for competitive YMYL)
- TEA used 4× but **never defined**
- **EB-5 Reform and Integrity Act of 2022 is never mentioned** — the entire statutory basis since 2022
- Zero USCIS.gov outbound citations on pillar guide
- No author byline on blog posts
- No "Last updated" date visible to users
- /the-team/ has only 2 named bios out of 10 staff; no named immigration attorney, no securities counsel
- 18 country pages risk being flagged as programmatic thin content
- /about-us/ accidentally ranks for "dunkin donuts harlingen tx" — investigate off-topic content

### 2.3 On-Page SEO — score 25/100

| Issue | Page(s) | Impact |
|---|---|---|
| Title is brand-only and lowercase | Homepage | Critical CTR loss |
| Meta description missing | Homepage + most money pages | 15-30% CTR opportunity lost |
| H1 not server-rendered | Homepage (Slider Revolution) | Possible AI crawl issue |
| 11/16 images have `alt=""` on the homepage | Sitewide | Image SEO + accessibility |
| OG image is 308×45 logo | Homepage | Bad social preview |
| OG image mismatched with schema logo (308×45 vs 674×150) | Homepage | Inconsistent entity |
| Open Graph description = raw page text with `[…]` | Homepage | Embarrassing social preview |
| `<html lang="en-US">` but ES content gets no `lang="es"` confirmation | ES pages | Locale signaling |
| Generators expose versions | All pages | Security + Lighthouse |
| Anchor text in internal links not optimized | All pages | Internal link equity wasted |
| Yoast Organization name is `openeb5` (lowercase) | Sitewide | Schema + title pollution |

### 2.4 Schema / Structured Data — score 25/100
See `reports/schema-markup.md`. Headlines:
- Organization schema is shell-only — no telephone, address, sameAs, founder, contactPoint, areaServed
- BreadcrumbList has 1 item — invalid for rich result
- No LocalBusiness/FinancialService schema (site has a physical office)
- No FAQPage schema anywhere
- No Article schema on blog posts (Yoast emits generic WebPage)
- No Person schema for team members
- No Service / InvestmentOrDeposit schema on /eb-5/ or project pages
- Ready-to-paste JSON-LD blocks provided in the schema report

### 2.5 Performance — score 25/100
See `reports/performance-cwv.md`. Estimated mobile metrics:
- LCP 4.5-7.5 s (target ≤ 2.5)
- INP 400-800 ms (target ≤ 200)
- CLS 0.15-0.35 (target ≤ 0.10)
- 72 stylesheets, 148 scripts on the homepage
- 23 plugins active, several abandoned/irrelevant (massive-cryptocurrency-widgets, meks-simple-flickr-widget, etc.)
- No WP cache plugin, no CDN
- PHPSESSID cookie blocks all CDN page caching

### 2.6 AI Search Readiness — score 28/100
See `reports/geo-ai-readiness.md`. Headlines:
- All AI crawlers allowed (good baseline)
- No `/llms.txt` (recommend creating; template provided)
- No FAQPage / HowTo / Article schema for AI extraction
- No named entities or government citations in pillar content
- No "citation capsules" — atomic factual passages AI can quote
- Entity signals very weak (no Wikidata, sparse sameAs)
- ChatGPT-User may not see content that depends on JS rendering

### 2.7 Images — score 30/100
- 11/16 homepage images use `alt=""` (decorative attribute applied indiscriminately)
- No `<picture>` element / WebP / AVIF detected — all PNG/JPG
- No image sitemap from Yoast (image SEO untapped)
- No `loading="lazy"` audit performed (likely missing on critical images)
- No `width` and `height` attributes on Elementor-rendered images → CLS contributor
- OG image is the wrong asset (308×45 logo instead of a proper 1200×630 social preview)

### 2.8 Backlinks & Authority — score 10/100
See `reports/backlinks-competitive.md`. Headlines:
- Authority Score 2/100, Trust Score 2/100
- 154 total backlinks from 93 referring domains — but ~0-5 are authentic editorial links
- Top referring domains are scrape farms (factmags.com, websiterace.com, domainsc.com, etc.) hosted on Singapore IPs
- Brand-anchor "open eb5" appears only once across the entire link graph
- Zero competitive overlap with real EB-5 niche sites
- No press releases for the I-956F approval (a release-worthy event)

---

## 3. Strategic Roadmap (90-day plan)

### Phase 1 — Foundation fixes (Weeks 1-2)
- Fix Yoast Organization name, phone, address (cascades sitewide)
- Rewrite homepage title, meta, hero copy
- Write meta descriptions for top 15 pages
- Strip `<meta name="generator">` tags
- Add HTTP security headers via nginx
- Add the FinancialService / LocalBusiness JSON-LD block
- Publish `/llms.txt`
- Delete abandoned plugins
- Install WP Rocket + Cloudflare

### Phase 2 — Content + schema (Weeks 3-6)
- Rewrite pillar guide `/the-complete-guide-to-eb-5-investment/` (3× word count, add USCIS citations, define TEA, add Reform Act 2022 section, add comparison tables, add FAQ block)
- Add FAQPage schema to /eb-5/ and pillar guide
- Add Article + Person (author) schema to all blog posts
- Write Person bios for all 8 administrative team members
- Add named immigration attorney + securities counsel to team page
- Replace Slider Revolution with static hero + preload
- Migrate blog URL pattern from `/YYYY/MM/DD/` to `/blog/slug/` with 301 redirects
- Audit and rewrite top 5 country pages (China, India, Vietnam, Brazil, Mexico)
- Submit Spanish blog posts to sitemap

### Phase 3 — Authority + AI visibility (Weeks 7-12)
- Build Crunchbase, USCIS RC directory, IIUSA member listing
- Run a PR push for the I-956F approval — press release + outreach to EB5Investors, IIUSA, Texas business outlets
- Launch original-research report ("State of EB-5 from LatAm investors 2026")
- Submit 4 guest posts to eb5investors.com / EB5Insights
- Publish 12 new blog posts targeting keyword-gap topics (EB-5 vs E-2, Reform Act explained, Reserved Visa categories, source of funds, etc.)
- Submit to IndexNow (Bing/Yandex) via Yoast
- Track monthly: AS, organic keywords, AI Overview citations, branded mentions

### Phase 4 — Continuous (after Day 90)
- Quarterly content refresh on the pillar and top 10 posts
- Monthly link-building campaign (2 earned mentions/month minimum)
- Quarterly E-E-A-T review (new team additions, certifications, project milestones)
- Quarterly schema audit
- Track Core Web Vitals continuously via CrUX

---

## 4. Expected Outcomes (with consistent execution)

| Metric | Day 0 | Day 90 target | Day 180 target | Day 365 target |
|---|---|---|---|---|
| Authority Score | 2 | 8 | 15 | 22 |
| Organic Keywords (US) | 20 | 200 | 600 | 1,500 |
| Estimated Monthly Organic Traffic | 0 | 300 | 1,500 | 5,000 |
| Average ranking position | n/a | 40 | 25 | 15 |
| AI Citation mentions/mo (manual sample) | 0 | 5 | 25 | 80 |
| Backlinks from authentic editorial sources | <5 | 25 | 75 | 200 |

(Targets assume consistent execution of the 90-day plan + sustained content investment. EB-5 is a high-difficulty YMYL niche; sustainable competitive position requires 12-24 months.)

---

## 5. Files in this audit

```
openeb5-seo-audit/
├── FULL-AUDIT-REPORT.md          ← this file
├── ACTION-PLAN.md                ← prioritized fix queue
├── reports/
│   ├── technical-seo.md          ← caching, security headers, sitemap, hreflang, plugins
│   ├── content-eeat.md           ← YMYL compliance, pillar audit, content gaps
│   ├── schema-markup.md          ← ready-to-paste JSON-LD for every page type
│   ├── performance-cwv.md        ← CWV estimate, resource inventory, plugin bloat
│   ├── geo-ai-readiness.md       ← AI crawler access, llms.txt template, citability
│   └── backlinks-competitive.md  ← backlink quality, competitor gap, keyword targets
└── data/
    ├── homepage.html             ← raw HTML snapshot
    ├── homepage-ES.html          ← Spanish homepage raw HTML
    ├── homepage_headers.txt      ← HTTP response headers
    ├── robots.txt
    ├── sitemap_index.xml
    ├── post-sitemap.xml
    ├── page-sitemap.xml
    ├── category-sitemap.xml
    ├── llms.txt                  ← 404 capture (file does not exist on site)
    ├── security.txt              ← 404 capture
    └── security-wellknown.txt    ← 404 capture
```

---

## 6. Next Steps (to integrate Ahrefs once attached)

When you attach openeb5.com to Ahrefs:

1. **Cross-check Authority Score** — Ahrefs DR vs SEMrush AS 2 (expect Ahrefs DR around 5-15 because Ahrefs's index is smaller)
2. **Backlink overlap** — Pull Ahrefs referring domains and diff against SEMrush's 93. Authentic editorial backlinks may show up better in one tool than the other.
3. **Ahrefs Content Gap tool** — Run with seeds `eb5investors.com`, `iiusa.org`, `civitascapital.com`, `eb5capital.com` to surface the actionable keyword gap. This will be more precise than SEMrush's gap tool because Ahrefs's keyword set is broader in the EB-5 niche.
4. **Ahrefs Site Audit** — Should report similar issues to this audit; use the prioritized issues report to validate.
5. **Top organic pages of competitors** — Ahrefs's "Top Pages 2.0" will reveal which exact URLs drive eb5investors.com's 6,333 monthly traffic so we can target their patterns.
6. **Disavow review** — If Ahrefs flags toxic backlinks at higher confidence than SEMrush, then reconsider the disavow recommendation in `backlinks-competitive.md`.
7. **Branded SOV** — Ahrefs Brand Radar for "Open EB5" / "OpenEB5" share-of-voice across LLM responses.
8. **Keyword tracker** — Set up tracking for: EB-5 visa, EB-5 minimum investment, EB-5 regional center, midtown pharr, EB-5 grandfathering, plus the 15 keyword-gap targets in `backlinks-competitive.md`.

Once Ahrefs data is in, I'll re-run the audit with cross-referenced metrics for a tighter prioritization. The plan above does not change directionally — only the precise list of link-building targets and content gaps will sharpen.

---

**Prepared for:** Open EB5 — internal SEO planning
**Prepared by:** Claude (Anthropic) — automated audit using SEMrush MCP + multi-skill SEO toolkit
