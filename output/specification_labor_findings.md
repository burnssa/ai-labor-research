# Specification Labor: Empirical Findings

## Summary

This document presents empirical evidence on whether the U.S. economy is shifting employment toward "specification" tasks — activities related to deciding *what* to produce, allocating resources, directing work, and shaping output — as distinct from "execution" tasks that involve implementing known procedures, processing information, and physically producing goods.

**Core finding:** The U.S. economy added 20 million jobs in management-task-intensive occupations between 2005 and 2024, versus only 5 million in execution-task-intensive occupations. Decomposing the management task gradient into cognitive complexity (PC1, R² = 0.905) and a specification-specific residual, approximately 12 million of the 20 million gain are in occupations that score high on specification-specific tasks (staffing, resource allocation, directing, selling) beyond what complexity alone predicts. This signal is distinct from the well-documented shift toward non-routine cognitive work.

---

## 1. Methodology

### Defining the specification-execution axis

We define the specification-execution gradient empirically by contrasting **management occupations** (SOC 11-XXXX: C-suite executives, directors, and managers across all fields, n=33) against **non-management occupations** (all other SOC codes, n=730) on 41 Generalized Work Activities from O\*NET v29.1.

**Rationale:** Management occupations are, by construction, the roles that decide what an organization produces, how resources are allocated, and who does what. Their distinctive task profile — the tasks they emphasize more than non-managers — reveals what specification labor looks like empirically.

**Critical control:** The management task profile correlates with general cognitive complexity (PC1 from PCA of 41 GWAs, R² = 0.905 at the occupation level). To isolate the specification-specific component, we residualize: we remove the part of the management contrast that is explained by complexity, and separately remove complexity from the employment growth signal. The residual correlation tests whether specification-specific tasks predict growth *beyond* what complexity alone predicts.

### Data sources

- **O\*NET v29.1** — Static task profile snapshot (41 GWAs with importance scores for ~763 occupations)
- **BLS OEWS** — National employment and wage data by occupation for 2005, 2009, 2014, 2019, 2024
- **Felten et al. (2021) AIOE** — AI occupational exposure scores
- **CPS ASEC 2024** — Individual-level data linking workers to employer size and occupation
- **Census BDS 1978-2023** — Firm dynamics by sector and firm age
- **INTAN-Invest / BEA** — Intangible investment decomposition

All temporal variation comes from employment shifting across occupations with fixed O\*NET task profiles. This is the cleanest approach — it measures "the economy is moving labor toward occupations that emphasize activity X."

---

## 2. The Specification-Specific Tasks

The tasks that define management *beyond what cognitive complexity predicts* (Exhibit 3, `exhibit_spec_specific_tasks.png`):

**Specification-specific (management emphasis > complexity prediction):**

| Task | Residual | Interpretation |
|------|----------|---------------|
| Staffing Organizational Units | +0.65 | Choosing who does what |
| Monitoring and Controlling Resources | +0.56 | Deciding where to allocate |
| Guiding, Directing, and Motivating Subordinates | +0.48 | Directing what gets done |
| Selling or Influencing Others | +0.46 | Persuading about what to produce/buy |
| Coordinating the Work and Activities of Others | +0.34 | Orchestrating execution |
| Resolving Conflicts and Negotiating with Others | +0.32 | Adjudicating competing specifications |
| Developing and Building Teams | +0.28 | Assembling human capital for a purpose |
| Coaching and Developing Others | +0.20 | Shaping others' capabilities toward goals |

**Complexity-specific but NOT specification (cognitive work that supports execution):**

| Task | Residual | Interpretation |
|------|----------|---------------|
| Updating and Using Relevant Knowledge | -0.48 | Keeping current (supports any work) |
| Documenting/Recording Information | -0.42 | Recording what happened |
| Getting Information | -0.39 | Gathering data inputs |
| Interpreting the Meaning of Information for Others | -0.38 | Translating data for others |
| Processing Information | -0.34 | Handling information flows |
| Making Decisions and Solving Problems | -0.27 | Problem-solving within given objectives |
| Organizing, Planning, and Prioritizing Work | -0.17 | Sequencing execution |
| Analyzing Data or Information | -0.15 | Data analysis (procedure-following) |

