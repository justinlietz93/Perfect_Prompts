# Standards-Governed Hexagonal Monolith (SGHM)

### Overview

This document defines a “Standards-Governed Hexagonal Monolith” (SGHM) template that fuses a domain-centric Ports & Adapters (Hexagonal) core with a first-class Governance & Enforcement Plane. The objective is to enable small-but-powerful CLIs and services that can scale into larger applications or be embedded behind UIs/backends without re-architecture, while automatically enforcing universal code and quality standards.

Core goals:
- Domain-centered business logic, isolated from technology
- Explicit contracts (ports) and replaceable adapters
- Governance-as-code that enforces naming, headers, docstrings, 500-LOC router rule, logging, telemetry, security, API contracts, tests, documentation, and hygiene—locally and in CI
- Clear growth path from CLI to service or UI-backed app

### EXAMPLE ONLY Project Map of an SGHM project

```text
sghm_app/
├─ pyproject.toml
├─ README.md
├─ .pre-commit-config.yaml
├─ .importlinter
├─ src/
│  └─ sghm_app/
│     ├─ presentation/                 # CLI / API / UI edges (thin)
│     │  ├─ cli/
│     │  │  ├─ app.py                  # Typer/FastAPI entrypoints (no business logic)
│     │  │  └─ routers/                # presentation routers only
│     │  └─ api/                       # (optional) REST/gRPC/GraphQL endpoints
│     ├─ application/                  # use cases (orchestration)
│     │  ├─ use_cases/                 # commands/queries
│     │  └─ handlers/                  # command/query handlers (optional)
│     ├─ domain/                       # pure domain (entities/value objects/services)
│     │  ├─ entities/
│     │  ├─ value_objects/
│     │  └─ services/
│     ├─ ports/                        # contracts (ABCs/Protocols) – no concrete code
│     │  ├─ repositories/
│     │  ├─ services/
│     │  └─ system/
│     ├─ adapters/                     # concrete implementations of ports
│     │  ├─ filesystem/
│     │  ├─ http/
│     │  ├─ cache/
│     │  └─ telemetry/
│     ├─ shared/                       # cross-cut utils (no business rules)
│     │  ├─ logging/
│     │  ├─ telemetry/
│     │  ├─ security/
│     │  └─ settings/
│     └─ config/
│        ├─ settings.py
│        └─ env/
├─ governance/                         # Governance & Enforcement Plane (policy-as-code)
│  ├─ tools/
│  │  ├─ enforce_headers.py            # require file headers
│  │  ├─ enforce_naming.py             # enforce snake_case, etc.
│  │  └─ enforce_size.py               # enforce 500-LOC + router refactor rule
│  ├─ policies/
│  │  ├─ architecture_contracts.md     # describes import rules (import-linter)
│  │  ├─ logging_policy.md
│  │  ├─ telemetry_policy.md
│  │  ├─ security_policy.md
│  │  ├─ api_contract_policy.md
│  │  ├─ testing_policy.md
│  │  └─ documentation_policy.md
│  └─ ci/
│     └─ quality-gates.yaml            # reference CI pipeline gates (coverage, lint, audit)
├─ tests/
│  ├─ unit/
│  │  ├─ domain/
│  │  └─ application/
│  ├─ contract/ports/                  # adapter contract-test suites per port
│  ├─ integration/
│  │  ├─ adapters/
│  │  └─ repositories/
│  └─ e2e/
│     ├─ cli/
│     └─ api/
└─ docs/
   ├─ ARCHITECTURE.md
   ├─ CONVENTIONS.md
   └─ ADRs/
```

### SGHM Architecture Implementation

SGHM combines Hexagonal Architecture with a codified Governance & Enforcement Plane that continuously verifies conformance to universal standards in development and CI.

#### Core Principles

