"""
Phase 1: Data Assembly
======================
Loads, inspects, harmonizes, and merges O*NET task profiles with OEWS employment/wage
data to produce a master analysis panel.

Steps:
  1a. Inspect each OEWS file (column names, SOC format, occupation count)
  1b. Build SOC harmonization table via crosswalks
  1c. Load O*NET Work Activities (GWA importance scores)
  1d. Load O*NET Skills (importance scores)
  1e. Merge O*NET profiles with OEWS employment/wages
  1f. Load Felten AIOE scores
  1g. Produce master_panel.csv
"""

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
os.makedirs(ANALYSIS, exist_ok=True)

# =============================================================================
# STEP 1a: Inspect each OEWS file
# =============================================================================
print("=" * 80)
print("STEP 1a: OEWS FILE COMPATIBILITY REPORT")
print("=" * 80)

oews_files = {
    1997: os.path.join(DATA, 'oes', 'national_1997_dl.xls'),
    2005: os.path.join(DATA, 'oes', 'oesm05nat', 'national_may2005_dl.xls'),
    2009: os.path.join(DATA, 'oes', 'oesm09nat', 'national_dl.xls'),
    2014: os.path.join(DATA, 'oes', 'oesm14nat', 'national_M2014_dl.xlsx'),
    2019: os.path.join(DATA, 'oes', 'oesm19nat', 'national_M2019_dl.xlsx'),
    2024: os.path.join(DATA, 'oes', 'oesm24nat', 'national_M2024_dl.xlsx'),
}

oews_info = {}

for year, fpath in sorted(oews_files.items()):
    print(f"\n--- {year}: {os.path.basename(fpath)} ---")

    # Read with flexible parsing
    try:
        if fpath.endswith('.xls'):
            df = pd.read_excel(fpath, engine='xlrd')
        else:
            df = pd.read_excel(fpath, engine='openpyxl')
    except Exception as e:
        print(f"  ERROR reading file: {e}")
        continue

    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")

    # Identify key columns by searching for patterns
    cols_lower = {c: c.lower().replace(' ', '_').replace('(', '').replace(')', '') for c in df.columns}

    # Find SOC code column
    soc_col = None
    for c in df.columns:
        cl = str(c).lower()
        if 'occ_code' in cl or 'soc' in cl.replace(' ', '') or cl == 'occ code':
            soc_col = c
            break
        if cl.strip() in ('occ_code', 'o*net-soc code'):
            soc_col = c
            break

    if soc_col is None:
        # Try first column if it looks like SOC codes
        first_col = df.columns[0]
        sample = str(df[first_col].dropna().iloc[0]) if len(df) > 0 else ''
        if '-' in sample and len(sample) >= 6:
            soc_col = first_col

    # Find employment column
    emp_col = None
    for c in df.columns:
        cl = str(c).lower()
        if 'tot_emp' in cl or cl == 'employment' or 'total employment' in cl.lower():
            emp_col = c
            break
        if cl.strip() == 'tot_emp':
            emp_col = c
            break

    # Find median wage column
    med_wage_col = None
    for c in df.columns:
        cl = str(c).lower()
        if 'a_median' in cl or 'median' in cl.lower() and 'annual' in cl.lower():
            med_wage_col = c
            break
        if cl.strip() == 'a_median':
            med_wage_col = c
            break

    # Find mean wage column
    mean_wage_col = None
    for c in df.columns:
        cl = str(c).lower()
        if 'a_mean' in cl or ('mean' in cl.lower() and 'annual' in cl.lower()):
            mean_wage_col = c
            break

    # SOC code format analysis
    if soc_col is not None:
        soc_sample = df[soc_col].dropna().astype(str)
        soc_lengths = soc_sample.str.len().value_counts().head(3)
        soc_examples = soc_sample.head(5).tolist()
        n_occs = soc_sample.nunique()

        # Check for SOC-like format (XX-XXXX)
        has_dash = soc_sample.str.contains('-').mean()
    else:
        soc_examples = ['NOT FOUND']
        n_occs = 0
        has_dash = 0

    info = {
        'file': os.path.basename(fpath),
        'shape': df.shape,
        'soc_col': soc_col,
        'emp_col': emp_col,
        'med_wage_col': med_wage_col,
        'mean_wage_col': mean_wage_col,
        'soc_examples': soc_examples[:3],
        'n_occupations': n_occs,
        'columns': list(df.columns),
    }
    oews_info[year] = info

    print(f"  SOC column: {soc_col}")
    print(f"  SOC examples: {soc_examples[:5]}")
    print(f"  SOC has dash format: {has_dash:.0%}")
    print(f"  Unique occupations: {n_occs}")
    print(f"  Employment column: {emp_col}")
    print(f"  Median wage column: {med_wage_col}")
    print(f"  Mean wage column: {mean_wage_col}")

