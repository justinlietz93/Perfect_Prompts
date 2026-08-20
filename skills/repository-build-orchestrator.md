---
name: repository-build-orchestrator
description: >-
  Plan, decompose, prompt, implement, and verify multi-file software repositories in a
  dependency-ordered sequence. Use for new repositories, major subsystem builds, or
  large multi-file rebuilds where architecture must be resolved before code is written.
  The workflow materializes repository intent into a project plan, a TODO execution
  ledger, a directory skeleton, per-folder/file contracts, per-file implementation
  prompts, and test-gated implementation units.
---

# Repository Build Orchestrator

Use this skill to build a repository systematically with the filesystem as persistent execution state.

The required pipeline is:

```text
USER REQUEST
    ↓
REPOSITORY + ARCHITECTURE PLAN
    ↓
TODO EXECUTION LEDGER
    ↓
EMPTY DIRECTORY SKELETON
    ↓
FOLDER + FILE CONTRACTS
    ↓
DEPENDENCY GRAPH / BUILD ORDER
    ↓
PROMPT-ONLY FILE STUBS
    ↓
PROMPT COMPLETENESS GATE
    ↓
DEPENDENCY-ORDERED IMPLEMENTATION
    ↓
PER-FILE TEST + INTEGRATION-TEST UPDATE
    ↓
VERIFICATION GATE
    ↓
NEXT FILE
```

The central rule is: **resolve architecture before implementation, and resolve each file's contract before writing its code.**

The repository, not the conversation, is the durable source of build state.

## When to use

Use this workflow when the task involves:

- creating a new multi-file repository;
- building a substantial subsystem with multiple interacting files;
- rebuilding or reorganizing a repository from a specification;
- handing a large implementation across multiple LLM/agent sessions;
- preventing architecture drift during long code-generation tasks;
- requiring every file to be individually specified, implemented, and tested.

Do not use the full workflow for a trivial one-file edit unless the user explicitly requests it.

# Non-negotiable invariants

1. **Do not begin production implementation during the planning or prompt-generation passes.**
2. **Write the repository/architecture plan before creating the project structure.**
3. **Write the TODO ledger from the plan before creating the project structure.**
4. **Create the directory skeleton before creating planned source files.**
5. **The first directory pass creates named folders/subfolders only. They remain empty.** Do not add placeholder files merely to make directories visible unless the environment requires it and the user authorizes it.
6. **Every planned folder and subfolder must have an explicit architectural responsibility.**
7. **Every planned file must have a defined role, dependencies, imports, exports/interfaces, integration points, test responsibility, and acceptance criteria before implementation begins.**
8. **Every planned implementation file must receive a complete implementation prompt before any production file is implemented.**
9. **Implementation order is dependency-derived: fewest unresolved dependencies first, most dependent files later.**
10. **A new file is not complete without an accommodating test or executable validation appropriate to that artifact.**
11. **The repository integration tests must be updated as each new file becomes part of the implemented system.**
12. **Do not mark a TODO item complete until its local tests and the relevant integration gate pass.**
13. **Do not duplicate existing architecture.** In an existing repository, inspect ownership and reusable mechanisms before introducing parallel machinery.
14. **Do not silently change the plan during implementation.** If implementation exposes an architectural defect, update the plan and TODO explicitly, regenerate affected file contracts/prompts, then resume.
15. **Keep prompts in implemented source files when the file format supports comments.** They are persistent implementation contracts and architectural provenance.

# Required durable artifacts

Unless the repository already has authoritative equivalents, create these files at the repository root:

- `PROJECT_PLAN.md` — architecture, boundaries, directory contracts, file contracts, dependency structure, system-wide invariants, testing strategy, and acceptance gates.
- `BUILD_TODO.md` — ordered execution ledger and current build state.

If equivalent project files already exist, extend them instead of creating duplicate authorities.

The TODO is the scheduling/state artifact. The plan is the architectural authority. Per-file prompts are local implementation contracts.

