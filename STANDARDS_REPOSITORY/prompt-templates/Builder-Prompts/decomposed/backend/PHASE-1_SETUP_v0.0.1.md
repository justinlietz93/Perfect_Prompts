**Subject: Phase 1: Backend Service Architecture Initialization and Strategic Build Planning for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt initiates the **Backend Architectural Planning Phase (Phase 1)** for the autonomous agent responsible for the **[Project Name]** service layer. Objectives:
    a. Internalize Apex Standards and Hybrid-Clean Architecture mandates for backend services (dependency rule, DI, repository pattern).
    b. Analyze functional requirements, domain workflows, and NFRs impacting service design (scalability, reliability, latency, observability).
    c. Define service boundaries, module responsibilities, data flow, and integration contracts.
    d. Address cross-cutting concerns (security, resilience, transactionality, configuration management).
    e. Produce a sequential backend build plan aligned with dependency order and infrastructure readiness.

**2. Core Execution Principles & Global Rules**
* **Apex Standards Adherence:** Follow the **Apex Software Compliance Standards Guide** (`[Specify relative path]`) precisely, referencing `[(Rule #X: CODE)](...)`.
* **Hybrid-Clean Architecture Enforcement:** Preserve dependency flow `Presentation → Business Logic → Repository Interfaces ← Infrastructure`. Backend business logic must remain framework-agnostic; infrastructure implements interfaces only.
* **Strict Sequential Execution:** Plans generated later must follow `Phase -> Task -> Step` order with checkboxes.
* **Internal Verification:** Verify each output against relevant standards, repository pattern requirements, and dependency inversion constraints.
* **Recursive Remediation:** Stop, analyze, remediate, and re-verify upon failure.
* **Autonomous Operation & Logging:** Operate autonomously; log per Section 5.

**3. Mandatory Quality & Finalization Rules**
Apply Apex Standards continuously:
* Code Quality & Structure (`QUAL-*`, `QUAL-SIZE`).
* Security & Compliance (`SEC-*`, authentication, authorization, data protection).
* Data Management (`DATA-*`, schema governance, migrations).
* Testing (`TEST-*`: unit, integration, contract, load, resilience).
* Documentation (`DOC-*`: architecture decisions, API specs).
* Implementation Correctness (`IMPL-*`).
* Infrastructure Alignment (`CONF-*`, `DEPL-*`).

**4. Directive Section: Phase 1 - Backend Architectural Planning**

* **Input Context:**
    * **Project Goal:** Deliver backend services for **[Project Name]**.
    * **Functional Requirements:** [List service endpoints, workflows, domain events, integration points.]
    * **Non-Functional Requirements:** [Performance (latency, throughput), scalability, reliability targets, data consistency, security/regulatory obligations, observability.] 
    * **Technology Stack:** [Languages, frameworks, databases, messaging, hosting platform.] 

* **Phase 1 Objective:** Establish backend architecture, module boundaries, interface contracts, data strategies, and build sequencing aligned with standards.