# =============================================================================
# STEP 1a (continued): Load and standardize each OEWS file
# =============================================================================
print("\n\n" + "=" * 80)
print("STEP 1a (continued): STANDARDIZED OEWS LOADING")
print("=" * 80)

def load_oews(year, fpath):
    """Load an OEWS file and return standardized DataFrame with columns:
    soc_code, occ_title, employment, median_wage, mean_wage, year"""

    if fpath.endswith('.xls'):
        df = pd.read_excel(fpath, engine='xlrd')
    else:
        df = pd.read_excel(fpath, engine='openpyxl')

    # Normalize column names
    col_map = {}
    for c in df.columns:
        cl = str(c).upper().strip()
        if cl in ('OCC_CODE', 'OCC CODE'):
            col_map[c] = 'soc_code'
        elif cl in ('OCC_TITLE', 'OCC TITLE', 'OCC_TITL', 'OCCUPATION TITLE'):
            col_map[c] = 'occ_title'
        elif cl == 'TOT_EMP':
            col_map[c] = 'employment'
        elif cl == 'A_MEDIAN':
            col_map[c] = 'median_wage'
        elif cl == 'A_MEAN':
            col_map[c] = 'mean_wage'
        elif cl in ('H_MEDIAN',):
            col_map[c] = 'median_hourly'
        elif cl in ('H_MEAN',):
            col_map[c] = 'mean_hourly'
        elif cl in ('OCC_GROUP', 'O_GROUP', 'GROUP'):
            col_map[c] = 'occ_group'

    df = df.rename(columns=col_map)

    # Keep only rows for detailed occupations (not summary groups)
    # Different years use different conventions:
    #   2005/2009: group column has NaN for detailed, 'major'/'total' for summaries
    #   2014+: OCC_GROUP column has 'detailed', 'major', 'minor', 'broad', 'total'
    if 'occ_group' in df.columns:
        grp = df['occ_group'].astype(str).str.lower().str.strip()
        if 'detailed' in grp.values:
            df = df[grp == 'detailed'].copy()
        else:
            # 2005/2009 style: NaN = detailed occupation, non-NaN = summary group
            df = df[df['occ_group'].isna()].copy()
    # Also filter by SOC code pattern: keep only codes matching XX-XXXX (7 chars with dash)
    if 'soc_code' in df.columns:
        df = df[df['soc_code'].astype(str).str.match(r'^\d{2}-\d{4}$', na=False)].copy()

    # Convert numeric columns
    for col in ['employment', 'median_wage', 'mean_wage', 'median_hourly', 'mean_hourly']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df['year'] = year

    # Select standard columns
    keep_cols = ['soc_code', 'occ_title', 'employment', 'median_wage', 'mean_wage', 'year']
    keep_cols = [c for c in keep_cols if c in df.columns]

    return df[keep_cols].copy()


# Drop 1997 — it uses pre-SOC OES codes that don't map cleanly
# Per the prompt instructions: "inspect carefully... if so, drop it"
print("\n  NOTE: Dropping 1997 OEWS file (uses pre-SOC OES codes, no column headers)")
del oews_files[1997]

oews_dfs = {}
for year, fpath in sorted(oews_files.items()):
    try:
        df = load_oews(year, fpath)
        oews_dfs[year] = df
        n_valid_emp = df['employment'].notna().sum() if 'employment' in df.columns else 0
        n_valid_wage = df['median_wage'].notna().sum() if 'median_wage' in df.columns else 0
        print(f"\n  {year}: {len(df)} detailed occupations, "
              f"{n_valid_emp} with employment, {n_valid_wage} with median wage")
        print(f"    SOC examples: {df['soc_code'].head(3).tolist()}")
        if 'employment' in df.columns:
            total_emp = df['employment'].sum()
            print(f"    Total employment: {total_emp:,.0f}")
    except Exception as e:
        print(f"\n  {year}: ERROR: {e}")