# Phase 0 — Establish ground truth

Before planning:

1. Read the user's complete request and extract explicit requirements, constraints, technologies, interfaces, quality expectations, and forbidden behavior.
2. If this is an existing repository, inspect the relevant repository architecture, documentation, code, tests, configuration, dependency manifests, and current state before proposing changes.
3. Identify what already exists, what is incomplete, what is reusable, and which subsystem owns each requested behavior.
4. Preserve established behavior unless the request requires changing it.
5. Record unresolved architectural questions in the plan. Resolve them from available evidence when possible rather than inventing local assumptions later.

Do not start coding here.

# Phase 1 — Write the repository and architecture plan

Create or update `PROJECT_PLAN.md` from the request before creating implementation files.

The initial plan must define at minimum:

## 1. Goal

- what the repository/system is for;
- what successful completion means;
- intended users or callers;
- runtime/deployment environment when relevant.

## 2. System boundaries

- what belongs inside this repository;
- what remains external;
- major interfaces to external systems;
- explicit non-goals when needed to prevent scope leakage.

## 3. Architectural decomposition

Define the major layers/subsystems and why each exists.

For each subsystem describe:

- responsibility;
- inputs;
- outputs;
- state owned;
- interfaces exposed;
- dependencies allowed;
- dependencies forbidden or intentionally avoided;
- lifecycle and control flow;
- error/failure responsibilities;
- performance/concurrency/security constraints when relevant.

## 4. Repository tree plan

Write the intended directory/subdirectory tree before creating it.

Example:

```text
project/
├── src/
│   ├── core/
│   ├── adapters/
│   └── services/
├── tests/
│   ├── unit/
│   └── integration/
├── scripts/
└── docs/
```

At this stage directories may be named without a complete per-file inventory. The goal is to make the structural decomposition explicit first.

## 5. Testing architecture

Define:

- unit/contract test location and conventions;
- integration-test location and conventions;
- full repository gate;
- fixtures/mocks/test utilities;
- negative controls and failure-path testing where relevant;
- platform-specific tests where relevant;
- performance/regression gates where relevant.

Every implementation file must eventually map to a concrete local validation and to integration coverage where it participates in an integrated path.

# Phase 2 — Convert the plan into `BUILD_TODO.md`

Create a TODO ledger directly from the architecture plan.

The ledger must include the structural passes as well as the implementation work. Do not make it only a list of code files.

Recommended top-level form:

```markdown
# Build TODO

## Phase A — Architecture
- [x] Write initial repository/architecture plan
- [ ] Create empty directory skeleton
- [ ] Define every directory contract
- [ ] Define complete planned file inventory
- [ ] Resolve dependency graph
- [ ] Write every per-file implementation prompt
- [ ] Pass prompt completeness gate

## Phase B — Implementation
- [ ] 001 `src/core/types.py`
  - Dependencies: none
  - Test: `tests/unit/core/test_types.py`
  - Integration impact: `tests/integration/test_core_flow.py`
  - [ ] implementation
  - [ ] accommodating test implemented
  - [ ] local tests pass
  - [ ] integration test updated
  - [ ] integration gate passes

- [ ] 002 `src/core/parser.py`
  - Dependencies: `src/core/types.py`
  - Test: `tests/unit/core/test_parser.py`
  - Integration impact: `tests/integration/test_core_flow.py`
  - [ ] implementation
  - [ ] accommodating test implemented
  - [ ] local tests pass
  - [ ] integration test updated
  - [ ] integration gate passes
```

The TODO must eventually record for each file:

- stable ordinal/build ID;
- exact path;
- artifact type;
- direct internal dependencies;
- external dependencies if material;
- corresponding test/validation file;
- integration-test suites affected;
- prompt status;
- implementation status;
- local test status;
- integration status.

Do not mark a parent item complete while any required sub-gate remains incomplete.

