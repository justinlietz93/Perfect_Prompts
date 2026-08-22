**Subject: Phase 3: Networking Track — Cross-System Connectivity Validation for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Phase 3 verifies that networking components interoperate correctly with backend services, security controls, and external integrations. The worker agent focuses on connectivity, routing, and resilience checks, leaving application fixes to other tracks.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Align with integration dashboard and architecture risk register.
* Apply `NET-TEST`, `SEC-NET`, `DR-NET`, and `OBS-NET` standards.
* Document any configuration changes as IaC updates.

**3. Mandatory Quality & Finalization Rules**
Store evidence in `networking/outputs/phase-3/`, including connectivity test logs, latency measurements, and failover drills. Update runbooks and quality checklist as items close.

**4. Directive Section: Networking Phase 3 Tasks**
* **Input Context:**
    * Backend service endpoints, security policies, monitoring dashboards.
    * Integration dashboard schedule and ADRs.

* **Execution Tasks (sequential):**
    - [ ] **Task 3.1: Connectivity Verification** *(Testing)*
        - [ ] Validate routing between tiers, ensuring firewall rules allow expected traffic only.
        - [ ] Run automated ping/traceroute/API connectivity checks per environment.
    - [ ] **Task 3.2: Performance & Latency Assessment** *(Performance)*
        - [ ] Measure network latency and throughput versus NFR targets.
        - [ ] Identify hotspots and propose optimizations without implementing backend changes.
    - [ ] **Task 3.3: Resilience & Failover Tests** *(Reliability)*
        - [ ] Simulate component failures (link loss, gateway outage) and confirm failover mechanisms operate as designed.
        - [ ] Document recovery times and alerting events.
    - [ ] **Task 3.4: Security Alignment** *(Security)*
        - [ ] Review network security logs for anomalies, confirm segmentation policies enforced.
        - [ ] Coordinate with security track on penetration test findings related to networking.
    - [ ] **Task 3.5: Reporting & Coordination** *(Communication)*
        - [ ] Update `networking_integration_report.md` summarizing status, issues, and dependencies.
        - [ ] Communicate required changes to backend/security teams with ticket references.

* **Internal Success Criteria:** Connectivity verified, performance meets targets, failover validated, no unresolved critical networking issues.
* **Internal Verification Method:** Review reports, ensure evidence stored, confirm scope remains networking-specific.

**5. Test Reporting Protocol (Internal)**
Log integration test outcomes in `docs/Test_Result_Analysis.md` tagged `NET-PH3`.

**6. Final Instruction for this Phase**
Confirm networking readiness for validation/testing phases and escalate any unresolved blockers.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