# =============================================================================
# STEP 1b: SOC Harmonization
# =============================================================================
print("\n\n" + "=" * 80)
print("STEP 1b: SOC HARMONIZATION")
print("=" * 80)

# Load SOC 2010 -> 2018 crosswalk from the Census occupation crosswalk file
# (the '2010 to 2018 Crosswalk' sheet in 2018-occupation-code-list-and-crosswalk.xlsx)
xwalk_10_18 = pd.read_excel(
    os.path.join(DATA, 'crosswalks', '2018-occupation-code-list-and-crosswalk.xlsx'),
    sheet_name='2010 to 2018 Crosswalk ',  # note trailing space
    skiprows=3, engine='openpyxl'
)
# The header row has: '2010 SOC code', '2010 Census Code', '2010 Census Title',
#                      '2018 SOC Code', '2018 Census Code', '2018 Census Title'
rename_map = {}
for c in xwalk_10_18.columns:
    cs = str(c).strip()
    if '2010' in cs and 'SOC' in cs:
        rename_map[c] = 'soc_2010'
    elif '2018' in cs and 'SOC' in cs:
        rename_map[c] = 'soc_2018'
    elif '2010' in cs and 'Title' in cs:
        rename_map[c] = 'title_2010'
    elif '2018' in cs and 'Title' in cs:
        rename_map[c] = 'title_2018'
xwalk_10_18 = xwalk_10_18.rename(columns=rename_map)
xwalk_10_18 = xwalk_10_18.dropna(subset=['soc_2010', 'soc_2018'])
xwalk_10_18['soc_2010'] = xwalk_10_18['soc_2010'].astype(str).str.strip()
xwalk_10_18['soc_2018'] = xwalk_10_18['soc_2018'].astype(str).str.strip()

print(f"\nSOC 2010->2018 crosswalk: {len(xwalk_10_18)} rows")

# Identify 1-to-1 mappings
fwd = xwalk_10_18.groupby('soc_2010')['soc_2018'].nunique()
bwd = xwalk_10_18.groupby('soc_2018')['soc_2010'].nunique()
one_to_one_2010 = set(fwd[fwd == 1].index)
one_to_one_2018 = set(bwd[bwd == 1].index)

# Conservative: only keep SOC 2010 codes that map to exactly 1 SOC 2018 code
clean_xwalk = xwalk_10_18[xwalk_10_18['soc_2010'].isin(one_to_one_2010)].copy()
clean_xwalk = clean_xwalk.drop_duplicates(subset=['soc_2010'])

print(f"  Total 2010 codes: {xwalk_10_18['soc_2010'].nunique()}")
print(f"  1-to-1 mappings: {len(clean_xwalk)}")
print(f"  Many-to-many dropped: {xwalk_10_18['soc_2010'].nunique() - len(clean_xwalk)}")

# Build the harmonization table: for each SOC 2018 code, list which 2010 code maps to it
soc_harmonized = clean_xwalk[['soc_2010', 'soc_2018']].copy()
soc_harmonized.to_csv(os.path.join(ANALYSIS, 'soc_2010_to_2018_clean.csv'), index=False)

# For the 1997 and 2005 OEWS files, check if they use SOC 2000 codes
# SOC 2000 and SOC 2010 are very similar for many codes
# For simplicity: try direct matching to SOC 2018 first, then via SOC 2010
print(f"\n  SOC code overlap between OEWS years and SOC 2018:")
onet_socs = set()
with open(os.path.join(DATA, 'onet', 'db_29_1_text', 'Occupation Data.txt'), 'r') as f:
    import csv
    reader = csv.DictReader(f, delimiter='\t')
    for r in reader:
        soc = r['O*NET-SOC Code'].split('.')[0]  # strip .00 suffix
        onet_socs.add(soc)

print(f"  O*NET SOC 2018 codes: {len(onet_socs)}")

