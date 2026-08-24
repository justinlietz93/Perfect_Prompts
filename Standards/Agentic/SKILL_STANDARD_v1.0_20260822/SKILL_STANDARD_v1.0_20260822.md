# Skill Standard

**Version:** 1.0.0  
**Date:** 2026-08-22  
**Authority status:** CANONICAL CANDIDATE — intended for adoption into `Standards/`  
**Scope:** Evergreen requirements for reusable LLM/agent skill packages: identity, activation, package anatomy, procedural contract, runtime interface, artifacts, validation, portability, lifecycle, and provenance.  
**Out of scope:** The domain-specific reasoning or task method inside any one skill; generic prompt-template requirements already governed by the Prompt Template Standard; transient project state; user profiles.

---

## 0. Governing Principle

> **A skill is a procedural package, not merely a long prompt.**

A canonical skill packages a reusable capability. It may contain instructions, reference material, schemas, scripts, validators, assets, runtime bindings, example invocations, and explicit output contracts.

The standard exists so that skills remain:

- semantically clear;
- composable with prompts, standards, methodologies, and agent instructions;
- portable across runtimes;
- auditable and testable;
- small enough to use, but rich enough to actually carry the capability.

A skill is successful when a future agent can activate it, understand its boundaries, locate its supporting artifacts, execute its workflow, and determine completion without reverse-engineering the package.

---

## 1. Skill Boundary

### 1.1 What a skill is

A skill is a reusable **capability package** for a defined class of work.

Typical examples from the evidence base include:

- prompt-construction assistance (`GAP_prompting_skill`);
- session preservation (`session_handoff_skill`);
- rigorous end-to-end data analysis (`comprehensive-data-analysis`);
- PDF work where rendering/layout matter (`pdf`);
- structured publication/research packaging (`rigorous_research`);
- downstream-agent relay behavior (`audit-and-instruct`);
- repository-level build orchestration (`repository-build-orchestrator`).

### 1.2 What a skill is not

A skill is not automatically any of the following:

- a persona;
- a methodology;
- a ruleset;
- a prompt template;
- an AGENTS policy file;
- a one-off project instruction set;
- a bare zip of random utilities.

A skill may contain or reference those artifacts, but it remains a separate class whose job is to package a reusable procedure.

### 1.3 Skill versus prompt template

A prompt template primarily standardizes an instruction contract for a task class.

A skill may include a prompt or prompt fragments, but it additionally packages the surrounding procedural machinery:

- where supporting references live;
- what scripts or validators must run;
- what files/artifacts get produced;
- how completion is judged;
- how the capability is surfaced in one or more runtimes.

If the capability disappears when the prompt text is separated from its surrounding artifacts, it was functioning as a skill, not merely a template.

---

## 2. Position in the Canonical Repository

### 2.1 Skills are neither Standards nor Profiles

- **Standards** govern evergreen rules.
- **Templates** provide specialized instruction instruments.
- **Profiles** capture evolving descriptive material.
- **Skills** package reusable operational capabilities.

A skill can depend on a standard and can internally use templates, but it should not be filed as a standard merely because it is important.

### 2.2 Skills are allowed to vary internally

Different skills may have incompatible workflows because their jobs differ.

For example:

- a session-handoff skill must preserve latent context and rejected paths;
- a PDF skill must care about layout rendering and environment dependencies;
- a research-publication skill must manage claims, burden assignment, and evidence packages;
- a data-analysis skill may require staged attempts, figures, and reproducibility.

The standard does **not** force a single universal skill workflow.

### 2.3 The narrowest valid instrument wins

If a task can be handled by a narrow skill, do not invoke a broader generic skill that imposes unrelated machinery.

---

## 3. Required Identity Contract

Every canonical skill package must declare a stable identity independent of filename.

Required identity fields:

- **Skill ID** — stable machine-friendly identifier;
- **Title** — human-readable name;
- **Version** — explicit version;
- **Status** — `DRAFT`, `CANDIDATE`, `CANONICAL`, `DEPRECATED`, or `ARCHIVED`;
- **Purpose** — what capability the skill provides;
- **Capability scope** — the semantic boundary of the skill;
- **Primary entry artifact** — usually `SKILL.md` or equivalent canonical entrypoint.

Recommended additional fields:

- `use_when`;
- `do_not_use_when`;
- `activation_triggers`;
- `required_inputs`;
- `optional_inputs`;
- `supporting_artifacts`;
- `output_contract`;
- `validation_contract`;
- `runtime_bindings`;
- `dependency_contract`;
- `source_lineage`;
- `supersedes`.

A top-level directory or zip name alone is not sufficient identity.

---

## 4. Activation Contract

Every skill must clearly state how and when it should activate.

### 4.1 Use-when contract

Describe the semantic job the skill covers.

Good:

- use when the task is to preserve current session state for later zero-loss resumption;
- use when PDF layout or rendering materially affects correctness;
- use when the user needs help constructing a Guided Autonomy prompt;
- use when a dataset must be analyzed end-to-end with reproducible outputs.

Avoid vague declarations like “use for advanced tasks.”

### 4.2 Do-not-use-when contract

Every skill must declare boundaries.

Examples:

- do not use a handoff skill to continue the project work itself;
- do not use a PDF skill for plain-text file handling where layout is irrelevant;
- do not use a research-bundle skill as a substitute for casual brainstorming;
- do not use a data-analysis skill when the user only asked for a single quick statistic.

### 4.3 Trigger vocabulary is supportive, not authoritative

Phrase lists help activation, but the semantic task outranks keyword matching.

A skill should not activate merely because one trigger word appeared out of context.

### 4.4 Multi-mode skills must name their modes

If one skill can operate in distinct modes, the package must declare:

- mode names;
- what selects each mode;
- what differs between modes;
- whether modes share artifacts or produce different outputs.

The GAP skill is the key evidence for this requirement.

---

## 5. Package Anatomy

A canonical skill package must expose its structure so a future agent can navigate it without guesswork.

### 5.1 Canonical entrypoint

A skill should have one controlling entry artifact, normally `SKILL.md`.

That entry artifact must tell the agent:

- what the skill is for;
- when to use it;
- what references/scripts/assets exist;
- what procedure to follow;
- what to produce;
- what quality gates apply.

### 5.2 Recommended package layout

Not every skill needs every subdirectory, but when present they should be semantically clean:

```text
skill-name/
├── SKILL.md                  # canonical entrypoint
├── references/              # domain references, schemas, examples, theory
├── scripts/                 # helper scripts, validators, renderers, tooling
├── schemas/                 # machine-readable contracts
├── assets/                  # icons, diagrams, supporting media
├── agents/                  # runtime-specific UI/binding metadata
├── examples/                # example inputs/outputs
├── tests/                   # fixtures or smoke tests when warranted
└── outputs/                 # only when the skill explicitly produces a durable package
```

### 5.3 Flat files are allowed when the skill is genuinely small

A small skill may be a single Markdown file plus minimal runtime metadata if that fully expresses the capability.

Smallness is acceptable. Hidden structure is not.

### 5.4 Zipped runtime bundles are not canonical source

Binary `.skill` or `.zip` distributions are permitted as delivery forms, but the canonical source must remain inspectable as plain files.

---

## 6. Procedural Contract

A skill must expose the procedure it expects the agent to follow.

### 6.1 Name the steps or phases

The procedure can be short or long, but it must be externally visible.

Examples from the evidence base:

- Session Handoff: classify session -> extract signals -> liminal analysis -> generate package -> quality gates.
- Rigorous Research: claim extraction -> burden assignment -> artifact generation -> coverage audit -> scoring -> closure certificate.
- Comprehensive Data Analysis: problem understanding -> research -> implementation attempts -> package assembly.

