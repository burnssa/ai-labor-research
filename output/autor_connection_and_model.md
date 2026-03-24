# Extending Autor's Framework: Specification vs Execution as a Second Task Dimension

## 1. Autor's Framework (the starting point)

### The four paradigms (WP 30074, "Unbridled Enthusiasm to Vast Uncertainty")

Autor (2022) organizes thinking about technology and labor into four successive paradigms:

1. **Education Race** (Tinbergen 1974; Katz & Murphy 1992): Technology is factor-augmenting — it makes workers more productive. Two skill types (H, L) compete in a CES production function. σ ≈ 1.4–1.7 between college and non-college workers. Key limitation: cannot explain absolute wage *declines* for low-skill workers.

2. **Task Polarization** (ALM 2003; Acemoglu & Autor 2011): Jobs are bundles of tasks. Technology *replaces* workers in routine tasks (codifiable rules) and *complements* them in non-routine tasks (tacit knowledge). Produces U-shaped polarization.

3. **Automation-Reinstatement Race** (Acemoglu & Restrepo 2018, 2019): Tasks are not static. Automation displaces labor; new task creation ("reinstatement") generates fresh demand. The net effect depends on which force dominates.

4. **AI Uncertainty**: AI overturns Polanyi's Paradox — computers can now infer tacit relationships. The boundary between automatable and non-automatable becomes unclear. "Vast uncertainty."

### The formal task model (WP 30389, "New Frontiers")

Tasks are indexed on a continuum [N_{j-1}, N_j] within each sector j:

```
Y_j = [∫ y_j(i)^((σ-1)/σ) di]^(σ/(σ-1))
```

Each task i is produced by either machines (if i < I_j) or labor (if i > I_j):

```
y_j(i) = B_j · q_j(i)^η · k_j(i)^(1-η)           if i ∈ [N_{j-1}, I_j]  (automated)
y_j(i) = B_j · q_j(i)^η · [γ_j(i) · n_j(i)]^(1-η)  if i ∈ (I_j, N_j]    (labor)
```

where γ_j(i) is strictly increasing — labor has progressively stronger comparative advantage in higher-indexed tasks.

**The labor composite** is Cobb-Douglas between high-skill (H) and low-skill (L):

```
n_j(i) = l_j(i)^{α_j} · h_j(i)^{1-α_j}
```

**Critical maintained assumption:** σ > 1 (tasks are gross substitutes). This is footnote 15, p. 23 of WP 30389.

### Autor's key empirical results

- 60% of 2018 employment is in job titles that didn't exist in 1940
- New work creation concentrates in professional/technical/managerial occupations (post-1980)
- Augmentation strongly predicts new job title emergence; automation does not
- Automation's employment-eroding effects more than doubled from 1940–80 to 1980–2018

### What Autor says about AI and specification-adjacent tasks

From WP 30074, p. 24:

> "I feel confident that the *most* skilled workers will likely continue to be complemented by advances in computing and AI — such as workers who invent, design, research, lead, entertain, and educate. But this observation is not limited to those with elite educations."

He predicts AI will automate "mid- and high-level decision-making tasks that have historically been performed by managers and professionals" — in finance, investing, inventory management, credit issuance, fraud detection, design.

But he provides this as a **prediction**, not a structural result. His framework cannot explain *why* some cognitive tasks resist automation more than others, because the labor composite treats all labor symmetrically within a task.

---

## 2. What's missing: the spec-exec dimension

### The gap in Autor's framework

Autor's task model has **one continuum**: automated ←→ human, ordered by comparative advantage γ(i). His labor decomposition has **one dimension**: skill (H vs L).

Neither dimension captures the distinction between:
- A marketing manager **deciding** what campaign to run (specification)
- A data analyst **executing** the analysis the manager requested (execution)

Both are non-routine cognitive tasks. Both may be high-skill. But they differ fundamentally in their relationship to AI capital: the analyst's work is increasingly within AI capabilities; the manager's decision about *what to analyze and why* is not.

### The specification-execution axis is orthogonal to both skill and routine/non-routine

Our empirical analysis defines specification by contrasting management occupations (SOC 11-XXXX) against all others on 41 O\*NET Generalized Work Activities, then residualizing against cognitive complexity (PC1). This ensures the axis measures something **beyond** skill/complexity.

