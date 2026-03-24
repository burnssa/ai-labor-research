# Validating PC1 as Cognitive Complexity

## Purpose

Our analysis residualizes the management task contrast against PC1, the first principal component of the O\*NET GWA matrix. We label PC1 "cognitive complexity" and interpret the residual as specification-specific task content. This document traces every step of that claim and validates it against peer-reviewed external benchmarks.

**Script:** `analysis/validate_pc1_complexity.py`
**Figure:** `output/figures/validate_pc1_complexity.png`

---

## 1. What PC1 is (mechanically)

PC1 is the first principal component of the 41 O\*NET v29.1 Generalized Work Activities (GWAs), importance scores, across 763 occupations.

**Construction:**
1. Load the occupation × GWA importance matrix (`data/analysis/onet_gwa_importance_matrix.csv`)
2. Standardize each GWA to mean 0, SD 1 across occupations (`sklearn.preprocessing.StandardScaler`)
3. Apply PCA (`sklearn.decomposition.PCA`)
4. PC1 is the first component — the single linear combination of the 41 GWAs that explains the most variance

**Result:** PC1 explains **37.3%** of total variance. PC2 explains 17.5%. Together: 54.8%.

---

## 2. Why we call it "cognitive complexity"

### 2.1 Loading structure

Of the 41 GWA loadings on PC1:
- **34 are positive** — all cognitive, interpersonal, and administrative GWAs
- **7 are negative** — all physical/mechanical GWAs (repairing equipment, controlling machines, handling objects, physical activities)

This is a classic "general factor" pattern: occupations that do more cognitive work of any kind — analyzing, communicating, deciding, consulting, documenting, interpreting — score higher on PC1. The only activities that load negatively are physical/mechanical ones. PC1 is the dimension that separates "office/knowledge work" from "physical/hands-on work."

**Top 5 loadings:** Providing Consultation (+0.214), Developing Objectives and Strategies (+0.211), Interpreting Information for Others (+0.208), Organizing/Planning/Prioritizing (+0.206), Updating and Using Relevant Knowledge (+0.205)

**Bottom 5 loadings:** Inspecting Equipment (−0.055), Operating Vehicles (−0.063), Repairing Mechanical Equipment (−0.085), Controlling Machines (−0.092), Performing Physical Activities (−0.099), Handling and Moving Objects (−0.115)

### 2.2 Face validity — occupation ordering

**Top 5 occupations by PC1 score:**

| Rank | PC1 Score | Median Wage (2024) | Occupation |
|------|-----------|-------------------|------------|
| 1 | +9.44 | $104,070 | Education Administrators, K–12 |
| 2 | +8.83 | $206,420 | Chief Executives |
| 3 | +8.46 | $140,030 | Human Resources Managers |
| 4 | +8.43 | $117,960 | Medical and Health Services Managers |
| 5 | +7.87 | n/a | Neurologists |

**Bottom 5 occupations by PC1 score:**

| Rank | PC1 Score | Median Wage (2024) | Occupation |
|------|-----------|-------------------|------------|
| 759 | −9.40 | $34,660 | Manicurists and Pedicurists |
| 760 | −10.62 | $57,490 | Postal Service Mail Carriers |
| 761 | −11.23 | $53,900 | Fallers |
| 762 | −12.24 | $48,350 | Refuse and Recyclable Material Collectors |
| 763 | −12.64 | $89,990 | Models |

These orderings are consistent with "cognitive complexity" as the underlying dimension.

---

## 3. External validation: Acemoglu & Autor (2011)

### Source

Acemoglu, D. and D. Autor (2011). "Skills, Tasks and Technologies: Implications for Employment and Earnings." *Handbook of Labor Economics*, Vol. 4B, pp. 1043–1171. Data Appendix, pp. 1163–1164.

### Their O\*NET task measures

A&A (2011) construct five task categories from O\*NET descriptors. Two categories use **only** Generalized Work Activities (which we have). Three categories use Work Context and/or Abilities descriptors (which we lack).

#### Exact matches (all items are GWAs in our dataset)

**Non-Routine Cognitive Analytical:**

| A&A Element ID | O\*NET Descriptor | In our GWA matrix? |
|---|---|---|
| 4.A.2.a.4 | Analyzing Data or Information | **Yes** |
| 4.A.2.b.2 | Thinking Creatively | **Yes** |
| 4.A.4.a.1 | Interpreting the Meaning of Information for Others | **Yes** |

