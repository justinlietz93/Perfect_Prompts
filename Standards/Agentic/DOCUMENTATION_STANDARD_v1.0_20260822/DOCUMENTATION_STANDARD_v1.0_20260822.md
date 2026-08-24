# Documentation Standard

**Version:** 1.0.0  
**Date:** 2026-08-22  
**Authority status:** CANONICAL CANDIDATE  
**Scope:** Evergreen rules for documentation authority, placement, custody, provenance, maintenance, generated material, history, handoffs, and validation across software, research, and mixed repositories.  
**Out of scope:** Project-specific document taxonomies, site generators, visual themes, publication tooling, and transient project state.

---

## 0. Governing Principle

> **Documentation must preserve the system's truth and rationale without becoming a second, competing implementation of that truth.**

Documentation is not one homogeneous layer. A durable repository must distinguish current authority, implementation evidence, operational state, history, source material, generated projections, and handoff state. Most documentation drift begins when those roles are allowed to blur.

A document's first job is therefore not to be comprehensive. Its first job is to have a **clear semantic role and authority boundary**.

---

## 1. Separate the Truth Planes

At minimum, repositories must distinguish these planes when they exist:

1. **Target / canonical authority** - what the system is intended or required to be.
2. **Current implementation truth** - what the executing code or realized artifact actually does now.
3. **Current-state / roadmap truth** - what is active, incomplete, blocked, transitional, or planned.
4. **Evidence / provenance truth** - observations, experiments, source packets, logs, reports, and historical artifacts that support or challenge claims.

No plane may silently impersonate another.

Examples:

- Current code does not rewrite the target architecture merely because it exists.
- A TODO does not prove implementation.
- A generated report does not become canonical design rationale.
- A handoff does not become long-term documentation authority.
- An archive does not become current truth because it contains the most detailed explanation.

When planes disagree, record the disagreement and state which source controls the decision being made.

---

## 2. Documentation Classes

Every durable document should belong to a recognizable class.

| Class | Purpose | Authority expectation |
|---|---|---|
| Canonical / normative | Defines current governing truth, rules, architecture, or contract | High; changes deliberate |
| Resident subsystem documentation | Durable anatomy, rationale, contracts, ownership, invariants | High within scope |
| Reference contract | API, CLI, schema, configuration, public interface truth | High when tied to source contract |
| Decision record | Records a durable decision, rationale, alternatives, consequences | Historical authority for that decision |
| Operational / runbook | Tells an operator how to perform or recover an action | Current only while verified |
| Current-state / roadmap | Records what is active, planned, blocked, or transitional | Time-sensitive; not design authority |
| Handoff | Preserves state for continuation | Transitional; not long-term authority |
| Generated projection | Derived view of another authority | Never independent authority |
| Evidence / source | Supports or challenges a claim | Evidence, not normative by default |
| Snapshot / report | Point-in-time description of a state or change | Historical / disposable |
| Draft | Unratified work in progress | Non-authoritative |
| Archive | Retained historical material | Historical only |

Repositories may use different names, but the semantic distinctions must remain.

---

## 3. Resident Documentation Must Be Durable

Documentation that lives beside source code or inside a subsystem is expected to remain useful after the current implementation episode ends.

Resident documentation should describe things such as:

- subsystem anatomy;
- architectural rationale;
- ownership and responsibility boundaries;
- public and internal contracts;
- invariants;
- state and data-flow ownership;
- failure behavior;
- extension points;
- stable operating semantics;
- non-obvious constraints.

Resident documentation should **not** be replaced by:

- point-in-time change summaries;
- repair receipts;
- temporary implementation snapshots;
- migration narration that only describes the current branch;
- transient test status;
- agent session summaries;
- disposable consolidation narratives.

Those artifacts may be valuable, but they belong in history, reports, handoffs, lab records, release notes, or other explicitly transient areas.

### 3.1 Snapshot replacement is a custody failure

Replacing durable anatomy/rationale with a snapshot of what was just changed destroys the documentation's long-term job.

A snapshot may supplement durable docs. It must not silently overwrite them.

---

