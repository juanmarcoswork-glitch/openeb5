# Schema Markup Audit & Generation — openeb5.com

**Date:** 2026-05-11
**Current source:** Yoast SEO @graph output

---

## 1. Current Schema Inventory

Homepage emits one JSON-LD block from Yoast containing:

| @type | Status | Issues |
|---|---|---|
| WebPage | ✅ Present | OK; uses dateModified |
| ImageObject (logo) | ⚠️ Present | Dimensions 308×45 in OG image but 674×150 in Organization.logo. Inconsistent. Logo is too narrow for square-aspect placements (e.g., Knowledge Panel needs square or close-to-square). |
| BreadcrumbList | ❌ Invalid | Only 1 ListItem ("Home"). Google requires ≥2 for rich result. |
| WebSite (+ SearchAction) | ✅ Present | SearchAction is OK; site has `/?s=...` working. |
| Organization | ⚠️ Severely weak | `name`: lowercase "openeb5"; `description`: empty string; **no telephone, address, contactPoint, sameAs, founder, foundingDate, areaServed, knowsLanguage** |

**Other pages sampled (`/eb-5/`, `/the-complete-guide-to-eb-5-investment/`, `/the-team/`):** Likely emit the same minimal Yoast graph (WebPage + WebSite + Organization). No page-specific entity enrichment.

---

## 2. Missing Schema Types (Critical Gaps)

| Schema | Recommended for page | Rich result impact |
|---|---|---|
| LocalBusiness / FinancialService | Homepage, /contact-us/ | Local pack eligibility, Knowledge Panel |
| FAQPage | /eb-5/, pillar guide, blog Q&A posts | FAQ rich snippet (high SERP real estate) |
| HowTo | Pillar guide (EB-5 process steps) | HowTo rich snippet (deprecated by Google but still good for AI extraction) |
| Article + Person | All 19 blog posts | Article rich snippet, author byline, AI citation eligibility |
| Service | /eb-5/, /investors/, /current-projects/ | Knowledge Panel, "About this result" eligibility |
| InvestmentOrLoan / FinancialProduct | /midtown-pharr/, /midtown-brownsville/, /current-projects/ | Search Console eligibility, GEO citability |
| Person | /the-team/, /advisory-board/ | E-E-A-T strengthening, author entity establishment |
| VideoObject | Pages embedding YouTube videos | Video rich snippet |
| Event | Webinars/seminars (if any) | Event rich snippet |
| Course | Could re-purpose pillar guide as Course | Featured snippet eligibility |
| BreadcrumbList | All non-home pages with proper crumbs | Breadcrumb rich snippet |

---

## 3. Ready-to-deploy JSON-LD blocks

