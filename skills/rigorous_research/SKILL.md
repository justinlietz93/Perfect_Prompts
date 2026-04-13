---
name: vdm-publication-bundle
description: >
  Generate, audit, and validate complete VDM research bundles following theorem-bearing manuscript standards. Use this skill when the user wants to: create a research bundle, Lean4 package from formal claims, SymPy adversarial symbolic audit script, a skeptical-reviewer Jupyter notebook, score papers w/ CRAFT/BASS review metrics, audit burden coverage, generate SHA256 manifests, create figures following standards, scaffold a new Complete Formalism publication from claims, or check whether existing bundles meet certificate requirements. Also trigger when the user mentions "publication bundle","validation bundle","CRAFT score","BASS score","burden coverage","claim attack","gate check","reviewer notebook","adversarial audit","publication certificate","closure certificate","artifact manifest", "figure standards", "review-ready", or any CF/CFN publication workflow. Even if the user just says "score this paper"/"check if this is publication-ready", use this skill.
---

# VDM Publication Bundle Skill

## Purpose

This skill operationalizes the full VDM publication validation pipeline. It takes a
formalism (paper, claims, derivations) and produces or audits a complete validation bundle
where every load-bearing claim is attacked by the strongest available artifact type.

The governing rule: **no claim may be treated as "covered" merely because it appears in one
artifact.** Coverage is complete only when each burden is attacked by the strongest artifact
type available for that burden.

## Architecture

The bundle has six required layers:

| Layer | Role | Strongest-for |
|-------|------|---------------|
| **Paper** | Carries the full load-bearing formal burden | Ontological / theorem-bearing |
| **Lean4** | Proves every exact formalizable statement | Logical / formal |
| **SymPy** | Attacks every symbolic identity and operator law | Algebraic / symbolic |
| **Jupyter** | Attacks every numerical/geometric/statistical consequence | Empirical / executable |
| **README** | Maps burdens to artifacts with run instructions | Operationalization |
| **SHA256SUMS** | Integrity-checks every artifact | Auditability |

## Workflow

When the user invokes this skill, determine which phase they're in:

### Phase 1: Claim Extraction
Read the paper or formalism. Extract every load-bearing claim, classify by burden type
(§4 of `references/paper_requirements.md`), and produce a claims register.

### Phase 2: Burden Assignment
For each claim, assign it to the strongest artifact type. Use the burden model:
- Ontological → Paper (definitions, theorem statements, derivation chains, scope)
- Logical → Lean4 (exact theorem-shape, equivalences, impossibilities)
- Algebraic → SymPy (closed-form identities, operator laws, bracket formulas)
- Empirical → Jupyter (numerical gates, Monte Carlo, robustness sweeps)

### Phase 3: Artifact Generation
Generate each artifact following its specific standard. Read the relevant reference
file BEFORE generating:

- **Lean4 package** → Read `references/lean_template.md` first
- **SymPy script** → Read `references/sympy_standard.md` first
- **Jupyter notebook** → Read `references/notebook_template.md` first
- **Figures** → Read `references/figure_standards.md` first
- **README / SHA256** → Read `references/bundle_manifest.md` first

### Phase 4: Coverage Audit
Run the coverage auditor to verify every burden is attacked:
```bash
python scripts/coverage_auditor.py --claims CLAIMS.md --manifest ARTIFACT_MANIFEST.md
```

### Phase 5: CRAFT/BASS Scoring
Score the bundle using CRAFT/BASS:
```bash
python scripts/craft_bass_scorer.py --paper <paper_path> --bundle <bundle_dir>
```

### Phase 6: Closure Certificate
Generate the closure certificate only after all burdens are resolved. Every claim must
end in exactly one bucket: proved, falsified, restricted, deferred, or unresolved.

## Reference Files

Read these BEFORE generating any artifact. Each contains the exact standard.

| Reference | When to read | What it governs |
|-----------|-------------|-----------------|
| `references/paper_requirements.md` | Always first | Full burden model, all artifact requirements |
| `references/lean_template.md` | Before any Lean4 work | Package structure, axiom audit, reviewer files |
| `references/notebook_template.md` | Before any Jupyter work | Dual-markdown structure, claim attack template |
| `references/figure_standards.md` | Before any figure | Palette, composition, honesty, anti-deception |
| `references/craft_bass_standards.md` | Before scoring | Claim ontology, BASS formula, verdict bands |
| `references/sympy_standard.md` | Before SymPy work | Adversarial audit rules, pass/fail closure |
| `references/bundle_manifest.md` | Before README/SHA256 | Coverage map, hash requirements, certificate |