The specification-specific tasks (staffing, resource allocation, directing, selling, negotiating) are:
- **Not just "high-skill"**: Retail supervisors and food service managers score high on spec but low on complexity
- **Not just "non-routine"**: Both specification and execution tasks are non-routine cognitive
- **About setting objectives vs optimizing within them**: Specification tasks involve expressing preferences about what should exist; execution tasks involve processing information within given objectives

### The core finding

The economy added 20M management-task-intensive jobs vs 5M execution-task-intensive jobs (2005–2024). Of the 20M, approximately 12M are in occupations that score high on specification-specific tasks beyond what cognitive complexity predicts (`generate_exhibits.py`). This signal is invisible in both the skill-premium framework and the routine/non-routine framework.

---

## 3. Proposed model extension

### Autor's labor composite (current)

```
n_j(i) = l(i)^{α_j} · h(i)^{1-α_j}
```

All labor within a task is combined Cobb-Douglas (σ = 1 between skill types). There is no distinction between directing work and executing it.

### Extension: decompose by spec vs exec

Replace the undifferentiated labor composite with a nested CES:

```
n_j(i) = [β · l_spec(i)^ρ + (1-β) · l_exec(i)^ρ]^{1/ρ}
```

where σ_spec = 1/(1-ρ) is the elasticity of substitution between specification and execution labor within each task.

**Alternatively**, following Autor's two-sector structure, decompose tasks themselves into specification and execution tiers:

```
Tier 1 (specification): What to produce, resource allocation, staffing, directing
Tier 2 (execution): Implementation, processing, producing

Y = F(Y_spec, Y_exec) where Y_exec = G(K_AI, L_exec)   [high substitutability]
                       and   Y_spec = H(K_AI, L_spec)   [low substitutability]
```

The key structural assumption: **σ(K_AI, L_exec) > σ(K_AI, L_spec)**. AI substitutes for execution but complements specification.

### How this changes the comparative statics

In Autor's model, when AI extends automation (I_j rises), labor is displaced from marginal tasks. The skill premium changes depend on which sector is affected.

In the extended model, AI extension has **heterogeneous effects within the non-automated task set**:

1. **Execution tasks above I_j**: AI may not fully automate these, but it substitutes partially (high σ). Employment in exec-intensive occupations grows slowly or declines.

2. **Specification tasks above I_j**: AI complements these (low σ). Each unit of spec labor directs more AI-augmented execution capacity. Employment in spec-intensive occupations grows.

3. **New task creation** (N_j rises): New tasks are disproportionately specification tasks — someone must decide the new task should exist. This is the mechanism through which Acemoglu & Restrepo's "task reinstatement" works.

### Implications for the σ > 1 assumption

Autor's formal results require σ > 1 between tasks (gross substitutes). Our finding that σ(K_AI, L_spec) < 1 does not contradict this — it concerns the elasticity between AI capital and specification labor *within* a task, not between tasks. The two elasticities operate at different levels of the production structure:

- **Between tasks**: σ_tasks > 1 (Autor's assumption — tasks are substitutable in production)
- **Within a task, between inputs**: σ(K, L_spec) < 1 (our finding — AI and spec labor are complements)

These are compatible. Even if tasks are substitutable, the *inputs* to each task may be complementary.

---

## 4. Why this matters for the AI-labor debate

### Autor's uncertainty

Autor concludes with "vast uncertainty" because AI has erased the boundary between automatable and non-automatable tasks. If AI can do anything, labor share → 0.

### Our response

The specification-execution decomposition suggests the uncertainty is **bounded**. Even if AI can execute any task, someone must still:

- Decide **what** to execute (product specification)
- Decide **who** does what (staffing, resource allocation)
- Decide **whether** the output is what was wanted (evaluation, adjudication)
- Express **preferences** about what should exist (the objective function itself)

These are not tasks that happen to be technically difficult for AI. They are *logically distinct* from optimization — they are the act of setting the objective that AI optimizes. The optimizer and the objective-setter are different roles by construction.

### Connecting to Autor's specific claims

| Autor's claim | Our extension |
|--------------|--------------|
| "The most skilled workers will be complemented" | It's not skill that determines complementarity — it's whether the work is specification or execution. A retail supervisor (low-skill, high-spec) benefits from AI; a data analyst (high-skill, low-spec) may not. |
| AI will automate "mid- and high-level decision-making" | Yes, but only the *execution* component of decision-making — processing information, evaluating options within given criteria. The *specification* component — deciding what criteria matter — resists automation. |
| 60% of employment is in "new work" | New work creation is specification work. Someone must decide a new occupation should exist. Our finding that spec-intensive employment grew +66% vs +16% for exec-intensive is the mechanism. |
| Augmentation concentrates in professional/managerial occupations | Because those occupations are specification-intensive. Our management contrast identifies *which* features of those occupations drive this pattern. |
| "Vast uncertainty" about what AI can do | The uncertainty is real for execution tasks. For specification tasks, the question is not about AI capability but about logical structure: optimization requires an objective; setting the objective is not optimization. |

### The LM-AIOE result sharpens this

Our strongest empirical finding: using **language-modeling-specific** AI exposure (the most relevant AI technology for cognitive work), the cross-sectional wage interaction is:

- β(spec × LM-AIOE) = +0.491, permutation p = 0.009, bootstrap 95% CI [+0.02, +0.97]
- The interaction is absent for image generation AI (+0.04, p = 0.56)

This means the complementarity is specific to the AI technology most directly capable of executing cognitive tasks. LLMs can write, analyze, summarize, code — but occupations where specification skills interact with LLM exposure show *higher* wage premiums, not lower. The more capable the AI execution engine, the more valuable the human specification layer.

---

## 5. Sketch of the article argument

1. **Start with Autor's framework**: Technology displaces labor from some tasks and creates new tasks. The net effect depends on the balance. AI has made the boundary uncertain.

2. **Introduce the missing dimension**: Within non-routine cognitive work, there are two distinct components — specification (deciding what to do) and execution (doing it). The routine/non-routine distinction misses this because both are non-routine.

3. **Present the empirical evidence**: The economy is shifting toward specification tasks (+20M management-task-intensive jobs vs +5M execution-task-intensive, of which ~12M are specification-specific beyond complexity). This is not just a skill story — it's orthogonal to cognitive complexity.

4. **Show the elasticity evidence**: Using LLM-specific AI exposure, specification-intensive occupations pay a *higher* wage premium in AI-exposed fields (β = +0.49, p = 0.009 permutation). This implies σ(LLM capital, spec labor) < 1 — they are complements. Image generation AI shows no such pattern.

5. **The structural argument**: This complementarity is not incidental. Specification tasks involve setting the objective function that AI optimizes. The optimizer and the objective-setter are logically distinct. This bounds the "vast uncertainty" — even as AI capability grows, the specification layer persists because it is the *input* to AI, not a task AI performs.

6. **Implications**: Labor share does not → 0 as AI scales, because specification labor is an essential complement to AI capital. The economy is already shifting employment toward specification — 50M workers in spec-intensive occupations vs 37M in exec-intensive (2024), up from near-parity in 2005.

---

## References

- Autor, D. (2022). "The Labor Market Impacts of Technological Change: From Unbridled Enthusiasm to Qualified Optimism to Vast Uncertainty." NBER WP 30074. https://www.nber.org/system/files/working_papers/w30074/w30074.pdf
- Autor, D., C. Chin, A. Salomons, B. Seegmiller (2024). "New Frontiers: The Origins and Content of New Work, 1940-2018." QJE 139(3), 1399-1465. NBER WP 30389. https://www.nber.org/system/files/working_papers/w30389/w30389.pdf
- Oberfield, E. and D. Raval (2021). "Micro Data and Macro Technology." Econometrica 89(2), 703-732. https://www.nber.org/system/files/working_papers/w20452/w20452.pdf
- Acemoglu, D. and D. Autor (2011). "Skills, Tasks and Technologies: Implications for Employment and Earnings." Handbook of Labor Economics Vol. 4B.
- Acemoglu, D. and P. Restrepo (2019). "Automation and New Tasks: How Technology Displaces and Reinstates Labor." JEP 33(2), 3-30.
- Katz, L. and K. Murphy (1992). "Changes in Relative Wages, 1963-1987: Supply and Demand Factors." QJE 107(1), 35-78.
- Felten, E., M. Raj, R. Seamans (2021). "Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and its Potential Uses." Strategic Management Journal 42(12), 2195-2217.
- Deming, D. (2017). "The Growing Importance of Social Skills in the Labor Market." QJE 132(4), 1593-1640.
- Korinek, A. and J. Suh (2024). "Scenarios for the Transition to AGI." NBER WP 32152.
