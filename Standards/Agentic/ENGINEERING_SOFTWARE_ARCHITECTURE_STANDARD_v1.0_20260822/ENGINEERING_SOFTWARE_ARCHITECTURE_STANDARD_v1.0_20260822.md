# Engineering and Software Architecture Standard

**Version:** 1.0.0  
**Date:** 2026-08-22  
**Authority status:** CANONICAL CANDIDATE  
**Scope:** Evergreen engineering and software-architecture rules that apply across projects without selecting one universal architecture pattern.  
**Out of scope:** Project-specific architecture, language-specific style guides, domain algorithms, safety classifications, and architecture-pattern standards that already live separately.

---

## 0. Governing Principle

> **Preserve the intended system before optimizing the local implementation. Architecture is admitted by requirements, invariants, and evidence, not by habit or convenience.**

The purpose of this standard is not to make every repository look alike. It is to keep engineering work structurally honest while allowing radically different systems to choose different architectures.

Clean Architecture, hexagonal architecture, event-driven systems, layered monoliths, MVC, serverless systems, emergence-based systems, and specialized native architectures can all be correct under different constraints.

The standard governs **how architecture is chosen, preserved, changed, and verified**.

---

## 1. Establish Authority Before Architecture Work

Before a consequential architecture change, identify the hierarchy of authority that controls the project.

Possible sources include:

- authored specification;
- canonical architecture documents;
- formal invariants;
- public contracts;
- requirements;
- accepted decision records;
- tests that encode intended behavior;
- actual runtime behavior;
- current implementation;
- roadmap / transitional state.

These sources are not automatically equal.

### 1.1 Current implementation is evidence, not automatic authority

Existing code may be:

- correct;
- transitional;
- incomplete;
- legacy;
- drifted;
- experimental;
- a workaround.

Do not infer the target architecture from whatever code happens to exist locally when stronger authored authority exists.

### 1.2 Conflicts stay visible

If sources conflict, state the conflict and which source controls the current decision. Do not silently reconcile them.

---

## 2. Reconstruct the Whole System Before Local Mechanism Design

A local module should not redefine the system around itself.

Before adding or replacing a meaningful mechanism, understand:

- the system goal;
- authoritative state;
- ownership boundaries;
- runtime path;
- data flow;
- dependency direction;
- persistence model;
- configuration path;
- failure semantics;
- public interfaces;
- performance/locality constraints;
- existing capabilities that may already own the behavior.

Inspection should be proportional to the task. This is not a ritual requirement to scan every file in every repository.

---

## 3. Trace Every New Mechanism to a Requirement or Invariant

Before creating a new abstraction, service, store, queue, cache, scheduler, walker, registry, adapter, manager, or other mechanism, answer:

1. What requirement or invariant requires it?
2. Which existing subsystem currently owns adjacent responsibility?
3. Why is extension or completion of existing capability insufficient?
4. What new semantic responsibility does this mechanism uniquely own?
5. How will its correctness be verified?

If the trace cannot be established, stop and investigate rather than inventing infrastructure.

### 3.1 Duplicate capability is a defect by default

Before adding a new capability, audit the repository for existing ownership.

A second mechanism is justified only when it is semantically distinct or a deliberate migration boundary.

Convenience, discoverability failure, or unfamiliar naming do not by themselves justify duplication.

---

## 4. Invariants Before Mechanisms

State what must remain true before designing how to enforce it.

Good architecture work moves in this order:

```text
requirement / source pressure
        -> invariant
        -> ownership
        -> boundary
        -> mechanism
        -> verification
```

Mechanisms may change. The invariant should explain why they exist.

This reduces framework-first architecture and prevents implementation detail from becoming the rationale for itself.

---

## 5. Choose Architecture by Fit, Not Fashion

Project-specific architecture standards are selectable instruments.

Selection should consider:

- domain shape;
- failure model;
- performance constraints;
- deployment environment;
- state model;
- data volume and locality;
- external integration needs;
- team / maintenance needs;
- auditability and provenance;
- expected evolution.

Do not combine architecture patterns merely because each contains a useful idea. A hybrid must have explicit boundary rules and a reason for each imported structure.

The narrowest architecture that truthfully fits the problem is preferred over a larger architecture with unused layers.

---

## 6. Ownership and Authoritative State

Every important state should have an identifiable owner.

Distinguish:

- authoritative state;
- derived projections;
- caches;
- indexes;
- replicas;
- snapshots;
- fixtures;
- UI state;
- persisted history.

Derived state must not silently become authoritative because it is easier to query.

### 6.1 Write paths and read paths may differ

Optimized read models, indexes, caches, and summaries may be rebuildable projections. They must not mutate or redefine workflow truth unless explicitly designed as an authority.

### 6.2 State transitions must be explicit

For consequential state:

- validate inputs before mutation;
- define transition legality;
- preserve failure atomicity where required;
- make partial failure visible;
- reject stale or incompatible writes when version/state identity matters.

---

## 7. Dependency Direction Must Be Explicit

Architecture is not real if dependency direction exists only in a diagram.

Define and, when practical, enforce:

- which layers/modules may depend on which;
- where domain/native types live;
- which modules own interfaces;
- which implementations sit behind boundaries;
- which imports are forbidden.

Use tests, import rules, linting, compile boundaries, package structure, or other mechanical checks when the architecture depends on those constraints.

---

## 8. External Systems Stay at the Boundary

Frameworks, SDKs, databases, external APIs, UI toolkits, queues, and provider models are boundary mechanisms.

Translate them into native project concepts rather than allowing external shapes to define internal truth.

Examples:

- provider errors -> project error types;
- API payloads -> domain/native types;
- storage rows -> persistence representation, not automatic domain model;
- UI convenience state -> projection, not core state;
- framework lifecycle -> adapter concern unless the domain actually depends on it.

This preserves replaceability and semantic ownership.

---

## 9. Configuration Is Data, Not Scattered Code

Configurable values must not be hardcoded into operational logic.

Examples include:

- paths;
- endpoints;
- ports;
- thresholds;
- feature flags;
- timeouts;
- retry limits;
- resource budgets;
- allowed modes;
- UI-configurable values.

Use a centralized, typed, validated configuration path appropriate to the project.

Defaults should be explicit and inspectable.

Secrets must remain outside source and ordinary version-controlled configuration.

---

## 10. Modularity and Size

Prefer high cohesion and low coupling.

A module should have one coherent semantic responsibility, not simply a convenient pile of related functions.

### 10.1 File-size policy

For new or actively modified functional source files:

- target **500 logical lines of code or fewer**;
- decompose larger files when the split improves semantic ownership;
- do not split mechanically into meaningless fragments merely to satisfy a number.

For pre-existing files already above the limit:

- record the violation when relevant;
- do not increase it casually;
- refactor when the file is part of the active architectural work or when size is obstructing correctness/reviewability.

---

## 11. Complexity, Locality, and Resource Budgets

Performance constraints are architecture constraints when the project depends on them.

Do not replace a locality-preserving, sparse, streaming, bounded, or incremental design with a global scan or dense representation merely because the implementation is simpler.

For projects with explicit complexity bounds:

- treat the bound as an invariant;
- analyze asymptotic changes before implementation;
- test representative scale;
- record deliberate exceptions.

For ordinary applications without such constraints, avoid premature optimization while still preventing obviously pathological designs.

---

## 12. Surgical Change Discipline

When modifying an existing system:

- touch what the requested change requires;
- preserve unrelated behavior;
- preserve public APIs unless change is intentional;
- preserve meaningful comments and rationale;
- remove only orphaned code caused by the change unless broader cleanup is authorized;
- avoid opportunistic refactors that make the diff harder to reason about.