### 3.1 Homepage — Replace the Organization block with FinancialService

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "FinancialService",
      "@id": "https://openeb5.com/#organization",
      "name": "Open EB5",
      "alternateName": "OpenEB5",
      "url": "https://openeb5.com/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://openeb5.com/#logo",
        "url": "https://openeb5.com/wp-content/uploads/2024/10/OpenEB5_logo.jpg",
        "width": 674,
        "height": 150,
        "caption": "Open EB5"
      },
      "image": { "@id": "https://openeb5.com/#logo" },
      "description": "USCIS-approved EB-5 Regional Center and investment advisory firm based in McAllen, Texas. We guide international investors through the EB-5 immigrant investor program — from project selection to permanent U.S. residency.",
      "telephone": "+1-855-673-6325",
      "email": "open@openeb5.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "3900 N. 10th St, Suite 1080",
        "addressLocality": "McAllen",
        "addressRegion": "TX",
        "postalCode": "78501",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 26.2627,
        "longitude": -98.2289
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
          "opens": "09:00",
          "closes": "18:00"
        }
      ],
      "knowsLanguage": ["en","es","zh","hi","vi","ko","fa","ar","pt"],
      "areaServed": [
        { "@type": "Country", "name": "United States" },
        { "@type": "Country", "name": "Mexico" },
        { "@type": "Country", "name": "China" },
        { "@type": "Country", "name": "India" },
        { "@type": "Country", "name": "Vietnam" },
        { "@type": "Country", "name": "South Korea" },
        { "@type": "Country", "name": "Brazil" },
        { "@type": "Country", "name": "Argentina" },
        { "@type": "Country", "name": "Colombia" },
        { "@type": "Country", "name": "Peru" },
        { "@type": "Country", "name": "Chile" }
      ],
      "sameAs": [
        "https://www.facebook.com/openeb5",
        "https://www.linkedin.com/company/open-eb5/",
        "https://www.instagram.com/open.eb5/",
        "https://www.youtube.com/@0penEB5"
      ],
      "hasCredential": [
        {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "license",
          "name": "USCIS Regional Center Designation",
          "recognizedBy": {
            "@type": "GovernmentOrganization",
            "name": "U.S. Citizenship and Immigration Services",
            "url": "https://www.uscis.gov/"
          },
          "identifier": "TODO_REPLACE_WITH_ACTUAL_RC_NUMBER"
        }
      ],
      "memberOf": {
        "@type": "Organization",
        "name": "Invest in the USA (IIUSA)",
        "url": "https://iiusa.org/"
      },
      "founder": {
        "@type": "Person",
        "name": "Emilio Guzmán"
      },
      "foundingLocation": {
        "@type": "Place",
        "address": { "@type": "PostalAddress", "addressLocality": "McAllen", "addressRegion": "TX", "addressCountry": "US" }
      },
      "parentOrganization": {
        "@type": "Organization",
        "name": "The Broaddus Companies",
        "url": "https://broaddususa.com/"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://openeb5.com/#website",
      "url": "https://openeb5.com/",
      "name": "Open EB5",
      "description": "USCIS-approved EB-5 Regional Center — invest in Texas projects for U.S. permanent residency.",
      "publisher": { "@id": "https://openeb5.com/#organization" },
      "inLanguage": ["en-US","es"],
      "potentialAction": [{
        "@type": "SearchAction",
        "target": { "@type": "EntryPoint", "urlTemplate": "https://openeb5.com/?s={search_term_string}" },
        "query-input": { "@type": "PropertyValueSpecification", "valueRequired": true, "valueName": "search_term_string" }
      }]
    },
    {
      "@type": "WebPage",
      "@id": "https://openeb5.com/#webpage",
      "url": "https://openeb5.com/",
      "name": "USCIS-Approved EB-5 Regional Center | Open EB5 — Texas",
      "isPartOf": { "@id": "https://openeb5.com/#website" },
      "about": { "@id": "https://openeb5.com/#organization" },
      "inLanguage": "en-US",
      "datePublished": "2024-10-22T19:20:31+00:00",
      "dateModified": "2026-02-04T00:40:01+00:00"
    }
  ]
}
</script>
```

> Replace `TODO_REPLACE_WITH_ACTUAL_RC_NUMBER` with the real USCIS Regional Center ID. Remove the `hasCredential` block if not yet designated.

### 3.2 /eb-5/ — Service + FAQPage + BreadcrumbList

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "@id": "https://openeb5.com/eb-5/#service",
      "name": "EB-5 Immigrant Investor Advisory",
      "url": "https://openeb5.com/eb-5/",
      "provider": { "@id": "https://openeb5.com/#organization" },
      "serviceType": "Immigration Investment Advisory",
      "areaServed": { "@type": "AdministrativeArea", "name": "Worldwide" },
      "audience": { "@type": "Audience", "audienceType": "International investors seeking U.S. permanent residency" },
      "description": "End-to-end EB-5 visa advisory: project due diligence, source-of-funds documentation, I-526E petition support, escrow management, and I-829 conditional removal guidance.",
      "offers": {
        "@type": "Offer",
        "priceCurrency": "USD",
        "price": "800000",
        "priceSpecification": {
          "@type": "PriceSpecification",
          "priceCurrency": "USD",
          "minPrice": "800000",
          "maxPrice": "1050000",
          "description": "USCIS minimum investment: $800,000 in a Targeted Employment Area (TEA) or $1,050,000 in a non-TEA project."
        }
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://openeb5.com/eb-5/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the minimum investment for an EB-5 visa in 2026?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The minimum EB-5 investment is $800,000 for projects located in a Targeted Employment Area (TEA) — typically rural areas or regions with unemployment at or above 150% of the national average. For projects outside a TEA, the minimum is $1,050,000. These amounts were set by the EB-5 Reform and Integrity Act of 2022."
          }
        },
        {
          "@type": "Question",
          "name": "What is a USCIS-approved Regional Center?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Regional Center is an entity designated by USCIS to sponsor EB-5 investment projects on behalf of foreign investors. Regional Centers can count both direct and indirect job creation toward the EB-5 program's 10-jobs-per-investor requirement, making compliance easier than the Direct EB-5 path."
          }
        },
        {
          "@type": "Question",
          "name": "How long does the EB-5 process take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Processing times vary by country of chargeability and project. As of 2026, I-526E petition processing averages 18–36 months. Conditional permanent residency is granted upon approval and consular processing; the I-829 to remove conditions is filed two years later."
          }
        },
        {
          "@type": "Question",
          "name": "What is the EB-5 Reform and Integrity Act of 2022?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Signed into law on March 15, 2022, the EB-5 Reform and Integrity Act reauthorized the Regional Center program through September 30, 2027, raised investment minimums, introduced reserved visa categories (rural, high unemployment, infrastructure), and added integrity measures including mandatory audits and fund administration."
          }
        },
        {
          "@type": "Question",
          "name": "What is the EB-5 grandfathering deadline?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The EB-5 Reform and Integrity Act includes grandfathering protections for petitions filed before September 30, 2026, meaning eligible investors can still receive a green card even if the Regional Center program later lapses. Investors planning EB-5 filings should consult with counsel about the September 30, 2026 deadline."
          }
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://openeb5.com/eb-5/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://openeb5.com/" },
        { "@type": "ListItem", "position": 2, "name": "EB-5 Program", "item": "https://openeb5.com/eb-5/" }
      ]
    }
  ]
}
</script>
```

