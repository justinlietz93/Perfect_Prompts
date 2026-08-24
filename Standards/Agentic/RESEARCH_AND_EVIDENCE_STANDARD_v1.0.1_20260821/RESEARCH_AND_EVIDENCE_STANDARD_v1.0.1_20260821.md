# Research & Evidence Standard

**Version:** 1.0.1  
**Date:** 2026-08-21  
**Authority status:** WORKING STANDARD — candidate for canonical adoption  
**Scope:** Research conception, claim formation, evidence production, computational validation, provenance, review, closure, and handoff.  
**Relationship to existing assets:** This standard governs research behavior and evidence packages. The existing `ORCHESTRA_RESEARCH_PACKAGE_TEMPLATE_v2.0_20260804` is a concrete implementation of many of these rules, but implementation tooling does not outrank clarified semantic intent. The current blanket Markdown rejection in the Orchestra notebook validator is specifically recorded as out of conformance with the reviewer-facing notebook contract. The publication package and unified publication requirements are stronger downstream release standards, not substitutes for the research process.

---

## 0. Governing Principle

The objective of research is truth. The default posture is curiosity carried through to verification.

A new idea, claim, theory, derivation, dataset, model, or artifact is treated as living research. It is entered at its actual strength before it is reduced, translated, criticized, or normalized. Unfamiliarity, ambition, institutional distance, or unusual terminology are not evidence against a claim.

Curiosity does not lower rigor. Rigor is curiosity completed far enough that the work can be attacked where it actually lives: definitions, derivations, code, proofs, data, figures, controls, manifests, and reproducible artifacts.

The governing sequence is:

1. Enter the idea at full strength.
2. Reconstruct the complete intended claim and its dependency chain.
3. Identify the generative core and the objects it acts on.
4. Connect it to adjacent or conventional structures without importing unearned equivalence.
5. Build examples, counterexamples, toy models, and candidate formalizations.
6. Identify exact proof, symbolic, numerical, architectural, historical, or empirical burdens.
7. Declare falsifiers, thresholds, controls, and scope before decisive testing.
8. Build attackable evidence artifacts.
9. Inspect what survives, fails, remains unresolved, or becomes scope-limited.
10. Preserve the result and the path that produced it.

A failure must be localized. If a claim breaks, identify the exact equation, assumption, inference, definition, code path, dataset, missing bridge, or scope boundary where the break occurs. Local failure does not justify global dismissal unless the dependency chain makes it global.

---

## 1. Research Object and Whole-Claim Integrity

### 1.1 Reconstruct before evaluation

No claim may be evaluated from an isolated sentence when its meaning depends on definitions, earlier constraints, surrounding arguments, retained state, downstream use, or a named formal object.

Before accepting, rejecting, or formalizing a claim:

- identify its objects and types;
- recover its explicit and implicit quantifiers;
- recover its hypotheses and dependencies;
- determine what is definition, derivation, conjecture, analogy, computation, observation, or interpretation;
- test the interpretation against surrounding structure;
- identify any projection, abstraction, or information loss between the complete object and the observed representation.

If a local reading conflicts with established surrounding structure, treat the reading as incomplete until the conflict is resolved.

### 1.2 Preserve claim strength

Do not silently downgrade a bold claim into a safer nearby claim. Do not inflate a narrow claim into a universal one. A corrected or narrowed claim must be explicitly identified as a different claim or successor version.

### 1.3 No unearned imports

A familiar external concept may be used to illuminate a new object, but analogy does not grant equivalence. Imported terminology, structures, conservation laws, symmetries, topologies, causal relations, or mathematical properties must be earned by an explicit map, derivation, theorem, or measured correspondence.

---

## 2. Authority, Custody, and Source Control

### 2.1 Active semantic authority

Every nontrivial research package must identify the source or sources that control the meaning of the work. Authority must be explicit rather than inferred from file location, recency, convenience, or implementation state.

For each controlling source, record:

- authority ID;
- exact path or artifact identity;
- content hash when practical;
- scope of authority;
- why it controls;
- known exclusions.

### 2.2 Conflict rule

When sources conflict, do not silently reconcile them. Record the conflict and state which source controls for the affected question. If the conflict cannot yet be resolved, preserve it as an unresolved research condition.