### 6.2 Declare required reads and artifact lookups

If the skill depends on a reference file, schema, or script, the entrypoint must tell the agent to read it.

Do not hide critical logic in a side file that the entrypoint never mentions.

### 6.3 Externalize support logic when it improves reuse

Repeated logic, schemas, rendering utilities, validators, and example structures should live in supporting files rather than bloating the entry prompt.

### 6.4 Keep the procedure load-bearing

A procedural section must not degenerate into motivational prose. It should allow another agent to actually perform the work.

---

## 7. Artifact and Output Contract

### 7.1 Every skill must define what it produces

Outputs may include:

- a structured handoff package;
- a research/publication bundle;
- a set of figures and analysis files;
- a generated prompt;
- a transformed PDF;
- a relay instruction package;
- a repository plan and implementation state.

### 7.2 Multi-artifact outputs must be named

If the skill produces multiple files, it must describe the manifest.

The Session Handoff skill is the clearest evidence: it names every output file and what each one means.

### 7.3 Human-readable and machine-readable outputs may coexist

If both are needed, the skill should say so explicitly rather than assuming one output form can substitute for the other.

### 7.4 Output location conventions must be clear

If the skill expects an `outputs/` directory, temporary workspace, or package root, say so.

---

## 8. Validation and Quality Gates

A canonical skill must describe how correctness is judged.

### 8.1 Completion conditions must be explicit

A skill is complete when its own declared outputs and quality gates are satisfied, not merely when the agent stops talking.

### 8.2 Validation can be textual, procedural, or executable

Examples:

- checklist review;
- schema validation;
- script-based verification;
- figure review;
- package completeness audit;
- smoke tests;
- reproducibility checks.

### 8.3 Validators should be packaged when warranted

If correctness is subtle and machine-checkable, the package should ship a validator or validation instructions.

The session handoff validator script is direct evidence for this rule.

### 8.4 Negative and misuse cases matter

Canonicalization should consider at least:

- happy-path execution;
- insufficient-input cases;
- wrong-trigger cases;
- missing dependency cases;
- malformed-output cases;
- overbroad invocation cases.

---

## 9. Runtime Interface and Portability

### 9.1 Separate semantic capability from runtime wrapper

The skill’s semantics should not be trapped inside one UI or one provider-specific wrapper.

### 9.2 Runtime-specific bindings are allowed

Examples include:

- `agents/openai.yaml` UI metadata;
- zipped `.skill` delivery bundles;
- environment-specific instructions.

These wrappers are permitted, but they must remain secondary to the canonical source.

### 9.3 Maintain semantic parity across bindings

Different bindings may adapt filenames, metadata shape, or packaging format, but they should not silently change the capability contract.

### 9.4 Declare dependencies and environment assumptions

If the skill relies on tools, libraries, rendering binaries, or OS-level setup, the package must say so.

The PDF skill strongly motivates this requirement.

---

## 10. Composition Rules

### 10.1 Skills can import neighboring artifacts

A skill may consume:

- standards;
- prompt templates;
- methodologies;
- rulesets;
- personas;
- state packages;
- tool contracts.

### 10.2 Imported artifacts retain their own authority

A skill that uses Guided Autonomy does not thereby become the canonical GAP standard.

A skill that invokes a prompt template does not redefine prompt-template rules.

### 10.3 Do not collapse everything into SKILL.md

The skill entrypoint should orchestrate the package, not absorb all adjacent artifact classes into one giant file.

### 10.4 Prefer explicit composition over hidden assumptions

If a skill expects a prompt template, state package, or validator, say so.

---

## 11. Documentation Standard for Skills

Every canonical skill package should include at least:

- canonical entrypoint (`SKILL.md` or equivalent);
- concise description/purpose;
- use-when / do-not-use-when guidance;
- procedure/workflow;
- supporting artifact map;
- output contract;
- quality gates;
- runtime/dependency notes when relevant;
- provenance/versioning.

