# Exploratory Data Analysis: Task Composition Shifts in the U.S. Labor Market

## 1. Data and Methodology

**Panel structure:** 5 time points (2005, 2009, 2014, 2019, 2024) × ~650-740 occupations per year, with 621 occupations present in all 5 years.

**Sources merged via SOC codes:**
- O\*NET v29.1 (static snapshot): 41 GWA importance scores + 35 skill importance scores per occupation
- BLS OEWS: employment counts + median/mean wages per occupation per year
- Felten AIOE: AI exposure scores per occupation

**Key design choice:** O\*NET ratings are a single snapshot. All temporal variation comes from *employment shifting across occupations with different task profiles*. This is the cleanest approach — it measures "the economy is moving labor toward occupations that emphasize activity X."

**Employment coverage:** ~90-100% of total national employment after SOC harmonization and filtering (emp ≥ 1,000).

---

## 2. Economy-Wide Task Composition Trends (Phase 2a)

All 41 GWAs are growing in employment-weighted importance — employment is shifting toward occupations that are generally more skill-intensive. But the magnitudes vary dramatically.

**Fastest growing (2005→2024 change in employment-weighted importance):**

| GWA | Change | % Change |
|-----|--------|----------|
| Providing Consultation and Advice to Others | +0.140 | +5.2% |
| Interpreting the Meaning of Information for Others | +0.125 | +4.1% |
| Developing and Building Teams | +0.111 | +3.7% |
| Staffing Organizational Units | +0.111 | +5.1% |
| Guiding, Directing, and Motivating Subordinates | +0.110 | +3.9% |
| Analyzing Data or Information | +0.107 | +3.4% |
| Coaching and Developing Others | +0.100 | +3.3% |
| Training and Teaching Others | +0.097 | +3.0% |
| Developing Objectives and Strategies | +0.094 | +3.2% |
| Making Decisions and Solving Problems | +0.091 | +2.4% |

**Shrinking or flat:**

| GWA | Change | % Change |
|-----|--------|----------|
| Handling and Moving Objects | -0.086 | -2.9% |
| Operating Vehicles/Equipment | -0.055 | -2.3% |
| Performing General Physical Activities | -0.040 | -1.4% |
| Controlling Machines and Processes | -0.039 | -1.5% |
| Repairing Mechanical Equipment | -0.035 | -1.7% |

**Pattern:** The growing activities are interpersonal, strategic, and judgment-oriented. The shrinking activities are physical and machine-related. This is consistent with the broad automation story, but the *specific* activities growing fastest — consultation, interpretation, team-building, staffing — are notably about *directing and shaping work* rather than *doing work*.

---

## 3. Growing vs Shrinking Occupations (Phase 2c)

Splitting occupations into quintiles by employment growth (2005→2024), the GWA differences are stark and almost entirely statistically significant (p < 0.001).

**Top differentiators favoring GROWING occupations:**

| GWA | Difference (Q5-Q1) | p-value |
|-----|-------------------|---------|
| Guiding, Directing, and Motivating Subordinates | +0.740 | < 0.001 |
| Staffing Organizational Units | +0.738 | < 0.001 |
| Coaching and Developing Others | +0.700 | < 0.001 |
| Developing and Building Teams | +0.681 | < 0.001 |
| Providing Consultation and Advice | +0.670 | < 0.001 |
| Selling or Influencing Others | +0.655 | < 0.001 |
| Monitoring and Controlling Resources | +0.614 | < 0.001 |
| Coordinating the Work and Activities of Others | +0.604 | < 0.001 |

**Top differentiators favoring SHRINKING occupations:**

| GWA | Difference (Q5-Q1) | p-value |
|-----|-------------------|---------|
| Controlling Machines and Processes | -0.508 | < 0.001 |
| Handling and Moving Objects | -0.505 | < 0.001 |
| Repairing Mechanical Equipment | -0.393 | < 0.001 |
| Performing General Physical Activities | -0.242 | 0.006 |

**Interpretation:** The fastest-growing occupations score dramatically higher on *people-directing, strategic, and advisory* activities. The fastest-shrinking score higher on *physical manipulation and machine operation*. The gap is largest for the "meta-work" activities — deciding who does what, coaching, consulting, staffing — rather than for core cognitive activities like Analyzing Data or Thinking Creatively (which both grow and shrink occupations score fairly high on).

---

## 4. Within Non-Routine Cognitive (Phase 2d) — The Novel Finding

This is the most important analysis. Among the ~368 occupations classified as non-routine cognitive (top half on an NRC composite), what differentiates the GROWING from SHRINKING ones?