### 2.3 Preserve controlling inputs

Controlling inputs are immutable evidence. Copy or snapshot them into the research package when required, hash them, and do not silently edit them in place. Derived or repaired versions must be distinct artifacts with lineage.

### 2.4 Separate authority from evidence and context

A source can be useful without being authoritative. Classify source roles where relevant as:

- **AUTHORITY** — controls meaning, requirements, or canonical state;
- **EVIDENCE** — supports or contradicts a claim;
- **REFERENCE** — provides concepts, methods, precedent, or comparison;
- **CONTEXT** — describes temporary or situational state;
- **EXCLUDED** — explicitly not controlling for the current work.

Implementation code is evidence of current behavior; it is not automatically architectural authority.

---

## 3. Research Package Identity and Branch Discipline

### 3.1 Every package has a question and a terminal condition

A research package must state:

- branch question;
- branch goal;
- exact terminal condition;
- active authority;
- scope and explicit exclusions;
- package identity and version;
- parent package or prior lineage when applicable.

Infrastructure work, intermediate repairs, partial lemmas, and negative controls are not terminal outcomes unless the terminal condition explicitly says they are.

### 3.2 Package identity is machine-readable

Directory names are for navigation. Machine-readable package metadata controls identity, lineage, version, roles, status, terminal condition, active authority, and supersession.

### 3.3 Closed work is immutable

Once a package is closed and hashed, do not rewrite it. Corrections, extensions, or reinterpretations create a successor package or version with explicit parent linkage.

---

## 4. Claim Architecture

### 4.1 Assign stable claim IDs before generating decisive evidence

Every load-bearing claim must receive a stable identifier before the decisive evidence is produced. Evidence must be able to point back to the exact claim it attacks.

### 4.2 Minimum claim record

Each claim record must contain:

- stable claim ID;
- exact claim text;
- claim or evidence class;
- hypotheses and quantifiers when applicable;
- scope;
- burden classification;
- decisive condition or metric;
- falsifier;
- dependencies;
- current status;
- supporting artifacts;
- contradicting artifacts;
- known projection or information-loss risks when relevant.

### 4.3 Claim classes

The CRAFT C0–C9 ontology may be used for review and extraction:

- C0 framing;
- C1 descriptive;
- C2 method;
- C3 derivational;
- C4 empirical;
- C5 causal/mechanistic;
- C6 generalization;
- C7 novelty;
- C8 significance;
- C9 falsifiability.

This ontology is a review aid. It does not replace the exact claim text or burden specification.

### 4.4 Evidence classes

Where the Orchestra evidence model is used, classify claims or inputs as:

- `RULE`;
- `CURRENT-CANON RESULT`;
- `RECOVERED`;
- `PROVISIONAL`;
- `CONDITIONAL DOWNSTREAM`.

### 4.5 Working statuses

Use explicit statuses rather than prose ambiguity:

- `UNTESTED`;
- `IN_PROGRESS`;
- `PASS`;
- `FAIL`;
- `BLOCKED`;
- `SUPERSEDED`;
- `NOT_APPLICABLE`.

`NOT_APPLICABLE` requires a scientific or structural reason. Missing tooling, inconvenience, or time pressure are not sufficient reasons when the burden actually exists.

### 4.6 Assumptions and nonclaims

Assumptions must be explicit and traceable to the claims that use them. Useful assumption types include inherited, local, regime-specific, computational, and unproved-required.

Exact nonclaims are used to prevent specific scope errors. They must not be scattered as generic defensive hedges. State them when they materially protect the claim boundary.

---

## 5. Burden Classification and Strongest-Available-Evidence Rule

A claim is not covered merely because some artifact mentions it. Each burden must be attacked by the strongest honest artifact type available for that burden.

### 5.1 Formal burden

Use formal proof for theorem-shape statements, exact equivalences, implication chains, impossibility statements, closure results, normal forms, exact reductions, and other discrete logical surfaces that can be represented honestly.

### 5.2 Symbolic burden

Use symbolic verification for algebraic, differential, projection, bracket, tensor, duality, operator, and closed-form identities. Symbolic computation is an adversarial check, not decorative algebra.

### 5.3 Numerical / computational burden