# Phase 3 — Create the empty directory skeleton

Using `PROJECT_PLAN.md` and `BUILD_TODO.md`, create **only the named directories and subdirectories**.

Rules:

1. Match the planned tree exactly.
2. Do not write production code.
3. Do not create planned source files yet.
4. Do not add speculative folders not justified by the architecture.
5. If directory creation exposes a structural inconsistency, repair the plan and TODO before proceeding.

After creation, compare the actual directory tree against the planned tree and correct drift.

# Phase 4 — Deepen the architecture into folder and file contracts

Now revisit the request, `PROJECT_PLAN.md`, `BUILD_TODO.md`, and the directory skeleton.

## 4A. Define every folder/subfolder contract

For every directory, add a directory-contract section to `PROJECT_PLAN.md` containing:

```markdown
### `src/core/`

**Purpose:**
What architectural responsibility this directory owns.

**Belongs here:**
Kinds of files and behavior that are valid here.

**Does not belong here:**
Responsibilities owned elsewhere.

**Allowed dependencies:**
Which internal layers/packages this directory may depend on.

**Dependents:**
Which higher-level layers are expected to consume it.

**Testing responsibility:**
How behavior from this directory is verified.
```

Do this for nested directories too. A directory must not exist merely because it is conventional.

## 4B. Expand the complete file inventory

For each planned directory, enumerate the files required to fulfill its contract.

For every file, define a file contract in `PROJECT_PLAN.md` before creating the file.

Each file contract must include:

- exact path;
- purpose;
- architectural owner/layer;
- why the file exists as a distinct unit;
- responsibilities;
- explicit non-responsibilities;
- public API or exports;
- internal imports/dependencies;
- external imports/dependencies;
- types/data structures owned;
- important invariants;
- expected control/data flow;
- callers/dependents;
- configuration/state used;
- error semantics;
- performance/concurrency/security constraints where relevant;
- accommodating test path and test strategy;
- integration test(s) that must change when the file is implemented;
- completion/acceptance criteria.

Do not merely list filenames. Resolve enough architecture that implementation no longer needs to invent the file's role.

# Phase 5 — Build and validate the dependency graph

Construct the dependency graph from the file contracts.

For every planned file, identify its direct internal dependencies.

Then derive implementation order using topological ordering.

## Ordering rule

Prefer files with:

1. zero unresolved internal dependencies;
2. then the fewest direct dependencies;
3. then the fewest transitive dependencies;
4. then the lower architectural layer/foundation role;
5. then the stable TODO ordinal as the final deterministic tie-breaker.

A file may depend on already-existing external libraries without moving later merely because those external dependencies are numerous. The build order is primarily about unresolved dependencies inside the repository.

## Cycles

If the planned file graph contains a dependency cycle:

1. do not code around the cycle;
2. identify whether the cycle is intentional or evidence of poor decomposition;
3. extract a shared protocol/type/interface/lower-level primitive when appropriate;
4. update the plan and TODO;
5. recompute ordering.

The TODO's implementation section must be rewritten into the resolved dependency order.

# Phase 6 — Create prompt-only file stubs

After the complete file inventory and dependency order are resolved, create the planned files as **prompt-only stubs**.

Do not implement production behavior yet.

Each implementation file gets a high-quality implementation prompt at the top using the target language's normal comment/doc-comment syntax.

Examples:

Python:

```python
"""
IMPLEMENTATION PROMPT
...
"""
```

Rust/TypeScript/Java/C/C++:

```text
/*
IMPLEMENTATION PROMPT
...
*/
```

Shell/YAML/TOML and other line-comment formats should use their native comment syntax.

If the final artifact format does not legally support comments, such as strict JSON or a binary/generated file, do not corrupt the target format. Store the contract in an adjacent `<filename>.prompt.md` sidecar and record that exception explicitly in `BUILD_TODO.md`.

## Required per-file prompt schema

