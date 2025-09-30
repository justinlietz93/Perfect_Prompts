**Subject: Phase 4: Networking Track — Network Validation & Compliance Certification for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Validate that the networking environment meets functional, security, compliance, and resilience requirements prior to release. The worker agent produces objective evidence for architecture and security review.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Apply standards `NET-VAL`, `SEC-AUDIT`, `DR-TEST`, `OPS-NET`, and `COMPLIANCE-NET`.
* Utilize production-like environments and configuration states.
* Any change requests must be tracked via IaC with peer review.

**3. Mandatory Quality & Finalization Rules**
Store validation outputs in `networking/outputs/phase-4/`, including audit results, penetration test evidence, failover metrics, and compliance certificates.

**4. Directive Section: Networking Phase 4 Tasks**
* **Input Context:**
    * Integration reports, security testing results, compliance requirements.
    * Monitoring dashboards and alerting configurations.

* **Execution Tasks (sequential):**
    - [ ] **Task 4.1: Validation Plan Alignment** *(Planning)*
        - [ ] Coordinate with security/testing teams on scope, tools, and success criteria.
        - [ ] Document plan in `networking_validation_plan.md`.
    - [ ] **Task 4.2: Functional & Performance Verification** *(Testing)*
        - [ ] Execute network performance tests (latency, bandwidth, packet loss) against targets.
        - [ ] Verify load balancer health checks and routing policies under load.
    - [ ] **Task 4.3: Security & Compliance Audits** *(Security)*
        - [ ] Perform firewall rule audits, port scans, and policy compliance checks.
        - [ ] Capture evidence for encryption-in-transit and segmentation requirements.
    - [ ] **Task 4.4: Resilience & Disaster Recovery Tests** *(Reliability)*
        - [ ] Run failover drills, multi-region cutover tests, or backup link activation per DR strategy.
        - [ ] Document RTO/RPO results.
    - [ ] **Task 4.5: Evidence Compilation** *(Documentation)*
        - [ ] Assemble `networking_validation_report.md` summarizing outcomes, issues, and sign-offs from security/operations.

* **Internal Success Criteria:** Validation plan executed, evidence compiled, outstanding issues documented with owners.
* **Internal Verification Method:** Ensure each requirement and standard cited has matching evidence; confirm artifacts stored correctly.

**5. Test Reporting Protocol (Internal)**
Log validation outcomes in `docs/Test_Result_Analysis.md` tagged `NET-PH4`.

**6. Final Instruction for this Phase**
Submit validation report to architecture and security for certification sign-off before release preparation.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
