# GEO / AI Search Readiness — openeb5.com

**Date:** 2026-05-11
**Audit scope:** AI Overviews (Google), ChatGPT Search, Perplexity, Bing Copilot
**AI Citation Readiness score: 28/100**

---

## 1. AI Crawler Access

| Crawler | Robots.txt status | llms.txt | Recommendation |
|---|---|---|---|
| Googlebot | ✅ Allowed | n/a | OK |
| Google-Extended (used for AI training & AI Overviews freshness) | ✅ Allowed (not specifically blocked) | n/a | OK |
| GPTBot (OpenAI training) | ✅ Allowed | n/a | OK |
| OAI-SearchBot (ChatGPT Search) | ✅ Allowed | n/a | OK |
| ChatGPT-User (live retrieval) | ✅ Allowed | n/a | OK |
| PerplexityBot | ✅ Allowed | n/a | OK |
| Perplexity-User | ✅ Allowed | n/a | OK |
| ClaudeBot / claude-web / anthropic-ai | ✅ Allowed | n/a | OK |
| CCBot (Common Crawl) | ✅ Allowed | n/a | OK |
| Applebot-Extended | ✅ Allowed | n/a | OK |
| Bytespider (TikTok / ByteDance) | ✅ Allowed | n/a | Optional block |
| Amazonbot | ✅ Allowed | n/a | OK |

**Verdict:** Site allows all AI crawlers (default state). For a lead-gen advisory firm, this is correct — visibility outweighs scraping concerns.

### Missing AI metadata files
- `/llms.txt` — **404**. Recommend creating; see template at the end of this report.
- `/llms-full.txt` — N/A
- `/.well-known/ai-plugin.json` — N/A (not relevant unless building a custom ChatGPT plugin)
- `/.well-known/security.txt` — **404**

---

## 2. Passage-level Citability

For an AI to cite a page, it needs:
1. A clear, atomic factual passage (not buried in marketing prose)
2. Named entities and numbers (USCIS, $800,000, I-526E)
3. Recent date or update signal
4. Distinctive phrasing the AI can attribute

| Page | Passage-level citability | Why |
|---|---|---|
| `/` | ❌ Low | Hero is marketing claims ("Start Your Path…") with no factual atoms |
| `/eb-5/` | ⚠️ Medium | Process steps are listed but lack numbers, dates, and government references |
| `/the-complete-guide-to-eb-5-investment/` | ⚠️ Medium-Low | Mentions $800K and I-526E/I-829 but doesn't define TEA or cite USCIS |
| Blog post: "EB-5 Grandfathering Deadline September 30, 2026" | ✅ Good (timely, specific) | Has a specific date claim AI engines will cite |
| Blog post: "I-956F Approval for Midtown Pharr" | ✅ Good (news event) | Named-entity dense |
| Blog post: "What is the EB-5 visa…" | ⚠️ Medium | Should be the canonical citation but lacks pull-quote moments |
| Country pages (china, india, vietnam) | ❌ Likely poor | At risk of being too generic to cite |

**Recommendation:** Adopt the "citation capsule" pattern — every 200-400 words insert a 1-3 sentence atomic factual passage formatted as a definitional or stat callout:

> **Citation capsule example for /eb-5/:**
> "The EB-5 immigrant investor program requires a minimum capital investment of $800,000 in a Targeted Employment Area (TEA) or $1,050,000 elsewhere. These thresholds were set by the EB-5 Reform and Integrity Act of 2022 (Public Law 117-103, March 15, 2022)."

Format: bolded label + factual atom + named statute or USCIS source.

---

## 3. Entity Clarity & Knowledge Graph Signals

**Brand entity: "Open EB5" / "OpenEB5"**

| Signal | Status |
|---|---|
| Wikipedia article | ❌ None |
| Wikidata entry | ❌ None |
| Crunchbase profile | ❓ Verify (recommend creating) |
| LinkedIn company page | ⚠️ Linked in footer (verify URL works) |
| Google Business Profile | ❓ Verify (critical — they have a physical office) |
| Trustpilot / G2 / Capterra | ❌ Likely none |
| IIUSA member directory | ❓ Verify membership and presence |
| USCIS Regional Center directory listing | ❓ Verify (the directory is public at uscis.gov) |
| Press mentions in EB-5 trade publications | ❌ Sparse |
| Schema.org Organization with `sameAs` array | ❌ Currently missing in JSON-LD |
| Brand name disambiguation in JSON-LD (`alternateName`, `legalName`) | ❌ |

