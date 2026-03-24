# Data Availability Survey: "Specification Labor" Research

*Compiled: March 2026*

---

## 1. Executive Summary

### Best-supported prediction: Prediction 1 (Specification Wage Premium)

Prediction 1 has **excellent** data support. You can construct a specification wage premium time series today using:
- **BLS OEWS** (occupational wages, 1997–2024, 6-digit SOC, national/state/metro)
- **O\*NET** (42 Generalized Work Activities to classify spec-vs-execution occupations)
- **Multiple AI exposure indices** (Felten, Webb, Eloundou — all downloadable, all mapped to SOC codes)
- **IPUMS-CPS** (individual-level wage data by occupation, 1962–present)

All four are **free, downloadable, and directly mergeable** via SOC codes.

### Prediction 2 (Craft Premium / Attention Economy)

Prediction 2 has **moderate** data support — strong in some dimensions, weak in others:
- **Strong**: Craft beer (Brewers Association), craft spirits (ACSA), Etsy GMV (SEC filings), indie bookstores (ABA), farmers markets (USDA) — all have multi-year trend data showing growing craft/specification-heavy segments
- **Moderate**: ATUS shopping time (2003–present, specific activity codes exist), BrightLocal review surveys (annual since ~2014)
- **Weak**: No single dataset cleanly measures "time spent on product research/evaluation" as a distinct category over long periods. Digital attention data (SimilarWeb, Comscore) is proprietary.

### Biggest gaps
1. No clean longitudinal measure of "consumer specification effort" (time/money spent choosing vs. consuming)
2. No public dataset linking craft premiums to execution-automation levels by industry
3. Historical time-use data pre-2003 exists (IPUMS) but categories don't map perfectly to modern "product research"
4. Lightcast/Burning Glass job postings data is proprietary (though academic subsets exist)

---

## 2. Prediction 1 Data Inventory: Specification Wage Premium

### 2.1 Occupational Wage Data