Use numerical or computational experiments for simulation claims, convergence, robustness, statistical behavior, geometry-facing consequences, thresholded gates, response diagnostics, finite examples, and executable consequences.

### 5.4 Empirical / observational burden

For claims grounded in measured or observed external data, preserve raw observations, acquisition conditions, preprocessing lineage, uncertainty, exclusions, and the exact mapping from observations to conclusions.

### 5.5 Architectural burden

For software, systems, or model architecture claims, inspect the actual implementation path, authoritative state, persistence model, failure atomicity, caches, fixed capacities, locality assumptions, and runtime behavior. Architecture cannot be established by documentation or unit tests alone when the executing system differs.

### 5.6 Figure burden

A figure may serve as reviewer-facing evidence, but it does not replace the derivation, dataset, computation, or proof that generated it.

### 5.7 Historical / source burden

For historical or literature claims, distinguish primary source, secondary synthesis, retrospective interpretation, and current reconstruction. Claims of novelty or priority require explicit prior-art comparison.

---

## 6. Experimental and Computational Method Standard

### 6.1 One claim or proof obligation per experiment unit

Every experiment or computational section must have one clearly identifiable claim, question, or proof obligation. Do not hide multiple independent claims behind one ambiguous output.

### 6.2 Declare the decision rule before execution

Before a decisive run, record:

- objective;
- exact claim attacked;
- method;
- inputs;
- parameters;
- seeds when stochastic;
- solver and tolerances;
- acceptance threshold;
- fail condition;
- negative control or adversarial case;
- expected output form.

Post-hoc threshold selection must be disclosed as exploratory rather than confirmatory.

### 6.3 Negative controls are mandatory when meaningful

A positive result is stronger when a deliberately broken or alternative construction fails as expected. Appropriate controls include:

- shuffles;
- broken constructions;
- wrong metrics;
- coordinate-breaking implementations;
- baseline models;
- null cases;
- stress conditions;
- removed hypotheses;
- adversarial parameter regimes.

### 6.4 Edge conditions and failure surfaces

Test meaningful boundaries, singular cases, limiting regimes, degenerate states, and known failure conditions. Do not report only the regime in which the implementation behaves well.

### 6.5 Finite evidence does not become an unbounded theorem

A finite sweep, prefix count, simulation run, numerical match, or sampled trace can support or falsify finite claims. It cannot by itself prove an all-depth, all-state, universal, asymptotic, or exact theorem.

### 6.6 Exact versus approximate arithmetic

Separate exact arithmetic from floating-point approximation. State precision, conditioning, numerical sensitivity, and residuals where they matter.

### 6.7 Reproduction record

A competent independent reviewer must be able to recover the run from the package. Record exact commands or procedures and all non-default choices that can change the result.

---

## 7. Notebook Standard — Paper Tutorial / “Tutorial Island”

### 7.1 Reviewer-facing purpose

The notebook is a **guided tutorial for the paper**, not a compressed audit log and not a machine-facing claim harness. Each paper should have a notebook that lets a technically competent reviewer walk through the argument in the same order the paper presents it, with lower cognitive density and stronger explanatory support.

The target experience is “tutorial island”: orient the reviewer, introduce each claim in plain technical prose, explain why it matters and what is about to be tested, then demonstrate the claim computationally with readable outputs and figures. The notebook should make the paper easier and more enjoyable to understand without weakening the evidence burden.

### 7.2 Paper-order walkthrough

Notebook structure must follow the paper rather than an implementation convenience order. For each substantive claim or proof unit, preserve the sequence in which the reader encounters it in the paper. A claim module should normally contain:

1. **Narrative exposition** — a Markdown cell stating the claim in accessible prose, locating it in the paper, naming the relevant objects and assumptions, and explaining what the following computation is intended to establish.
2. **Executable demonstration** — one coherent code cell per claim or claim-subsection whenever practical. It should implement the relevant test directly, with unusually clear comments that explain the reasoning as well as the mechanics.
3. **Readable evidence output** — concise numeric or textual results, a declared threshold or decision rule when applicable, and at least one informative figure when a visual representation materially helps understanding.
4. **Scoped conclusion** — an explicit `PASS` / `FAIL`, established / unsupported, or equivalent verdict whose wording matches the actual burden.
5. **Companion-evidence bridge** — where Lean 4, SymPy, source code, data files, derivations, or other package artifacts carry part of the burden, the notebook explains what they contribute and identifies the relevant artifact rather than forcing the reviewer to infer the connection.

