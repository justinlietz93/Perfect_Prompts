# Emergence Based Architecture

## Overview

Emergence Based Architecture (EBA) is an invariant-first software architecture for systems whose correct shape cannot be safely imposed in advance.

EBA does not begin with controllers, services, repositories, workers, pipelines, or framework conventions. It begins with the material the system receives, the observations that can be made about it, the invariants that must hold, and the structures that earn admission through evidence and constraint.

The goal is to prevent premature architecture while still maintaining strong engineering discipline.

EBA is useful when a system must discover, preserve, transform, validate, or project structure from complex material such as text, events, simulations, documents, signals, proofs, workflows, or domain-specific state.

---

## Core Goals

- Preserve source identity and lineage.
- Separate observation from decision.
- Admit structure only when it is supported by evidence.
- Make invariants explicit and testable.
- Keep rejected or uncertain structures inspectable.
- Treat external frameworks, storage, APIs, and tools as boundary mechanisms.
- Prevent generic architectural vocabulary from replacing native system language.
- Support steady refinement without losing prior evidence.
- Maintain strict dependency direction and automated governance.
- Produce versioned, auditable projections for users and machines.

---

## One-Sentence Definition

Emergence Based Architecture is an invariant-first architecture where internal structure is admitted through source preservation, observation, constraint, formation, operation, projection, and boundary translation.

---

## When To Use EBA

Use EBA when:

- The domain is not naturally CRUD-shaped.
- The system transforms or interprets complex source material.
- Premature layering would hide important distinctions.
- The architecture must preserve provenance and explain decisions.
- The system needs strong validation, auditability, or reversibility.
- External frameworks must not define the system's core concepts.
- The correct internal vocabulary is expected to sharpen over time.
- The system may evolve through repeated discovery and correction.

Examples:

- Text chunking engines
- Compilers and interpreters
- Document analysis systems
- Knowledge graph builders
- Simulation engines
- Scientific data pipelines
- Event interpretation systems
- Rule engines
- Search and retrieval systems
- Planning systems
- Workflow formation engines
- Domain-specific operating layers
- Verification and audit systems

Avoid EBA when the application is simple, conventional, and already well-described by CRUD, MVC, three-tier, or plain hexagonal architecture.

---

## Core Principle

The architecture must not import a shape before the system earns it.

A module, concept, service, or boundary should exist because the system has revealed a stable need for it, not because a framework template expects it.

Bad:

```text
Create UserManager because applications usually have managers.
Create DocumentService because services are a default layer.
Create ChunkRepository because persistence might exist later.
```

Better:

```text
Create SourceRecord because input identity must be preserved.
Create Observation because evidence must be separated from decisions.
Create Invariant because some condition must never be violated.
Create Candidate because structure is proposed before it is accepted.
Create Projection because external output must not define internal truth.
```

---

## Architectural Flow

EBA organizes a system around the following flow:

```text
source
  → observation
  → invariant
  → formation
  → operation
  → projection
  → boundary
```

This is not a runtime pipeline that every request must literally execute from start to finish. It is an architectural admission order.

The system first preserves what it receives. Then it observes. Then it checks what must remain true. Then it forms candidate structures. Then it operates on admitted structures. Then it projects useful views. Finally, it crosses external boundaries through ports, adapters, CLIs, APIs, storage, or UI.

---

## Layer Summary

| Layer | Purpose | Decision Authority |
|---|---|---|
| `source/` | Preserve canonical material, identity, and lineage | Defines what was received |
| `observation/` | Collect evidence without mutation | Reports what is seen |
| `invariant/` | Define and test what must remain true | Rejects invalid states |
| `formation/` | Propose, accept, reject, repair, and reconcile structure | Admits internal structures |
| `operation/` | Execute lawful system behavior and state transitions | Performs work |
| `projection/` | Produce versioned external views | Renders without redefining truth |
| `boundary/` | Interface with external tools, frameworks, storage, and users | Translates across system edges |
| `policy/` | Declare architecture, naming, dependency, and contract rules | Governs development |
| `shared/` | Provide small primitives without domain authority | Supports all layers |

---

## Standard Project Layout

