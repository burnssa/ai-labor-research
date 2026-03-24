# AI Occupational Exposure (AIOE): Dataset Summary

## Source

Felten, E., M. Raj, and R. Seamans (2021). "Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and its Potential Uses." *Strategic Management Journal*, 42(12), 2195–2217.

The AIOE measures how exposed each occupation is to AI capabilities by linking AI benchmark performance on specific tasks to the O\*NET abilities those tasks require. It is **not** a measure of automation risk or job loss — it measures the degree to which AI applications are relevant to the abilities an occupation requires.

## How AIOE is constructed

1. **AI application benchmarks:** Felten et al. track AI system performance on 10 application categories (abstract strategy games, real-time video games, image recognition, visual question answering, image generation, reading comprehension, language modeling, translation, speech recognition, instrumental track recognition).

2. **Application-to-ability mapping:** A crowd-sourced relatedness matrix (Appendix D in the data file) maps each AI application to 52 O\*NET worker abilities (e.g., "Language Modeling" relates to "Written Comprehension," "Written Expression," "Oral Comprehension"). Each cell is a 0–1 relatedness score.

3. **Ability-level AI exposure (Appendix E):** For each O\*NET ability, compute a weighted average of AI benchmark scores across the 10 applications, weighted by the application-ability relatedness. This gives an "ability-level AI exposure" score for each of the 52 abilities.

4. **Occupation-level AIOE (Appendix A):** For each occupation, compute a weighted average of ability-level AI exposures, weighted by how important each ability is for that occupation (from O\*NET ability importance scores). This gives the final AIOE score.

**Key design feature:** AIOE captures which occupations use abilities that AI systems are getting better at, regardless of whether those occupations are actually being automated. A high AIOE means "AI is relevant to the cognitive abilities this job requires," not "AI will replace this job."

## Files

All in `data/ai-exposure/`:

| File | Contents | Key columns |
|------|----------|-------------|
| `AIOE_DataAppendix.xlsx` | Full dataset with 6 sheets | See below |
| `Language_Modeling_AIOE_AIIE.xlsx` | LM-specific exposure | SOC Code, Language Modeling AIOE |
| `Image_Generation_AIOE_AIIE.xlsx` | Image generation-specific exposure | SOC Code, Image Generation AIOE |

### Sheets in AIOE_DataAppendix.xlsx

| Sheet | Description | Rows | Key columns |
|-------|-------------|------|-------------|
| Appendix A | AIOE by occupation | 774 | SOC Code, Occupation Title, AIOE |
| Appendix B | AIIE by industry (4-digit NAICS) | 250 | NAICS, Industry Title, AIIE |
| Appendix C | AIGE by geography (FIPS) | 3,271 | FIPS Code, Geographic Area, AIGE |
| Appendix D | AI application × ability relatedness matrix | 52 × 10 | O\*NET abilities as rows, 10 AI applications as columns |
| Appendix E | Ability-level AI exposure | 52 | O\*NET Abilities, Ability-Level AI Exposure |

## Foreign keys

| AIOE field | Links to | Format | Match rate |
|------------|----------|--------|------------|
| SOC Code (Appendix A) | O\*NET occupations, BLS OEWS | SOC 2010 format (XX-XXXX) | 662 of 774 match our harmonized panel |
| O\*NET Abilities (Appendix D, E) | O\*NET v29.1 Abilities taxonomy (1.A.\*) | Ability name strings | All 52 abilities |
| NAICS (Appendix B) | Census/BLS industry codes | 4-digit NAICS | — |

**SOC version note:** The AIOE uses SOC 2010 codes. Our master panel harmonizes to SOC 2018. Most codes are identical between versions; the `data/crosswalks/soc_2010_to_2018_crosswalk.xlsx` handles the ~50 codes that changed. After harmonization, 662 of 774 AIOE occupations match our panel.

## Summary statistics

| Statistic | Broad AIOE | LM-AIOE |
|-----------|-----------|---------|
| N occupations | 662 (matched) | 662 (matched) |
| Mean | −0.024 | — |
| SD | 1.013 | — |
| Min | −2.67 (Dancers) | −1.85 (Pressers) |
| Max | +1.53 (Genetic Counselors) | +1.93 (Telemarketers) |
| Median | −0.12 | — |
| Correlation (broad vs LM) | — | r = 0.977 |

The broad AIOE and LM-AIOE are very highly correlated (r = 0.977) but differ at the extremes — LM-AIOE emphasizes language/text-heavy occupations (teachers, writers) over numerical/analytical ones (actuaries, accountants).

## Top 10 most AI-exposed occupations (broad AIOE)

| Rank | AIOE | PC1 | Spec Resid | Wage | Employment | Occupation |
|------|------|-----|-----------|------|------------|-----------|
| 1 | +1.53 | +2.27 | +0.058 | $98,910 | 3,510 | Genetic Counselors |
| 2 | +1.53 | +3.48 | +0.132 | $90,400 | 62,830 | Financial Examiners |
| 3 | +1.52 | +2.57 | +0.127 | $125,770 | 28,340 | Actuaries |
| 4 | +1.50 | −0.61 | +0.104 | $87,930 | 47,170 | Budget Analysts |
| 5 | +1.50 | +1.63 | +0.042 | $156,210 | 25,580 | Judges |
| 6 | +1.49 | −0.24 | +0.126 | $48,510 | 59,900 | Procurement Clerks |
| 7 | +1.48 | +4.50 | +0.161 | $81,680 | 1,448,290 | Accountants and Auditors |
| 8 | +1.47 | +0.78 | +0.126 | $121,680 | 2,220 | Mathematicians |
| 9 | +1.46 | −4.59 | +0.066 | $60,400 | 13,220 | Judicial Law Clerks |
| 10 | +1.46 | +6.22 | +0.201 | $103,960 | 176,420 | Education Administrators, Postsecondary |

