**Subject: Phase 3: Backend Integration, Cross-Service Assembly, and Infrastructure Enablement for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt initiates **Phase 3: Backend Integration**. The agent must assemble completed backend components, activate shared infrastructure, and validate service interactions. Objectives:
    a. Inventory completed services, domain modules, repositories, and adapters ready for integration.
    b. Compose application service orchestration, pipeline wiring, and DI container registrations.
    c. Configure infrastructure dependencies (databases, message brokers) ensuring repository implementations align with interfaces.
    d. Execute integration, contract, and performance smoke tests across service boundaries.
    e. Document integration results, remediation, and configuration changes.

**2. Core Execution Principles & Global Rules**
* Enforce Apex Standards, Hybrid-Clean dependency rule, and repository pattern.
* Execute integration plan sequentially with `- [ ]` tasks.
* Perform internal verification referencing relevant rules (`TEST-INTEG`, `DATA-TRANS`, `CONF-MAN`).
* Apply iterative remediation for integration defects.
* Log all activities per Section 5.

**3. Mandatory Quality & Finalization Rules**
Maintain:
* Code & Architecture Standards (`QUAL-*`, `ARCH-*`).
* Security & Compliance (`SEC-*` for secrets, auth flows, encryption).
* Data Consistency (`DATA-*`, migration checks).
* Testing Standards (`TEST-INTEG`, `TEST-CONTRACT`, `TEST-PERF-SMOKE`).
* Configuration Management (`CONF-*`, environment parity).
* Documentation Updates (`DOC-*` for integration diagrams, runbooks).

**4. Directive Section: Phase 3 - Backend Integration Execution**

* **Inputs:**
    * `[Path to Phase 2 Outputs]`: Completed component plans and code references.
    * `[Infrastructure Configuration Files]`: Database/messaging configuration templates.
    * `[Path to Standards Guide]`
    * `[Integration Targets List]`: Services/modules ready for assembly.

* **Integration Workflow:**
    1.  **Context Assembly:**
        * Confirm readiness of each component via Phase 2 plan completion.
        * Map required DI registrations, transaction scopes, and configuration keys.
        * Identify shared resources (connection pools, caches) requiring setup.
    2.  **Integration Plan Generation:**
        * Produce sequential plan for wiring services, repositories, adapters, messaging subscriptions, and background jobs.
        * Include tasks for schema migrations, seed data, and environment configuration updates.
        * Define verification tasks: contract tests, integration suites, health checks, performance smoke tests.
        * Reference relevant standards for each task, and define success criteria/verification method.
    3.  **Execute Plan:**
        * Apply DI configuration and module registration updates.
        * Configure infrastructure resources (database migrations, queue/topic provisioning) per plan.
        * Run integration/contract/performance smoke tests; capture results.
        * Resolve defects iteratively until success criteria met.
        * Update documentation (sequence diagrams, deployment notes) and logs.
    4.  **Compliance Review:**
        * Ensure dependency rule intact (no infrastructure leaking into business logic).
        * Validate configuration secrets managed securely.
        * Confirm tests and monitoring hooks (health endpoints) operational.

* **Internal Success Criteria:** Integration plan executed, services communicating correctly, tests passing, configuration documented, logs updated.
* **Internal Verification Method:** Final audit of plan vs execution, review dependency graph, rerun targeted tests if necessary.

**5. Test Reporting Protocol**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Service pair/module), Test Type (integration/contract/smoke), Metrics (latency, error rate), Status, Findings.
* **Update Frequency:** After each integration cycle.

**6. Final Instruction**
Complete backend integration per plan, provide summary of wired services, configuration changes, test outcomes, and remediation steps.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