```text
eba_app/
├─ pyproject.toml
├─ README.md
├─ .pre-commit-config.yaml
├─ .importlinter
│
├─ src/
│  └─ eba_app/
│     │
│     ├─ source/
│     │  ├─ records/
│     │  │  ├─ source_record.py
│     │  │  ├─ source_span.py
│     │  │  └─ source_identity.py
│     │  ├─ normalization/
│     │  │  ├─ reversible_normalizer.py
│     │  │  └─ normalization_trace.py
│     │  └─ lineage/
│     │     ├─ lineage_map.py
│     │     └─ provenance.py
│     │
│     ├─ observation/
│     │  ├─ instruments/
│     │  │  ├─ base_instrument.py
│     │  │  └─ instrument_result.py
│     │  ├─ evidence/
│     │  │  ├─ observation.py
│     │  │  ├─ evidence_set.py
│     │  │  └─ confidence.py
│     │  └─ reports/
│     │     └─ observation_report.py
│     │
│     ├─ invariant/
│     │  ├─ rules/
│     │  │  ├─ invariant.py
│     │  │  ├─ invariant_result.py
│     │  │  └─ invariant_registry.py
│     │  ├─ checks/
│     │  │  ├─ losslessness_check.py
│     │  │  ├─ identity_check.py
│     │  │  ├─ boundary_check.py
│     │  │  └─ contradiction_check.py
│     │  └─ ledger/
│     │     ├─ invariant_ledger.py
│     │     └─ violation_record.py
│     │
│     ├─ formation/
│     │  ├─ candidates/
│     │  │  ├─ candidate.py
│     │  │  ├─ candidate_set.py
│     │  │  └─ candidate_reason.py
│     │  ├─ selection/
│     │  │  ├─ selector.py
│     │  │  ├─ selection_policy.py
│     │  │  └─ rejection.py
│     │  └─ assembly/
│     │     ├─ assembler.py
│     │     ├─ repair.py
│     │     └─ reconciliation.py
│     │
│     ├─ operation/
│     │  ├─ commands/
│     │  │  └─ command.py
│     │  ├─ transitions/
│     │  │  ├─ transition.py
│     │  │  ├─ transition_result.py
│     │  │  └─ transition_policy.py
│     │  ├─ state/
│     │  │  ├─ system_state.py
│     │  │  └─ state_view.py
│     │  └─ services/
│     │     └─ operation_service.py
│     │
│     ├─ projection/
│     │  ├─ views/
│     │  │  ├─ view_model.py
│     │  │  └─ rendered_view.py
│     │  ├─ exporters/
│     │  │  ├─ export_plan.py
│     │  │  └─ export_result.py
│     │  └─ schemas/
│     │     ├─ public_schema.py
│     │     └─ schema_version.py
│     │
│     ├─ boundary/
│     │  ├─ ports/
│     │  │  ├─ source_loader.py
│     │  │  ├─ artifact_writer.py
│     │  │  ├─ clock.py
│     │  │  ├─ id_provider.py
│     │  │  └─ telemetry_sink.py
│     │  ├─ adapters/
│     │  │  ├─ filesystem/
│     │  │  ├─ http/
│     │  │  ├─ sqlite/
│     │  │  └─ telemetry/
│     │  └─ presentation/
│     │     ├─ cli/
│     │     └─ api/
│     │
│     ├─ policy/
│     │  ├─ architecture_policy.py
│     │  ├─ naming_policy.py
│     │  ├─ dependency_policy.py
│     │  └─ public_contract_policy.py
│     │
│     └─ shared/
│        ├─ errors.py
│        ├─ result.py
│        ├─ ids.py
│        └─ typing.py
│
├─ governance/
│  ├─ tools/
│  │  ├─ enforce_imports.py
│  │  ├─ enforce_file_size.py
│  │  ├─ enforce_native_names.py
│  │  ├─ enforce_invariant_ledger.py
│  │  ├─ enforce_boundary_purity.py
│  │  └─ enforce_projection_contracts.py
│  ├─ policies/
│  │  ├─ architecture_contracts.md
│  │  ├─ naming_policy.md
│  │  ├─ invariant_policy.md
│  │  ├─ admission_policy.md
│  │  ├─ boundary_policy.md
│  │  ├─ projection_policy.md
│  │  ├─ testing_policy.md
│  │  └─ documentation_policy.md
│  └─ ci/
│     └─ quality-gates.yaml
│
├─ tests/
│  ├─ unit/
│  │  ├─ source/
│  │  ├─ observation/
│  │  ├─ invariant/
│  │  ├─ formation/
│  │  ├─ operation/
│  │  └─ projection/
│  ├─ contract/
│  │  ├─ boundary_ports/
│  │  └─ public_schemas/
│  ├─ contradiction/
│  │  ├─ malformed_inputs/
│  │  ├─ invariant_violations/
│  │  └─ false_structure_cases/
│  ├─ integration/
│  │  └─ boundary_adapters/
│  └─ e2e/
│     ├─ cli/
│     └─ api/
│
└─ docs/
   ├─ ARCHITECTURE.md
   ├─ SYSTEM_LANGUAGE.md
   ├─ INVARIANTS.md
   ├─ BOUNDARIES.md
   ├─ PROJECTIONS.md
   ├─ DECISION_LEDGER.md
   └─ ADRs/
```