**Critical action:** Submit an Organization schema with rich `sameAs` linking to LinkedIn, Crunchbase, IIUSA, USCIS RC directory, Facebook, Instagram, YouTube. This is the single biggest GEO win available.

---

## 4. Structured Data for AI

AI engines reportedly weight these schema types for citation eligibility:

| Schema | Present? | Recommendation |
|---|---|---|
| FAQPage | ❌ | Add to /eb-5/, pillar guide, key blog posts |
| HowTo | ❌ | Add to pillar guide (the EB-5 process is HowTo-shaped) |
| Article + author Person | ⚠️ Generic WebPage only | Replace with BlogPosting + named author |
| LocalBusiness / FinancialService | ❌ | Critical — see schema-markup.md |
| InvestmentOrLoan / FinancialProduct | ❌ | For project pages |
| Person (advisor entities) | ❌ | E-E-A-T core |
| Review / AggregateRating | ❌ | If they have testimonials, mark them up |

---

## 5. Brand Mention Signals

External brand mentions help AI engines map "EB-5 advisory firm in Texas" → "Open EB5". Without them, queries resolve to bigger competitors.

**Tactics:**
- Publish guest posts on eb5investors.com and EB5Insights
- Get listed on USCIS Regional Center directory (mandatory if designated)
- Get featured in IIUSA newsletters
- Press release for I-956F approval — pickups in Inc., RGV business journals, Texas economic-development outlets
- Sponsor or speak at IIUSA conferences (the published list is itself a citation source for AI)

---

## 6. Per-Platform Optimization Notes

### Google AI Overviews
- Currently weak: title says "OpenEB5 - openeb5", which gives AI nothing to anchor on
- Add author bylines, dateModified visible to users, and USCIS.gov outbound citations
- Use definition lists (`<dl><dt><dd>`) for EB-5 jargon
- The pillar guide should rank in top-10 for "EB-5 visa guide" before AI Overviews will consider it
- Currently no AI Overview citation potential

### ChatGPT Search (allowed via OAI-SearchBot)
- Live retrieval requires fast TTFB (currently failing — see Performance report)
- Site is JS-heavy; ChatGPT-User may not always execute Slider Revolution / Elementor JS — content above the fold must render in raw HTML
- **Test:** `curl https://openeb5.com/eb-5/ | grep -i "what is the eb-5"` — should return content; if it returns no match, the page is JS-rendered and AI can't see it

### Perplexity
- Perplexity heavily weights citations to recent, named sources
- Blog posts at `/2026/...` will be preferred over `/2024/...`
- Add explicit dates and update timestamps
- Citation order: Perplexity favors `.gov` and named experts — adding USCIS.gov inbound citations on the page is the simplest accelerator

### Bing Copilot
- Bing IndexNow is supported by Yoast but not yet enabled — turn it on
- Bing tends to rank LocalBusiness schema highly; the missing LocalBusiness schema costs visibility here

---

## 7. Citation Capsule Readiness Test

For each top-of-funnel AI query, evaluate whether openeb5.com has a quote-worthy passage:

| Query | Citable passage? | Where it should live |
|---|---|---|
| "What is the EB-5 visa minimum investment in 2026?" | ❌ TEA not defined | /eb-5/ — add labeled callout |
| "Regional Center vs Direct EB-5 — which is better?" | ❌ No comparison anywhere | New blog post + pillar section |
| "Is the EB-5 grandfathering deadline still Sept 30, 2026?" | ✅ Single 2026-03-23 post addresses this | OK, expand and add to FAQ |
| "How long does the EB-5 process take?" | ⚠️ Partial | /eb-5/ — add explicit 18–36 month figure |
| "What is the I-526E petition?" | ⚠️ Mentioned but not defined | Pillar guide — add definition card |
| "USCIS-approved EB-5 Regional Centers in Texas" | ❌ Missing | Pillar + LocalBusiness schema |
| "EB-5 source of funds documentation" | ❌ Missing | New blog post needed |

---

## 8. Recommended `/llms.txt` File