**Key insight:** The specification-specific tasks are about **directing, allocating, staffing, selling, negotiating** — deciding what gets done and by whom. The complexity-specific tasks are about **information processing, documenting, interpreting, staying current** — cognitive work that supports execution of given objectives. This is not the same as the routine/non-routine distinction; both columns are non-routine cognitive work.

### Disentangling the management gradient: three components

The raw management task gradient (what differentiates managers from non-managers) is a composite of two signals: general cognitive complexity and specification-specific tasks. The table below shows the top 5 GWAs ranked by each component, making the distinction concrete.

| Rank | Management Gradient (raw) | Cognitive Complexity (PC1) | Specification Residual (mgmt after removing PC1) |
|------|---------------------------|---------------------------|--------------------------------------------------|
| 1 | Staffing Organizational Units (+1.205) | Providing Consultation and Advice (+0.214) | Staffing Organizational Units (+0.653) |
| 2 | Guiding, Directing, and Motivating Subordinates (+1.069) | Developing Objectives and Strategies (+0.211) | Monitoring and Controlling Resources (+0.560) |
| 3 | Monitoring and Controlling Resources (+0.957) | Interpreting the Meaning of Information for Others (+0.208) | Guiding, Directing, and Motivating Subordinates (+0.477) |
| 4 | Developing and Building Teams (+0.912) | Organizing, Planning, and Prioritizing Work (+0.206) | Selling or Influencing Others (+0.460) |
| 5 | Coordinating the Work and Activities of Others (+0.904) | Updating and Using Relevant Knowledge (+0.205) | Coordinating the Work and Activities of Others (+0.342) |

**Reading the table:** The left column captures *everything* that makes managers distinctive — but R² = 0.905 of this is explained by cognitive complexity (middle column). The PC1 column is generic high-skill cognitive work: consulting, strategizing, interpreting, organizing, learning. These activities characterize any demanding knowledge-work occupation, not specification-specifically.

The right column isolates what managers do *beyond* being cognitively skilled: staffing, resource allocation, directing subordinates, selling, and coordinating. These are the activities that survive residualization — the specification-specific component. Note that "Developing and Building Teams" (rank 4 on the raw gradient) drops out of the residual top 5, replaced by "Selling or Influencing Others" — team-building loads heavily on complexity, while selling is specification-specific.

When exhibit 1 (`exhibit_employment_shift.png`) shows +20M jobs in management-task-intensive occupations, it captures all three columns. Exhibit 2 (`exhibit_employment_shift_decomposed.png`) decomposes this: of the +20M, approximately +12M are in occupations that score high on the specification residual (right column), while +8M are in occupations whose management-task score is driven primarily by cognitive complexity (middle column).

---

## 3. The Core Finding: Employment Reallocation Toward Specification Tasks

The central evidence comes from the employment decomposition, not a single correlation statistic.

Exhibit 1 (`exhibit_employment_shift.png`) shows +20M jobs in management-task-intensive occupations vs +5M in execution-task-intensive occupations (2005–2024). Exhibit 2 (`exhibit_employment_shift_decomposed.png`) decomposes this: of the +20M, approximately +12M are in occupations that are specification-intensive beyond what cognitive complexity predicts, while +8M are in occupations whose management-task score is driven primarily by complexity. This decomposition is robust to restricting the sample to above-median-complexity occupations (`robustness_complexity_split.py`: +8.8M spec-specific vs +6.4M complexity-driven among cognitively complex jobs).

At the occupation level, spec_residual has a modest positive association with employment growth among above-median-complexity occupations (Spearman r = 0.108, p = 0.06; employment-weighted Pearson r = 0.143). The qualitative pattern in the GWA task space is consistent: tasks that are specification-specific (Staffing, Controlling Resources, Selling, Building Teams, Guiding Subordinates) characterize growing occupations, while tasks that are complexity-specific but not specification (Documenting, Getting Information, Processing Information, Organizing/Planning) do not independently predict growth.