---

## Layer Details

### 1. `source/`

The `source/` layer contains canonical material and identity.

It answers:

- What did the system receive?
- Where did it come from?
- How is identity preserved?
- What transformations are reversible?
- How do derived structures point back to their source?

Rules:

- Source records are canonical.
- Source identity must be stable.
- Source spans must be traceable.
- Normalization must produce a trace.
- Nothing downstream may silently discard source material.
- Derived structures must preserve lineage.

Typical contents:

```text
source_record.py
source_span.py
source_identity.py
normalization_trace.py
lineage_map.py
provenance.py
```

Do not place business operations, IO adapters, or presentation logic in `source/`.

---

### 2. `observation/`

The `observation/` layer collects evidence without deciding final structure.

It answers:

- What can be seen?
- Where was it seen?
- How confident is the observation?
- Which observations agree or conflict?
- Which observations are incomplete or uncertain?

Rules:

- Observation does not mutate source records.
- Observation does not admit final structures.
- Observation does not perform boundary IO.
- Observation results must include source references.
- Confidence and uncertainty should be explicit.
- Observers should be individually testable.

Typical contents:

```text
base_instrument.py
instrument_result.py
observation.py
evidence_set.py
confidence.py
observation_report.py
```

Avoid names like `processor`, `manager`, or `engine` unless an ADR justifies them.

---

### 3. `invariant/`

The `invariant/` layer defines what must remain true.

It answers:

- What must never be violated?
- What must be checked before structure is admitted?
- What conditions must survive transformation?
- What violations must be reported?
- Which assumptions are now stable enough to enforce?

Rules:

- Every invariant must be testable.
- Every invariant violation must produce a reportable result.
- Invariants must not depend on boundary adapters.
- Invariants must not perform IO.
- Invariant checks must be deterministic unless explicitly documented.
- Invariants should use source identity and observation evidence where possible.

Typical contents:

```text
invariant.py
invariant_result.py
invariant_registry.py
losslessness_check.py
identity_check.py
boundary_check.py
contradiction_check.py
invariant_ledger.py
violation_record.py
```

Examples of invariants:

```text
Every derived output must preserve source lineage.
Every public projection must declare a schema version.
No boundary adapter may define native identity.
No observation may mutate canonical source state.
No irreversible transformation may occur without explicit lossy mode.
Every accepted structure must cite evidence or policy.
```

---

### 4. `formation/`

The `formation/` layer proposes and admits internal structure.

It answers:

- What structures are suggested by the evidence?
- Which candidates hold under invariants?
- Which candidates fail?
- Why was a structure accepted?
- Why was a structure rejected?
- How are partial or malformed candidates repaired?

Rules:

- Candidates are not final structures.
- Accepted structures must cite evidence, invariant checks, or policy.
- Rejected structures must leave a reason record.
- Repair must preserve lineage.
- Formation must not rely on external framework assumptions.
- Formation must not perform boundary IO.

Typical contents:

```text
candidate.py
candidate_set.py
candidate_reason.py
selector.py
selection_policy.py
rejection.py
assembler.py
repair.py
reconciliation.py
```

The existence of a convenient framework object is not a valid reason to admit a structure.

---

### 5. `operation/`

The `operation/` layer performs lawful work on admitted structures.

It answers:

- What can the system do?
- Which commands are valid?
- Which transitions are allowed?
- What state changes occurred?
- Which invariants were preserved?
- What result should be handed to projection?

Rules:

- Operations must preserve invariants.
- Operations should be explicit transitions.
- State changes must be inspectable.
- Operations may depend on boundary ports, but not concrete adapters.
- Operations must not let projections define internal truth.
- Operations should be use-case shaped, not framework shaped.

Typical contents:

```text
command.py
transition.py
transition_result.py
transition_policy.py
system_state.py
state_view.py
operation_service.py
```

Use `operation_service.py` only when it describes a real operation boundary. Do not create services by default.

---

### 6. `projection/`

The `projection/` layer renders internal results into useful views.

It answers:

- What should external users or machines see?
- What schema is promised?
- What was simplified?
- What was omitted?
- What view is stable enough to version?
- How does this projection map back to internal structures?

Rules:

- Projection does not define internal truth.
- Projection must be versioned when public.
- Projection may simplify, but it must not lie.
- Projection must declare lossy omissions when applicable.
- Projection should preserve lineage where relevant.
- Projection should not import concrete boundary adapters.

Typical contents:

```text
view_model.py
rendered_view.py
export_plan.py
export_result.py
public_schema.py
schema_version.py
```

Examples:

```text
json_response_view
markdown_report_view
audit_view
summary_view
search_index_view
cli_table_view
api_contract_view
```

---

### 7. `boundary/`

The `boundary/` layer handles external contact.

It contains ports, adapters, presentation, storage, network clients, framework code, telemetry sinks, file IO, and API/CLI entrypoints.

It answers:

- How does external material enter?
- How do external users invoke the system?
- How are internal projections exported?
- How are framework errors translated?
- Which concrete tools implement abstract capabilities?

Rules:

- Boundary code may translate.
- Boundary code may not define native concepts.
- Boundary code may not own internal identity.
- Boundary code may not leak provider assumptions inward.
- Boundary code must convert external failures into internal error types.
- Concrete adapters must implement explicit ports.
- Presentation handlers must stay thin.

Typical contents:

```text
ports/source_loader.py
ports/artifact_writer.py
ports/clock.py
ports/id_provider.py
ports/telemetry_sink.py

adapters/filesystem/
adapters/http/
adapters/sqlite/
adapters/telemetry/

presentation/cli/
presentation/api/
```

---

### 8. `policy/`

The `policy/` layer declares development-time and architecture-time rules.

It answers:

- What names are allowed?
- What dependencies are allowed?
- What contracts must exist?
- What requires an ADR?
- What is banned until justified?
- What must CI enforce?

Rules:

- Policy should be explicit.
- Policy should be enforceable where practical.
- Policy should prefer native system language over imported architecture language.
- Policy should not hide uncertainty behind generic terms.
- Policy should require ADRs for major structural decisions.

Typical contents:

```text
architecture_policy.py
naming_policy.py
dependency_policy.py
public_contract_policy.py
```

---

### 9. `shared/`

The `shared/` layer contains small primitives that have no domain authority.

It answers:

- What tiny utilities are needed across layers?
- Which generic errors or result types are shared?
- Which typing helpers reduce repetition?

Rules:

- No business rules.
- No native concept ownership.
- No imports from project-specific layers.
- Keep small.
- Split aggressively if it starts accumulating meaning.

Typical contents:

```text
errors.py
result.py
ids.py
typing.py
```

---

## Dependency Direction

Allowed dependency flow:

```text
boundary      → operation, projection, shared
projection    → operation, invariant, source, shared
operation     → formation, invariant, source, boundary.ports, shared
formation     → observation, invariant, source, shared
invariant     → source, shared
observation   → source, shared
source        → shared
policy        → shared
shared        → nothing project-specific
```

Forbidden dependency flow:

```text
source        → observation / invariant / formation / operation / projection / boundary
observation   → formation / operation / projection / boundary
invariant     → formation / operation / projection / boundary
formation     → operation / projection / boundary
operation     → boundary.adapters / boundary.presentation
projection    → boundary.adapters / boundary.presentation
boundary.adapters → boundary.presentation
```

Boundary ports may be imported inward only where an operation must request an external capability. Concrete adapters must never be imported inward.

---

## Import-Linter Example

