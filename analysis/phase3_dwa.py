"""
Phase 3: Detailed Work Activities (DWA) Analysis
=================================================
Higher granularity than GWAs. DWAs are binary (present/absent per occupation).
Track employment-weighted prevalence over time.
"""

import pandas as pd
import numpy as np
import os
import csv
from collections import defaultdict

ROOT = '/Users/burnssa/Code/ai-labor-research'
DATA = os.path.join(ROOT, 'data')
ANALYSIS = os.path.join(DATA, 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# Load master panel for employment data
master = pd.read_csv(os.path.join(ANALYSIS, 'master_panel.csv'))
years = sorted(master['year'].unique())
first_year, last_year = years[0], years[-1]

# Load DWA reference
dwa_titles = {}
with open(os.path.join(DATA, 'onet', 'db_29_1_text', 'DWA Reference.txt'), 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for r in reader:
        dwa_titles[r['DWA ID']] = r['DWA Title']

# Load Tasks-to-DWAs mapping (which occupations have which DWAs)
occ_dwas = defaultdict(set)
with open(os.path.join(DATA, 'onet', 'db_29_1_text', 'Tasks to DWAs.txt'), 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for r in reader:
        soc = r['O*NET-SOC Code'].split('.')[0]  # strip .00 suffix
        occ_dwas[soc].add(r['DWA ID'])

print(f"DWAs: {len(dwa_titles)}")
print(f"Occupations with DWA data: {len(occ_dwas)}")

# =============================================================================
# 3a. DWA Prevalence Over Time
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 3a: DWA EMPLOYMENT-WEIGHTED PREVALENCE OVER TIME")
print("=" * 80)

# For each DWA, compute employment-weighted prevalence:
# = sum of employment for occupations that include this DWA / total employment
dwa_prevalence = {}

for y in years:
    ydf = master[master['year'] == y][['soc_2018_harmonized', 'employment']].dropna()
    total_emp = ydf['employment'].sum()

    prev = {}
    for dwa_id in dwa_titles:
        # Which occupations in this year have this DWA?
        matching_socs = set()
        for soc in ydf['soc_2018_harmonized'].unique():
            if dwa_id in occ_dwas.get(soc, set()):
                matching_socs.add(soc)

        if matching_socs:
            emp = ydf[ydf['soc_2018_harmonized'].isin(matching_socs)]['employment'].sum()
            prev[dwa_id] = emp / total_emp
        else:
            prev[dwa_id] = 0.0

    dwa_prevalence[y] = prev
    print(f"  {y}: computed prevalence for {len(prev)} DWAs")

prev_panel = pd.DataFrame(dwa_prevalence)
prev_panel['dwa_title'] = prev_panel.index.map(dwa_titles)

# Compute change
prev_panel['change'] = prev_panel[last_year] - prev_panel[first_year]
prev_panel['pct_change'] = prev_panel['change'] / prev_panel[first_year].replace(0, np.nan) * 100

# Sort by change
prev_sorted = prev_panel.sort_values('change', ascending=False)

print(f"\n  TOP 30 DWAs by GROWTH in employment-weighted prevalence ({first_year}-{last_year}):")
print(f"  {'DWA':<72} {first_year:>6} {last_year:>6} {'Change':>8}")
print("  " + "-" * 95)
for i, (dwa_id, row) in enumerate(prev_sorted.head(30).iterrows()):
    print(f"  {row['dwa_title'][:70]:<72} {row[first_year]:6.4f} {row[last_year]:6.4f} {row['change']:+8.5f}")

print(f"\n  BOTTOM 30 DWAs by DECLINE in employment-weighted prevalence ({first_year}-{last_year}):")
print(f"  {'DWA':<72} {first_year:>6} {last_year:>6} {'Change':>8}")
print("  " + "-" * 95)
for i, (dwa_id, row) in enumerate(prev_sorted.tail(30).iterrows()):
    print(f"  {row['dwa_title'][:70]:<72} {row[first_year]:6.4f} {row[last_year]:6.4f} {row['change']:+8.5f}")

prev_panel.to_csv(os.path.join(ANALYSIS, 'dwa_prevalence_by_year.csv'))

# =============================================================================
# 3b. DWA Keyword Exploration
# =============================================================================
print("\n" + "=" * 80)
print("PHASE 3b: DWA KEYWORD EXPLORATION")
print("=" * 80)

spec_keywords = ['select', 'choose', 'evaluate', 'judge', 'recommend', 'design',
                 'curate', 'specify', 'determine requirements', 'assess needs',
                 'envision', 'conceptualize', 'prioritize', 'approve',
                 'develop strategy', 'develop plan', 'develop concept']

exec_keywords = ['operate', 'assemble', 'install', 'maintain', 'process',
                 'calculate', 'enter data', 'file ', 'transport', 'clean',
                 'inspect', 'repair', 'load', 'sort', 'monitor equipment',
                 'calibrate', 'measure', 'pour ', 'cut ', 'weld',
                 'package', 'stack', 'drive']

def classify_dwa_keyword(title):
    t = title.lower()
    for kw in spec_keywords:
        if kw in t:
            return 'spec_keyword'
    for kw in exec_keywords:
        if kw in t:
            return 'exec_keyword'
    return 'neither'

dwa_classes = {dwa_id: classify_dwa_keyword(title) for dwa_id, title in dwa_titles.items()}

n_spec = sum(1 for v in dwa_classes.values() if v == 'spec_keyword')
n_exec = sum(1 for v in dwa_classes.values() if v == 'exec_keyword')
print(f"  Spec-keyword DWAs: {n_spec}")
print(f"  Exec-keyword DWAs: {n_exec}")
print(f"  Neither: {len(dwa_classes) - n_spec - n_exec}")

# Compute aggregate prevalence for each keyword group
for group_name, group_label in [('Specification keywords', 'spec_keyword'),
                                 ('Execution keywords', 'exec_keyword')]:
    group_dwas = [d for d, c in dwa_classes.items() if c == group_label]
    print(f"\n  {group_name} ({len(group_dwas)} DWAs):")
    print(f"  {'Year':>6}  {'Aggregate prevalence':>20}")
    for y in years:
        # Aggregate: fraction of employment in occupations that have ANY DWA from this group
        ydf = master[master['year'] == y][['soc_2018_harmonized', 'employment']].dropna()
        total_emp = ydf['employment'].sum()
        matching_emp = 0
        for soc in ydf['soc_2018_harmonized'].unique():
            soc_dwas = occ_dwas.get(soc, set())
            if soc_dwas & set(group_dwas):
                emp = ydf[ydf['soc_2018_harmonized'] == soc]['employment'].sum()
                matching_emp += emp
        prevalence = matching_emp / total_emp if total_emp > 0 else 0
        print(f"  {y:>6}  {prevalence:20.4f}")

    # Also compute mean prevalence across all DWAs in the group
    mean_prev = {}
    for y in years:
        vals = [prev_panel.loc[d, y] for d in group_dwas if d in prev_panel.index]
        mean_prev[y] = np.mean(vals) if vals else 0
    print(f"  Mean per-DWA prevalence:")
    for y in years:
        print(f"    {y}: {mean_prev[y]:.5f}")

print("\n" + "=" * 80)
print("PHASE 3 COMPLETE")
print("=" * 80)
