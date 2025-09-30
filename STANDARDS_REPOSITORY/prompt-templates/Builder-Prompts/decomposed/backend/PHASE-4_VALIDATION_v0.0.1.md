**Subject: Phase 4: Backend Validation, Reliability Hardening, and Pre-Release Assurance for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt initiates **Phase 4: Backend Validation**. The agent must ensure backend services meet functional, performance, reliability, and security expectations before release. Objectives:
    a. Execute comprehensive automated and manual validation across APIs, messaging workflows, and data persistence.
    b. Perform load, stress, and resilience testing; validate observability and alerting.
    c. Verify security posture (authz, encryption, secrets management) and compliance requirements.
    d. Capture evidence, log defects, perform remediation cycles until success criteria satisfied.
    e. Update documentation (test reports, risk register) reflecting validation status.

**2. Core Execution Principles & Global Rules**
* Enforce Apex Standards; maintain dependency rule and repository pattern integrity during fixes.
* Execute validation plan sequentially and perform rigorous internal verification referencing relevant rules.
* Iterate on remediation for failing scenarios; document all outcomes.
* Log validation activities per Section 5.

**3. Mandatory Quality & Finalization Rules**
Focus on:
* Testing Standards (`TEST-*`: unit, integration, contract, load, soak, chaos).
* Performance Standards (`QUAL-PERF`, latency/error budgets, throughput targets).
* Security Standards (`SEC-*`: authN/authZ, data protection, secrets management).
* Reliability & Resilience (`QUAL-RES`, fallback strategies).
* Documentation Standards (`DOC-*`, `FINAL-*` readiness checks).

**4. Directive Section: Phase 4 - Backend Validation Execution**

* **Inputs:**
    * `[Validation Plan Template]`, `[Load Test Scenarios]`, `[Security Checklist]`.
    * `[Monitoring/Alerting Configuration]`.
    * `[Path to Integrated Backend Output]`.

* **Validation Workflow:**
    1.  **Plan Validation Campaign:**
        * Inventory test suites covering APIs, domain workflows, messaging, background jobs, database migrations.
        * Define success metrics and acceptance thresholds for each suite.
        * Schedule execution order and environment preparation.
    2.  **Execute Automated Suites:**
        * Run unit/integration/contract suites; ensure environment parity.
        * Execute load/stress/soak tests capturing latency, throughput, resource utilization.
        * Run chaos/resilience scenarios (network latency injection, dependency failure) if applicable.
    3.  **Security Validation:**
        * Validate authentication/authorization flows, token handling, secrets storage, encryption at rest/in transit.
        * Run SAST/DAST/security scans; evaluate vulnerabilities and remediate.
    4.  **Observability & Alerting Verification:**
        * Confirm metrics, logs, traces cover critical operations.
        * Test alert thresholds and escalation workflows.
    5.  **Defect Management & Remediation:**
        * Log defects with severity and remediation plan.
        * Iterate on fixes, rerun impacted tests, confirm compliance with dependency rule.
    6.  **Evidence & Documentation:**
        * Compile validation report summarizing tests, metrics, residual risks.
        * Update risk register, change log, and readiness checklist.

* **Internal Success Criteria:** All planned tests executed; thresholds met or documented exceptions; no unresolved critical defects; documentation/logs updated.
* **Internal Verification Method:** Perform final audit vs validation plan, verify evidence attachments, confirm monitoring/alerting results, ensure architectural boundaries preserved.

**5. Test Reporting Protocol**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Service/API/Workflow), Test Type (load, contract, chaos), Metrics (latency, error %, resource usage), Status, Remediation.
* **Update Frequency:** After each suite run and remediation cycle.

**6. Final Instruction**
Execute the validation campaign, deliver summarized metrics, remediation logs, and go/no-go recommendation for backend release readiness.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
