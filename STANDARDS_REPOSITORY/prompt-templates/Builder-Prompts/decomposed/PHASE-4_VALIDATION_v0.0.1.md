**Subject: Phase 4: System-Level Validation, Performance Hardening, and Defect Eradication for [Project Name]**

**Date:** [Customizer: Insert Current Date]
**Time:** [Customizer: Insert Current Time with UTC Offset]

**1. Overall Purpose**
This prompt governs **Phase 4: System Validation & Hardening** of **[Project Name]**. The executing agent must:
    a. Expand integration outcomes into full-system validation covering end-to-end functional flows, NFR targets, and resilience scenarios.
    b. Develop and execute comprehensive automated and manual test suites (functional, regression, performance, security) aligned with Phase 1 architectural drivers and updated requirements.
    c. Identify, triage, and eliminate defects or gaps exposed during validation while preserving architectural integrity and standards compliance.
    d. Produce consolidated validation evidence, metrics, and residual risk assessments for release readiness review.

**2. Core Execution Principles & Global Rules (VALIDATION FOCUS)**
*(Customizer Note: Keep consistent phrasing; adjust bracketed values.)*

* **Apex Standards Adherence:** Strictly comply with the **Apex Software Compliance Standards Guide** located at `[User Input: Path to Standards Guide]`. Every test artifact, bug fix, and documentation update must include precise `[(Rule #X: CODE)](...)` references.
* **Sequential Validation Workflow:** Follow the Phase 4 plan sequentially (`- [ ]`), ensuring each Task meets `Internal Success Criteria` verified via `Internal Verification Method` before progressing.
* **Defect Handling Discipline:** On encountering failures, perform structured root-cause analysis, implement corrective actions, re-run impacted tests, and update logs before proceeding.
* **Evidence-Driven Reporting:** Capture metrics, logs, and artifacts for each validation activity. Maintain traceability between tests and requirements/NFRs.
* **Autonomous Operation:** Operate independently while updating the internal Test Reporting log per Section 5.

**3. Mandatory Quality & Finalization Rules (Validation Emphasis)**
Enforce all applicable standards in the **Apex Software Compliance Standards Guide** (`[User Input: Path to Standards Guide]`), prioritizing:
* Testing & Verification (Section 14: `TEST-*`, including `TEST-AUTO`, `TEST-COV`, `TEST-PERF`)
* Security (Section 13: `SEC-*`, e.g., `SEC-AUTH`, `SEC-INPUT`)
* Reliability & Resilience (Reference `QUAL-REL` or equivalent rules if defined)
* Implementation Correctness (Section 19: `IMPL-*`)
* Documentation (Section 18: `DOC-*`, ensure test evidence & runbooks)
* Configuration Management (Section 12: `CONF-*` for test environments)
* Final Validation Protocols (Section 21: `FINAL-*`)

**4. Directive Section: Phase 4 - Validation & Hardening**

* **Context Provided by User (Customizer Inputs):**
    * `[User Input: Project Name]`
    * `[User Input: Phase 1 Architectural Drivers & NFR Targets Path]`
    * `[User Input: Phase 2 & 3 Deliverables Paths]`
    * `[User Input: Path to Standards Guide]`
    * `[User Input: Current Codebase/Test Harness Location]`

* **Instructions for Worker LLM:**

    1.  **Establish Validation Objectives:**
        * Extract prioritized functional scenarios and NFR targets from Phase 1 outputs.
        * Map each scenario/target to concrete validation activities (test suites, tooling, data requirements).
        * Confirm availability of necessary environments, fixtures, and monitoring hooks.

    2.  **Construct Comprehensive Validation Plan:**
        * Produce a detailed `Phase -> Task -> Step` plan (`- [ ]`) covering:
            * End-to-end functional regression suites.
            * Data integrity verification.
            * Performance, load, and stress testing.
            * Security and privacy assessments (static, dynamic as applicable).
            * Resilience/chaos scenarios if specified.
            * Bug triage and remediation workflow.
            * Evidence aggregation & reporting tasks.
        * Reference appropriate standards in each step.

    3.  **Execute Validation Activities:**
        * Implement or update required tests/harnesses.
        * Run all planned test suites, capturing metrics & logs.
        * Document failures with root cause notes, remediate defects, and re-run affected tests until passing.

    4.  **Compile Validation Evidence:**
        * Aggregate test reports, coverage summaries, performance charts, and security scan outputs.
        * Update documentation (validation summary, risk log, decision records) to reflect outcomes.
        * Ensure traceability from requirements/NFRs to test results.

    5.  **Self-Assessment & Exit Criteria:**
        * Confirm all validation objectives are satisfied or residual risks documented with mitigation plans.
        * Verify all standards references and internal verifications are complete.
        * Prepare readiness recommendation for Phase 5 (Release & Transition).

* **Internal Success Criteria (Worker Self-Check):** All planned validation suites executed with passing results or documented residual risks; defects resolved; evidence compiled; documentation updated.
* **Internal Verification Method:** Review test outputs, confirm remediation actions, ensure logs updated, cross-check standards compliance for every modified artifact.

**5. Test Reporting Protocol (Internal)**
* **Log File Location:** `docs/Test_Result_Analysis.md`
* **Data Points per Entry:** Date/Time, Scope (Validation Phase), Test Suite/Scenario, Result, Metrics (coverage %, latency, throughput, error rate, security findings), Remediation Notes.
* **Update Frequency:** After each executed suite and upon defect resolution.

**6. Final Instruction**
Execute the validation directives sequentially. Upon completion:
    * Deliver a validation summary with key metrics, pass/fail counts, and remaining risks.
    * Provide locations of generated reports/artifacts.
    * Supply the executed validation plan with all tasks marked `- [x]`.
    * State readiness recommendation for progression to Phase 5.

**7. Contextual Footer**
*(Instructions generated: [Customizer Timestamp]. Location context: [Customizer Location])* 