| Source | URL | Access | Years | Granularity | Format | Relevance | Notes |
|--------|-----|--------|-------|-------------|--------|-----------|-------|
| **BLS OEWS** | [bls.gov/oes/](https://www.bls.gov/oes/) | Free | 1997–2024 | Annual; national/state/530+ MSAs; ~830 occupations by 6-digit SOC (2018 SOC from May 2021+) | Excel, CSV via download server | **HIGH** | Core wage dataset. Median & mean wages, employment counts. Download via [bls.gov/oes/tables.htm](https://www.bls.gov/oes/tables.htm). Historical data (1988–95) available but not directly comparable. SOC transition in 2018 requires crosswalk for longitudinal analysis. |
| **IPUMS-CPS** | [cps.ipums.org](https://cps.ipums.org/) | Free (registration) | 1962–present | Individual-level microdata; annual (ASEC) + monthly; national + state | Custom extracts (CSV, Stata, SPSS, SAS) | **HIGH** | Individual-level wage data (INCWAGE annual; EARNWEEK weekly; HOURWAGE hourly). Harmonized occupation codes. Better for distributional analysis and controlling for demographics. Requires account creation. |
| **ACS via IPUMS-USA** | [usa.ipums.org](https://usa.ipums.org/) | Free (registration) | 2000–present (annual); 1980–2000 (decennial) | Individual-level; national/state/PUMA | Custom extracts | **HIGH** | Larger sample sizes than CPS for small-area estimates. INCWAGE variable by occupation. |
| **Census BDS** | [census.gov/programs-surveys/bds/data.html](https://www.census.gov/programs-surveys/bds/data.html) | Free | 1978–2023 | Annual; national/state/MSA; by firm age/size/industry | CSV | **MEDIUM** | Firm entry/exit rates, job creation/destruction. Relevant for entrepreneurship/specification angle. 38 tables, 24 variables. |
| **BLS Consumer Expenditure Survey** | [bls.gov/cex/](https://www.bls.gov/cex/) | Free | 1984–present | Annual; national; by demographic characteristics | CSV, PDF | **MEDIUM** | Can track spending shifts toward specification-heavy goods (specialty food, craft goods, design services). Categories may be too aggregated for clean spec/commodity split. |

### 2.2 Occupation Classification & Task Content

| Source | URL | Access | Years | Granularity | Format | Relevance | Notes |
|--------|-----|--------|-------|-------------|--------|-----------|-------|
| **O\*NET Database** | [onetcenter.org/database.html](https://www.onetcenter.org/database.html) | Free (CC BY 4.0) | Current (v23.1); updated ~2x/year | ~1,000 occupations; 42 GWAs, 2,000+ DWAs, tasks, skills, abilities | Excel, CSV, MySQL, SQL Server, Oracle | **CRITICAL** | **This is your primary classification tool.** 42 Generalized Work Activities map directly to your spec/execution distinction (see Section 2.3 below). Full SOC code mapping. |
| **O\*NET Work Activities Taxonomy** | [onetonline.org/find/descriptor/browse/Work_Activities/](https://www.onetonline.org/find/descriptor/browse/Work_Activities/) | Free | Current | 42 GWAs organized in 4 categories with subcategories | Online browsable; downloadable via database | **CRITICAL** | See full taxonomy below. Each GWA has importance and level scores per occupation. |
| **Autor et al. (2024) "New Frontiers"** | [Harvard Dataverse DOI:10.7910/DVN/7RYD2E](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/7RYD2E) | Free | 1940–2018 | Occupation-level; decennial | Large files hosted on SharePoint (linked from Dataverse) | **HIGH** | Replication data for "New Frontiers: The Origins and Content of New Work, 1940–2018" (QJE 2024). Shows how new job categories emerge. Links patent data to new job title creation. Very relevant for spec labor thesis — new work = new specification. Published in QJE 139(3): 1399–1465. |

### 2.3 O\*NET Generalized Work Activities: Specification vs. Execution Mapping

The 42 GWAs can be classified for your framework:

**SPECIFICATION-SIDE (deciding WHAT to make/evaluating what was made):**
- 4.A.2.b.2 — **Thinking Creatively**
- 4.A.2.b.1 — **Making Decisions and Solving Problems**
- 4.A.2.a.1 — **Judging the Qualities of Objects, Services, or People**
- 4.A.2.b.4 — **Developing Objectives and Strategies**
- 4.A.2.b.5 — **Scheduling Work and Activities**
- 4.A.2.b.6 — **Organizing, Planning, and Prioritizing Work**
- 4.A.2.a.4 — **Analyzing Data or Information**
- 4.A.2.a.3 — **Evaluating Information to Determine Compliance with Standards**
- 4.A.4.b.5 — **Coaching and Developing Others**
- 4.A.4.b.6 — **Providing Consultation and Advice to Others**
- 4.A.4.a.6 — **Selling or Influencing Others**

**EXECUTION-SIDE (making the thing that was specified):**
- 4.A.3.a.3 — **Controlling Machines and Processes**
- 4.A.3.a.2 — **Handling and Moving Objects**
- 4.A.3.a.1 — **Performing General Physical Activities**
- 4.A.3.a.4 — **Operating Vehicles, Mechanized Devices, or Equipment**
- 4.A.3.b.3 — **Repairing and Maintaining Mechanical Equipment**
- 4.A.3.b.4 — **Repairing and Maintaining Electronic Equipment**
- 4.A.2.a.2 — **Processing Information** (borderline — could be either)
- 4.A.3.b.5 — **Documenting/Recording Information**

**METHODOLOGY**: For each occupation, O\*NET provides importance scores (1–5) and level scores (1–7) for each GWA. You can construct a **Specification Intensity Index** = (mean importance of spec-side GWAs) / (mean importance of all GWAs), or a ratio of spec-to-execution GWA scores.

### 2.4 AI Exposure / Automation Scores

| Source | URL | Access | Format | Methodology | Relevance | Notes |
|--------|-----|--------|--------|-------------|-----------|-------|
| **Felten, Raj & Seamans (2021) AIOE** | [github.com/AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE) | Free | Excel (.xlsx) | Links 10 AI applications to 52 O\*NET abilities; maps to 6-digit SOC (Appendix A), 4-digit NAICS (B), county FIPS (C). Includes ability-application matrix from MTurk survey (D). | **HIGH** | Most directly useful. Can merge with OEWS wages via SOC. Also has generative AI extensions (Image Generation, Language Modeling files). Published in Strategic Management Journal 42(12): 2195–2217. |
| **Eloundou et al. (2024) GPT Exposure** | [github.com/EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) (file: `gptsRgpts_occ_lvl.csv`) | Free | CSV | Human + GPT-4 rated alignment between LLM capabilities and O\*NET tasks. Three exposure definitions (E1, E1+0.5×E2, E1+E2). ~80% of US workforce has ≥10% task exposure. | **HIGH** | Published in Science 384: 1306–1308 (2024). Distinguishes direct LLM exposure (E1) from tool-augmented (E2) — relevant for spec vs. execution since E2 tasks may include specification work that humans still direct. |
| **Webb (2022) AI/Software/Robot Exposure** | [github.com/EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) (file: `exposure_by_occ1990dd_lswt2010.csv`) | Free | CSV | Text overlap between patent descriptions (Google Patents) and O\*NET job task descriptions. Separates AI, software, and robot exposure. | **HIGH** | Key finding: AI targets high-skill tasks (unlike software/robots). Can distinguish which specification tasks are AI-exposed vs. which execution tasks are. Uses David Dorn's occ1990dd codes (crosswalk included in repo). |
| **Eisfeldt, Schubert, Taska & Zhang (2024)** | [github.com/EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) (file: `genaiexp_estz_occscores.csv`) | Free | CSV | Generative AI exposure scores at occupation level | **HIGH** | Additional gen AI exposure measure complementing Eloundou. |
| **Frey & Osborne (2017)** | Appendix of published paper in Technological Forecasting & Social Change 114: 254–280 | Free (paper appendix) | PDF table (702 occupations) | Gaussian process classifier; automation probability 0–1 for 702 SOC occupations. | **MEDIUM** | Older methodology (pre-LLM) but widely cited. 47% of US jobs at high automation risk. Data in paper appendix — need to extract from PDF or find digitized version. |

**Critical resource**: The [EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) GitHub repo aggregates **all four major exposure indices** plus CPS microdata, O\*NET databases, and SOC crosswalks in one place. This is your one-stop shop.

### 2.5 Job Market / Posting Data

| Source | URL | Access | Relevance | Notes |
|--------|-----|--------|-----------|-------|
| **Lightcast (Burning Glass/EMSI)** | [lightcast.io](https://lightcast.io) | **Paid** (enterprise) | HIGH | 2.5B+ job postings, 800M+ career profiles. Gold standard. Academic access via data sharing agreements or Federal Statistical Research Data Centers. Some derived datasets published by researchers on Mendeley. |
| **Indeed Hiring Lab** | [hiringlab.org](https://www.hiringlab.org/) | Free (research reports only) | MEDIUM | Publishes wage trend analyses and labor market reports. No raw data downloads but useful for narrative evidence. |
| **LinkedIn Economic Graph** | N/A | **Not publicly available** | LOW | Data only available through LinkedIn's internal research team or approved partnerships. |
| **Glassdoor Research** | N/A | **Not publicly available** as datasets | LOW | Individual salary reports available but no bulk research datasets. |
| **Census Business Trends & Outlook Survey** | Included in EIG repo (National.xlsx, Sector.xlsx) | Free | MEDIUM | AI adoption at firm level (3.7% late 2023 → 6.6% late 2024). |

---

## 3. Prediction 2 Data Inventory: Craft Premium / Attention Economy

### 3.1 Consumer Time Allocation

| Source | URL | Access | Years | Granularity | Format | Relevance | Notes |
|--------|-----|--------|-------|-------------|--------|-----------|-------|
| **ATUS (via BLS)** | [bls.gov/tus/data.htm](https://www.bls.gov/tus/data.htm) | Free | 2003–present | Annual; ~10K–13K respondents/year; 24-hr diary; national | CSV/DAT files | **HIGH** | Key activity codes: **0701xx** (shopping/purchasing) — 070101 (grocery), 070103 (food not groceries), 070104 (shopping except groceries/food/gas), 070105 (waiting). **0702xx** (researching purchases) — 070201 (by telephone), 070299 (n.e.c., likely captures online research). **CRITICAL NOTE**: The 0702 "researching purchases" codes were **added in 2010** — pre-2010 research time is coded under general shopping, creating a structural break. Activity lexicon at [bls.gov/tus/lexicons.htm](https://www.bls.gov/tus/lexicons.htm). |
| **ATUS via IPUMS (ATUS-X)** | [atusdata.org](https://www.atusdata.org/atus/) | Free (registration) | 2003–present | Individual-level; harmonized time-use variables | Custom extracts (CSV, Stata, etc.) | **HIGH** | Much easier interface than raw BLS files. Pre-built time-use variables. Can link to CPS demographic data. 431 detailed activity categories. Eating & Health Module adds grocery shopping detail. |
| **IPUMS Historical Time Use (AHTUS-X)** | [ahtusdata.org](https://www.ahtusdata.org/ahtus/) | Free (registration) | 1965–present (US samples from 1965, 1975, 1985, 1993, 1998, 2003+) | Individual-level; harmonized across decades | Custom extracts (Stata, SPSS, CSV) | **HIGH** | Can extend shopping/consumption time series back to 1965. Harmonized categories across different survey instruments. Part of Multinational Time Use Study (MTUS). |
| **Multinational Time Use Study (MTUS)** | [timeuse.org/mtus](https://www.timeuse.org/mtus) | Free (registration) | US: 1965, 1975, 1985, 1992–94, 1998, 2003+; 25+ countries | Harmonized 69-category scheme across countries/decades | Stata, SPSS | **HIGH** | "Shopping" is a harmonized category available 1965–present. No separate "research purchases" subcategory in harmonized scheme. Best source for cross-national, multi-decade shopping time series. Use for long-run trend; supplement with ATUS 0702xx codes for recent "research" detail. |
| **Pew Research Center** | [pewresearch.org](https://www.pewresearch.org/) | Free (reports) | Various | National surveys | Reports/PDF | **MEDIUM** | 90% of US adults daily internet users (2024); 41% "almost constantly" online. 76% buy online via smartphone. Useful for framing but not fine-grained time allocation. |

### 3.2 Digital Attention & Review Ecosystem

| Source | URL | Access | Years | Granularity | Format | Relevance | Notes |
|--------|-----|--------|-------|-------------|--------|-----------|-------|
| **Google Trends** | [trends.google.com](https://trends.google.com) | Free | 2004–present | Weekly/monthly; national/state/metro; by search term | CSV download; new API (alpha, limited access) | **HIGH** | Can construct indices for "[product] review", "best [product]", "[x] vs [y]" search volume over time. Relative scale (0-100) requires normalization. New alpha API available (announced July 2025) with daily/weekly/monthly aggregations — apply for access. Use [`pytrends`](https://github.com/GeneralMills/pytrends) Python library for programmatic extraction. |
| **BrightLocal Consumer Review Survey** | [brightlocal.com/research/local-consumer-review-survey/](https://www.brightlocal.com/research/local-consumer-review-survey/) | Free (reports) | ~2010–2026 (annual) | National consumer surveys (~1,100 respondents) | Reports/infographics | **HIGH** | Tracks review-reading behavior over time. Key trend data: "always/regularly" read reviews grew from ~22% (2010) → ~77% (2022) → 41% "always" (2026). Consumers using avg 6 review sites in 2026. ChatGPT for local recs: 6% → 45% in one year. |
| **Amazon Review Dataset (McAuley Lab, UCSD)** | [nijianmo.github.io/amazon/index.html](https://nijianmo.github.io/amazon/index.html) | Free (academic) | 1996–2018 | ~233 million reviews; by product category | JSON (gzipped) | **VERY HIGH** | Construct year-by-year review volume growth curves directly. Standard academic dataset for review research. Also available: [Stanford SNAP Amazon Reviews](https://snap.stanford.edu/data/web-Amazon.html) (~35M reviews to 2013). |
| **Yelp Open Dataset** | [yelp.com/dataset](https://www.yelp.com/dataset) | Free (academic use) | ~2004–present | ~7M reviews, 150K+ businesses | JSON | **HIGH** | Cumulative review growth: ~4.5M (2009) → 53M (2013) → 142M (2017) → 265M (2023). From [Yelp IR](https://www.yelp-ir.com/) earnings reports. |
| **TripAdvisor** | [ir.tripadvisor.com](https://ir.tripadvisor.com/) | Free (earnings reports) | ~2009–present | Cumulative review counts from IR | Reports | **MEDIUM** | Growth: ~25M (2009) → 200M (2014) → 660M (2018) → 1B+ (2022). Dramatic specification infrastructure growth. |
| **SimilarWeb** | [similarweb.com](https://www.similarweb.com) | **Paid** (limited free tier) | — | — | — | MEDIUM | Category-level traffic data on shopping/review sites. No free bulk download. |
| **Comscore** | [comscore.com](https://www.comscore.com) | **Paid** (academic consortium available) | ~2005+ | Time-on-site by category | Enterprise | MEDIUM | Apply for academic access at comscore.com/About/Academic-Consortium. Panels track time-on-site by category going back to mid-2000s. |
| **Statista** | [statista.com](https://www.statista.com) | **Paid** (some free charts) | Various | Curated statistics | Charts/tables | MEDIUM | Pre-purchase research behavior data (e.g., 86% of consumers use reviews before purchase, 2024). |

### 3.3 Craft/Artisan Market Data

| Source | URL | Access | Years | Granularity | Format | Relevance | Notes |
|--------|-----|--------|-------|-------------|--------|-----------|-------|
| **Brewers Association** | [brewersassociation.org/statistics-and-data/](https://www.brewersassociation.org/statistics-and-data/) | Free (some stats); Paid (detailed) | ~2005–present (some series back to ~1980 for brewery counts) | Annual; national + state; market share, volume, pricing | Online stats; reports for members | **HIGH** | Craft beer is the canonical "specification premium" example. **Key data point**: craft = ~13% of volume but ~25–27% of dollar sales → **~2x per-unit price premium** for specification. Free national/state stats, economic impact data, production data. Detailed data requires BA membership. |
| **American Craft Spirits Association** | [americancraftspirits.org](https://americancraftspirits.org/) | Free (press releases); Paid (full reports) | 2016–present (Craft Spirits Data Project) | Annual; national + state | Reports | **HIGH** | 3,069 active craft distillers (2024, +11.5%). Volume declining (12.7M cases, -6.1%) but still significant. $7.58B in sales. Market share 7.5% by value. Good "craft premium under pressure" story. |
| **DISCUS** | [distilledspirits.org](https://distilledspirits.org/) | Free (annual briefings) | Annual | National | Reports/press releases | **MEDIUM** | Total spirits market context. Annual economic briefings publicly available. |
| **Specialty Food Association** | [specialtyfood.com/state-of-the-industry-report/](https://www.specialtyfood.com/state-of-the-industry-report/) | **Paid** ($800–$2,000+) | 20+ years | Annual; 35 categories; retail/foodservice/online channels | Reports | **HIGH** | Specialty food sales ~$206B. 20 years of tracking data with 10-year forecasts in 35 categories. Expensive but comprehensive. Key press releases with top-line numbers are free. |
| **USDA Farmers Markets** | [ams.usda.gov/local-food-directories/farmersmarkets](https://www.ams.usda.gov/local-food-directories/farmersmarkets) | Free | 1994–present | Annual counts; by state; individual market listings | Directory (online); API | **HIGH** | Growth from 1,755 (1994) → 8,771 (2019). Growth slowing since 2011. $7B/year market. Download at [catalog.data.gov](https://catalog.data.gov/dataset/farmers-markets-directory-and-geographic-data). API: `search.ams.usda.gov/farmersmarkets/v1/data.svc/` |
| **USDA Local Food Marketing Practices Survey** | [nass.usda.gov](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Local_Food/) | Free | 2015, 2020 | Farm-level; by marketing channel | CSV via NASS QuickStats | **MEDIUM** | Farm-level data on direct-to-consumer sales. Direct sales carry inherent premium over wholesale commodity prices — quantifies the specification premium at farm level. |
| **Etsy (SEC filings)** | [sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1370637](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1370637) | Free | 2015–present (public since IPO) | Quarterly/annual; GMV, active sellers, active buyers | 10-K/10-Q filings (HTML/PDF) | **HIGH** | GMV: $5.0B (2019) → $13.5B (2021, COVID peak) → $12.6B (2024). Active sellers: 2.7M (2019) → 8.1M (2024). Proxy for handmade/curated goods demand. |
| **American Booksellers Association** | [bookweb.org/btw-topics/industry-statistics](https://www.bookweb.org/btw-topics/industry-statistics) | Free (some stats); membership for detail | 2009–present | Annual; national | Reports/press releases | **HIGH** | Indie bookstores: 1,401 (2009 low) → 3,218 (2024, +70% since 2020). 422 new openings in 2025 (+24%). Online sales up 580% since 2020. Trend toward niche concepts (157 romance-specific stores). |
| **Airbnb Experiences** | SEC filings | Free | 2016–present | Quarterly | 10-K/10-Q | **MEDIUM** | Limited breakout of "Experiences" segment vs. core lodging. |

### 3.4 Consumer Expenditure

| Source | URL | Access | Years | Granularity | Format | Relevance |
|--------|-----|--------|-------|-------------|--------|-----------|
| **BLS Consumer Expenditure Survey** | [bls.gov/cex/](https://www.bls.gov/cex/) | Free | 1984–present | Annual; national; by demographics, income quintiles | CSV, PDF | **MEDIUM** — categories are broad but can track food-away-from-home vs. food-at-home, entertainment, apparel vs. services, etc. |

---

## 4. Supplementary / Cross-cutting Data Inventory

### 4.1 Intangible Capital

| Source | URL | Access | Years | Countries | Format | Relevance | Notes |
|--------|-----|--------|-------|-----------|--------|-----------|-------|
| **EUKLEMS & INTANProd** | [euklems-intanprod-llee.luiss.it](https://euklems-intanprod-llee.luiss.it/) | Free | 1995–2021 (2025 release) | 27 EU + US + Japan + UK; 40 sectors | Excel, CSV, R (.rds), Stata (.dta) | **HIGH** | Includes **Industrial Design, Organizational Capital, Brand, and Training** as separate intangible investment categories — directly maps to specification vs. execution intangibles. Manufacturing detail (13 industries) + services breakdown. |
| **Global INTAN-Invest** | [global-intaninvest.luiss.it](https://global-intaninvest.luiss.it/) | Free | 1995–2024 (July 2025 release) | 32 economies (27 EU + Brazil, India, Japan, UK, US) | Online + downloadable | **HIGH** | Corrado-Hulten-Sichel framework. Annual + quarterly estimates. The CHS framework explicitly categorizes intangibles into three groups — this is **directly usable** for your thesis: |

**CHS Intangible Investment Categories (critical for your spec/exec distinction):**

| CHS Category | Sub-types | Your Classification |
|-------------|-----------|-------------------|
| **Computerized Information** | Software, databases | **EXECUTION intangibles** — tools for making/delivering |
| **Innovative Property** | R&D, mineral exploration, creative/entertainment originals, design | **MIXED** — design is specification; process R&D is execution |
| **Economic Competencies** | Brand equity/advertising, organizational capital/management consulting, market research/consumer insights, worker training | **SPECIFICATION intangibles** — deciding what to make, how to position it |

You can show that "economic competencies" (specification labor outputs) have grown as a share of total intangible investment over time. Conference Board has extended CHS series: [conference-board.org/topics/intangible-capital](https://www.conference-board.org/topics/intangible-capital) (may require membership for latest data).

### 4.2 R&D and Innovation

| Source | URL | Access | Years | Format | Relevance |
|--------|-----|--------|-------|--------|-----------|
| **NSF BERD Survey** (successor to SIRD→BRDIS) | [ncses.nsf.gov/surveys/business-enterprise-research-development/2023](https://ncses.nsf.gov/surveys/business-enterprise-research-development/2023) | Free (published tables); Restricted (microdata via FSRDC) | 1953–present (SIRD historical); 2008+ (BRDIS/BERD) | Tables (web/PDF); microdata (Stata) | **MEDIUM** — Primary source for business R&D spending. Can track R&D by industry. Difficult to split product vs. process R&D from published tables alone. |
| **USPTO PatentsView** | [patentsview.org/download/data-download-tables](https://patentsview.org/download/data-download-tables) | Free | 1976–present | MySQL dump, bulk download | **MEDIUM** — ~450 technology classes, ~150K subclasses. Classification is by technology field, not product/process. Would need custom classification to distinguish product from process patents. CPC (Cooperative Patent Classification) codes can help somewhat. |
| **USPTO Research Datasets** | [uspto.gov/ip-policy/economic-research/research-datasets](https://www.uspto.gov/ip-policy/economic-research/research-datasets) | Free | Various | Various | **MEDIUM** — Historical patent data files, inventor-level data, assignment data. |

### 4.3 Industry-Level Automation and Labor Share

| Source | URL | Access | Years | Coverage | Format | Relevance |
|--------|-----|--------|-------|----------|--------|-----------|
| **EU KLEMS** (via EUKLEMS & INTANProd) | See above | Free | 1995–2021 | 27 EU + US + Japan + UK; 40 sectors | Excel, CSV, R, Stata | **HIGH** — Industry-level labor compensation shares, capital stocks, employment by worker type. Can track labor share trends by industry and correlate with automation. |
| **Penn World Table 11.0** | [rug.nl/ggdc/productivity/pwt/](https://www.rug.nl/ggdc/productivity/pwt/) | Free | 1950–2019 (v11.0) | 183 countries | Excel, Stata, R, CSV; also on FRED | **MEDIUM** — Country-level labor share (multiple measures: comp_sh, lab_sh). Good for cross-country comparison but not industry-level. |
| **McKinsey Global AI Survey** | [mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) | Free (reports) | 2017–2025 (annual) | Global; by function/industry | Reports | **MEDIUM** — 78% of organizations using AI in ≥1 function (2025, up from 55% in 2023). IT/Marketing/Sales at 36% adoption. Useful for framing which industries are most execution-automated. |
| **Census Business Trends & Outlook Survey** | [census.gov](https://www.census.gov/) (also in EIG repo) | Free | 2023–present | National; by sector | Excel | **MEDIUM** — AI adoption at firm level: 3.7% (late 2023) → 6.6% (late 2024). More conservative than McKinsey (structured implementation vs. any use). |
| **Census Annual Business Survey (ABS) — Technology Module** | [census.gov/programs-surveys/abs.html](https://www.census.gov/programs-surveys/abs.html) | Free (published tables) | 2018–present | Annual; by NAICS 2-digit+; by firm size; by technology type (AI/ML, robotics, cloud) | Downloadable tables | **HIGH** — Best nationally representative data on AI adoption rates by industry. Can correlate with EU KLEMS labor shares to test whether specification-intensive labor holds up in most-automated industries. |
| **Brynjolfsson, Mitchell & Rock — SML Index** | Academic papers / replication files | Free (check authors' websites) | — | Occupation/task level | — | **MEDIUM** — "Suitability for Machine Learning" index scores occupations/tasks. Relevant for distinguishing spec tasks (low SML) from execution tasks (high SML). Search NBER working papers. |

---

## 5. Recommended Data Pipeline

### Pipeline A: Specification Wage Premium Time Series (Prediction 1)

**Step 1: Build the Classification**
1. Download O\*NET database (Excel format) from [onetcenter.org/database.html](https://www.onetcenter.org/database.html)
2. Extract `Work Activities` table — get importance scores for all 42 GWAs per occupation
3. Compute **Specification Intensity Index (SII)** per occupation = weighted average of spec-side GWA importance scores / total GWA importance scores (see Section 2.3 for which GWAs map to each side)
4. Rank occupations by SII. Top quintile = "specification-intensive"; bottom quintile = "execution-intensive"
5. Validate against intuition: do product managers, creative directors, UX researchers, VCs, art directors, executive chefs rank high? Do assembly workers, data entry, machine operators rank low?

**Step 2: Merge with Wages**
1. Download OEWS annual data (national, all occupations) from [bls.gov/oes/tables.htm](https://www.bls.gov/oes/tables.htm) for all available years (1997–2024)
2. Map O\*NET-SOC codes to OEWS SOC codes (crosswalk available in O\*NET supplemental files)
3. For each year, compute median wage of spec-intensive vs. execution-intensive occupation groups
4. Plot wage ratio (spec/exec) over time → this is your "specification wage premium" time series

**Step 3: Add AI Exposure Dimension**
1. Download Felten AIOE from [github.com/AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE) (`AIOE_DataAppendix.xlsx`, Appendix A)
2. Download Eloundou GPT exposure from [github.com/EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) (`gptsRgpts_occ_lvl.csv`)
3. Merge both onto your occupation-level dataset via SOC codes
4. Test: Among high-AI-exposure occupations, is the spec premium growing faster? Among low-AI-exposure occupations, is it stable?

**Step 4 (Advanced): Individual-Level Analysis**
1. Use IPUMS-CPS (ASEC) for regression analysis: log(wage) = f(SII, AI_exposure, SII×AI_exposure, controls)
2. Controls: education, experience, industry, year FEs
3. Test whether SII×year interaction is positive (spec premium widening over time)
4. Test whether SII×AI_exposure interaction is positive (spec premium wider in AI-exposed fields)

### Pipeline B: Consumption Research Effort Time Series (Prediction 2)

**Step 1: ATUS Shopping Time**
1. Register at [atusdata.org](https://www.atusdata.org/atus/) (IPUMS ATUS-X)
2. Extract time-use variables for activity codes 0701xx (Consumer Purchases/Shopping) for all years 2003–present
3. Compute annual average minutes/day spent on shopping/purchasing activities
4. Break out by subcategory (grocery shopping 070101 vs. other shopping 070104 vs. comparison shopping)
5. Plot trend over time

**Step 2: Google Trends Product Research Index**
1. Go to [trends.google.com](https://trends.google.com)
2. Search for terms: "best [product]", "[product] review", "[product] vs", "which [product] should I buy"
3. Download monthly time series (2004–present)
4. Construct composite "Product Research Search Index" — average across multiple product categories
5. Normalize and plot trend

**Step 3: Review Economy Growth**
1. Compile BrightLocal survey data (2014–2026) — percentage reading reviews, number of sites consulted, frequency
2. Add Etsy GMV/seller growth (SEC filings, 2015–2024) as proxy for curated goods demand
3. Add indie bookstore counts (ABA, 2009–2025)
4. Create composite "specification consumption" indicator

### Pipeline C: Craft Premium by Industry (Prediction 2)

1. **Beer**: Brewers Association craft vs. total market data → price premium per unit of craft vs. macro beer
2. **Spirits**: ACSA data → craft spirits price/case vs. total market price/case
3. **Food**: USDA farmers market growth + Specialty Food Association top-line numbers → specialty food share of total food retail
4. **Retail/Handmade**: Etsy GMV as share of total US e-commerce (Census e-commerce data available)
5. **Books**: Indie bookstore revenue vs. total book market (Association of American Publishers data)
6. Plot all five on one chart: "Craft/Specification Premium by Industry Over Time"

---

## 6. Gaps and Workarounds

### Suggested Composite "Consumer Specification Labor Index" (for Prediction 2)

Combine five series to build a compelling empirical case:

1. **Long-run shopping time** (MTUS/ATUS): total shopping hours, 1965–present — to show baseline
2. **Research-specific time** (ATUS code 0702): 2010–present — to show the research component is growing even if total shopping is flat
3. **Google Trends index**: basket of "[product] review" and "best [product]" queries, 2004–present — to show search-for-specification behavior growing
4. **Review volume curve**: cumulative reviews on Amazon (233M, 1996–2018) + Yelp (265M) + TripAdvisor (1B+) — to show the infrastructure for specification labor has exploded
5. **Survey evidence**: BrightLocal + Pew on % reading reviews — to show consumers report dramatically increased engagement

**The story**: total shopping time may be flat or declining, but the *research/specification component* is growing rapidly. This is consistent with a shift from "shopping as acquiring" to "shopping as specifying."

### Gap 1: No clean "consumer specification effort" measure
**Workaround**: Construct a composite index from:
- ATUS shopping time (07xxxx codes)
- Google Trends product research search volume
- BrightLocal review-reading frequency data
- Smartphone screen time on shopping apps (potentially from App Annie/Sensor Tower — paid)

### Gap 2: No dataset linking craft premiums to execution-automation levels
**Workaround**: Manually pair industries:
- Beer/spirits production is highly automated → compute craft price premium
- Book retailing is highly automated (Amazon) → compute indie bookstore price comparison
- Use EU KLEMS industry capital intensity or robot density (IFR data) as automation proxy, then correlate with craft segment market share

### Gap 3: Historical time-use data pre-2003 has different categories
**Workaround**: Use IPUMS AHTUS-X harmonized categories. The 1965/1975/1985 US surveys have shopping time but categories are broader. Focus on "purchasing goods and services" aggregate category which is available across decades.

### Gap 4: Lightcast/Burning Glass job postings data is proprietary
**Workaround**:
- Check if your institution has a Lightcast license
- Use the Mendeley-published subset (labor market concentration data, 2007Q1–2021Q2)
- Use OEWS for occupational employment trends instead (free, comprehensive)
- Check NBER/academic working papers that publish derived Lightcast datasets in their replication files

### Gap 5: Frey & Osborne automation probabilities not in clean downloadable format
**Workaround**: The 702-occupation automation probability table is in the paper's appendix. Several researchers have digitized it — check the EIG GitHub repo or search for "Frey Osborne automation probability CSV github."

### Gap 6: Consumer expenditure data too aggregated for spec/commodity split
**Workaround**: Use CE data at the highest available detail level. Focus on categories where spec/commodity distinction is clearest: food-at-home vs. food-away-from-home, apparel vs. services, entertainment subcategories. Supplement with industry-specific data (Brewers Association, SFA, etc.)

---

## 7. Quick Wins: Download and Analyze TODAY

### Quick Win 1: O\*NET Specification Index + OEWS Wages (2–3 hours)

**What to do:**
1. Download O\*NET v23.1 Excel database → extract `Work Activities` file
2. Download OEWS May 2024 national all-occupations file from [bls.gov/oes/tables.htm](https://www.bls.gov/oes/tables.htm)
3. Compute SII per occupation (ratio of spec-side to execution-side GWA importance scores)
4. Merge with wages via SOC code
5. Scatter plot: SII (x-axis) vs. median annual wage (y-axis) → do spec-intensive occupations pay more?
6. Repeat for 2017 and 2024 → is the slope steepening?

**Expected result**: Strong positive correlation between specification intensity and wages, potentially steepening over time.

### Quick Win 2: AI Exposure × Specification Interaction (1–2 hours)

**What to do:**
1. Use Quick Win 1 output (SII + wages by occupation)
2. Download Felten AIOE scores from [github.com/AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE)
3. Merge on SOC codes
4. Create 2×2: High-SII/Low-SII × High-AIOE/Low-AIOE
5. Compare wages across the four quadrants

**Expected result**: Highest wages in High-SII/High-AIOE (specification roles in AI-exposed fields). Lowest wages in Low-SII/High-AIOE (execution roles being automated). This would be a strong preliminary signal for your thesis.

### Quick Win 3: Craft Premium Trend Chart (1 hour)

**What to do:**
1. Pull Etsy GMV from SEC filings (2015–2024): $2.4B → $13.5B → $12.6B
2. Pull indie bookstore counts from ABA press releases (2009–2025): 1,401 → 3,218
3. Pull farmers market counts from USDA (1994–2019): 1,755 → 8,771
4. Pull craft beer market share from Brewers Association (free national stats)
5. Plot all four on one chart with indexed growth (base year = earliest available)

**Expected result**: Dramatic growth in specification-heavy market segments across multiple industries, even as execution (manufacturing, fulfillment) becomes more automated.

---

## 8. Key Source: Autor et al. (2024) "New Frontiers"

### Paper Details
- **Title**: "New Frontiers: The Origins and Content of New Work, 1940–2018"
- **Authors**: David H. Autor, Caroline Chin, Anna Salomons, Bryan Seegmiller
- **Published**: The Quarterly Journal of Economics 139(3): 1399–1465 (2024)
- **NBER WP**: [nber.org/papers/w30389](https://www.nber.org/papers/w30389)
- **Paper PDF**: [shapingwork.mit.edu](https://shapingwork.mit.edu/wp-content/uploads/2024/03/Autor_Chin_Salomons_Seegmiller_Dec-2023.pdf)

### Replication Data
- **Location**: [Harvard Dataverse DOI:10.7910/DVN/7RYD2E](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/7RYD2E)
- **Note**: Files are too large for direct Dataverse hosting — linked to SharePoint download
- **Released**: March 28, 2024

### Relevance to Your Thesis
This paper is **directly relevant** because it asks: what kinds of new work emerge in response to technological change? Key findings:
- New job titles emerge from **demand shocks** — technology creates new things people want
- New work is driven by technological progress that **replaces some jobs while complementing others**
- The creation of new occupations is fundamentally a **specification activity** — humans decide what new roles are needed
- Patent-linked new work tends to emerge in industries experiencing technological disruption
- This supports your claim that specification labor is irreducible: even as AI automates execution, the creation of new categories of work (deciding what new things to do) remains human

### Earlier Related Autor Datasets
| Dataset | Source | Notes |
|---------|--------|-------|
| Autor, Levy & Murnane (2003) task content | Available through paper replication files | Original task-content measures (routine vs. non-routine, cognitive vs. manual) — foundational taxonomy that your spec/exec distinction builds on |
| Autor & Dorn (2013) | David Dorn's website | Service occupation growth, job polarization data. Occupation crosswalks (occ1990dd) widely used — included in EIG repo |

---

## Appendix: All Download Links in One Place

### Free, Download Now
| Resource | Direct Link |
|----------|-------------|
| O\*NET Database v23.1 (Excel) | [onetcenter.org/database.html](https://www.onetcenter.org/database.html) |
| OEWS Annual Data (1997–2024) | [bls.gov/oes/tables.htm](https://www.bls.gov/oes/tables.htm) |
| Felten AIOE Index | [github.com/AIOE-Data/AIOE](https://github.com/AIOE-Data/AIOE) |
| EIG AI Unemployment Repo (Eloundou, Webb, Eisfeldt + CPS + crosswalks) | [github.com/EIG-Research/AI-unemployment](https://github.com/EIG-Research/AI-unemployment) |
| IPUMS-CPS (registration required) | [cps.ipums.org](https://cps.ipums.org/) |
| IPUMS-ATUS (registration required) | [atusdata.org](https://www.atusdata.org/atus/) |
| IPUMS Historical Time Use (registration required) | [ahtusdata.org](https://www.ahtusdata.org/ahtus/) |
| Census BDS (1978–2023) | [census.gov/programs-surveys/bds/data.html](https://www.census.gov/programs-surveys/bds/data.html) |
| USDA Farmers Market Directory | [catalog.data.gov](https://catalog.data.gov/dataset/farmers-markets-directory-and-geographic-data) |
| Autor et al. (2024) Replication Data | [doi.org/10.7910/DVN/7RYD2E](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/7RYD2E) |
| Penn World Table 11.0 | [rug.nl/ggdc/productivity/pwt/](https://www.rug.nl/ggdc/productivity/pwt/) |
| EUKLEMS & INTANProd (2025 release) | [euklems-intanprod-llee.luiss.it](https://euklems-intanprod-llee.luiss.it/) |
| Global INTAN-Invest | [global-intaninvest.luiss.it](https://global-intaninvest.luiss.it/) |
| USPTO PatentsView | [patentsview.org/download/data-download-tables](https://patentsview.org/download/data-download-tables) |
| NSF BERD Survey | [ncses.nsf.gov/surveys/business-enterprise-research-development/2023](https://ncses.nsf.gov/surveys/business-enterprise-research-development/2023) |
| Google Trends | [trends.google.com](https://trends.google.com) |
| BrightLocal Review Surveys | [brightlocal.com/research/](https://www.brightlocal.com/research/) |
| Amazon Review Dataset (McAuley/UCSD, 233M reviews) | [nijianmo.github.io/amazon/index.html](https://nijianmo.github.io/amazon/index.html) |
| Yelp Open Dataset (7M reviews) | [yelp.com/dataset](https://www.yelp.com/dataset) |
| MTUS (cross-national time use, 1965+) | [timeuse.org/mtus](https://www.timeuse.org/mtus) |
| Census ABS (AI adoption by industry) | [census.gov/programs-surveys/abs.html](https://www.census.gov/programs-surveys/abs.html) |
| pytrends (Google Trends Python library) | [github.com/GeneralMills/pytrends](https://github.com/GeneralMills/pytrends) |
| Etsy SEC Filings | [sec.gov (EDGAR, CIK 1370637)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1370637&type=10-K) |

### Paid / Restricted Access
| Resource | Access Type | Approximate Cost |
|----------|-------------|-----------------|
| Lightcast (Burning Glass) | Enterprise subscription | $10K–$100K+/year |
| Specialty Food Association Report | Purchase | $800–$2,000+ |
| SimilarWeb Pro | Subscription | $199+/month |
| Statista | Subscription | $199+/month |
| NSF BERD Microdata | FSRDC access | Institutional |

---

## 9. Deep-Dive: Census Bureau & BLS Sources for Specification Labor Research

### 9.1 American Community Survey (ACS) via IPUMS-USA

**Portal**: [usa.ipums.org](https://usa.ipums.org/usa/) (free, requires registration)

#### Why ACS over CPS?

The ACS is a ~3.5 million person/year survey (roughly 1% of the US population annually). The 5-year ACS pooled files represent a ~5% sample (15+ million people). By contrast, the CPS Annual Social and Economic Supplement (ASEC) surveys ~60,000–100,000 people. This means ACS can produce reliable estimates for **detailed (6-digit SOC equivalent) occupations at the metro area level**, which CPS cannot. For your research, this enables computing specification wage premiums for specific occupations within specific metro areas — critical for testing whether the premium varies by local labor market conditions.

#### Years Available

| Sample Type | Years | Notes |
|------------|-------|-------|
| ACS 1-year | 2000–2024 | Annual. Most recent (2024) released December 2025 via IPUMS. |
| ACS 5-year | 2005–2009 through 2018–2022 | Rolling 5-year pools. Larger samples for small-area estimates. |
| Decennial Census | 1850–2020 | Full enumeration (100% sample through 2000 long form). Via IPUMS. |
| Puerto Rico Community Survey (PRCS) | 2005–present | Parallel to ACS. |

#### Key Variables for Your Research

| Variable | Description | Available Years (ACS) | Notes |
|----------|-------------|----------------------|-------|
| **OCCSOC** | 6-digit alphanumeric SOC code | 2000–present | Uses 2000 SOC for 2000–2009, 2010 SOC for 2010–2017, 2018 SOC for 2018–onward. **This is your primary merge key to BLS OES data.** Some codes aggregated when cell sizes < 10,000. |
| **OCC** | 4-digit Census occupation code | 1950–present | Census-specific coding; use OCCSOC for SOC compatibility. |
| **OCC2010** | Harmonized occupation code (Census 2010 basis) | 1950–present | IPUMS-created harmonized code for longitudinal comparability across decades. Best for long-run analysis but loses some 6-digit detail. |
| **INCWAGE** | Wage and salary income (pre-tax, previous year) | 2000–present (ACS); 1940+ (census) | Total pre-tax wages, salaries, commissions, bonuses, tips. For ACS/PRCS, universe is persons age 16+. Top-coded at varying thresholds by year. |
| **INCBUS00** | Net self-employment income (business/farm) | 2000–present (ACS) | Net income from own business, professional practice, or farm after subtracting expenses. Can be negative (losses). |
| **INCBUS** | Non-farm business income | 1950–2000 (census) | Pre-2000 equivalent. Add INCFARM to get INCBUS00 equivalent. |
| **INCEARN** | Total earned income | 2000–present | INCEARN = INCWAGE + INCBUS00. Total labor earnings including self-employment. |
| **INCTOT** | Total personal income | 1950–present | All income sources combined. |
| **UHRSWORK** | Usual hours worked per week | 2000–present | 2-digit. Reports usual weekly hours if worked previous year. |
| **WKSWORK1** | Weeks worked last year (continuous) | 2008–present (ACS) | Exact number of weeks. For pre-2008 ACS and census, use WKSWORK2 (intervals). |
| **WKSWORK2** | Weeks worked last year (intervals) | 2000–present | Categorical: 1–13, 14–26, 27–39, 40–47, 48–49, 50–52. Available for all ACS years. |
| **CLASSWKR** | Class of worker | 1950–present | Key values: Self-employed (10), Wage/salary private (22–23), Government (24–28). From 1988+, self-employed distinguishes incorporated (14) vs. unincorporated (13). **Use this as your self-employment flag.** |
| **CLASSWKRD** | Class of worker (detailed) | 1950–present | Detailed version. Codes: 13 = self-employed, not incorporated; 14 = self-employed, incorporated; 22 = private for-profit wage/salary; 23 = private not-for-profit wage/salary; 25–28 = federal/state/local government. |
| **EDUC** | Educational attainment | 1850–present | Highest year of school or degree completed. Harmonized across all census/ACS years. |
| **DEGFIELD** | Field of bachelor's degree | 2009–present (ACS only) | Detailed field-of-study codes. Only for those with bachelor's or higher. |
| **DEGFIELD2** | Second field of bachelor's degree | 2009–present (ACS only) | For double majors. |
| **AGE** | Age | All years | — |
| **IND** | Industry code | 1850–present | Census industry codes. From 2013 ACS+, based on 2012 NAICS. |
| **INDNAICS** | NAICS industry code (string) | 2000–present | Direct NAICS codes. Can map to BDS/ABS NAICS sectors. |
| **MET2013** | Metropolitan area (2013 OMB delineation) | 2005–present | Identifies Core-Based Statistical Areas (CBSAs). ~380 metro areas identified. **Use this for metro-level analysis.** |
| **METAREA** | Metropolitan area (historical) | 1850–present | Older metro definitions, less consistent across years. Prefer MET2013. |
| **PUMA** | Public Use Microdata Area | 2000–present | Smallest geography in ACS microdata. Minimum 100,000 population. ~2,400 PUMAs nationally. Can approximate metro areas and sub-metro regions. |
| **PERWT** | Person weight | All years | **Must use this** for weighted tabulations to get population-representative estimates. |

#### OCC-to-SOC Crosswalk

IPUMS provides a direct crosswalk between OCC (Census codes) and OCCSOC (SOC codes) for 2000+ samples, downloadable at [usa.ipums.org/usa/volii/occtooccsoc18.shtml](https://usa.ipums.org/usa/volii/occtooccsoc18.shtml). Note that some Census OCC codes map to aggregated SOC codes (e.g., "15-1250" instead of "15-1251" and "15-1252" separately) when the Census collapsed categories for confidentiality. For merging with BLS OES, you may need to aggregate OES occupations to match the ACS level of detail.

#### Constructing Hourly Wages from ACS

ACS does not directly report hourly wages. Construct an approximation:
```
hourly_wage_approx = INCWAGE / (UHRSWORK * WKSWORK1)
```
Filter to full-time, full-year workers (UHRSWORK >= 35, WKSWORK1 >= 50) for cleaner estimates. Use WKSWORK2 midpoints if WKSWORK1 is not available.

#### How to Extract Data

1. Register at [usa.ipums.org](https://usa.ipums.org/usa/)
2. Select samples (e.g., ACS 2005–2024 annual)
3. Select variables (OCCSOC, INCWAGE, INCBUS00, UHRSWORK, WKSWORK1, CLASSWKR, EDUC, AGE, IND, MET2013, PERWT, YEAR)
4. Submit extract; download as CSV, Stata, SAS, or SPSS
5. Typical extract for all ACS years with these variables: ~50–100 GB uncompressed

---

### 9.2 Census Business Dynamics Statistics (BDS)

**Data home**: [census.gov/programs-surveys/bds/data.html](https://www.census.gov/programs-surveys/bds/data.html)
**Datasets page**: [census.gov/data/datasets/time-series/econ/bds/bds-datasets.html](https://www.census.gov/data/datasets/time-series/econ/bds/bds-datasets.html)
**API**: [api.census.gov/data/timeseries/bds](https://api.census.gov/data/timeseries/bds)
**Explorer tool**: [bds.explorer.ces.census.gov](https://bds.explorer.ces.census.gov)
**Codebook/Glossary PDF**: [census.gov/content/dam/Census/programs-surveys/business-dynamics-statistics/codebook-glossary.pdf](https://www.census.gov/content/dam/Census/programs-surveys/business-dynamics-statistics/codebook-glossary.pdf)

#### Years: 1978–2023 (annual time series)

#### Key Variables (from BDS Codebook)

| Variable | Description | Relevance |
|----------|-------------|-----------|
| **firms** | Count of firms | Denominator for entry/exit rates |
| **estabs** | Count of establishments | Firms can have multiple establishments |
| **emp** | Employment (March 12 payroll) | Total jobs |
| **denom** | Average employment (used as denominator for rates) | Davis-Haltiwanger-Schuh denominator = average of t and t-1 employment |
| **estabs_entry** | Count of establishment entrants (births) | New establishments opened in year t |
| **estabs_entry_rate** | Establishment entry rate | estabs_entry / denom_estabs |
| **estabs_exit** | Count of establishment exits (deaths) | Establishments closed in year t |
| **estabs_exit_rate** | Establishment exit rate | estabs_exit / denom_estabs |
| **firmdeath_firms** | Count of firm deaths | Firms that cease operations entirely |
| **firmdeath_estabs** | Establishments lost to firm deaths | Establishments closing because their parent firm died |
| **firmdeath_emp** | Employment lost to firm deaths | Jobs lost from firm closures |
| **job_creation** | Gross job creation | Sum of employment gains from expanding + entering establishments |
| **job_creation_births** | Job creation from establishment births | Jobs at brand-new establishments |
| **job_creation_continuers** | Job creation from continuing establishments | Jobs added by existing, expanding establishments |
| **job_creation_rate** | Job creation rate | job_creation / denom |
| **job_destruction** | Gross job destruction | Sum of employment losses from contracting + exiting establishments |
| **job_destruction_deaths** | Job destruction from establishment deaths | Jobs lost from closing establishments |
| **job_destruction_continuers** | Job destruction from continuing establishments | Jobs lost by existing, contracting establishments |
| **job_destruction_rate** | Job destruction rate | job_destruction / denom |
| **net_job_creation** | Net job creation | job_creation - job_destruction |
| **net_job_creation_rate** | Net job creation rate | net_job_creation / denom |
| **reallocation_rate** | Job reallocation rate | job_creation_rate + job_destruction_rate |

#### Dimensional Breakdowns Available

| Dimension | Abbreviation in Filename | Values |
|-----------|--------------------------|--------|
| Economy-wide | `ec` | National aggregate |
| State | `st` | 50 states + DC |
| Metro (MSA) | `met` or `msa` | ~380 metro areas |
| NAICS Sector | `sec` | 2-digit NAICS (20 sectors) |
| Firm Age | `fa` or `fac` | Detailed (0,1,2,...,26+) or Coarse (0-1, 2-3, 4-5, 6-10, 11+) |
| Firm Size | `fz` or `ifzc` | By current employment or initial firm size (coarse) |
| Establishment Age | `ea` or `eac` | Establishment-level age categories |
| Establishment Size | `isz` or `iszc` | By employment |

#### CSV Download URLs

Base URL: `https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/`

Key files for your research (filename pattern: `bds2023_[dimensions].csv`):

| File | Dimensions | Use Case |
|------|-----------|----------|
| `bds2023_ec.csv` | Economy-wide | National time series of firm entry/exit, 1978–2023 |
| `bds2023_sec.csv` | By NAICS sector | **Core file**: firm births/deaths by industry sector |
| `bds2023_sec_fa.csv` | Sector x Firm Age | New firm survival by industry |
| `bds2023_sec_fac_ifzc.csv` | Sector x Firm Age (coarse) x Initial Size (coarse) | Startup dynamics by industry |
| `bds2023_st.csv` | By state | Geographic variation in entrepreneurship |
| `bds2023_met.csv` or `bds2023_msa.csv` | By MSA | Metro-level firm dynamics |
| `bds2023_met_sec_fz.csv` | Metro x Sector x Firm Size | Metro-industry-level detail |
| `bds2023_st_met_sec_fa.csv` | State x Metro x Sector x Firm Age | Most granular geographic-industry file |

**For your specification-entrepreneurship hypothesis**, the key files are:
1. **`bds2023_sec.csv`** — Track firm entry rates over time by 2-digit NAICS sector. Compare entry rates in specification-intensive sectors (NAICS 54: Professional/Scientific/Technical, NAICS 62: Healthcare, NAICS 71: Arts/Entertainment, NAICS 72: Accommodation/Food Services) vs. execution-intensive sectors (NAICS 31-33: Manufacturing, NAICS 48-49: Transportation/Warehousing).
2. **`bds2023_sec_fa.csv`** — Track survival rates of young firms (age 0–5) by sector.
3. **`bds2023_ec.csv`** — National time series for aggregate firm entry rate trends.

#### API Example

```
https://api.census.gov/data/timeseries/bds?get=firms,estabs,emp,estabs_entry,estabs_entry_rate,firmdeath_firms,job_creation,job_creation_rate&for=us:*&NAICS=54&YEAR=2023&key=YOUR_API_KEY
```

Variables list: [api.census.gov/data/timeseries/bds/variables.html](https://api.census.gov/data/timeseries/bds/variables.html)
Examples: [api.census.gov/data/timeseries/bds/examples.html](https://api.census.gov/data/timeseries/bds/examples.html)

---

### 9.3 Census Annual Business Survey (ABS) — Technology Module

**About**: [census.gov/programs-surveys/abs/about.html](https://www.census.gov/programs-surveys/abs/about.html)
**Data tables**: [census.gov/programs-surveys/abs/data/tables.html](https://www.census.gov/programs-surveys/abs/data/tables.html)
**API portal**: [census.gov/data/developers/data-sets/abs.html](https://www.census.gov/data/developers/data-sets/abs.html)
**Technical docs**: [census.gov/programs-surveys/abs/technical-documentation.html](https://www.census.gov/programs-surveys/abs/technical-documentation.html)

#### Survey Overview

The ABS is conducted by the Census Bureau in partnership with NSF's National Center for Science and Engineering Statistics (NCSES). It surveys a nationally representative sample of employer businesses. Sample sizes vary: ~850,000 firms (2018), ~300,000 firms (2019+). Results are tabulated by NAICS sector (2-digit), firm size, demographics, geography.

#### Technology Questions by Year

| Year | API Endpoint | Technologies Covered | Sample Size | Notes |
|------|-------------|---------------------|-------------|-------|
| **2018** | `abstcb` | AI (6 subtypes), Cloud services, Augmented reality, Automated storage/retrieval, RFID, Robotics, Touchscreens/kiosks | ~850K firms | First technology module. Variables at `api.census.gov/data/2018/abstcb/variables.html` |
| **2019** | `abstcb` | **AI** (automated guided vehicles, machine learning, machine vision, natural language processing, voice recognition), **Cloud**, **Robotics**, **Specialized Software**, **Specialized Equipment** | ~300K firms | Most detailed AI subtype breakdown. Tables at [census.gov/data/tables/2019/econ/abs/2019-abs-automation-technology-module.html](https://www.census.gov/data/tables/2019/econ/abs/2019-abs-automation-technology-module.html) |
| **2020** | `absmcb` | AI, Cloud, Computer infrastructure, Automation, IoT devices, Mobile communication, Digital collaboration | ~300K firms | Shifted categories slightly. Added COVID impact questions. |
| **2021** | `absmcb` | Module Business Characteristics: technology types, financing, pandemic effects | ~300K firms | Tables at [census.gov/data/tables/2021/econ/abs/2021-abs-mcb.html](https://www.census.gov/data/tables/2021/econ/abs/2021-abs-mcb.html) |
| **2022** | `abscb` or `abscs` | Characteristics of Businesses including technology use | ~300K firms | Variables at `api.census.gov/data/2022/abscs/variables.html` |
| **2023** | (2024 release) | Reference year 2023 data; includes R&D, manufacturing, management practices, financing | ~300K firms | Most recent. API documentation at [census.gov/programs-surveys/abs/technical-documentation/api/2023.html](https://www.census.gov/programs-surveys/abs/technical-documentation/api/2023.html) |

#### AI Adoption Rates by NAICS Sector (from 2018 ABS)

| NAICS Sector | Current AI Use | Expected Future AI Use |
|-------------|---------------|----------------------|
| 51 — Information | Highest | Highest |
| 54 — Professional, Scientific, Technical | High | High |
| 52 — Finance and Insurance | High | High |
| 62 — Healthcare and Social Assistance | Moderate-High | High (medical/diagnostic labs ~23%) |
| 31-33 — Manufacturing | Moderate | Moderate |
| 23 — Construction | Lowest | Lowest |
| 11 — Agriculture | Lowest | Low |

**Overall**: ~6% of firms reported AI use in 2018. Large firms (5,000+ employees) had much higher adoption. Software publishing (~16%), computer systems design (~14%), data processing (~14%), and medical/diagnostic labs (~23%) had the highest rates at detailed industry level.

#### Key AI Subtypes Tracked (2019 ABS)

- Automated guided vehicles (AGVs)
- Machine learning
- Machine vision
- Natural language processing (NLP)
- Voice recognition

#### Is ABS the Best Source for "Which Industries Are Automating Execution Fastest"?

**Yes, for firm-level adoption.** The ABS is the most comprehensive nationally representative survey of technology adoption by US businesses. It provides adoption rates by 2-digit NAICS sector, firm size, and geography. For your research question, compare AI/automation adoption rates across NAICS sectors, then cross-reference with your specification intensity classification of those sectors. Industries with high automation adoption AND growing specification-labor shares would be strong evidence for your thesis.

**Complement with**: Census Business Trends and Outlook Survey (BTOS) for more recent/frequent data (quarterly, 2023–present; shows AI adoption rising from 3.7% to 6.6% of firms over one year). Also McKinsey Global AI Survey for qualitative/functional breakdown.

#### API Example (2018 Technology Module)

```
https://api.census.gov/data/2018/abstcb?get=GEO_ID,NAME,NAICS2017,NAICS2017_LABEL,FACTORS_P&for=us:*&key=YOUR_API_KEY
```

Full variable list: `https://api.census.gov/data/2018/abstcb/variables.html`
Technical PDF: [census.gov ABS API TCB documentation](https://www2.census.gov/programs-surveys/abs/technical-documentation/api/ABS_API_TCB-2-9-2021.pdf)

**Key academic papers using ABS technology data:**
- McElheran, Kristina, et al. "AI Adoption in America: Who, What, and Where" (2024). Census Working Paper CES-WP-23-48. [PDF](https://www2.census.gov/ces/wp/2023/CES-WP-23-48.pdf)
- Zolas, Nikolas, et al. "Advanced Technologies Adoption and Use by U.S. Firms: Evidence from the Annual Business Survey" (2021). NBER WP 28290. [PDF](https://www.nber.org/system/files/working_papers/w28290/w28290.pdf)
- Dinlersoz, Emin. "Tracking Firm Use of AI in Real Time" (2024). Census Working Paper CES-WP-24-16. [PDF](https://www.census.gov/hfp/btos/downloads/CES-WP-24-16.pdf)

---

### 9.4 BLS Consumer Expenditure Survey (CE/CEX)

**Home**: [bls.gov/cex/](https://www.bls.gov/cex/)
**PUMD download**: [bls.gov/cex/pumd_data.htm](https://www.bls.gov/cex/pumd_data.htm)
**PUMD documentation**: [bls.gov/cex/pumd_doc.htm](https://www.bls.gov/cex/pumd_doc.htm)
**Published tables**: [bls.gov/cex/tables.htm](https://www.bls.gov/cex/tables.htm)
**Getting started guide**: [bls.gov/cex/pumd-getting-started-guide.htm](https://www.bls.gov/cex/pumd-getting-started-guide.htm)
**Novice guide (PDF)**: [bls.gov/cex/pumd_novice_guide.pdf](https://www.bls.gov/cex/pumd_novice_guide.pdf)

#### Years Available

| Data Type | Years | Notes |
|-----------|-------|-------|
| Public-use microdata (PUMD) | **1980–2024** | Not available for 1982–1983. Hierarchical groupings only from 1996+. |
| Published tables | 1984–present | Annual averages and detailed breakdowns. |

#### Data Format and Structure

**Two surveys, one program:**
- **Interview Survey**: Covers ~95% of expenditures. Major and recurring items (housing, vehicles, insurance, healthcare, education, etc.). Quarterly interviews over 5 quarters per consumer unit.
- **Diary Survey**: Covers frequently purchased items (food, beverages, tobacco, personal care, nonprescription drugs, household supplies). 2-week diaries.

**File formats**: SAS (.sas7bdat), Stata (.dta), CSV (comma-delimited). SPSS no longer supported.

**Public-use microdata**: YES. Full microdata files are freely downloadable. Each annual package contains Interview and Diary files.

**Key PUMD files within each annual package:**
- **FMLI** — Consumer Unit (family) characteristics and summary expenditure variables
- **MTBI** — Monthly expenditure detail by UCC (Universal Classification Code)
- **MEMI** — Member-level characteristics
- **ITBI** / **DTBI** — Item-level detail for Interview / Diary

#### The 14 Major Expenditure Categories

| Category | 2024 Share of Spending | Specification-Relevance |
|----------|----------------------|------------------------|
| **Housing** | 33.4% | Moderate — rental vs. owned, location choices |
| **Transportation** | 17.0% | Low — mostly commodity |
| **Food** | 12.9% | **HIGH** — food-away-from-home vs. food-at-home is a key spec proxy |
| **Personal Insurance & Pensions** | 12.5% | Low |
| **Healthcare** | 7.9% | Moderate — elective/specialty care |
| **Entertainment** | 4.6% | **HIGH** — subcategories distinguish spec-heavy from commodity |
| **Cash Contributions** | 2.9% | Low |
| **Apparel & Services** | 2.5% | Moderate — commodity vs. designer/custom |
| **Education** | 2.0% | Moderate |
| **Miscellaneous** | 1.6% | — |
| **Personal Care** | 1.2% | Moderate — commodity vs. specialty products |
| **Alcoholic Beverages** | 0.8% | **HIGH** — craft vs. commodity (pair with Brewers Assoc. data) |
| **Tobacco** | 0.4% | Low |
| **Reading** | 0.2% | Moderate — indie bookstores vs. mass market |

#### Universal Classification Codes (UCCs) — The Expenditure Taxonomy

UCCs are 6-digit codes that classify expenditures at the most detailed level. They are organized in a **hierarchical grouping** system.

**Hierarchical grouping files** (available for 1996+) come in three types:
- **CE-HG-Integ-[YEAR]** — Integrated groupings (both surveys combined; used for published tables)
- **CE-HG-Inter-[YEAR]** — Interview survey UCCs only
- **CE-HG-Diary-[YEAR]** — Diary survey UCCs only

Download from: [bls.gov/cex/pumd_doc.htm](https://www.bls.gov/cex/pumd_doc.htm)

#### Key UCCs for Specification-vs-Commodity Analysis

**Food at Home vs. Food Away from Home:**

| UCC / Category | Description | Survey | Spec/Commodity |
|---------------|-------------|--------|---------------|
| **FOODHOME** (aggregate) | Food at home | Diary + Interview | More commodity (groceries) |
| UCC 790210 | All grocery purchases, including nonfood | Interview | Commodity baseline |
| UCC 790240 | Food purchases at grocery stores | Interview | Ended Q1 2023; replaced by 790210 |
| **FOODAWAY** (aggregate) | Food away from home | Interview | **Specification-heavy** |
| FOODAWYPQ / FOODAWYCQ | Food away from home summary variables | Interview | Created 2024 Q2+ |
| 190901 | Food/drink at employer/school cafeterias | Interview | Mixed |
| 190902 | Food on trips | Interview | Specification (curated experience) |
| 190903 | School lunches | Interview | Commodity |
| 190904 | Meals as pay | Interview | — |
| 790310–790340 | Meals at restaurants (breakfast, lunch, dinner, snacks) | Interview | Specification |

**Food away from home** includes: all meals (breakfast/brunch, lunch, dinner, snacks, nonalcoholic beverages) including tips at fast food, take-out, delivery, concession stands, buffets/cafeterias, full-service restaurants, vending machines, and mobile vendors. Also includes board, meals as pay, catered affairs (weddings, bar mitzvahs), school lunches, and meals on trips.

**Entertainment Subcategories:**

| Subcategory | Examples | Spec/Commodity |
|------------|---------|---------------|
| Fees and admissions | Movies, theater, concerts, sports events, clubs, recreation lessons | **HIGH specification** — choosing experiences |
| Audio and visual equipment | TVs, DVDs, streaming devices, speakers, video games | Mixed (hardware = commodity; content = spec) |
| Pets, toys, hobbies, playground equipment | Hobbies, crafts, specialty toys | **Moderate specification** |
| Other entertainment | Photography, recreation vehicles, boats, musical instruments | Mixed |

In 2024 data: TV/radios/sound equipment ~33% of entertainment spending; fees/admissions ~30%.

**Alcoholic Beverages:**

| Subcategory | Spec/Commodity |
|------------|---------------|
| Beer and ale at home | Can pair with Brewers Assoc. craft share data |
| Wine at home | Specification-heavy (varietal, region, vintage) |
| Spirits at home | Can pair with ACSA craft spirits data |
| Alcoholic beverages away from home | **HIGH specification** (cocktail bars, craft beer bars, wine bars) |

**Other Specification-Relevant Categories:**

| Category | UCCs/Subcategories | Why |
|----------|-------------------|-----|
| Apparel: Services | Tailoring, alterations, clothing rental, watch/jewelry repair | Custom/craft vs. commodity |
| Personal care: Services | Haircuts, salons, spas | Specification-heavy (choosing stylist/treatment) |
| Housing: Household operations | Babysitting, day care, moving, household services | Specification of service provider |
| Education | Tuition, books, supplies | Increasingly differentiated (online vs. in-person, specialty programs) |

#### Tracking Specification Consumption Over Time

**Concrete analysis with CEX data:**

1. **Food-away-from-home share of total food** — Track FOODAWAY / (FOODAWAY + FOODHOME) annually, 1984–2024. Rising share = more specification (choosing restaurants, cuisines, experiences vs. buying commoditized groceries).

2. **Entertainment fees/admissions share** — Track "fees and admissions" as share of total entertainment spending. Rising share = more experiential/curated consumption.

3. **Alcoholic beverages away-from-home share** — Track away-from-home alcohol as share of total alcohol spending. Rising share = more specification (choosing craft bars, cocktail experiences).

4. **Services share of total spending** — Track total service expenditures vs. goods expenditures. Services are inherently more specification-heavy.

#### Published Tables (No Microdata Required)

Published tables at [bls.gov/cex/tables.htm](https://www.bls.gov/cex/tables.htm) provide pre-computed breakdowns by:
- Income quintile and decile
- Age of reference person
- Region and population size class
- Race and Hispanic origin
- Consumer unit composition
- Education of reference person
- Number of earners
- Occupation of reference person

The **"Occupation of reference person"** tables are directly useful — compare spending patterns of specification-intensive occupations vs. execution-intensive occupations.

#### R Package for CEX Analysis

The `cepumd` R package ([CRAN](https://cran.r-project.org/web/packages/cepumd/cepumd.pdf)) provides functions to calculate CE weighted estimates from PUMD, handle the hierarchical grouping files, and aggregate UCCs.

---

### 9.5 Cross-Source Integration Strategy

#### Linking Keys Across Sources

| Source A | Source B | Link Variable | Notes |
|----------|----------|--------------|-------|
| ACS (IPUMS) | BLS OES | OCCSOC ↔ SOC code | Direct merge at 6-digit SOC. Some ACS codes aggregated. |
| ACS (IPUMS) | O*NET | OCCSOC ↔ O*NET-SOC | O*NET uses hybrid SOC codes. Crosswalk at onetcenter.org. |
| ACS (IPUMS) | BDS | INDNAICS ↔ NAICS sector | ACS has individual-level NAICS; BDS has 2-digit sector aggregates. |
| ACS (IPUMS) | ABS | INDNAICS ↔ NAICS sector | Same NAICS mapping. |
| BDS | ABS | NAICS sector | Both use 2-digit NAICS. Direct merge on sector + year. |
| CEX | ACS | Occupation of reference person | Broad occupation categories only (not 6-digit SOC). |
| BDS | BLS OES | NAICS sector ↔ NAICS (industry employment) | OES also publishes by NAICS industry. |

#### Recommended Analysis Combining All Four Sources

**Test: "Specification-intensive industries show higher firm entry rates as AI automates execution"**

1. From **ABS**: Identify NAICS sectors with highest AI/automation adoption rates (2018–2023)
2. From **BDS**: Get firm entry rates, firm birth counts, and new-firm job creation by NAICS sector over time (1978–2023)
3. From **ACS**: Compute average specification intensity (using O*NET SII merged via OCCSOC) of workers in each NAICS sector
4. From **CEX**: Track whether consumer spending is shifting toward sectors with high specification intensity

**Expected finding**: Sectors with the highest AI adoption (Information, Professional Services) also show the highest firm entry rates for new specification-intensive businesses, while sectors with low AI adoption show stable or declining entry rates.
