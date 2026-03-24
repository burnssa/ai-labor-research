"""
Generate publication exhibits for the specification labor article.

Exhibit 1: exhibit_employment_shift.png
  Employment in management-task-intensive vs execution-task-intensive
  occupations (top/bottom tercile on management task gradient), 2005-2024.
  NOTE: This uses the raw management gradient, which correlates heavily
  with cognitive complexity (PC1). It shows the shift toward management-
  like tasks, not specification-specifically.

Exhibit 2: exhibit_employment_shift_decomposed.png
  Decomposes the management-gradient top tercile (exhibit 1's red line)
  into two stacked components:
  - Employment in occupations that are BOTH management-task-intensive AND
    specification-intensive (top tercile on spec_residual) — the
    specification-specific component
  - Employment in occupations that are management-task-intensive but NOT
    specification-intensive — the complexity-driven component
  Plus the execution-intensive bottom tercile for reference.
  This makes the complexity confound visually explicit in actual job counts.

Inputs (all pre-computed by spec_exec_management_contrast.py and
elasticity_estimation.py):
  - data/analysis/mgmt_spec_employment_shares.csv
  - data/analysis/spec_ai_panel.csv
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
os.makedirs(FIGURES, exist_ok=True)

# ── Load data ────────────────────────────────────────────────────────────
shares = pd.read_csv(os.path.join(ANALYSIS, 'mgmt_spec_employment_shares.csv'))
panel = pd.read_csv(os.path.join(ANALYSIS, 'spec_ai_panel.csv'))

years = sorted(shares['year'].astype(int).tolist())
first_year, last_year = years[0], years[-1]

# =============================================================================
# Exhibit 1: Management-Task-Intensive vs Execution-Task-Intensive Employment
# =============================================================================
fig, ax = plt.subplots(figsize=(10, 6.5))

top = shares['top_emp'] / 1e6
bot = shares['bottom_emp'] / 1e6
yr = shares['year']

ax.plot(yr, top, '-o', color='#C62828', linewidth=2.5, markersize=8,
        label='Management-task-intensive occupations\n(top tercile on management task gradient)')
ax.plot(yr, bot, '-s', color='#1565C0', linewidth=2.5, markersize=8,
        label='Execution-task-intensive occupations\n(bottom tercile on management task gradient)')

# Shaded area between the lines
ax.fill_between(yr, bot, top, alpha=0.10, color='#C62828',
                where=(top >= bot))

# Annotate net change
top_delta = top.iloc[-1] - top.iloc[0]
bot_delta = bot.iloc[-1] - bot.iloc[0]
ax.annotate(f'+{top_delta:.0f}M', xy=(yr.iloc[-1], top.iloc[-1]),
            xytext=(8, 0), textcoords='offset points',
            fontsize=11, fontweight='bold', color='#C62828', va='center')
ax.annotate(f'+{bot_delta:.0f}M', xy=(yr.iloc[-1], bot.iloc[-1]),
            xytext=(8, 0), textcoords='offset points',
            fontsize=11, fontweight='bold', color='#1565C0', va='center')

ax.set_xticks(yr.values)
ax.set_xticklabels([str(int(y)) for y in yr.values])
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Employment (millions of workers)', fontsize=11)
ax.set_title('The Management-Task Shift: Employment in Management-Task-Intensive\n'
             'vs Execution-Task-Intensive Occupations (U.S. economy, 2005\u20132024)',
             fontsize=13, fontweight='bold', pad=12)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.25)
ax.set_ylim(bottom=28)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'exhibit_employment_shift.png'),
            dpi=250, bbox_inches='tight')
plt.close()
print(f"Saved: exhibit_employment_shift.png")

# =============================================================================
# Exhibit 2: Decomposed Employment — Splitting the Management-Task Top Tercile
# =============================================================================
# Take the management-gradient top tercile from exhibit 1 and decompose it:
# which of those occupations are also specification-intensive (top tercile on
# spec_residual) vs merely complexity-driven?

resid_cuts = panel['spec_residual'].dropna().quantile([1/3, 2/3]).values
mgmt_cuts = panel['spec_score'].dropna().quantile([1/3, 2/3]).values

decomp_rows = []
for year in years:
    emp_col = f'emp_{year}'
    valid = panel.dropna(subset=[emp_col, 'spec_score', 'spec_residual'])

    # Management-gradient top tercile (same group as exhibit 1 red line)
    mgmt_top_mask = valid['spec_score'] > mgmt_cuts[1]
    mgmt_top_total = valid.loc[mgmt_top_mask, emp_col].sum()

    # Of those, which are ALSO specification-intensive (top tercile on residual)?
    spec_and_mgmt = mgmt_top_mask & (valid['spec_residual'] > resid_cuts[1])
    spec_component = valid.loc[spec_and_mgmt, emp_col].sum()

    # The rest are management-task-intensive due to complexity, not specification
    complexity_component = mgmt_top_total - spec_component

    # Execution-intensive bottom tercile (same as exhibit 1 blue line)
    mgmt_bot = valid.loc[valid['spec_score'] < mgmt_cuts[0], emp_col].sum()

    decomp_rows.append({
        'year': year,
        'mgmt_top_total': mgmt_top_total,
        'spec_component': spec_component,
        'complexity_component': complexity_component,
        'exec_bottom': mgmt_bot,
    })

decomp = pd.DataFrame(decomp_rows)
decomp.to_csv(os.path.join(ANALYSIS, 'exhibit_employment_decomposed.csv'), index=False)

fig, ax = plt.subplots(figsize=(10, 6.5))

yr = decomp['year']
spec = decomp['spec_component'] / 1e6
cpx = decomp['complexity_component'] / 1e6
bot = decomp['exec_bottom'] / 1e6

# Stacked area for the management-task top tercile
ax.fill_between(yr, 0, spec, alpha=0.35, color='#2E7D32', step=None)
ax.fill_between(yr, spec, spec + cpx, alpha=0.25, color='#C62828', step=None)

# Lines on top of the stacked areas
ax.plot(yr, spec, '-^', color='#2E7D32', linewidth=2.5, markersize=8,
        label='Specification-specific component\n'
              '(mgmt-task top tercile AND spec-residual top tercile)')
ax.plot(yr, spec + cpx, '-o', color='#C62828', linewidth=2.5, markersize=8,
        label='Total management-task-intensive\n'
              '(top tercile on management gradient)')
ax.plot(yr, bot, '-s', color='#1565C0', linewidth=2.5, markersize=8,
        label='Execution-task-intensive\n'
              '(bottom tercile on management gradient)')

# Annotate final values
total_final = (spec.iloc[-1] + cpx.iloc[-1])
total_delta = total_final - (spec.iloc[0] + cpx.iloc[0])
spec_final = spec.iloc[-1]
spec_delta = spec.iloc[-1] - spec.iloc[0]
cpx_final = cpx.iloc[-1]
cpx_delta = cpx.iloc[-1] - cpx.iloc[0]
bot_final = bot.iloc[-1]
bot_delta = bot.iloc[-1] - bot.iloc[0]

ax.annotate(f'{total_final:.0f}M total (+{total_delta:.0f}M)',
            xy=(last_year, total_final), xytext=(8, 6),
            textcoords='offset points', fontsize=9, fontweight='bold',
            color='#C62828', va='bottom')

# Label the two stacked bands
mid_spec = spec_final / 2
mid_cpx = spec_final + cpx_final / 2
ax.annotate(f'{spec_final:.0f}M spec-specific\n(+{spec_delta:.0f}M)',
            xy=(last_year, mid_spec), xytext=(-90, 0),
            textcoords='offset points', fontsize=8.5, fontweight='bold',
            color='#2E7D32', va='center',
            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=1.2))
ax.annotate(f'{cpx_final:.0f}M complexity-driven\n(+{cpx_delta:.0f}M)',
            xy=(last_year, mid_cpx), xytext=(-100, 0),
            textcoords='offset points', fontsize=8.5, fontweight='bold',
            color='#9E3030', va='center',
            arrowprops=dict(arrowstyle='->', color='#9E3030', lw=1.2))

ax.annotate(f'{bot_final:.0f}M (+{bot_delta:.0f}M)',
            xy=(last_year, bot_final), xytext=(8, 0),
            textcoords='offset points', fontsize=9, fontweight='bold',
            color='#1565C0', va='center')

ax.set_xticks(yr)
ax.set_xticklabels([str(int(y)) for y in yr])
ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Employment (millions of workers)', fontsize=11)
ax.set_title('Decomposing the Management-Task Shift:\n'
             'How Much Is Specification-Specific vs Complexity-Driven?\n'
             '(U.S. economy, 2005\u20132024)',
             fontsize=13, fontweight='bold', pad=12)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.25)

# Explanatory note
note = (
    'The red line (exhibit 1) is decomposed into two components:\n'
    'Green = occupations that are management-task-intensive AND\n'
    '  score high on specification residual (after removing PC1).\n'
    'Red band = remaining management-task-intensive occupations\n'
    '  whose high score is driven by cognitive complexity.\n\n'
    'Management gradient R\u00b2 = 0.91 with PC1 (complexity).'
)
props = dict(boxstyle='round,pad=0.6', facecolor='#F5F5F5',
             edgecolor='#BBB', alpha=0.9)
ax.text(0.98, 0.03, note, transform=ax.transAxes, fontsize=7,
        va='bottom', ha='right', bbox=props)

plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'exhibit_employment_shift_decomposed.png'),
            dpi=250, bbox_inches='tight')
plt.close()
print(f"Saved: exhibit_employment_shift_decomposed.png")

# Print summary table
print(f"\n{'Year':>6} {'Mgmt Top(M)':>12} {'Spec Comp(M)':>13} {'Cpx Comp(M)':>12} {'Exec Bot(M)':>12}")
print("-" * 58)
for _, row in decomp.iterrows():
    print(f"{int(row['year']):>6} {row['mgmt_top_total']/1e6:>12.1f} "
          f"{row['spec_component']/1e6:>13.1f} "
          f"{row['complexity_component']/1e6:>12.1f} "
          f"{row['exec_bottom']/1e6:>12.1f}")
