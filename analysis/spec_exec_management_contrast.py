"""
Specification vs Execution: Management Contrast Approach
==========================================================
Defines the specification-execution axis empirically by contrasting
C-suite/director-level occupations (SOC 11-XXXX) against non-managerial
occupations in the same broad fields.

The logic: managers and directors are, by construction, the people who
decide WHAT to produce. Their task profile reveals what specification
labor looks like. Non-managerial workers in the same fields do more
execution. The GWAs that differentiate them define the spec-exec gradient.

Then: is the economy shifting employment toward occupations that score
higher on this management-derived specification gradient?

Steps:
  1. Split O*NET occupations into management (SOC 11-XXXX) vs non-management
  2. Compute GWA contrast (management minus non-management)
  3. Score all occupations on this "management task gradient"
  4. Track employment-weighted score over time
  5. Test: controlling for overall complexity (PC1), is the management-
     specific component growing?
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# Load data
master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
gwa_cols = list(gwa_matrix.columns)
years = sorted(master['year'].unique())
first_year, last_year = years[0], years[-1]

# Load occupation data for titles
import csv
occ_names = {}
with open(os.path.join(DATA, 'onet', 'db_29_1_text', 'Occupation Data.txt'), 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for r in reader:
        soc = r['O*NET-SOC Code'].split('.')[0]
        occ_names[soc] = r['Title']

# =============================================================================
# Step 1: Split into management vs non-management
# =============================================================================
print("=" * 80)
print("STEP 1: MANAGEMENT vs NON-MANAGEMENT SPLIT")
print("=" * 80)

# SOC 11-XXXX = Management Occupations
# These are the C-suite, directors, and managers
mgmt_socs = [soc for soc in gwa_matrix.index if soc.startswith('11-')]
non_mgmt_socs = [soc for soc in gwa_matrix.index if not soc.startswith('11-')]

print(f"Management occupations (SOC 11-XXXX): {len(mgmt_socs)}")
print(f"Non-management occupations: {len(non_mgmt_socs)}")

# Show what's in the management category
print(f"\nManagement occupations include:")
for soc in sorted(mgmt_socs)[:15]:
    print(f"  {soc}  {occ_names.get(soc, 'Unknown')}")
print(f"  ... and {len(mgmt_socs) - 15} more")

# =============================================================================
# Step 2: Compute GWA contrast
# =============================================================================
print("\n" + "=" * 80)
print("STEP 2: MANAGEMENT vs NON-MANAGEMENT GWA CONTRAST")
print("=" * 80)

mgmt_profile = gwa_matrix.loc[mgmt_socs].mean()
non_mgmt_profile = gwa_matrix.loc[non_mgmt_socs].mean()
diff = mgmt_profile - non_mgmt_profile

diff_df = pd.DataFrame({
    'management': mgmt_profile,
    'non_management': non_mgmt_profile,
    'difference': diff,
}).sort_values('difference', ascending=False)

# Statistical tests
pvals = {}
for gwa in gwa_cols:
    m_vals = gwa_matrix.loc[mgmt_socs, gwa].dropna()
    nm_vals = gwa_matrix.loc[non_mgmt_socs, gwa].dropna()
    if len(m_vals) > 5 and len(nm_vals) > 5:
        _, p = stats.mannwhitneyu(m_vals, nm_vals, alternative='two-sided')
        pvals[gwa] = p

diff_df['p_value'] = diff_df.index.map(pvals)
diff_df['significant'] = diff_df['p_value'] < 0.05

print(f"\nGWAs ranked by Management minus Non-Management importance:")
print(f"{'GWA':<55} {'Mgmt':>6} {'Non-M':>6} {'Diff':>7} {'p':>8} {'Sig':>4}")
print("-" * 90)
for gwa, row in diff_df.iterrows():
    sig = '***' if row['p_value'] < 0.001 else ('**' if row['p_value'] < 0.01 else
           ('*' if row['p_value'] < 0.05 else ''))
    print(f"{gwa:<55} {row['management']:6.3f} {row['non_management']:6.3f} "
          f"{row['difference']:+7.3f} {row['p_value']:8.4f} {sig:>4}")

diff_df.to_csv(os.path.join(ANALYSIS, 'gwa_management_vs_nonmanagement.csv'))

# =============================================================================
# Step 3: Score all occupations on management-task gradient
# =============================================================================
print("\n" + "=" * 80)
print("STEP 3: SCORE ALL OCCUPATIONS")
print("=" * 80)

# Use management-contrast weights
spec_weights = diff_df['difference']

def compute_composite(row, gwa_cols, weights):
    vals = row[gwa_cols]
    w = weights.reindex(gwa_cols).fillna(0)
    return (vals * w).sum() / w.abs().sum()

master['mgmt_spec_score'] = master.apply(
    lambda row: compute_composite(row, gwa_cols, spec_weights), axis=1)

# Show the score distribution and top/bottom occupations
ref = master[master['year'] == last_year].copy()

print(f"\nManagement-specification score distribution ({last_year}):")
print(f"  Mean: {ref['mgmt_spec_score'].mean():.4f}")
print(f"  Median: {ref['mgmt_spec_score'].median():.4f}")
print(f"  Std: {ref['mgmt_spec_score'].std():.4f}")

print(f"\nTop 15 occupations (most management-like task profile):")
for _, row in ref.nlargest(15, 'mgmt_spec_score').iterrows():
    soc = row['soc_2018_harmonized']
    print(f"  {row['mgmt_spec_score']:.3f}  {row['occ_title'][:60]:<60}  emp={row['employment']:>10,.0f}")

print(f"\nBottom 15 occupations (least management-like task profile):")
for _, row in ref.nsmallest(15, 'mgmt_spec_score').iterrows():
    print(f"  {row['mgmt_spec_score']:.3f}  {row['occ_title'][:60]:<60}  emp={row['employment']:>10,.0f}")

# Sanity check: do the SOC 11-XXXX occupations actually score highest?
mgmt_in_ref = ref[ref['soc_2018_harmonized'].str.startswith('11-')]
non_mgmt_in_ref = ref[~ref['soc_2018_harmonized'].str.startswith('11-')]
print(f"\nSanity check:")
print(f"  Mean score for SOC 11-XXXX (management): {mgmt_in_ref['mgmt_spec_score'].mean():.4f}")
print(f"  Mean score for non-management: {non_mgmt_in_ref['mgmt_spec_score'].mean():.4f}")

# =============================================================================
# Step 4: Track employment-weighted score over time
# =============================================================================
print("\n" + "=" * 80)
print("STEP 4: EMPLOYMENT TRENDS ALONG MANAGEMENT-SPEC GRADIENT")
print("=" * 80)

# Exclude SOC 11-XXXX from the tracking — we want to know if
# NON-MANAGEMENT occupations are becoming more management-like in their tasks
print("\nA) ALL occupations (including management):")
for year in years:
    ydf = master[(master['year'] == year) & master['employment'].notna()]
    w = ydf['employment']
    wmean = (ydf['mgmt_spec_score'] * w).sum() / w.sum()
    total = w.sum()
    print(f"  {year}: mean score = {wmean:.4f}  (total emp = {total:,.0f})")

print("\nB) NON-MANAGEMENT occupations only (excluding SOC 11-XXXX):")
for year in years:
    ydf = master[(master['year'] == year) & master['employment'].notna() &
                  ~master['soc_2018_harmonized'].str.startswith('11-')]
    w = ydf['employment']
    wmean = (ydf['mgmt_spec_score'] * w).sum() / w.sum()
    total = w.sum()
    print(f"  {year}: mean score = {wmean:.4f}  (non-mgmt emp = {total:,.0f})")

# Tercile-based employment tracking
cuts = ref['mgmt_spec_score'].quantile([1/3, 2/3]).values

tercile_data = []
for year in years:
    ydf = master[(master['year'] == year) & master['employment'].notna() &
                  master['mgmt_spec_score'].notna()]
    total = ydf['employment'].sum()
    top = ydf[ydf['mgmt_spec_score'] > cuts[1]]['employment'].sum()
    bottom = ydf[ydf['mgmt_spec_score'] < cuts[0]]['employment'].sum()
    middle = total - top - bottom
    tercile_data.append({
        'year': year,
        'top_spec': top / total,
        'middle': middle / total,
        'bottom_exec': bottom / total,
        'top_emp': top,
        'bottom_emp': bottom,
        'total': total,
    })

tdf = pd.DataFrame(tercile_data)
tdf.to_csv(os.path.join(ANALYSIS, 'mgmt_spec_employment_shares.csv'), index=False)

print(f"\nEmployment share by management-spec tercile:")
print(f"{'Year':>6} {'Top (spec)':>12} {'Middle':>10} {'Bottom (exec)':>15} {'Top Emp(M)':>12} {'Bot Emp(M)':>12}")
print("-" * 70)
for _, row in tdf.iterrows():
    print(f"{int(row['year']):>6} {row['top_spec']:>12.1%} {row['middle']:>10.1%} "
          f"{row['bottom_exec']:>15.1%} {row['top_emp']/1e6:>12.1f} {row['bottom_emp']/1e6:>12.1f}")

# =============================================================================
# Step 5: Decompose — complexity vs specification-specific
# =============================================================================
print("\n" + "=" * 80)
print("STEP 5: CONTROLLING FOR COMPLEXITY (PC1)")
print("=" * 80)

# Load PCA
scaler = StandardScaler()
X = scaler.fit_transform(gwa_matrix.dropna())
pca = PCA()
pca.fit(X)

occ_pca = pd.DataFrame(
    pca.transform(X),
    index=gwa_matrix.dropna().index,
    columns=[f'PC{i+1}' for i in range(X.shape[1])]
)

# The management contrast vector in GWA space
mgmt_vec = spec_weights.reindex(gwa_cols).fillna(0).values
mgmt_vec_std = mgmt_vec / scaler.scale_
mgmt_in_pc = pca.transform(mgmt_vec_std.reshape(1, -1))[0]

print(f"Management contrast vector projected onto PCs:")
for i in range(5):
    print(f"  PC{i+1}: {mgmt_in_pc[i]:+.3f} ({pca.explained_variance_ratio_[i]*100:.1f}% var)")

# The management contrast loads heavily on PC1 (complexity).
# To test whether spec-specific tasks are growing BEYOND just complexity,
# we need to residualize.

# For each occupation, compute:
#   - PC1 score (complexity)
#   - Management spec score
#   - Residual spec score = spec score after partialing out PC1

master_with_pc = master.merge(occ_pca[['PC1']], left_on='soc_2018_harmonized',
                               right_index=True, how='left', suffixes=('', '_pca'))
if 'PC1_pca' in master_with_pc.columns:
    master_with_pc = master_with_pc.rename(columns={'PC1_pca': 'pc1_score'})
elif 'PC1' in master_with_pc.columns and 'pc1_score' not in master_with_pc.columns:
    master_with_pc = master_with_pc.rename(columns={'PC1': 'pc1_score'})

# Residualize: regress mgmt_spec_score on pc1_score, take residuals
from numpy.polynomial import polynomial as P

valid = master_with_pc[(master_with_pc['year'] == last_year) &
                        master_with_pc['mgmt_spec_score'].notna() &
                        master_with_pc['pc1_score'].notna()]

slope, intercept = np.polyfit(valid['pc1_score'], valid['mgmt_spec_score'], 1)
print(f"\nRegression: mgmt_spec_score = {intercept:.4f} + {slope:.4f} * PC1")
print(f"  R² = {np.corrcoef(valid['pc1_score'], valid['mgmt_spec_score'])[0,1]**2:.3f}")

master_with_pc['spec_residual'] = master_with_pc['mgmt_spec_score'] - (intercept + slope * master_with_pc['pc1_score'])

print(f"\nEmployment-weighted trends AFTER controlling for complexity:")
print(f"{'Year':>6} {'Complexity(PC1)':>16} {'Mgmt Spec':>11} {'Spec Residual':>15}")
print("-" * 50)
for year in years:
    ydf = master_with_pc[(master_with_pc['year'] == year) & master_with_pc['employment'].notna()]
    w = ydf['employment']
    pc1_mean = (ydf['pc1_score'] * w).sum() / w.sum()
    spec_mean = (ydf['mgmt_spec_score'] * w).sum() / w.sum()
    resid_mean = (ydf['spec_residual'] * w).sum() / w.sum()
    print(f"{year:>6} {pc1_mean:>16.4f} {spec_mean:>11.4f} {resid_mean:>15.4f}")

# =============================================================================
# Step 6: Charts
# =============================================================================
print("\n" + "=" * 80)
print("STEP 6: CHARTS")
print("=" * 80)

# Chart 1: Management vs non-management GWA contrast (bar chart)
fig, ax = plt.subplots(figsize=(14, 16))
colors = ['#C62828' if d > 0 else '#1565C0' for d in diff_df['difference']]
ax.barh(range(len(diff_df)), diff_df['difference'], color=colors, alpha=0.85, height=0.7)
ax.set_yticks(range(len(diff_df)))
ax.set_yticklabels(diff_df.index, fontsize=8.5)

for i, (gwa, row) in enumerate(diff_df.iterrows()):
    val = row['difference']
    sig = '***' if row['p_value'] < 0.001 else ('**' if row['p_value'] < 0.01 else
           ('*' if row['p_value'] < 0.05 else ''))
    if abs(val) > 0.01:
        if val > 0:
            ax.text(val + 0.01, i, f'{val:+.2f}  ({row["management"]:.1f} vs {row["non_management"]:.1f}) {sig}',
                    fontsize=7, va='center', ha='left', color='#333')
        else:
            ax.text(val - 0.01, i, f'{val:+.2f}  ({row["non_management"]:.1f} vs {row["management"]:.1f}) {sig}',
                    fontsize=7, va='center', ha='right', color='#333')

ax.axvline(x=0, color='black', linewidth=0.8)
ax.grid(True, axis='x', alpha=0.2)
ax.set_xlabel('Difference in Mean GWA Importance (1-5 scale)\n'
              'Management (SOC 11-XXXX) minus Non-Management', fontsize=10)
ax.set_title('The Specification-Execution Gradient:\n'
             'What Tasks Differentiate Management from Non-Management Occupations?',
             fontsize=13, fontweight='bold', pad=15)

textstr = (
    'Management = SOC 11-XXXX (C-suite, directors,\n'
    '  and managers across all fields)\n'
    'Non-Management = all other SOC codes\n\n'
    'Red = more important for MANAGEMENT\n'
    'Blue = more important for NON-MANAGEMENT\n\n'
    'Management occupations decide WHAT to produce;\n'
    'their distinctive tasks define the\n'
    '"specification" end of the gradient.\n\n'
    '*** p<0.001  ** p<0.01  * p<0.05'
)
props = dict(boxstyle='round,pad=0.8', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9)
ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=7.5,
        va='bottom', ha='right', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'spec_mgmt_vs_nonmgmt_gwas.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Saved: spec_mgmt_vs_nonmgmt_gwas.png")

# Chart 2: Employment trends — raw and residualized
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Panel 1: Raw employment in top vs bottom tercile
ax1 = axes[0]
ax1.plot(tdf['year'], tdf['top_emp'] / 1e6, '-o', color='#C62828', linewidth=2,
         markersize=5, label='Top tercile (most management-like tasks)')
ax1.plot(tdf['year'], tdf['bottom_emp'] / 1e6, '-s', color='#1565C0', linewidth=2,
         markersize=5, label='Bottom tercile (least management-like tasks)')
ax1.set_ylabel('Employment (millions)', fontsize=11)
ax1.set_title('Is the Economy Shifting Toward Management-Like (Specification) Tasks?',
              fontsize=13, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: Decomposed trends
ax2 = axes[1]
trend_data = []
for year in years:
    ydf = master_with_pc[(master_with_pc['year'] == year) & master_with_pc['employment'].notna()]
    w = ydf['employment']
    pc1_mean = (ydf['pc1_score'] * w).sum() / w.sum()
    spec_mean = (ydf['mgmt_spec_score'] * w).sum() / w.sum()
    resid_mean = (ydf['spec_residual'] * w).sum() / w.sum()
    trend_data.append({'year': year, 'complexity': pc1_mean, 'spec_total': spec_mean, 'spec_residual': resid_mean})

trend_df = pd.DataFrame(trend_data)
trend_df.to_csv(os.path.join(ANALYSIS, 'mgmt_spec_decomposed_trends.csv'), index=False)

# Normalize to first year for comparability
for col in ['complexity', 'spec_total', 'spec_residual']:
    trend_df[f'{col}_indexed'] = trend_df[col] - trend_df[col].iloc[0]

ax2.plot(trend_df['year'], trend_df['spec_total_indexed'], '-o', color='#C62828',
         linewidth=2, markersize=5, label='Management-spec score (total)')
ax2.plot(trend_df['year'], trend_df['complexity_indexed'], '-s', color='#666',
         linewidth=2, markersize=5, label='Complexity (PC1) — control')
ax2.plot(trend_df['year'], trend_df['spec_residual_indexed'], '-^', color='#2E7D32',
         linewidth=2, markersize=5, label='Specification residual (after removing complexity)')
ax2.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax2.set_ylabel('Change from 2005 baseline', fontsize=11)
ax2.set_xlabel('Year', fontsize=11)
ax2.set_title('Decomposition: How Much Is Specification vs Just Complexity?',
              fontsize=13, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

textstr2 = (
    'Total spec score = weighted sum of GWAs that\n'
    'differentiate managers from non-managers.\n'
    'Complexity = PC1 of GWA space (general skill level).\n'
    'Residual = spec component after partialing out complexity.\n\n'
    'If the green line rises, the economy is shifting toward\n'
    'specification tasks BEYOND just becoming more complex.'
)
ax2.text(0.02, 0.02, textstr2, transform=ax2.transAxes, fontsize=7,
         va='bottom', ha='left', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'spec_employment_trend_decomposed.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: spec_employment_trend_decomposed.png")

print("\n" + "=" * 80)
print("COMPLETE")
print("=" * 80)