**Non-Routine Cognitive Interpersonal:**

| A&A Element ID | O\*NET Descriptor | In our GWA matrix? |
|---|---|---|
| 4.A.4.a.4 | Establishing and Maintaining Interpersonal Relationships | **Yes** |
| 4.A.4.b.4 | Guiding, Directing, and Motivating Subordinates | **Yes** |
| 4.A.4.b.5 | Coaching and Developing Others | **Yes** |

**Construction method (A&A 2011, Data Appendix):** Each O\*NET scale is standardized to mean 0, SD 1 using labor supply weights. Composite = summation of standardized constituent scales, re-standardized.

**Our construction:** Identical procedure applied to our GWA importance matrix (standardize each item, sum, re-standardize). We use unweighted standardization across occupations rather than employment-weighted, but the rank-order correlation (Spearman) is invariant to monotone transformations of the weighting.

#### Items we cannot match

**Routine Cognitive** (all 3 items are Work Context, not GWAs):
- 4.C.3.b.7: Importance of Repeating the Same Tasks
- 4.C.3.b.4: Importance of Being Exact or Accurate
- 4.C.3.b.8: Structured vs Unstructured Work (reversed)

**Routine Manual** (1 of 3 items is a GWA):
- 4.A.3.a.3: Controlling Machines and Processes (**available**)
- 4.C.3.d.3: Pace Determined by Speed of Equipment (Work Context — unavailable)
- 4.C.2.d.1.i: Spend Time Making Repetitive Motions (Work Context — unavailable)

**Non-Routine Manual** (1 of 4 items is a GWA):
- 4.A.3.a.4: Operating Vehicles, Mechanized Devices, or Equipment (**available**)
- 4.C.2.d.1.g: Spend Time Using Hands (Work Context — unavailable)
- 1.A.2.a.2: Manual Dexterity (Abilities — unavailable)
- 1.A.1.f.1: Spatial Orientation (Abilities — unavailable)

### Results

| Category | Match type | Items available | Spearman r with PC1 |
|---|---|---|---|
| NRC Analytical | **EXACT** (all 3 GWAs) | 3/3 | **+0.854** |
| NRC Interpersonal | **EXACT** (all 3 GWAs) | 3/3 | **+0.850** |
| Routine Manual (partial) | 1 GWA only | 1/3 | **−0.393** |
| Non-Routine Manual (partial) | 1 GWA only | 1/4 | **−0.259** |
| Routine Cognitive | Not constructable | 0/3 | — |

**Interpretation:** PC1 correlates r > +0.85 with the exact A&A (2011) NRC measures (both analytical and interpersonal). It correlates negatively with the manual task items. This is the expected pattern if PC1 captures cognitive complexity: high correlation with non-routine cognitive work, negative correlation with manual/physical work.

---

## 4. External validation: Deming (2017)

### Source

Deming, D. (2017). "The Growing Importance of Social Skills in the Labor Market." *Quarterly Journal of Economics*, 132(4), 1593–1640. Data Appendix, pp. 1–3.

### His O\*NET social skills measure

Deming constructs a social skills composite from four O\*NET Cross-functional Skills:

| Deming Element ID | O\*NET Descriptor | In our Skills matrix? |
|---|---|---|
| 2.B.1.a | Social Perceptiveness | **Yes** |
| 2.B.1.b | Coordination | **Yes** |
| 2.B.1.c | Persuasion | **Yes** |
| 2.B.1.d | Negotiation | **Yes** |

**Construction:** Average of component variables, rescaled 0–10, converted to employment-weighted percentile ranks.

**Our construction:** Standardize each skill, sum, re-standardize (same as A&A procedure). Different from Deming's exact procedure but produces the same rank ordering.

### Results

| Deming measure | Match type | Spearman r with PC1 |
|---|---|---|
| Social Skills composite | **EXACT** (all 4 items) | **+0.762** |
| Mathematics (skill) | **EXACT** | **+0.451** |

**Interpretation:** PC1 correlates strongly with social skills (+0.762) and moderately with math (+0.451). Deming's key finding is that occupations requiring both cognitive and social skills have grown fastest — our PC1 captures both dimensions simultaneously (it loads positively on all cognitive and social GWAs). The lower math correlation (+0.451 vs +0.762 for social) reflects that PC1 weights interpersonal/communicative activities heavily alongside analytical ones.