### 3.3 /the-complete-guide-to-eb-5-investment/ — Article + HowTo + FAQ

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://openeb5.com/the-complete-guide-to-eb-5-investment/#article",
      "headline": "The Complete EB-5 Investor Visa Guide (2026)",
      "description": "Step-by-step guide to the EB-5 immigrant investor program: $800,000 minimum, TEA designation, Regional Center vs Direct, I-526E and I-829 petitions, and the path to a U.S. green card.",
      "image": "https://openeb5.com/wp-content/uploads/your-pillar-hero.jpg",
      "datePublished": "2024-10-22",
      "dateModified": "2026-05-11",
      "author": {
        "@type": "Person",
        "name": "Emilio Guzmán",
        "jobTitle": "CEO",
        "url": "https://openeb5.com/the-team/",
        "sameAs": ["https://www.linkedin.com/in/TODO"]
      },
      "reviewedBy": {
        "@type": "Person",
        "name": "TODO — Named Immigration Attorney",
        "jobTitle": "Immigration Counsel",
        "hasCredential": {
          "@type": "EducationalOccupationalCredential",
          "credentialCategory": "Bar Admission",
          "recognizedBy": { "@type": "Organization", "name": "TODO — State Bar" }
        }
      },
      "publisher": { "@id": "https://openeb5.com/#organization" },
      "mainEntityOfPage": { "@type": "WebPage", "@id": "https://openeb5.com/the-complete-guide-to-eb-5-investment/" },
      "about": [
        { "@type": "Thing", "name": "EB-5 Visa" },
        { "@type": "Thing", "name": "Immigrant Investor Program" },
        { "@type": "Thing", "name": "USCIS Regional Center Program" },
        { "@type": "Thing", "name": "EB-5 Reform and Integrity Act of 2022" }
      ]
    },
    {
      "@type": "HowTo",
      "name": "How to Obtain a U.S. Green Card Through the EB-5 Visa Program",
      "totalTime": "P36M",
      "estimatedCost": { "@type": "MonetaryAmount", "currency": "USD", "value": "800000" },
      "step": [
        { "@type": "HowToStep", "position": 1, "name": "Initial consultation & eligibility", "text": "Confirm accredited-investor status and source-of-funds documentation pathway." },
        { "@type": "HowToStep", "position": 2, "name": "Project selection & due diligence", "text": "Choose a USCIS-approved Regional Center project; review the I-956F project filing, business plan, and economic study." },
        { "@type": "HowToStep", "position": 3, "name": "Investment & escrow", "text": "Transfer the $800,000 (TEA) or $1,050,000 (non-TEA) to escrow." },
        { "@type": "HowToStep", "position": 4, "name": "File I-526E petition", "text": "Submit Form I-526E and supporting documents to USCIS." },
        { "@type": "HowToStep", "position": 5, "name": "Conditional permanent residency", "text": "Upon approval, complete consular processing or adjustment of status." },
        { "@type": "HowToStep", "position": 6, "name": "Sustain investment & create jobs", "text": "Capital must be at risk and create at least 10 jobs over the conditional residency period." },
        { "@type": "HowToStep", "position": 7, "name": "File I-829 to remove conditions", "text": "Within 90 days of the 2-year anniversary, file I-829 to obtain unconditional permanent residency." }
      ]
    }
  ]
}
</script>
```

### 3.4 /midtown-pharr/ — InvestmentOrLoan + RealEstateAgent fallback

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "InvestmentOrDeposit",
  "@id": "https://openeb5.com/midtown-pharr/#offering",
  "name": "Midtown Pharr EB-5 Investment Project",
  "amount": { "@type": "MonetaryAmount", "currency": "USD", "value": "800000" },
  "provider": { "@id": "https://openeb5.com/#organization" },
  "url": "https://openeb5.com/midtown-pharr/",
  "description": "Midtown Pharr is a USCIS-approved EB-5 Regional Center project in Pharr, Texas. The project received I-956F approval, enabling I-526E petitions to be filed. Located in a Targeted Employment Area (TEA), qualifying investors at the $800,000 minimum.",
  "identifier": [
    { "@type": "PropertyValue", "propertyID": "USCIS I-956F Filing", "value": "TODO_REPLACE_WITH_I956F_RECEIPT" },
    { "@type": "PropertyValue", "propertyID": "Regional Center", "value": "Open EB5" },
    { "@type": "PropertyValue", "propertyID": "TEA Designation", "value": "Confirmed — High Unemployment Area" }
  ],
  "location": {
    "@type": "Place",
    "name": "Pharr, Texas, USA",
    "address": { "@type": "PostalAddress", "addressLocality": "Pharr", "addressRegion": "TX", "addressCountry": "US" }
  }
}
</script>
```