Every implementation prompt must be sufficiently complete that a fresh capable LLM can implement the file without having to invent architecture.

Use this structure, adapting terminology to the language/project:

```text
IMPLEMENTATION PROMPT

Path:
<exact repository path>

Architectural role:
<which subsystem/layer owns this file and why>

Objective:
<what this file must accomplish>

Context:
<relevant system behavior and how this file participates>

Prerequisites / internal dependencies:
<exact files/interfaces that must already exist>

Allowed external dependencies:
<libraries/runtime facilities it may import/use>

Required imports:
<known imports and why they are needed>

Public API / exports:
<classes, functions, traits, interfaces, commands, schemas, constants, etc.>

Owned state / data structures:
<state and representations this file owns>

Required behavior:
<complete behavioral requirements, ordered where useful>

Invariants:
<properties that must always remain true>

Integration points:
<who calls this file, what it calls, protocols/contracts crossed>

Error and edge-case behavior:
<failure semantics, validation, malformed inputs, boundary cases>

Performance / concurrency / resource constraints:
<only constraints actually required by the project>

Security / safety constraints:
<when applicable>

Non-responsibilities:
<nearby behavior that belongs elsewhere, preventing scope creep/duplication>

Accommodating test:
<exact test path and the behaviors/negative controls it must verify>

Integration-test update:
<exact integration suite(s) or scenario(s) that must be extended when this file is implemented>

Acceptance criteria:
<objective conditions for considering this file complete>

Implementation guidance:
<language/project conventions and any important existing examples to reuse>
```

## Prompt quality rules

A good per-file prompt:

- is specific to that file, not generic boilerplate;
- reflects the whole repository architecture;
- names exact dependencies and interfaces where they are already resolved;
- does not hide architectural decisions inside vague phrases such as "as appropriate" when the plan can resolve them;
- prevents the file from taking responsibility owned elsewhere;
- specifies observable behavior rather than merely naming implementation techniques;
- includes failure paths and boundary behavior;
- specifies how the file will be tested;
- tells the implementer what integration coverage must change;
- does not pre-write the production code unless a literal interface/signature is already part of the architecture;
- preserves user constraints and existing repository conventions.

# Phase 7 — Create prompt-only test stubs

Every planned implementation file must have an accommodating test or executable validation planned before implementation.

Create its test file as a prompt-only stub during the prompt pass when the test does not already exist.

Its prompt must specify:

- source file under test;
- behavior/invariants to exercise;
- positive cases;
- boundary cases;
- negative/failure cases;
- relevant fixtures/mocks/fakes;
- regression cases implied by the request;
- expected integration with the repository test harness;
- pass/fail criteria.

For non-code artifacts, use the strongest appropriate executable validation rather than pretending every artifact has conventional unit-test semantics. Examples:

- config file → parser/schema/config-loading test;
- migration → migration/apply/rollback test;
- CLI script → subprocess/exit-code/output test;
- build file → build/configuration validation;
- documentation that participates in generated docs → docs build/link/example validation;
- static schema → schema validation and compatibility test.

The rule remains: every new repository artifact must have a concrete way to prove it is valid and integrated.

# Phase 8 — Prompt completeness gate

**Do not begin production implementation until this gate passes.**

Verify all of the following:

- [ ] `PROJECT_PLAN.md` reflects the complete requested architecture.
- [ ] `BUILD_TODO.md` contains the complete planned file inventory.
- [ ] actual directory skeleton matches the plan.
- [ ] every directory has a responsibility contract.
- [ ] every file has a file contract.
- [ ] every file's direct internal dependencies are known.
- [ ] dependency graph is acyclic or intentionally resolved.
- [ ] implementation TODO is topologically/dependency ordered.
- [ ] every implementation file has a prompt-only stub or documented sidecar prompt.
- [ ] every new file has an accommodating test/validation mapped to it.
- [ ] every new test file has its own prompt if it must be created.
- [ ] integration-test impact is specified for every integrated production file.
- [ ] no production behavior has accidentally been implemented during the prompt pass.