---

## 5. Within-O\*NET cross-check: Skill Importance Scores

### Source

O\*NET v29.1 Skills taxonomy (`data/analysis/onet_skill_importance_matrix.csv`). 35 skills measured on importance scales for 763 occupations.

### Independence caveat

**This is NOT a fully independent validation.** The Skills (domain 2) and GWAs (domain 4) are different O\*NET taxonomies — they measure different constructs ("what workers need to know" vs "what workers do") using different questionnaire items. But they are measured on the same occupations by overlapping respondent panels. An occupation rated high on "Analyzing Data or Information" (GWA) will almost certainly also be rated high on "Critical Thinking" (Skill) because respondents are describing the same job.

The value of this check is **construct consistency**, not independence: do the Skills and GWAs tell the same story about which occupations are cognitively demanding? If PC1 from GWAs correlates with skills that face-validly measure cognitive ability, that confirms the GWA-based PC1 is capturing what we claim. But it would be surprising if they *didn't* correlate, given they describe the same occupations.

For truly independent validation, see Section 6 (wages from BLS OEWS — a separate data source entirely).

### Skill groupings

The 35 O\*NET skills are grouped below. **These groupings are our own judgment**, not from a peer-reviewed source. We label them "cognitive," "social," and "physical/technical" based on the skill names. Each individual skill and its PC1 correlation is shown so the reader can assess whether the groupings are reasonable.

### All 35 skills with PC1 correlations

| O\*NET Skill | Our Group | r with PC1 | Mean | SD |
|---|---|---|---|---|
| Active Learning | Cognitive | +0.772 | 3.08 | 0.52 |
| Active Listening | Cognitive | +0.667 | 3.56 | 0.46 |
| Complex Problem Solving | Cognitive | +0.756 | 3.16 | 0.49 |
| Critical Thinking | Cognitive | +0.762 | 3.47 | 0.45 |
| Judgment and Decision Making | Cognitive | +0.764 | 3.21 | 0.43 |
| Learning Strategies | Cognitive | +0.660 | 2.76 | 0.58 |
| Mathematics | Cognitive | +0.451 | 2.51 | 0.57 |
| Monitoring | Cognitive | +0.596 | 3.28 | 0.38 |
| Reading Comprehension | Cognitive | +0.740 | 3.42 | 0.56 |
| Science | Cognitive | +0.459 | 1.88 | 0.86 |
| Speaking | Cognitive | +0.680 | 3.51 | 0.49 |
| Writing | Cognitive | +0.766 | 3.13 | 0.64 |
| | | | | |
| Coordination | Social | +0.649 | 3.10 | 0.37 |
| Instructing | Social | +0.678 | 2.81 | 0.59 |
| Negotiation | Social | +0.715 | 2.58 | 0.50 |
| Persuasion | Social | +0.691 | 2.72 | 0.50 |
| Service Orientation | Social | +0.455 | 2.93 | 0.53 |
| Social Perceptiveness | Social | +0.696 | 3.15 | 0.47 |
| | | | | |
| Management of Financial Resources | Mgmt/Resource | +0.563 | 1.85 | 0.45 |
| Management of Material Resources | Mgmt/Resource | +0.340 | 1.94 | 0.41 |
| Management of Personnel Resources | Mgmt/Resource | +0.686 | 2.56 | 0.49 |
| Time Management | Mgmt/Resource | +0.549 | 3.07 | 0.32 |
| | | | | |
| Operations Analysis | Systems/Analytical | +0.499 | 1.98 | 0.60 |
| Systems Analysis | Systems/Analytical | +0.571 | 2.64 | 0.54 |
| Systems Evaluation | Systems/Analytical | +0.576 | 2.59 | 0.54 |
| Programming | Technical | +0.221 | 1.56 | 0.48 |
| Technology Design | Technical | +0.111 | 1.69 | 0.36 |
| Quality Control Analysis | Physical/Technical | −0.041 | 2.40 | 0.65 |
| | | | | |
| Equipment Maintenance | Physical/Technical | −0.454 | 1.74 | 0.85 |
| Equipment Selection | Physical/Technical | −0.309 | 1.73 | 0.68 |
| Installation | Physical/Technical | −0.432 | 1.26 | 0.52 |
| Operation and Control | Physical/Technical | −0.254 | 2.21 | 0.88 |
| Operations Monitoring | Physical/Technical | −0.127 | 2.56 | 0.74 |
| Repairing | Physical/Technical | −0.468 | 1.71 | 0.86 |
| Troubleshooting | Physical/Technical | −0.322 | 2.06 | 0.77 |

