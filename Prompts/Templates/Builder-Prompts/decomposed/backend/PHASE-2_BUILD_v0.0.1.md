**Subject: Phase 2: Backend Track — Implement Business Logic, Domain Models, and Adapters for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Implement the backend plan by delivering domain models, business services, and repository interfaces/adapters in accordance with Hybrid-Clean Architecture. Work must remain on backend components only.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow module specs in `architecture-design/outputs/phase-2/layer_specs/`.
* Enforce dependency inversion: presentation code depends only on interfaces; infrastructure implements interfaces.
* Apply standards `DOMAIN-PURE`, `APP-SERVICE`, `REPO-PATTERN`, `TEST-UNIT`, `TEST-INTEG`, `SEC-API`.
* Each component must include tests, documentation, and observability hooks defined in Phase 1.

**3. Mandatory Quality & Finalization Rules**
* Organize code under `<src_root>/application`, `<src_root>/domain`, and `<src_root>/infrastructure` per architecture structure.
* Maintain `backend/CHANGELOG.md` and update `backend_quality_checklist.md` as items complete.
* Avoid touching frontend/networking/security directories except when defining contracts or stubs needed by backend.

**4. Directive Section: Backend Phase 2 Tasks**
* **Input Context:**
    * Backend Phase 1 plan, architecture guardrails, interface catalog.
    * Data schema definitions and infrastructure requirements.

* **Execution Tasks (sequential):**
    - [ ] **Task 2.1: Project Scaffolding** *(Setup)*
        - [ ] Set up folder structure, dependency injection container, and build tooling per standards.
        - [ ] Create base interfaces for services and repositories.
    - [ ] **Task 2.2: Domain Model Implementation** *(Domain)*
        - [ ] Implement aggregates, value objects, and domain events with invariants enforced.
        - [ ] Write unit tests validating domain behaviour without infrastructure dependencies.
    - [ ] **Task 2.3: Application Service Layer** *(Business Logic)*
        - [ ] Implement use-case services orchestrating domain operations via repositories and external service ports.
        - [ ] Add application-level validation, error handling, and logging.
    - [ ] **Task 2.4: Infrastructure Adapters** *(Adapters)*
        - [ ] Implement repository adapters, external API clients, and messaging gateways respecting interface contracts.
        - [ ] Configure transaction management and persistence mappings.
    - [ ] **Task 2.5: Testing & Observability** *(Quality)*
        - [ ] Create unit and integration tests hitting coverage targets; include contract tests for external interfaces.
        - [ ] Instrument logging/metrics per observability requirements.
    - [ ] **Task 2.6: Documentation & Readiness** *(Documentation)*
        - [ ] Update developer documentation covering service endpoints, domain diagrams, and adapter configuration.
        - [ ] Record outstanding issues or dependencies for integration phase.

* **Internal Success Criteria:** All planned backend components implemented with tests and docs; quality checklist satisfied; no layer violations.
* **Internal Verification Method:** Review dependency graph ensuring only allowed edges exist; confirm tests pass and documentation updated.

**5. Test Reporting Protocol (Internal)**
Log unit/integration test outcomes in `docs/Test_Result_Analysis.md` tagged `BACK-PH2`.

**6. Final Instruction for this Phase**
Package backend modules for integration testing and alert networking/security tracks of any required configuration.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