## Critical Rules

1. **No cosmetic companions.** Lean4 must prove real theorem-shape statements, not trivial
   examples while the hard burden lives elsewhere. SymPy must be an adversarial audit, not
   illustrative algebra. Jupyter must attack claims, not display dashboards.

2. **No hidden assumptions.** Every step delegated from the paper must be explicitly tagged
   with what is being delegated and why. "Standard argument", "it is well known", and
   "follows similarly" are forbidden without exact specification.

3. **No validation by assertion.** A claim is validated only when it is attacked by the
   strongest artifact type and survives. Appearance in an artifact is not coverage.

4. **Dual-markdown structure.** Every non-title markdown cell in the Jupyter notebook must
   have two ordered sections: (1) Friendly orientation — plain language setup, (2) Mechanical
   review contract — exact burden, constraints, and failure conditions.

5. **Figures follow the Constitution.** Every figure must communicate exactly one message.
   Palette must match data classification. No rainbow on quantitative data. No fill patterns.
   Sizes scale to area, not radius. Canvas set to target dimensions from the start.

6. **Explicit pass/fail.** SymPy must end in `FINAL_RESULT: PASS` or `FINAL_RESULT: FAIL`
   and exit nonzero on failure. Every Jupyter gate must call `terminal_log()` and
   `append_gate()` with explicit metrics, thresholds, and verdict.

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/coverage_auditor.py` | Check burden-to-artifact coverage | `python scripts/coverage_auditor.py --claims CLAIMS.md` |
| `scripts/craft_bass_scorer.py` | Compute CRAFT/BASS composite score | `python scripts/craft_bass_scorer.py --input scores.json` |
| `scripts/sha256_manifest.py` | Generate SHA256SUMS for all artifacts | `python scripts/sha256_manifest.py --bundle-dir .` |
| `scripts/scaffold_bundle.py` | Scaffold a new empty bundle from claims | `python scripts/scaffold_bundle.py --paper-id CFXX --claims claims.json` |

## Output Structure

A complete bundle looks like:

```
CFXX-bundle/
├── paper/
│   └── CFXX_paper.pdf (or .md/.tex)
├── lean4/
│   ├── lakefile.lean
│   ├── lean-toolchain
│   ├── lake-manifest.json
│   ├── CFXXLib/
│   │   └── Basic.lean
│   ├── CFXXLibTest/
│   │   └── Smoke.lean
│   ├── Audit/
│   │   ├── AxiomAudit.lean
│   │   └── flagship-theorems.txt
│   ├── scripts/
│   │   ├── audit_axioms.sh
│   │   └── recompute_sha256.py
│   ├── REVIEW.md
│   ├── CLAIMS.md
│   ├── CLOSURE_CERTIFICATE.md
│   └── ARTIFACT_MANIFEST.md
├── sympy/
│   └── CFXX_symbolic_audit.py
├── notebooks/
│   └── CFNXX_skeptical_reviewer.ipynb
├── README.md
└── SHA256SUMS
```

## Forbidden Failure Modes

- Paper that is front matter only (no derivations, no gates, no falsifiers)
- Lean4 that formalizes only trivial claims while real theorems stay outside
- SymPy that illustrates algebra without adversarial attack
- Jupyter that depends on hidden CSVs or external manifests at runtime
- Notebook that opens with internal audit gates (T0, T1, T2) instead of science
- README without run instructions or coverage map
- Missing SHA256SUMS
- Any claim treated as validated without being attacked

## Bundle Completeness Checklist

Before declaring a bundle complete, verify:

- [ ] Every load-bearing claim explicitly identified
- [ ] Every exact formalizable statement in Lean4 (or classified with reason)
- [ ] Every symbolic identity/operator law in SymPy
- [ ] Every numerical/geometric/statistical consequence in Jupyter
- [ ] Every artifact runnable from README instructions
- [ ] Every artifact hash-listed in SHA256SUMS
- [ ] Coverage map shows no unclassified burden
- [ ] Every unresolved item explicitly marked (not silently omitted)
- [ ] Closure certificate generated with all claims in exactly one bucket