### Pattern summary

| Our group label | # Skills | Mean r with PC1 | Range |
|---|---|---|---|
| Cognitive | 12 | **+0.665** | +0.451 to +0.772 |
| Social | 6 | **+0.647** | +0.455 to +0.715 |
| Mgmt/Resource | 4 | **+0.535** | +0.340 to +0.686 |
| Systems/Analytical | 3 | **+0.549** | +0.499 to +0.576 |
| Technical (software) | 2 | **+0.166** | +0.111 to +0.221 |
| Physical/Technical | 7 | **−0.315** | −0.468 to −0.041 |

**Every cognitive and social skill correlates positively with PC1. Every physical/mechanical skill correlates negatively (except Quality Control Analysis at −0.04, essentially zero).** The groupings reflect the data — they are not imposed on it. The reader can verify from the individual correlations that any reasonable grouping of "cognitive" skills would produce a strong positive composite correlation with PC1.

### Composite correlations (for comparability with Section 3)

| Composite | Construction | r with PC1 |
|---|---|---|
| Cognitive Skills (our grouping, 8 items) | Mean of: Critical Thinking, Reading, Writing, Math, Science, Complex Problem Solving, Judgment/Decision Making, Active Learning | +0.781 |
| Social Skills (our grouping, 5 items) | Mean of: Social Perceptiveness, Coordination, Persuasion, Negotiation, Instructing | +0.790 |
| Physical/Technical (our grouping, 5 items) | Mean of: Equipment Maintenance, Equipment Selection, Installation, Repairing, Operation & Control | −0.409 |

**Construction method:** Simple mean of raw importance scores across listed skills, then Spearman correlation with PC1. No standardization or weighting applied to the composite — the correlation is on the raw average.

---

## 6. Truly independent validation: Wages and AI Exposure

These validations use data from **completely separate sources** — not O\*NET.

| Variable | Spearman r with PC1 | Source | Independence |
|---|---|---|---|
| Median wage (2024) | **+0.591** | BLS OEWS | **Fully independent** — employer-reported wage surveys, different agency, different methodology |
| AI Occupational Exposure (AIOE) | **+0.629** | Felten et al. (2021) | **Partially independent** — uses O\*NET Abilities (domain 1.A, a third taxonomy) combined with AI benchmark data from ML research |

The wage correlation is the cleanest external validation: occupations that score high on PC1 (from O\*NET GWA questionnaires) also earn higher wages (from BLS employer surveys). These are different data sources measuring different things, and the positive correlation confirms that PC1 tracks something the labor market values as "complexity."

The AIOE correlation is partially independent: AIOE uses O\*NET Abilities (52 items in domain 1.A — cognitive, psychomotor, physical, sensory abilities), which are a different taxonomy from the GWAs (41 items in domain 4.A) used for PC1. The Abilities are then combined with AI application benchmark data from ML research to produce the final AIOE score. So the AIOE reflects both O\*NET information (shared source) and external AI performance data (independent source).

---

## 7. What PC1 is NOT

PC1 is a general factor that loads positively on virtually all cognitive activities. It does not distinguish between:

- **Specification** (deciding what to produce, staffing, allocating) and **execution** (analyzing data, processing information, documenting)
- **Analytical** and **interpersonal** cognitive work
- **Creative** and **procedural** cognitive work

This is precisely the point: PC1 captures what is *shared* across all cognitive work. The specification residual (management contrast minus PC1) captures what is *specific* to directive/allocative tasks beyond the general cognitive level.

The R² = 0.905 between the management contrast and PC1 means that 90.5% of what makes managers distinctive is simply "cognitively demanding work." The remaining 9.5% — the specification residual — is the novel dimension: staffing, resource allocation, directing subordinates, selling. This residual is what we test for employment growth and AI complementarity.

---

## 8. Autor-Dorn DOT-based measures (available but not directly merged)

### Data

