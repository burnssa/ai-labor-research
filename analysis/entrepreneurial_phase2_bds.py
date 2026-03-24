"""
Entrepreneurial Analysis Phase 2: BDS Firm Dynamics
=====================================================
Analyzes young-firm job creation share and startup rates by sector over time.

Uses:
  - bds2023_sec_fa.csv (sector × firm age)
  - bds2023_sec.csv (sector totals)
  - bds2023_fa.csv (economy-wide by firm age)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

def safe_numeric(series):
    """Convert to numeric, treating 'X' (suppressed), 'D', 'S' as NaN."""
    return pd.to_numeric(series, errors='coerce')

# NAICS sector names
SECTOR_NAMES = {
    '11': 'Agriculture', '21': 'Mining/Oil/Gas', '22': 'Utilities',
    '23': 'Construction', '31-33': 'Manufacturing', '42': 'Wholesale',
    '44-45': 'Retail', '48-49': 'Transportation', '51': 'Information',
    '52': 'Finance/Insurance', '53': 'Real Estate',
    '54': 'Prof/Sci/Technical', '55': 'Mgmt of Companies',
    '56': 'Admin/Support', '61': 'Education', '62': 'Healthcare',
    '71': 'Arts/Entertainment', '72': 'Accomm/Food Svc', '81': 'Other Services',
}

# Load data
sec_fa = pd.read_csv(os.path.join(DATA, 'bds', 'bds2023_sec_fa.csv'))
sec = pd.read_csv(os.path.join(DATA, 'bds', 'bds2023_sec.csv'))
fa = pd.read_csv(os.path.join(DATA, 'bds', 'bds2023_fa.csv'))

# Convert numeric columns
for df in [sec_fa, sec, fa]:
    for col in ['firms', 'estabs', 'emp', 'job_creation', 'job_creation_births',
                'job_creation_continuers', 'job_destruction', 'net_job_creation',
                'firmdeath_firms', 'firmdeath_emp', 'denom']:
        if col in df.columns:
            df[col] = safe_numeric(df[col])
    df['year'] = df['year'].astype(int)

print(f"sec_fa: {sec_fa.shape}, years: {sec_fa['year'].min()}-{sec_fa['year'].max()}")
print(f"Firm age values: {sorted(sec_fa['fage'].unique())}")

# Define young vs mature
YOUNG_AGES = ['a) 0', 'b) 1', 'c) 2', 'd) 3', 'e) 4', 'f) 5']
MATURE_AGES = ['h) 11 to 15', 'i) 16 to 20', 'j) 21 to 25', 'k) 26+']

# =============================================================================
# 2a. Young-Firm Job Creation Share by Sector Over Time
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2a: YOUNG-FIRM JOB CREATION SHARE")
print("=" * 80)

# Economy-wide first
print("\nEconomy-wide young-firm (age 0-5) share of job creation:")
econ_results = []
for year in sorted(fa['year'].unique()):
    ydf = fa[fa['year'] == year]
    young = ydf[ydf['fage'].isin(YOUNG_AGES)]
    all_firms = ydf

    young_jc = young['job_creation'].sum()
    total_jc = all_firms['job_creation'].sum()
    young_emp = young['emp'].sum()
    total_emp = all_firms['emp'].sum()

    if total_jc > 0 and total_emp > 0:
        econ_results.append({
            'year': year,
            'young_job_creation': young_jc,
            'total_job_creation': total_jc,
            'young_jc_share': young_jc / total_jc,
            'young_emp': young_emp,
            'total_emp': total_emp,
            'young_emp_share': young_emp / total_emp,
            'young_firms': young['firms'].sum(),
            'total_firms': all_firms['firms'].sum(),
        })

econ_df = pd.DataFrame(econ_results)
econ_df.to_csv(os.path.join(ANALYSIS, 'bds_economywide_young_firm_shares.csv'), index=False)

print(f"  {'Year':>6} {'Young JC Share':>15} {'Young Emp Share':>16} {'Young Firm Share':>16}")
for _, row in econ_df.iloc[::5].iterrows():  # every 5th year
    print(f"  {int(row['year']):>6} {row['young_jc_share']:>15.1%} {row['young_emp_share']:>16.1%} "
          f"{row['young_firms']/row['total_firms']:>16.1%}")

# By sector
sector_results = []
for sector in sorted(SECTOR_NAMES.keys()):
    for year in sorted(sec_fa['year'].unique()):
        sdf = sec_fa[(sec_fa['sector'] == sector) & (sec_fa['year'] == year)]
        young = sdf[sdf['fage'].isin(YOUNG_AGES)]
        all_ages = sdf

        young_jc = young['job_creation'].sum()
        total_jc = all_ages['job_creation'].sum()
        young_emp = young['emp'].sum()
        total_emp = all_ages['emp'].sum()

        if total_jc > 0 and total_emp > 0:
            sector_results.append({
                'sector': sector,
                'sector_name': SECTOR_NAMES.get(sector, sector),
                'year': year,
                'young_jc_share': young_jc / total_jc,
                'young_emp_share': young_emp / total_emp,
            })

sector_df = pd.DataFrame(sector_results)
sector_df.to_csv(os.path.join(ANALYSIS, 'bds_sector_young_firm_shares.csv'), index=False)

# --- Economy-wide chart ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

ax1.plot(econ_df['year'], econ_df['young_jc_share'] * 100, '-o', color='#C62828',
         markersize=3, linewidth=2, label='Young firms (age 0-5)')
ax1.set_ylabel('Share of Total Job Creation (%)', fontsize=11)
ax1.set_title('Young-Firm Share of Job Creation (Economy-Wide, 1978-2023)',
              fontsize=13, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()

ax2.plot(econ_df['year'], econ_df['young_emp_share'] * 100, '-o', color='#1565C0',
         markersize=3, linewidth=2, label='Young firms (age 0-5)')
ax2.set_ylabel('Share of Total Employment (%)', fontsize=11)
ax2.set_xlabel('Year', fontsize=11)
ax2.set_title('Young-Firm Share of Employment (Economy-Wide, 1978-2023)',
              fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_young_firm_share_economywide.png'), dpi=250, bbox_inches='tight')
plt.close()
print("\nSaved: ent_young_firm_share_economywide.png")

# --- Sector facets: young-firm job creation share ---
focus_sectors = ['31-33', '54', '51', '71', '62', '44-45', '72', '23']
focus_names = [SECTOR_NAMES[s] for s in focus_sectors]

fig, axes = plt.subplots(2, 4, figsize=(20, 8), sharey=True)
axes = axes.flatten()

for idx, sector in enumerate(focus_sectors):
    ax = axes[idx]
    sdf = sector_df[sector_df['sector'] == sector]
    ax.plot(sdf['year'], sdf['young_jc_share'] * 100, '-', color='#C62828', linewidth=1.5)
    ax.set_title(SECTOR_NAMES[sector], fontsize=10, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1978, 2023)
    if idx >= 4:
        ax.set_xlabel('Year', fontsize=9)
    if idx % 4 == 0:
        ax.set_ylabel('Young-Firm JC Share (%)', fontsize=9)

fig.suptitle('Young-Firm (Age 0-5) Share of Job Creation by Sector',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_young_firm_jc_by_sector.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: ent_young_firm_jc_by_sector.png")

# =============================================================================
# 2b. Startup Rate Trends by Sector
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 2b: STARTUP RATES BY SECTOR")
print("=" * 80)

# From sec_fa, get age-0 firms and employment
startup_results = []
for sector in sorted(SECTOR_NAMES.keys()):
    for year in sorted(sec_fa['year'].unique()):
        age0 = sec_fa[(sec_fa['sector'] == sector) & (sec_fa['year'] == year) & (sec_fa['fage'] == 'a) 0')]
        total = sec[(sec['sector'] == sector) & (sec['year'] == year)]

        if len(age0) > 0 and len(total) > 0:
            new_firms = age0['firms'].sum()
            total_firms = safe_numeric(total['firms']).sum()
            new_emp = age0['emp'].sum()
            total_emp = safe_numeric(total['emp']).sum()

            if total_firms > 0 and total_emp > 0:
                startup_results.append({
                    'sector': sector,
                    'sector_name': SECTOR_NAMES.get(sector, sector),
                    'year': year,
                    'startup_rate': new_firms / total_firms,
                    'startup_emp_share': new_emp / total_emp,
                    'new_firms': new_firms,
                    'new_firm_emp': new_emp,
                })

startup_df = pd.DataFrame(startup_results)
startup_df.to_csv(os.path.join(ANALYSIS, 'bds_startup_rates_by_sector.csv'), index=False)

# Compute change in startup rate by sector
startup_change = []
for sector in SECTOR_NAMES:
    early = startup_df[(startup_df['sector'] == sector) & (startup_df['year'] <= 1985)]
    late = startup_df[(startup_df['sector'] == sector) & (startup_df['year'] >= 2019)]
    if len(early) > 0 and len(late) > 0:
        early_rate = early['startup_rate'].mean()
        late_rate = late['startup_rate'].mean()
        startup_change.append({
            'sector': sector,
            'sector_name': SECTOR_NAMES[sector],
            'early_rate': early_rate,
            'late_rate': late_rate,
            'change': late_rate - early_rate,
            'pct_change': (late_rate - early_rate) / early_rate * 100,
        })

startup_change_df = pd.DataFrame(startup_change).sort_values('change', ascending=False)
print(f"\nStartup rate change (avg 1978-85 vs avg 2019-23):")
print(f"{'Sector':<22} {'Early':>7} {'Late':>7} {'Change':>8}")
print("-" * 48)
for _, row in startup_change_df.iterrows():
    print(f"{row['sector_name']:<22} {row['early_rate']:>7.1%} {row['late_rate']:>7.1%} {row['change']:>+8.1%}")

# --- Small multiples: startup rate over time ---
fig, axes = plt.subplots(4, 5, figsize=(22, 16), sharey=True)
axes = axes.flatten()

for idx, sector in enumerate(sorted(SECTOR_NAMES.keys())):
    if idx >= len(axes):
        break
    ax = axes[idx]
    sdf = startup_df[startup_df['sector'] == sector]
    ax.plot(sdf['year'], sdf['startup_rate'] * 100, '-', color='#1565C0', linewidth=1.5)
    ax.set_title(SECTOR_NAMES[sector], fontsize=9, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1978, 2023)
    ax.tick_params(labelsize=7)

# Hide unused subplot
if len(SECTOR_NAMES) < len(axes):
    axes[-1].set_visible(False)

fig.suptitle('Startup Rate (New Firms / Total Firms) by NAICS Sector, 1978-2023',
             fontsize=14, fontweight='bold', y=1.01)
fig.text(0.5, -0.01, 'Year', ha='center', fontsize=11)
fig.text(-0.01, 0.5, 'Startup Rate (%)', va='center', rotation=90, fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_startup_rate_all_sectors.png'), dpi=200, bbox_inches='tight')
plt.close()
print("Saved: ent_startup_rate_all_sectors.png")

# =============================================================================
# Summary statistics
# =============================================================================
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)

# Economy-wide young-firm JC share trend
early_jc = econ_df[econ_df['year'] <= 1985]['young_jc_share'].mean()
mid_jc = econ_df[(econ_df['year'] >= 2000) & (econ_df['year'] <= 2007)]['young_jc_share'].mean()
late_jc = econ_df[econ_df['year'] >= 2019]['young_jc_share'].mean()

print(f"\nEconomy-wide young-firm (age 0-5) share of job creation:")
print(f"  1978-85 average: {early_jc:.1%}")
print(f"  2000-07 average: {mid_jc:.1%}")
print(f"  2019-23 average: {late_jc:.1%}")
print(f"  Change (early to late): {late_jc - early_jc:+.1%} ({(late_jc/early_jc - 1)*100:+.1f}%)")

early_emp = econ_df[econ_df['year'] <= 1985]['young_emp_share'].mean()
late_emp = econ_df[econ_df['year'] >= 2019]['young_emp_share'].mean()
print(f"\nEconomy-wide young-firm share of employment:")
print(f"  1978-85 average: {early_emp:.1%}")
print(f"  2019-23 average: {late_emp:.1%}")
print(f"  Change: {late_emp - early_emp:+.1%}")

print("\n" + "=" * 80)
print("PHASE 2 (BDS) COMPLETE")
print("=" * 80)