If any item fails, remain in the planning/prompt phase and repair it.

# Phase 9 — Dependency-ordered implementation

After the prompt completeness gate passes, begin actual implementation from the first dependency-ready TODO item.

Treat each source file and its verification changes as one atomic build unit.

For each TODO item:

## 9A. Reload context

Before editing, read:

1. the relevant sections of `PROJECT_PLAN.md`;
2. the current item and dependency metadata in `BUILD_TODO.md`;
3. the target file's implementation prompt;
4. the target test file's prompt or existing test context;
5. every direct internal dependency that defines interfaces used by this file;
6. relevant integration tests;
7. existing code that establishes conventions or reusable mechanisms.

Do not implement from the per-file prompt in isolation if surrounding architecture has changed.

## 9B. Verify readiness

Confirm:

- all internal dependencies are implemented and passing their gates;
- required interfaces actually match the prompt assumptions;
- no newer repository state invalidates the planned contract.

If a mismatch exists, update the plan/TODO/prompts first rather than locally improvising incompatible architecture.

## 9C. Implement the production file

Implement the target file according to:

1. the current user request;
2. the project plan;
3. the TODO contract/order;
4. the per-file prompt;
5. established dependency interfaces;
6. repository engineering conventions.

The plan has higher authority than stale local prompt wording. If they conflict, reconcile the artifacts explicitly.

Keep the implementation prompt in the file when the format supports it unless the user asks for it to be removed.

## 9D. Implement/update the accommodating test

In the same work unit:

- create or complete the mapped test file;
- cover the required positive behavior;
- cover meaningful boundaries;
- cover specified failure/negative behavior;
- verify important invariants;
- avoid tests that merely mirror implementation internals without validating behavior.

A production file without its accommodating test is an incomplete TODO item.

## 9E. Update integration tests immediately

Do not defer integration coverage until the end of the repository build.

For every newly implemented production file that participates in an integrated system path:

1. identify the comprehensive integration suite(s) listed in its contract;
2. extend those tests so the new file is exercised in the real cross-file path;
3. add or update fixtures/setup as necessary;
4. preserve existing integration coverage;
5. test both the new behavior and regression of the previously working path.

This creates a monotonically expanding integration gate as the repository grows.

## 9F. Run the verification gate

At minimum run:

1. the accommodating test for the new file;
2. relevant neighboring/subsystem tests;
3. affected integration tests;
4. the repository's broader test gate when feasible and required by the project.

Also run format/lint/type/build/static checks defined by the repository.

Do not advance because code "looks right." Advance on evidence from the defined gates.

## 9G. Repair before advancing

If any gate fails:

- diagnose the actual failure;
- repair the current file/test/integration interaction;
- do not move to a more dependent TODO item;
- do not weaken a valid test merely to obtain a pass;
- if the failure reveals an architectural error, return to the plan/TODO/prompt layer and correct the affected dependency chain.

## 9H. Record completion

Only after the complete work unit passes:

- mark implementation complete;
- mark accommodating test complete;
- mark local test gate passed;
- mark integration test update complete;
- mark integration gate passed;
- optionally record completion timestamp/commit/reference when useful;
- advance to the next dependency-ready TODO item.

# Phase 10 — Integration suite grows with the repository

The integration suite is not a final-stage afterthought.

It must evolve after every production-file implementation.

Think of repository construction as:

```text
File 1 + Test 1 + Integration Δ1 → PASS
File 2 + Test 2 + Integration Δ2 → PASS
File 3 + Test 3 + Integration Δ3 → PASS
...
File N + Test N + Integration ΔN → PASS
```

This prevents the repository from accumulating locally correct files that have never been proven to compose.

When a foundational file has no meaningful standalone integration path yet, update the earliest available integration/contract harness that can exercise it, or explicitly record the deferred integration edge and the exact dependent TODO item that must activate it. Do not silently omit integration responsibility.

