# Modeling Strict Complementarity: Specification as Irreducible Input

## The core claim to formalize

- Execution labor and AI capital are substitutes (σ > 1): AI can increasingly do execution work
- Specification labor is **not substitutable at all**: no amount of AI capital can replace the act of deciding what to produce, who does what, and how resources are allocated
- This bounds labor share above zero even as AI scales arbitrarily

Below are three formalizations, from simplest to most structurally motivated.

---

## Option A: Nested CES with Leontief top (σ_spec = 0)

The most direct representation. Two nesting levels:

**Inner nest (execution):** AI capital substitutes for execution labor.

```
Y_exec = [α · K_AI^ρ + (1-α) · L_exec^ρ]^{1/ρ}     where ρ > 0, so σ_exec = 1/(1-ρ) > 1
```

**Outer nest (specification):** Specification labor is strictly complementary — you need both spec labor and execution output:

```
Y = min(A · L_spec, Y_exec)         [Leontief — σ_spec = 0]
```

### Properties

In equilibrium, the binding constraint determines output:

- **When spec is scarce** (A · L_spec < Y_exec): Y = A · L_spec. Output is entirely determined by specification labor. Adding more AI capital or execution labor does nothing — the economy is bottlenecked on deciding what to produce.

- **When spec is abundant** (A · L_spec > Y_exec): Y = Y_exec. The economy is bottlenecked on execution capacity. More AI capital raises output.

### What happens as K_AI → ∞

If σ_exec > 1, capital can fully substitute for execution labor:

```
Y_exec → α^{1/ρ} · K_AI     as K_AI → ∞ (capital dominates)
```

But output is still bounded: **Y = min(A · L_spec, α^{1/ρ} · K_AI) = A · L_spec** once K is large enough. The economy necessarily shifts to the spec-constrained regime. Output grows only by adding specification labor.

### Labor share

When spec-constrained: MPL_spec = A, so w_spec · L_spec = A · L_spec = Y. **All income accrues to specification labor** (capital earns zero marginal product since execution capacity is slack).

This is too extreme for a realistic model — it says that in the limit, capital earns nothing. But it captures the conceptual point cleanly: specification labor is the irreducible bottleneck.

### Verdict

Cleanest representation of "strict complementarity." Good for conveying the intuition. Too extreme for quantitative implications.

---

## Option B: Nested CES with Cobb-Douglas top (σ_spec = 1)

Soften the Leontief to Cobb-Douglas between spec and execution output:

**Inner nest (execution):**

```
Y_exec = [α · K_AI^ρ + (1-α) · L_exec^ρ]^{1/ρ}     where σ_exec > 1
```

**Outer nest:**

```
Y = L_spec^β · Y_exec^{1-β}     where β ∈ (0,1)
```

### What happens as K_AI → ∞

```
Y_exec → α^{1/ρ} · K_AI

Y → L_spec^β · (α^{1/ρ} · K_AI)^{1-β}
```

Output grows with capital, but with diminishing returns (exponent 1-β < 1). Each additional unit of capital is less valuable without more specification labor.

### Labor share

By the Cobb-Douglas property:

```
Specification labor share = β                    (constant, always)
Execution labor share     → 0 as K_AI → ∞       (capital substitutes away exec labor)
Capital share             → (1-β) as K_AI → ∞
Total labor share         → β > 0                (bounded below)
```

**β is the floor on labor share.** If specification-intensive occupations currently account for ~57% of employment (50M of 87M in our data), and if those workers capture income proportional to their contribution, β might be in the range 0.3–0.5.

### Key implication

Even with arbitrarily capable AI that can do all execution work:
- **Labor share never reaches zero** — it converges to β
- **Employment shifts toward specification** — the economy needs more L_spec to complement growing K
- **Specification wages rise** — w_spec = β · Y / L_spec, and Y is growing faster than L_spec
- **Execution wages fall** — exec workers compete with capital in a σ > 1 world

### Connection to the data

This is consistent with what we observe:
- Spec employment: 30M → 50M (+66%, 2005–2024)
- Exec employment: 32M → 37M (+16%)
- Spec/exec wage ratio: 2.07 → 1.96 (slight decline — but spec wages rising in absolute terms)

The slight decline in the wage *ratio* is consistent with the spec share growing (more spec workers → lower marginal product of each), while the absolute growth is consistent with Y growing fast enough to dominate.

### Verdict

The most useful formalization for the article. Simple, well-understood, gives clean results. The parameter β directly maps to "what fraction of economic value requires human specification."

---

## Option C: Specification as scope, execution as scale (variety model)

The most structurally motivated option. Draws on the logic of endogenous growth theory (Romer 1990) where "inventors" determine the *number* of product varieties and "producers" determine the *quantity* of each.

**Specification labor determines the scope of production** — how many distinct products/services/projects the economy pursues:

```
Y = [∫₀^{N} y(v)^{(σ-1)/σ} dv]^{σ/(σ-1)}
```

where N is the number of "varieties" (products, projects, initiatives) and each variety v is produced with:

```
y(v) = K_AI(v)^α · L_exec(v)^{1-α}
```

**The specification labor input:** Each variety requires δ units of specification labor to *exist* — to be conceived, resourced, directed, and evaluated:

```
N = L_spec / δ
```