The notebook may begin with a short orientation section explaining the paper's objective, the notebook's route through the paper, prerequisites, and how to interpret its evidence.

### 7.3 Computational-cell contract

Narrative cells are expected. The executable evidence cells retain the strict computational discipline:

- no runtime file I/O unless an explicitly approved notebook mode requires it;
- no network dependence;
- no infrastructure-only executable cells;
- each executable claim cell states or makes explicit its acceptance criterion where the claim admits one;
- each claim demonstration includes a negative control or adversarial case when one is meaningful;
- each demonstration emits concrete numeric and/or human-readable results rather than opaque logs;
- each demonstration uses figures when visualization helps the reviewer see the mechanism or decision boundary;
- each demonstration ends with an explicit scoped verdict;
- strict closure requires the relevant cells to be executed and their outputs rendered;
- matching decision figures are exported separately into the package-level `figures/` directory by code outside the notebook when the package requires standalone figure artifacts.

Notebook state must not be the sole copy of decisive evidence.

### 7.4 Prose and code-quality requirement

Reviewer accessibility is part of notebook correctness. Dense code, unexplained notation, unexplained arrays, giant dumps, cryptic variable names, or walls of machine-readable output are defects even when the computation itself is correct.

Comments should explain the causal or mathematical purpose of important steps, not merely restate syntax. Markdown should explain the idea before the code forces the reviewer to reverse-engineer it. Outputs should be curated so that the reviewer can see *why* the result supports or falsifies the claim.

The notebook is therefore intentionally redundant with parts of the paper and package: its job is to **teach the argument through executable evidence**.

### 7.5 Current Orchestra validator contradiction is an implementation defect

`CRAFT_BASS_Review_Standards_v3.md` rewards narrative Markdown and reviewer-friendly notebook exposition. That is aligned with the intended notebook design described above. The current `ORCHESTRA_RESEARCH_PACKAGE_TEMPLATE_v2.0_20260804/tools/validate_package.py` instead rejects every Markdown cell, while `notebooks/README.md` frames notebooks as reviewer artifacts.

The Markdown rejection is **not the controlling semantic rule**. It is a drifted validator constraint that contradicts the intended reviewer-facing notebook contract. It must not be used to strip explanatory prose from notebooks merely to obtain validator success.

Required remediation for the Orchestra template:

- allow Markdown cells;
- distinguish narrative Markdown from prohibited infrastructure-only executable cells;
- preserve validation of claim evidence cells for thresholds, controls, outputs, figures, execution state, and scoped verdicts;
- permit or require claim identifiers in notebook metadata so narrative and executable cells can be associated with the same claim;
- validate paper/claim ordering where the package exposes that order;
- never treat reviewer-facing explanation as a validation defect.

Until the template validator is repaired, a tutorial-style notebook may be semantically conformant to this standard while failing the old Orchestra validator. That failure identifies the validator as out of conformance with the standard, not the notebook.

### 7.6 Notebook results remain scoped

A computational `PASS` means the declared implementation-level or finite test passed under the stated inputs, assumptions, and thresholds. It is not permission to promote the result into a universal theorem without the corresponding analytical or formal bridge. Conversely, when a theorem is carried by Lean 4 or another proof artifact, the notebook should explain the theorem and show the reviewer how that formal result connects to the paper claim rather than replacing the proof with a plot.

---

## 8. Formal Verification Standard

### 8.1 Formalize where a real formal burden exists

Use Lean 4 or another proof assistant when the claim has an honest theorem surface. Do not create cosmetic proof scaffolds whose trivial theorem is weaker than the paper or research claim.

### 8.2 The proof must match the claim

Formalization may not obtain tractability by silently:

- weakening quantifiers;
- shrinking the domain;
- converting a derived result into an axiom;
- assuming the conclusion;
- replacing the complete object with an easier projection;
- importing a theorem whose hypotheses are not established.

Any necessary formal simplification must be declared and its relationship to the original claim classified.

### 8.3 Reproducible formal artifact

A formal package must record:

- toolchain/version;
- dependencies;
- exact build command;
- theorem inventory or mapped theorem surface;
- build status;
- commit or artifact identity when used for publication or certification.

A clean build establishes only the encoded theorem surface. It does not establish that the encoding faithfully captures an external scientific claim unless that bridge is separately justified.

---

## 9. Symbolic Verification Standard

Symbolic tools such as SymPy are used to attack identities, not to decorate derivations.

For every nontrivial symbolic burden:

- state the identity and domain;
- expose assumptions such as commutativity, nonzero denominators, branch choices, and parameter restrictions;
- compute or simplify both sides independently where practical;
- report the residual or exact equality result;
- test singular and removed-hypothesis cases when meaningful;
- preserve the runnable script or exact notebook unit;
- classify the result as local symbolic evidence, not automatically as a global theorem.

---

## 10. Data, Code, and Provenance Standard

### 10.1 Full lineage

Evidence must be traceable from source inputs to reported findings. A source map should identify:

- claim ID;
- output artifact;
- generating code or method;
- inputs;
- parameters;
- command;
- hash.

### 10.2 No hidden dependencies

Research artifacts may not depend on unpublished local files, secret preprocessing steps, undocumented services, or inaccessible external data without explicit disclosure and classification.

### 10.3 Raw to processed separation

Where raw data exists, preserve it separately from processed data. Derived data must identify the transformation that created it.

### 10.4 Environment and versions

Record exact software versions, important library versions, environment definitions, hardware constraints when material, seeds, and numerical solver configuration.

### 10.5 Code as evidence, not authority

Executable code establishes what the implementation does. It does not by itself establish that the behavior is mathematically correct, architecturally intended, or semantically equivalent to a theory.

---

## 11. Figure and Visualization Standard

Figures are arguments, not decoration.

The priority order is:

1. accuracy;
2. clarity;
3. aesthetics.

Each decision figure must communicate one principal message. If two independent messages are required, split the figure.

Required rules:

- use data-appropriate palette classes;
- preserve perceptual ordering;
- avoid rainbow/jet quantitative maps without a compelling explicit reason;
- use color economically;
- label units, transformations, panels, and variables;
- avoid deceptive axes, arbitrary 3D effects, inconsistent scales, and hidden missing data;
- distinguish conceptual diagrams, hypotheses, simulations, and measurements visually;
- do not let aesthetic certainty exceed epistemic certainty;
- design at target publication dimensions;
- write captions that make the figure interpretable without guessing;
- archive the figure as an individual top-level evidence file when it participates in a package decision.

Every figure should be reproducible from recorded inputs and generating code or method.

---

## 12. Findings, Negative Results, and Research Memory

### 12.1 Preserve all outcome classes

Research findings must distinguish:

- positive findings;
- negative findings;
- unresolved findings;
- falsified claims or branches;
- blocked work;
- interpretation and speculation.

Negative and unresolved results remain visible. Do not erase them because the branch later succeeds.

### 12.2 Append-only lab journal

The lab journal is chronological research memory. Old entries are not rewritten to match later conclusions.

Each material entry should record:

- objective;
- inputs and authority;
- exact change or method;
- command or procedure;
- observed result;
- negative control;
- decision;
- next action;
- files created or modified.

Corrections are new entries that point back to the earlier record.

---

## 13. Review and Adjudication

### 13.1 Reviewers inspect; they do not silently rewrite

A reviewer, validator, guardian, or auditor may identify defects, request changes, or issue a verdict. They must not rewrite the evidence they are adjudicating and then validate the rewritten version as though it were the original evidence.

### 13.2 Separate research work from adjudication

The Orchestra Operator / Guardian / Auditor role model is the current concrete implementation:

- Operator performs work in the active version;
- Guardian records same-version rule adjudication;
- Auditor closes adjudication and controls successor-version advancement.

Other workflows may use different names, but must preserve custody separation between producing evidence and independently adjudicating it when independent review is claimed.

### 13.3 Adversarial review must be specific

A useful review identifies:

- exact claim;
- exact failure or risk;
- evidence inspected;
- missing assumption or bridge;
- counterexample or falsifier when available;
- required repair.

Generic unease, prestige signaling, or social caution are not substitutes for technical review.