# Phase 11 — Final repository gate

After all implementation TODO items are complete:

1. verify the actual repository tree against `PROJECT_PLAN.md`;
2. verify every planned file exists;
3. verify no unplanned duplicate subsystem was introduced;
4. verify TODO dependencies and completion state are accurate;
5. run the full unit/contract test suite;
6. run the complete integration suite;
7. run build/type/lint/static/security/performance gates required by the project;
8. inspect failures and warnings rather than reporting completion from exit code alone;
9. update plan/TODO documentation to match final reality;
10. leave no item marked complete unless its claimed evidence exists.

Completion means the implemented repository, its tests, its integration behavior, and its durable planning artifacts agree with one another.

# Existing-repository adaptation

When this workflow is used on an existing repository, do **not** recreate the repository as if it were blank.

Instead:

1. reconstruct the current architecture first;
2. map existing files/folders into the plan;
3. identify only the new or changed artifacts required by the request;
4. preserve validated existing behavior;
5. use existing tests and integration suites as the baseline;
6. create prompts only for files being added or materially rebuilt unless the user asks for complete repository re-specification;
7. dependency-order the changed work against both existing and new dependencies.

# TODO state model

A useful explicit state model for each implementation node is:

```text
PLANNED
  ↓
CONTRACTED
  ↓
PROMPTED
  ↓
DEPENDENCIES READY
  ↓
IMPLEMENTED
  ↓
LOCAL TEST PASS
  ↓
INTEGRATION UPDATED
  ↓
INTEGRATION PASS
  ↓
COMPLETE
```

Never skip from `PLANNED` directly to `IMPLEMENTED`.

# Session handoff / resumability

This workflow should survive loss of conversation context.

At any point, a new agent should be able to recover state by reading, in order:

1. user/request specification if persisted;
2. `PROJECT_PLAN.md`;
3. `BUILD_TODO.md`;
4. target file's implementation prompt;
5. dependency files;
6. target/local tests;
7. integration suite.

The next action should be derivable from those artifacts without relying on hidden chat history.

# Progress reporting

During a long build, report concrete repository state rather than vague progress.

Useful updates include:

- architecture plan written;
- TODO generated with N planned implementation nodes;
- directory skeleton created;
- N/N directory contracts resolved;
- N/N file contracts resolved;
- dependency graph validated;
- N/N per-file prompts written;
- prompt completeness gate passed;
- current implementation node and dependencies;
- local/integration tests passed for the current node;
- remaining TODO count.

# Failure conditions

Stop advancing the implementation sequence and repair state if any of these occur:

- a file's purpose cannot be stated precisely;
- a file imports an internal dependency not represented in the plan;
- dependency order contradicts actual imports/interfaces;
- a dependency cycle appears unexpectedly;
- implementation requires inventing a new subsystem not in the architecture;
- a new file has no accommodating test/validation;
- integration coverage is being deferred without an explicit activation point;
- a test fails and the next TODO item depends on the failing artifact;
- the TODO says complete while the filesystem/tests say otherwise;
- local prompt and project plan materially disagree.

Repair the authoritative artifacts first, then continue.

# Core principle

The purpose of this skill is not merely to make an LLM write files one at a time. It is to **compile a user request into an explicit repository architecture, compile that architecture into a dependency-aware file specification graph, materialize each file specification into the filesystem, and only then execute the graph under continuously expanding tests.**

The build sequence is therefore:

```text
REQUEST
→ PLAN
→ TODO
→ DIRECTORY SKELETON
→ DIRECTORY CONTRACTS
→ FILE CONTRACTS
→ DEPENDENCY GRAPH
→ PER-FILE PROMPTS
→ PROMPT GATE
→ FILE + TEST + INTEGRATION DELTA
→ VERIFY
→ NEXT FILE
→ FULL REPOSITORY GATE
```