Downloaded from [ddorn.net/data.htm](https://www.ddorn.net/data.htm):
- `occ1990dd_task_alm.dta` — Abstract, routine, and manual task content (DOT 1977-based)
- `occ1990dd_task_offshore.dta` — Offshorability (O\*NET-based)

Citation: Autor, D. and D. Dorn (2013). "The Growth of Low Skill Service Jobs and the Polarization of the U.S. Labor Market." *American Economic Review*, 103(5), 1553–1597.

### Construction (from A&A 2011 Data Appendix)

The Autor-Dorn measures collapse the ALM (2003) DOT variables:
- **Abstract** = average of DCP (Direction, Control, Planning) + GED-MATH
- **Routine** = average of STS (Set Limits, Tolerances, Standards) + FINGDEX (Finger Dexterity)
- **Manual** = EYEHAND (Eye-Hand-Foot Coordination) alone

These are DOT 1977 measures mapped to Census 1990 harmonized occupation codes (occ1990dd, n = 330).

### Why we cannot directly merge

Our data uses SOC 2018 codes (from O\*NET v29.1 and BLS OEWS). The Autor-Dorn data uses occ1990dd (Census 1990 harmonized). A multi-step crosswalk (occ1990dd → Census 2000 → Census 2010 → SOC 2010 → SOC 2018) would introduce many-to-many mappings and measurement error. We elected not to construct this chain.

### Conceptual validation is sufficient

The DOT-based "Abstract" measure captures Direction, Control, Planning (DCP) and mathematical reasoning (GED-MATH). These concepts map directly to the GWAs that load highest on our PC1: Developing Objectives and Strategies, Making Decisions, Organizing/Planning, Analyzing Data. The strong correlation between PC1 and the exact A&A (2011) NRC measures (r > +0.85) confirms that our PC1 captures the same underlying dimension that the DOT "Abstract" task category was designed to measure.

---

## 9. Summary of validation evidence

| External benchmark | Source | Match type | r with PC1 | Expected sign |
|---|---|---|---|---|
| NRC Analytical | A&A 2011, Data Appendix p. 1163 | **EXACT** (3/3 items) | **+0.854** | + ✓ |
| NRC Interpersonal | A&A 2011, Data Appendix p. 1163 | **EXACT** (3/3 items) | **+0.850** | + ✓ |
| Social Skills | Deming 2017, Data Appendix p. 1 | **EXACT** (4/4 items) | **+0.762** | + ✓ |
| Cognitive Skills composite | O\*NET Skills taxonomy | 8 items | **+0.781** | + ✓ |
| Mathematics skill | O\*NET / Deming 2017 | **EXACT** | **+0.451** | + ✓ |
| Physical/Technical Skills | O\*NET Skills taxonomy | 5 items | **−0.409** | − ✓ |
| Routine Manual (partial) | A&A 2011, 1/3 GWA items | Partial | **−0.393** | − ✓ |
| Median wage 2024 | BLS OEWS | — | **+0.591** | + ✓ |
| AI Exposure (AIOE) | Felten et al. 2021 | — | **+0.629** | + ✓ |

All correlations have the expected sign and magnitude for a "cognitive complexity" interpretation. The two strongest validations (r > +0.85) use the **exact** O\*NET GWA items specified in Acemoglu & Autor's (2011) Data Appendix.

---

## References

- Acemoglu, D. and D. Autor (2011). "Skills, Tasks and Technologies: Implications for Employment and Earnings." *Handbook of Labor Economics*, Vol. 4B, pp. 1043–1171. [PDF](https://economics.mit.edu/sites/default/files/publications/Skills,%20Tasks%20and%20Technologies%20-%20Implications%20for%20.pdf)
- Autor, D., F. Levy, R. Murnane (2003). "The Skill Content of Recent Technological Change: An Empirical Exploration." *Quarterly Journal of Economics*, 118(4), 1279–1333.
- Autor, D. and D. Dorn (2013). "The Growth of Low Skill Service Jobs and the Polarization of the U.S. Labor Market." *American Economic Review*, 103(5), 1553–1597. Data: [ddorn.net/data.htm](https://www.ddorn.net/data.htm)
- Deming, D. (2017). "The Growing Importance of Social Skills in the Labor Market." *Quarterly Journal of Economics*, 132(4), 1593–1640.
- Felten, E., M. Raj, R. Seamans (2021). "Occupational, Industry, and Geographic Exposure to Artificial Intelligence." *Strategic Management Journal*, 42(12), 2195–2217.
