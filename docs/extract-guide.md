# Extract Guide: What to Pull from IPUMS, Census & BLS/CEX

---

## 1. IPUMS-CPS: Individual-Level Wage Regressions

### Why CPS on top of OES?

OES gives you occupation-level **medians/means** — great for descriptive charts but you can't control for confounders. CPS gives you **individual-level microdata** so you can run:

```
log(wage_i) = β₁·SpecIndex_occ + β₂·AI_Exposure_occ + β₃·(Spec×AI) + γ·X_i + δ_t + ε_i
```

where X_i = education, age, experience, race, sex, industry, metro, union status. This is the publishable regression you need.

**Other CPS advantages over OES:**
- Wage **distributions** (not just means/medians) — you can measure within-occupation inequality
- **Self-employment** flag — spec-intensive workers may increasingly be self-employed
- **Individual demographics** — test whether spec premium varies by education, race, gender
- CPS monthly rotation means some individuals appear in multiple months (short panel)
- Goes back to **1982** for earnings (vs. 1997 for OES)

### ASEC vs. Outgoing Rotation Group (ORG): Use ORG for Wages

CPS has **two distinct wage measurement systems** — this matters:

| Feature | ASEC (March supplement) | ORG (monthly, rotation groups 4 & 8) |
|---------|------------------------|--------------------------------------|
| Wage measure | **INCWAGE** (recalled annual earnings, prior year) | **EARNWEEK** / **HOURWAGE** (current job, usual earnings) |
| Sample/year | ~60K–100K persons | ~180K–220K earners (pooling 12 months) |
| Recall bias | High (full prior year) | Low (current job) |
| Top-coding | Varies by year | $2,885/week (1998+) |
| Self-employed | Included | Excluded (wage workers only) |
| Weight | ASECWT | EARNWT (÷12 when pooling months) |

