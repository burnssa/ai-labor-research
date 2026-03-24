# Data Inventory for "Specification Labor" Research

*Current as of March 2026*

This document describes all datasets currently downloaded and available for analysis, organized by what each dataset contains and what it can be used for.

---

## 1. Occupational Task & Attribute Data

### O*NET v29.1 (`data/onet/db_29_1_text/`)
- **Format:** Tab-delimited text files (40 files)
- **Coverage:** ~1,000 occupations covering the entire US economy, keyed by O*NET-SOC code (e.g., `11-2021.00`)
- **Key files for this research:**
  - `Work Activities.txt` (8.2MB) — 41 Generalized Work Activities per occupation, with Importance (1-5) and Level (1-7) scores. The GWAs are organized in 4 categories: Information Input, Mental Processes, Work Output, Interacting With Others.
  - `Occupation Data.txt` (260K) — SOC code, title, and description for each occupation
  - `Task Statements.txt` (2.6MB) — Occupation-specific task descriptions (~20-30 per occupation)
  - `Task Ratings.txt` (11MB) — Importance/relevance/frequency ratings for each task
  - `Tasks to DWAs.txt` (1.1MB) — Maps tasks to 2,087 Detailed Work Activities
  - `DWA Reference.txt` (183K) — Titles for all 2,087 DWAs
  - `Skills.txt` (5.3MB) — 35 skills per occupation with importance/level scores
  - `Abilities.txt` (8.0MB) — 52 abilities per occupation
  - `Knowledge.txt` (5.3MB) — 33 knowledge domains per occupation
  - `Work Context.txt` (33MB) — Working conditions/environment descriptors
  - `Work Styles.txt` (1.2MB) — Personal characteristics (attention to detail, initiative, etc.)
- **What we tried:** Building a "Specification Intensity Index" from GWAs and DWAs. Both approaches had problems — GWAs are too coarse to distinguish "deciding what to make" from "deciding how to make it," and DWA text-matching produced too many false positives and only classified 42 of 2,087 DWAs as spec-related.

### AI Exposure Scores (`data/ai-exposure/`)
- **Felten, Raj & Seamans (2021) AIOE Index** — `AIOE_DataAppendix.xlsx`
  - Appendix A: 775 occupations with AI Occupational Exposure scores by 6-digit SOC
  - Appendix B: Industry-level scores by 4-digit NAICS
  - Appendix C: County-level scores by FIPS
  - Appendix D: AI Application-Ability matrix (52 abilities × 10 AI applications, from MTurk survey)
  - Appendix E: Standardized ability-level exposure
- **Generative AI extensions:**
  - `Image_Generation_AIOE_AIIE.xlsx` — Image gen AI exposure by occupation and industry
  - `Language_Modeling_AIOE_AIIE.xlsx` — Language model AI exposure by occupation and industry
- **SOC crosswalk:** `soc_2010_to_2018_crosswalk.xlsx`
- **Note:** The Eloundou (GPT exposure), Webb (patent-based), and Eisfeldt (gen AI) scores are in the EIG-Research/AI-unemployment GitHub repo but require git-lfs to download. The repo's code files reference them at paths like `data/1raw/gptsRgpts_occ_lvl.csv`.

---

## 2. Occupational Wage Data

### BLS OES/OEWS (`data/oes/`)
- **Format:** Excel files, one per year
- **Coverage:** National, all occupations (~830), median and mean wages, employment counts
- **Years downloaded:** 1997, 2005, 2009, 2014, 2019, 2024
- **Key files:**
  - `national_1997_dl.xls`
  - `oesm05nat/national_may2005_dl.xls`
  - `oesm09nat/national_dl.xls`
  - `oesm14nat/national_M2014_dl.xlsx`
  - `oesm19nat/national_M2019_dl.xlsx`
  - `oesm24nat/national_M2024_dl.xlsx`
- **Key columns:** SOC code, occupation title, employment total, mean hourly/annual wage, median hourly/annual wage, 10th/25th/75th/90th percentile wages
- **Merge key:** SOC code → merges to O*NET and AIOE data

### CPS ASEC Microdata (`data/cps-asec/`)
- **Format:** CSV (2019-2025), fixed-width .dat.gz (2005, 2009, 2014)
- **Coverage:** Individual-level survey, ~60K-100K persons/year, nationally representative
- **Years downloaded:**
  - CSV: 2019, 2020, 2021, 2022, 2023, 2024, 2025 (in `csv/` as zips; 2024 extracted to `csv/2024/pppub24.csv`)
  - Fixed-width: 2005, 2009, 2014 (in `fixed-width/`)