**Top differentiators within NRC:**

| GWA | NRC-Q1 (shrinking) | NRC-Q5 (growing) | Difference | p-value |
|-----|-------------------|------------------|------------|---------|
| Staffing Organizational Units | 2.074 | 2.890 | +0.816 | < 0.001 |
| Providing Consultation and Advice | 2.733 | 3.471 | +0.738 | < 0.001 |
| Guiding/Directing Subordinates | 2.760 | 3.461 | +0.700 | < 0.001 |
| Monitoring and Controlling Resources | 2.483 | 3.164 | +0.681 | 0.001 |
| Coaching and Developing Others | 2.887 | 3.564 | +0.678 | < 0.001 |
| Coordinating Others | 2.939 | 3.573 | +0.634 | < 0.001 |
| Developing Objectives and Strategies | 3.059 | 3.643 | +0.584 | < 0.001 |
| Developing and Building Teams | 3.020 | 3.591 | +0.571 | < 0.001 |

**Activities that do NOT differentiate growing from shrinking NRC:**

| GWA | Difference | p-value |
|-----|-----------|---------|
| Working with Computers | +0.079 | 0.866 |
| Processing Information | +0.057 | 0.810 |
| Communicating with External People | +0.010 | 0.201 |
| Handling and Moving Objects | -0.170 | 0.701 |
| Controlling Machines | -0.154 | 0.554 |

**This is the key finding.** Within the non-routine cognitive category that AI is now penetrating, the *surviving and growing* occupations are distinguished NOT by being more analytically or technically skilled, but by being more **directive, strategic, and interpersonally authoritative**. The growing NRC occupations are the ones that tell other people what to do, set organizational direction, build teams, consult, and coach. The shrinking NRC occupations may be just as cognitively demanding, but their cognitive work is more *procedural* — processing information, working with computers, evaluating compliance.

