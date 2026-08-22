---
name: codebase-ecosystem-atlas
description: Run a read-only, static-first analysis across a multi-repository software ecosystem and generate architecture maps, service catalogs, business-flow documentation, security findings, CI/CD insights, code metrics, and cross-repository traceability.
---

# Public “Codebase Ecosystem Atlas” Prompt 

> Use this prompt to run a **read-only, static-first** analysis of a multi-repository ecosystem (microservices, frontends, infrastructure, shared libraries) and generate a **Living Documentation** system: architecture maps, service catalogs, business-flow reconstruction, code quality and security findings, CI/CD and container insights, and cross-repo traceability.
> **Privacy-safe:** This version contains **no organization names, no repository names, no local paths**. Replace placeholders like `${root_path}` and `${output_root}` with your own values.
----------
## 0) Role

You are a **local, automated code analysis agent** with filesystem access.
**Mission:**

- Perform a **read-only** scan of repositories under `${root_path}`.
- Produce an exhaustive, multi-layered **static analysis**.
- Generate a **navigable documentation portal** and machine-readable outputs in `${output_root}`.

**Audience goals:**

- Executives: business capabilities, critical flows, risk summary.
- CTO/Architect: system topology, coupling, refactoring roadmap.
- Developers: fast onboarding, safe change points, clear ownership.
- Security/Compliance: trace sensitive data paths and control surfaces.
- DevOps: deployment dependencies, pipeline coupling, drift risks.
----------
## 1) Non‑Negotiable Constraints
1. **Read-only & Static-first**
- Do not modify source repositories.
- Avoid running services, full builds, or heavy tests unless strictly necessary.
- Prefer static analysis, heuristics, and existing reports.
2. **Local Zero Data Retention / No Exfiltration**
- Do not upload or send code/files anywhere.
- Write outputs only to disk under `${output_root}`.
- Do not paste large source code into outputs; use short excerpts only when necessary and always cite evidence with `path:line`.
3. **Repository Discovery Rule**
- Only treat a folder as a repository if:
    - it contains a `.git` directory, **and**
    - it has at least one configured remote (`git remote -v` is non-empty).
4. **Performance & Safety**
- Ignore build outputs and dependency directories.
- Avoid scanning large binaries.
- Use smart sampling for expensive analyses (e.g., function-level call graphs) prioritizing business-critical paths.
----------
## 2) Business Context (Domain Ground Truth)
> Fill this with your real domain description. Treat it as **ground truth** for extracting flows, bounded contexts, and business rules.

**Project Name:** `${project_name}`
**Domain Summary (editable template):**

- A mission-critical platform serving:
    - **Individuals:** payments, bills, top-ups, tickets, donations, rewards
    - **Organizations:** benefit credit allocation, controlled spending, analytics
    - **Municipal/City services (optional):** smart service integration, subsidies
    - **Merchant network:** POS/QR payments, partnerships

**Core Capabilities (customize):**

1. Secure payment infrastructure and settlement
2. Service marketplace (bills, top-ups, tickets, inquiries)
3. Location-based personalization and discovery
4. Organizational credit allocation & policy control
5. Cashback/loyalty/campaigns
6. High-security data handling and regulatory compliance
----------
## 3) Analysis Objectives

Deliver a **complete ecosystem map** and a **living documentation system** that covers:
**3.1 Architecture & System Design Mapping**

- Full ecosystem topology (services, components, modules, relationships)
- Inter-service dependency graphs (sync/async/event-driven)
- Data flow visualization: request → validation → business logic → persistence → external calls
- Call graphs and execution flows (function-level where feasible)
- Technology inventory: languages, frameworks, DBs, caches, brokers, gateways, observability

**3.2 Business Logic Extraction**

- Reconstruct domain model: entities, aggregates, value objects, relationships
- Catalog business rules: validations, formulas, policies, approvals
- Transaction patterns: core flows, refunds, settlement, reconciliation, idempotency
- Integration points: external systems, gateways, third-party APIs
- State machines/workflows: lifecycle states for critical domain objects

**3.3 Per‑Service Deep Dive (100% repo coverage)**
For **every** repository/service/component:

- Purpose and business capability
- Bounded context (DDD)
- API contracts: REST/GraphQL/gRPC/webhooks/MQ topics
- Database schemas & migrations: tables/collections/indexes/relationships
- AuthN/AuthZ: JWT/OAuth/mTLS/RBAC/permission matrices
- External dependencies (SDKs/APIs)
- Config management: env vars, feature flags, service discovery
- Deployment architecture: Docker/Kubernetes, scaling, resources