- **Key variables in person file (pppub{YY}.csv):**
  - `PEIOOCC` — Census occupation code (NOT SOC; needs crosswalk)
  - `WSAL_VAL` — Wage and salary income (annual)
  - `SEMP_VAL` — Self-employment income
  - `ERN_VAL` — Total earnings
  - `A_USLHRS` — Usual hours worked per week
  - `WKSWORK` — Weeks worked last year
  - `HRSWK` — Hours per week last year
  - `A_AGE`, `A_SEX`, `PRDTRACE`, `PEHSPNON` — Demographics
  - `A_HGA` — Education
  - `A_CLSWKR` — Class of worker (self-employment flag)
  - `A_WKSTAT` — Full/part-time status
  - `MARSUPWT` — Person weight (required for representative estimates)
  - `PEIOIND` — Census industry code
- **Documentation:** Data dictionary PDF and SAS layout in `docs/`
- **Merge key:** `PEIOOCC` → Census-to-SOC crosswalk → O*NET/OES

### Crosswalks (`data/crosswalks/`)
- `2018-occupation-code-list-and-crosswalk.xlsx` — Census 2018 code → 2018 SOC (for CPS 2020+)
- `2010-occ-codes-with-crosswalk-from-2002-2011.xls` — Census 2010 → 2010 SOC + Census 2002 → 2010 crosswalk (for CPS 2005-2019)
- `soc_2010_to_2018_crosswalk.xlsx` — SOC 2010 → SOC 2018 bridge
- `2018-ACS-PUMS-Occupation-Code-List.xlsx` — ACS PUMS occupation codes

---

## 3. Consumer Time Use Data

### ATUS 2003-2024 (`data/atus/`)
- **Format:** Fixed-width/CSV-like .dat files with SAS/SPSS/Stata read-in programs
- **Coverage:** ~10K-13K respondents/year (declining to ~7,700 in 2024), 24-hour time diary, nationally representative
- **Key files:**
  - `atussum_0324.dat` (235MB) — **Activity summary file.** One row per respondent, one column per activity code. Columns named `tXXXXXX` where XXXXXX is the 6-digit activity code. Contains total minutes spent on each activity on diary day. This is the primary analysis file.
  - `atusresp_0324.dat` (99MB) — Respondent demographics, weights, diary day info
  - `atuscps_0324.dat` (1.1GB) — Links ATUS respondents to their CPS records (occupation, earnings, education)
- **Key activity code columns in summary file (consumer specification relevant):**
  - `t070101` — Grocery shopping
  - `t070102` — Purchasing gas
  - `t070103` — Purchasing food (not groceries)
  - `t070104` — Shopping, except groceries, food, and gas (DISCRETIONARY SHOPPING)
  - `t070105` — Waiting associated with shopping
  - `t070199` — Shopping, n.e.c.
  - `t070201` — **Comparison shopping** (includes reading product reviews)
  - `t070299` — Researching purchases, n.e.c.
  - `t180701` — Travel to grocery shopping
  - `t180782` — Travel to other shopping
  - `t120308` — Computer use for leisure (excl. games) — may capture browsing/research coded as leisure
  - `t020901` — Financial management
  - `t020902` — Household organization & planning
- **Key demographic columns:** `TUYEAR` (year), `TUFNWGTP`/`TU20FWGT` (weights), `TEAGE`, `TESEX`, `PEEDUCA`, `TELFS` (labor force status), `TUDIARYDAY`, `TRHOLIDAY`
- **What we found:** Total shopping time fell from 24→18 min/day (2003-2024). Explicit purchase research time (0702) is vanishingly small (~0.05-0.22 min/day) — diary methodology doesn't capture fragmented product research. Leisure computer use rose substantially but we can't isolate shopping-related browsing within it.
- **Lexicon:** `lexiconnoex0324.pdf` — Complete activity coding scheme 2003-2024. 17 major categories, 6-digit codes.

---

## 4. Firm Dynamics Data

