"""
Phase 2: Exploratory Data Analysis
====================================
Using the master panel from Phase 1, compute:
  2a. Employment-weighted GWA importance over time
  2b. AIOE tercile breakdowns
  2c. Task composition of growing vs shrinking occupations
  2d. Within non-routine cognitive differentiation
  2e. Wage correlation trends by GWA
  2f. Repeat core analyses with Skills
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from scipy import stats
import os
import warnings
warnings.filterwarnings('ignore')

ROOT = '/Users/burnssa/Code/ai-labor-research'
ANALYSIS = os.path.join(ROOT, 'data', 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')
os.makedirs(FIGURES, exist_ok=True)

# Load master panel
master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
print(f"Master panel: {master.shape}")

# Identify GWA and skill columns
gwa_cols = [c for c in master.columns if c not in [
    'soc_code', 'occ_title', 'employment', 'median_wage', 'mean_wage',
    'year', 'soc_2018_harmonized', 'occ_group', 'median_hourly', 'mean_hourly',
    'aioe_score', 'soc_code_aioe'
] and not c.endswith('_skill')]
# Remove any non-GWA columns that slipped through
gwa_cols = [c for c in gwa_cols if master[c].dtype in ['float64', 'int64'] and master[c].max() <= 5.5]

skill_cols = [c for c in master.columns if c.endswith('_skill') or
              (c in [col for col in master.columns] and c not in gwa_cols
               and c not in ['soc_code', 'occ_title', 'employment', 'median_wage',
                             'mean_wage', 'year', 'soc_2018_harmonized', 'occ_group',
                             'median_hourly', 'mean_hourly', 'aioe_score', 'soc_code_aioe']
               and master[c].dtype in ['float64', 'int64'] and master[c].max() <= 5.5)]

# Let me be more precise - load the GWA and skill names directly
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
skill_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_skill_importance_matrix.csv'), index_col=0)
gwa_cols = [c for c in gwa_matrix.columns if c in master.columns]
skill_cols = [c for c in skill_matrix.columns if c in master.columns]

print(f"GWA columns: {len(gwa_cols)}")
print(f"Skill columns: {len(skill_cols)}")

years = sorted(master['year'].unique())
print(f"Years: {years}")

# =============================================================================
# 2a. Employment-Weighted GWA Importance Over Time
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2a: EMPLOYMENT-WEIGHTED GWA IMPORTANCE OVER TIME")
print("=" * 80)

def emp_weighted_mean(df, cols, weight_col='employment'):
    """Compute employment-weighted mean for each column."""
    w = df[weight_col].fillna(0)
    total_w = w.sum()
    if total_w == 0:
        return pd.Series({c: np.nan for c in cols})
    return pd.Series({c: (df[c] * w).sum() / total_w for c in cols})

# Compute for each year
ew_by_year = {}
for y in years:
    ydf = master[master['year'] == y].dropna(subset=['employment'])
    ew_by_year[y] = emp_weighted_mean(ydf, gwa_cols)

ew_panel = pd.DataFrame(ew_by_year).T
ew_panel.index.name = 'year'
ew_panel.to_csv(os.path.join(ANALYSIS, 'gwa_emp_weighted_by_year.csv'))

# Compute changes
first_year, last_year = years[0], years[-1]
total_change = ew_panel.loc[last_year] - ew_panel.loc[first_year]
pct_change = total_change / ew_panel.loc[first_year] * 100

change_df = pd.DataFrame({
    f'importance_{first_year}': ew_panel.loc[first_year],
    f'importance_{last_year}': ew_panel.loc[last_year],
    'total_change': total_change,
    'pct_change': pct_change,
}).sort_values('total_change', ascending=False)

print(f"\nAll 41 GWAs ranked by change in employment-weighted importance ({first_year}-{last_year}):")
print(f"{'GWA':<58} {first_year:>6} {last_year:>6} {'Change':>8} {'%Chg':>7}")
print("-" * 85)
for gwa, row in change_df.iterrows():
    print(f"{gwa:<58} {row[f'importance_{first_year}']:6.3f} {row[f'importance_{last_year}']:6.3f} "
          f"{row['total_change']:+8.4f} {row['pct_change']:+6.2f}%")

change_df.to_csv(os.path.join(ANALYSIS, 'gwa_emp_weighted_changes.csv'))

# --- Heatmap ---
fig, ax = plt.subplots(figsize=(10, 16))
# Sort by total change
sorted_gwas = change_df.index.tolist()
heatmap_data = ew_panel[sorted_gwas].T
sns.heatmap(heatmap_data, annot=True, fmt='.3f', cmap='YlOrRd',
            linewidths=0.5, ax=ax, cbar_kws={'label': 'Employment-Weighted Importance'})
ax.set_title(f'Employment-Weighted GWA Importance by Year\n(sorted by {first_year}-{last_year} change)',
             fontsize=13, fontweight='bold')
ax.set_xlabel('Year')
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'p2a_gwa_heatmap.png'), dpi=200, bbox_inches='tight')
plt.close()

# --- Slope chart: top 10 positive + top 10 negative ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

top10_pos = change_df.head(10).index.tolist()
top10_neg = change_df.tail(10).index.tolist()

for gwa in top10_pos:
    vals = [ew_panel.loc[y, gwa] for y in years]
    ax1.plot(years, vals, '-o', markersize=4, label=gwa[:40])
ax1.set_title('10 GWAs with Largest INCREASE', fontsize=12, fontweight='bold')
ax1.set_ylabel('Employment-Weighted Importance')
ax1.legend(fontsize=7, loc='upper left')
ax1.grid(True, alpha=0.3)

for gwa in top10_neg:
    vals = [ew_panel.loc[y, gwa] for y in years]
    ax2.plot(years, vals, '-o', markersize=4, label=gwa[:40])
ax2.set_title('10 GWAs with Largest DECREASE', fontsize=12, fontweight='bold')
ax2.set_ylabel('Employment-Weighted Importance')
ax2.legend(fontsize=7, loc='upper left')
ax2.grid(True, alpha=0.3)

plt.suptitle(f'GWA Trends: Employment-Weighted Importance ({first_year}-{last_year})',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'p2a_gwa_slopes.png'), dpi=200, bbox_inches='tight')
plt.close()

print(f"\nSaved: p2a_gwa_heatmap.png, p2a_gwa_slopes.png")

# =============================================================================
# 2b. AIOE Tercile Breakdowns
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2b: AIOE TERCILE ANALYSIS")
print("=" * 80)

# Assign AIOE terciles based on 2024 data (or most recent available)
aioe_ref = master[master['year'] == last_year][['soc_2018_harmonized', 'aioe_score']].dropna()
aioe_ref = aioe_ref.drop_duplicates(subset='soc_2018_harmonized')
tercile_cuts = aioe_ref['aioe_score'].quantile([1/3, 2/3]).values
aioe_ref['aioe_tercile'] = pd.cut(aioe_ref['aioe_score'],
                                   bins=[-np.inf, tercile_cuts[0], tercile_cuts[1], np.inf],
                                   labels=['Low AI Exposure', 'Medium AI Exposure', 'High AI Exposure'])
print(f"  AIOE tercile cuts: {tercile_cuts}")
print(f"  Tercile counts: {aioe_ref['aioe_tercile'].value_counts().to_dict()}")

# Merge terciles back to master
master_t = master.merge(aioe_ref[['soc_2018_harmonized', 'aioe_tercile']],
                        on='soc_2018_harmonized', how='left')

# Compute emp-weighted GWA importance by year × tercile
ew_by_tercile = {}
for tercile in ['Low AI Exposure', 'Medium AI Exposure', 'High AI Exposure']:
    tercile_data = {}
    for y in years:
        tdf = master_t[(master_t['year'] == y) & (master_t['aioe_tercile'] == tercile)]
        tdf = tdf.dropna(subset=['employment'])
        if len(tdf) > 0:
            tercile_data[y] = emp_weighted_mean(tdf, gwa_cols)
    ew_by_tercile[tercile] = pd.DataFrame(tercile_data).T

# Compute change for each tercile
print(f"\nGWA changes by AIOE tercile ({first_year}-{last_year}):")
tercile_changes = {}
for tercile, panel in ew_by_tercile.items():
    if first_year in panel.index and last_year in panel.index:
        chg = panel.loc[last_year] - panel.loc[first_year]
        tercile_changes[tercile] = chg

tc_df = pd.DataFrame(tercile_changes)
tc_df.to_csv(os.path.join(ANALYSIS, 'gwa_changes_by_aioe_tercile.csv'))

# Print top divergences: where high-AIOE and low-AIOE move in opposite directions
if 'High AI Exposure' in tc_df.columns and 'Low AI Exposure' in tc_df.columns:
    tc_df['high_minus_low'] = tc_df['High AI Exposure'] - tc_df['Low AI Exposure']
    tc_df_sorted = tc_df.sort_values('high_minus_low', ascending=False)

    print(f"\n{'GWA':<50} {'Low AIOE':>10} {'Med AIOE':>10} {'High AIOE':>10} {'Hi-Lo':>8}")
    print("-" * 92)
    for gwa, row in tc_df_sorted.iterrows():
        print(f"{gwa:<50} {row.get('Low AI Exposure', np.nan):+10.4f} "
              f"{row.get('Medium AI Exposure', np.nan):+10.4f} "
              f"{row.get('High AI Exposure', np.nan):+10.4f} "
              f"{row['high_minus_low']:+8.4f}")

# --- Faceted slope chart ---
fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)
# Pick top 5 positive + top 5 negative overall changes
top5 = change_df.head(5).index.tolist()
bot5 = change_df.tail(5).index.tolist()
highlight_gwas = top5 + bot5

colors_pos = plt.cm.Reds(np.linspace(0.3, 0.9, 5))
colors_neg = plt.cm.Blues(np.linspace(0.3, 0.9, 5))

for idx, (tercile, panel) in enumerate(ew_by_tercile.items()):
    ax = axes[idx]
    for i, gwa in enumerate(top5):
        if gwa in panel.columns:
            vals = [panel.loc[y, gwa] if y in panel.index else np.nan for y in years]
            ax.plot(years, vals, '-o', color=colors_pos[i], markersize=3,
                    label=gwa[:35] if idx == 0 else None, linewidth=1.5)
    for i, gwa in enumerate(bot5):
        if gwa in panel.columns:
            vals = [panel.loc[y, gwa] if y in panel.index else np.nan for y in years]
            ax.plot(years, vals, '-s', color=colors_neg[i], markersize=3,
                    label=gwa[:35] if idx == 0 else None, linewidth=1.5)
    ax.set_title(tercile, fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Year')

axes[0].set_ylabel('Employment-Weighted Importance')
axes[0].legend(fontsize=6, loc='lower left')
plt.suptitle(f'GWA Trends by AI Exposure Tercile ({first_year}-{last_year})',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'p2b_aioe_tercile_slopes.png'), dpi=200, bbox_inches='tight')
plt.close()
print(f"\nSaved: p2b_aioe_tercile_slopes.png")

# =============================================================================
# 2c. Task Composition of Growing vs Shrinking Occupations
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2c: GROWING vs SHRINKING OCCUPATIONS")
print("=" * 80)

# Get occupations present in both first and last year
first_df = master[master['year'] == first_year][['soc_2018_harmonized', 'employment', 'occ_title']].dropna()
last_df = master[master['year'] == last_year][['soc_2018_harmonized', 'employment']].dropna()
merged = first_df.merge(last_df, on='soc_2018_harmonized', suffixes=('_first', '_last'))
merged['emp_growth'] = (merged['employment_last'] - merged['employment_first']) / merged['employment_first']
merged = merged.replace([np.inf, -np.inf], np.nan).dropna(subset=['emp_growth'])

# Assign quintiles
merged['growth_quintile'] = pd.qcut(merged['emp_growth'], 5, labels=[
    'Q1 (fastest shrinking)', 'Q2', 'Q3', 'Q4', 'Q5 (fastest growing)'])

print(f"  Occupations with growth data: {len(merged)}")
print(f"\n  Growth quintile summary:")
for q in merged['growth_quintile'].unique():
    qdf = merged[merged['growth_quintile'] == q]
    print(f"    {q}: n={len(qdf)}, emp_growth median={qdf['emp_growth'].median()*100:+.1f}%, "
          f"range=[{qdf['emp_growth'].min()*100:.1f}%, {qdf['emp_growth'].max()*100:.1f}%]")

# Get GWA profiles for each quintile (use last_year O*NET-merged data)
last_gwa = master[master['year'] == last_year][['soc_2018_harmonized', 'employment'] + gwa_cols].dropna()
q_profiles = merged[['soc_2018_harmonized', 'growth_quintile', 'employment_last']].merge(
    last_gwa.drop(columns=['employment']), on='soc_2018_harmonized')

q1_label = 'Q1 (fastest shrinking)'
q5_label = 'Q5 (fastest growing)'

q1_profile = emp_weighted_mean(
    q_profiles[q_profiles['growth_quintile'] == q1_label], gwa_cols, weight_col='employment_last')
q5_profile = emp_weighted_mean(
    q_profiles[q_profiles['growth_quintile'] == q5_label], gwa_cols, weight_col='employment_last')

diff = q5_profile - q1_profile
diff_df = pd.DataFrame({
    'Q1_shrinking': q1_profile,
    'Q5_growing': q5_profile,
    'difference': diff,
}).sort_values('difference', ascending=False)

# Statistical tests
pvals = {}
for gwa in gwa_cols:
    g1 = q_profiles[q_profiles['growth_quintile'] == q1_label][gwa].dropna()
    g5 = q_profiles[q_profiles['growth_quintile'] == q5_label][gwa].dropna()
    if len(g1) > 5 and len(g5) > 5:
        stat, pval = stats.mannwhitneyu(g5, g1, alternative='two-sided')
        pvals[gwa] = pval
    else:
        pvals[gwa] = np.nan

diff_df['p_value'] = diff_df.index.map(pvals)
diff_df['significant'] = diff_df['p_value'] < 0.05

print(f"\n  GWAs that differentiate GROWING from SHRINKING occupations:")
print(f"  {'GWA':<55} {'Q1(shrk)':>9} {'Q5(grow)':>9} {'Diff':>8} {'p-val':>8} {'Sig':>4}")
print("  " + "-" * 97)
for gwa, row in diff_df.iterrows():
    sig = '***' if row['p_value'] < 0.001 else ('**' if row['p_value'] < 0.01 else
           ('*' if row['p_value'] < 0.05 else ''))
    print(f"  {gwa:<55} {row['Q1_shrinking']:9.3f} {row['Q5_growing']:9.3f} "
          f"{row['difference']:+8.4f} {row['p_value']:8.4f} {sig:>4}")

diff_df.to_csv(os.path.join(ANALYSIS, 'gwa_growing_vs_shrinking.csv'))

# --- Difference chart ---
fig, ax = plt.subplots(figsize=(12, 14))
colors = ['#E53935' if d > 0 else '#1E88E5' for d in diff_df['difference']]
bars = ax.barh(range(len(diff_df)), diff_df['difference'], color=colors, alpha=0.8)
ax.set_yticks(range(len(diff_df)))
ax.set_yticklabels(diff_df.index, fontsize=8)
ax.set_xlabel('Difference: Q5 (fastest growing) minus Q1 (fastest shrinking)', fontsize=11)
ax.set_title('GWA Importance: What Differentiates Growing from Shrinking Occupations',
             fontsize=13, fontweight='bold')
ax.axvline(x=0, color='black', linewidth=0.5)
# Mark significance
for i, (gwa, row) in enumerate(diff_df.iterrows()):
    if row['significant']:
        ax.text(row['difference'] + (0.005 if row['difference'] > 0 else -0.005),
                i, '*', fontsize=10, va='center',
                ha='left' if row['difference'] > 0 else 'right', color='black')
ax.annotate('Red = more important for GROWING occupations\nBlue = more important for SHRINKING occupations',
            xy=(0.02, 0.02), xycoords='axes fraction', fontsize=9, color='gray')
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'p2c_growing_vs_shrinking_diff.png'), dpi=200, bbox_inches='tight')
plt.close()
print(f"\n  Saved: p2c_growing_vs_shrinking_diff.png")

# =============================================================================
# 2d. Within Non-Routine Cognitive
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2d: WITHIN NON-ROUTINE COGNITIVE")
print("=" * 80)

# Define NRC using GWA scores on the last-year data
nrc_positive = ['Analyzing Data or Information', 'Thinking Creatively',
                'Interpreting the Meaning of Information for Others',
                'Making Decisions and Solving Problems']
nrc_negative = ['Performing General Physical Activities',
                'Handling and Moving Objects',
                'Controlling Machines and Processes']

last_year_data = master[master['year'] == last_year].copy()
# Composite score
last_year_data['nrc_pos'] = last_year_data[nrc_positive].mean(axis=1)
last_year_data['nrc_neg'] = last_year_data[nrc_negative].mean(axis=1)
last_year_data['nrc_composite'] = last_year_data['nrc_pos'] - last_year_data['nrc_neg']

# Top half = NRC occupations
nrc_threshold = last_year_data['nrc_composite'].median()
nrc_socs = set(last_year_data[last_year_data['nrc_composite'] >= nrc_threshold]['soc_2018_harmonized'])

print(f"  NRC composite threshold (median): {nrc_threshold:.3f}")
print(f"  NRC occupations: {len(nrc_socs)}")
print(f"  Non-NRC occupations: {len(last_year_data) - len(nrc_socs)}")

# Within NRC: split by employment growth
nrc_growth = merged[merged['soc_2018_harmonized'].isin(nrc_socs)].copy()
nrc_growth['nrc_growth_quintile'] = pd.qcut(
    nrc_growth['emp_growth'], 5, labels=['Q1 (NRC shrinking)', 'Q2', 'Q3', 'Q4', 'Q5 (NRC growing)'],
    duplicates='drop')

print(f"  NRC occupations with growth data: {len(nrc_growth)}")

# GWA profiles for growing vs shrinking NRC
nrc_q_profiles = nrc_growth[['soc_2018_harmonized', 'nrc_growth_quintile', 'employment_last']].merge(
    last_gwa.drop(columns=['employment']), on='soc_2018_harmonized')

nrc_q1 = 'Q1 (NRC shrinking)'
nrc_q5 = 'Q5 (NRC growing)'

nrc_q1_prof = emp_weighted_mean(
    nrc_q_profiles[nrc_q_profiles['nrc_growth_quintile'] == nrc_q1], gwa_cols, weight_col='employment_last')
nrc_q5_prof = emp_weighted_mean(
    nrc_q_profiles[nrc_q_profiles['nrc_growth_quintile'] == nrc_q5], gwa_cols, weight_col='employment_last')

nrc_diff = nrc_q5_prof - nrc_q1_prof
nrc_diff_df = pd.DataFrame({
    'NRC_Q1_shrinking': nrc_q1_prof,
    'NRC_Q5_growing': nrc_q5_prof,
    'difference': nrc_diff,
}).sort_values('difference', ascending=False)

# Statistical tests within NRC
nrc_pvals = {}
for gwa in gwa_cols:
    g1 = nrc_q_profiles[nrc_q_profiles['nrc_growth_quintile'] == nrc_q1][gwa].dropna()
    g5 = nrc_q_profiles[nrc_q_profiles['nrc_growth_quintile'] == nrc_q5][gwa].dropna()
    if len(g1) > 5 and len(g5) > 5:
        stat, pval = stats.mannwhitneyu(g5, g1, alternative='two-sided')
        nrc_pvals[gwa] = pval
    else:
        nrc_pvals[gwa] = np.nan

nrc_diff_df['p_value'] = nrc_diff_df.index.map(nrc_pvals)
nrc_diff_df['significant'] = nrc_diff_df['p_value'] < 0.05

print(f"\n  Within NRC: GWAs differentiating GROWING from SHRINKING:")
print(f"  {'GWA':<55} {'NRC-Q1':>8} {'NRC-Q5':>8} {'Diff':>8} {'p-val':>8} {'Sig':>4}")
print("  " + "-" * 95)
for gwa, row in nrc_diff_df.iterrows():
    sig = '***' if row['p_value'] < 0.001 else ('**' if row['p_value'] < 0.01 else
           ('*' if row['p_value'] < 0.05 else ''))
    print(f"  {gwa:<55} {row['NRC_Q1_shrinking']:8.3f} {row['NRC_Q5_growing']:8.3f} "
          f"{row['difference']:+8.4f} {row['p_value']:8.4f} {sig:>4}")

nrc_diff_df.to_csv(os.path.join(ANALYSIS, 'gwa_within_nrc_growing_vs_shrinking.csv'))

# --- Within-NRC difference chart ---
fig, ax = plt.subplots(figsize=(12, 14))
colors = ['#E53935' if d > 0 else '#1E88E5' for d in nrc_diff_df['difference']]
ax.barh(range(len(nrc_diff_df)), nrc_diff_df['difference'], color=colors, alpha=0.8)
ax.set_yticks(range(len(nrc_diff_df)))
ax.set_yticklabels(nrc_diff_df.index, fontsize=8)
ax.set_xlabel('Difference: Q5 (growing NRC) minus Q1 (shrinking NRC)', fontsize=11)
ax.set_title('Within Non-Routine Cognitive Occupations:\nWhat Differentiates Growing from Shrinking?',
             fontsize=13, fontweight='bold')
ax.axvline(x=0, color='black', linewidth=0.5)
for i, (gwa, row) in enumerate(nrc_diff_df.iterrows()):
    if row['significant']:
        ax.text(row['difference'] + (0.005 if row['difference'] > 0 else -0.005),
                i, '*', fontsize=10, va='center',
                ha='left' if row['difference'] > 0 else 'right', color='black')
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'p2d_within_nrc_diff.png'), dpi=200, bbox_inches='tight')
plt.close()
print(f"\n  Saved: p2d_within_nrc_diff.png")

# =============================================================================
# 2e. Wage Correlation Trends by GWA
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2e: WAGE CORRELATION TRENDS")
print("=" * 80)

wage_corrs = {}
for y in years:
    ydf = master[(master['year'] == y) & master['median_wage'].notna() &
                  (master['median_wage'] > 0)].copy()
    corrs = {}
    for gwa in gwa_cols:
        if ydf[gwa].notna().sum() > 20:
            r, p = stats.spearmanr(ydf[gwa], ydf['median_wage'])
            corrs[gwa] = r
    wage_corrs[y] = corrs

wage_corr_panel = pd.DataFrame(wage_corrs)
wage_corr_panel.index.name = 'GWA'
wage_corr_panel.to_csv(os.path.join(ANALYSIS, 'gwa_wage_correlations_by_year.csv'))

# Compute change in correlation
corr_change = wage_corr_panel[last_year] - wage_corr_panel[first_year]
corr_change_df = pd.DataFrame({
    f'corr_{first_year}': wage_corr_panel[first_year],
    f'corr_{last_year}': wage_corr_panel[last_year],
    'corr_change': corr_change,
}).sort_values('corr_change', ascending=False)

print(f"\nGWA-Wage correlations (Spearman) ranked by change ({first_year}-{last_year}):")
print(f"{'GWA':<55} {'r_'+str(first_year):>8} {'r_'+str(last_year):>8} {'Change':>8}")
print("-" * 83)
for gwa, row in corr_change_df.iterrows():
    print(f"{gwa:<55} {row[f'corr_{first_year}']:+8.3f} {row[f'corr_{last_year}']:+8.3f} "
          f"{row['corr_change']:+8.4f}")

corr_change_df.to_csv(os.path.join(ANALYSIS, 'gwa_wage_correlation_changes.csv'))

# =============================================================================
# 4a. THE KEY SUMMARY EXHIBIT
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 4a: KEY SUMMARY SCATTER PLOT")
print("=" * 80)

# Merge employment-weighted importance change (2a) with wage correlation change (2e)
key_df = pd.DataFrame({
    'emp_weighted_change': change_df['total_change'],
    'wage_corr_change': corr_change_df['corr_change'],
    f'current_importance': ew_panel.loc[last_year],
}).dropna()

fig, ax = plt.subplots(figsize=(14, 11))

# Point size proportional to current importance
sizes = (key_df[f'current_importance'] - key_df[f'current_importance'].min()) / \
        (key_df[f'current_importance'].max() - key_df[f'current_importance'].min()) * 200 + 30

ax.scatter(key_df['emp_weighted_change'], key_df['wage_corr_change'],
           s=sizes, alpha=0.6, c='#37474F', edgecolors='white', linewidth=0.5)

# Label all points
for gwa, row in key_df.iterrows():
    # Shorten long names
    short = gwa.replace('Communicating with Supervisors, Peers, or Subordinates', 'Comm w/ Supervisors/Peers')
    short = short.replace('Communicating with People Outside the Organization', 'Comm w/ External People')
    short = short.replace('Establishing and Maintaining Interpersonal Relationships', 'Interpersonal Relations')
    short = short.replace('Evaluating Information to Determine Compliance with Standards', 'Eval Compliance')
    short = short.replace('Estimating the Quantifiable Characteristics of Products, Events, or Information', 'Estimating Quantities')
    short = short.replace('Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment', 'Drafting/Technical Spec')
    short = short.replace('Organizing, Planning, and Prioritizing Work', 'Organizing/Planning Work')
    short = short.replace('Performing General Physical Activities', 'Physical Activities')
    short = short.replace('Repairing and Maintaining Mechanical Equipment', 'Repair Mechanical')
    short = short.replace('Repairing and Maintaining Electronic Equipment', 'Repair Electronic')
    short = short.replace('Operating Vehicles, Mechanized Devices, or Equipment', 'Operating Vehicles/Equip')
    short = short.replace('Guiding, Directing, and Motivating Subordinates', 'Guiding/Directing Subordinates')
    short = short.replace('Monitoring Processes, Materials, or Surroundings', 'Monitoring Processes')
    short = short.replace('Resolving Conflicts and Negotiating with Others', 'Negotiating/Conflicts')
    short = short.replace('Judging the Qualities of Objects, Services, or People', 'Judging Qualities')
    short = short.replace('Identifying Objects, Actions, and Events', 'Identifying Objects/Events')
    short = short.replace('Inspecting Equipment, Structures, or Materials', 'Inspecting Equipment')
    short = short.replace('Updating and Using Relevant Knowledge', 'Using Relevant Knowledge')
    short = short.replace('Making Decisions and Solving Problems', 'Decision Making')
    short = short.replace('Performing for or Working Directly with the Public', 'Working w/ Public')
    short = short.replace('Interpreting the Meaning of Information for Others', 'Interpreting Info for Others')
    short = short.replace('Providing Consultation and Advice to Others', 'Consulting/Advising')
    short = short.replace('Coordinating the Work and Activities of Others', 'Coordinating Others')
    short = short.replace('Performing Administrative Activities', 'Admin Activities')
    short = short.replace('Scheduling Work and Activities', 'Scheduling')
    short = short.replace('Developing Objectives and Strategies', 'Developing Strategy')
    short = short.replace('Coaching and Developing Others', 'Coaching Others')
    short = short.replace('Developing and Building Teams', 'Building Teams')
    short = short.replace('Assisting and Caring for Others', 'Assisting/Caring')
    short = short.replace('Training and Teaching Others', 'Training/Teaching')
    short = short.replace('Selling or Influencing Others', 'Selling/Influencing')
    short = short.replace('Staffing Organizational Units', 'Staffing')
    short = short.replace('Monitoring and Controlling Resources', 'Controlling Resources')
    short = short.replace('Analyzing Data or Information', 'Analyzing Data')
    short = short.replace('Documenting/Recording Information', 'Documenting')
    short = short.replace('Handling and Moving Objects', 'Handling Objects')
    short = short.replace('Controlling Machines and Processes', 'Controlling Machines')
    short = short.replace('Thinking Creatively', 'Thinking Creatively')
    short = short.replace('Processing Information', 'Processing Info')
    short = short.replace('Working with Computers', 'Working w/ Computers')
    short = short.replace('Getting Information', 'Getting Info')

    ax.annotate(short, (row['emp_weighted_change'], row['wage_corr_change']),
                fontsize=6.5, alpha=0.85,
                textcoords='offset points', xytext=(5, 3))

# Quadrant labels
xlim = ax.get_xlim()
ylim = ax.get_ylim()
ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax.axvline(x=0, color='gray', linewidth=0.5, linestyle='--')

ax.text(xlim[1]*0.95, ylim[1]*0.95, 'Growing prevalence +\ngrowing wage premium',
        fontsize=9, ha='right', va='top', color='#2E7D32', fontstyle='italic', alpha=0.7)
ax.text(xlim[0]*0.95, ylim[0]*0.95, 'Shrinking prevalence +\nshrinking wage premium',
        fontsize=9, ha='left', va='bottom', color='#C62828', fontstyle='italic', alpha=0.7)

ax.set_xlabel(f'Change in Employment-Weighted Importance ({first_year}-{last_year})', fontsize=12)
ax.set_ylabel(f'Change in Wage Correlation ({first_year}-{last_year})', fontsize=12)
ax.set_title('The Key Exhibit: Which Work Activities Are Growing in Both\nPrevalence and Wage Premium?',
             fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'p4a_key_exhibit_scatter.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"  Saved: p4a_key_exhibit_scatter.png")

# =============================================================================
# 2f. Repeat with Skills
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2f: SKILLS ANALYSIS (ROBUSTNESS CHECK)")
print("=" * 80)

# Employment-weighted skill importance over time
ew_skills_by_year = {}
for y in years:
    ydf = master[master['year'] == y].dropna(subset=['employment'])
    available_skills = [c for c in skill_cols if c in ydf.columns]
    if available_skills:
        ew_skills_by_year[y] = emp_weighted_mean(ydf, available_skills)

if ew_skills_by_year:
    ew_skills_panel = pd.DataFrame(ew_skills_by_year).T
    skill_change = ew_skills_panel.loc[last_year] - ew_skills_panel.loc[first_year]
    skill_change_df = pd.DataFrame({
        f'importance_{first_year}': ew_skills_panel.loc[first_year],
        f'importance_{last_year}': ew_skills_panel.loc[last_year],
        'total_change': skill_change,
    }).sort_values('total_change', ascending=False)

    print(f"\nSkills ranked by change in employment-weighted importance ({first_year}-{last_year}):")
    print(f"{'Skill':<45} {first_year:>8} {last_year:>8} {'Change':>8}")
    print("-" * 73)
    for skill, row in skill_change_df.iterrows():
        name = skill.replace('_skill', '') if skill.endswith('_skill') else skill
        print(f"{name:<45} {row[f'importance_{first_year}']:8.3f} {row[f'importance_{last_year}']:8.3f} "
              f"{row['total_change']:+8.4f}")

    skill_change_df.to_csv(os.path.join(ANALYSIS, 'skill_emp_weighted_changes.csv'))

    # Wage correlations for skills
    skill_wage_corrs = {}
    for y in years:
        ydf = master[(master['year'] == y) & master['median_wage'].notna() &
                      (master['median_wage'] > 0)].copy()
        corrs = {}
        available_skills = [c for c in skill_cols if c in ydf.columns]
        for sk in available_skills:
            if ydf[sk].notna().sum() > 20:
                r, p = stats.spearmanr(ydf[sk], ydf['median_wage'])
                corrs[sk] = r
        skill_wage_corrs[y] = corrs

    if skill_wage_corrs:
        skill_corr_panel = pd.DataFrame(skill_wage_corrs)
        skill_corr_change = skill_corr_panel[last_year] - skill_corr_panel[first_year]
        skill_corr_df = pd.DataFrame({
            f'corr_{first_year}': skill_corr_panel[first_year],
            f'corr_{last_year}': skill_corr_panel[last_year],
            'corr_change': skill_corr_change,
        }).sort_values('corr_change', ascending=False)

        print(f"\nSkill-Wage correlations ranked by change:")
        print(f"{'Skill':<45} {'r_'+str(first_year):>8} {'r_'+str(last_year):>8} {'Change':>8}")
        print("-" * 73)
        for skill, row in skill_corr_df.iterrows():
            name = skill.replace('_skill', '') if skill.endswith('_skill') else skill
            print(f"{name:<45} {row[f'corr_{first_year}']:+8.3f} {row[f'corr_{last_year}']:+8.3f} "
                  f"{row['corr_change']:+8.4f}")

        skill_corr_df.to_csv(os.path.join(ANALYSIS, 'skill_wage_correlation_changes.csv'))

print("\n" + "=" * 80)
print("PHASE 2 COMPLETE")
print("=" * 80)
print(f"\nAll outputs saved to:")
print(f"  CSVs: {ANALYSIS}/")
print(f"  Figures: {FIGURES}/")