- Domain-Centric Core: Business rules live in `domain/` with no technology or framework dependencies.
- Ports & Adapters: All IO and external interactions occur via `ports/` (interfaces) and `adapters/` (implementations).
- Application Orchestration: Use cases coordinate domain behavior via ports (no concrete adapter coupling).
- Composition at the Edge: Presentation wires concrete adapters to ports at startup; inner layers remain abstract.
- Governance-as-Code: Automated checks enforce:
  - File headers and complete docstrings/comments for every function/class/method/decorator
  - 500-LOC maximum per file; router refactor into subfolder if exceeded
  - Naming conventions; ≤10 code files per directory where practical
  - Structured logging, telemetry, security scanning, API contract versioning, testing, documentation, hygiene
- Progressive Scalability: Start as CLI; evolve to API/service or embed behind UI with minimal change.

#### Layer Structure

1) Presentation (Edges)
- Responsibilities: CLI commands, API endpoints, input validation, output formatting
- Dependencies: Application and Shared only
- Rules:
  - No business logic; thin handlers delegating to use cases
  - Use DTOs/response models; never expose domain entities directly
  - Provide versioned output contracts (e.g., `--schema-version`, content negotiation)

2) Application (Use Cases)
- Responsibilities: Orchestrate domain operations, transaction boundaries, mapping between DTOs and domain
- Dependencies: Domain + Ports interfaces (and Shared)
- Rules:
  - No concrete adapter imports; depend only on ports
  - Implement command/query handlers; ensure explicit error semantics

3) Domain (Core)
- Responsibilities: Entities, value objects, domain services, invariants
- Dependencies: None (pure Python, no frameworks)
- Rules:
  - No IO, no logging, no telemetry—pure logic
  - Stable language and ubiquitous nomenclature

4) Ports (Contracts)
- Responsibilities: ABCs/Protocols defining external capabilities (repositories, http, cache, clock, telemetry, llm, etc.)
- Dependencies: Domain types and Shared primitives only
- Rules:
  - Single Responsibility per port
  - Clear error contracts and idempotency semantics

5) Adapters (Implementations)
- Responsibilities: Provide technology-specific implementations of ports (filesystem, HTTP, cache, etc.)
- Dependencies: Ports + Shared (+ Domain types for mapping)
- Rules:
  - Translate provider errors to standardized port errors
  - No imports from Presentation; keep orchestration concerns out

6) Shared
- Responsibilities: Structured logging, telemetry utilities, security helpers, configuration, small utilities
- Rules:
  - No business rules; avoid circular dependencies

#### Governance & Enforcement Plane

- Import Rules (import-linter):
  - Presentation → Application → Domain, Ports
  - Application → Domain, Ports
  - Domain → (no outward imports)
  - Adapters → Ports (+ Domain types allowed for mapping), but never Presentation/Application
- Pre-commit & CI Quality Gates:
  - Formatting (Black), lint (Ruff), typing (MyPy), tests (pytest + coverage gate ≥85%), secrets (detect-secrets), SAST (bandit), dep audit (pip-audit)
  - File headers enforced; naming enforced; 500-LOC enforced with router refactor message
- Documentation:
  - Required file headers; module and public symbol docstrings
  - `docs/ARCHITECTURE.md` and `docs/CONVENTIONS.md` maintained
  - ADRs for significant decisions
- Router Rule:
  - If a file exceeds 500 LOC, create a subfolder named after the module, split responsibilities into smaller files, and replace the original with a thin “router” that imports/exports
- Directory Hygiene:
  - Prefer ≤10 code files per directory; introduce subfolders to reduce clutter
  - One class per file where practical; class name should match filename (PEP 8 style guiding)

#### Interfaces, Contracts, and API Requirements

- Purity & Placement:
  - All cross-boundary contracts defined in `ports/` (and DTOs in Application/Shared)
  - Contracts are technology-agnostic (no framework or transport coupling)
- Dependency Direction (enforced):
  - Presentation → Application → Domain/Ports; never directly to Adapters
  - Adapters implement Ports; never imported by inner layers
- Port Taxonomy (minimum set):
  - Repositories (data), Services (integration: HTTP/LLM/cache), System (clock/uuid/fs), Telemetry (span/log emitters if abstracted)