### 3.5 /the-team/ — Person array

For each team member with a bio, emit a Person:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Person",
      "@id": "https://openeb5.com/the-team/#emilio-guzman",
      "name": "Emilio Guzmán",
      "jobTitle": "Chief Executive Officer",
      "worksFor": { "@id": "https://openeb5.com/#organization" },
      "image": "https://openeb5.com/wp-content/uploads/team/emilio-guzman.jpg",
      "url": "https://openeb5.com/the-team/#emilio-guzman",
      "sameAs": ["https://www.linkedin.com/in/TODO"],
      "alumniOf": [
        { "@type": "EducationalOrganization", "name": "Harvard Business School", "url": "https://www.hbs.edu/" }
      ],
      "knowsAbout": ["EB-5 Visa Program","Real Estate Investment","International Capital","U.S. Immigration Investment"],
      "description": "25+ years in residential and commercial real estate, board member of the U.S.-Mexico Business Association, has assisted over 300 investor families."
    },
    {
      "@type": "Person",
      "@id": "https://openeb5.com/the-team/#ricardo-rubiano",
      "name": "Ricardo Rubiano",
      "jobTitle": "CEO Open Multifamily",
      "worksFor": { "@id": "https://openeb5.com/#organization" },
      "alumniOf": [
        { "@type": "CollegeOrUniversity", "name": "U.S. Naval Academy" },
        { "@type": "CollegeOrUniversity", "name": "Texas A&M University" }
      ],
      "knowsAbout": ["Multifamily Real Estate Development","EB-5 Project Underwriting"]
    }
    // Add Person blocks for the 8 administrative staff once bios are written.
  ]
}
</script>
```

### 3.6 Blog posts — Article (replace generic WebPage)

For each `/YYYY/MM/DD/slug/` URL (also for `/ES/YYYY/MM/DD/slug/`):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Open EB5 Secures I-956F Approval for Midtown Pharr",
  "description": "Open EB5 receives USCIS I-956F project approval for the Midtown Pharr development in the Rio Grande Valley, enabling investors to file I-526E petitions.",
  "image": ["https://openeb5.com/wp-content/uploads/2026/04/midtown-pharr-hero.jpg"],
  "datePublished": "2026-04-27",
  "dateModified": "2026-04-27",
  "author": {
    "@type": "Person",
    "name": "Emilio Guzmán",
    "url": "https://openeb5.com/the-team/#emilio-guzman"
  },
  "publisher": { "@id": "https://openeb5.com/#organization" },
  "mainEntityOfPage": "https://openeb5.com/2026/04/27/open-eb5-secures-i-956f-approval-for-midtown-pharr-a-milestone-in-the-rio-grande-valley/",
  "articleSection": "News",
  "inLanguage": "en-US"
}
</script>
```