* **Execution Plan (complete sequentially):**
    -   [ ] **Task 1.1: Standards & Context Confirmation** *(Setup/Meta)*
        -   [ ] * **Step 1.1.1 [(Rule #? : INIT-CONF)](...):** Confirm understanding of Apex rules, Hybrid-Clean dependency rule, repository pattern requirements, DI strategy, and location of standards documents.
        -   [ ] * **Step 1.1.2 [(Rule #? : INPUT-VAL)](...):** Validate access to requirements, domain models, current data sources, and target stack specifics.

    -   [ ] **Task 1.2: Domain & NFR Analysis** *(Understanding the Problem)*
        -   [ ] * **Step 1.2.1:** Map domain capabilities, aggregates, and core workflows.
        -   [ ] * **Step 1.2.2:** Analyze NFR impacts on concurrency, scaling, data consistency, security, and resilience.
        -   [ ] * **Step 1.2.3:** Evaluate technology stack implications (framework constraints, database characteristics, messaging semantics).
        -   [ ] * **Step 1.2.4 [(Rule #? : ARCH-DRIVE)](...):** Prioritize top 5-7 architectural drivers influencing backend design.

    -   [ ] **Task 1.3: Architecture Definition** *(Solution Structure)*
        -   [ ] * **Step 1.3.1 [(Rule #? : ARCH-PAT)](...):** Assess candidate patterns (modular monolith, CQRS, event-driven) against drivers; select and justify.
        -   [ ] * **Step 1.3.2:** Define layers/modules (presentation adapters, application services, domain, infrastructure) with responsibilities.
        -   [ ] * **Step 1.3.3 [(Rule #? : ARCH-COMP)](...):** Identify application services, domain services, repositories, integration adapters.
        -   [ ] * **Step 1.3.4 [(Rule #? : ARCH-INT)](...):** Map interactions (sync/async flows, command/query, event dispatch).
        -   [ ] * **Step 1.3.5 [(Rule #? : ARCH-DEP)](...):** Document dependency matrix ensuring outer layers depend on abstractions only.

    -   [ ] **Task 1.4: Data & Integration Strategy** *(Cross-Cutting)*
        -   [ ] * **Step 1.4.1 [(Rule #? : DATA-MOD)](...):** Define domain entities, aggregates, value objects, and data ownership.
        -   [ ] * **Step 1.4.2 [(Rule #? : API-DES)](...):** Outline API contracts (REST/gRPC), serialization formats, versioning, and security controls.
        -   [ ] * **Step 1.4.3 [(Rule #? : DATA-INT)](...):** Specify integration patterns (message queues, event buses) and consistency strategies.
        -   [ ] * **Step 1.4.4 [(Rule #? : QUAL-OBS)](...):** Establish observability strategy (logging, metrics, tracing) aligned with backend workloads.

    -   [ ] **Task 1.5: Operability & Resilience Strategy**
        -   [ ] * **Step 1.5.1 [(Rule #? : SEC-AUTH)](...):** Define authentication/authorization mechanisms, secrets handling, and role enforcement.
        -   [ ] * **Step 1.5.2 [(Rule #? : QUAL-RES)](...):** Plan resilience measures (circuit breakers, retries, backoff, idempotency).
        -   [ ] * **Step 1.5.3 [(Rule #? : CONF-MAN)](...):** Document configuration management across environments (12-factor alignment).
        -   [ ] * **Step 1.5.4 [(Rule #? : QUAL-MON)](...):** Specify monitoring/alerting metrics (latency, error rate, throughput, queue depth).

    -   [ ] **Task 1.6: Build Sequencing**
        -   [ ] * **Step 1.6.1 [(Rule #? : PLAN-SEQ)](...):** Create execution order for services, interfaces, repositories, infrastructure adapters respecting dependencies.
        -   [ ] * **Step 1.6.2 [(Rule #? : PLAN-JUST)](...):** Justify sequence referencing dependency matrix, risk mitigation, and value delivery.

    -   [ ] **Task 1.7: Consolidation & Verification**
        -   [ ] * **Step 1.7.1:** Consolidate architecture diagrams, sequence plans, and strategies into blueprint.
        -   [ ] * **Step 1.7.2 [(Rule #? : PLAN-VER)](...):** Verify outputs against objectives, standards, and dependency rules.

* **Internal Success Criteria:** Completion of tasks 1.1-1.7; architecture defined and compliant; strategies documented; build sequence justified; blueprint verified.
* **Internal Verification Method:** Execute Step 1.7.2, cross-check drivers to decisions, ensure repository interfaces abstracted, confirm DI boundaries.

**5. Test Reporting Protocol (Internal)**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Service/Module), Planned Tests, Metrics (latency targets, error budgets), Status, Findings.
* **Update Frequency:** After relevant planning validation or subsequent backend testing phases.

**6. Final Instruction**
Execute tasks sequentially to produce the backend architectural blueprint and build plan. Await approval before moving to Phase 2 component implementation.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
