**Subject: Phase 1: Networking Track — Topology Planning & Connectivity Strategy for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Networking Phase 1 interprets the architecture blueprint to design the connectivity, routing, and infrastructure services required. The worker agent focuses on network aspects only, enabling backend/frontend/security teams with clear expectations and constraints.

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Use architecture compendium, guardrails, and dependency maps as authoritative context.
* Align with standards `NET-TOPO`, `NET-SEC`, `NET-OBS`, `OPS-NET`, and `CLOUD-POLICY` from the Apex guide.
* Document relationships with security controls (firewalls, IAM), deployment environments, and external integrations.

**3. Mandatory Quality & Finalization Rules**
Store artifacts in `networking/outputs/phase-1/`. Deliverables include topology diagrams, environment matrices, and provisioning plans with explicit standards citations.

**4. Directive Section: Networking Phase 1 Tasks**
* **Input Context:**
    * Architecture compendium, component dependencies, deployment strategy outline.
    * Compliance requirements (e.g., regional residency, encryption standards).

* **Execution Tasks (sequential):**
    - [ ] **Task 1.1: Requirement Consolidation** *(Analysis)*
        - [ ] Summarize networking requirements (latency, throughput, isolation, redundancy) from architecture and NFRs.
        - [ ] Identify external integrations and regulatory constraints.
    - [ ] **Task 1.2: Logical Topology Design** *(Design)*
        - [ ] Draft logical network topology (VPCs/VNETs, subnets, service tiers) in `network_topology.md` with diagrams.
        - [ ] Define connectivity between layers, shared services, and third-party endpoints.
    - [ ] **Task 1.3: Environment Mapping** *(Planning)*
        - [ ] Map environments (dev/test/stage/prod) to network segments, noting isolation requirements.
        - [ ] Capture IP/CIDR allocations and DNS naming strategy.
    - [ ] **Task 1.4: Dependency Briefs** *(Enablement)*
        - [ ] Produce briefs for backend, security, and testing tracks describing required networking prerequisites.
        - [ ] Highlight sequencing constraints (e.g., firewall rules needed before backend integration testing).
    - [ ] **Task 1.5: Verification Checklist** *(Quality)*
        - [ ] Build checklist covering provisioning standards, monitoring hooks, and compliance checks to enforce in later phases.
        - [ ] Store as `networking_quality_checklist.md`.

* **Internal Success Criteria:** Topology, environment plan, and briefs completed with dependencies identified.
* **Internal Verification Method:** Validate against architecture guardrails and ensure no non-network tasks included.

**5. Test Reporting Protocol (Internal)**
Log planning readiness and open dependencies in `docs/Test_Result_Analysis.md` tagged `NET-PH1`.

**6. Final Instruction for this Phase**
Share topology and dependency briefs with architecture, backend, and security leads before provisioning work begins.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