---

## 4. Implementation Path

**On Yoast SEO:**
- Yoast → General → Site Representation → set Organization name to `Open EB5` (proper capitalization). Set organization phone & logo. This fixes ~80% of the Organization schema issues sitewide.
- Yoast → Search Appearance → Content Types → enable schema enhancement for Posts (Article), Pages (WebPage), and any custom post types.
- Pro plan or **WPCode** snippets for the non-default types (LocalBusiness/FinancialService, FAQPage, HowTo, InvestmentOrDeposit, Person).

**Recommended workflow:**
1. Update Yoast Organization globally (fixes brand name + logo across all pages).
2. Install **WPCode** (free).
3. Add a global snippet that injects the FinancialService block on the homepage only (via URL targeting).
4. Add page-specific snippets for FAQ, HowTo, Article on the pillar pages.
5. Validate with Google Rich Results Test: https://search.google.com/test/rich-results
6. Validate with Schema.org Validator: https://validator.schema.org/

---

## 5. Priority Implementation Order

| # | Page | Schema | Impact | Effort |
|---|---|---|---|---|
| 1 | All pages | Fix Organization name + add LocalBusiness fields globally via Yoast | Critical — affects Knowledge Panel | 1 hour |
| 2 | /eb-5/ | FAQPage + Service + Breadcrumb | High — FAQ rich snippet | 2 hours |
| 3 | /the-complete-guide-to-eb-5-investment/ | Article + HowTo + FAQ | High — featured snippet + AI citation | 3 hours |
| 4 | /the-team/ | Person × 10 | High — E-E-A-T | 4 hours (needs bio content first) |
| 5 | /midtown-pharr/ + /midtown-brownsville/ | InvestmentOrDeposit + Breadcrumb | High — project page conversion | 2 hours each |
| 6 | All blog posts | Article (replace generic WebPage) | Medium — sitewide blog | 1 hour (template change in Yoast) |
| 7 | All pages | Fix BreadcrumbList (≥2 items) | Medium — Breadcrumb rich result | 1 hour |
| 8 | YouTube embeds | VideoObject | Medium — video rich snippet | 2 hours |

**Schema score (current): 25/100** → **target after fixes: 90/100**