```ini
[importlinter]
root_package = eba_app

[importlinter:contract:layered]
name = EBA layered dependency direction
type = layers
layers =
    eba_app.boundary.presentation
    eba_app.boundary.adapters
    eba_app.operation
    eba_app.projection
    eba_app.formation
    eba_app.invariant
    eba_app.observation
    eba_app.source
    eba_app.shared

[importlinter:contract:forbidden_adapters_inward]
name = Concrete boundary adapters cannot be imported inward
type = forbidden
source_modules =
    eba_app.source
    eba_app.observation
    eba_app.invariant
    eba_app.formation
    eba_app.operation
    eba_app.projection
forbidden_modules =
    eba_app.boundary.adapters
    eba_app.boundary.presentation
```

Adjust this to match the exact package structure. Import-linter layer syntax can be strict, so validate it in CI.

---

## Admission Path

Every major internal concept must have an admission path.

```text
source evidence
  → observation
  → invariant pressure
  → candidate structure
  → accepted operation
  → projected view
  → boundary use
```

A concept that skips this path should be treated as suspicious until justified.

Example:

```text
raw source span
  → observations attached to that span
  → invariants checked against identity and coverage
  → candidate internal structure
  → accepted transition
  → versioned projection
  → exported artifact
```

Bad admission:

```text
The framework expects a controller, so we create one.
The database wants a repository, so we make repository the system language.
The API shape is convenient, so it becomes the internal model.
```

---

## Naming Policy

EBA uses naming discipline to prevent vague architecture from hiding uncertainty.

### Preferred Early Names

Use these when the structure is still being discovered:

```text
record
span
identity
lineage
provenance
observation
evidence
confidence
invariant
check
violation
candidate
selection
rejection
reason
assembly
repair
reconciliation
transition
policy
state
projection
view
schema
boundary
port
adapter
ledger
report
```

### Names That Require Care

Do not use these names by default:

```text
manager
controller
service
processor
handler
engine
orchestrator
repository
factory
pipeline
workflow
task
job
agent
worker
runtime
kernel
```

These names are not forbidden, but they require justification.

Use them only when:

- The concept is stable.
- The responsibility is narrow.
- The name does not hide uncertainty.
- There is no more precise native name.
- An ADR explains why the name is correct.

### Banned Patterns

Avoid:

```text
misc.py
utils.py
helpers.py
common.py
stuff.py
processor.py
manager.py
service.py
thing.py
```

If a file feels like `utils.py`, split it by actual responsibility.

---

## Governance Plane

EBA should include a governance plane that enforces architecture, naming, tests, and public contracts.

Recommended files:

```text
governance/
├─ tools/
│  ├─ enforce_imports.py
│  ├─ enforce_file_size.py
│  ├─ enforce_native_names.py
│  ├─ enforce_invariant_ledger.py
│  ├─ enforce_boundary_purity.py
│  └─ enforce_projection_contracts.py
├─ policies/
│  ├─ architecture_contracts.md
│  ├─ naming_policy.md
│  ├─ invariant_policy.md
│  ├─ admission_policy.md
│  ├─ boundary_policy.md
│  ├─ projection_policy.md
│  ├─ testing_policy.md
│  └─ documentation_policy.md
└─ ci/
   └─ quality-gates.yaml
```

Recommended quality gates:

```text
1. File size limit enforced.
2. Import direction enforced.
3. Public outputs schema-versioned.
4. Every invariant has tests.
5. Every accepted structure preserves lineage.
6. Every rejected candidate records a reason.
7. Every adapter has a port contract test.
8. Every architecture-level noun appears in SYSTEM_LANGUAGE.md.
9. No banned vague names without an ADR.
10. No irreversible transformation without explicit lossy mode.
11. Boundary adapters are not imported inward.
12. Projection contracts are validated in CI.
```

---

## Documentation Requirements

Recommended docs:

```text
docs/
├─ ARCHITECTURE.md
├─ SYSTEM_LANGUAGE.md
├─ INVARIANTS.md
├─ BOUNDARIES.md
├─ PROJECTIONS.md
├─ DECISION_LEDGER.md
└─ ADRs/
```

### `ARCHITECTURE.md`

Explains how this specific project applies EBA.

Must include:

- Layer map
- Dependency rules
- Boundary rules
- Key concepts
- Public outputs
- Testing strategy

### `SYSTEM_LANGUAGE.md`

Defines native project vocabulary.

Must include:

- Accepted nouns
- Rejected nouns
- Terms requiring ADRs
- Boundary-only terms
- Projection-only terms
- Deprecated terms

### `INVARIANTS.md`

Lists rules that must remain true.

Must include:

- Invariant name
- Description
- Enforcement location
- Test location
- Violation behavior

### `BOUNDARIES.md`

Explains external contact.

Must include:

- Ports
- Adapters
- Error translation
- External assumptions
- Security constraints

### `PROJECTIONS.md`

Explains public views.

Must include:

- Schema versions
- Lossy vs lossless projections
- Omitted fields
- Compatibility rules
- Deprecation policy

### `DECISION_LEDGER.md`

Records architectural admissions and rejections.

Must include:

- Decision
- Evidence
- Alternatives rejected
- Invariants involved
- Consequences
- Review date if uncertain

---

## Testing Strategy

EBA uses normal tests plus contradiction tests.

```text
tests/
├─ unit/
├─ contract/
├─ contradiction/
├─ integration/
└─ e2e/
```

### Unit Tests

Test pure source, observation, invariant, formation, operation, and projection logic.

### Contract Tests

Test all boundary ports and public schemas.

Every adapter must pass the same contract suite for its port.

### Contradiction Tests

Test deformation and false structure.

They ask:

- Can the system detect false structure?
- Can it refuse malformed input?
- Can it preserve identity under transformation?
- Can it reject tempting but invalid candidates?
- Can it report uncertainty instead of pretending?
- Can it prevent boundary assumptions from becoming internal truth?

### Integration Tests

Test concrete adapters against real or simulated external systems.

### E2E Tests

Test full CLI/API flows and public contracts.

---

## Architecture Review Checklist

Use this checklist before merging major changes.

```text
[ ] Does the change preserve source identity and lineage?
[ ] Are observations separated from decisions?
[ ] Are new invariants explicit and tested?
[ ] Does any new structure have an admission path?
[ ] Are rejected alternatives recorded when relevant?
[ ] Does the change avoid vague names like manager/service/processor?
[ ] Are boundary adapters kept out of internal layers?
[ ] Are public projections versioned?
[ ] Does the change avoid framework-driven internal concepts?
[ ] Are contradiction tests added for false positives or malformed cases?
[ ] Are docs updated when system language changes?
[ ] Is an ADR added for major structural decisions?
```

---

## ADR Template

```markdown
# ADR-0000: Title

## Status

Proposed | Accepted | Superseded | Rejected

## Context

What pressure, evidence, contradiction, or requirement led to this decision?

## Decision

What structure, rule, name, dependency, or behavior is being admitted?

## Evidence

What observations, tests, failures, use cases, or invariants support this?

## Alternatives Considered

What was rejected and why?

## Consequences

What becomes easier?
What becomes harder?
What must be monitored?

## Review Trigger

When should this be revisited?
```

---

## Invariant Record Template

```markdown
# Invariant: Name

## Statement

A precise statement of what must remain true.

## Scope

Where this invariant applies.

## Rationale

Why the system requires this.

## Enforcement

Code, tests, governance tools, or review gates that enforce it.

## Violation Behavior

What happens when this invariant fails?

## Test Coverage

Where the invariant is tested.

## Related Decisions

Links to ADRs or decision ledger entries.
```

---

## Candidate Rejection Record Template

```markdown
# Rejection: Name

## Candidate

What structure, boundary, name, operation, or projection was considered?

## Reason For Rejection

Why it was not admitted.

## Evidence

What observations, tests, contradictions, or invariants caused rejection?

## Reconsideration Trigger

What would need to change before reconsidering it?
```

---

## Boundary Port Template

```python
from typing import Protocol


class SourceLoader(Protocol):
    """Boundary port for loading source material into the system."""

    def load(self, location: str) -> bytes:
        """Load source bytes from an external location."""
        ...
```

Rules:

- The port defines capability, not provider behavior.
- The port should use system-native input and output types.
- Provider-specific options belong in adapters or config.
- Provider errors must be translated into system errors.

---

## Public Projection Template

