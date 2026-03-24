"""
Entrepreneurial Analysis Phase 2c: Empirically-Derived Growth Profile
======================================================================
Instead of hand-classifying sectors as "specification" vs "execution,"
uses the empirical GWA differentiation pattern from Phase 2c (which GWAs
distinguish growing from shrinking occupations) as a data-driven composite.

Each occupation gets a "growth profile score" = weighted sum of its GWA
importance scores, where weights are the empirical Q5-Q1 differences from
the growing-vs-shrinking analysis. No a priori assumptions about what
counts as "specification."

Produces:
  - Employment shares by growth-profile tercile over time
  - Occupation-level growth profile scores
  - Charts showing employment shift toward growth-profile occupations
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
ANALYSIS = os.path.join(ROOT, 'data', 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# Load master panel and GWA column list
master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
gwa_cols = [c for c in gwa_matrix.columns if c in master.columns]

years = sorted(master['year'].unique())
first_year, last_year = years[0], years[-1]

# Load the growing-vs-shrinking GWA differences from Phase 2c
# These are the empirical weights: how much each GWA differentiates
# fast-growing (Q5) from fast-shrinking (Q1) occupations
diff_2c = pd.read_csv(os.path.join(ANALYSIS, 'gwa_growing_vs_shrinking.csv'), index_col=0)
weights = diff_2c['difference']

print("GWA weights (from Phase 2c growing-vs-shrinking analysis):")
print("(positive = more important in growing occupations)")
for gwa, w in weights.sort_values(ascending=False).items():
    print(f"  {w:+.4f}  {gwa}")

# Compute weighted composite for each occupation
def compute_composite(row, gwa_cols, weights):
    vals = row[gwa_cols]
    w = weights.reindex(gwa_cols).fillna(0)
    return (vals * w).sum() / w.abs().sum()

master['growth_profile_score'] = master.apply(
    lambda row: compute_composite(row, gwa_cols, weights), axis=1)

# Tercile cuts based on last year
ref = master[master['year'] == last_year]
score_cuts = ref['growth_profile_score'].quantile([1/3, 2/3]).values
print(f"\nGrowth profile score tercile cuts: {score_cuts[0]:.3f}, {score_cuts[1]:.3f}")

# Track employment shares by tercile
print(f"\nEmployment share by growth-profile tercile:")
print(f"{'Year':>6} {'Bottom (decline)':>18} {'Middle':>10} {'Top (growth)':>14} {'Total Emp':>12}")
print("-" * 65)

tercile_data = []
for year in years:
    ydf = master[(master['year'] == year) & master['employment'].notna() &
                  master['growth_profile_score'].notna()]
    total = ydf['employment'].sum()
    bottom = ydf[ydf['growth_profile_score'] < score_cuts[0]]['employment'].sum() / total
    top = ydf[ydf['growth_profile_score'] > score_cuts[1]]['employment'].sum() / total
    middle = 1 - bottom - top
    tercile_data.append({'year': year, 'bottom': bottom, 'middle': middle, 'top': top, 'total': total})
    print(f"{year:>6} {bottom:>18.1%} {middle:>10.1%} {top:>14.1%} {total:>12,.0f}")

tdf = pd.DataFrame(tercile_data)
tdf.to_csv(os.path.join(ANALYSIS, 'growth_profile_employment_shares.csv'), index=False)

# Save occupation-level scores
occ_scores = master[master['year'] == last_year][['soc_2018_harmonized', 'occ_title',
    'employment', 'median_wage', 'growth_profile_score', 'aioe_score']].copy()
occ_scores = occ_scores.sort_values('growth_profile_score', ascending=False)
occ_scores.to_csv(os.path.join(ANALYSIS, 'occupation_growth_profile_scores.csv'), index=False)

# --- Charts ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.stackplot(tdf['year'],
    tdf['top'] * 100, tdf['middle'] * 100, tdf['bottom'] * 100,
    labels=['Top tercile (growth-profile)', 'Middle tercile', 'Bottom tercile (decline-profile)'],
    colors=['#C62828', '#999', '#1565C0'], alpha=0.7)
ax1.set_ylabel('Share of Total Employment (%)', fontsize=11)
ax1.set_title('Employment Share by Empirically-Derived Growth Profile\n'
              '(composite of GWAs that differentiate growing from shrinking occupations)',
              fontsize=12, fontweight='bold')
ax1.legend(loc='center right', fontsize=9)
ax1.grid(True, alpha=0.2)

ax2.plot(tdf['year'], tdf['top'] * tdf['total'] / 1e6, '-o', color='#C62828',
         linewidth=2, markersize=4, label='Top tercile (growth-profile)')
ax2.plot(tdf['year'], tdf['bottom'] * tdf['total'] / 1e6, '-s', color='#1565C0',
         linewidth=2, markersize=4, label='Bottom tercile (decline-profile)')
ax2.set_ylabel('Employment (millions)', fontsize=11)
ax2.set_xlabel('Year', fontsize=11)
ax2.set_title('Absolute Employment in Growth-Profile vs Decline-Profile Occupations',
              fontsize=12, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

textstr = (
    'Growth profile = composite of GWA importance scores,\n'
    'weighted by how much each GWA empirically differentiates\n'
    'fast-growing from fast-shrinking occupations (2005-2024).\n'
    'No a priori classification of "specification" vs "execution."'
)
props = dict(boxstyle='round,pad=0.5', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9)
ax2.text(0.02, 0.98, textstr, transform=ax2.transAxes, fontsize=7.5,
         va='top', ha='left', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_growth_profile_employment.png'), dpi=250, bbox_inches='tight')
plt.close()
print("\nSaved: ent_growth_profile_employment.png")

# Print top/bottom occupation examples
print(f"\nTop 10 growth-profile occupations (2024):")
for _, row in occ_scores.head(10).iterrows():
    print(f"  {row['occ_title'][:55]:<55} emp={row['employment']:>10,.0f}  score={row['growth_profile_score']:.3f}")

print(f"\nBottom 10 growth-profile occupations (2024):")
for _, row in occ_scores.tail(10).iterrows():
    print(f"  {row['occ_title'][:55]:<55} emp={row['employment']:>10,.0f}  score={row['growth_profile_score']:.3f}")

print("\nDone.")