A changed line should be traceable to the task, its dependency, or a required cleanup caused by the task.

Large architectural changes are allowed when the architecture genuinely requires them. They must be explicit rather than smuggled into cleanup.

---

## 13. Testing Is Part of Architecture

Tests must verify both behavior and architectural boundaries where those boundaries are load-bearing.

### 13.1 New behavior requires accommodating tests

Every new behavior-bearing module/file should have a test at the closest meaningful level unless there is a clear structural reason it cannot.

When interactions change, update integration tests to cover the new path.

### 13.2 Tests do not define truth by themselves

A passing test suite does not prove the architecture is correct if the tests encode the wrong architecture.

Validation should include, as relevant:

- unit behavior;
- integration paths;
- public contracts;
- negative cases;
- failure behavior;
- migration behavior;
- performance/locality budgets;
- architecture/import boundaries;
- end-to-end real-use paths.

### 13.3 Runtime evidence matters

When a claim concerns the actual executing path, inspect or execute that path. Unit tests and documentation alone are insufficient.

---

## 14. Error and Failure Semantics

Failures should be explicit, typed or distinguishable where useful, and actionable at the correct boundary.

Avoid:

- swallowed errors;
- infinite loading / waiting states;
- generic success after partial failure;
- retries without bounds or observability;
- translating every failure into an undifferentiated exception/string;
- mutating authoritative state before validation completes when atomicity is required.

The system should preserve enough failure context to diagnose what actually happened.

---

## 15. Migration and Transitional Architecture

Migration states are real architecture states and should be documented as such.

When old and new systems coexist:

- state which side owns authoritative writes;
- state how reads are resolved;
- state synchronization rules;
- state cutover criteria;
- state rollback path when appropriate;
- prevent both systems from silently becoming independent authorities.

Transitional code must not be mistaken for the long-term target simply because it is currently executable.

---

## 16. Documentation and Architecture Must Remain Independent but Aligned

Architecture changes must update durable documentation when the approved architecture changes.

Implementation work must not rewrite canonical documentation merely to make the implementation appear compliant.

Document:

- architecture boundaries;
- invariants;
- state ownership;
- public contracts;
- important decisions and rationale;
- deliberate exceptions;
- migrations.

Keep transient repair narratives outside durable source-folder anatomy.

---

## 17. Completion and Release Claims

Do not declare an engineering task complete merely because:

- code was written;
- unit tests passed;
- a scaffold exists;
- a validator checks the new schema;
- a README says the feature exists.

Completion must match the task's real burden.

For user-facing or integrated capabilities, exercise the relevant end-to-end path before claiming completion when feasible.

Report partial completion precisely when the full path has not been verified.

---

## 18. Anti-Patterns

Reject or challenge:

- architecture imposed before the problem is understood;
- duplicate subsystems with overlapping ownership;
- local convenience redefining the target architecture;
- caches/projections becoming hidden sources of truth;
- frameworks defining the domain model;
- hardcoded operational configuration;
- global scans introduced into locality-constrained systems;
- abstractions with no current responsibility;
- configuration or feature flexibility added speculatively;
- large unrelated refactors inside a focused fix;
- tests that prove only the new implementation's assumptions;
- architecture diagrams with unenforced dependency direction;
- transitional architecture presented as final architecture;
- documentation rewritten to ratify implementation drift.

---

## 19. Architecture Change Gate

Before a material architectural change is accepted, answer:

1. What authoritative requirement or pressure motivates it?
2. What invariant does it protect?
3. What subsystem owns the responsibility?
4. Was existing capability audited first?
5. What dependency direction changes?
6. What state becomes authoritative, derived, or transitional?
7. What external boundaries are involved?
8. What configuration changes?
9. What tests prove behavior and architecture?
10. What runtime path was exercised?
11. What documentation must change?
12. What would falsify or reverse the decision?

If these cannot be answered for a consequential change, the architecture is not ready to be promoted.
