**Subject: Phase 5: Backend Release Preparation, Deployment Finalization, and Operational Handoff for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt governs **Phase 5: Backend Release**. The agent must finalize documentation, deployment assets, and operational readiness for backend services. Objectives:
    a. Prepare deployment artifacts (container images, manifests, migration packages) compliant with standards.
    b. Finalize documentation (runbooks, API references, change logs, ADR updates).
    c. Coordinate release readiness reviews, risk assessments, and approvals.
    d. Execute deployment plan (staged/canary/blue-green) and validate post-deploy health.
    e. Establish monitoring, alerting, and support processes for operations handoff.

**2. Core Execution Principles & Global Rules**
* Enforce Apex Standards: `DEPL-*`, `CONF-*`, `DOC-*`, `FINAL-*`, `OPER-*`.
* Maintain dependency rule; ensure release artifacts do not introduce forbidden couplings.
* Execute release plan sequentially; verify success criteria before completion.
* Log release activities, approvals, and telemetry checks per Section 5.

**3. Mandatory Quality & Finalization Rules**
* Deployment Standards (`DEPL-*`, `CONF-*`): pipelines, configuration segregation, secrets management.
* Security Standards (`SEC-*`): vulnerability scans, key rotation, compliance evidence.
* Operational Standards (`OPER-*`): monitoring dashboards, alerting, SLO/SLA definitions.
* Documentation Standards (`DOC-*`): runbooks, API release notes.
* Final Verification Standards (`FINAL-*`): go/no-go checklist, rollback plan.

**4. Directive Section: Phase 5 - Backend Release Execution**

* **Inputs:**
    * `[Deployment Pipeline Config]`, `[Infrastructure as Code Templates]`.
    * `[Release Notes Template]`, `[Runbook Template]`.
    * `[Monitoring/Alerting Setup]`, `[Support Roster]`.
    * `[Validation Report]` from Phase 4.

* **Release Workflow:**
    1.  **Documentation & Communication:**
        * Update API documentation, change logs, ADRs, and release communications.
        * Prepare stakeholder announcements detailing scope, risks, rollback plan.
    2.  **Deployment Packaging:**
        * Build/sign container images or artifacts, attach provenance metadata.
        * Apply configuration for each environment using secure secrets management.
        * Validate CI/CD pipeline steps (build, test, deploy) and AMD-compatible dependencies.
    3.  **Readiness Review:**
        * Conduct release readiness meeting summarizing validation results, residual risks, mitigation plans.
        * Obtain approvals from product, security, operations leads.
    4.  **Launch Execution:**
        * Execute deployment (canary/blue-green/rolling) as defined.
        * Run post-deploy smoke/health checks, database migration verification, and monitor telemetry (latency, error rate, queue depth).
        * Capture evidence and respond to anomalies.
    5.  **Operational Handoff:**
        * Update runbooks, incident response procedures, on-call rotations.
        * Configure dashboards and alerts; verify notifications reach correct channels.
        * Schedule post-release review.

* **Internal Success Criteria:** Documentation complete; artifacts validated; approvals recorded; deployment executed successfully; monitoring active; logs updated.
* **Internal Verification Method:** Review release checklist, verify artifact integrity, confirm documentation links, ensure monitoring alerts firing, validate rollback plan is ready.

**5. Test Reporting Protocol**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Release Task, Tests (smoke, health checks), Metrics (latency, error rate, resource usage), Status, Notes.
* **Update Frequency:** After each release activity and post-deploy validation.

**6. Final Instruction**
Execute release workflow, deliver final summary with deployment identifiers, telemetry snapshots, documentation references, and confirm transition to operations.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
