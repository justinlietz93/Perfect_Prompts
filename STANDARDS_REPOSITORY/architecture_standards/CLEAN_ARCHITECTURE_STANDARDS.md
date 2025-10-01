### Overview

This document defines a generic full-stack app template focusing on architectural strategies:
- modular monolith with microservices decoupling layered clean architecture (presentation, application, domain, infrastructure).
- Every project must be designed first conceptually from the Top-down. Then ask:
      - "Given this end goal concept, what axiomatic primitives, data structures, algorithms, and pipelines will be required necessary and optimal to build this project as conceptually defined?"
- Top-down: Define high-level abstractions (interfaces, contracts, user stories, Questions: "what are we building?", "how will it work?", "why are we building this?", "who cares?") first.
- Bottom-up: Build from primitives (data structures, algorithms).
- Ensure extended future scalability, stability + flexibility, maintainability via loose coupling, high cohesion.

### EXAMPLE ONLY Project Map of an agentic AI project following the Hybrid Clean Architecture in Python

```go
agentic-tools/
├─ pyproject.toml
├─ README.md
├─ src/
│  ├─ ui/                       # presentation (clients only)
│  │  ├─ web/
│  │  │  ├─ adapters/           # calls api via interfaces DTOs
│  │  │  └─ state/
│  │  └─ cli/
│  │     └─ commands/
│  ├─ api/                      # presentation (server)
│  │  ├─ http/
│  │  │  ├─ controllers/
│  │  │  ├─ routers/
│  │  │  ├─ dto/
│  │  │  └─ middleware/
│  │  └─ di/                    # wire interfaces→impl at the edge
│  ├─ business_logic/           # application layer only
│  │  ├─ agents/
│  │  │  ├─ orchestrators/      # multi-agent planners
│  │  │  ├─ planners/           # task decomposition
│  │  │  ├─ tools/              # tool use protocols
│  │  │  ├─ memory/             # episodic/semantic policies (by iface)
│  │  │  └─ policies/           # safety, routing, retries
│  │  ├─ services/              # use-case services
│  │  ├─ use_cases/             # CQRS commands/queries
│  │  └─ validators/
│  ├─ domain/                   # pure models
│  │  ├─ entities/
│  │  ├─ value_objects/
│  │  └─ events/
│  ├─ interfaces/               # ports (contracts only)
│  │  ├─ repositories/          # e.g., IUserRepo, ITaskRepo
│  │  ├─ services/              # ILLM, IMessageBus, ICache, IVectorIndex
│  │  ├─ agents/                # IAgentRuntime, ITool, IMemoryStore
│  │  └─ unit_of_work.py
│  ├─ abstractions/             # shared types/base classes
│  │  ├─ dto/
│  │  ├─ errors/
│  │  ├─ result.py
│  │  └─ types.py
│  ├─ persistence/              # data plumbing (no business rules)
│  │  ├─ orm/
│  │  │  ├─ models/
│  │  │  ├─ mappers/
│  │  │  └─ migrations/
│  │  ├─ vector/
│  │  ├─ graph/
│  │  └─ connection/            # sessions, pools, UoW impl
│  ├─ repositories/             # adapters implementing repository ports
│  │  ├─ sql/
│  │  ├─ nosql/
│  │  ├─ vector/
│  │  └─ memory/
│  ├─ infrastructure/           # other adapters
│  │  ├─ llm/
│  │  ├─ message_bus/
│  │  ├─ cache/
│  │  ├─ http_clients/
│  │  └─ telemetry/
│  ├─ shared/
│  │  ├─ logging/
│  │  ├─ security/
│  │  └─ settings/
│  ├─ config/
│  │  ├─ settings.py
│  │  └─ env/
│  └─ tests/
│     ├─ unit/
│     ├─ integration/
│     └─ e2e/
└─ docs/
   └─ ADRs/
```

### Hybrid-Clean Architecture Implementation

This section documents the Hybrid-Clean Architecture approach, combining modular monolith design with Clean Architecture principles. 
This serves as a generic template for implementing scalable, maintainable applications across projects.

#### Core Principles