### Census BDS 1978-2023 (`data/bds/`)
- **Format:** CSV
- **Coverage:** Annual, all private-sector employer firms
- **Files:**
  - `bds2023_sec.csv` (143K) — By NAICS 2-digit sector (19 sectors × 46 years). Variables: firms, establishments, employment, estab entry/exit rates, job creation/destruction rates, firm deaths.
  - `bds2023_sec_fa.csv` (1.4MB) — By sector × firm age (0, 1, 2, ..., 26+). Can track startup dynamics by industry.
  - `bds2023_fa.csv` (84K) — Economy-wide by firm age
  - `bds2023_st.csv` (369K) — By state
- **What we explored:** Startup rates by NAICS sector. Arts/Entertainment (+65%), Healthcare (+54%), Accommodation/Food (+53%) show strong new-firm growth vs. Manufacturing (-33%), Wholesale (-48%). But NAICS 2-digit is too coarse to distinguish "craft" from "commodity" businesses within a sector.

### Census ABS Technology Module (`data/abs/`)
- **Format:** Pipe-delimited .dat files
- **Coverage:** ~300K-850K firms, by NAICS industry, firm size, demographics
- **Files:**
  - `AB2300CSCB01.dat` (450MB) — 2023 ABS, business characteristics including technology adoption
  - `ABSCB2019.dat` (123MB) — 2019 ABS, technology module with AI subtype detail (machine learning, NLP, machine vision, voice recognition, automated guided vehicles)
  - `AB2300CSCB01_FIELDS.txt` — Data dictionary (pipe-delimited field definitions)
- **Key variables:** NAICS2022, QDESC (question code), BUSCHAR (business characteristic), FIRMPDEMP (number of firms), EMP (employees), RCPPDEMP (revenue)
- **Highest AI adoption sectors (2018 data):** Information (NAICS 51), Professional/Scientific/Technical (54), Finance (52)

---

## 5. Cross-Country / Macro Data

### Penn World Table 11.0 (`data/pwt/`)
- `pwt110.dta` (3.3MB) — Stata format. 183 countries, 1950-2019. Country-level labor share (`labsh`), capital share, TFP, GDP, employment. Useful for cross-country labor share trends but not industry-level.

---

## 6. Generated Outputs (`output/`)

- `craft_premium_timeseries.csv` — 139 datapoints across 6 craft/specification industries (craft beer, craft spirits, Etsy, farmers markets, indie bookstores, specialty food). Compiled from public sources (Brewers Association, ACSA, SEC filings, USDA, ABA, SFA).
- `craft_premium_growth.png` — Two-panel chart: indexed growth of craft segments + craft beer volume vs. dollar share showing ~2x specification premium.
- `atus_consumer_time_trends.csv` — Annual weighted averages 2003-2024 for shopping, research, travel-to-shopping, and leisure computer use time.
- `atus_consumer_specification_time.png` — Three-panel chart showing declining shopping time, declining travel/rising computer use, and tiny but rising purchase research time.

---

## 7. Documentation

- `data-availability-survey.md` — Comprehensive survey of all potential data sources with URLs, access types, relevance assessments, and download links
- `extract-guide.md` — Specific variable lists for IPUMS-CPS, IPUMS-ATUS, ACS, BDS, ABS, and CEX extracts
- `data/cps-asec/README.md` — CPS ASEC variable name mapping (IPUMS names → Census names)

---

## What's NOT downloaded (requires registration, payment, or browser download)

| Dataset | Barrier | What it would add |
|---------|---------|-------------------|
| IPUMS CPS/ATUS/ACS | Registration (may require institutional affiliation) | Harmonized variables, easier merges, ORG earnings data |
| Eloundou/Webb/Eisfeldt AI exposure CSVs | git-lfs needed for EIG GitHub repo | Additional AI exposure measures by occupation |
| BLS CEX microdata | BLS blocks automated download | Consumer expenditure detail by category (food-away-from-home share, etc.) |
| MTUS/AHTUS historical time use | IPUMS or CTUR registration | Shopping time back to 1965, but only one coarse "Shopserv" category |
| Lightcast job postings | Paid enterprise ($10K+/yr) | Job posting trends by occupation and skill |
| EU KLEMS / INTAN-Invest | Free download (not yet attempted) | Industry-level labor shares + intangible investment decomposition (brand, design, software separately) |
| Google Trends | Free, no registration | Product research search volume indices over time |
| BLS CEX published tables | BLS blocks automated download | Pre-computed food-away-from-home share trends 1984-2024 |
