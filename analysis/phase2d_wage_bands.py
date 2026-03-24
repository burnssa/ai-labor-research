"""
Phase 2d Extension: Within-NRC Analysis by Wage Band
=====================================================
Controls for seniority by splitting NRC occupations into wage terciles
(based on 2005 median wage) and repeating the growing-vs-shrinking analysis.

Produces:
  - 3 individual bar charts (one per wage band)
  - CSV data for each band
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
ANALYSIS = os.path.join(ROOT, 'data', 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
gwa_cols = [c for c in gwa_matrix.columns if c in master.columns]

years = sorted(master['year'].unique())
first_year, last_year = years[0], years[-1]

# Define NRC occupations
nrc_positive = ['Analyzing Data or Information', 'Thinking Creatively',
                'Interpreting the Meaning of Information for Others',
                'Making Decisions and Solving Problems']
nrc_negative = ['Performing General Physical Activities',
                'Handling and Moving Objects',
                'Controlling Machines and Processes']

last_data = master[master['year'] == last_year].copy()
last_data['nrc_composite'] = last_data[nrc_positive].mean(axis=1) - last_data[nrc_negative].mean(axis=1)
nrc_threshold = last_data['nrc_composite'].median()
nrc_socs = set(last_data[last_data['nrc_composite'] >= nrc_threshold]['soc_2018_harmonized'])

# Employment growth
first_df = master[master['year'] == first_year][['soc_2018_harmonized', 'employment', 'median_wage', 'occ_title']].dropna()
last_df = master[master['year'] == last_year][['soc_2018_harmonized', 'employment', 'median_wage']].dropna()
merged = first_df.merge(last_df, on='soc_2018_harmonized', suffixes=('_first', '_last'))
merged['emp_growth'] = (merged['employment_last'] - merged['employment_first']) / merged['employment_first']
merged = merged.replace([np.inf, -np.inf], np.nan).dropna(subset=['emp_growth'])

nrc_merged = merged[merged['soc_2018_harmonized'].isin(nrc_socs)].copy()

# Assign wage bands using FIRST year median wage (locks occupations into bands)
wage_terciles = nrc_merged['median_wage_first'].quantile([1/3, 2/3]).values
nrc_merged['wage_band'] = pd.cut(nrc_merged['median_wage_first'],
                                  bins=[0, wage_terciles[0], wage_terciles[1], np.inf],
                                  labels=['Lower-pay', 'Mid-pay', 'Upper-pay'])

print(f"Wage band cuts (2005 median wage): ${wage_terciles[0]:,.0f}, ${wage_terciles[1]:,.0f}")

# GWA profiles for last year
last_gwa = master[master['year'] == last_year][['soc_2018_harmonized', 'employment'] + gwa_cols].dropna()

def emp_weighted_mean(df, cols, weight_col='employment_last'):
    w = df[weight_col].fillna(0)
    total = w.sum()
    if total == 0:
        return pd.Series({c: np.nan for c in cols})
    return pd.Series({c: (df[c] * w).sum() / total for c in cols})

# Compute diffs and charts for each band
band_configs = [
    ('Lower-pay', 'lowerpay_nrc', '$18K\u201340K median wage, n=99'),
    ('Mid-pay', 'midpay_nrc', '$40K\u201357K median wage, n=100'),
    ('Upper-pay', 'upperpay_nrc', '$57K\u2013142K median wage, n=99'),
]

for band_label, file_slug, subtitle in band_configs:
    band_df = nrc_merged[nrc_merged['wage_band'] == band_label].copy()
    median_growth = band_df['emp_growth'].median()

    growing = band_df[band_df['emp_growth'] >= median_growth]
    shrinking = band_df[band_df['emp_growth'] < median_growth]

    growing_profiles = growing[['soc_2018_harmonized', 'employment_last']].merge(
        last_gwa.drop(columns=['employment']), on='soc_2018_harmonized')
    shrinking_profiles = shrinking[['soc_2018_harmonized', 'employment_last']].merge(
        last_gwa.drop(columns=['employment']), on='soc_2018_harmonized')

    if len(growing_profiles) < 5 or len(shrinking_profiles) < 5:
        print(f"  {band_label}: too few occupations, skipping")
        continue

    grow_mean = emp_weighted_mean(growing_profiles, gwa_cols)
    shrink_mean = emp_weighted_mean(shrinking_profiles, gwa_cols)
    diff = grow_mean - shrink_mean

    pvals = {}
    for gwa in gwa_cols:
        g = growing_profiles[gwa].dropna()
        s = shrinking_profiles[gwa].dropna()
        if len(g) > 3 and len(s) > 3:
            _, p = stats.mannwhitneyu(g, s, alternative='two-sided')
            pvals[gwa] = p
        else:
            pvals[gwa] = np.nan

    result_df = pd.DataFrame({
        'shrinking': shrink_mean,
        'growing': grow_mean,
        'difference': diff,
        'p_value': pd.Series(pvals),
    })
    result_df.to_csv(os.path.join(ANALYSIS, f'gwa_within_nrc_{file_slug}.csv'))

    # --- Chart ---
    df = result_df.sort_values('difference', ascending=True)
    fig, ax = plt.subplots(figsize=(13, 15))

    colors = ['#C62828' if d > 0 else '#1565C0' for d in df['difference']]
    ax.barh(range(len(df)), df['difference'], color=colors, alpha=0.85, height=0.7)
    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df.index, fontsize=8.5)

    for i, (gwa, row) in enumerate(df.iterrows()):
        val = row['difference']
        q1 = row['shrinking']
        q5 = row['growing']
        sig = ''
        if row['p_value'] < 0.001: sig = '***'
        elif row['p_value'] < 0.01: sig = '**'
        elif row['p_value'] < 0.05: sig = '*'
        if abs(val) > 0.01:
            if val > 0:
                ax.text(val + 0.01, i, f'{val:+.2f}  ({q1:.1f} \u2192 {q5:.1f}) {sig}',
                        fontsize=7.5, va='center', ha='left', color='#333')
            else:
                ax.text(val - 0.01, i, f'{val:+.2f}  ({q5:.1f} \u2190 {q1:.1f}) {sig}',
                        fontsize=7.5, va='center', ha='right', color='#333')

    ax.axvline(x=0, color='black', linewidth=0.8)
    ax.grid(True, axis='x', alpha=0.2)
    ax.set_xlim(-0.65, 1.05)
    ax.set_xlabel('Difference in Mean GWA Importance (1-5 scale)\n'
                  'Growing minus Shrinking NRC occupations (within wage band)', fontsize=10)
    ax.set_title(f'Within {band_label}-pay NRC Occupations:\n'
                 f'Which Task Activities Distinguish Growing from Shrinking?\n({subtitle})',
                 fontsize=13, fontweight='bold', pad=15)

    # Annotation box - bottom right
    textstr = (
        'Growing = above-median employment\n'
        f'  growth within this wage band (2005\u21922024)\n'
        'Shrinking = below-median employment\n'
        f'  growth within this wage band\n\n'
        'Bar = mean GWA importance in growing\n'
        '  minus shrinking (employment-weighted)\n'
        'Parentheses: (shrinking \u2192 growing)\n'
        '  on the 1-5 importance scale\n\n'
        '*** p<0.001  ** p<0.01  * p<0.05'
    )
    props = dict(boxstyle='round,pad=0.8', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9)
    ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=7.5,
            verticalalignment='bottom', horizontalalignment='right', bbox=props)

    ax.text(0.98, 0.32, 'Red = more important in GROWING occupations',
            transform=ax.transAxes, fontsize=8.5, color='#C62828', fontweight='bold',
            ha='right', va='bottom')
    ax.text(0.98, 0.30, 'Blue = more important in SHRINKING occupations',
            transform=ax.transAxes, fontsize=8.5, color='#1565C0', fontweight='bold',
            ha='right', va='top')

    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES, f'p2d_nrc_{file_slug}.png'), dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  Saved: p2d_nrc_{file_slug}.png + CSV")

print("\nDone.")