- **Modular Monolith**: Single deployable unit composed of multiple projects/modules for separation of concerns, enabling microservices-like decoupling without full microservices overhead.
- **Clean Architecture Layers**: Strict layering with dependency inversion to ensure testability, maintainability, and framework independence.
- **Dependency Rule**: Dependencies flow inward only; outer layers depend on inner layers via abstractions (interfaces).
- **File Size Limit**: No source code file shall exceed 500 lines of code (LOC) to maintain readability and facilitate refactoring.
- **Directory Structure**: Subfolders should be used liberally to avoid keeping dissimilar files in the same directory, maintaining <= 10 code files per directory, and staying organized by reducing clutter.
- **Classes**: There should be no more than 1 class per file, and a class should share the name of the file it's in whenever possible. As a rule of thumb, abide by PEP 8.
  Examples:
  - base_controller.py -> BaseController
  - base/controller.py -> BaseController
  - abstract_llm.py -> AbstractLLM
  - abstractions/llm.py -> AbstractLLM
  - repositories/user.py -> UserRepository
  - user_repository.py -> UserRepository

#### Layer Structure

1. **Presentation Layer** (Outer)
   - **Projects**: API/Web projects, UI/Mobile clients, Console apps
   - **Responsibilities**: HTTP/REST endpoints, real-time hubs (e.g., SignalR), UI rendering, user interaction
   - **Dependencies**: Only on Business Logic interfaces and Shared utilities
   - **Rules**:
     - Controllers/handlers are thin; delegate business logic to services/managers
     - Use DTOs for data transfer (defined in Shared projects)
     - No direct database access or business rules

2. **Application/Business Logic Layer**
   - **Projects**: Core business logic projects and their interface abstractions
   - **Responsibilities**: Domain rules, business workflows, validations, service/manager classes
   - **Dependencies**: On Domain models, Repository interfaces, external service abstractions
   - **Rules**:
     - Services/managers implement interfaces from abstraction projects
     - Use repository pattern for data access
     - Contain all business rules and validations
     - Framework-agnostic (no direct ORM/framework references)

3. **Domain Layer**
   - **Projects**: Domain model projects
   - **Responsibilities**: Plain Old CLR Objects (POCOs), domain entities, value objects
   - **Dependencies**: None (pure domain models)
   - **Rules**:
     - No business logic (anemic models)
     - Framework-independent
     - Used across all layers

4. **Infrastructure/Persistence Layer** (Inner)
   - **Projects**: Data access projects, ORM implementations
   - **Responsibilities**: ORM DbContext, entity mappings, repository implementations, migrations
   - **Dependencies**: On Domain models for entities
   - **Rules**:
     - Implement repository interfaces from Business Logic abstractions
     - Handle data persistence and ORM details
     - No business logic

5. **Shared and Abstractions**
   - **Projects**: Common utilities, cross-cutting concerns, external service abstractions
   - **Responsibilities**: Common DTOs, utilities, external API interfaces (e.g., AI, payment)
   - **Dependencies**: Minimal; used across layers
   - **Rules**:
     - Define contracts for cross-cutting concerns
     - Abstractions enable pluggable implementations

6. **Configurations and Parameters**
   - **Config**: All configurations must be in a centralized config/ folder at the root of the project.
     In the case of repositories with multiple projects, there would be a central config for each individual project within their root directories.
   - **Parameters**: Any and all static or default parameters must be kept alongside the central configurations within the config/ directory.
     This can be an individual yaml, json, or other type of file that contains all otherwise hard-coded parameter defaults or constants.
     If it is more suitable for the parameter to be an environment variable, then store it in an .env and make sure that file is in the .gitignore listing.
     