- Error, Idempotency, Retries:
  - Define domain-specific exceptions per port; map provider errors to port errors
  - Specify idempotent operations; document retry/backoff semantics
- API/CLI Contracts:
  - Public outputs versioned via `schema_version` field and/or content negotiation
  - Machine-readable schemas (OpenAPI/JSON Schema) are the source of truth
  - Standard error envelope with correlation/trace IDs

#### Dependency Flow

```
[Presentation] → [Application (Use Cases)] → [Ports (Contracts)] ← [Adapters (Impl)]
                         ↓
                     [Domain]
                         ↓
                      [Shared]
```

- Allowed directions are enforced via import-linter contracts
- Composition/wiring at Presentation (or a composition root) only

#### AI/External Service Integration Points

- All integrations implemented as adapters of ports (`ports/services/*`)
- Application decides orchestration and mapping; Domain remains independent
- Contract tests validate adapter conformance (e.g., LLM, vector store, message bus)

#### Rules for AI Agents

1. Maintain strict layer separation; never import concrete adapters into Application or Domain.
2. Define ports first; implement adapters after interface clarity is established.
3. Enforce the 500-LOC rule; apply the router refactor pattern when exceeded.
4. Prefer pure functions and immutable models in Domain; avoid side effects.
5. Centralize DTO mapping in Application; avoid leaking Domain types to Presentation.
6. Use constructor injection for all dependencies; wire them at edges only.
7. Write contract tests for each port; all adapters must pass the suite.
8. Keep logs structured; do not log secrets or PII; propagate correlation IDs.

#### Example Implementation

- CLI handler (Presentation) parses args, configures logging/telemetry, builds adapters, invokes `application.use_cases.*`
- Use case (Application) accepts port instances, orchestrates domain services, returns versioned DTO
- Adapter (Adapters) performs IO and translates errors to port-defined exceptions
- Domain code remains pure and testable with zero IO

### AI Agent Development Guidelines

Critical Rules:
1) File Size Enforcement: Never create/modify files >500 LOC; split with router if breached.
2) Dependency Direction: Enforce import rules; no inward violations.
3) Interface-First Design: Define ports in `ports/` before writing adapters.
4) Layer Isolation:
   - Presentation: request parsing, simple validation, DTO marshalling, no business logic
   - Application: orchestration, mapping, transactions
   - Domain: entities/value objects/services only
   - Adapters: IO details, provider error translation
5) Repository Pattern: Data access only through repository ports.
6) Dependency Injection: Use constructor injection; wire at composition root.
7) Framework Independence: Keep domain clean of frameworks and IO.
8) Modular Boundaries: One responsibility per module; minimize ripple effects across modules.
9) Logging/Telemetry Discipline: Structured logs; spans around use cases and adapter calls; no sensitive data in logs/spans.

Code Review Checklist:
- [ ] File size ≤500 LOC and router pattern followed if split
- [ ] Imports respect layer rules (checked by import-linter)
- [ ] All public symbols have docstrings; files have headers
- [ ] No adapter imports in Application/Domain
- [ ] DTO mapping centralized in Application
- [ ] Port errors and idempotency semantics documented and implemented
- [ ] Tests: unit (domain/application), contract (ports), integration (adapters), e2e (cli/api)
- [ ] Structured logging; telemetry spans present for critical paths
- [ ] Security scans pass; secrets not committed; dependency audits clean

### Architectural Concepts

- Hexagonal/Ports & Adapters at the core; Governance & Enforcement Plane around it
- CQRS optional at Application level for complex read/write flows
- Evented edges possible via additional ports (message bus, event store)
- Backward-compatible API evolution via schema versioning and deprecation windows

### UI/UX Strategies

- For CLI: terse help, stable flags, machine-output modes (e.g., `--format json`)
- For API: consistent pagination/filtering/error envelopes; client SDKs generated from schema
- For UI: keep controllers thin; fetch via ports or API clients generated from contracts

