"""
Phase 4: PCA Analysis of GWA Dimensions
=========================================
Reduces the 41 GWAs to principal components, then projects the
growing-vs-shrinking difference vectors into PC space.

Produces:
  - PCA loading biplot (pca_gwa_dimensions.png)
  - Projected difference vectors (pca_diff_vectors_projected.png)
  - GWA growth differentials mapped onto PC space by wage band
    (pca_gwa_growth_diff_by_band.png)
  - PCA dimension legend chart (pca_dimension_legend.png)
  - CSV of loadings (gwa_pca_loadings.csv)
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

ROOT = '/Users/burnssa/Code/ai-labor-research'
ANALYSIS = os.path.join(ROOT, 'data', 'analysis')
FIGURES = os.path.join(ROOT, 'output', 'figures')

# Load GWA matrix and fit PCA
gwa_matrix = pd.read_csv(os.path.join(ANALYSIS, 'onet_gwa_importance_matrix.csv'), index_col=0)
gwa_cols = list(gwa_matrix.columns)

scaler = StandardScaler()
X = scaler.fit_transform(gwa_matrix.dropna())
pca = PCA()
pca.fit(X)

loadings = pd.DataFrame(pca.components_[:4].T, index=gwa_cols, columns=['PC1','PC2','PC3','PC4'])
loadings.to_csv(os.path.join(ANALYSIS, 'gwa_pca_loadings.csv'))

print(f"Variance explained: PC1={pca.explained_variance_ratio_[0]*100:.1f}%, "
      f"PC2={pca.explained_variance_ratio_[1]*100:.1f}%, "
      f"PC3={pca.explained_variance_ratio_[2]*100:.1f}%")

# Short name helper
def shorten(gwa):
    replacements = [
        ('Communicating with Supervisors, Peers, or Subordinates', 'Comm w/ Peers'),
        ('Communicating with People Outside the Organization', 'Comm w/ External'),
        ('Establishing and Maintaining Interpersonal Relationships', 'Interpersonal Rels'),
        ('Evaluating Information to Determine Compliance with Standards', 'Eval Compliance'),
        ('Estimating the Quantifiable Characteristics of Products, Events, or Information', 'Estimating Quantities'),
        ('Drafting, Laying Out, and Specifying Technical Devices, Parts, and Equipment', 'Drafting/Technical'),
        ('Organizing, Planning, and Prioritizing Work', 'Organizing/Planning'),
        ('Performing General Physical Activities', 'Physical Activities'),
        ('Repairing and Maintaining Mechanical Equipment', 'Repair Mechanical'),
        ('Repairing and Maintaining Electronic Equipment', 'Repair Electronic'),
        ('Operating Vehicles, Mechanized Devices, or Equipment', 'Operating Vehicles'),
        ('Guiding, Directing, and Motivating Subordinates', 'Guiding Subordinates'),
        ('Monitoring Processes, Materials, or Surroundings', 'Monitoring Processes'),
        ('Resolving Conflicts and Negotiating with Others', 'Negotiating'),
        ('Judging the Qualities of Objects, Services, or People', 'Judging Qualities'),
        ('Identifying Objects, Actions, and Events', 'Identifying Objects'),
        ('Inspecting Equipment, Structures, or Materials', 'Inspecting Equipment'),
        ('Updating and Using Relevant Knowledge', 'Using Knowledge'),
        ('Making Decisions and Solving Problems', 'Decision Making'),
        ('Performing for or Working Directly with the Public', 'Working w/ Public'),
        ('Interpreting the Meaning of Information for Others', 'Interpreting Info'),
        ('Providing Consultation and Advice to Others', 'Consulting/Advising'),
        ('Coordinating the Work and Activities of Others', 'Coordinating Others'),
        ('Performing Administrative Activities', 'Admin Activities'),
        ('Scheduling Work and Activities', 'Scheduling'),
        ('Developing Objectives and Strategies', 'Dev Strategy'),
        ('Coaching and Developing Others', 'Coaching Others'),
        ('Developing and Building Teams', 'Building Teams'),
        ('Assisting and Caring for Others', 'Assisting/Caring'),
        ('Training and Teaching Others', 'Training/Teaching'),
        ('Selling or Influencing Others', 'Selling/Influencing'),
        ('Staffing Organizational Units', 'Staffing'),
        ('Monitoring and Controlling Resources', 'Controlling Resources'),
        ('Analyzing Data or Information', 'Analyzing Data'),
        ('Documenting/Recording Information', 'Documenting'),
        ('Handling and Moving Objects', 'Handling Objects'),
        ('Controlling Machines and Processes', 'Controlling Machines'),
        ('Processing Information', 'Processing Info'),
        ('Working with Computers', 'Working w/ Computers'),
        ('Getting Information', 'Getting Info'),
    ]
    for old, new in replacements:
        gwa = gwa.replace(old, new)
    return gwa

def project_diff(diff_series):
    vec = diff_series.reindex(gwa_cols).fillna(0).values
    vec_std = vec / scaler.scale_
    return pca.transform(vec_std.reshape(1, -1))[0]

# Load difference data
nrc_overall = pd.read_csv(os.path.join(ANALYSIS, 'gwa_within_nrc_growing_vs_shrinking.csv'), index_col=0)
ew_changes = pd.read_csv(os.path.join(ANALYSIS, 'gwa_emp_weighted_changes.csv'), index_col=0)
band_data = {}
for fname, label in [
    ('gwa_within_nrc_lowerpay_nrc.csv', 'Lower-pay NRC ($18K-$40K)'),
    ('gwa_within_nrc_midpay_nrc.csv', 'Mid-pay NRC ($40K-$57K)'),
    ('gwa_within_nrc_upperpay_nrc.csv', 'Upper-pay NRC ($57K-$142K)'),
]:
    band_data[label] = pd.read_csv(os.path.join(ANALYSIS, fname), index_col=0)

# ============================================================
# Chart 1: PCA loading biplot
# ============================================================
fig, ax = plt.subplots(figsize=(14, 12))

for gwa in gwa_cols:
    x, y = loadings.loc[gwa, 'PC1'], loadings.loc[gwa, 'PC2']
    color = '#1565C0' if y > 0.15 else ('#C62828' if y < -0.05 else '#666')
    ax.scatter(x, y, s=40, color=color, alpha=0.8, zorder=3)
    ax.annotate(shorten(gwa), (x, y), fontsize=6.5, textcoords='offset points',
                xytext=(4, 3), alpha=0.85)

ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax.axvline(x=0, color='gray', linewidth=0.5, linestyle='--')
ax.set_xlabel(f'PC1: General Cognitive Complexity ({pca.explained_variance_ratio_[0]*100:.0f}% variance)', fontsize=12)
ax.set_ylabel(f'PC2: Physical/Mechanical vs Interpersonal/Digital ({pca.explained_variance_ratio_[1]*100:.0f}% variance)', fontsize=12)
ax.set_title('Fundamental Dimensions of Work Activities\n(PCA of 41 GWAs across 763 occupations)',
             fontsize=14, fontweight='bold')
ax.text(0.22, 0.35, 'High complexity +\nPhysical/Mechanical', fontsize=9, color='#1565C0', fontstyle='italic', alpha=0.6)
ax.text(0.22, -0.12, 'High complexity +\nInterpersonal/Digital', fontsize=9, color='#C62828', fontstyle='italic', alpha=0.6)
ax.text(-0.12, 0.30, 'Low complexity +\nPhysical/Mechanical', fontsize=9, color='#1565C0', fontstyle='italic', alpha=0.6)
ax.grid(True, alpha=0.15)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'pca_gwa_dimensions.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: pca_gwa_dimensions.png")

# ============================================================
# Chart 2: Projected difference vectors
# ============================================================
fig, ax = plt.subplots(figsize=(12, 10))

v = project_diff(nrc_overall['difference'])
ax.scatter(v[0], v[1], s=200, c='#C62828', marker='D', zorder=5, edgecolors='white', linewidth=1.5)
ax.annotate('All NRC occupations\n(growing vs shrinking)', (v[0], v[1]),
            fontsize=10, fontweight='bold', textcoords='offset points', xytext=(10, 10), color='#C62828')

band_colors = {
    'Lower-pay NRC ($18K-$40K)': '#FF8F00',
    'Mid-pay NRC ($40K-$57K)': '#6A1B9A',
    'Upper-pay NRC ($57K-$142K)': '#00695C',
}
for band_label, bdf in band_data.items():
    v = project_diff(bdf['difference'])
    ax.scatter(v[0], v[1], s=150, c=band_colors[band_label], marker='o', zorder=5,
              edgecolors='white', linewidth=1.5)
    ax.annotate(band_label.replace('NRC ', 'NRC\n'), (v[0], v[1]),
                fontsize=9, textcoords='offset points', xytext=(10, -15), color=band_colors[band_label])

v = project_diff(ew_changes['total_change'])
ax.scatter(v[0], v[1], s=150, c='#37474F', marker='s', zorder=5, edgecolors='white', linewidth=1.5)
ax.annotate('Economy-wide\nemp shift (2005\u21922024)', (v[0], v[1]),
            fontsize=9, textcoords='offset points', xytext=(10, 5), color='#37474F')

ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax.axvline(x=0, color='gray', linewidth=0.5, linestyle='--')
ax.set_xlabel(f'PC1: General Cognitive Complexity ({pca.explained_variance_ratio_[0]*100:.0f}% variance)', fontsize=12)
ax.set_ylabel(f'PC2: Physical/Mechanical vs Interpersonal/Digital ({pca.explained_variance_ratio_[1]*100:.0f}% variance)', fontsize=12)
ax.set_title('Where Do Growing-vs-Shrinking Differences Fall\nin the Fundamental Dimensions of Work?',
             fontsize=14, fontweight='bold')
textstr = (
    'Each point represents a difference vector:\n'
    'the GWA profile that distinguishes growing\n'
    'from shrinking occupations, projected onto\n'
    'the two main dimensions of work variation.\n\n'
    'All vectors point toward higher PC1\n'
    '(more cognitive complexity) \u2014 the economy\n'
    'is shifting toward more complex work.\n\n'
    'Within NRC, the vectors also point toward\n'
    'higher PC2 \u2014 growing cognitive jobs\n'
    'emphasize physical presence and\n'
    'interpersonal direction, not just\n'
    'digital information processing.'
)
props = dict(boxstyle='round,pad=0.8', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=8,
        verticalalignment='top', horizontalalignment='left', bbox=props)
ax.grid(True, alpha=0.15)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'pca_diff_vectors_projected.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: pca_diff_vectors_projected.png")

# ============================================================
# Chart 3: GWA growth differentials in PC space, 4 panels
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(18, 16))
axes = axes.flatten()

datasets = [
    ('All NRC Occupations', nrc_overall),
    ('Lower-pay NRC ($18K-$40K)', band_data['Lower-pay NRC ($18K-$40K)']),
    ('Mid-pay NRC ($40K-$57K)', band_data['Mid-pay NRC ($40K-$57K)']),
    ('Upper-pay NRC ($57K-$142K)', band_data['Upper-pay NRC ($57K-$142K)']),
]

for idx, (title, diff_df) in enumerate(datasets):
    ax = axes[idx]
    for gwa in gwa_cols:
        pc1 = loadings.loc[gwa, 'PC1']
        pc2 = loadings.loc[gwa, 'PC2']
        diff = diff_df.loc[gwa, 'difference'] if gwa in diff_df.index else 0
        size = abs(diff) * 400 + 15
        if diff > 0.1:
            color, alpha = '#C62828', 0.8
        elif diff < -0.1:
            color, alpha = '#1565C0', 0.8
        elif diff > 0:
            color, alpha = '#EF9A9A', 0.6
        elif diff < 0:
            color, alpha = '#90CAF9', 0.6
        else:
            color, alpha = '#999', 0.4
        ax.scatter(pc1, pc2, s=size, c=color, alpha=alpha, edgecolors='white', linewidth=0.5, zorder=3)
        if abs(diff) > 0.15 or (idx == 0 and abs(diff) > 0.1):
            ax.annotate(f'{shorten(gwa)}\n({diff:+.2f})', (pc1, pc2),
                       fontsize=5.5, textcoords='offset points', xytext=(4, 4),
                       alpha=0.85, color='#333')
    ax.axhline(y=0, color='gray', linewidth=0.3, linestyle='--')
    ax.axvline(x=0, color='gray', linewidth=0.3, linestyle='--')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('PC1: Cognitive Complexity', fontsize=9)
    ax.set_ylabel('PC2: Physical/Mechanical \u2191  vs  Interpersonal/Digital \u2193', fontsize=9)
    ax.grid(True, alpha=0.1)

legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#C62828', markersize=12,
           label='Strong growth differential (>+0.1)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#EF9A9A', markersize=8,
           label='Weak growth differential (0 to +0.1)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#90CAF9', markersize=8,
           label='Weak shrink differential (0 to -0.1)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#1565C0', markersize=12,
           label='Strong shrink differential (<-0.1)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#999', markersize=6,
           label='Dot size = |difference|'),
]
axes[0].legend(handles=legend_elements, loc='lower left', fontsize=7, framealpha=0.9)
fig.suptitle('GWA Growth Differentials (Q5\u2212Q1) Mapped onto Fundamental Work Dimensions\n'
             'Each dot is one GWA; position = PCA loading; color/size = how much more important it is\n'
             'in GROWING (red) vs SHRINKING (blue) NRC occupations',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'pca_gwa_growth_diff_by_band.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: pca_gwa_growth_diff_by_band.png")

# ============================================================
# Chart 4: PCA dimension legend
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 12))

# PC1
pc1_sorted = loadings['PC1'].sort_values(ascending=True)
top20 = pc1_sorted.tail(20)
colors_pc1 = ['#C62828' if v >= top20.min() else '#1565C0' if v <= pc1_sorted.head(20).max() else '#999'
              for v in pc1_sorted]
ax1.barh(range(len(pc1_sorted)), pc1_sorted.values, color=colors_pc1, alpha=0.85, height=0.7)
ax1.set_yticks(range(len(pc1_sorted)))
ax1.set_yticklabels(pc1_sorted.index, fontsize=8)
for i, (gwa, val) in enumerate(pc1_sorted.items()):
    ax1.text(val + 0.003 if val >= 0 else val - 0.003, i, f'{val:+.3f}',
             fontsize=7, va='center', ha='left' if val >= 0 else 'right', color='#444')
ax1.axvline(x=0, color='black', linewidth=0.8)
ax1.set_xlabel('PC1 Loading', fontsize=11)
ax1.set_title('PC1: General Cognitive Complexity\n(37% of variance)', fontsize=13, fontweight='bold')
ax1.grid(True, axis='x', alpha=0.2)
ax1.text(0.97, 0.02, 'Higher loading = activity is more\npresent in cognitively complex jobs\n\n'
         'Lower loading = activity is more\npresent in simpler jobs',
         transform=ax1.transAxes, fontsize=8, va='bottom', ha='right',
         bbox=dict(boxstyle='round,pad=0.6', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9))

# PC2
pc2_sorted = loadings['PC2'].sort_values(ascending=True)
top20_pc2 = pc2_sorted.tail(20)
colors_pc2 = ['#1565C0' if v >= top20_pc2.min() else '#C62828' if v <= pc2_sorted.head(20).max() else '#999'
              for v in pc2_sorted]
ax2.barh(range(len(pc2_sorted)), pc2_sorted.values, color=colors_pc2, alpha=0.85, height=0.7)
ax2.set_yticks(range(len(pc2_sorted)))
ax2.set_yticklabels(pc2_sorted.index, fontsize=8)
for i, (gwa, val) in enumerate(pc2_sorted.items()):
    ax2.text(val + 0.005 if val >= 0 else val - 0.005, i, f'{val:+.3f}',
             fontsize=7, va='center', ha='left' if val >= 0 else 'right', color='#444')
ax2.axvline(x=0, color='black', linewidth=0.8)
ax2.set_xlabel('PC2 Loading', fontsize=11)
ax2.set_title('PC2: Physical/Mechanical vs. Interpersonal/Digital\n(18% of variance)', fontsize=13, fontweight='bold')
ax2.grid(True, axis='x', alpha=0.2)
ax2.text(0.97, 0.02, 'Higher loading (blue) = activity is\nmore present in physical/mechanical jobs\n\n'
         'Lower loading (red) = activity is more\npresent in interpersonal/digital jobs',
         transform=ax2.transAxes, fontsize=8, va='bottom', ha='right',
         bbox=dict(boxstyle='round,pad=0.6', facecolor='#F5F5F5', edgecolor='#BBB', alpha=0.9))

fig.suptitle('PCA Dimension Legend: What Do the Axes Mean?\n'
             'Loadings of all 41 Generalized Work Activities on the two principal components',
             fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES, 'pca_dimension_legend.png'), dpi=250, bbox_inches='tight')
plt.close()
print("Saved: pca_dimension_legend.png")

print("\nAll PCA charts saved.")