7. **Documentation and Assets**
   - **Code Documentation**: Code documentation is of first class order in this architecture.
     Every method, function, class, and file must have professional, easy to understand, readable documentation.
     Comments are helpful to explain gaps that aren't necessarily suitable for docstrings or headers.
     - **Project Documentation**: The central location for the code docs, notebooks, in depth guides, and tutorials belong within the docs/ folder at the project root.
       (some exceptions may apply, see Layer Structure / item #6 / Config / for more details on this).
       
#### Interfaces, Contracts, and API Requirements

- Contract location and purity
  - All cross-layer communication MUST occur via interfaces (ports) and DTOs defined in a dedicated contracts area that depends only on shared primitives and (optionally) domain types.
  - Contracts MUST NOT depend on frameworks, transport libraries, or infrastructure details.

- Dependency direction (enforced)
  - Presentation → Application (interfaces/DTOs) only; Presentation MUST NOT reference Domain or Infrastructure directly.
  - Application → Domain and Contracts; Application MUST NOT reference Infrastructure.
  - Infrastructure → Domain and Contracts; Infrastructure implements ports and MUST NOT be referenced by inner layers.

- Port taxonomy (minimum set)
  - Data access: Repository ports and a Unit of Work port.
  - Integration: Message Bus, Cache, HTTP Client, Secret Store, Telemetry.
  - AI/LLM: Model runtime, Tool execution, Embedding/Vector index, Memory store.
  - System: Clock, UUID/ID generator, Filesystem/Blob store.
  - Each port MUST have a single responsibility and clear error semantics.

- API surface (presentation/server)
  - The server-side API MUST expose a versioned public contract (REST/gRPC/GraphQL acceptable) with:
    - Versioning policy (e.g., URL or header) and deprecation window.
    - Standard error envelope with stable error codes and trace/correlation id.
    - Idempotency for unsafe methods where applicable (keys and replay handling).
    - Pagination, filtering, sorting conventions; consistent status codes.
    - Security: Authn/Authz requirements, rate limits, and input validation guarantees.
  - API contracts SHOULD be machine-readable (e.g., OpenAPI/Protobuf) and MUST be the single source of truth for generated clients and DTOs.

- DTO and mapping rules
  - Presentation MUST exchange DTOs, never domain entities.
  - Mapping between Domain and DTOs MUST be centralized in Application (use case layer), not scattered across Presentation/Infrastructure.
  - DTOs MUST be stable, versioned, and backward compatible within a major version.

- Error contracts and retries
  - Ports MUST define expected error types, retry semantics, and idempotency expectations.
  - Infrastructure adapters MUST translate provider-specific errors to the standardized port errors.

- Testability and compliance
  - Each port MUST ship with contract tests that any adapter MUST pass (adapter test kit).
  - Consumer-driven contracts SHOULD be used for external API integrations.
  - Mocks/fakes for ports MUST be provided to enable fast unit tests in Application.

- DI and composition root
  - Implementations are wired at the edge (composition root) only; inner layers are unaware of concrete types.
  - A default wiring profile MUST exist for local/dev; alternative profiles MAY exist for prod/staging.

- Stability and evolution
  - Contracts are treated as stable artifacts; changes follow semantic versioning.
  - Breaking contract changes MUST trigger a new major version and an explicit migration path.

- Naming and granularity
  - Interface names MUST describe capability (e.g., Repository, Service, Bus) rather than technology (e.g., Sql, Kafka) to avoid coupling.
  - Keep ports minimal; split interfaces if a capability set grows beyond a single responsibility.

- Documentation
  - Every interface and API endpoint MUST include purpose, inputs/outputs, error cases, and examples.
  - Each feature must have it's own documentation file with clear working links to related features.
  - The public API reference MUST be generated from the source of truth and included in project documentation.

- Enforcement notes
  - Static checks (imports/architecture rules) SHOULD block outer→inner violations and domain leaks to Presentation.
  - Contract test suites MUST run in CI; adapters cannot be merged unless they pass the port compliance tests.       

#### Dependency Flow

```
[Presentation] → [Business Logic Services] → [Repository Interfaces] ← [Repository Implementations]
     ↓              ↓                              ↓
[Shared DTOs]   [Domain Models]                [ORM Framework]
```

- Arrows indicate allowed dependencies
- Interfaces act as contracts between layers
- DI container wires implementations at runtime

#### AI/External Service Integration Points

- Service abstractions in Business Logic layer for external dependencies
- Separate projects for AI/external services with abstraction layers
- Abstractions allow swapping implementations without touching core logic

#### Rules for AI Agents

1. **Maintain Layer Separation**: Outer layers depend on inner layers only through abstractions (interfaces), never on concrete implementations. Inner layers must not reference or depend on outer layers in any way.
2. **Use Interfaces**: All cross-layer communication via interfaces defined in abstraction projects
3. **Enforce 500 LOC Limit**: Break large files into smaller, focused classes
4. **Dependency Injection**: Register implementations in DI container, inject interfaces
5. **Repository Pattern**: Data access only through repository interfaces
6. **Testability**: Design for unit testing by depending on abstractions
7. **Framework Independence**: Keep domain models free of framework-specific code
8. **Modular Boundaries**: Changes in one module should not require changes in others

#### Example Implementation

- Controller injects `IService` (interface)
- `Service` implements `IService`, injects `IRepository`
- `Repository` implements `IRepository`, uses ORM
- All layers communicate via domain models

This architecture ensures applications remain maintainable, testable, and evolvable while supporting complex features like real-time communication and AI integration.

### AI Agent Development Guidelines

**Critical Rules for AI Agents:**

1. **File Size Enforcement**: Never create or modify files exceeding 500 lines of code. Break large classes into smaller, focused components.

2. **Dependency Direction**: Always maintain inward dependency flow. Outer layers (Presentation) depend on inner layers (Business Logic) only through interfaces. Inner layers never reference outer layers.

3. **Interface-First Design**: Define interfaces in abstraction projects before implementing concrete classes. All cross-layer communication must use interfaces.

4. **Layer Isolation**:
   - Presentation layer: Only HTTP handling, DTOs, and interface calls
   - Business Logic layer: Pure business rules, no framework references
   - Domain layer: POCO models only, no dependencies
   - Infrastructure layer: Only data access implementations

5. **Repository Pattern**: All data access must go through repository interfaces, never direct ORM calls from business logic.

6. **Dependency Injection**: Use constructor injection for all dependencies. Register implementations in DI container at startup.

7. **Framework Independence**: Keep domain models free of any framework-specific attributes or references.

8. **Modular Boundaries**: Each project/module should have a single responsibility. Changes in one module should not require changes in others.

**Code Review Checklist for AI Agents:**

- [ ] File size ≤ 500 LOC
- [ ] No outer-to-inner dependencies
- [ ] All public methods have interface contracts
- [ ] Business logic contains no UI/database code
- [ ] Domain models are framework-agnostic
- [ ] Dependencies injected via interfaces
- [ ] Repository pattern used for data access

### Architectural Concepts

- **Layered Architecture**: Separate concerns: UI layer (presentation), Business logic (application/domain), Data access (infrastructure), Cross-cutting (logging, security).
- **Patterns**: MVC for controllers; CQRS for read/write separation; Event-driven for real-time; Repository for DB abstraction.
- **Modularity**: Use dependency inversion; interfaces for decoupling. Modules as independent units with explicit dependencies.
- **Scalability Strategies**: Horizontal scaling; stateless services; load balancing. Vertical via optimization.
- **Fault Tolerance**: Circuit breakers; retries; graceful degradation.

### UI/UX Strategies

- **Responsive Design**: Fluid grids, flexible images, media queries. Progressive enhancement.
- **UX Principles**: User-centered; accessibility (semantic structure); minimalism for intuitiveness.
- **State Management**: Centralized store; immutable updates to prevent side effects.

### Performance Strategies (Speed & Power)

- **Speed**: Asynchronous processing; caching (in-memory, distributed); lazy/eager loading; compression.
- **Power Efficiency**: Throttle I/O; batch operations; profile hotspots (CPU, memory).
- **Optimization Techniques**: Algorithmic efficiency (O(n) bounds); indexing; pagination.

### Memory Optimization & Safety

- **Strategies**: Garbage collection tuning; object pooling; weak references. Avoid leaks via resource cleanup (RAII pattern).
- **Cleanup**: Use try-finally for resources; monitor heap usage; manual deallocation where applicable.
- **Pseudocode** (Safe Resource Handling):

```
function processData(data):
    resource = acquireResource()
    try:
        // Process
        result = compute(data, resource)
        return result
    finally:
        releaseResource(resource)  // Guarantee cleanup
```

### Logging Strategies

- **Levels & Structure**: Hierarchical (debug/info/warn/error); structured formats (JSON) for querying.
- **Centralization**: Aggregate logs; correlation IDs for tracing requests.
- **Rotation**: Time/size-based; alerting on anomalies.

### Security Strategies

- **Principles**: Least privilege; defense in depth; input validation everywhere.
- **Auth/Access**: Token-based (stateless); role-based access control (RBAC); encryption in transit/rest.
- **Vulnerabilities Mitigation**: Sanitize inputs; secure headers; rate limiting; auditing.

### Networking / API Strategies

- **Design**: RESTful principles (stateless, cacheable); GraphQL for flexible queries; versioning.
- **Optimization**: Keep-alive connections; payload minimization; error handling (standard codes).
- **Reliability**: Idempotency; timeouts; backoff retries.

### Controller / Backend Logic Strategies

- **Separation**: Thin controllers (orchestrate); fat services (logic). Use middleware for cross-concerns.
- **Error Handling**: Centralized handler; custom exceptions; logging integration.
- **Pseudocode** (Controller):

```
controller getItem(id):
    try:
        item = service.fetchItem(id)
        return response(200, item)
    catch NotFoundError:
        return response(404, "Not found")
    catch Error:
        log(error)
        return response(500, "Internal error")
```

### Data Activities & ACID Strategies

- **Transactions**: Atomic operations; two-phase commit for distributed.
- **Consistency Models**: Strong vs. eventual; use locking/optimistic concurrency.
- **Data Integrity**: Constraints (PK/FK); validation at boundaries.

### Database Design & Optimizations

- **When to Use**:

  | Type        | Use Case                          | Optimizations                  |
  |-------------|-----------------------------------|--------------------------------|
  | Relational | Structured data, joins, ACID     | Indexes, normalization (3NF), partitioning |
  | Hierarchical | Nested/JSON docs, flexible schema| Denormalization, embedding     |
  | Vector     | Embeddings, similarity search    | Approximate nearest neighbors  |
  | Graph      | Relationships, traversals        | Indexing edges, query planning |

- **Strategies**: Sharding for scale; replication for availability; query optimization (EXPLAIN plans).

### Source Control Strategies

- **Branching**: Feature branches; release/hotfix. Semantic versioning.
- **Collaboration**: Pull requests; code reviews; hooks for linting.

### CI/CD Strategies

- **Pipeline**: Build/test/deploy stages; parallel jobs. Blue-green deployments for zero downtime.
- **Automation**: Infrastructure as code; monitoring integration.

### Engineering Approach: Bottom-Up & Top-Down

- **Top-Down**: Start with ideal system model (e.g., UML diagrams for entities/flows); define APIs/contracts.
- **Bottom-Up**: Implement low-level primitives (e.g., custom data structures); integrate upwards, validating against high-level.
- **Iteration**: Prototype; refactor; discard mismatches. Measure impact via metrics (latency, throughput).

Apply these strategies agnostically; adapt to context for optimal template.

### Testing Strategies

Adopt comprehensive, automated testing pyramid: Heavy unit tests (fast, isolated), moderate integration (components interaction), light end-to-end (full flow). Use TDD/BDD for development. Coverage goal: 80%+. Tools-agnostic: Mock dependencies; parallel execution; mutation testing for robustness.

- **Unit Testing**: Isolate functions/modules. Test pure logic, edge cases, errors. Strategy: Arrange-Act-Assert; parameterize for variations.
- **Integration Testing**: Verify module interactions (e.g., API-DB). Use in-memory mocks; test contracts/interfaces.
- **End-to-End (E2E)**: Simulate user flows. Browser automation; API smoke tests.
- **Performance Testing**: Load/stress (throughput, latency); benchmark baselines.
- **Security Testing**: Static analysis (SAST); dynamic (DAST); penetration simulations.
- **Accessibility Testing**: Automated audits (WCAG); manual reviews.
- **Chaos Engineering**: Inject failures (e.g., network delays) to test resilience.
- **Clarity & Logging**: Always add brief logged explanations for any programmatic test that explains what the test is actually attempting to prove / disprove. So if all tests are run the console will show each test with a printed line about what it's trying to accomplish.

Integration in CI/CD: Run on every commit; fail-fast. Flaky test quarantine.

### Validation Domains & Best Combination

Validation ensures correctness across layers. Best combo: Layered defense—client-side (immediate feedback), server-side (authoritative), DB-level (integrity). Combine preventive (static types, schemas) with runtime checks. Use fail-early principle.

| Domain          | Description & Strategies                          | Best Practices & Combo Integration |
|-----------------|---------------------------------------------------|------------------------------------|
| Input Validation | Sanitize/validate user inputs (forms, APIs). Prevent injections, overflows. | Client (regex, schemas) + Server (validators). Combo: With security (OWASP rules); tie to unit tests. |
| Data Validation | Ensure data integrity (formats, ranges, relations). ACID enforcement. | Schema validation + Constraints (DB). Combo: With integration tests; optimistic locking for concurrency. |
| Business Logic Validation | Check rules/constraints (e.g., auth, workflows). | Domain-driven invariants; assertions in services. Combo: BDD scenarios + E2E; audit logs for post-validation. |
| UI/UX Validation | Verify rendering, responsiveness, accessibility. | Snapshot testing; visual regression. Combo: With performance (load times); user session replays. |
| Security Validation | Auth, encryption, access controls. | Token expiry checks; role validations. Combo: Pen tests + Runtime monitoring; integrate with logging. |
| Performance Validation | Resource usage, scalability thresholds. | Metrics assertions (e.g., <100ms response). Combo: With chaos; continuous profiling in prod. |

Overall Strategy: Orthogonal validation—cross-cut domains via aspects (e.g., AOP for logging validations). Automate 90%; manual for exploratory. Measure effectiveness via defect escape rate.