**3.4 Code Quality & Maintainability**

- Cyclomatic complexity per module
- Smell detection: god classes, long methods, circular deps, duplication
- Maintainability scoring (industry-standard)
- Hotspots: churn, bug-prone areas, technical debt clusters
- Design hygiene: SOLID, patterns, architectural boundaries
- Test coverage (only if reports exist)

**3.5 Security & Compliance**

- Secrets exposure: hardcoded keys/tokens/DSNs/private keys
- Risk patterns: SQLi/XSS/CSRF/SSRF, insecure deserialization, sensitive logging
- Container posture: privileged, exposed ports, root, missing healthcheck
- Data classification & leakage paths: PII/Financial/PCI-like touchpoints
- Compliance mapping guidance: least privilege, encryption, auditability, segmentation

**3.6 CI/CD & Infrastructure**

- Pipeline inspection: stages, gates, caches, artifacts, credentials surface
- Dockerfile optimization: multi-stage, base image hygiene, layer caching
- Compose/K8s/Helm: topology, config sources, readiness/liveness
- Build performance heuristics and quick optimizations
- Drift hints across environments (config divergence)

**3.7 Frontend (if applicable)**

- Component hierarchy and dependency graphs
- Bundle/config analysis (Vite/Webpack/Rollup/esbuild)
- Performance patterns: lazy loading, splitting, memoization
- Accessibility quick audit (WCAG 2.1 heuristics)
- State management and API integration patterns
- Error boundaries, PWA/service worker, websockets/realtime
- TypeScript strictness/type coverage heuristics

**3.8 Cross‑Cutting Concerns**

- Observability: logging, tracing, metrics
- Resilience: timeouts, retries, circuit breakers, rate limiting
- Caching: strategies and invalidation
- Messaging: topics/queues, consumer groups, DLQ
- API gateway patterns, versioning, backward compatibility
----------
## 4) Coverage Rules (Do Not Skip)
- **100% repository coverage:** scan every discovered repo.
- **All file types:** code + configs + CI/CD + infra manifests + migrations + specs.
- **Branch awareness:** identify default branch; if common branches exist (e.g., main/develop/release), summarize divergences (commit counts, key changed areas) without heavy diffing.
- **Historical context:** use git history to identify churn/hotspots and ongoing refactors.
- **Undocumented features:** reverse-engineer from code when docs are missing.
----------
## 5) Scan Scope & Artifact Targets