This is consistent with (though doesn't prove) the specification-labor hypothesis: the human work that persists is the work of *deciding what should be done*, not *doing it*.

---

## 5. Wage Premium Trends (Phase 2e)

GWA-wage correlations (Spearman) are remarkably stable over 2005-2024. The changes are small (< 0.05 in absolute terms). Activities with the *strongest* wage correlations in both years:

- Analyzing Data (+0.67), Interpreting Information (+0.61), Making Decisions (+0.59), Updating Knowledge (+0.61) — all high and stable
- Handling Objects (-0.48), Physical Activities (-0.43), Controlling Machines (-0.29) — all negative and stable

**Modest movers:**
- Training and Teaching: wage correlation *falling* (from +0.33 to +0.28) — growing in prevalence but its wage premium is slightly eroding
- Assisting and Caring: wage correlation *rising* (from -0.18 to -0.14) — becoming less of a wage penalty
- Administrative Activities: wage correlation *falling* (from +0.31 to +0.26)

**In the key scatter plot (employment-weighted change × wage-correlation change):** Most GWAs cluster in the right half (growing prevalence) with near-zero wage-correlation change. The GWAs growing fastest in prevalence (Consultation, Interpreting, Team-Building, Staffing) have *slightly declining* wage correlations — consistent with these activities becoming more widespread (less exclusively high-wage) while still commanding strong absolute wage levels. The upper-right quadrant (growing both prevalence and premium) is mostly empty, with the notable exception of "Building Teams" and "Getting Information."

---

## 6. Automation Exposure Interaction (Phase 2b)

Splitting occupations into AIOE terciles reveals a clear pattern: the "specification-like" GWA trends are **concentrated in the high-AIOE tercile**.

**GWAs with largest High-AIOE vs Low-AIOE divergence:**

| GWA | Low AIOE change | High AIOE change | Difference |
|-----|----------------|-----------------|------------|
| Providing Consultation/Advice | -0.001 | +0.214 | +0.216 |
| Developing Objectives/Strategies | +0.020 | +0.167 | +0.147 |
| Staffing | +0.016 | +0.156 | +0.140 |
| Guiding/Directing Subordinates | +0.018 | +0.153 | +0.135 |
| Developing Teams | +0.021 | +0.152 | +0.131 |

In low-AIOE occupations (mostly physical/manual work), these strategic activities barely changed. In high-AIOE occupations (most exposed to AI), these activities grew substantially — employment shifted *toward the more strategic/directive occupations within the AI-exposed group*.

Meanwhile, some activities declined more in high-AIOE occupations:
- Handling Objects: low AIOE = flat, high AIOE = -0.074
- Working with Public: low AIOE = +0.082, high AIOE = -0.023
- Administrative Activities: low AIOE = +0.032, high AIOE = -0.043

---

## 7. DWA Granularity Check (Phase 3)

**Growing DWAs:** Dominated by healthcare-specific activities (medical diagnosis, treatment planning, patient data analysis). This reflects the massive healthcare employment growth, not a task-content shift per se. Beyond healthcare: "Supervise employees" (+0.036), "Develop procedures to evaluate organizational activities" (+0.032), and "Update knowledge about emerging trends" (+0.030).

**Shrinking DWAs:** Clerical, retail, and routine information-processing: "Answer telephones" (-0.052), "File documents" (-0.041), "Greet customers" (-0.040), "Compile data" (-0.039), "Execute sales transactions" (-0.038). These are classic routine-cognitive and routine-interpersonal activities.

**Keyword analysis:** Spec-keyword DWAs' per-DWA mean prevalence grew from 0.00735 to 0.00950 (+29%). Exec-keyword DWAs stayed flat (0.01193 to 0.01178, -1.3%). This directional finding supports the hypothesis, though the absolute prevalence numbers are small and the keyword classification is crude.

---

## 8. Skills Robustness Check (Phase 2f)

The skills analysis confirms the GWA findings. Fastest-growing skills by employment-weighted importance:

| Skill | Change |
|-------|--------|
| Science | +0.122 |
| Operations Analysis | +0.110 |
| Systems Evaluation | +0.108 |
| Systems Analysis | +0.108 |
| Active Learning | +0.096 |
| Complex Problem Solving | +0.095 |
| Management of Personnel Resources | +0.093 |
| Critical Thinking | +0.091 |

Declining skills: Equipment Maintenance (-0.017), Repairing (-0.015), Operation and Control (-0.004). Only 3 of 35 skills are declining — virtually everything cognitive is growing.

---

## 9. Limitations

1. **Single O\*NET snapshot.** Task content within occupations may have changed over 2005-2024, but we can't measure that. We only capture employment *reallocation* across occupations with fixed task profiles.

2. **Only 5 time points.** 2005-2024 spans an interesting period (pre-smartphone, post-smartphone, pre-LLM), but trend interpretation is limited with n=5.

3. **SOC crosswalk attrition.** ~621 of ~800 occupations survive harmonization across all 5 years. Some occupations are dropped at boundaries where SOC codes split or merge.

4. **National-level only.** No geographic or industry decomposition. The healthcare growth that dominates the DWA analysis may be driven by demographic aging, not automation dynamics.

5. **No causal identification.** Employment shifts are caused by many factors — demand, demographics, trade, regulation — not only automation. The correlation with AIOE is suggestive but not causal.

6. **O\*NET granularity.** GWAs like "Making Decisions and Solving Problems" are too broad — they don't distinguish *what kind* of decisions. The DWA analysis is finer but binary (present/absent, no intensity).

---

## 10. Interpretation

**Does the data support the specification-labor hypothesis?**

The data is *consistent with* the hypothesis but does not definitively prove it. Here's what we observe:

**Supportive evidence:**
- The fastest-growing work activities are about *directing, advising, and shaping what others do* — consultation, team-building, staffing, strategy, coaching. These are specification-adjacent.
- The fastest-shrinking are about *physical execution* — handling objects, operating machines, repairs.
- **Within non-routine cognitive occupations**, the differentiation between growing and shrinking is driven by *directive/strategic* activities, not by *analytical/technical* ones. This suggests a split *within* cognitive work — consistent with the specification/execution distinction.
- This pattern is **more pronounced in high-AI-exposure occupations** — exactly where you'd expect the specification/execution split to emerge if automation is the driver.
- At the DWA level, declining activities cluster around *routine information processing and transactions*, while the specification-keyword group is growing ~29%.

**Complicating factors:**
- Much of the employment growth driving these trends is in **healthcare**, which is a specific sectoral story (aging population) that may not generalize.
- The GWAs growing fastest are mostly *managerial/supervisory*, which could simply reflect a well-known trend toward organizational complexity rather than a specification/execution split.
- Wage correlations are nearly flat — the economy isn't (yet) paying a notably *growing* premium for specification-type activities specifically. The premium was already there in 2005.
- The effects are real but modest in absolute magnitude (~0.1 point on a 5-point scale over 19 years).

**What would strengthen the case:**
- Archived O\*NET data showing task *intensity* changes within occupations (not just employment shifts)
- Industry-by-occupation employment matrices to isolate the healthcare effect
- Post-2022 data showing whether LLM deployment accelerates the within-NRC divergence
- International comparison (do countries with faster AI adoption show faster divergence?)