## 4. Canonical Documentation Is Protected Authority

Canonical documents are not implementation scratch space.

### 4.1 Implementation work does not authorize documentation rewrites

Changing code, repairing a subsystem, consolidating files, or completing a migration does not automatically grant permission to rewrite the canonical architecture that the implementation is supposed to satisfy.

Unless documentation change is explicitly part of the task:

- preserve canonical docs;
- use them to evaluate the implementation;
- record discrepancies separately;
- propose required doc changes for ratification when reality legitimately changed.

### 4.2 Never validate a rewrite against itself

The following sequence is prohibited:

1. modify implementation;
2. rewrite canonical documentation to describe that implementation;
3. validate the implementation against the rewritten documentation.

That is circular custody. It removes the independent authority needed to detect drift.

### 4.3 Supersede rather than erase

When a canonical decision genuinely changes:

- identify the old authority;
- record why it no longer controls;
- create or update the successor;
- preserve lineage;
- make the current authority unambiguous.

Do not silently rewrite historical decisions as though the new decision had always been the rule.

---

## 5. One Current Owner Per Claim

Every important current claim should have one identifiable owner.

Examples:

- API shape -> schema / OpenAPI / typed contract;
- CLI behavior -> command schema or generated help;
- configuration -> typed settings or config schema;
- subsystem architecture -> canonical architecture document;
- release state -> release metadata / canonical status page.

Guides, tutorials, READMEs, generated pages, and examples may project that truth. They must not become competing authorities.

### 5.1 Duplicate authority rule

If two current documents appear to own the same claim and disagree:

1. do not casually merge their prose;
2. identify the semantic role of each;
3. determine which source has authority;
4. preserve useful historical information outside the current-truth path;
5. update links and readers to the survivor;
6. record the decision if material.

Exact mirrors require an explicit generation or synchronization rule.

---

## 6. Provenance Is Part of Documentation Correctness

A reader should be able to determine where a material claim came from.

For load-bearing documentation, preserve as applicable:

- source documents;
- source commit or release;
- schema / contract version;
- generating tool and version;
- input hashes;
- evidence package identifiers;
- decision record;
- review or ratification status;
- last verification date.

A detailed page with unknown provenance is weaker than a concise page whose authority can be established.

---

## 7. Generated Documentation

Generated documentation is a **projection**.

Rules:

- Do not hand-edit generated files.
- Preserve the generation path.
- Record inputs and tool identity when material.
- Make generated files reproducible.
- Detect stale generated artifacts in validation or CI when practical.
- Prefer a readable human summary for raw generated data.
- Archive or version old generated outputs when they remain historically useful.

If generated prose conflicts with its source contract, fix the generator or source. Do not patch the generated output to make the conflict disappear.

---

## 8. Snapshots, Reports, Change Summaries, and History

Historical artifacts answer **what happened**, not **what is true now**.

They should preserve:

- date / version / commit;
- scope of the observation;
- what changed;
- what was measured;
- what remained unresolved;
- links to the controlling current authority when known.

They must be visibly labeled as historical or point-in-time.

Do not put a transient snapshot where a future maintainer will reasonably interpret it as the subsystem's durable resident documentation.

---

## 9. Handoffs Are State Transfer, Not Canon

A handoff should preserve enough state to resume work:

- current objective;
- authoritative sources;
- completed work;
- active branch / version / artifacts;
- decisions already made;
- rejected paths and why;
- unresolved questions;
- next actions;
- environment or execution state when relevant.

Handoffs are deliberately redundant with live work. That does not make them canonical architecture.

If a handoff contains a durable discovery, promote that discovery into the appropriate canonical or resident document through an explicit update.

---

## 10. Documentation Placement

Placement should communicate semantic role.

Recommended patterns:

```text
docs/
├── pages/          # current reader-facing docs
├── contracts/      # machine-checkable or normative contracts
├── architecture/   # durable system knowledge and ADRs
├── operations/     # current runbooks
├── roadmap/        # current-state planning
├── generated/      # reproducible projections
├── sources/        # imported evidence/source packets
├── reports/        # point-in-time reports and audits
├── handoffs/       # continuation state
├── drafts/         # unratified work
└── archive/        # superseded/historical material
```

