"""
Entrepreneurial Analysis Phase 3: Intangible Investment Decomposition
======================================================================
Uses INTAN-Invest (CHS framework) and BEA IPP data to track specification-type
vs execution-type intangible investment over time.

CHS Framework mapping:
  EXECUTION: Software & databases (I_NatAcc minus R&D minus artistic originals)
  MIXED: R&D
  SPECIFICATION: Brand (I_Brand), Design (I_Design), Org Capital (I_OrgCap)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# =============================================================================
# Load INTAN-Invest US data
# =============================================================================
print("=" * 80)
print("LOADING INTAN-INVEST US DATA (CHS Framework)")
print("=" * 80)

intan = pd.read_excel(
    os.path.join(DATA, 'intangibles', 'US_AEX_formatted.xlsx'),
    sheet_name='Current prices', engine='openpyxl'
)

print(f"Years: {intan['year'].min()}-{intan['year'].max()}")
print(f"Columns: {list(intan.columns)}")

# The CHS decomposition:
# I_NatAcc = national accounts intangibles (software, R&D, artistic originals)
# I_OrgCap = organizational capital (specification)
# I_Design = design (specification)
# I_Brand = brand equity / market research (specification)
# I_NFP = new financial products (mixed)
# I_NonNatAcc = total non-national-accounts intangibles
# I_Intan = total intangibles

# Create specification vs execution grouping
intan['spec_capital'] = intan['I_OrgCap'] + intan['I_Design'] + intan['I_Brand']
intan['mixed_capital'] = intan['I_NFP']  # new financial products
intan['natacct_capital'] = intan['I_NatAcc']  # software + R&D + artistic (execution-heavy)
intan['total_intan'] = intan['I_Intan']

# Compute shares
intan['spec_share'] = intan['spec_capital'] / intan['total_intan']
intan['natacct_share'] = intan['natacct_capital'] / intan['total_intan']
intan['intan_gdp_share'] = intan['total_intan'] / intan['GDP']
intan['spec_gdp_share'] = intan['spec_capital'] / intan['GDP']
intan['natacct_gdp_share'] = intan['natacct_capital'] / intan['GDP']

# Individual component shares
intan['orgcap_share'] = intan['I_OrgCap'] / intan['total_intan']
intan['design_share'] = intan['I_Design'] / intan['total_intan']
intan['brand_share'] = intan['I_Brand'] / intan['total_intan']

print(f"\nIntangible Investment Decomposition ($ millions, current prices):")
print(f"{'Year':>6} {'Total Intan':>12} {'NatAcct':>10} {'OrgCap':>10} {'Design':>10} {'Brand':>10} {'NFP':>10} {'Spec/Total':>11}")
for _, row in intan.iterrows():
    print(f"{int(row['year']):>6} {row['total_intan']:>12,.0f} {row['natacct_capital']:>10,.0f} "
          f"{row['I_OrgCap']:>10,.0f} {row['I_Design']:>10,.0f} {row['I_Brand']:>10,.0f} "
          f"{row['I_NFP']:>10,.0f} {row['spec_share']:>11.1%}")

intan.to_csv(os.path.join(ANALYSIS, 'intangible_decomposition_us.csv'), index=False)

# =============================================================================
# Load BEA IPP data from FRED
# =============================================================================
print("\n" + "=" * 80)
print("LOADING BEA IPP DATA (from FRED)")
print("=" * 80)

bea_series = {
    'total_ipp': 'Y001RC1A027NBEA',
    'software': 'B985RC1A027NBEA',
    'rd': 'Y006RC1A027NBEA',
    'entertainment': 'Y020RC1A027NBEA',
}

bea_dfs = {}
for name, series_id in bea_series.items():
    fpath = os.path.join(DATA, 'bea', f'{series_id}.csv')
    if os.path.exists(fpath):
        df = pd.read_csv(fpath)
        df.columns = ['date', 'value']
        df['year'] = pd.to_datetime(df['date']).dt.year
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        bea_dfs[name] = df[['year', 'value']].dropna()
        print(f"  {name}: {len(bea_dfs[name])} years ({bea_dfs[name]['year'].min()}-{bea_dfs[name]['year'].max()})")

# Merge into a single BEA panel
bea = bea_dfs['total_ipp'].rename(columns={'value': 'total_ipp'})
for name in ['software', 'rd', 'entertainment']:
    if name in bea_dfs:
        bea = bea.merge(bea_dfs[name].rename(columns={'value': name}), on='year', how='outer')

# Focus on 1960+ (IPP categories start getting meaningful in the 1960s)
bea = bea[bea['year'] >= 1960].copy()

# Compute shares
bea['software_share'] = bea['software'] / bea['total_ipp']
bea['rd_share'] = bea['rd'] / bea['total_ipp']
bea['entertainment_share'] = bea['entertainment'] / bea['total_ipp']

print(f"\nBEA IPP Investment ($ billions, selected years):")
print(f"{'Year':>6} {'Total IPP':>10} {'Software':>10} {'R&D':>10} {'Entertain':>10} {'Soft%':>7} {'R&D%':>7} {'Ent%':>7}")
for _, row in bea[bea['year'].isin([1970, 1980, 1990, 2000, 2010, 2020, 2024])].iterrows():
    print(f"{int(row['year']):>6} {row['total_ipp']:>10.1f} {row.get('software', 0):>10.1f} "
          f"{row.get('rd', 0):>10.1f} {row.get('entertainment', 0):>10.1f} "
          f"{row.get('software_share', 0):>7.1%} {row.get('rd_share', 0):>7.1%} "
          f"{row.get('entertainment_share', 0):>7.1%}")

bea.to_csv(os.path.join(ANALYSIS, 'bea_ipp_investment.csv'), index=False)

# =============================================================================
# Charts
# =============================================================================
print("\n" + "=" * 80)
print("GENERATING CHARTS")
print("=" * 80)

# --- Chart 1: INTAN-Invest CHS decomposition ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

years = intan['year']
ax1.stackplot(years,
    intan['natacct_capital'] / 1e6,
    intan['I_OrgCap'] / 1e6,
    intan['I_Design'] / 1e6,
    intan['I_Brand'] / 1e6,
    intan['I_NFP'] / 1e6,
    labels=['National Accounts (Software, R&D, Artistic)',
            'Organizational Capital', 'Design',
            'Brand/Market Research', 'New Financial Products'],
    colors=['#1565C0', '#C62828', '#FF8F00', '#2E7D32', '#6A1B9A'],
    alpha=0.8)
ax1.set_ylabel('Investment ($ trillions)', fontsize=11)
ax1.set_title('US Intangible Investment by CHS Category (INTAN-Invest, 2010-2024)',
              fontsize=13, fontweight='bold')
ax1.legend(loc='upper left', fontsize=8)
ax1.grid(True, alpha=0.2)

# Shares
ax2.plot(years, intan['spec_share'] * 100, '-o', color='#C62828', linewidth=2,
         markersize=4, label='Specification Capital\n(OrgCap + Design + Brand)')
ax2.plot(years, intan['natacct_share'] * 100, '-s', color='#1565C0', linewidth=2,
         markersize=4, label='National Accounts Capital\n(Software + R&D + Artistic)')
ax2.set_ylabel('Share of Total Intangible Investment (%)', fontsize=11)
ax2.set_xlabel('Year', fontsize=11)
ax2.set_title('Specification vs Execution Capital Share of Total Intangibles',
              fontsize=13, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_intangible_chs_decomposition.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: ent_intangible_chs_decomposition.png")

# --- Chart 2: BEA IPP long-run trends ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Levels
ax1.plot(bea['year'], bea['software'], '-', color='#1565C0', linewidth=2, label='Software')
ax1.plot(bea['year'], bea['rd'], '-', color='#FF8F00', linewidth=2, label='R&D')
ax1.plot(bea['year'], bea['entertainment'], '-', color='#C62828', linewidth=2, label='Entertainment/Artistic Originals')
ax1.set_ylabel('Investment ($ billions)', fontsize=11)
ax1.set_title('BEA: Private Fixed Investment in Intellectual Property Products (1960-2025)',
              fontsize=13, fontweight='bold')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Shares
ax2.plot(bea['year'], bea['software_share'] * 100, '-', color='#1565C0', linewidth=2, label='Software')
ax2.plot(bea['year'], bea['rd_share'] * 100, '-', color='#FF8F00', linewidth=2, label='R&D')
ax2.plot(bea['year'], bea['entertainment_share'] * 100, '-', color='#C62828', linewidth=2,
         label='Entertainment/Artistic Originals')
ax2.set_ylabel('Share of Total IPP Investment (%)', fontsize=11)
ax2.set_xlabel('Year', fontsize=11)
ax2.set_title('Composition of IPP Investment Over Time', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_bea_ipp_trends.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: ent_bea_ipp_trends.png")

# --- Chart 3: Specification capital components (INTAN-Invest detail) ---
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, intan['I_OrgCap'] / 1e6, '-o', color='#C62828', linewidth=2, markersize=4,
        label='Organizational Capital')
ax.plot(years, intan['I_Brand'] / 1e6, '-s', color='#2E7D32', linewidth=2, markersize=4,
        label='Brand / Market Research')
ax.plot(years, intan['I_Design'] / 1e6, '-^', color='#FF8F00', linewidth=2, markersize=4,
        label='Design')
ax.plot(years, intan['I_NFP'] / 1e6, '-d', color='#6A1B9A', linewidth=2, markersize=4,
        label='New Financial Products')

ax.set_ylabel('Investment ($ trillions)', fontsize=11)
ax.set_xlabel('Year', fontsize=11)
ax.set_title('Specification Capital Components (INTAN-Invest US, 2010-2024)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'ent_spec_capital_components.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: ent_spec_capital_components.png")

# =============================================================================
# Summary
# =============================================================================
print("\n" + "=" * 80)
print("KEY FINDINGS")
print("=" * 80)

first = intan[intan['year'] == intan['year'].min()].iloc[0]
last = intan[intan['year'] == intan['year'].max()].iloc[0]

print(f"\nINTAN-Invest US ({int(first['year'])}-{int(last['year'])}):")
print(f"  Total intangible investment: ${first['total_intan']/1e6:.2f}T -> ${last['total_intan']/1e6:.2f}T "
      f"({(last['total_intan']/first['total_intan']-1)*100:+.0f}%)")
print(f"  Specification capital (OrgCap+Design+Brand):")
print(f"    Level: ${first['spec_capital']/1e6:.2f}T -> ${last['spec_capital']/1e6:.2f}T "
      f"({(last['spec_capital']/first['spec_capital']-1)*100:+.0f}%)")
print(f"    Share of total intangibles: {first['spec_share']:.1%} -> {last['spec_share']:.1%} "
      f"({(last['spec_share']-first['spec_share'])*100:+.1f}pp)")
print(f"  National accounts capital (Software+R&D+Artistic):")
print(f"    Level: ${first['natacct_capital']/1e6:.2f}T -> ${last['natacct_capital']/1e6:.2f}T "
      f"({(last['natacct_capital']/first['natacct_capital']-1)*100:+.0f}%)")
print(f"    Share of total intangibles: {first['natacct_share']:.1%} -> {last['natacct_share']:.1%}")

print(f"\n  Component growth ({int(first['year'])}-{int(last['year'])}):")
for name, col in [('Org Capital', 'I_OrgCap'), ('Design', 'I_Design'),
                   ('Brand', 'I_Brand'), ('New Fin Products', 'I_NFP')]:
    growth = (last[col] / first[col] - 1) * 100
    print(f"    {name}: {growth:+.0f}%")

bea_first = bea[bea['year'] == 1990].iloc[0] if 1990 in bea['year'].values else None
bea_last = bea[bea['year'] == bea['year'].max()].iloc[0]
if bea_first is not None:
    print(f"\nBEA IPP (1990-{int(bea_last['year'])}):")
    print(f"  Software share of IPP: {bea_first['software_share']:.1%} -> {bea_last['software_share']:.1%}")
    print(f"  R&D share of IPP: {bea_first['rd_share']:.1%} -> {bea_last['rd_share']:.1%}")
    print(f"  Entertainment share of IPP: {bea_first['entertainment_share']:.1%} -> {bea_last['entertainment_share']:.1%}")

print("\n" + "=" * 80)
print("PHASE 3 (INTANGIBLES) COMPLETE")
print("=" * 80)
