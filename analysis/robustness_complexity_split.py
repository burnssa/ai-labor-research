"""
Robustness Check: Does specification-residual predict employment growth
when restricted to above-median-complexity occupations?

Motivation: The spec_residual (management gradient after removing PC1)
mechanically inflates low-complexity jobs that have any interpersonal/
selling/directing component. Manicurists, cashiers, and fast food workers
score high on the residual not because they "specify" in the article's
sense, but because the linear model predicts near-zero management score
for them and any small positive value becomes a large residual.

This script tests whether the core relationships hold when we restrict
to occupations above the median on PC1 (cognitive complexity), where the
linear residualization is better-behaved and the "specification" label
has stronger face validity.

Tests:
  1. GWA-level: Does the management-residual vs growth-residual
     correlation hold among above-median-complexity occupations?
  2. Occupation-level: Does spec_residual predict employment growth
     among above-median-complexity occupations?
  3. Employment decomposition: Recompute exhibit 2 restricted to
     above-median-complexity occupations.

Inputs:
  - data/analysis/spec_ai_panel.csv
  - data/analysis/onet_gwa_importance_matrix.csv
  - data/analysis/master_panel.csv
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

panel = pd.read_csv(os.path.join(ANALYSIS, 'spec_ai_panel.csv'))
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
gwa_cols = list(gwa_matrix.columns)
years = sorted(master['year'].unique())
first_year, last_year = years[0], years[-1]

# =============================================================================
# Recompute PCA, management contrast, and residuals from source
# =============================================================================
scaler = StandardScaler()
X = scaler.fit_transform(gwa_matrix.dropna())
pca = PCA()
pca.fit(X)

occ_pca = pd.DataFrame(
    pca.transform(X),
    index=gwa_matrix.dropna().index,
    columns=[f'PC{i+1}' for i in range(X.shape[1])]
)

# Management contrast weights
mgmt_socs = [s for s in gwa_matrix.index if s.startswith('11-')]
non_mgmt_socs = [s for s in gwa_matrix.index if not s.startswith('11-')]
mgmt_profile = gwa_matrix.loc[mgmt_socs].mean()
non_mgmt_profile = gwa_matrix.loc[non_mgmt_socs].mean()
mgmt_weights = mgmt_profile - non_mgmt_profile

# Occupation-level management score and PC1
occ_scores = pd.DataFrame({
    'pc1': occ_pca['PC1'],
    'mgmt_score': gwa_matrix.apply(
        lambda row: (row[gwa_cols] * mgmt_weights.reindex(gwa_cols).fillna(0)).sum()
        / mgmt_weights.abs().sum(), axis=1),
}, index=gwa_matrix.index)

# Residualize management score on PC1
valid_occs = occ_scores.dropna()
slope, intercept = np.polyfit(valid_occs['pc1'], valid_occs['mgmt_score'], 1)
occ_scores['spec_residual'] = occ_scores['mgmt_score'] - (intercept + slope * occ_scores['pc1'])

median_pc1 = occ_scores['pc1'].median()

print("=" * 80)
print("ROBUSTNESS: COMPLEXITY-SPLIT ANALYSIS")
print("=" * 80)
print(f"Median PC1 (complexity): {median_pc1:.3f}")
print(f"Occupations above median: {(occ_scores['pc1'] >= median_pc1).sum()}")
print(f"Occupations below median: {(occ_scores['pc1'] < median_pc1).sum()}")

# =============================================================================
# Test 1: GWA-level correlation — full sample vs above-median complexity
# =============================================================================
print("\n" + "=" * 80)
print("TEST 1: GWA-LEVEL CORRELATION")
print("Does spec-residual predict growth-residual at the task level?")
print("=" * 80)

# Compute employment growth by GWA (how much each GWA characterizes growing occupations)
# For each GWA, correlate its importance across occupations with employment growth
occ_growth = panel.dropna(subset=[f'emp_{first_year}', f'emp_{last_year}', 'spec_score']).copy()
occ_growth['emp_growth'] = (occ_growth[f'emp_{last_year}'] - occ_growth[f'emp_{first_year}']) / occ_growth[f'emp_{first_year}']
occ_growth['emp_growth'] = occ_growth['emp_growth'].clip(-2, 5)  # winsorize extremes

# Merge GWA data
occ_growth = occ_growth.merge(gwa_matrix, left_on='soc_code', right_index=True, how='inner')
occ_growth = occ_growth.merge(occ_pca[['PC1']], left_on='soc_code', right_index=True, how='inner')

def gwa_growth_correlation(df, label):
    """Compute management-residual vs growth-residual correlation across 41 GWAs."""
    gwa_mgmt_resid = []
    gwa_growth_resid = []

    for gwa in gwa_cols:
        # Management residual for this GWA (already computed above)
        mgmt_val = mgmt_weights.get(gwa, 0)
        pc1_loading = pca.components_[0][gwa_cols.index(gwa)]
        # Residualize mgmt weight against PC1 loading
        # (simplified: use the occupation-level regression for GWA-level)
        gwa_mgmt_resid.append(mgmt_val)

        # Growth residual: correlation of this GWA with emp growth, after removing PC1
        emp_w = df[f'emp_{last_year}']
        gwa_vals = df[gwa]
        pc1_vals = df['PC1']
        growth_vals = df['emp_growth']

        # Partial correlation: GWA importance -> growth, controlling for PC1
        # Residualize both on PC1
        if gwa_vals.std() > 0:
            s1, i1 = np.polyfit(pc1_vals, gwa_vals, 1)
            gwa_resid = gwa_vals - (i1 + s1 * pc1_vals)
            s2, i2 = np.polyfit(pc1_vals, growth_vals, 1)
            growth_resid = growth_vals - (i2 + s2 * pc1_vals)
            r, _ = stats.spearmanr(gwa_resid, growth_resid)
            gwa_growth_resid.append(r)
        else:
            gwa_growth_resid.append(0)

    # Now correlate: across 41 GWAs, do management-residual and growth-residual align?
    mgmt_resid_vec = mgmt_weights.reindex(gwa_cols).fillna(0).values
    pc1_loadings = pca.components_[0]
    s, i = np.polyfit(pc1_loadings, mgmt_resid_vec, 1)
    mgmt_resid_clean = mgmt_resid_vec - (i + s * pc1_loadings)

    r_spearman, p_spearman = stats.spearmanr(mgmt_resid_clean, gwa_growth_resid)
    r_pearson, p_pearson = stats.pearsonr(mgmt_resid_clean, gwa_growth_resid)

    print(f"\n  {label}:")
    print(f"    Spearman r = {r_spearman:.3f} (p = {p_spearman:.4f})")
    print(f"    Pearson  r = {r_pearson:.3f} (p = {p_pearson:.4f})")
    print(f"    N occupations in sample: {len(df)}")
    return mgmt_resid_clean, gwa_growth_resid, r_spearman, p_spearman

# Full sample
mgmt_r_full, growth_r_full, r_full, p_full = gwa_growth_correlation(occ_growth, "Full sample")

# Above-median complexity only
high_cpx = occ_growth[occ_growth['PC1'] >= median_pc1]
mgmt_r_high, growth_r_high, r_high, p_high = gwa_growth_correlation(high_cpx, "Above-median complexity only")

# Below-median complexity only
low_cpx = occ_growth[occ_growth['PC1'] < median_pc1]
mgmt_r_low, growth_r_low, r_low, p_low = gwa_growth_correlation(low_cpx, "Below-median complexity only")

# =============================================================================
# Test 2: Occupation-level — spec_residual predicts growth?
# =============================================================================
print("\n" + "=" * 80)
print("TEST 2: OCCUPATION-LEVEL CORRELATION")
print("Does spec_residual predict employment growth across occupations?")
print("=" * 80)

occ_test = panel.dropna(subset=['spec_residual', 'complexity_pc1', 'emp_growth']).copy()
occ_test['emp_growth_w'] = occ_test['emp_growth'].clip(-2, 5)

for label, mask in [
    ("Full sample", occ_test.index == occ_test.index),
    ("Above-median complexity", occ_test['complexity_pc1'] >= median_pc1),
    ("Below-median complexity", occ_test['complexity_pc1'] < median_pc1),
]:
    sub = occ_test[mask]
    # Unweighted
    r_s, p_s = stats.spearmanr(sub['spec_residual'], sub['emp_growth_w'])
    r_p, p_p = stats.pearsonr(sub['spec_residual'], sub['emp_growth_w'])

    # Employment-weighted pearson
    w = sub[f'emp_{first_year}'].fillna(0)
    if w.sum() > 0:
        wmean_x = (sub['spec_residual'] * w).sum() / w.sum()
        wmean_y = (sub['emp_growth_w'] * w).sum() / w.sum()
        wcov = (w * (sub['spec_residual'] - wmean_x) * (sub['emp_growth_w'] - wmean_y)).sum() / w.sum()
        wvar_x = (w * (sub['spec_residual'] - wmean_x)**2).sum() / w.sum()
        wvar_y = (w * (sub['emp_growth_w'] - wmean_y)**2).sum() / w.sum()
        r_w = wcov / (np.sqrt(wvar_x) * np.sqrt(wvar_y)) if wvar_x > 0 and wvar_y > 0 else 0
    else:
        r_w = 0

    print(f"\n  {label} (N={len(sub)}):")
    print(f"    Spearman r = {r_s:.3f} (p = {p_s:.4f})")
    print(f"    Pearson  r = {r_p:.3f} (p = {p_p:.4f})")
    print(f"    Emp-weighted Pearson r = {r_w:.3f}")

# =============================================================================
# Test 3: Employment decomposition — above-median complexity only
# =============================================================================
print("\n" + "=" * 80)
print("TEST 3: EMPLOYMENT DECOMPOSITION (ABOVE-MEDIAN COMPLEXITY ONLY)")
print("Recomputing exhibit 2 restricted to cognitively complex occupations")
print("=" * 80)

# Use only occupations with PC1 >= median
high_cpx_panel = panel[panel['complexity_pc1'] >= median_pc1].copy()

resid_cuts = high_cpx_panel['spec_residual'].dropna().quantile([1/3, 2/3]).values
mgmt_cuts = high_cpx_panel['spec_score'].dropna().quantile([1/3, 2/3]).values

print(f"\nTercile cuts (above-median complexity only):")
print(f"  Management gradient: [{mgmt_cuts[0]:.3f}, {mgmt_cuts[1]:.3f}]")
print(f"  Spec residual: [{resid_cuts[0]:.3f}, {resid_cuts[1]:.3f}]")

decomp_rows = []
for year in years:
    emp_col = f'emp_{year}'
    valid = high_cpx_panel.dropna(subset=[emp_col, 'spec_score', 'spec_residual'])

    mgmt_top_mask = valid['spec_score'] > mgmt_cuts[1]
    mgmt_top_total = valid.loc[mgmt_top_mask, emp_col].sum()

    spec_and_mgmt = mgmt_top_mask & (valid['spec_residual'] > resid_cuts[1])
    spec_component = valid.loc[spec_and_mgmt, emp_col].sum()
    complexity_component = mgmt_top_total - spec_component

    mgmt_bot = valid.loc[valid['spec_score'] < mgmt_cuts[0], emp_col].sum()

    decomp_rows.append({
        'year': year,
        'mgmt_top_total': mgmt_top_total,
        'spec_component': spec_component,
        'complexity_component': complexity_component,
        'exec_bottom': mgmt_bot,
    })

decomp = pd.DataFrame(decomp_rows)
decomp.to_csv(os.path.join(ANALYSIS, 'robustness_complexity_split_decomp.csv'), index=False)

print(f"\n{'Year':>6} {'Mgmt Top(M)':>12} {'Spec Comp(M)':>13} {'Cpx Comp(M)':>12} {'Exec Bot(M)':>12}")
print("-" * 58)
for _, row in decomp.iterrows():
    print(f"{int(row['year']):>6} {row['mgmt_top_total']/1e6:>12.1f} "
          f"{row['spec_component']/1e6:>13.1f} "
          f"{row['complexity_component']/1e6:>12.1f} "
          f"{row['exec_bottom']/1e6:>12.1f}")

# Compute deltas
first = decomp.iloc[0]
last = decomp.iloc[-1]
print(f"\nChanges ({int(first['year'])}-{int(last['year'])}):")
for col, label in [('mgmt_top_total', 'Mgmt-task top'),
                    ('spec_component', 'Spec-specific'),
                    ('complexity_component', 'Complexity-driven'),
                    ('exec_bottom', 'Execution bottom')]:
    delta = (last[col] - first[col]) / 1e6
    pct = (last[col] - first[col]) / first[col] * 100
    print(f"  {label:<20}: {delta:+.1f}M ({pct:+.0f}%)")

# =============================================================================
# Summary figure: side-by-side comparison
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7), sharey=True)

# Panel A: Full sample (from generate_exhibits.py data)
full_panel = panel.copy()
full_resid_cuts = full_panel['spec_residual'].dropna().quantile([1/3, 2/3]).values
full_mgmt_cuts = full_panel['spec_score'].dropna().quantile([1/3, 2/3]).values

full_decomp = []
for year in years:
    emp_col = f'emp_{year}'
    valid = full_panel.dropna(subset=[emp_col, 'spec_score', 'spec_residual'])
    mgmt_top_mask = valid['spec_score'] > full_mgmt_cuts[1]
    mgmt_top_total = valid.loc[mgmt_top_mask, emp_col].sum()
    spec_and_mgmt = mgmt_top_mask & (valid['spec_residual'] > full_resid_cuts[1])
    spec_comp = valid.loc[spec_and_mgmt, emp_col].sum()
    cpx_comp = mgmt_top_total - spec_comp
    mgmt_bot = valid.loc[valid['spec_score'] < full_mgmt_cuts[0], emp_col].sum()
    full_decomp.append({
        'year': year, 'mgmt_top_total': mgmt_top_total,
        'spec_component': spec_comp, 'complexity_component': cpx_comp,
        'exec_bottom': mgmt_bot,
    })
full_decomp = pd.DataFrame(full_decomp)

for ax, df, title_suffix in [
    (axes[0], full_decomp, "All Occupations"),
    (axes[1], decomp, "Above-Median Complexity Only"),
]:
    yr = df['year']
    spec = df['spec_component'] / 1e6
    cpx = df['complexity_component'] / 1e6
    bot = df['exec_bottom'] / 1e6

    ax.fill_between(yr, 0, spec, alpha=0.35, color='#2E7D32')
    ax.fill_between(yr, spec, spec + cpx, alpha=0.25, color='#C62828')

    ax.plot(yr, spec, '-^', color='#2E7D32', linewidth=2, markersize=7,
            label='Specification-specific')
    ax.plot(yr, spec + cpx, '-o', color='#C62828', linewidth=2, markersize=7,
            label='Total management-task-intensive')
    ax.plot(yr, bot, '-s', color='#1565C0', linewidth=2, markersize=7,
            label='Execution-task-intensive')

    # Annotate deltas
    spec_delta = spec.iloc[-1] - spec.iloc[0]
    total_delta = (spec.iloc[-1] + cpx.iloc[-1]) - (spec.iloc[0] + cpx.iloc[0])
    bot_delta = bot.iloc[-1] - bot.iloc[0]

    ax.annotate(f'+{total_delta:.0f}M total',
                xy=(yr.iloc[-1], spec.iloc[-1] + cpx.iloc[-1]),
                xytext=(6, 6), textcoords='offset points',
                fontsize=9, fontweight='bold', color='#C62828', va='bottom')
    ax.annotate(f'+{spec_delta:.0f}M spec',
                xy=(yr.iloc[-1], spec.iloc[-1]),
                xytext=(6, -4), textcoords='offset points',
                fontsize=9, fontweight='bold', color='#2E7D32', va='top')
    ax.annotate(f'+{bot_delta:.0f}M',
                xy=(yr.iloc[-1], bot.iloc[-1]),
                xytext=(6, 0), textcoords='offset points',
                fontsize=9, fontweight='bold', color='#1565C0', va='center')

    ax.set_xticks(yr)
    ax.set_xticklabels([str(int(y)) for y in yr])
    ax.set_xlabel('Year', fontsize=11)
    ax.set_title(title_suffix, fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=8, loc='upper left')

axes[0].set_ylabel('Employment (millions of workers)', fontsize=11)

fig.suptitle('Robustness: Does the Specification Signal Survive\n'
             'Restricting to Cognitively Complex Occupations?',
             fontsize=14, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'robustness_complexity_split.png'),
            dpi=250, bbox_inches='tight')
plt.close()
print(f"\nSaved: robustness_complexity_split.png")

print("\n" + "=" * 80)
print("COMPLETE")
print("=" * 80)
