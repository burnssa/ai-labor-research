"""
Specification vs Execution: Empirical Derivation from Firm Structure
=====================================================================
Uses CPS employer-size data to identify tasks characteristic of small/new
firms (specification-heavy by construction) vs large/mature firms (more
execution-heavy), then scores all occupations on this dimension and tracks
employment shifts.

Approach:
  1. From CPS 2024: compare occupational mix at small firms (<25 emp) vs
     large firms (500+ emp). Small firms are more likely young and
     entrepreneurial — their workers are closer to the "deciding what to
     produce" layer.
  2. Map CPS occupations to O*NET task profiles via crosswalks.
  3. Compute: which GWAs/tasks are disproportionately important at small
     firms vs large firms? This is the "specification gradient" derived
     from firm structure, not from researcher judgment.
  4. Score all occupations on this gradient.
  5. Track employment shifts along this gradient over time (using OEWS).

Also: contrast self-employed + management (SOC 11-XXXX) vs non-managerial
occupations as a complementary specification proxy.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# =============================================================================
# Step 1: Load CPS 2024 with employer size and occupation
# =============================================================================
print("=" * 80)
print("STEP 1: LOAD CPS WITH EMPLOYER SIZE")
print("=" * 80)

cps = pd.read_csv(os.path.join(DATA, 'cps-asec', 'csv', '2024', 'pppub24.csv'),
                   usecols=['A_CLSWKR', 'NOEMP', 'PEIOOCC', 'PEIOIND', 'MARSUPWT',
                            'WSAL_VAL', 'A_MJOCC', 'A_AGE', 'ERN_VAL'])

# Filter to employed workers
employed = cps[cps['A_CLSWKR'].isin([1, 2, 3, 4, 5])].copy()
print(f"Employed workers: {len(employed)}")

# NOEMP coding (employer size):
# 0 = Not in universe, 1 = Under 10, 2 = 10-24, 3 = 25-99,
# 4 = 100-499, 5 = 500-999, 6 = 1000+
NOEMP_LABELS = {0: 'N/A', 1: '<10', 2: '10-24', 3: '25-99',
                4: '100-499', 5: '500-999', 6: '1000+'}

# Define firm size groups
employed['firm_size'] = 'other'
employed.loc[employed['NOEMP'].isin([1, 2]), 'firm_size'] = 'small'  # <25 employees
employed.loc[employed['NOEMP'].isin([5, 6]), 'firm_size'] = 'large'  # 500+
employed.loc[employed['A_CLSWKR'] == 5, 'firm_size'] = 'self_employed'

print(f"\nFirm size distribution:")
for fs in ['self_employed', 'small', 'large', 'other']:
    n = (employed['firm_size'] == fs).sum()
    wt = employed[employed['firm_size'] == fs]['MARSUPWT'].sum()
    print(f"  {fs:>15}: {n:>6} unweighted, {wt:>15,.0f} weighted")

# =============================================================================
# Step 2: Map CPS occupation codes to SOC 2018 (for O*NET merge)
# =============================================================================
print("\n" + "=" * 80)
print("STEP 2: MAP CPS OCCUPATIONS TO SOC 2018")
print("=" * 80)

# Load Census 2018 → SOC crosswalk
import openpyxl
wb = openpyxl.load_workbook(os.path.join(DATA, 'crosswalks',
                            '2018-occupation-code-list-and-crosswalk.xlsx'))
ws = wb['2018 Census Occ Code List']

census_to_soc = {}
for row in ws.iter_rows(min_row=5, values_only=True):
    title, census_code, soc_code = row[1], row[2], row[3]
    if census_code is not None and soc_code is not None:
        census_str = str(census_code).strip().zfill(4)
        soc_str = str(soc_code).strip()
        if len(soc_str) >= 7 and '-' in soc_str:
            census_to_soc[census_str] = soc_str

print(f"Census-to-SOC mappings: {len(census_to_soc)}")

# Map CPS PEIOOCC (Census occ code) to SOC
employed['census_occ'] = employed['PEIOOCC'].astype(str).str.strip().str.zfill(4)
employed['soc_code'] = employed['census_occ'].map(census_to_soc)

match_rate = employed['soc_code'].notna().mean()
print(f"CPS occupation → SOC match rate: {match_rate:.1%}")

# =============================================================================
# Step 3: Compute weighted occupational mix by firm size group
# =============================================================================
print("\n" + "=" * 80)
print("STEP 3: OCCUPATIONAL MIX BY FIRM SIZE")
print("=" * 80)

# Load O*NET GWA matrix
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
gwa_cols = list(gwa_matrix.columns)

# For each firm-size group, compute employment-weighted mean GWA importance
# by linking CPS person → SOC → O*NET GWA profile

# Merge O*NET profiles onto CPS records
employed_with_gwa = employed[employed['soc_code'].notna()].merge(
    gwa_matrix, left_on='soc_code', right_index=True, how='inner')

print(f"CPS records with O*NET GWA data: {len(employed_with_gwa)}")

def weighted_mean_profile(df, cols, weight_col='MARSUPWT'):
    w = df[weight_col].fillna(0)
    total = w.sum()
    if total == 0:
        return pd.Series({c: np.nan for c in cols})
    return pd.Series({c: (df[c] * w).sum() / total for c in cols})

# Compute profiles for each firm-size group
profiles = {}
for fs in ['self_employed', 'small', 'large']:
    fsdf = employed_with_gwa[employed_with_gwa['firm_size'] == fs]
    profiles[fs] = weighted_mean_profile(fsdf, gwa_cols)
    print(f"  {fs}: {len(fsdf)} records, weighted pop = {fsdf['MARSUPWT'].sum():,.0f}")

# =============================================================================
# Step 4: Compute "small-firm premium" for each GWA
# =============================================================================
print("\n" + "=" * 80)
print("STEP 4: SMALL-FIRM vs LARGE-FIRM GWA CONTRAST")
print("=" * 80)

# Small+self vs large — which GWAs characterize small/entrepreneurial firms?
small_profile = weighted_mean_profile(
    employed_with_gwa[employed_with_gwa['firm_size'].isin(['self_employed', 'small'])], gwa_cols)
large_profile = profiles['large']

diff = small_profile - large_profile
diff_df = pd.DataFrame({
    'small_firm': small_profile,
    'large_firm': large_profile,
    'difference': diff,
}).sort_values('difference', ascending=False)

# Statistical significance
pvals = {}
for gwa in gwa_cols:
    small_vals = employed_with_gwa[employed_with_gwa['firm_size'].isin(['self_employed', 'small'])][gwa]
    large_vals = employed_with_gwa[employed_with_gwa['firm_size'] == 'large'][gwa]
    if len(small_vals) > 30 and len(large_vals) > 30:
        _, p = stats.mannwhitneyu(small_vals.dropna(), large_vals.dropna(), alternative='two-sided')
        pvals[gwa] = p

diff_df['p_value'] = diff_df.index.map(pvals)
diff_df['significant'] = diff_df['p_value'] < 0.05

print(f"\nGWAs ranked by Small+Self-Employed minus Large-Firm importance:")
print(f"{'GWA':<55} {'Small':>6} {'Large':>6} {'Diff':>7} {'p':>8} {'Sig':>4}")
print("-" * 90)
for gwa, row in diff_df.iterrows():
    sig = '***' if row['p_value'] < 0.001 else ('**' if row['p_value'] < 0.01 else
           ('*' if row['p_value'] < 0.05 else ''))
    print(f"{gwa:<55} {row['small_firm']:6.3f} {row['large_firm']:6.3f} "
          f"{row['difference']:+7.4f} {row['p_value']:8.4f} {sig:>4}")

diff_df.to_csv(os.path.join(ANALYSIS, 'gwa_small_vs_large_firm.csv'))

# =============================================================================
# Step 5: Score occupations and track employment over time
# =============================================================================
print("\n" + "=" * 80)
print("STEP 5: SCORE OCCUPATIONS AND TRACK OVER TIME")
print("=" * 80)

# Use the small-large difference as weights for a "small-firm profile" composite
spec_weights = diff_df['difference']

master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
years = sorted(master['year'].unique())

def compute_composite(row, gwa_cols, weights):
    vals = row[gwa_cols]
    w = weights.reindex(gwa_cols).fillna(0)
    return (vals * w).sum() / w.abs().sum()

master['small_firm_score'] = master.apply(
    lambda row: compute_composite(row, gwa_cols, spec_weights), axis=1)

# Track employment-weighted mean score over time
print(f"\nEmployment-weighted mean 'small-firm profile score' over time:")
print(f"(Higher = occupation task profile matches small/entrepreneurial firm pattern)")
for year in years:
    ydf = master[(master['year'] == year) & master['employment'].notna()]
    w = ydf['employment']
    wmean = (ydf['small_firm_score'] * w).sum() / w.sum()
    print(f"  {year}: {wmean:.4f}")

# Tercile-based employment shares
ref = master[master['year'] == years[-1]]
cuts = ref['small_firm_score'].quantile([1/3, 2/3]).values

tercile_data = []
for year in years:
    ydf = master[(master['year'] == year) & master['employment'].notna() &
                  master['small_firm_score'].notna()]
    total = ydf['employment'].sum()
    top = ydf[ydf['small_firm_score'] > cuts[1]]['employment'].sum() / total
    bottom = ydf[ydf['small_firm_score'] < cuts[0]]['employment'].sum() / total
    middle = 1 - top - bottom
    tercile_data.append({'year': year, 'top_spec': top, 'middle': middle, 'bottom_exec': bottom, 'total': total})

tdf = pd.DataFrame(tercile_data)
tdf.to_csv(os.path.join(ANALYSIS, 'small_firm_profile_employment_shares.csv'), index=False)

print(f"\nEmployment share by small-firm-profile tercile:")
print(f"{'Year':>6} {'Top (small-firm)':>18} {'Middle':>10} {'Bottom (large-firm)':>20}")
for _, row in tdf.iterrows():
    print(f"{int(row['year']):>6} {row['top_spec']:>18.1%} {row['middle']:>10.1%} {row['bottom_exec']:>20.1%}")

# =============================================================================
# Step 6: Charts
# =============================================================================
print("\n" + "=" * 80)
print("STEP 6: CHARTS")
print("=" * 80)

# Chart 1: Small vs Large firm GWA contrast
fig, ax = plt.subplots(figsize=(14, 16))

colors = ['#C62828' if d > 0 else '#1565C0' for d in diff_df['difference']]
ax.barh(range(len(diff_df)), diff_df['difference'], color=colors, alpha=0.85, height=0.7)
ax.set_yticks(range(len(diff_df)))
ax.set_yticklabels(diff_df.index, fontsize=8.5)

for i, (gwa, row) in enumerate(diff_df.iterrows()):
    val = row['difference']
    sig = '***' if row['p_value'] < 0.001 else ('**' if row['p_value'] < 0.01 else
           ('*' if row['p_value'] < 0.05 else ''))
    if abs(val) > 0.005:
        if val > 0:
            ax.text(val + 0.003, i, f'{val:+.3f}  ({row["small_firm"]:.2f} vs {row["large_firm"]:.2f}) {sig}',
                    fontsize=7, va='center', ha='left', color='#333')
        else:
            ax.text(val - 0.003, i, f'{val:+.3f}  ({row["large_firm"]:.2f} vs {row["small_firm"]:.2f}) {sig}',
                    fontsize=7, va='center', ha='right', color='#333')

ax.axvline(x=0, color='black', linewidth=0.8)
ax.grid(True, axis='x', alpha=0.2)
ax.set_xlabel('Difference in Employment-Weighted GWA Importance\n'
              'Small+Self-Employed (<25 emp) minus Large Firms (500+ emp)',
              fontsize=10)
ax.set_title('Which Tasks Characterize Small/Entrepreneurial vs Large Firms?\n'
             '(CPS 2024, weighted by employment)',
             fontsize=13, fontweight='bold', pad=15)

textstr = (
    'Small firms (<25 employees) + self-employed\n'
    'vs Large firms (500+ employees)\n'
    'from CPS ASEC 2024 person-level data\n\n'
    'Red = more important at small/entrepreneurial firms\n'
    'Blue = more important at large firms\n\n'
    '*** p<0.001  ** p<0.01  * p<0.05'
)
props = dict(boxstyle='round,pad=0.8', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9)
ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=7.5,
        va='bottom', ha='right', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'spec_small_vs_large_firm_gwas.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Saved: spec_small_vs_large_firm_gwas.png")

# Chart 2: Employment shift along small-firm-profile dimension
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(tdf['year'], tdf['top_spec'] * tdf['total'] / 1e6, '-o', color='#C62828',
        linewidth=2, markersize=5, label='Top tercile (small-firm profile)')
ax.plot(tdf['year'], tdf['bottom_exec'] * tdf['total'] / 1e6, '-s', color='#1565C0',
        linewidth=2, markersize=5, label='Bottom tercile (large-firm profile)')
ax.set_ylabel('Employment (millions)', fontsize=11)
ax.set_xlabel('Year', fontsize=11)
ax.set_title('Employment in Occupations with Small-Firm vs Large-Firm Task Profiles\n'
             '(scored by empirical GWA contrast: small+self-employed vs 500+ employee firms)',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

textstr2 = (
    'Task profile derived from CPS 2024:\n'
    'which GWAs are more important at small firms\n'
    '(<25 emp + self-employed) vs large firms (500+).\n'
    'Occupations scored on this contrast, then\n'
    'employment tracked over time via OEWS.'
)
ax.text(0.02, 0.98, textstr2, transform=ax.transAxes, fontsize=7.5,
        va='top', ha='left', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'spec_employment_shift_firm_derived.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: spec_employment_shift_firm_derived.png")

# =============================================================================
# Step 7: Compare the two approaches
# =============================================================================
print("\n" + "=" * 80)
print("STEP 7: CORRELATION WITH GROWTH-PROFILE APPROACH")
print("=" * 80)

# Load the Phase 2c growth-profile scores for comparison
growth_scores = pd.read_csv(os.path.join(ANALYSIS, 'occupation_growth_profile_scores.csv'))

# Merge with small-firm scores
ref_scores = master[master['year'] == years[-1]][['soc_2018_harmonized', 'small_firm_score']].dropna()
ref_scores = ref_scores.drop_duplicates(subset='soc_2018_harmonized')

comparison = growth_scores.merge(ref_scores, on='soc_2018_harmonized', how='inner')

if len(comparison) > 0:
    r, p = stats.spearmanr(comparison['growth_profile_score'], comparison['small_firm_score'])
    print(f"Spearman correlation between growth-profile score and small-firm-profile score:")
    print(f"  r = {r:.3f}, p = {p:.2e}")
    print(f"  (positive = occupations that LOOK LIKE small-firm work also GROW faster)")
    print(f"  n = {len(comparison)} occupations")

print("\n" + "=" * 80)
print("COMPLETE")
print("=" * 80)
