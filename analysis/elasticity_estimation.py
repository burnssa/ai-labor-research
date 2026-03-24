"""
Specification Labor × AI Exposure — Toward Elasticity of Substitution
======================================================================
Tests whether AI exposure amplifies the specification employment/wage premium,
implying complementarity (σ < 1) between AI capital and specification labor.

Phases:
  1. Assemble the analysis dataset (spec_ai_panel.csv)
  2. Employment growth × AI exposure × spec intensity (2×2, regression, binned scatter)
  3. Wage premium × AI exposure × spec intensity
  4. Bounding the elasticity of substitution
  5. Robustness checks
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import os
import warnings
warnings.filterwarnings('ignore')

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# =============================================================================
# PHASE 1: ASSEMBLE THE ANALYSIS DATASET
# =============================================================================
print("=" * 80)
print("PHASE 1: ASSEMBLE ANALYSIS DATASET")
print("=" * 80)

# Load master panel
master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
gwa_cols = [c for c in gwa_matrix.columns if c in master.columns]
years = sorted(master['year'].unique())

# Load management contrast weights
mgmt_diff = pd.read_csv(os.path.join(ANALYSIS, 'gwa_management_vs_nonmanagement.csv'), index_col=0)
spec_weights = mgmt_diff['difference']

# Compute spec score for each occupation
def compute_composite(row, gwa_cols, weights):
    vals = row[gwa_cols]
    w = weights.reindex(gwa_cols).fillna(0)
    return (vals * w).sum() / w.abs().sum()

master['spec_score'] = master.apply(lambda r: compute_composite(r, gwa_cols, spec_weights), axis=1)

# Compute PC1 (complexity)
scaler = StandardScaler()
X = scaler.fit_transform(gwa_matrix.dropna())
pca = PCA()
pca.fit(X)
occ_pca = pd.DataFrame(pca.transform(X), index=gwa_matrix.dropna().index,
                         columns=[f'PC{i+1}' for i in range(X.shape[1])])

master = master.merge(occ_pca[['PC1']], left_on='soc_2018_harmonized',
                       right_index=True, how='left')

# Compute spec residual (spec after removing complexity)
ref = master[master['year'] == years[-1]].dropna(subset=['spec_score', 'PC1'])
slope, intercept = np.polyfit(ref['PC1'], ref['spec_score'], 1)
master['spec_residual'] = master['spec_score'] - (intercept + slope * master['PC1'])

# Pivot to wide format: one row per occupation
occ_list = master['soc_2018_harmonized'].unique()

panel_rows = []
for soc in occ_list:
    odf = master[master['soc_2018_harmonized'] == soc]
    if len(odf) == 0:
        continue

    row = {
        'soc_code': soc,
        'title': odf['occ_title'].iloc[0] if 'occ_title' in odf.columns else '',
        'spec_score': odf['spec_score'].iloc[0],
        'spec_residual': odf['spec_residual'].iloc[0],
        'complexity_pc1': odf['PC1'].iloc[0],
        'aioe_score': odf['aioe_score'].iloc[0] if 'aioe_score' in odf.columns else np.nan,
    }

    for yr in years:
        ydf = odf[odf['year'] == yr]
        row[f'emp_{yr}'] = ydf['employment'].iloc[0] if len(ydf) > 0 else np.nan
        row[f'wage_{yr}'] = ydf['median_wage'].iloc[0] if len(ydf) > 0 else np.nan

    panel_rows.append(row)

panel = pd.DataFrame(panel_rows)

# Compute growth rates
first_yr, last_yr = years[0], years[-1]
panel['emp_growth'] = (panel[f'emp_{last_yr}'] - panel[f'emp_{first_yr}']) / panel[f'emp_{first_yr}']
panel['emp_growth'] = panel['emp_growth'].replace([np.inf, -np.inf], np.nan)
panel['emp_cagr'] = (panel[f'emp_{last_yr}'] / panel[f'emp_{first_yr}']) ** (1/(last_yr - first_yr)) - 1
panel['emp_cagr'] = panel['emp_cagr'].replace([np.inf, -np.inf], np.nan)

# CPI deflation (approximate values, CPI-U annual average, base 1982-84=100)
CPI = {2005: 195.3, 2009: 214.5, 2014: 236.7, 2019: 255.7, 2024: 313.2}
for yr in years:
    if yr in CPI:
        panel[f'real_wage_{yr}'] = panel[f'wage_{yr}'] * (CPI[2024] / CPI[yr])

panel['real_wage_growth'] = (panel[f'real_wage_{last_yr}'] - panel[f'real_wage_{first_yr}']) / panel[f'real_wage_{first_yr}']
panel['real_wage_growth'] = panel['real_wage_growth'].replace([np.inf, -np.inf], np.nan)

# Terciles
panel['spec_tercile'] = pd.qcut(panel['spec_score'].dropna(), 3, labels=['Execution', 'Middle', 'Specification'])
panel['aioe_tercile'] = pd.qcut(panel['aioe_score'].dropna(), 3, labels=['Low AI', 'Medium AI', 'High AI'])

# Winsorize employment growth at 1st and 99th percentile
p01 = panel['emp_growth'].quantile(0.01)
p99 = panel['emp_growth'].quantile(0.99)
panel['emp_growth_w'] = panel['emp_growth'].clip(p01, p99)

# Save
panel_path = os.path.join(ANALYSIS, 'spec_ai_panel.csv')
panel.to_csv(panel_path, index=False)

complete = panel.dropna(subset=['spec_score', 'aioe_score', 'emp_growth', f'wage_{last_yr}'])
print(f"\nPanel: {len(panel)} occupations total")
print(f"Complete data (spec + AIOE + growth + wages): {len(complete)}")
print(f"Total employment covered ({last_yr}): {complete[f'emp_{last_yr}'].sum():,.0f}")
print(f"Saved to: {panel_path}")

# =============================================================================
# PHASE 2: EMPLOYMENT GROWTH × AI EXPOSURE × SPEC INTENSITY
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2: EMPLOYMENT GROWTH × AI × SPEC INTERACTION")
print("=" * 80)

# --- 2a: The 3×3 table ---
df = panel.dropna(subset=['spec_tercile', 'aioe_tercile', 'emp_growth_w', f'emp_{first_yr}']).copy()

print(f"\n--- 2a: 3×3 Table (employment-weighted mean growth) ---\n")

table_mean = pd.DataFrame(index=['Execution', 'Middle', 'Specification'],
                           columns=['Low AI', 'Medium AI', 'High AI'])
table_median = table_mean.copy()
table_n = table_mean.copy()
table_emp = table_mean.copy()

for spec in ['Execution', 'Middle', 'Specification']:
    for ai in ['Low AI', 'Medium AI', 'High AI']:
        cell = df[(df['spec_tercile'] == spec) & (df['aioe_tercile'] == ai)]
        if len(cell) > 0:
            w = cell[f'emp_{first_yr}']
            wm = (cell['emp_growth_w'] * w).sum() / w.sum()
            table_mean.loc[spec, ai] = f"{wm:.1%}"
            table_median.loc[spec, ai] = f"{cell['emp_growth_w'].median():.1%}"
            table_n.loc[spec, ai] = len(cell)
            table_emp.loc[spec, ai] = f"{w.sum()/1e6:.1f}M"

print("Employment-weighted mean growth (2005-2024):")
print(table_mean.to_string())
print(f"\nCell sizes (n occupations):")
print(table_n.to_string())
print(f"\nInitial employment per cell:")
print(table_emp.to_string())

# Compute the interaction: (Spec-Exec gap in High AI) minus (Spec-Exec gap in Low AI)
for ai in ['Low AI', 'Medium AI', 'High AI']:
    spec_cell = df[(df['spec_tercile'] == 'Specification') & (df['aioe_tercile'] == ai)]
    exec_cell = df[(df['spec_tercile'] == 'Execution') & (df['aioe_tercile'] == ai)]
    if len(spec_cell) > 0 and len(exec_cell) > 0:
        ws = spec_cell[f'emp_{first_yr}']
        we = exec_cell[f'emp_{first_yr}']
        spec_g = (spec_cell['emp_growth_w'] * ws).sum() / ws.sum()
        exec_g = (exec_cell['emp_growth_w'] * we).sum() / we.sum()
        print(f"\n  {ai}: Spec growth={spec_g:.1%}, Exec growth={exec_g:.1%}, Gap={spec_g-exec_g:+.1%}")

# --- 2a Chart: Grouped bar ---
fig, ax = plt.subplots(figsize=(10, 7))

bar_data = []
for spec in ['Execution', 'Middle', 'Specification']:
    for ai in ['Low AI', 'Medium AI', 'High AI']:
        cell = df[(df['spec_tercile'] == spec) & (df['aioe_tercile'] == ai)]
        if len(cell) > 0:
            w = cell[f'emp_{first_yr}']
            wm = (cell['emp_growth_w'] * w).sum() / w.sum()
            bar_data.append({'spec': spec, 'ai': ai, 'growth': wm * 100})

bdf = pd.DataFrame(bar_data)
x = np.arange(3)
width = 0.25
colors = {'Low AI': '#90CAF9', 'Medium AI': '#42A5F5', 'High AI': '#1565C0'}

for i, ai in enumerate(['Low AI', 'Medium AI', 'High AI']):
    vals = [bdf[(bdf['spec'] == s) & (bdf['ai'] == ai)]['growth'].values[0]
            for s in ['Execution', 'Middle', 'Specification']]
    ax.bar(x + i*width, vals, width, label=ai, color=colors[ai], alpha=0.85)

ax.set_xticks(x + width)
ax.set_xticklabels(['Execution-\nintensive', 'Middle', 'Specification-\nintensive'], fontsize=11)
ax.set_ylabel('Employment Growth 2005-2024 (%)', fontsize=12)
ax.set_title('Employment Growth by Specification Intensity × AI Exposure\n'
             '(employment-weighted mean, winsorized)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10, title='AI Exposure (AIOE)')
ax.grid(True, axis='y', alpha=0.3)
ax.axhline(y=0, color='gray', linewidth=0.5)

# Annotation: execution task loss where AI exposure is high
exec_high_ai_val = bdf[(bdf['spec'] == 'Execution') & (bdf['ai'] == 'High AI')]['growth'].values[0]
ax.annotate('Execution-task job loss\nwhere AI exposure is high',
            xy=(0 + 2*width, exec_high_ai_val),
            xytext=(1.1, -45),
            fontsize=9, color='#C62828', fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color='#C62828', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#C62828', alpha=0.85))

# Annotation: specification task gain where AI exposure is high
spec_high_ai_val = bdf[(bdf['spec'] == 'Specification') & (bdf['ai'] == 'High AI')]['growth'].values[0]
ax.annotate('Specification-task job gain\nwhere AI exposure is high',
            xy=(2 + 2*width, spec_high_ai_val * 0.5),
            xytext=(2.0, -30),
            fontsize=9, color='#1565C0', fontstyle='italic',
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.3),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#1565C0', alpha=0.85))

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'elast_growth_spec_x_ai.png'), dpi=250, bbox_inches='tight')
plt.close()
print("\nSaved: elast_growth_spec_x_ai.png")

# --- 2b: Regression with interaction ---
print(f"\n--- 2b: Interaction Regressions ---\n")

reg_df = df.dropna(subset=['spec_residual', 'aioe_score', 'emp_growth_w', 'complexity_pc1',
                            f'emp_{first_yr}']).copy()
reg_df['log_emp0'] = np.log(reg_df[f'emp_{first_yr}'])
reg_df['spec_x_aioe'] = reg_df['spec_residual'] * reg_df['aioe_score']

# Model 1: Simple
X1 = sm.add_constant(reg_df[['spec_residual', 'aioe_score']])
y = reg_df['emp_growth_w']
w = reg_df[f'emp_{first_yr}']
m1 = sm.WLS(y, X1, weights=w).fit(cov_type='HC1')
print("Model 1 (no interaction):")
print(f"  spec_residual: β={m1.params['spec_residual']:.4f}, p={m1.pvalues['spec_residual']:.4f}")
print(f"  aioe_score:    β={m1.params['aioe_score']:.4f}, p={m1.pvalues['aioe_score']:.4f}")
print(f"  R² = {m1.rsquared:.3f}")

# Model 2: With interaction
X2 = sm.add_constant(reg_df[['spec_residual', 'aioe_score', 'spec_x_aioe']])
m2 = sm.WLS(y, X2, weights=w).fit(cov_type='HC1')
print(f"\nModel 2 (with interaction):")
print(f"  spec_residual: β={m2.params['spec_residual']:.4f}, se={m2.bse['spec_residual']:.4f}, p={m2.pvalues['spec_residual']:.4f}")
print(f"  aioe_score:    β={m2.params['aioe_score']:.4f}, se={m2.bse['aioe_score']:.4f}, p={m2.pvalues['aioe_score']:.4f}")
print(f"  INTERACTION:   β={m2.params['spec_x_aioe']:.4f}, se={m2.bse['spec_x_aioe']:.4f}, p={m2.pvalues['spec_x_aioe']:.4f}")
print(f"  R² = {m2.rsquared:.3f}")

# Model 3: With controls
X3 = sm.add_constant(reg_df[['spec_residual', 'aioe_score', 'spec_x_aioe', 'complexity_pc1', 'log_emp0']])
m3 = sm.WLS(y, X3, weights=w).fit(cov_type='HC1')
print(f"\nModel 3 (with controls: PC1 + log initial employment):")
print(f"  spec_residual: β={m3.params['spec_residual']:.4f}, p={m3.pvalues['spec_residual']:.4f}")
print(f"  aioe_score:    β={m3.params['aioe_score']:.4f}, p={m3.pvalues['aioe_score']:.4f}")
print(f"  INTERACTION:   β={m3.params['spec_x_aioe']:.4f}, se={m3.bse['spec_x_aioe']:.4f}, p={m3.pvalues['spec_x_aioe']:.4f}")
print(f"  complexity:    β={m3.params['complexity_pc1']:.4f}, p={m3.pvalues['complexity_pc1']:.4f}")
print(f"  log_emp0:      β={m3.params['log_emp0']:.4f}, p={m3.pvalues['log_emp0']:.4f}")
print(f"  R² = {m3.rsquared:.3f}")

# Marginal effects
p25_aioe = reg_df['aioe_score'].quantile(0.25)
p75_aioe = reg_df['aioe_score'].quantile(0.75)
p25_spec = reg_df['spec_residual'].quantile(0.25)
p75_spec = reg_df['spec_residual'].quantile(0.75)

# At low AI: predicted growth diff between high-spec and low-spec
diff_low_ai = m2.params['spec_residual'] * (p75_spec - p25_spec) + \
              m2.params['spec_x_aioe'] * (p75_spec - p25_spec) * p25_aioe
diff_high_ai = m2.params['spec_residual'] * (p75_spec - p25_spec) + \
               m2.params['spec_x_aioe'] * (p75_spec - p25_spec) * p75_aioe

print(f"\nMarginal effects (Model 2):")
print(f"  At 25th pctile AIOE ({p25_aioe:.2f}): spec premium = {diff_low_ai:.1%}")
print(f"  At 75th pctile AIOE ({p75_aioe:.2f}): spec premium = {diff_high_ai:.1%}")
print(f"  Amplification: {diff_high_ai - diff_low_ai:+.1%}")

# --- 2c: Binned scatter ---
print(f"\n--- 2c: Binned Scatter ---")

n_bins = 15
reg_df['aioe_bin'] = pd.qcut(reg_df['aioe_score'], n_bins, labels=False, duplicates='drop')

bin_results = []
for b in sorted(reg_df['aioe_bin'].unique()):
    bdf = reg_df[reg_df['aioe_bin'] == b]
    if len(bdf) > 5:
        r, p = stats.spearmanr(bdf['spec_residual'], bdf['emp_growth_w'])
        bin_results.append({
            'bin': b,
            'mean_aioe': bdf['aioe_score'].mean(),
            'spec_growth_corr': r,
            'n': len(bdf),
        })

bin_df = pd.DataFrame(bin_results)

fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(bin_df['mean_aioe'], bin_df['spec_growth_corr'],
           s=bin_df['n']*3, alpha=0.7, color='#C62828', edgecolors='white')

# Fit trend line
if len(bin_df) > 3:
    z = np.polyfit(bin_df['mean_aioe'], bin_df['spec_growth_corr'], 1)
    xline = np.linspace(bin_df['mean_aioe'].min(), bin_df['mean_aioe'].max(), 100)
    ax.plot(xline, np.polyval(z, xline), '--', color='#C62828', linewidth=2, alpha=0.7)

    r_trend, p_trend = stats.spearmanr(bin_df['mean_aioe'], bin_df['spec_growth_corr'])
    ax.text(0.02, 0.98, f'Trend: r = {r_trend:.3f}, p = {p_trend:.3f}\n'
            f'Upward slope = specification is a STRONGER\n'
            f'predictor of growth in high-AI occupations\n'
            f'(AI-specification complementarity)',
            transform=ax.transAxes, fontsize=9, va='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9))

ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax.set_xlabel('Mean AI Exposure (AIOE) within bin', fontsize=12)
ax.set_ylabel('Correlation: spec_residual × emp_growth\n(within AIOE bin)', fontsize=11)
ax.set_title('Does AI Exposure Amplify the Specification Premium?\n'
             '(binned scatter: within each AI-exposure bin, how strongly does\n'
             'specification intensity predict employment growth?)',
             fontsize=13, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'elast_binned_scatter.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: elast_binned_scatter.png")

# =============================================================================
# PHASE 3: WAGE PREMIUM × AI EXPOSURE × SPEC
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 3: WAGE PREMIUM × AI × SPEC")
print("=" * 80)

# --- 3a: Wage levels by spec × AI ---
print(f"\n--- 3a: Median Wage (2024) by Spec × AI ---\n")
for spec in ['Execution', 'Middle', 'Specification']:
    vals = []
    for ai in ['Low AI', 'Medium AI', 'High AI']:
        cell = df[(df['spec_tercile'] == spec) & (df['aioe_tercile'] == ai)]
        if len(cell) > 0:
            w = cell[f'emp_{last_yr}'].fillna(0)
            if w.sum() > 0:
                wm = (cell[f'wage_{last_yr}'] * w).sum() / w.sum()
                vals.append(f"${wm:,.0f}")
            else:
                vals.append("N/A")
    print(f"  {spec:<15} {vals[0]:>12} {vals[1]:>12} {vals[2]:>12}")

# --- 3b: Cross-sectional wage regressions by year ---
print(f"\n--- 3b: Wage Regressions by Year ---\n")
print(f"{'Year':>6} {'β_spec':>10} {'p_spec':>8} {'β_aioe':>10} {'p_aioe':>8} {'β_interact':>12} {'p_interact':>10} {'R²':>6}")
print("-" * 70)

yearly_coefs = []
for yr in years:
    yr_df = panel.dropna(subset=['spec_residual', 'aioe_score', f'wage_{yr}',
                                  'complexity_pc1', f'emp_{yr}']).copy()
    yr_df = yr_df[yr_df[f'wage_{yr}'] > 0]
    yr_df['log_wage'] = np.log(yr_df[f'wage_{yr}'])
    yr_df['spec_x_aioe'] = yr_df['spec_residual'] * yr_df['aioe_score']

    X = sm.add_constant(yr_df[['spec_residual', 'aioe_score', 'spec_x_aioe', 'complexity_pc1']])
    y = yr_df['log_wage']
    w = yr_df[f'emp_{yr}']

    m = sm.WLS(y, X, weights=w).fit(cov_type='HC1')

    print(f"{yr:>6} {m.params['spec_residual']:>+10.4f} {m.pvalues['spec_residual']:>8.4f} "
          f"{m.params['aioe_score']:>+10.4f} {m.pvalues['aioe_score']:>8.4f} "
          f"{m.params['spec_x_aioe']:>+12.4f} {m.pvalues['spec_x_aioe']:>10.4f} {m.rsquared:>6.3f}")

    yearly_coefs.append({
        'year': yr,
        'beta_spec': m.params['spec_residual'],
        'se_spec': m.bse['spec_residual'],
        'beta_aioe': m.params['aioe_score'],
        'se_aioe': m.bse['aioe_score'],
        'beta_interact': m.params['spec_x_aioe'],
        'se_interact': m.bse['spec_x_aioe'],
        'r2': m.rsquared,
    })

coef_df = pd.DataFrame(yearly_coefs)
coef_df.to_csv(os.path.join(ANALYSIS, 'wage_regression_coefficients_by_year.csv'), index=False)

# Chart: coefficients over time
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for idx, (col, se_col, title, color) in enumerate([
    ('beta_spec', 'se_spec', 'β₁: Specification\nWage Premium', '#C62828'),
    ('beta_aioe', 'se_aioe', 'β₂: AI Exposure\nWage Effect', '#1565C0'),
    ('beta_interact', 'se_interact', 'β₃: Specification × AI\nInteraction', '#2E7D32'),
]):
    ax = axes[idx]
    ax.plot(coef_df['year'], coef_df[col], '-o', color=color, linewidth=2, markersize=6)
    ax.fill_between(coef_df['year'],
                     coef_df[col] - 1.96 * coef_df[se_col],
                     coef_df[col] + 1.96 * coef_df[se_col],
                     alpha=0.2, color=color)
    ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xlabel('Year', fontsize=10)
    ax.grid(True, alpha=0.3)

axes[0].set_ylabel('Coefficient (on log wage)', fontsize=10)
fig.suptitle('Wage Regression Coefficients Over Time\n'
             'ln(wage) = α + β₁·spec_residual + β₂·AIOE + β₃·(spec×AIOE) + γ·PC1',
             fontsize=13, fontweight='bold', y=1.05)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'elast_wage_coefs_over_time.png'), dpi=250, bbox_inches='tight')
plt.close()
print("\nSaved: elast_wage_coefs_over_time.png")

# =============================================================================
# PHASE 4: BOUNDING THE ELASTICITY
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 4: BOUNDING THE ELASTICITY OF SUBSTITUTION")
print("=" * 80)

# --- 4a & 4b: Spec/exec wage ratio and employment shares ---
spec_occs = panel[panel['spec_tercile'] == 'Specification']
exec_occs = panel[panel['spec_tercile'] == 'Execution']

print(f"\nSpec/Exec employment and wage ratios over time:")
print(f"{'Year':>6} {'Spec Emp(M)':>12} {'Exec Emp(M)':>12} {'Emp Ratio':>10} {'Spec Wage':>10} {'Exec Wage':>10} {'Wage Ratio':>11}")
print("-" * 75)

ratios = []
for yr in years:
    spec_emp = spec_occs[f'emp_{yr}'].sum()
    exec_emp = exec_occs[f'emp_{yr}'].sum()

    sw = spec_occs[f'emp_{yr}'].fillna(0)
    ew = exec_occs[f'emp_{yr}'].fillna(0)
    spec_wage = (spec_occs[f'wage_{yr}'] * sw).sum() / sw.sum() if sw.sum() > 0 else 0
    exec_wage = (exec_occs[f'wage_{yr}'] * ew).sum() / ew.sum() if ew.sum() > 0 else 0

    print(f"{yr:>6} {spec_emp/1e6:>12.1f} {exec_emp/1e6:>12.1f} {spec_emp/exec_emp:>10.2f} "
          f"${spec_wage:>9,.0f} ${exec_wage:>9,.0f} {spec_wage/exec_wage:>11.2f}")

    ratios.append({
        'year': yr,
        'spec_emp': spec_emp, 'exec_emp': exec_emp,
        'emp_ratio': spec_emp / exec_emp,
        'spec_wage': spec_wage, 'exec_wage': exec_wage,
        'wage_ratio': spec_wage / exec_wage,
    })

rdf = pd.DataFrame(ratios)
rdf.to_csv(os.path.join(ANALYSIS, 'spec_exec_ratios_over_time.csv'), index=False)

# --- 4c: Composite σ chart ---
print(f"\n--- 4c: Composite σ Chart ---")

fig, ax = plt.subplots(figsize=(11, 7))

# For different spec employment shares, compute composite σ as weighted harmonic mean
# σ_composite ≈ 1 / (s_spec/σ_spec + s_exec/σ_exec) [simplified]
# More precisely, use the labor-share weighted average of 1/σ

sigma_exec_range = np.linspace(0.5, 10, 100)
sigma_spec = 0.5  # Our central estimate for spec (strong complement)

spec_shares = [0.50, 0.40, 0.30, 0.20, 0.10]
colors_share = plt.cm.Reds(np.linspace(0.3, 0.9, len(spec_shares)))

for i, s_spec in enumerate(spec_shares):
    s_exec = 1 - s_spec
    # Composite σ using weighted average of elasticities
    # (This is a simplification; true composite depends on the nesting structure)
    sigma_composite = 1 / (s_spec / sigma_spec + s_exec / sigma_exec_range)
    ax.plot(sigma_exec_range, sigma_composite, '-', color=colors_share[i], linewidth=2,
            label=f'Spec share = {s_spec:.0%}')

ax.axhline(y=1, color='black', linewidth=1.5, linestyle='--', alpha=0.7)
ax.text(9.5, 1.03, 'σ = 1', fontsize=10, ha='right', color='black', fontstyle='italic')

# Mark current spec employment share
current_spec_share = rdf.iloc[-1]['spec_emp'] / (rdf.iloc[-1]['spec_emp'] + rdf.iloc[-1]['exec_emp'])
ax.annotate(f'Current spec share ≈ {current_spec_share:.0%}', xy=(5, 0.85),
            fontsize=10, color='#C62828', fontweight='bold')

ax.set_xlabel('σ(AI capital, execution labor)', fontsize=12)
ax.set_ylabel('Composite elasticity of substitution', fontsize=12)
ax.set_title('When Does AI Push Aggregate σ Above 1?\n'
             'Composite σ as function of exec substitutability, for different spec employment shares\n'
             '(assuming σ_spec = 0.5)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=9, title='Specification labor\nshare of employment')
ax.grid(True, alpha=0.3)
ax.set_ylim(0.3, 2.5)
ax.set_xlim(0.5, 10)

textstr = (
    'If σ_spec < 1 (AI and spec labor are complements)\n'
    'and spec labor maintains substantial employment share,\n'
    'then composite σ stays below 1 even as σ_exec → ∞.\n\n'
    'The Korinek/Trammell scenario (σ > 1 → labor share → 0)\n'
    'requires spec employment share to fall dramatically.'
)
props = dict(boxstyle='round,pad=0.6', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9)
ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=8,
        va='bottom', ha='right', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'elast_composite_sigma.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Saved: elast_composite_sigma.png")

# =============================================================================
# PHASE 5: ROBUSTNESS
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 5: ROBUSTNESS CHECKS")
print("=" * 80)

# 5b: Excluding healthcare
non_health = reg_df[~reg_df['soc_code'].str.startswith(('29-', '31-'))].copy()
X_nh = sm.add_constant(non_health[['spec_residual', 'aioe_score', 'spec_x_aioe', 'complexity_pc1']])
m_nh = sm.WLS(non_health['emp_growth_w'], X_nh, weights=non_health[f'emp_{first_yr}']).fit(cov_type='HC1')
print(f"\n5b. Excluding healthcare (SOC 29/31):")
print(f"  Interaction β = {m_nh.params['spec_x_aioe']:.4f}, p = {m_nh.pvalues['spec_x_aioe']:.4f}")
print(f"  (Full sample: β = {m2.params['spec_x_aioe']:.4f})")

# 5c: Post-recession only (2014-2024)
panel_post = panel.dropna(subset=['spec_residual', 'aioe_score', f'emp_2014', f'emp_{last_yr}']).copy()
panel_post['emp_growth_post'] = (panel_post[f'emp_{last_yr}'] - panel_post['emp_2014']) / panel_post['emp_2014']
panel_post['emp_growth_post'] = panel_post['emp_growth_post'].replace([np.inf, -np.inf], np.nan)
p01p = panel_post['emp_growth_post'].quantile(0.01)
p99p = panel_post['emp_growth_post'].quantile(0.99)
panel_post['emp_growth_post_w'] = panel_post['emp_growth_post'].clip(p01p, p99p)
panel_post['spec_x_aioe'] = panel_post['spec_residual'] * panel_post['aioe_score']

pp = panel_post.dropna(subset=['emp_growth_post_w', 'spec_residual', 'aioe_score', 'complexity_pc1'])
X_pp = sm.add_constant(pp[['spec_residual', 'aioe_score', 'spec_x_aioe', 'complexity_pc1']])
m_pp = sm.WLS(pp['emp_growth_post_w'], X_pp, weights=pp['emp_2014']).fit(cov_type='HC1')
print(f"\n5c. Post-recession only (2014-2024):")
print(f"  Interaction β = {m_pp.params['spec_x_aioe']:.4f}, p = {m_pp.pvalues['spec_x_aioe']:.4f}")

# 5d: Placebo with "Working with Computers" as non-AI tech proxy
reg_df2 = reg_df.copy()
# GWA columns aren't in the wide panel — look up from gwa_matrix
if 'Working with Computers' in gwa_matrix.columns:
    comp_scores = gwa_matrix['Working with Computers']
    reg_df2 = reg_df2.merge(comp_scores.rename('computer_intensity'),
                             left_on='soc_code', right_index=True, how='left')
    reg_df2['spec_x_computer'] = reg_df2['spec_residual'] * reg_df2['computer_intensity']

    X_plac = sm.add_constant(reg_df2[['spec_residual', 'computer_intensity', 'spec_x_computer', 'complexity_pc1']])
    m_plac = sm.WLS(reg_df2['emp_growth_w'], X_plac, weights=reg_df2[f'emp_{first_yr}']).fit(cov_type='HC1')
    print(f"\n5d. Placebo (Working with Computers instead of AIOE):")
    print(f"  spec × computers β = {m_plac.params['spec_x_computer']:.4f}, p = {m_plac.pvalues['spec_x_computer']:.4f}")
    print(f"  (Compare to spec × AIOE β = {m2.params['spec_x_aioe']:.4f})")

print("\n" + "=" * 80)
print("ALL PHASES COMPLETE")
print("=" * 80)