**The economy is not just getting more cognitively complex. It is specifically shifting toward the subset of cognitive work that involves deciding what to do, as opposed to the subset that involves processing information about what has been decided.** The evidence for this comes from the employment decomposition and the qualitative task-space pattern, not from a single correlation.

---

## 4. Employment Scale

Exhibit 1 (`exhibit_employment_shift.png`) shows the absolute employment shift along the raw management task gradient:

- **Management-task-intensive occupations** (top tercile on management task gradient): 30M → 50M workers (+20M, +66%)
- **Execution-task-intensive occupations** (bottom tercile): 32M → 37M workers (+5M, +16%)

The lines crossed around 2009. By 2024, management-task-intensive occupations employ 13 million more workers than execution-task-intensive ones.

Exhibit 2 (`exhibit_employment_shift_decomposed.png`) decomposes the top tercile into specification-specific and complexity-driven components:

- **Specification-specific component** (management-task top tercile AND spec-residual top tercile): 20M → 32M workers (+12M)
- **Complexity-driven component** (management-task top tercile but NOT spec-residual top tercile): 10M → 18M workers (+8M)

Approximately 60% of the management-task employment shift is attributable to specification-specific tasks; the remaining 40% reflects the broader trend toward cognitively complex work.

---

## 5. Relationship to Existing Literature

### 5.1 Autor, Levy & Murnane (2003) and the Routine/Non-Routine Framework