**Notable:** High-AIOE occupations span a wide range of cognitive complexity (PC1 from −4.59 to +6.22) and specification intensity (spec residual from +0.042 to +0.201). They are predominantly analytical/evaluative roles — examining financial data, assessing risk, applying rules. Accountants (1.4M workers) are the largest high-AIOE occupation by employment.

## Top 10 most AI-exposed occupations (LM-AIOE)

| Rank | LM-AIOE | Wage | Employment | Occupation |
|------|---------|------|------------|-----------|
| 1 | +1.93 | $34,410 | 66,430 | Telemarketers |
| 2 | +1.86 | $78,270 | 59,590 | English Language and Literature Teachers |
| 3 | +1.81 | $77,010 | 21,170 | Foreign Language and Literature Teachers |
| 4 | +1.81 | $81,500 | 19,860 | History Teachers, Postsecondary |
| 5 | +1.80 | $126,650 | 22,800 | Law Teachers, Postsecondary |
| 6 | +1.80 | $78,050 | 20,840 | Philosophy and Religion Teachers |
| 7 | +1.77 | $82,540 | 12,380 | Sociology Teachers, Postsecondary |
| 8 | +1.77 | $94,680 | 17,170 | Political Science Teachers |
| 9 | +1.75 | $71,470 | 13,560 | Criminal Justice Teachers |
| 10 | +1.75 | $101,690 | 2,950 | Sociologists |

**Notable:** LM-AIOE highlights occupations built around language: teaching humanities/social sciences, telemarketing (scripted persuasion), sociology. These are roles where language comprehension, written expression, and oral communication are the core abilities — precisely what LLMs excel at. The contrast with broad AIOE (which highlights numerical/analytical roles like actuaries) reflects the specific AI technology being measured.

## Bottom 10 least AI-exposed occupations (broad AIOE)

| Rank | AIOE | PC1 | Spec Resid | Wage | Employment | Occupation |
|------|------|-----|-----------|------|------------|-----------|
| 1 | −2.67 | −8.44 | +0.219 | n/a | 9,060 | Dancers |
| 2 | −2.11 | −1.73 | +0.132 | $46,180 | 303,620 | Exercise Trainers |
| 3 | −2.04 | −8.25 | +0.108 | $38,140 | 7,220 | Helpers — Painters/Plasterers |
| 4 | −1.97 | −4.16 | +0.002 | $59,280 | 14,140 | Reinforcing Iron Workers |
| 5 | −1.95 | −8.71 | +0.052 | $33,880 | 26,830 | Pressers, Textile |
| 6 | −1.94 | −3.80 | −0.167 | $46,480 | 15,660 | Helpers — Brickmasons |
| 7 | −1.93 | −3.63 | +0.210 | $32,670 | 522,010 | Dining Room Attendants |
| 8 | −1.90 | −3.95 | +0.034 | $46,940 | 22,640 | Fence Erectors |
| 9 | −1.90 | +0.31 | +0.001 | $40,590 | 5,170 | Helpers — Roofers |
| 10 | −1.83 | −8.45 | +0.109 | $39,790 | 67,500 | Slaughterers and Meat Packers |

**Notable:** Low-AIOE occupations are overwhelmingly physical — construction helpers, textile pressers, meat packers, dancers. They require abilities (manual dexterity, physical coordination, stamina) that AI benchmarks do not assess. These jobs have low cognitive complexity (PC1 strongly negative) and moderate-to-positive spec residual — many involve face-to-face direction or physical judgment that loads on the specification axis even at low complexity.

## Relevance to our analysis

AIOE enters our analysis in the cross-sectional wage interaction:

```
ln(wage_j) = α + β₁·spec_residual_j + β₂·AIOE_j + β₃·(spec × AIOE)_j + γ·PC1_j + ε_j
```

β₃ > 0 means occupations with higher AI exposure pay a larger specification wage premium, implying σ(AI capital, spec labor) < 1.

**Headline result (LM-AIOE):** β₃ = +0.491 (permutation p = 0.009, bootstrap 95% CI [+0.02, +0.97]). The complementarity is specific to language-modeling AI — image generation AIOE shows no interaction (β₃ = +0.04, p = 0.56).

**Interpretation:** In occupations where LLMs are most capable (language-heavy roles), specification skills command a *higher* wage premium, not a lower one. The more relevant AI is to an occupation's core abilities, the more the market rewards the specification component of that occupation's work.

## References

- Felten, E., M. Raj, R. Seamans (2021). "Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and its Potential Uses." *Strategic Management Journal*, 42(12), 2195–2217.
- Felten, E., M. Raj, R. Seamans (2023). "How does AI affect occupations and industries?" (update with Language Modeling and Image Generation variants)