for year in sorted(oews_dfs.keys()):
    df = oews_dfs[year]
    oews_socs = set(df['soc_code'].dropna().unique())

    # Direct match to O*NET
    direct_match = oews_socs & onet_socs

    # Via 2010->2018 crosswalk
    via_xwalk = set()
    for soc in oews_socs:
        mapped = clean_xwalk[clean_xwalk['soc_2010'] == soc]['soc_2018']
        if len(mapped) > 0:
            via_xwalk.add(mapped.iloc[0])

    combined = direct_match | via_xwalk

    # Compute employment coverage
    matched_emp = df[df['soc_code'].isin(direct_match) |
                     df['soc_code'].isin(clean_xwalk['soc_2010'])]['employment'].sum()
    total_emp = df['employment'].sum()
    pct = matched_emp / total_emp * 100 if total_emp > 0 else 0

    print(f"  {year}: {len(oews_socs)} OEWS codes, {len(direct_match)} direct O*NET match, "
          f"{len(via_xwalk)} via crosswalk, {pct:.1f}% employment covered")

# =============================================================================
# STEP 1c: Load O*NET Work Activities (GWA Importance scores)
# =============================================================================
print("\n\n" + "=" * 80)
print("STEP 1c: O*NET WORK ACTIVITIES")
print("=" * 80)

wa_df = pd.read_csv(os.path.join(DATA, 'onet', 'db_29_1_text', 'Work Activities.txt'), sep='\t')

# Filter to Importance scale only
wa_im = wa_df[wa_df['Scale ID'] == 'IM'].copy()
wa_im['soc_code'] = wa_im['O*NET-SOC Code'].str.split('.').str[0]

# Pivot to matrix: rows = SOC codes, columns = GWAs
gwa_matrix = wa_im.pivot_table(
    index='soc_code',
    columns='Element Name',
    values='Data Value',
    aggfunc='mean'  # Average across sub-SOCs (e.g., 11-1011.00 and 11-1011.03)
)

print(f"  GWA importance matrix: {gwa_matrix.shape[0]} occupations × {gwa_matrix.shape[1]} GWAs")
print(f"  GWA names: {list(gwa_matrix.columns)[:5]}... (total {len(gwa_matrix.columns)})")
print(f"  Missing values: {gwa_matrix.isna().sum().sum()}")

gwa_matrix.to_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'))

# =============================================================================
# STEP 1d: Load O*NET Skills (Importance scores)
# =============================================================================
print("\n\n" + "=" * 80)
print("STEP 1d: O*NET SKILLS")
print("=" * 80)

skills_df = pd.read_csv(os.path.join(DATA, 'onet', 'db_29_1_text', 'Skills.txt'), sep='\t')
skills_im = skills_df[skills_df['Scale ID'] == 'IM'].copy()
skills_im['soc_code'] = skills_im['O*NET-SOC Code'].str.split('.').str[0]

skill_matrix = skills_im.pivot_table(
    index='soc_code',
    columns='Element Name',
    values='Data Value',
    aggfunc='mean'
)

print(f"  Skill importance matrix: {skill_matrix.shape[0]} occupations × {skill_matrix.shape[1]} skills")
print(f"  Skill names: {list(skill_matrix.columns)[:5]}... (total {len(skill_matrix.columns)})")

skill_matrix.to_csv(os.path.join(ANALYSIS, 'onet_skill_importance_matrix.csv'))

# =============================================================================
# STEP 1e: Load Felten AIOE scores
# =============================================================================
print("\n\n" + "=" * 80)
print("STEP 1e: FELTEN AIOE SCORES")
print("=" * 80)

aioe_df = pd.read_excel(
    os.path.join(DATA, 'ai-exposure', 'AIOE_DataAppendix.xlsx'),
    sheet_name='Appendix A', skiprows=1, engine='openpyxl'
)
# Standardize columns
aioe_cols = list(aioe_df.columns)
aioe_df.columns = ['soc_code', 'occ_title', 'aioe_score'] + aioe_cols[3:]
aioe_df = aioe_df[['soc_code', 'aioe_score']].dropna()
aioe_df['soc_code'] = aioe_df['soc_code'].astype(str).str.strip()