The foundational [ALM task framework](https://academic.oup.com/qje/article-abstract/118/4/1279/1925105) classifies tasks as routine vs. non-routine and cognitive vs. manual. Computers substitute for routine tasks (both cognitive and manual) and complement non-routine cognitive tasks.

**How our finding extends ALM:** The specification-execution axis is *orthogonal to routine/non-routine within the non-routine cognitive category*. ALM treats non-routine cognitive work as monolithic. We show that within NRC, there are two distinct components:
- **Specification NRC:** directing, allocating, staffing, selling — growing faster
- **Information-processing NRC:** documenting, analyzing, interpreting, organizing — growing slower

This decomposition is invisible in the ALM framework because both components score equally high on "non-routine cognitive." Our management-contrast methodology separates them.

### 5.2 Acemoglu & Autor (2011) — Skills, Tasks and Technologies

[Acemoglu & Autor (2011)](https://economics.mit.edu/sites/default/files/publications/Skills,%20Tasks%20and%20Technologies%20-%20Implications%20for%20.pdf) extend ALM to model task reallocation between labor and capital. Their framework predicts that as the price of computing falls, tasks where machines have comparative advantage shift to capital, while tasks where humans retain comparative advantage remain with labor.

**How our finding informs their framework:** The specification-specific tasks we identify (staffing, resource allocation, negotiation, selling, coaching) are precisely the tasks where human comparative advantage is most durable. These tasks require:
- **Subjective judgment** about what is valuable (not optimizable against a known objective)
- **Social authority** to direct others' actions (not delegable to a non-agent)
- **Preference expression** about what should exist (not derivable from existing data)

These are qualitatively different from other non-routine cognitive tasks like "processing information" or "analyzing data," which are increasingly within AI capabilities.

### 5.3 Acemoglu & Restrepo (2019) — Automation and New Tasks

[Acemoglu & Restrepo (2019)](https://www.aeaweb.org/articles?id=10.1257/jep.33.2.3) model the balance between automation (displacing labor from existing tasks) and the creation of new tasks (reinstating labor demand). They show that if new task creation keeps pace with automation, labor demand is sustained.

**Connection:** Our specification tasks are precisely where "new task creation" happens. Someone must decide that a new product category, organizational structure, or market position should exist. This specification activity is the mechanism through which Acemoglu & Restrepo's "new tasks" enter the economy. If specification labor is irreducible, the new-task-creation channel remains open even as AI automates execution within existing tasks.

### 5.4 Autor (2024) — New Frontiers: The Origins and Content of New Work

[Autor, Chin, Salomons & Seegmiller (2024)](https://academic.oup.com/qje/article/139/3/1399/7612757) show that new job categories emerge from demand shocks — technology creates new things people want, which generates new occupations. They link patent data to the creation of new job titles from 1940 to 2018.

**Connection:** The creation of "new work" is fundamentally a specification activity. Someone decides that a new occupation should exist — that this type of work is worth doing. Our finding that specification-specific tasks are growing faster than other cognitive tasks is consistent with the economy generating more specification-layer activity to direct an increasingly capable but specification-dependent execution layer.

### 5.5 Korinek & Suh (2024) — Scenarios for the Transition to AGI

[Korinek & Suh (2024)](https://www.nber.org/papers/w32152) model scenarios where AI approaches AGI and analyze implications for labor share. In their framework, if AI can eventually perform ALL tasks, labor share goes to zero.

**How our finding pushes back:** The specification tasks we identify may represent a category of human input that is not just technically difficult to automate but *logically irreducible*. Resource allocation, preference expression, and directing others' actions involve setting the *objective function* itself — not optimizing within a given one. If AI systems optimize objectives set by humans, then the activity of setting those objectives (specification) remains irreducibly human regardless of AI capability. This would bound the labor share above zero even as execution tasks are fully automated.

### 5.6 Corrado, Hulten & Sichel (2005, 2009) — Intangible Capital

The [CHS framework](https://academic.oup.com/roiw/article/55/3/661/5146775) decomposes intangible investment into computerized information (software/databases), innovative property (R&D, design), and economic competencies (brand, organizational capital, training).

**Our intangible data finding:** Using INTAN-Invest data for the US (2010-2024), specification capital (organizational capital + design + brand) held roughly steady at ~51% of total intangible investment, while national accounts capital (software + R&D) grew faster. In absolute terms, specification capital doubled from $1.18T to $2.39T. The specification layer is growing in absolute scale even as the execution layer (software) grows faster — consistent with specification being necessary but leveraged by execution automation.

### 5.7 Deming (2017) — Social Skills

[Deming (2017)](https://academic.oup.com/qje/article/132/4/1593/3861633) shows growing labor market returns to social skills, measured via O\*NET variables. He finds that occupations requiring both cognitive and social skills have grown faster and command higher wages.

**Overlap and distinction:** Our specification-specific tasks (staffing, selling, negotiating, coaching, coordinating) are highly social. Deming's finding is consistent with and complementary to ours. However, our framework provides a *why*: these social tasks are growing not just because they require human interaction, but because they are the mechanism through which the economy specifies what to produce. They are specification labor that happens to be social, not just social labor.

---

## 6. Implications for Capital-Labor Substitutability

### The standard model

In standard production theory, output Y = F(K, L) where K is capital and L is labor, with elasticity of substitution σ governing how easily one replaces the other. If σ > 1, capital and labor are gross substitutes — more capital means less labor demand. If σ < 1, they are complements.

The AI-labor debate often assumes σ → ∞ as AI becomes more capable: eventually AI (capital) can do everything labor can, so labor share → 0.

### What our findings suggest

Our results suggest a more nuanced picture. Decomposing labor into specification and execution components:

**Y = F(K, L_spec, L_exec)**

where L_spec = specification labor (directing, allocating, staffing, choosing what to produce) and L_exec = execution labor (implementing, processing, producing).

- **σ(K, L_exec)** is high and rising — AI/capital is increasingly substitutable for execution labor. This is the standard automation story and is consistent with the declining employment share in execution-intensive occupations we document.

- **σ(K, L_spec)** may be bounded — specification labor involves *setting* the objective that capital optimizes. By construction, the optimizer and the objective-setter are logically distinct roles. You can automate the search for the best restaurant to visit; you cannot automate the fact that *someone must want to eat.*

- **Complementarity between K and L_spec:** As K (AI/automation) becomes more capable, each unit of specification labor directs more execution capacity. This is consistent with our finding that specification-intensive occupations grew employment by 66% (2005-2024) while execution-intensive grew only 16% — the economy is adding more specification labor to direct an expanding capital-execution base.

### The irreducible human input

The specification tasks we identify — staffing, resource allocation, selling, negotiating, coaching — share a common feature: they involve **expressing or adjudicating preferences** about what should exist or who should do what. These are not information-processing tasks that could in principle be derived from data. They require an agent with preferences — a *principal* in the principal-agent sense.

Even a perfectly capable AI system needs someone to specify:
- What product to build (not which of known products to optimize)
- Who to hire and for what purpose
- How to allocate scarce resources among competing goals
- What market position to adopt
- Whether an organizational change is worth making

These are the tasks our analysis identifies as specification-specific, and they are the tasks most strongly associated with employment growth beyond the general complexity trend.

---

## 7. Estimating the Elasticity of Substitution

### Approach

We test whether AI capital and specification labor are complements (σ < 1) or substitutes (σ > 1) using three independent approaches. Under CES, if σ < 1, occupations with higher AI exposure should pay a *larger* specification wage premium. Full methodology, results, and robustness details are in [`elasticity_analysis_overview.md`](elasticity_analysis_overview.md).

**Scripts:** `elasticity_estimation.py`, `elasticity_bounds.py`, `elasticity_robustness.py`

### Cross-sectional wage interaction (the main test)

For each year, we regress log occupation wages on spec\_residual, AIOE, their interaction, and PC1:

```
ln(wage_j) = α + β₁·spec_residual + β₂·AIOE + β₃·(spec × AIOE) + γ·PC1 + ε
```

Under CES: **β₃ > 0 implies σ < 1**. The interaction is positive in all 5 years.

**Headline result (Language Modeling AIOE):** Using LLM-specific AI exposure — the AI technology most directly relevant to cognitive work — the pooled interaction is:

- **β₃ = +0.491 (parametric p < 0.0001)**
- **Permutation p = 0.009** (one-sided, 2,000 permutations shuffling spec scores across occupations)
- **Cluster bootstrap 95% CI: [+0.02, +0.97]** — excludes zero
- Individually significant in 3 of 5 years (2005, 2009, 2014)
- Image Generation AIOE shows no interaction (+0.04, p = 0.56) — the effect is specific to language/cognitive AI

The broad AIOE measure (Felten et al.) gives a weaker but directionally consistent result: β₃ = +0.315 (parametric p = 0.002), but the cluster bootstrap CI includes zero ([-0.12, +0.75]).

### Interpreting the negative base specification premium

The coefficient β₁ is negative (~−0.5 to −0.8): at a given complexity level, more specification-intensive occupations earn *less*. This is because, after removing cognitive complexity (PC1), the highest-scoring spec occupations include retail supervisors, food service managers, and sales roles — directive but not high-complexity jobs that pay less than equally-complex technical roles.

The interaction β₃ > 0 means AI exposure progressively erases this penalty. At high LLM exposure, specification skills command a premium rather than a penalty. Examples:

| AIOE bucket | High-spec occupations | Low-spec occupations | Weighted mean wage (high vs low spec) |
|-------------|----------------------|---------------------|--------------------------------------|
| Low AIOE | Waiters, maids, fast-food cooks | Diesel mechanics, maintenance workers | $37K vs $52K (spec penalty) |
| Mid AIOE | Cashiers, retail supervisors | Airline pilots, nurse anesthetists | $49K vs $77K (spec penalty) |
| High AIOE | Marketing managers, sales managers | Aerospace/electrical engineers | $74K vs $101K (gap narrows) |

### Aggregate trends

Relative spec/exec employment rose 44% (0.94 → 1.35) while relative wages declined only 5% (2.07 → 1.96) from 2005 to 2024. Under CES, this requires a large demand shift toward specification labor — consistent with technology (including AI) raising the marginal product of specification work.

### CPS microdata (Track B)

Using CPS ASEC 2024 individual-level data (n = 38,598 workers):

- Spec × AIOE (direct AI exposure): β = +0.084 (p = 0.064) — marginally significant, positive
- Triple interaction (spec × large firm × high AI): β = +0.377 (p = 0.070) — where both firm size and AI exposure are high, the spec premium is amplified

### Diff-in-diff (Track C)

Comparing employment acceleration (2019–2024 vs 2005–2019), spec-intensive occupations in high-AI fields accelerated +0.76 percentage points more than exec-intensive ones in high-AI fields. The regression interaction is positive (+0.024) but not significant (p = 0.15), consistent with only 2–3 years of significant LLM adoption.

### Robustness summary

| Test | Broad AIOE | LM-AIOE |
|------|-----------|---------|
| Pooled β₃ | +0.315 | **+0.491** |
| Permutation p (one-sided) | 0.054 | **0.009** |
| Bootstrap 95% CI | [−0.12, +0.75] | **[+0.02, +0.97]** |
| Bootstrap excludes zero | No | **Yes** |
| Leave-one-out sign stability | 100% positive | — |
| Placebo random axis | 100th percentile | — |
| Unweighted β₃ | −0.068 | −0.014 |

The main result (LM-AIOE) survives permutation inference and cluster bootstrapping. The persistent weakness across both AIOE measures is that the interaction is driven by employment weighting — large-employment occupations drive the pattern, while the median occupation does not show it. This is interpretable (large occupations shape the labor market) but is a genuine limitation.

### Connection to Oberfield & Raval (2021)

Oberfield & Raval estimate σ(K, L) ≈ 0.5 at the plant level and ≈ 0.7 aggregate for US manufacturing (Econometrica 2021). Our plausible range (σ ∈ [0.3, 1.5], weight below 1) overlaps their estimates. The nested CES interpretation: σ(AI, L\_exec) may be high (substitution), while σ(AI, L\_spec) is low (complementarity), with the aggregate σ ≈ 0.7 as a weighted average.

---

## 8. Limitations

1. **Single O\*NET snapshot.** Task content within occupations may have changed over 2005-2024, but we measure only employment reallocation across occupations with fixed profiles.

2. **Five time points.** The employment trend has only 5 observations (2005, 2009, 2014, 2019, 2024). The direction is clear but granular dynamics are uncertain.

3. **Management as specification proxy.** Not all management is specification (some is routine administration), and not all specification is management (entrepreneurs, product designers, creative directors may not be in SOC 11-XXXX). The proxy is defensible but imperfect.

4. **Complexity confound.** R² = 0.905 between the management gradient and PC1 at the occupation level (`spec_exec_management_contrast.py`, line 269). The residual (specification-specific) component is real — approximately 60% of the +20M employment shift is in occupations that score high on specification tasks beyond complexity (`generate_exhibits.py`) — but most of the raw management gradient is attributable to cognitive complexity, not specification specifically. The occupation-level correlation between spec_residual and employment growth is modest (Spearman r = 0.108 among above-median-complexity occupations; `robustness_complexity_split.py`).

5. **No causal identification.** Employment shifts are driven by demand, demographics, trade, regulation, and technology jointly. We show correlation with AI exposure (AIOE) but cannot isolate automation as the causal driver.

6. **National level only.** No geographic or industry decomposition within the task analysis. The firm dynamics analysis (BDS) shows sector-level patterns but at coarse NAICS 2-digit granularity.

7. **Employment weighting drives elasticity results.** The cross-sectional wage interaction (β₃ > 0) is present in employment-weighted regressions but reverses sign without weights. The result describes the labor market in aggregate (where millions of workers are) rather than the typical occupation. This is a genuine limitation of the elasticity analysis.

8. **No IV strategy for elasticity.** Unlike Oberfield & Raval (2021), we use reduced-form cross-sectional variation rather than instrumented wage variation. Our results identify correlation patterns consistent with σ < 1, not causal estimates of σ.

---

## 8. Data and Reproducibility

All analysis is in Python scripts in `analysis/`:

| Script | What it produces |
|--------|-----------------|
| `phase1_data_assembly.py` | Master panel merging O\*NET, OEWS, AIOE |
| `phase2_eda.py` | GWA employment trends, growing/shrinking, within-NRC, wage correlations |
| `phase2d_wage_bands.py` | Within-NRC analysis by pay band |
| `phase3_dwa.py` | Detailed Work Activity prevalence trends |
| `phase4_pca.py` | PCA of GWA space, dimension charts |
| `spec_exec_management_contrast.py` | Management contrast, scoring, decomposition |
| `spec_exec_from_firm_structure.py` | Small vs large firm task contrast |
| `entrepreneurial_phase2_bds.py` | Young-firm job creation shares |
| `entrepreneurial_phase2c_growth_profile.py` | Empirical growth profile employment |
| `entrepreneurial_phase3_intangibles.py` | CHS intangible decomposition |
| `elasticity_estimation.py` | Initial elasticity exploration: 3×3 tables, interaction regressions, wage trends |
| `elasticity_bounds.py` | Three-track estimation: Katz-Murphy, CPS microdata, diff-in-diff |
| `elasticity_robustness.py` | Robustness: permutation, LOO, placebo, bootstrap, LM-AIOE tests |

Raw data sources, crosswalks, and intermediate datasets documented in `data-inventory.md`. Detailed elasticity methodology in [`elasticity_analysis_overview.md`](elasticity_analysis_overview.md).

---

## Key Exhibits

1. **`exhibit_employment_shift.png`** — Employment in management-task-intensive vs execution-task-intensive occupations: 50M vs 37M (2024). Generated by `generate_exhibits.py`.
2. **`exhibit_employment_shift_decomposed.png`** — Decomposes the management-task top tercile: +12M specification-specific vs +8M complexity-driven. Generated by `generate_exhibits.py`.
3. **`robustness_complexity_split.png`** — Side-by-side comparison of full sample vs above-median-complexity restriction. Generated by `robustness_complexity_split.py`.
4. **`exhibit_spec_residual_scatter.png`** — GWA-level scatter of management-specific residual vs growth residual. **Note:** generated in interactive session, not by committed script. Qualitative pattern is consistent with findings but the correlation statistic annotated on the plot is sensitive to methodology (see `robustness_complexity_split.py` for details).
5. **`exhibit_spec_specific_tasks.png`** — What makes management distinctive beyond complexity: staffing, resource control, directing, selling. **Note:** generated in interactive session, not by committed script. Underlying data in `gwa_management_vs_nonmanagement.csv`.
6. **`craft_premium_growth.png`** — Consumer willingness to pay ~2x for specification-intensive (craft) goods. **Note:** generated in interactive session, not by committed script.
7. **`p2d_within_nrc_diff.png`** — Within non-routine cognitive occupations, growing ones emphasize directive/advisory tasks. Generated by `phase2_eda.py`.
8. **`pca_gwa_growth_diff_by_band.png`** — PCA view of growth differentials across pay bands. Generated by `phase4_pca.py`.
9. **`spec_residual_by_payband.png`** — Decomposition within fixed pay bands (complexity dominates, residual flat). **Note:** generated in interactive session, not by committed script.

### Elasticity of Substitution

8. **`elast_wage_coefs_over_time.png`** — β₁ (spec premium), β₂ (AI wage effect), β₃ (interaction) with 95% CIs, 2005–2024
9. **`elast_katz_murphy.png`** — Aggregate spec/exec trends: relative employment, wages, implied demand shift
10. **`elast_bounds_synthesis.png`** — Four-panel synthesis: KM demand shift, cross-section interaction, CPS micro, summary
11. **`elast_dd_acceleration.png`** — Diff-in-diff scatter: employment acceleration by spec intensity and AI exposure
12. **`elast_cps_firmsize.png`** — CPS 2024: large-firm wage premium by specification tercile

### Robustness

13. **`robust_permutation_test.png`** — Null distribution from 2,000 permutations (broad AIOE)
14. **`robust_leave_one_out.png`** — 754 LOO estimates, all positive; DFBETA influence analysis
15. **`robust_placebo_axis.png`** — 1,000 random task axes; spec-exec in 100th percentile
16. **`robust_bootstrap_ci.png`** — Cluster bootstrap distribution (broad AIOE)
17. **`robust_lm_aioe.png`** — **Headline:** LM-AIOE permutation (p=0.009) and bootstrap (CI excludes 0)
18. **`robust_synthesis.png`** — Four-panel robustness synthesis
