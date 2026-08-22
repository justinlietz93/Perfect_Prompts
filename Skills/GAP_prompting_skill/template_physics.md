# GAP Template — Physics / Theoretical / Formal Methods

Use this template when the constraints are mathematical axioms, formal derivation
rules, physical laws, or theoretical frameworks. The vocabulary matters — naming
specific formalisms creates stronger attention anchoring in the target agent.

---

## Template

```
I was thinking about why we keep running into issues with **[Current Bug/Friction
Point]**, and I want to get your thoughts on the theoretical architecture here.

Based on our formal rules for **[Insert Core Axiom/Formalism Name]**, we know
that **[State the hard mathematical or logical constraint]**.

If that is the case, wouldn't it make sense that **[The specific problematic
variable/function/derivation step]** is actually a representation of **[Theory A]**,
while our standard baseline represents **[Theory B]**?

If you agree with this theoretical split, how should we architect the Python
codebase to ensure these two systems are processed independently, so we don't
accidentally violate **[Core Axiom]**?
```

---

## Slot Definitions

| Slot | What goes here | Good example | Bad example |
|------|---------------|--------------|-------------|
| **Current Bug/Friction Point** | The specific symptom you're seeing | "the Fisher-KPP prediction drifts at high k" | "it's broken" |
| **Core Axiom/Formalism Name** | The named formal rule — use its actual name | "S1 Metriplectic Split" | "the math rules" |
| **Hard constraint** | The mathematical statement, ideally in notation | "H and S must decompose orthogonally" | "things should be separate" |
| **Problematic element** | The specific code object or derivation step | "the `compute_dispersion()` return value" | "the output" |
| **Theory A / Theory B** | The two sides of the formal split | "dissipative sector / Hamiltonian sector" | "part 1 / part 2" |

---

## Worked Example (VDM Context)

```
I was thinking about why the dispersion relation keeps picking up a spurious
imaginary component at high wavenumber, and I want to get your thoughts on
the theoretical architecture here.

Based on the S1 Metriplectic Split formalism, we know that the Hamiltonian
flow (energy-conserving) and the gradient flow (entropy-producing) must
decompose orthogonally — they cannot mix operators.

If that is the case, wouldn't it make sense that the `thermal_damping` term
in `compute_dispersion()` is actually a pure gradient-flow quantity that got
accidentally folded into the Hamiltonian propagator, contaminating the
energy-conserving sector with dissipation?

If you agree with this theoretical split, how should we architect the
dispersion module so that Hamiltonian and gradient-flow contributions are
computed by strictly separate operator pipelines, and only combined at the
final observable level?
```

---

## Domain-Specific Tips

- **Name your formalisms.** "Metriplectic split" is better than "energy-entropy
  decomposition" because it's a unique search key in the agent's attention.
- **Use notation where possible.** LaTeX or symbolic expressions in the constraint
  statement create stronger anchoring than prose descriptions.
- **Specify the level of mathematical rigor.** If the constraint is a theorem,
  say "theorem." If it's a conjecture you're treating as axiomatic for this
  codebase, say that too. The agent needs to know the epistemic status.
- **Reference your documents by name.** If you have a CF document or formal
  spec, name it. "Per CF000 Section 3.2" is a powerful constraint anchor.