**The ORG is likely superior for your wage analysis** because:
- Measures **current** wages (not recalled annual earnings)
- 3x the ASEC sample when pooling 12 months
- Gives `HOURWAGE` directly for hourly workers
- EPI and most labor economists use ORG for wage distribution analysis
- Ref: [EPI ORG methodology](https://microdata.epi.org/methodology/wagevariables/)

**Use ASEC for**: self-employment analysis (ORG excludes self-employed), annual income (INCWAGE), and linking to INCBUS00 (business income).

### IPUMS-CPS Extract: Variables to Select

Go to [cps.ipums.org](https://cps.ipums.org/), create account, start new extract.

**Sample selection:**
- **For ORG analysis**: Select all Basic Monthly samples 2003–2025 (or 2000–2025 for deeper history)
- **For ASEC analysis**: Select ASEC samples for same years
- Post-2002 gives consistent occupation coding; pre-2003 requires crosswalk

#### Core Variables

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **YEAR** | Survey year | Time dimension |
| **ASECWT** | ASEC person weight | Required for nationally representative estimates |
| **EARNWT** | Earner weight (for ORG) | If using outgoing rotation group earnings |

#### Occupation & Industry

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **OCC** | Detailed occupation (original Census codes) | Raw occupation code |
| **OCC2010** | Harmonized occupation (2010 Census scheme) | **Key variable** — harmonized 1968–present (~540 categories). Use this for longitudinal analysis. Maps approximately to SOC. |
| **OCC1990** | Harmonized occupation (1990 basis) | Alternative harmonization; matches David Dorn's crosswalk (occ1990dd) used in the EIG repo |
| **OCCSOC** | SOC code (string, 6-digit) | Direct SOC mapping for 2000+ — **this is what merges to O\*NET and OES**. Available 2003+. Use for post-2003 analysis. |
| **IND** | Detailed industry (original codes) | Raw industry |
| **IND1990** | Harmonized industry (1990 basis) | Longitudinal industry comparison |

#### Earnings/Wages — ASEC

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **INCWAGE** | Annual wage & salary income (prior year) | Primary annual wage measure. Available 1962+. |
| **UHRSWORKLY** | Usual hours worked per week (last year) | Compute hourly wage = INCWAGE / (UHRSWORKLY × WKSWORK1) |
| **WKSWORK1** | Weeks worked last year (continuous) | For annual-to-hourly conversion. 1976+. |
| **WKSWORK2** | Weeks worked last year (intervals) | Fallback if WKSWORK1 unavailable. 1962+. |
| **CLASSWLY** | Class of worker (last year) | Self-employment flag for annual earnings |
| **FULLPART** | Full/part-time status (last year) | Filter to full-time |

#### Earnings/Wages — ORG (Preferred for Wage Analysis)

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **EARNWEEK** | Usual weekly earnings (current job) | Primary ORG wage measure. Top-coded $2,885 (1998+). |
| **HOURWAGE** | Hourly wage (if paid hourly) | Direct hourly rate. 1979+. |
| **HOURWAGE2** | Hourly wage (consistent rounding/topcodes) | Cleaner version. |
| **PAIDHOUR** | Paid by the hour? | Flag for which wage measure to use |
| **UHRSWORKORG** | Usual hours at current job | For non-hourly: hourly_wage = EARNWEEK / UHRSWORKORG |
| **ELIGORG** | Eligible for ORG (rotation groups 4 & 8) | Filter to ORG-eligible respondents |

#### Panel Linking Variables

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **CPSIDP** | Person-level identifier | Link same individual across months. CPS 4-8-4 rotation = observe same person up to 8 months over 16 months. |
| **CPSID** | Household identifier | Household-level linking |
| **MISH** | Month-in-sample (1–8) | Identify rotation position. ORG = MISH 4 or 8. Same person in MISH 4 and MISH 8 gives earnings 12 months apart. |

#### Demographics (Controls)

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **AGE** | Age | Experience proxy |
| **SEX** | Sex | Control |
| **RACE** | Race | Control |
| **HISPAN** | Hispanic origin | Control |
| **EDUC** | Education (general) | Control; also test if spec premium varies by education |
| **EDUC99** | Education (detailed, 1990+ consistent) | More detailed education categories |
| **SCHLCOLL** | School/college attendance | Student status |

#### Employment Characteristics

| Variable | Description | Why You Need It |
|----------|-------------|-----------------|
| **EMPSTAT** | Employment status | Filter to employed |
| **CLASSWKR** | Class of worker | Distinguish **self-employed** (values 13-14) from wage workers. Spec workers may increasingly be self-employed/freelance. |
| **WKSTAT** | Full/part-time status | Control |
| **UNION** | Union membership | Control; test if spec premium differs for union workers |
| **FIRMSIZE** | Firm size | Test if spec premium varies by firm size |
| **STATEFIP** | State FIPS code | Geographic controls |
| **METRO** | Metro/non-metro | Geographic controls |
| **METAREA** | Metropolitan area | More granular geography |

#### Output Settings
- Format: **Stata (.dta)** or **CSV**
- Case selection: AGE 16–65, EMPSTAT = employed
- Select all target years

### How to Merge CPS with O\*NET

1. Use **OCCSOC** (available 2003+) → merge directly to O\*NET SOC codes and your Specification Intensity Index
2. For pre-2003 data, use **OCC2010** → use Census-to-SOC crosswalk at [usa.ipums.org/usa/volii/occtooccsoc18.shtml](https://usa.ipums.org/usa/volii/occtooccsoc18.shtml)
3. For matching to the EIG AI-unemployment repo data, use **OCC1990** → matches David Dorn's `occ1990dd` crosswalk included in the repo
4. See IPUMS forum thread on O\*NET-CPS crosswalk workflow: [forum.ipums.org/t/onet-cps-crosswalk/4345](https://forum.ipums.org/t/onet-cps-crosswalk/4345)

**Caveat**: Census codes are based on SOC but aggregated where cell sizes < 10,000. The mapping is often many-to-many. Attach O\*NET work activity scores at the aggregated level where CPS codes map cleanly.

### Sample Sizes

- **ASEC**: ~75K–100K persons/year (of which ~40K–60K are employed wage workers)
- **ORG** (pooled 12 months): ~180K–220K earners/year — **3x the ASEC sample**
- At detailed occupation level (~540 OCC2010 categories), average ~400 ORG obs per occupation per year
- **Warning**: Your specification-intensive occupations (art directors, creative directors, VCs, A&R) are **small occupations** — expect only 50–200 observations per year for some. Pool multiple years (e.g., 2015–2023) for adequate power, or classify at broader occupation-group level.
- ORG excludes self-employed — if spec workers increasingly freelance, you're missing them. Use ASEC (CLASSWLY) as complement.

---

## 2. IPUMS-ATUS: Consumer Specification Time

### What to Extract

Go to [atusdata.org](https://www.atusdata.org/atus/), create account, start new extract.

**Sample selection:** All years 2003–2024 (or latest available).

#### Time-Use Variables (the core data)

In the ATUS-X extract system, you select **time-use variables** which are pre-computed minutes-per-day for activity categories. Key ones:

| Variable | Activity Code | Description | Why You Need It |
|----------|--------------|-------------|-----------------|
| **BLS_PURCH** | 07xxxx | Total consumer purchases time (all shopping) | Primary "shopping time" measure. Broadest definition. |
| **ACT_PURCH** | 070100 | Shopping (store, telephone, internet) | Narrower: just the shopping act itself |
| **ACT_PURCH1** | 070101 | Grocery shopping | Separate out routine purchasing |
| **ACT_PURCH4** | 070104 | Shopping except groceries, food, gas | **Discretionary shopping** — closer to "specification" |
| **ACT_PURCH5** | 070105 | Waiting associated with shopping | |
| **ACT_RSCH** | 070200 | **Researching purchases** | **Most directly relevant.** Only available 2010+. This IS consumer specification labor. |
| **ACT_RSCH1** | 070201 | **Comparison shopping** | Includes "comparing prices at different stores" AND "reading product reviews". This is your spec labor variable. |
| **ACT_RSCH99** | 070299 | Researching purchases, n.e.c. | Other purchase research not elsewhere classified |

Also grab these for context:
| Variable | Description | Why |
|----------|-------------|-----|
| **BLS_LEIS** | Total leisure time | Denominator / context |
| **BLS_WORK** | Total work time | Context |
| **BLS_HHACT** | Total household activities | Context |
| **ACT_COMP** | Computer use (leisure) | May capture browsing/research coded as leisure |

**Critical note:** `ACT_RSCH` (070200 series) was added to the ATUS coding lexicon in **2010**. Before 2010, purchase research was folded into general shopping (0701xx) or leisure computer use. This creates a structural break — you can do:
- 2003–present: total shopping time (BLS_PURCH)
- 2010–present: research time specifically (ACT_RSCH)

#### Demographic Variables (for breakdowns)

| Variable | Description | Why |
|----------|-------------|-----|
| **WT06** | ATUS person weight | Required for representative estimates |
| **AGE** | Age | Break out by age group (younger cohorts may research more) |
| **SEX** | Sex | Gendered shopping/research patterns |
| **EDUC** or **EDUCYRS** | Education | Does research effort increase with education? |
| **RACE** | Race | Control |
| **EMPSTAT** | Employment status | Employed vs. not — do workers research differently? |
| **HH_SIZE** | Household size | More people = more purchasing decisions? |
| **FAMINCOME** | Family income | Does income predict research effort? Higher income = more spec labor? |
| **DAY** | Day of week | Shopping patterns vary by day |
| **HOLIDAY** | Holiday flag | Control |
| **STATEFIP** | State | Geographic variation |

#### Activity-Level Variables (if doing activity-level extract)

| Variable | Description | Why |
|----------|-------------|-----|
| **ACTIVITY** | 6-digit activity code | Raw code for each diary episode |
| **DURATION** | Minutes spent on activity | Duration per episode |
| **WHERE** | Location code | Key for online proxy: 1=home (proxy online), 6=grocery store, 7=other store/mall. Cross-tab WHERE×activity over time to show shift from in-store to at-home shopping. |

#### Eating & Health Module (EHM) — Special Years

Available in: 2006–2008, 2014–2016, 2022–2023. The **2022–23 wave** directly asks about online grocery shopping participation — a direct measure, not just a WHERE proxy. Use weight `EHWT` instead of `WT06` for EHM analysis.

#### Linked CPS Variables

ATUS respondents are drawn from CPS households, so you can also request linked CPS variables:
- **OCC2010** / **OCC2** — occupation of respondent → test if spec-occupation workers also do more consumption research
- **EARNWEEK** — earnings → test income-research correlation
- **CLASSWKR** — self-employed flag
- **EDUC** — education → does research effort increase with education?

#### What Analysis Is Feasible

| Analysis | Feasibility | Notes |
|----------|-------------|-------|
| Annual trend in total shopping time (2003–present) | **Strong** | ~10K respondents/year; ~40–45% report any shopping on diary day |
| Annual trend in research time (2010–present) | **Moderate** | 0702 is a small category (<5% prevalence); noisy year-to-year. Pool 2–3 year windows. **No one has published this analysis yet — gap you can fill.** |
| Breakdown by age/education/income | **Moderate** | Use 3-year pooled samples. Recent years have lower sample sizes (~7,700 in 2024, response rate 32%). |
| Online vs. in-store proxy | **Moderate** | Use WHERE=1 (home) + shopping codes as proxy for online. WHERE=6,7 (grocery/other store) for in-store. Not perfect but usable. |
| Shopping time by occupation of respondent | **Weak** | Very thin cells. Link via OCC2 variable to test if spec-occupation workers do more research. |
| Shopping time falling while spending rises | **Strong** | NerdWallet/ATUS analysis: shopping time per day has *decreased* since 2003 while e-commerce spending rose ~470%. Supports narrative that online = more time-efficient execution, but specification effort persists. |

---

## 3. Census ACS via IPUMS-USA: Large-Sample Wage Data

### Why ACS in Addition to CPS?

- ACS sample is **~3.5 million people/year** vs. CPS ~60K–100K
- This means you can get **reliable wage estimates for detailed occupations at the metro level**
- Critical for geographic variation: does the spec premium differ across cities?
- Available 2000–present (annual), plus decennial Census microdata 1980–2000

### IPUMS-USA Extract: Variables to Select

Go to [usa.ipums.org](https://usa.ipums.org/), create account, start new extract.

**Sample selection:** ACS samples 2005–2023 (or latest). For deeper history: 2000 Census 5% sample, 1990 Census 5%, 1980 Census 5%.

| Variable | Description | Why |
|----------|-------------|-----|
| **YEAR** | Survey year | |
| **PERWT** | Person weight | Required |
| **INCWAGE** | Annual wage/salary income | Primary wage measure |
| **OCC** | Occupation (Census codes) | Raw codes |
| **OCC2010** | Harmonized occupation | Consistent over time |
| **OCCSOC** | SOC code (2000+) | **Merges directly to O\*NET** |
| **IND** | Industry | |
| **UHRSWORK** | Usual hours worked per week | For hourly wage computation |
| **WKSWORK2** | Weeks worked last year (intervals) | For annual-to-hourly |
| **AGE** | Age | Control |
| **SEX** | Sex | Control |
| **RACE** | Race | Control |
| **HISPAN** | Hispanic origin | Control |
| **EDUC** / **EDUCD** | Education (general / detailed) | Control |
| **CLASSWKR** | Class of worker | Self-employment flag |
| **STATEFIP** | State | Geography |
| **MET2013** | Metropolitan area (2013 delineation) | Metro-level spec premium |
| **PUMA** | Public Use Microarea | Sub-metro geography |

### ACS vs. CPS: When to Use Which

| Dimension | CPS (ASEC) | ACS |
|-----------|------------|-----|
| Sample size | ~60K–100K/year | **~3.5M/year** |
| Wage detail | Weekly + hourly earnings, top-coded | Annual income only, top-coded higher |
| Occupation detail | OCC2010 (~540) + OCCSOC | OCC2010 (~540) + OCCSOC |
| Geographic detail | State + metro (noisy) | **State + metro + PUMA (reliable)** |
| Time depth | 1962+ (earnings: 1982+) | **1980+** (decennial); 2000+ (annual) |
| Union status | **Yes** | No |
| Hours/weeks | Continuous | Intervals (WKSWORK2) |
| Best for | Regressions with controls; time trends | **Geographic variation; small-occupation analysis** |

**Recommendation:** Use CPS for your main regression analysis (more wage detail, union/firm controls). Use ACS for geographic analysis and occupation-level charts where you need large cell sizes.

---

## 4. Census Business Dynamics Statistics (BDS): Entrepreneurship

### What to Download

Go to [census.gov/data/datasets/time-series/econ/bds/bds-datasets.html](https://www.census.gov/data/datasets/time-series/econ/bds/bds-datasets.html)

All files are CSV. Key tables:

| Table | File | What It Contains | Why |
|-------|------|-----------------|-----|
| **Economy-wide** | `bds_e.csv` | Aggregate firm/establishment dynamics | Baseline trends |
| **By Sector (NAICS 2-digit)** | `bds_sec.csv` | Firm entry/exit by industry sector | **Core table.** Test: is firm creation growing faster in spec-intensive industries (NAICS 54 Professional Services, 71 Arts/Entertainment, 72 Accommodation/Food) vs. execution-intensive (NAICS 31-33 Manufacturing, 48-49 Transportation/Warehousing)? |
| **By NAICS 3-digit** | `bds_n3.csv` | More detailed industry breakdown | Finer-grained industry comparisons |
| **By NAICS 4-digit** | `bds_n4.csv` | Most detailed industry breakdown | Specific sub-industries |
| **By Firm Age** | `bds_fa.csv` | Dynamics by firm age (startups vs. mature) | Startup rates over time |
| **By State** | `bds_st.csv` | Geographic variation | State-level spec entrepreneurship |
| **By MSA** | `bds_ma.csv` | Metro-level dynamics | Metro-level analysis |

**Key variables in each table:**

| Variable | Description |
|----------|-------------|
| `firms` | Number of firms |
| `estabs` | Number of establishments |
| `emp` | Employment |
| `job_creation` | Gross job creation |
| `job_destruction` | Gross job destruction |
| `net_job_creation` | Net job creation |
| `firmdeath_firms` | Number of firm deaths |
| `firmdeath_emp` | Employment at dying firms |
| `estabs_entry` | Establishment births |
| `estabs_exit` | Establishment deaths |

**Years:** 1978–2023, annual.

**Suggested analysis:**
1. Compute firm entry rate by NAICS sector over time: `new_firms / total_firms`
2. Classify sectors as spec-intensive vs. execution-intensive
3. Test whether the entry-rate gap between spec and exec sectors has widened

---

## 5. Census Annual Business Survey (ABS): AI Adoption by Industry

### What to Download

Go to [ncses.nsf.gov/surveys/annual-business-survey/2023](https://ncses.nsf.gov/surveys/annual-business-survey/2023)

Download the full set (Excel ZIP, 801 KB). Key tables for your research:

| Tables | Content | Why |
|--------|---------|-----|
| **Tables 74–75** | Use of AI as production technology, by NAICS industry and company size (2020–22) | **Core table.** Which industries are automating execution with AI? |
| **Tables 76–77** | Cloud computing adoption by industry | Supporting evidence on automation |
| **Tables 78–79** | Specialized software adoption by industry | Supporting evidence |
| **Tables 80–81** | Robotics adoption by industry | Physical execution automation |
| **Tables 82–83** | Specialized equipment adoption by industry | Physical execution automation |

**Key insight sectors:**
- NAICS 51 (Information) and 54 (Professional/Scientific/Technical Services) = highest AI adoption
- Compare to your O\*NET specification intensity scores by industry to test: do the most AI-adopting industries show the strongest spec wage premium?

---

## 6. BLS Consumer Expenditure Survey (CE/CEX): Spending Patterns

### What to Download

**Option A: Published tables (fastest)**
Go to [bls.gov/cex/tables.htm](https://www.bls.gov/cex/tables.htm) — pre-built tables with expenditure breakdowns by demographics. Available back to 1984.

**Option B: Public-use microdata (for custom analysis)**
Go to [bls.gov/cex/pumd_data.htm](https://www.bls.gov/cex/pumd_data.htm) — individual household-level expenditure data in CSV, SAS, or Stata format. Available 1980–2024 (except 1982–83).

### Key Expenditure Categories for Spec vs. Commodity

The CEX uses the **CPI-U item coding scheme**. The two survey instruments capture different detail:

**Interview Survey (MTBI/FMLI files):** Major expenditures, regular payments
**Diary Survey:** Detailed food and daily purchases

| Category | CEX Item Codes | Spec/Commodity Signal |
|----------|---------------|----------------------|
| **Food at home** | FOODHOME | Commodity (mass-market grocery) |
| **Food away from home** | FOODAWAY | Leans specification (restaurant choice = curation) |
| **Alcoholic beverages** | ALCBEV | Break out by type if possible — craft vs. mass |
| **Apparel & services** | APPAREL | Could split: fast fashion (commodity) vs. boutique (spec) |
| **Entertainment** | ENTRTAIN | Specification-heavy (choosing experiences) |
| **Reading** | READING | Indie bookstore proxy |
| **Education** | EDUCATN | Specification of human capital |
| **Personal care** | PERSCARE | Increasingly specification-heavy (curated beauty) |
| **Miscellaneous** | MISC | |
| **Household furnishings** | FURNISH | Design/spec-heavy |

**Suggested analysis:**
1. Track **food-away-from-home as % of total food** over time (1984–2024) — this is a classic "specification premium" measure: you pay more for someone to curate/prepare the food
2. Track **entertainment + reading + personal care** as share of total expenditure — these are specification-intensive categories
3. Compare across income quintiles: do higher-income households spend more on specification-heavy categories?

### CEX Microdata Structure

The FMLI files (Interview Survey, household level) have pre-computed summary variables:

| Variable | Description |
|----------|-------------|
| `FINCBTXM` | Total income before taxes |
| `TOTEXPPQ` | Total expenditures, current quarter |
| `FOODPQ` | Total food, current quarter |
| `FABORPQ` | Food away from home, current quarter |
| `FHOMEPQ` | Food at home, current quarter |
| `ALCBEVPQ` | Alcoholic beverages, current quarter |
| `ENTERTPQ` | Entertainment, current quarter |
| `READPQ` | Reading, current quarter |
| `APPARPQ` | Apparel, current quarter |

These summary variables make it easy to compute shares over time.

**R package**: The [`cepumd`](https://cran.r-project.org/web/packages/cepumd/cepumd.pdf) R package provides functions to calculate CE weighted estimates from PUMD, handle the hierarchical grouping files, and aggregate UCCs.

**NBER extracts**: NBER has cleaned CE extracts merging quarterly interview files into annual records, but these are restricted to NBER computing systems (not downloadable). Use the BLS PUMD directly.

---

## 7. Priority Order: What to Pull First

### Tier 1: Pull this week (high-value, easy)

1. **IPUMS-CPS extract** — ASEC samples 2005–2025, variables listed above. ~30 min to set up, extract ready in hours. This is your regression dataset.

2. **BDS by sector** — download `bds_sec.csv` from Census. One file, instant download. Compute firm entry rates by industry.

3. **ABS Tables 74–75** — AI adoption by industry. One Excel download. Cross-reference with your O\*NET spec index.

### Tier 2: Pull next week (important but more setup)

4. **IPUMS-ATUS extract** — 2003–2024, time-use variables listed above. ~30 min to set up. Produces your "consumer specification time" trend.

5. **CEX published tables** — Food-away-from-home share trend from bls.gov/cex/tables.htm. Quick grab.

6. **IPUMS-USA (ACS) extract** — if you need metro-level spec premium variation. Larger dataset, more processing time.

### Tier 3: Pull if time permits (supplementary)

7. **CEX PUMD microdata** — for custom expenditure analysis by income/demographics.
8. **BDS by NAICS 3-digit** — finer industry detail on firm dynamics.
9. **ABS full 85 tables** — robotics, software, cloud adoption alongside AI.