```python
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class PublicProjection:
    """Versioned public view of an internal result."""

    schema_version: str
    projection_kind: str
    data: dict[str, Any]
    omitted: list[str]
    warnings: list[str]
```

Rules:

- Every public projection has a schema version.
- Omitted fields must be explicit when relevant.
- Warnings should be machine-readable where practical.
- Projection must not expose unstable internal structures accidentally.

---

## Minimal Implementation Order

For a new EBA project, implement in this order:

```text
1. Create source identity and lineage primitives.
2. Create observation and evidence primitives.
3. Write the first invariants.
4. Add candidate structures.
5. Add selection, rejection, and repair records.
6. Add one lawful operation.
7. Add one projection.
8. Add boundary ports.
9. Add one CLI or API boundary.
10. Add concrete adapters.
11. Add governance checks.
12. Add contradiction fixtures.
13. Add docs and ADRs.
```

This prevents the project from starting at the boundary and letting the framework define the system.

---

## Comparison To Other Architectures

### Versus Layered Architecture

Layered architecture organizes by technical responsibility.

EBA organizes by admission of structure.

### Versus Hexagonal Architecture

Hexagonal architecture protects domain logic from external systems.

EBA does that too, but also separates source, observation, invariant, formation, operation, and projection before the boundary.

### Versus Clean Architecture

Clean Architecture emphasizes dependency direction and use cases.

EBA emphasizes how internal concepts become legitimate before they become use cases.

### Versus Event-Driven Architecture

Event-driven architecture organizes around events and handlers.

EBA only admits events if the system's material and invariants justify event semantics.

### Versus MVC

MVC organizes user-facing applications.

EBA treats UI and API as boundary projections, not internal truth.

---

## Anti-Patterns

### 1. Framework-First Architecture

Starting with framework folders before the native system language exists.

```text
controllers/
services/
repositories/
models/
```

### 2. Service Blob

Putting all uncertain logic into a `service.py` file.

### 3. Premature Repository

Creating repositories before persistence semantics are known.

### 4. Observation Mutation

Letting observation code change source state.

### 5. Projection Authority

Letting API response shape define internal models.

### 6. Boundary Leakage

Letting provider assumptions enter internal structures.

### 7. Invisible Rejection

Discarding failed candidates without recording why.

### 8. Unversioned Output

Exposing public machine-readable output without schema versioning.

### 9. Generic Naming Fog

Using manager, processor, handler, engine, service, or utility names because the true responsibility is unclear.

### 10. Loss Without Declaration

Dropping, normalizing, compressing, or simplifying material without trace or explicit lossy mode.

---

## File Size And Directory Hygiene

Recommended defaults:

```text
Maximum file size: 500 LOC
Preferred directory size: 10 code files or fewer
One primary concept per file
Router files allowed only to preserve import ergonomics
```

If a file exceeds the limit:

1. Identify separate responsibilities.
2. Split into a directory named after the original module.
3. Move responsibilities into focused files.
4. Replace the original file with a thin router if needed.
5. Add or update tests.

---

## Public Contract Rules

Every public CLI, API, export, report, or machine-readable artifact must define:

```text
schema_version
projection_kind
source lineage where applicable
warnings
omissions where applicable
error envelope
compatibility policy
```

Breaking changes require:

```text
schema version bump
migration note
test update
documentation update
ADR or decision ledger entry
```

---

## Boundary Rules

Boundary code includes:

```text
CLI
API
UI
filesystem
database
HTTP clients
message queues
object storage
telemetry systems
LLM providers
embedding providers
third-party SDKs
framework glue
```

Boundary code may:

```text
parse external input
validate boundary-level request shape
call operations
render projections
write artifacts
translate provider errors
manage external resources
```

Boundary code may not:

```text
define internal identity
own invariants
mutate source records outside admitted operations
define projection truth
skip ports for external capabilities
leak provider models inward
```

---

## EBA Summary

Emergence Based Architecture is strict, but not rigid.

It does not reject structure. It requires structure to be earned.

It does not reject frameworks. It confines them to boundaries.

It does not reject services, repositories, controllers, pipelines, or workers. It refuses to let those names appear before the system has revealed that they are actually the right names.

The architecture succeeds when the codebase reads as if it was discovered from the problem itself, not stamped from a generic template.