print(f"  AIOE scores: {len(aioe_df)} occupations")
print(f"  Score range: {aioe_df['aioe_score'].min():.3f} to {aioe_df['aioe_score'].max():.3f}")
print(f"  Mean: {aioe_df['aioe_score'].mean():.3f}, Median: {aioe_df['aioe_score'].median():.3f}")

# =============================================================================
# STEP 1f: Build master panel
# =============================================================================
print("\n\n" + "=" * 80)
print("STEP 1f: BUILDING MASTER PANEL")
print("=" * 80)

# Strategy:
# - For each OEWS year, map SOC codes to SOC 2018 (via crosswalk if needed)
# - Merge with O*NET GWA matrix, skill matrix, and AIOE scores
# - Stack all years into a panel

def harmonize_soc(soc, year):
    """Map a SOC code to SOC 2018. Returns SOC 2018 code or None."""
    soc = str(soc).strip()
    # If already in O*NET (SOC 2018), use directly
    if soc in onet_socs:
        return soc
    # Try crosswalk from SOC 2010 → 2018
    match = clean_xwalk[clean_xwalk['soc_2010'] == soc]
    if len(match) > 0:
        return match.iloc[0]['soc_2018']
    return None

panels = []
for year in sorted(oews_dfs.keys()):
    df = oews_dfs[year].copy()

    # Harmonize SOC codes
    df['soc_2018'] = df['soc_code'].apply(lambda s: harmonize_soc(s, year))

    # Drop unmapped
    n_before = len(df)
    df = df.dropna(subset=['soc_2018'])
    n_after = len(df)

    # Merge with GWA matrix
    df = df.merge(gwa_matrix, left_on='soc_2018', right_index=True, how='inner')
    n_with_gwa = len(df)

    # Merge with skill matrix
    df = df.merge(skill_matrix, left_on='soc_2018', right_index=True, how='left', suffixes=('', '_skill'))

    # Merge with AIOE
    df = df.merge(aioe_df[['soc_code', 'aioe_score']],
                  left_on='soc_2018', right_on='soc_code', how='left', suffixes=('', '_aioe'))
    if 'soc_code_aioe' in df.columns:
        df = df.drop(columns=['soc_code_aioe'])

    # Filter: employment >= 1000
    if 'employment' in df.columns:
        emp_before = df['employment'].sum()
        df = df[df['employment'] >= 1000]
        emp_after = df['employment'].sum()

        print(f"  {year}: {n_before} OEWS → {n_after} SOC-harmonized → {n_with_gwa} with GWA → "
              f"{len(df)} with emp≥1000 ({emp_after/emp_before*100:.1f}% of employment, "
              f"AIOE coverage: {df['aioe_score'].notna().mean()*100:.1f}%)")

    panels.append(df)

master = pd.concat(panels, ignore_index=True)

# Rename soc_2018 to just soc_code for clarity
if 'soc_2018' in master.columns:
    master = master.rename(columns={'soc_2018': 'soc_2018_harmonized'})

print(f"\n  MASTER PANEL: {master.shape[0]} rows × {master.shape[1]} columns")
print(f"  Years: {sorted(master['year'].unique())}")
print(f"  Unique SOC codes: {master['soc_2018_harmonized'].nunique()}")

# Save
master_path = os.path.join(ANALYSIS, 'master_panel.csv')
master.to_csv(master_path, index=False)
print(f"\n  Saved to {master_path}")
print(f"  File size: {os.path.getsize(master_path) / 1e6:.1f} MB")

# Summary: which occupations are present in ALL years?
all_years = sorted(master['year'].unique())
soc_by_year = {y: set(master[master['year'] == y]['soc_2018_harmonized']) for y in all_years}

in_all_years = set.intersection(*soc_by_year.values())
print(f"\n  Occupations present in ALL {len(all_years)} years: {len(in_all_years)}")

for n_years in range(len(all_years), 0, -1):
    from itertools import combinations
    for combo in combinations(all_years, n_years):
        in_combo = set.intersection(*[soc_by_year[y] for y in combo])
        if len(in_combo) > 0:
            print(f"  Occupations in {n_years} years ({combo[0]}-{combo[-1]}): {len(in_combo)}")
            break

print("\n" + "=" * 80)
print("PHASE 1 COMPLETE")
print("=" * 80)