### Performance Strategies (Speed & Power)

- Prefer pure domain functions for hotspot logic; benchmark in isolation
- Use adapters with batching, streaming, or caching where appropriate
- Add spans and timings for critical paths; watch tail latency in CI perf checks

### Memory Optimization & Safety

- Keep domain models lean (pydantic/BaseModel or dataclasses as appropriate)
- Avoid retaining large intermediates in Presentation/Application
- Cleanup external resources in adapters; use context managers

### Logging Strategies

- Structlog JSON by default; correlation/trace IDs in each event
- Single initialization point; no ad-hoc basicConfig calls scattered
- Separate user-facing output (stdout) from diagnostic logs (stderr)

### Security Strategies

- SAST (bandit), secrets scanning (detect-secrets), dep audit (pip-audit)
- Principle of least privilege in adapters (FS paths, network scopes)
- Input validation at edges; explicit allowlists for external calls
- SBOM, license allowlists, signing/attestation (optional but recommended)

### Networking / API Strategies

- Stable, versioned contracts; include schema generation in CI
- Timeouts, retries with backoff, circuit breakers where needed (adapter side)
- Idempotency keys for non-safe operations exposed via API

### Controller / Backend Logic Strategies

- Presentation handlers exclusively orchestrate; no business rules
- Central error handling; translate to standard error envelopes
- Map DTOs in Application; never leak domain types outwards

### Data Activities & ACID Strategies

- If persistence is added, keep it in adapters; domain stays persistence-agnostic
- Unit-of-Work port for transactional boundaries (if needed)
- Optimistic concurrency controls implemented at adapter layer with clear semantics

### Database Design & Optimizations

- Choose storage technology per use case; abstract via repository ports
- Keep storage schemas outside domain; handle mapping and migrations in adapters
- Indexing, pagination, and read models can be specialized without touching core

### Source Control Strategies

- Feature branches; protected main; required reviews
- Conventional commits recommended; changelog generated from commits
- ADRs for significant decisions under `docs/ADRs/`

### CI/CD Strategies

- CI gates: lint, types, tests (unit/contract/integration/e2e), coverage ≥85%, import-linter, secrets/SAST/deps
- Optional: perf smoke tests; schema diff check requiring version bump
- Release: tag artifacts; publish schema; SBOM and attestations (optional)

### Engineering Approach: Bottom-Up & Top-Down

- Top-Down: define contracts (ports), DTOs, and use cases first
- Bottom-Up: implement domain primitives and small pure functions early for feedback
- Iterate: measure via tests and telemetry; refactor with confidence due to enforcement

### Testing Strategies

- Unit: domain and application (fast, pure); heavy coverage
- Contract: per-port suites adapters must pass (pre-merge requirement)
- Integration: adapters with real or simulated backends
- E2E: CLI/API flows; verify error envelopes and schema versions
- Performance: lightweight timings; regression thresholds to catch slowdowns

### Validation Domains & Best Combination

| Domain            | Strategy                                             | Practice                                                           |
|-------------------|------------------------------------------------------|--------------------------------------------------------------------|
| Architecture      | import-linter contracts                              | CI fails on layer violations                                       |
| Code Hygiene      | pre-commit hooks, router rule enforcement            | Mandatory headers, naming, ≤500 LOC                                |
| API Contracts     | schema gen + diff checks                             | Enforce version bumps for breaking changes                         |
| Security          | SAST + secrets + dep audit                           | Fail builds on high-severity findings                              |
| Observability     | structured logs + spans in use cases/adapters        | Correlate with trace IDs; no PII                                   |
| Testing           | unit + contract + integration + e2e + coverage gate  | ≥85% target; quarantine flaky tests responsibly                    |

---

By adopting SGHM, teams gain the clarity and testability of Hexagonal Architecture and the operational reliability of policy-as-code enforcement, ensuring that even small utilities start life production-ready and can scale gracefully into services or UI-backed applications without architectural debt.