This is an example, not a required directory tree. The semantic roles are required; the exact folders are not.

---

## 11. README and Source-Folder Rules

### 11.1 Root README

The root README is orientation, not the entire project specification.

It should answer:

- what the project is;
- why it exists;
- how to start or navigate;
- where current authority lives;
- where to find deeper documentation.

### 11.2 Source-folder README

A subsystem README may describe:

- file layout;
- responsibility boundaries;
- public interfaces;
- contracts and invariants;
- important imports / dependencies;
- tests;
- extension points;
- stable local operating rules.

It should not become a running diary of every refactor performed in that directory.

---

## 12. Documentation Must Match Reality Without Losing Independence

Documentation correctness requires checking the actual system where the claim is implementation-dependent.

Examples:

- runtime path claims -> inspect runtime path;
- configuration claims -> inspect schema / loader;
- CLI claims -> inspect live help or command schema;
- public behavior -> execute representative flow;
- performance claims -> inspect measurements;
- generated-artifact claims -> verify generation.

But verification against implementation does not erase the target/current distinction. When canonical target and runtime differ, the correct result may be **documented non-conformance**, not silent canonical rewrite.

---

## 13. Change Procedure

For a material documentation change:

1. identify document class and authority;
2. identify the claim(s) being changed;
3. locate controlling sources / contracts;
4. determine whether this is correction, clarification, supersession, status update, or history;
5. make the smallest complete change;
6. preserve rationale and lineage;
7. update dependent references where necessary;
8. run documentation validation;
9. record the change in the appropriate history mechanism.

---

## 14. Documentation Validation

Validation should scale with repository size, but important repositories should automate what can drift.

Useful checks include:

- broken links and anchors;
- duplicate authority;
- stale generated artifacts;
- invalid status terms;
- contract/prose divergence;
- orphaned current pages;
- missing provenance;
- inconsistent versions;
- references from current docs into archive/draft authority;
- undocumented public configuration or interfaces.

A documentation build passing does not prove the documentation is semantically correct. Semantic authority must also be checked.

---

## 15. AI Agent Documentation Rules

When an AI agent edits documentation, it must first determine:

- what document class it is editing;
- which source controls the claim;
- whether the task authorizes canonical change;
- whether generated or historical material is involved;
- whether another current page owns the same claim.

An agent must not:

- rewrite canon to fit its implementation;
- replace durable resident docs with a change summary;
- hand-edit generated files;
- promote roadmap or draft behavior into current truth;
- erase rejected decisions or historical rationale silently;
- infer implementation status from aspirational prose;
- create a second current source of truth because it is convenient.

---

## 16. Anti-Patterns

Reject or repair these patterns:

- **Snapshot-as-anatomy:** a point-in-time description replaces durable subsystem documentation.
- **Documentation laundering:** implementation drift is made legitimate by rewriting the docs around it.
- **Authority collision:** two current pages own the same claim.
- **Generated hand-edit:** a derived page is patched instead of regenerating its source.
- **History-as-current:** archive/report prose is treated as live guidance.
- **Roadmap inflation:** intended work is documented as shipped behavior.
- **Handoff canonization:** a session summary quietly becomes design authority.
- **Rationale stripping:** an edit keeps the conclusion but removes why it exists.
- **Orphan provenance:** a claim survives after its source, version, or evidence link disappears.
- **Documentation by accumulation:** every session adds another file without deciding which existing document owns the information.

---

## 17. Canonicalization Gate

A documentation system is ready for canonical use when:

- document classes and authority are visible;
- canonical claims have identifiable owners;
- resident documentation is durable rather than episodic;
- target/current/history/state planes remain distinguishable;
- generated material is reproducible and non-authoritative;
- provenance is preserved for load-bearing claims;
- supersession/history is explicit;
- handoffs cannot silently replace canon;
- basic drift checks are executable or clearly defined.

The governing test is simple:

> **Could a future maintainer determine what is true, why it is true, what only used to be true, and which artifact has the right to decide?**