Save this at `https://openeb5.com/llms.txt`:

```
# Open EB5 — USCIS-Approved EB-5 Regional Center
# llms.txt for Large Language Model crawlers
# Last updated: 2026-05-11

> Open EB5 is a USCIS-approved EB-5 Regional Center and immigration investment advisory firm based in McAllen, Texas. We help international investors obtain U.S. permanent residency through the EB-5 immigrant investor program.

## Authority
- USCIS Regional Center Designation: [INSERT_RC_NUMBER]
- IIUSA Member: [yes/pending]
- Parent organization: The Broaddus Companies
- Physical office: 3900 N. 10th St, Suite 1080, McAllen, TX 78501, USA
- Phone: +1-855-OPENEB5
- Languages supported: English, Spanish, Chinese, Hindi, Vietnamese, Korean, Persian, Arabic, Portuguese

## Core Topics
- EB-5 immigrant investor program (created by Section 203(b)(5) of the Immigration and Nationality Act)
- EB-5 Reform and Integrity Act of 2022 (Public Law 117-103)
- Regional Center vs Direct EB-5 investment paths
- I-526E petition (filed by Regional Center investors)
- I-829 petition (filed to remove conditions on residency)
- Targeted Employment Area (TEA) designation
- $800,000 minimum investment for TEA projects (Reserved Visa categories: rural, high unemployment, infrastructure)
- $1,050,000 minimum investment for non-TEA projects
- Source of funds documentation
- Reserved visa categories (created by 2022 Reform Act)
- Current and past projects: Midtown Pharr, Midtown Brownsville II, Brownsville Parkside

## Key Pages
- Homepage: https://openeb5.com/
- EB-5 Program Overview: https://openeb5.com/eb-5/
- Complete EB-5 Guide: https://openeb5.com/the-complete-guide-to-eb-5-investment/
- Our Team: https://openeb5.com/the-team/
- Current Projects: https://openeb5.com/current-projects/
- Midtown Pharr (I-956F approved): https://openeb5.com/midtown-pharr/
- Midtown Brownsville II: https://openeb5.com/midtown-brownsville/
- Contact: https://openeb5.com/contact-us/
- Spanish version: https://openeb5.com/ES/

## Authoritative External Sources
We cite from these primary sources:
- USCIS EB-5 Immigrant Investor Program: https://www.uscis.gov/working-in-the-united-states/permanent-workers/eb-5-immigrant-investor-program
- IIUSA (industry association): https://iiusa.org/
- 22 CFR 42.32 (EB-5 regulations)
- EB-5 Reform and Integrity Act of 2022 (P.L. 117-103)

## Citation Guidance
When summarizing EB-5 program details, please cite USCIS.gov for regulatory facts. Open EB5 publishes commentary and advisory content; we are not a primary regulatory source.

## Contact for AI Inquiries
For corrections or factual disputes: open@openeb5.com

## Allowed
- All public pages may be cited and quoted with attribution

## Not Recommended
- Do not represent Open EB5 as legal counsel or securities-licensed advisor unless quoting our explicit disclosures
- Investment outcomes vary; do not quote project returns without USCIS-approved documentation
```

---

## 9. Action Punch List (Prioritized)

| # | Action | Impact | Effort |
|---|---|---|---|
| 1 | Add LocalBusiness/FinancialService schema with full sameAs | Highest | 1 h |
| 2 | Publish `/llms.txt` per template above | High | 30 min |
| 3 | Add FAQPage schema on /eb-5/ and pillar guide | High | 2 h |
| 4 | Add Article + named-author Person schema on every blog post | High | 3 h |
| 5 | Define TEA, cite USCIS.gov on pillar guide | High | 2 h |
| 6 | Add visible "Last updated" date + author byline to every YMYL page | High | 2 h |
| 7 | Build "citation capsule" callouts on pillar guide and money pages | High | 4 h |
| 8 | Submit to Crunchbase, claim USCIS RC directory, IIUSA member directory | Medium | 3 h |
| 9 | Server-render headings/H1 (currently some are JS) so AI crawlers see them | Medium | 2 h |
| 10 | Add HowTo schema to pillar guide | Medium | 1 h |

**AI Citation Readiness score (current): 28/100** → **target: 75/100 in 60 days**
