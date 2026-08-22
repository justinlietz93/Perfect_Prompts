**Subject: Phase 2: Networking Track — Provision Connectivity & Core Infrastructure for [Project Name]**

**Date:** [Enter Current Date]
**Time:** [Enter Current Time & UTC Offset]

**1. Overall Purpose**
Provision network resources according to the approved topology, establishing secure connectivity for all tracks. Work must be limited to networking components (VPCs/VNETs, subnets, gateways, firewalls, load balancers, DNS, etc.).

**2. Core Execution Principles & Global Rules (MANDATORY)**
* Follow topology design, environment map, and quality checklist from Phase 1.
* Apply standards `NET-PROV`, `INFRA-AS-CODE`, `SEC-EDGE`, `OBS-NET`, and `DR-NET`.
* All provisioning must be expressed as infrastructure-as-code (IaC) when possible.

**3. Mandatory Quality & Finalization Rules**
Store IaC templates, configuration files, and documentation in `networking/outputs/phase-2/`. Track changes via version control, include tagging strategy, and document rollback procedures.

**4. Directive Section: Networking Phase 2 Tasks**
* **Input Context:**
    * Topology diagrams, environment mapping, dependency briefs.
    * Cloud provider accounts or datacenter configuration guides.

* **Execution Tasks (sequential):**
    - [ ] **Task 2.1: IaC Framework Setup** *(Setup)*
        - [ ] Configure IaC tooling (Terraform/Pulumi/etc.) with remote state and policy enforcement.
        - [ ] Establish module/library structure for reusable networking components.
    - [ ] **Task 2.2: Core Network Provisioning** *(Implementation)*
        - [ ] Create VPCs/VNETs, subnets, routing tables, and gateways per environment.
        - [ ] Implement segmentation and isolation (public/private subnets, service tiers).
    - [ ] **Task 2.3: Security Edge Configuration** *(Security)*
        - [ ] Define firewall rules, security groups, and network ACLs meeting security track requirements.
        - [ ] Integrate with identity-aware proxies or zero-trust solutions as specified.
    - [ ] **Task 2.4: Traffic Management Setup** *(Operations)*
        - [ ] Provision load balancers, API gateways, and DNS entries per component needs.
        - [ ] Document routing policies, health checks, and failover behaviour.
    - [ ] **Task 2.5: Observability Enablement** *(Quality)*
        - [ ] Configure flow logs, metrics, and alerting for critical networking components.
        - [ ] Ensure logging destinations align with operations tooling.
    - [ ] **Task 2.6: Documentation & Validation** *(Documentation)*
        - [ ] Update `networking_runbook.md` with provisioning steps, dependencies, and verification commands.
        - [ ] Record outstanding tasks for integration phase.

* **Internal Success Criteria:** Networking resources provisioned via IaC, security controls enforced, documentation updated.
* **Internal Verification Method:** Run IaC plan/apply validations, review logs/metrics, confirm configuration matches topology.

**5. Test Reporting Protocol (Internal)**
Log provisioning validation results in `docs/Test_Result_Analysis.md` tagged `NET-PH2`.

**6. Final Instruction for this Phase**
Notify backend and security tracks that networking infrastructure is available for integration, providing access instructions.

**7. Contextual Footer**
*(Generated on: [Enter Current Date & Time]. Location: [Enter Locale].)*