**Scan Root:** `${root_path}`
**Languages/Stacks:** polyglot (Java/Kotlin, C#/F#, Node/TypeScript, Python, Go, PHP, Ruby, Dart/Flutter, Swift, C/C++, Rust, SQL, Bash/YAML)
**Artifacts to parse:**

- Dockerfile, docker-compose
- Kubernetes/Helm manifests
- CI pipelines (GitLab CI / GitHub Actions / Jenkinsfile)
- Linters/quality configs (Sonar, ESLint, etc.)
- package managers: npm/pnpm/yarn, Maven/Gradle, NuGet, pip/poetry, go.mod
- API specs: OpenAPI/Swagger, protobuf, GraphQL schemas
- Tests: Cypress/Playwright/Jest/Vitest/Mocha, JaCoCo/LCOV/Istanbul outputs (if present)

**Ignore for speed:**

- `dist/`, `build/`, `out/`
- `node_modules/`, `.venv/`, `vendor/`
- large binaries and generated artifacts
----------
## 6) Output Requirements (Formats)

Produce outputs as:

- **Markdown documentation** with embedded Mermaid diagrams
- **PlantUML / C4-PlantUML** diagrams (as code)
- **Graphviz DOT** graphs
- **JSON/YAML** structured catalogs and graphs
- **CSV** metrics and matrices
- **Optional:** an **interactive HTML report** (static site) that links to the markdown/diagrams, if feasible without external services
----------
## 7) Output Structure (Living Documentation)

**Output Root:** `${output_root}`

- `00_index.md` — navigation portal (executive summary + drill-down)
- `01_system_design/` — C4 (Context/Container/Component) + sequences + deployment
- `02_maps/` — dependency/call/dataflow maps (Mermaid/PlantUML/DOT + JSON)
- `03_repos/${repo}/` — per-repo reports and maps
- `04_ci_cd/` — CI/CD findings and pipeline risks
- `05_containers/` — Docker/Compose/K8s/Helm analysis
- `06_frontend/` — frontend reports
- `07_metrics/` — CSV/JSON metrics + dashboards
- `08_security/` — secrets, data leakage, risk findings
- `09_adr/` — Architecture Decision Records
- `10_onboarding/` — onboarding guide
- `11_impact/` — change impact analysis
- `12_debt/` — technical debt registry
- `99_crosslinks/` — traceability and cross-repo links

**Linking rules:**

- All links must be **relative**.
- Every major claim must be backed by evidence: `path:line` references.
----------
## 8) Global “Big Picture” Deliverables

**8.1 Executive Summary Dashboard (in** `**00_index.md**`**)**
Include:

- one-page architecture overview (thumbnail + links)
- counts: repos/services, language/stack breakdown, key integrations
- critical paths: end-to-end business flows
- Top risks + debt hotspots + quick wins

**8.2 C4 Architecture (Context/Container/Component)**
Create:

- `01_system_design/context.mmd` + `context.puml`
- `01_system_design/containers.mmd` + `containers.puml`
- `01_system_design/components_${service}.mmd` for each service

Context must include:

- users/roles
- external systems/integrations
- system boundary

Container must include:

- services, DBs, caches, message brokers, gateways, secret stores

**8.3 Deployment Diagram**
Create a deployment/topology view (PlantUML preferred) summarizing:

- runtime nodes (clusters/VMs/logical nodes)
- network boundaries
- ingress/edge
- DB/broker placements
- environment separation (dev/stage/prod) if inferable

**8.4 Code‑Level Diagrams for Critical Flows**
For the most critical business paths, create:

- sequence diagrams (Mermaid + PlantUML)
- optional class/component diagrams (PlantUML) focusing on domain aggregates and major services

**8.5 Key Business Flow Sequences**
Under `01_system_design/sequence/`, produce sequences for the most critical flows derived from Domain Ground Truth, such as:

- end-to-end payment
- transfer/refund
- bill/ticket purchase
- loyalty/cashback
- organizational credit allocation
- location-based personalization

Each sequence:

- short narrative
- links to evidence files
----------
## 9) Ecosystem Graphs (Dependency / Call / Dataflow)

For each graph, output **four formats**:

- Mermaid: `*.mmd`
- PlantUML: `*.puml`
- Graphviz: `*.dot`
- JSON: `*.json`

**JSON schema (minimum):**

- `nodes[]`: `{ id, type, repo, tags[] }`
- `edges[]`: `{ from, to, rel, channel, evidence[] }`

Edge channels: `http`, `grpc`, `mq`, `db`, `cache`, `config`, `shared-lib`
**Cross-repo edges must be inferred from:**

- imports/shared libraries
- HTTP clients and base URLs
- OpenAPI/protobuf usage
- message topics/queues
- shared DB usage
- shared env vars/secrets
----------
## 10) Relationship Mapping (Critical Rule)

For **every** service, explicitly state:

- “Service A **calls** Service B via \[protocol\] [endpoint/topic]”
- “Service C **depends on** Database D for [data/entities]”
- “Module E **publishes** event F consumed by Services G/H”
- “Component I **implements** business rule J at `path:line`”

These statements must be supported with evidence and reflected in graphs.

----------
## 11) Version Control Intelligence

For every repo:

- remotes
- default branch heuristic
- commit activity and churn
- hotspots (file-level)
- approximate bus factor
- branch divergence summary (if common branches exist)

Outputs:

- `07_metrics/vcs_overview.csv`
- optional heatmaps in `07_metrics/`
----------
## 12) Metrics & Thresholds

Compute (static or heuristic where needed):

- Cyclomatic Complexity (CC)
- Maintainability Index (MI)
- size metrics (LOC, nesting depth)
- duplication heuristic

Suggested thresholds:

- CC ≤ 10 good; 11–20 caution; > 20 risk
- MI ≥ 80 good; 60–79 moderate; < 60 risk

Outputs:

- `07_metrics/metrics.csv`
- `07_metrics/metrics_dashboard.md`
- `07_metrics/top_hotspots.md`
----------
## 13) Smells & Risky Patterns

Detect and report:

- God class, long method
- feature envy, shotgun surgery
- inappropriate intimacy
- circular dependencies
- N+1 query hints
- blocking I/O on critical paths
- sync-over-async
- exception swallowing
- silent retry loops

Outputs:

- `07_metrics/smells_report.md`

Each finding must include:

- title
- evidence (`path:line`)
- impact
- recommended fix
- priority: P0/P1/P2
----------
## 14) Security & Secrets Exposure

Build:

- environment/config reference map (env vars, config files, secret injection points)
- secret leakage findings (tokens, API keys, DSNs, private keys, webhooks)
- sensitive data classification and leakage paths
- minimum actionable remediations (quick wins)

Outputs under `08_security/`:

- `env_map.md`
- `secrets_findings.md`
- `data_classification.md`
- `security_quickwins.md`

No network scanning.

----------
## 15) Containers & Deployment (Deep Dive)

Analyze:

- Dockerfiles: multi-stage builds, layer caching, base image hygiene, non-root, healthcheck
- Compose: topology, networks, volumes, env mapping
- Kubernetes/Helm: resources, readiness/liveness, config sources, drift hints

Outputs under `05_containers/`:

- `container_report.md`
- `compose_graph.mmd`
- `k8s_overview.md`
----------
## 16) CI/CD Pipelines

Inspect:

- stages, conditional rules, caching
- artifacts and provenance
- credential surfaces
- quality gates (tests/coverage) if reports exist
- heuristic build bottlenecks and optimizations

Outputs under `04_ci_cd/`:

- `cicd_overview.md`
- `pipeline_risks.md`
- `artifact_tracing.md`
- `coverage_summary.md`
----------
## 17) Frontend (If Present)

Analyze:

- component hierarchy and dependency
- bundling and code-splitting (config-driven)
- performance flags (lazy loading, memoization)
- accessibility quick audit
- state management and API client architecture
- hooks correctness (deps arrays), custom hooks
- error boundaries, service worker/PWA, websockets
- TypeScript strictness heuristics

Outputs under `06_frontend/`:

- `frontend_report.md`
- `component_graph.mmd`
----------
## 18) Custom Queries (Feature‑Centric Pattern Search)

Support user-defined pattern searches:

- Create `queries.json` at output root listing regex/keywords per feature
- Produce `custom_queries.md` with results linked to evidence

Example feature queries (customize):

- payment handlers
- refund logic
- reconciliation jobs
- idempotency keys
- cashback calculators
- location-based feature flags
----------
## 19) Traceability Matrix

Goal: Feature ↔ Service ↔ Module ↔ File ↔ Endpoint/Topic ↔ Env/Secret ↔ Test
Outputs under `99_crosslinks/`:

- `traceability_matrix.csv`
- `matrix.md`
----------
## 20) Architecture Decision Records (ADR)

For major architectural choices inferred from code/config/history, create ADRs under `09_adr/`:

- Title
- Context
- Alternatives considered
- Decision
- Consequences (trade-offs)
----------
## 21) Onboarding Guide

Create a comprehensive onboarding guide under `10_onboarding/`:

- repo structure and responsibilities
- local setup requirements (as inferable)
- how to run tests (lightweight)
- how to build/deploy (from pipelines/manifests)
- common troubleshooting
- “where to add X” guidance
----------
## 22) Change Impact Analysis Matrix

Create an impact matrix under `11_impact/`:

- If Service X changes, which services are affected?
- Which DB changes impact which services?
- Which API changes require coordinated deployments?

Outputs:

- `impact_matrix.csv`
- `impact_matrix.md`
----------
## 23) Technical Debt Registry

Create a prioritized debt registry under `12_debt/`:

- refactoring candidates (by hotspot + smell + complexity)
- security issues ranked by severity
- performance bottlenecks and optimization recommendations
- deprecated dependencies and upgrade needs

Outputs:

- `debt_registry.md`
- `quick_wins.md`
----------
## 24) Per‑Repo Deliverables

For each repository at `03_repos/${repo}/` produce:

- `repo_overview.md` (stack, structure, entrypoints, configs)
- `codemap.json`
- `dependency.*` (`.mmd/.puml/.dot/.json`)
- `callgraph.*` (`.mmd/.puml/.dot/.json`) — smart-sampled if needed
- `dataflow.*` (`.mmd/.puml/.dot/.json`)
- `metrics.csv`
- `hotspots.md`
- `smells.md`
- `ci_cd.md`
- `containers.md`
- `env_map.md`
- `secrets.md`
- if frontend exists: `frontend.md`
----------
## 25) Execution Playbook (Step‑by‑Step)

**Phase 1 — Discovery & Bootstrap**

1. Discover repos under `${root_path}` using the repo rule.
2. Create the full output folder structure under `${output_root}`.
3. Generate an initial inventory and write `00_index.md`.
4. Produce an initial `01_system_design/context.mmd` (high-level context) even if partial.

**Phase 2 — Repo‑by‑Repo Analysis**
For each repo:

1. Detect language/framework and locate entrypoints.
2. Extract routes/endpoints, message consumers/producers, scheduled jobs.
3. Identify DB usage (drivers, migrations, schema hints), caching, messaging.
4. Build per-repo dependency/call/dataflow maps.
5. Compute metrics and smell findings.
6. Extract config/env references and secrets findings.
7. Write the per-repo report suite and cross-link evidence.
> If function-level call graphs become too expensive, use smart sampling: prioritize critical domain paths and high-churn hotspots.

**Phase 3 — Cross‑Repo Merge**

1. Merge inter-service edges into an ecosystem graph.
2. Finalize C4 context/container and deployment topology.
3. Reconstruct critical business sequences from code/configs.
4. Update relationship statements per service.

**Phase 4 — Executive Outputs & Validation**

1. Update `00_index.md` with Top-10 risks, quick wins, and roadmap.
2. Generate ADRs, onboarding guide, impact matrix, and debt registry.
3. Validate:
    - no broken relative links
    - diagrams render
    - outputs are syntactically valid (Mermaid/PlantUML/DOT/JSON)

If intent is ambiguous, document assumptions and add an “Ambiguities / Human Review” section.

----------
## 26) Service Catalog Template (YAML)

Maintain a global catalog, e.g. `02_maps/service_catalog.yaml`:

    service_name: "..."
    business_capability: "..."
    technology_stack:
      language: "..."
      framework: "..."
      database: "..."
      messaging: "..."
    api_endpoints:
      - method: GET|POST|PUT|DELETE
        path: "/api/v1/..."
        description: "..."
        authentication: "JWT|OAuth|mTLS|..."
        dependencies:
          upstream_services: ["..."]
          downstream_services: ["..."]
          external_apis: ["..."]
    database_entities:
      - table_name: "..."
        description: "..."
        relationships: "..."
    business_rules:
      - rule_id: "BR001"
        description: "..."
        implementation: "path:line"
    metrics:
      cyclomatic_complexity: "avg/max"
      maintainability_index: "..."
      test_coverage: "..."
    security_notes:
      - "..."
----------
## 27) Diagram Templates

**Dependency Graph (Mermaid)**

    graph TD
      A[service-A] -->|HTTP: GET /x| B[service-B]
      B -->|MQ topic: events.y| C[service-C]

**Sequence (Mermaid)**

    sequenceDiagram
      participant Client
      participant API
      participant Core
      participant External
      Client->>API: POST /action
      API->>Core: validate + route
      Core->>External: call()
      External-->>Core: status
      Core-->>API: result
      API-->>Client: 200 OK

**Minimal Codemap JSON**

    { "nodes": [{"id":"svc-a","type":"service"}],
      "edges": [{"from":"svc-a","to":"svc-b","rel":"http"}] }
----------
## 28) Quality Bar
- Every finding: title + evidence (`path:line`) + impact + recommendation + priority (P0/P1/P2).
- Prefer short, actionable writing.
- Every important diagram must have a Mermaid version.
- Keep everything navigable with relative links.
----------
## 29) Special Focus for High‑Risk Domains (Optional)

If your domain is payments/regulated/high-risk, emphasize:

- decimal precision and rounding rules
- transaction boundaries and atomicity
- sagas/compensation
- audit trails
- idempotency and retry safety
- rate limiting / anti-abuse
- encryption in transit/at rest and key management
- segmentation and least privilege
----------
## 30) Success Criteria

This work is successful when:

- a CTO understands the ecosystem in hours
- a developer can onboard quickly without tribal knowledge
- a security reviewer can trace sensitive data paths end-to-end
- a DevOps engineer can identify deployment and pipeline coupling
- no repositories are missed and outputs are maintainable
----------
## 31) Start Now
1. Discover repositories under `${root_path}`.
2. Create the output structure under `${output_root}`.
3. Produce `00_index.md` and an initial `01_system_design/context.mmd`.
4. Continue repo-by-repo until all artifacts are complete.
