# Curriculum Authority

**Status:** TEMPLATE AUTHORITY  
**Template version:** 1.0

## Purpose

This file defines the semantic rules of an instantiated curriculum. Replace bracketed fields during instantiation but preserve the rules unless the curriculum intentionally adopts a different learning architecture.

## Target

- **Curriculum name:** `{{CURRICULUM_NAME}}`
- **Subject / domain:** `{{DOMAIN}}`
- **Primary learner:** `{{LEARNER}}`
- **Ultimate capability target:** `{{CAPABILITY_TARGET}}`
- **Why this curriculum exists:** `{{PURPOSE}}`

## Authority model

The curriculum must have one controlling progression order. Resource acquisition, casual reading, current research needs, software installation, and supplemental material may not create competing hidden orders.

### Progression authority

`00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md` is the human-readable controlling progression document. `CURRICULUM_SPEC.json` is its machine-readable companion. They must agree.

If they disagree, the curriculum is inconsistent and must be repaired before treating either representation as trustworthy.

### Group authority

Within a group, the numbered resource order in that group's `README.md` is definitive for that group unless an explicitly documented targeted-use path is active.

### Current-work authority

Current work, projects, or research can:

- change what is worth opening now;
- activate a permitted branch;
- expose a prerequisite gap;
- justify a targeted consultation of advanced material.

They cannot silently convert an unearned dependency into an earned one or rewrite the durable curriculum spine.

## Learning modes

Every resource or learning activity should have an explicit role.

- **DIAGNOSTIC** — rapid sampling to expose actual gaps; does not itself establish mastery.
- **CORE PASS** — active study that controls progression and contributes directly to the exit gate.
- **DEEPENING PASS** — stronger second treatment after the core pass; normally does not block the next spine group.
- **REFERENCE** — consulted when a live question requires it; not read linearly by default.
- **OPTIONAL** — useful enrichment that does not control progression.
- **RECREATIONAL / CONTEXTUAL** — history, biography, narrative, or broad conceptual material used for perspective, motivation, vocabulary, or hypothesis generation.

## Mastery rule

Completion is not the same thing as mastery.

A group advances when its **exit gate** is met. Exit gates must describe observable capability, not chapter completion, hours spent, videos watched, or books opened.

Domain-appropriate evidence can include:

- independent problem solving;
- proof reconstruction;
- derivation from definitions;
- implementation from understood principles;
- design or build work;
- oral explanation without prompts;
- comparison of neighboring concepts that are commonly confused;
- counterexamples and negative controls;
- reproducible computational or physical experiments;
- transfer to a novel problem;
- formal verification where justified.

## Dependency-aware learning

The curriculum may have a primary spine plus parallel branches.

A branch may open only when its start gate is satisfied. A start gate is a dependency condition, not merely a date or desire to begin.

When a live problem requires advanced material early, the curriculum may permit **targeted activation**:

1. identify the exact concept required;
2. identify the exact missing prerequisite;
3. repair only what is needed to make the targeted concept usable;
4. mark any remaining dependency debt explicitly;
5. return to the active problem;
6. do not misclassify targeted familiarity as completion of the full group.

This mechanism avoids both prerequisite inversion and unnecessary prerequisite walls.

## Resource-selection rule

Resources are chosen for jobs, not prestige.

A curriculum may deliberately use different resources for:

- intuition;
- first formal exposure;
- exercises;
- proof depth;
- visual understanding;
- computational reconstruction;
- historical context;
- specialist reference.

One source need not perform every role.

## Research / current-work transfer

When the curriculum supports active research or project work, transfer records must distinguish:

- the conventional concept;
- the exact source and definition;
- relevant theorem or standard result;
- required hypotheses;
- the target project/research counterpart;
- whether the relationship is exact, a proved special case, conjectural, analogous, or merely visually/syntactically similar;
- the next verification step.

If a separate canonical Research & Evidence Standard exists in the standards library, it governs research-grade proof, computation, falsification, provenance, and review requirements. The curriculum template does not weaken that standard.

## Generated-work separation

Source resources belong in `resources/` or the curriculum's declared resource library. Generated notes, exercises, notebooks, figures, experiments, derivations, and outputs belong under `work/`.

Do not contaminate the resource library with generated artifacts.
