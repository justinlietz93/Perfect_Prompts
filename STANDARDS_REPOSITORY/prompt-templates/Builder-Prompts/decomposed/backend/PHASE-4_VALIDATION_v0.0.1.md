**Subject: Phase 4: Backend Track — Service Validation & Reliability Assurance for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Validate backend services against functional, performance, reliability, and security requirements. The worker agent compiles objective evidence demonstrating that backend components comply with architecture standards and are ready for release.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Apply `TEST-SVC`, `PERF-API`, `RESILIENCE`, `SEC-API`, and `DOC-VAL` standards.
* Use release-candidate builds and production-like data fixtures.
* Do not modify frontend/security artifacts except to request fixes.

**3. Mandatory Quality & Finalization Rules**
Store results in `backend/outputs/phase-4/`. Include test reports, performance metrics, chaos/resilience findings, and compliance summaries.

**4. Directive Section: Backend Phase 4 Tasks**
* **Input Context:**
    * Integration report, testing track validation plan, architecture certification checklist.
    * Monitoring/observability requirements.

* **Execution Tasks (sequential):**
    - [ ] **Task 4.1: Validation Plan Alignment** *(Planning)*
        - [ ] Coordinate scope with testing track; define target environments and data sets.
        - [ ] Document plan in `backend_validation_plan.md`.
    - [ ] **Task 4.2: Functional & Regression Testing** *(Testing)*
        - [ ] Execute automated regression suite covering service contracts and edge cases.
        - [ ] Perform exploratory tests for complex workflows.
    - [ ] **Task 4.3: Performance & Load Testing** *(Performance)*
        - [ ] Run load/stress tests hitting defined throughput and latency goals.
        - [ ] Capture resource utilization metrics and compare to budgets.
    - [ ] **Task 4.4: Resilience & Chaos Exercises** *(Reliability)*
        - [ ] Conduct failure injection scenarios (e.g., dependency outage, network latency) ensuring graceful degradation.
        - [ ] Document recovery times and alerting behaviour.
    - [ ] **Task 4.5: Security Verification** *(Security)*
        - [ ] Validate authentication/authorization flows, input validation, and data protection requirements.
        - [ ] Coordinate with security track on penetration test findings and remediations.
    - [ ] **Task 4.6: Evidence Compilation** *(Documentation)*
        - [ ] Assemble `backend_validation_report.md` summarizing results, open issues, and sign-off fields.

* **Internal Success Criteria:** Validation plan executed, evidence recorded, no unresolved critical defects; sign-offs prepared.
* **Internal Verification Method:** Ensure each requirement traced to validation evidence; confirm results stored and referenced.

**5. Test Reporting Protocol (Internal)**
Update `docs/Test_Result_Analysis.md` with validation outcomes tagged `BACK-PH4`.

**6. Final Instruction for this Phase**
Provide validation report to architecture and testing leads for certification approval.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
