**Subject: Phase 5: Frontend Release Preparation, Documentation Finalization, and Launch Execution for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt covers **Phase 5: Frontend Release**. The agent must ensure the integrated UI is production-ready, thoroughly documented, and smoothly deployed. Objectives include:
    a. Finalizing user-facing documentation, changelogs, and design system updates.
    b. Preparing deployment artifacts (bundles, manifests, environment configs) aligned with performance/security requirements.
    c. Coordinating release readiness reviews, risk assessments, and stakeholder sign-off.
    d. Executing launch plan (staged rollout, feature flags) and monitoring initial telemetry.
    e. Establishing operational handoff materials, runbooks, and support escalation paths.

**2. Core Execution Principles & Global Rules**
* Adhere to Apex Standards Guide, especially `FINAL-*`, `DOC-*`, `CONF-*`, and `OPER-*` rules.
* Maintain dependency discipline; ensure release artifacts respect Presentation layer boundaries.
* Execute release plan sequentially and verify success criteria before marking tasks complete.
* Log all release activities, approvals, and telemetry checkpoints per Section 5.

**3. Mandatory Quality & Finalization Rules**
* Documentation Standards (`DOC-*`: user guides, admin notes, storybook updates).
* Configuration & Deployment Standards (`CONF-*`, `DEPL-*`): environment configs, CD pipelines.
* Security Standards (`SEC-*`): CSP, integrity hashes, vulnerability scans.
* Operational Standards (`OPER-*`, `FINAL-*`): monitoring, alerting, rollback readiness.
* Testing Standards (`TEST-*`): smoke tests post-deploy.

**4. Directive Section: Phase 5 - Frontend Release Execution**

* **Inputs Required:**
    * `[Release Notes Template]`, `[Documentation Repositories]`.
    * `[Deployment Pipeline Config]` and `[Environment Variables Spec]`.
    * `[Monitoring/Alerting Setup]` and `[Runbook Template]`.
    * `[Stakeholder Contact List]` for approvals and communication.

* **Release Plan Requirements:**
    1.  **Documentation Finalization:**
        * Update end-user documentation, changelog, and design system catalog entries.
        * Ensure Storybook/visual catalogs reflect final component states.
    2.  **Deployment Packaging:**
        * Produce optimized bundles with integrity hashes and environment-specific manifests.
        * Validate CI/CD pipelines (lint, test, build, deploy) and ensure AMD-friendly build options per policy.
        * Confirm feature flags/rollout toggles configured per risk plan.
    3.  **Readiness Review & Approvals:**
        * Conduct release readiness review referencing validation results and residual risks.
        * Capture approvals from product, security, and operations stakeholders.
    4.  **Launch Execution:**
        * Execute deployment via defined pipeline (blue/green, canary, or feature-flag gating).
        * Run post-deployment smoke tests, accessibility spot checks, and performance sampling.
        * Monitor telemetry dashboards (Core Web Vitals, error rates) and document observations.
    5.  **Operational Handoff:**
        * Update runbooks, support contact flows, incident response procedures.
        * Provide knowledge transfer materials (release summary, known issues, troubleshooting tips).
        * Schedule follow-up review to assess launch outcomes.

* **Internal Success Criteria:** Documentation completed; deployment artifacts validated; approvals recorded; launch executed with successful telemetry; operational handoff finalized; logs updated.
* **Internal Verification Method:** Review release checklist, confirm artifact integrity hashes, verify documentation updates, ensure monitoring alerts configured, validate runbook completeness.

**5. Test Reporting Protocol (Release Focus)**
* **Log File:** `docs/Test_Result_Analysis.md`
* **Data Points:** Date/Time, Scope (Release phase activity), Tests (smoke, monitoring checks), Metrics (error rate, Core Web Vitals post-launch), Status, Notes.
* **Update Frequency:** After each major release task and post-deployment validation cycle.

**6. Final Instruction**
Complete all release tasks, provide final status summary including documentation links, deployment identifiers, telemetry snapshots, and confirm readiness for steady-state operations.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