This is not a production function choice — it's a structural constraint. You cannot produce a variety without someone specifying it.

### Equilibrium

With symmetric allocation across varieties:

```
K_AI(v) = K_AI / N,     L_exec(v) = L_exec / N

y(v) = (K_AI/N)^α · (L_exec/N)^{1-α} = (1/N) · K_AI^α · L_exec^{1-α}

Y = N^{σ/(σ-1)} · (1/N) · K_AI^α · L_exec^{1-α}
  = N^{1/(σ-1)} · K_AI^α · L_exec^{1-α}
```

Substituting N = L_spec/δ:

```
Y = (L_spec/δ)^{1/(σ-1)} · K_AI^α · L_exec^{1-α}
```

### Properties

**Specification labor has increasing returns to output through variety expansion:**

```
∂Y/∂L_spec = [1/(σ-1)] · Y / L_spec
```

The elasticity of output with respect to spec labor is 1/(σ-1). If σ = 2 (moderate task substitutability), this elasticity is 1 — doubling spec labor doubles output by doubling the number of projects each directed by AI-augmented execution.

**Capital and exec labor substitute within each variety** (Cobb-Douglas here, but could be CES with σ_exec > 1).

**Specification labor is not substitutable** — it doesn't appear in the within-variety production function at all. It determines *how many* varieties exist, not *how much* of each is produced. Capital and exec labor cannot create a new variety; only spec labor can.

### What happens as K_AI → ∞

```
Y → (L_spec/δ)^{1/(σ-1)} · K_AI^α · L_exec^{1-α}
```

Output grows with capital, but the spec-labor term (L_spec/δ)^{1/(σ-1)} acts as a multiplicative scalar. The economy gets more execution capacity per variety but not more varieties. To translate capital growth into proportional output growth, you need spec labor to grow proportionally.

### Labor shares

```
Spec labor share:  1/(σ-1) / [1/(σ-1) + 1]  =  1/σ
Exec labor share:  (1-α) · (σ-1)/σ
Capital share:     α · (σ-1)/σ
```

As AI substitutes for exec labor (α rises toward 1):
- Exec labor share → 0
- Capital share → (σ-1)/σ
- Spec labor share → 1/σ (unchanged — structural floor)

For σ = 2: spec labor share = 50%. For σ = 3: spec labor share = 33%.

### Why this model is appealing

1. **Spec labor creates varieties, not quantities.** This captures the conceptual point precisely: specification is about deciding *what* to produce, not *how much*. AI can scale execution but cannot conceive new products/projects.

2. **The irreducibility is structural, not parametric.** Spec labor isn't complementary because σ happens to be low — it's complementary because it enters the production function *at a different level*. It's not an input to production; it's an input to the *scope* of production.

3. **Maps to the empirical pattern:** New work creation (Autor's finding that 60% of jobs are "new") is literally N growing — spec labor expanding the variety set. Augmentation concentrating in professional/managerial occupations is spec labor directing new varieties.

4. **Capital accumulation increases demand for spec labor:** More K means each variety is more productive, so the return to adding another variety (more spec labor) increases. This is the complementarity mechanism.

### Verdict

The most structurally compelling model. Requires more exposition but gives the cleanest separation between "what AI does" (scales execution within varieties) and "what humans do" (choose which varieties to produce). The irreducibility is a structural feature of the model, not a parameter assumption.

---

## Comparison

| Feature | Option A (Leontief) | Option B (Cobb-Douglas) | Option C (Variety) |
|---------|--------------------|-----------------------|-------------------|
| σ(K, L_spec) | 0 (fixed proportions) | n/a (different nesting) | n/a (different role) |
| Spec labor's role | Input alongside exec output | Input alongside exec output | Determines scope/variety |
| Labor share floor | 100% (too extreme) | β (realistic, tunable) | 1/σ_tasks |
| As K→∞ | Y bounded by L_spec | Y grows, share → β | Y grows, share → 1/σ |
| Irreducibility | Parametric (σ = 0) | Functional form (Cobb-Douglas) | **Structural** (different level) |
| Tractability | Simple | Simple | Moderate |
| Connection to Autor | Extends task model | Extends task model | Extends new-work-creation model |
| Best for | Intuition, talks | Article's formal framework | Deepest theoretical argument |

---

## Recommendation for the article

**Lead with Option C** as the conceptual model — it's the most novel and the argument that spec labor determines scope (not scale) is the distinctive contribution. The phrase "you can automate the search for the best restaurant; you cannot automate the fact that someone must want to eat" maps directly to "AI scales execution within varieties; spec labor determines how many varieties exist."

**Use Option B** for the quantitative framework — it's tractable, gives the labor-share-floor result cleanly (labor share → β > 0), and connects directly to the CES estimation literature (Oberfield & Raval, Katz-Murphy).

**Use Option A** only as a limiting case to illustrate the extreme: "if specification is truly Leontief with execution, then output is entirely bounded by spec labor regardless of AI capability."

### The key equation for the article

```
Y = L_spec^β · [α · K_AI^ρ + (1-α) · L_exec^ρ]^{(1-β)/ρ}

where ρ > 0 (σ_exec > 1: AI substitutes for execution labor)
and   β > 0 (specification labor share is a permanent floor)
```

As K_AI → ∞: total labor share → β. The economy doesn't run out of work; it runs out of specification capacity.