Optional but recommended when warranted:

- schema files;
- validators;
- examples;
- runtime metadata;
- smoke tests;
- generated distribution bundles.

The documentation should help the next agent perform the skill, not merely advertise it.

---

## 12. Lifecycle and Promotion

### 12.1 Draft versus canonical

A skill becomes a canonical candidate only when it is more than an interesting prompt.

Evidence for promotion should include:

- actual use across more than one instance;
- identifiable boundaries;
- explicit outputs;
- enough supporting artifacts to preserve the capability;
- review of failure/misuse cases.

### 12.2 Supersession must be explicit

If a skill replaces an earlier one, state the lineage.

### 12.3 Archive delivery forms separately from canonical source

Binary package exports and runtime-specific copies should not replace the canonical inspectable source tree.

### 12.4 Retain source lineage

Even superseded skill generations remain evidence for how the capability evolved.

---

## 13. Anti-Patterns

The following are canonical defects or strong warnings:

1. **Prompt masquerading as a skill** — long instruction text with no package anatomy, artifacts, or output contract.
2. **Hidden critical dependency** — side files materially control the capability but are never mentioned by the entrypoint.
3. **Undeclared activation sprawl** — the skill claims to solve an overly broad set of unrelated jobs.
4. **Runtime lock-in without reason** — semantics depend on one wrapper when the canonical source could have preserved them plainly.
5. **Opaque binary authority** — zipped distributions replace inspectable source.
6. **Checklist without procedure** — quality gates exist, but no actual workflow is provided.
7. **Procedure without completion** — steps exist, but no one can tell when the skill succeeded.
8. **Artifact dumping** — scripts, schemas, assets, and prompts exist with no package map or orchestration.
9. **Neighbor-layer collapse** — persona, methodology, state, rules, prompt, and skill are merged into one unanalyzable blob.
10. **Historical confusion** — old or experimental variants are treated as current canonical skill behavior without lineage review.

---

## 14. Minimal Canonical Skill Metadata

A canonical skill package should expose machine-readable metadata equivalent to the following shape:

```json
{
  "skill_id": "session-handoff",
  "title": "Session Handoff",
  "version": "1.0.0",
  "status": "CANONICAL",
  "purpose": "Preserve session state for zero-loss resumption.",
  "entrypoint": "SKILL.md",
  "use_when": ["Need to preserve current working context for later continuation."],
  "do_not_use_when": ["Task is to continue the project work itself rather than package state."],
  "supporting_artifacts": [
    "references/state_schema.md",
    "scripts/validate_snapshot.py",
    "scripts/render_mermaid.py"
  ],
  "outputs": [
    "00_executive_narrative.md",
    "01_state_snapshot.json"
  ],
  "runtime_bindings": ["zip bundle", "agent metadata"],
  "source_lineage": []
}
```

See the companion schema and example files in this package.

---

## 15. Relationship to the Prompt Template Standard

The Prompt Template Standard and Skill Standard are companion artifacts.

- Use the **Prompt Template Standard** when the main question is how to define a reusable instruction instrument.
- Use the **Skill Standard** when the main question is how to package a reusable procedural capability with surrounding artifacts.

A skill may embed or invoke prompt templates.
A prompt template may be one component inside a skill.
Neither replaces the other.

---

## 16. Canonicalization Gate

A skill package is ready for canonical-candidate status when all of the following are true:

- the skill has a stable identity and scope;
- activation boundaries are explicit;
- the package anatomy is inspectable;
- the procedure is externally visible;
- outputs and quality gates are named;
- supporting artifacts are mapped;
- runtime/dependency assumptions are declared;
- portability or representation policy is clear;
- provenance is recorded;
- the package has survived at least a basic misuse/failure review.

If those conditions are missing, the artifact may still be useful, but it is not yet an evergreen canonical skill.