### 13.4 CRAFT/BASS is diagnostic, not authority

CRAFT/BASS can score claim support, handwaving, falsifiability, terminology, assumptions, traceability, reproducibility, and reviewer-friendliness. Its scores are diagnostic summaries. They do not override the underlying claim/evidence record.

---

## 14. Closure, Versioning, and Integrity

### 14.1 Terminal outcomes

A research branch closes only when its declared terminal condition is satisfied. Normal terminal outcomes include:

- a nontrivial positive internally generated result;
- a proof or decisive demonstration that the branch hypothesis is false;
- an exact external dependency that blocks further work, recorded as `BLOCKED` rather than `PASS`.

The research process may legitimately preserve unresolved questions. Publication closure is a separate, stronger gate.

### 14.2 Manifest and hashes

A closed package must generate its manifest from final bytes rather than hand-maintaining it. The manifest and `SHA256SUMS` must agree with actual package contents.

### 14.3 No placeholder closure

Strict closure requires:

- no active placeholder markers;
- declared branch goal;
- declared terminal condition;
- nonempty active authority;
- stable claim records;
- required decision evidence;
- valid manifest and hashes;
- all required artifacts present and runnable.

### 14.4 Preserve the closed package

A closed package is immutable evidence. Preserve the archive and external checksum together. Any change creates a successor version.

---

## 15. Research-to-Publication Boundary

Research packages and publication packages have different jobs.

### Research package

A research package may contain:

- provisional claims;
- failed claims;
- unresolved findings;
- active alternatives;
- partial formalization;
- experimental branches;
- blocked dependencies.

Its job is to preserve an honest, reproducible path through the research question.

### Publication package

A publication package is a downstream release object. The existing publication standard requires the paper itself to carry the load-bearing claims and derivations, with formal, symbolic, numerical, figure, reproducibility, and release burdens mapped to appropriate artifacts.

Audit language such as `PASS/FAIL`, gate ledgers, internal file paths, and package machinery belongs in the evidence/review layer unless the scientific argument genuinely requires it. The reviewer checklist correctly distinguishes paper presentation from technical audit machinery.

Do not force active-research mechanics into the prose of the final paper merely because they are essential inside the research package.

---

## 16. Concept Transfer Standard

When conventional mathematics, physics, computer science, neuroscience, or another external domain is used to interpret a new research object, create a concept-transfer record containing:

- conventional concept;
- source and section;
- exact definition;
- standard theorem;
- required hypotheses;
- worked example;
- counterexample when a hypothesis is removed;
- candidate counterpart in the active research system;
- exact relationship classification;
- map or readout required;
- falsification target;
- computational test;
- proof obligation.

Allowed relationship classes include:

- exact;
- proved special case;
- conjectural;
- structural analogy;
- visual resemblance only.

Do not collapse these categories.

---

## 17. Anti-Patterns and Automatic Failures

The following practices violate this standard unless an explicit scoped exception is justified:

- evaluating a reduced version of the claim instead of the whole claim;
- silent reconciliation of conflicting authorities;
- rewriting canonical evidence during review;
- converting a derived result into an assumption;
- hiding a missing bridge inside terminology;
- treating implementation behavior as architectural authority;
- treating a numerical match as a universal proof;
- treating a figure as the evidence source rather than a view of evidence;
- omitting negative or falsified findings;
- selecting thresholds after observing the decisive result without disclosure;
- using hidden files or undocumented preprocessing;
- formalizing a weakened theorem and presenting it as the original claim;
- creating cosmetic Lean, symbolic, or notebook artifacts solely to claim coverage;
- hand-maintaining a release manifest that is supposed to certify final bytes;
- modifying a closed evidence archive rather than creating a successor;
- treating `BLOCKED` as `PASS`;
- using generic caution, prestige, institutional familiarity, or social plausibility as evidence;
- allowing validation tooling to redefine the scientific claim it is meant to test.

---

## 18. Compact Operating Checklist

Before decisive research work:

- [ ] Whole claim reconstructed.
- [ ] Active semantic authority identified.
- [ ] Conflicting sources recorded rather than silently reconciled.
- [ ] Branch question and terminal condition declared.
- [ ] Stable claim IDs assigned.
- [ ] Assumptions, scope, dependencies, and falsifiers explicit.
- [ ] Burden class assigned to each claim.
- [ ] Thresholds and controls declared before decisive execution.

