# CPS ASEC Microdata

## Files

### CSV format (2019–2025) — `csv/`
Each zip contains 4 files:
- `pppub{YY}.csv` — **Person file** (wages, occupation, demographics) — this is the main file you need
- `hhpub{YY}.csv` — Household file
- `ffpub{YY}.csv` — Family file
- `asec_csv_repwgt_{YEAR}.csv` — Replicate weights (for standard errors)

### Fixed-width format (2005, 2009, 2014) — `fixed-width/`
- `.dat.gz` files requiring SAS/Stata/R read-in programs to parse
- Data dictionaries in `docs/`

### Documentation — `docs/`
- `asec2024_ddl_pub_full.pdf` — Full 2024 data dictionary
- `asec2024_persfmt.txt` — Person file variable layout (SAS INPUT format)
- `asec2014_pubuse_dd.txt` — 2014 data dictionary

## Key Variables in Person File (pppub{YY}.csv)

Variables mapped from the extract-guide.md IPUMS names to Census ASEC names:

| Extract Guide (IPUMS) | Census ASEC Name | Column | Description |
|----------------------|-----------------|--------|-------------|
| YEAR | H_YEAR or from filename | — | Survey year |
| Person ID | PERIDNUM | 1 | Unique person identifier |
| ASECWT | MARSUPWT | 138 | March supplement person weight |
| AGE | A_AGE | 80 | Age |
| SEX | A_SEX | 81 | Sex (1=Male, 2=Female) |
| RACE | PRDTRACE | 42 | Race (detailed) |
| HISPAN | PEHSPNON | 14 | Hispanic origin (1=Hispanic, 2=Not) |
| EDUC | A_HGA | 123 | Highest grade attended |
| OCC (detailed) | PEIOOCC | 816 | Census occupation code (current/last job) |
| OCC (major group) | A_MJOCC | 91 | Major occupation group |
| IND (detailed) | PEIOIND | 815 | Census industry code |
| IND (major group) | A_MJIND | 89 | Major industry group |
| INCWAGE | WSAL_VAL | 778 | Wage and salary income |
| INCBUS (self-emp) | SEMP_VAL | 689 | Self-employment income |
| Total earnings | ERN_VAL | 199 | Total earnings |
| UHRSWORK | A_USLHRS | 117 | Usual hours worked per week |
| WKSWORK | WKSWORK | 775 | Weeks worked last year |
| HRSWK | HRSWK | 237 | Hours per week last year |
| CLASSWKR | A_CLSWKR | 130 | Class of worker |
| WKSTAT | A_WKSTAT | 132 | Full/part-time status |
| COW (class of worker) | PRCOW1 | 56 | Class of worker (current) |
| LJCW | LJCW | 479 | Class of worker (longest job last year) |
| STATEFIP | GESTFIPS | — | State FIPS code |
| EMPSTAT | PRPERTYP / PEMLR | — | Employment status |

## Computing Hourly Wages

```python
# Approximate hourly wage from annual data
hourly_wage = WSAL_VAL / (WKSWORK * HRSWK)

# Filter to full-time full-year workers for cleaner estimates:
# A_USLHRS >= 35 and WKSWORK >= 50
```

## Occupation Code Crosswalk

Census occupation codes (PEIOOCC) are NOT the same as SOC codes used by O*NET and OES.
You need the Census-to-SOC crosswalk:
- 2020+ uses 2018 Census codes → 2018 SOC
- 2011-2019 uses 2010 Census codes → 2010 SOC
- 2003-2010 uses 2002 Census codes → 2000 SOC

Crosswalk available at: https://www.census.gov/topics/employment/industry-occupation/guidance/code-lists.html

## Notes
- Pre-2019 files are fixed-width and need parsing scripts
- Variable names and positions can change between years — always check the data dictionary
- MARSUPWT (weight) must be used for all tabulations
- Top-coding thresholds for WSAL_VAL vary by year