For every evidence artifact:

- [ ] Exact claim attacked is identifiable.
- [ ] Inputs and parameters are recoverable.
- [ ] Negative/adversarial control exists where meaningful.
- [ ] Edge and failure conditions are tested where meaningful.
- [ ] Result is classified locally without scope inflation.
- [ ] Artifact provenance is recorded.

Before package closure:

- [ ] Positive, negative, unresolved, falsified, and blocked results are preserved.
- [ ] Lab history has not been rewritten.
- [ ] Review is custody-separated from evidence production when independent adjudication is claimed.
- [ ] Manifest and hashes match final bytes.
- [ ] Terminal condition is actually satisfied.
- [ ] Closed package is frozen and successor rules are explicit.

---

## 19. Source Authority and Lineage

This v1.0.1 standard was synthesized from the user-supplied standards, templates, curriculum research-method material, and explicit clarification of intended behavior. It does not silently supersede source authority.

**Semantic authority outranks validator accident.** A validator, generator, schema, or template utility is an implementation of the standard, not an independent source of meaning. When implementation tooling contradicts an explicit governing requirement or clarified design intent, record the mismatch and repair the tooling. Do not promote the implementation defect into a new standard merely because it is executable.

For the notebook contract specifically, the explicit reviewer-facing “tutorial island” intent controls the semantic requirement. The current Orchestra Markdown rejection is therefore a known implementation defect.

### Primary controlling source family

1. `Templates.zip / ORCHESTRA_RESEARCH_PACKAGE_TEMPLATE_v2.0_20260804/`
   - `README.md`
   - `AUTHORITY.md`
   - `WORKFLOW.md`
   - `CLAIMS.md`
   - `FINDINGS.md`
   - `LAB_JOURNAL.md`
   - `HANDOFF.md`
   - `source_maps/SOURCE_MAP_TEMPLATE.md`
   - `docs/METHODS_TEMPLATE.md`
   - `docs/RESULTS_TEMPLATE.md`
   - `notebooks/README.md`
   - `lean/README.md`
   - `schemas/*.json`
   - `tools/validate_package.py`

2. `Templates.zip / ORCHESTRA_PUBLICATION_PACKAGE_TEMPLATE_v2.0_20260804/`
   - `PUBLICATION_REQUIREMENTS.md`
   - `claims/CLAIM_LEDGER.md`
   - `claims/ASSUMPTION_LEDGER.md`
   - `claims/NONCLAIMS.md`
   - `validation/COVERAGE_MAP.md`

### Existing standards incorporated

3. `Standards.zip / vdm_research_standards/Paper_Requirements/unified_publication_requirements_v3.md`
   - curiosity-first posture;
   - burden model;
   - formal/symbolic/numerical attack;
   - figure integrity;
   - reproducibility and release requirements.

4. `Standards.zip / Reviewer_Checklist/Reviewer_Checklist.md`
   - separation of paper presentation from deep technical audit;
   - theorem, numerical, symbolic, exactness, and reproducibility checks.

5. `Standards.zip / vdm_research_standards/Paper_Requirements/CRAFT_BASS_Review_Standards_v3.md`
   - claim ontology;
   - assumption/dependency/scope audit;
   - reproducibility and review diagnostics.

6. `Standards.zip / vdm_research_standards/Lean4_Workflow.md`
   - mechanically verified theorem surfaces;
   - reproducible toolchain, CI, commit, and publication linkage.

7. `Standards.zip / curiosity_first_research_note.txt`
   - generative contact before reflexive reduction;
   - artifact-level attack rather than posture-level skepticism.

### Curriculum research-method lineage

The Phase Calculus / VDM curriculum also contains aligned research-method templates for claim audit, concept transfer, computational experiment discipline, negative controls, proof/evidence separation, and exact relationship classification. Those rules are consistent with the standard above and remain useful specialized implementations.

---

## 20. Adoption Rule

This document becomes canonical only by explicit adoption into the standards library or by another authority mechanism chosen by the user. Until then, it is a working synthesis intended to consolidate the already-existing research standard without rewriting or erasing its sources.
