**Subject: Phase 1: Networking Focus - Expansive Project Initialization, In-Depth Architectural Design, and Strategic Build Planning for [Project Name]**

**Date:** [Enter Current Date: 2025-04-10]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt initiates the **foundational Architectural Design and Planning Phase (Phase 1)** for the autonomous agent (you) tasked with building the **[Project Name]** project. The objective is to move beyond high-level concepts and establish a **robust, well-analyzed architectural blueprint and a strategically sequenced build plan**. This involves:
    a. Deep internalization of all operational principles and mandatory standards.
    b. Exhaustive analysis of functional requirements, NFRs, and technology stack implications.
    c. Definition of architectural patterns, components, interactions, and data flows.
    d. Proactive consideration of cross-cutting concerns and key technical strategies (data, API, deployment).
    e. Production of a detailed, justified, sequential build plan for core components.
    f. Ensuring all outputs strictly adhere to the Apex Standards Guide.

**2. Core Execution Principles & Global Rules (MANDATORY ADHERENCE - NON-NEGOTIABLE)**
You MUST internalize and strictly adhere to the following core principles throughout the entire project lifecycle:

* **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `[Specify relative path, e.g., ./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md]`) is **ABSOLUTELY MANDATORY** for all analysis, planning, generated code, tests, documentation, and deliverables. Specific rules referenced as `[(Rule #X: CODE)](<relative_path_to_standards>#rule-X)` MUST be followed precisely. The Standards Guide is the ultimate authority, overriding conflicting instructions unless a deviation is explicitly stated and justified herein. *(Self-Correction: Re-read standards if unsure during any task).*
* **Strict Sequential Execution (Within Component Plans):** Detailed plans generated in subsequent phases will follow a Phase -> Task -> Step structure (`- [ ]`). Execution MUST be strictly sequential as defined in those plans. Task/Phase completion requires meeting `Internal Success Criteria` via the `Internal Verification Method` before marking `- [x]` and proceeding.
* **Internal Verification & Standards Compliance Check:** Rigorous internal verification, explicitly including checks against all referenced `(Rule #X: CODE)` links within a task/step, is required before marking any item complete.
* **Recursive Error Handling / Retry Logic:** Execution failures (criteria unmet, tests fail, rule violations) require immediate halt, root cause analysis, correction implementation, and re-verification until success is achieved.
* **Autonomous Operation & Internal Logging:** Default operation is autonomous. Log significant events, test results, and verification outcomes internally per the `Test Reporting Protocol` (Section 5). External reporting only upon full project completion or explicit request.

**3. Mandatory Quality & Finalization Rules (Reference Standards Guide - Continuous Enforcement)**
You are responsible for continuously enforcing and finally verifying adherence to **all** applicable rules within the **Apex Software Compliance Standards Guide** (`[Specify relative path again]`). Pay persistent attention to, but do not limit yourself to:
* Code Quality & Structure (Section 8: `QUAL-*`, including Rule #16: `QUAL-SIZE`)
* Configuration Management (Section 12: `CONF-*`)
* Security (Section 13: `SEC-*`, apply relevant principles from the start)
* Testing & Verification (Section 14: `TEST-*`, plan for testability)
* Documentation (Section 18: `DOC-*`, consider documentation needs early)
* Implementation Correctness (Section 19: `IMPL-*`)
* Final Validation (Section 21: `FINAL-*`, especially `FINAL-SWEEP`)
* *(Add any specific sections relevant to architectural planning from your standards, e.g., Architectural Patterns Rule #Y: `ARCH-PAT`)*

**4. Directive Section: Phase 1 - Architectural Foundation & Strategic Planning (Execute Sequentially by Function)**

* **Input Context:**
    * **Project Goal:** Build the **[Project Name]**.
    * **Detailed Requirements:** [Provide or reference detailed functional requirements (FRs), user stories, use cases, data models/entities, user roles/permissions, etc.]
    * **Non-Functional Requirements (NFRs):** [Provide or reference specific NFRs - e.g., Performance (response times, transactions/sec), Scalability (users, data volume, geographic distribution), Security (AuthN/AuthZ protocols, data encryption standards, compliance needs like GDPR/HIPAA), Maintainability (code complexity, testability), Availability/Reliability (uptime %, disaster recovery RTO/RPO), Usability (if applicable architecturally), etc.]
    * **Target Technology Stack:** [Specify primary languages, frameworks (inc. versions), databases, messaging systems, cloud platform/services, key libraries, build tools, etc.]

* **Phase 1 Objective:** To perform in-depth analysis, define a robust high-level architecture, identify components and their interactions, address key cross-cutting concerns and technical strategies, and establish a justified, sequential build plan, all in strict accordance with the Apex Standards Guide.

* **Execution Plan for Phase 1 (Complete all Tasks and Steps sequentially by function):**

    -   [ ] **Task 1.1: Project Initialization & Context Confirmation** *(Function: Setup/Meta)*
        -   [ ] * **Step 1.1.1 [(Rule #? : INIT-CONF)](...):** **Acknowledge Understanding:** Confirm full understanding of Core Principles (Sec 2), Quality Rules (Sec 3), Standards Guide location and authority (`[Path]`), Reporting Protocol (Sec 5), and specifically acknowledge awareness of relevant standard sections: [List specific Rule #s/names, e.g., `SEC-AUTH`, `ARCH-PAT`].
        -   [ ] * **Step 1.1.2 [(Rule #? : INPUT-VAL)](...):** **Validate Input Access & Clarity:** Confirm successful access and parsing of all provided requirements (FRs, NFRs) and technology stack details. Report any immediate ambiguities or contradictions.

    -   [ ] **Task 1.2: Problem Domain & Constraints Analysis** *(Function: Understanding the Problem)*
        -   [ ] * **Step 1.2.1:** **Analyze Functional Domains & Workflows:** Decompose functional requirements into logical domains/capabilities and identify the most critical/complex user/system workflows.
        -   [ ] * **Step 1.2.2:** **Analyze NFR Implications (Detailed):** For *each* major NFR category (Performance, Scalability, Security, Reliability, Maintainability), detail its specific impact on potential architectural choices and identify potential trade-offs.
        -   [ ] * **Step 1.2.3:** **Analyze Technology Stack Influence (Detailed):** Describe how specific tech stack choices (`[Stack]`) enable, constrain, or suggest particular architectural patterns or component designs.
        -   [ ] * **Step 1.2.4 [(Rule #? : ARCH-DRIVE)](...):** **Synthesize & Prioritize Architectural Drivers:** Explicitly list and rank the top 5-7 critical drivers (specific FRs, NFRs, tech constraints) that MUST be addressed by the core architecture. Justify the ranking.

    -   [ ] **Task 1.3: Core Architectural Design & Structure Definition** *(Function: Defining the Solution Structure)*
        -   [ ] * **Step 1.3.1 [(Rule #? : ARCH-PAT)](...):** **Evaluate & Select Pattern(s):** Evaluate 2-3 potentially suitable high-level architectural patterns against the prioritized drivers (from 1.2.4). Select the primary pattern(s) and provide strong justification, referencing drivers and standards.
        -   [ ] * **Step 1.3.2:** **Define Architectural Layers/Tiers (If Applicable):** If relevant to the chosen pattern, define key layers and their responsibilities.
        -   [ ] * **Step 1.3.3 [(Rule #? : ARCH-COMP)](...):** **Identify & Describe Core Components:** Based on the pattern(s) and functional domains, identify primary logical components. Define each component's single responsibility and boundaries concisely.
        -   [ ] * **Step 1.3.4 [(Rule #? : ARCH-INT)](...):** **Map Component Interactions & Protocols:** Detail primary communication pathways, interaction styles (e.g., Sync REST, Async Event), and data formats between components. Consider generating a textual interaction diagram (e.g., PlantUML/Mermaid).
        -   [ ] * **Step 1.3.5 [(Rule #? : ARCH-DEP)](...):** **Analyze & Document Dependencies:** Create an explicit dependency matrix or list showing build-time and run-time dependencies between components.

    -   [ ] **Task 1.4: Foundational Technical Strategy Definition** *(Function: Addressing Foundational Technical Aspects)*
        -   [ ] * **Step 1.4.1 [(Rule #? : DATA-MOD)](...):** **Conceptual Data Model:** Define core data entities, essential attributes, and key relationships (e.g., using Mermaid E-R syntax or structured list). Identify potential partitioning needs based on NFRs.
        -   [ ] * **Step 1.4.2 [(Rule #? : API-DES)](...):** **API Design Philosophy:** If APIs are core, define primary style (REST, GraphQL, gRPC) and foundational principles (versioning, standard formats, auth integration, common parameters).
        -   [ ] * **Step 1.4.3 [(Rule #? : DEPL-STRAT)](...):** **Deployment Strategy Outline:** Describe target deployment units (e.g., Containers, Functions), target platform services (e.g., AKS, ECS, Azure Functions), and key infrastructure components (e.g., Load Balancer, API Gateway, DB).
        -   [ ] * **Step 1.4.4 [(Rule #? : CICD-PIPE)](...):** **CI/CD Pipeline Vision:** Outline conceptual CI/CD stages (e.g., Commit -> SAST -> Build -> Unit Test -> Package -> Deploy Dev -> ...) and key tools (e.g., Azure DevOps, GitHub Actions).

    -   [ ] **Task 1.5: Operability & Quality Strategy Definition** *(Function: Ensuring Quality & Operability)*
        -   [ ] * **Step 1.5.1 [(Rule #? : SEC-AUTH)](...):** **Authentication & Authorization Strategy:** Detail the proposed mechanism (e.g., Dedicated IdP, Azure AD B2C), token types, and role/permission enforcement approach.
        -   [ ] * **Step 1.5.2 [(Rule #? : QUAL-LOG)](...):** **Logging Strategy:** Specify library/framework, aggregation approach, key contextual info (e.g., correlation IDs), and levels.
        -   [ ] * **Step 1.5.3 [(Rule #? : QUAL-MON)](...):** **Monitoring & Alerting Strategy:** Define key technical/business metrics per component, monitoring tools, and high-level alerting approach.
        -   [ ] * **Step 1.5.4 [(Rule #? : CONF-MAN)](...):** **Configuration Management Strategy:** Detail how configuration will be managed across environments (e.g., Azure App Config, Vault, Env Vars via K8s).
        -   [ ] * **Step 1.5.5 [(Rule #? : QUAL-ERR)](...):** **Centralized Error Handling & Reporting:** Outline strategy for consistent error handling and reporting/surfacing (e.g., Middleware, Error Tracking Service).

    -   [ ] **Task 1.6: Strategic Build Sequence Formulation** *(Function: Planning the Build)*
        -   [ ] * **Step 1.6.1 [(Rule #? : PLAN-SEQ)](...):** **Develop Optimized Build Sequence:** Based *explicitly* on documented dependencies (1.3.5) and potential parallelism, formulate the build sequence for core components (from 1.3.3). Prioritize foundational elements.
        -   [ ] * **Step 1.6.2 [(Rule #? : PLAN-JUST)](...):** **Justify Sequence:** Provide detailed justification for each position in the sequence, referencing specific dependencies, NFR drivers, or enabling parallel paths.

    -   [ ] **Task 1.7: Phase 1 Consolidation & Verification** *(Function: Setup/Meta)*
        -   [ ] * **Step 1.7.1:** **Consolidate Architectural Blueprint:** Assemble outputs from Tasks 1.2-1.6 into a single, coherent document/section. Ensure clear formatting (Markdown lists, tables, code blocks for diagrams/models).
        -   [ ] * **Step 1.7.2 [(Rule #? : PLAN-VER)](...):** **Perform Self-Verification:** Review the consolidated output against objectives (Sec 1), directives (Sec 4 Tasks), and standards (Sec 2, 3). Verify consistency, completeness, traceability, and confirm all Phase 1 steps are complete.

* **Internal Success Criteria for Phase 1:**
    * Completion and verification of all steps within Tasks 1.1 through 1.7.
    * Comprehensive analysis (Task 1.2) documented.
    * Core architecture (Task 1.3) robustly defined and justified.
    * Foundational technical strategies (Task 1.4) established.
    * Operability and quality strategies (Task 1.5) defined.
    * Optimized build sequence (Task 1.6) formulated and justified.
    * All outputs consolidated and verified (Task 1.7), aligning with Apex Standards.
* **Internal Verification Method for Phase 1:**
    * Execute Step 1.7.2 rigorously.
    * Cross-reference NFR analysis (Task 1.2) with architectural choices (Task 1.3) and operability strategies (Task 1.5).
    * Trace dependencies (1.3.5) directly to the build sequence justification (1.6.2).
    * Validate technical strategies (Task 1.4) against requirements (Task 1.2) and tech stack.
    * Check for explicit standards references and use of requested output formats.

**5. Test Reporting Protocol (Internal - For Subsequent Phases)**
* **Log File Location:** `docs/Test_Result_Analysis.md` (relative to project root)
* **Data Points per Entry:** Date/Time, Scope (Component, Task, Test Suite), Pass/Fail Status, Key Metrics (e.g., Coverage %, Latency), Summary Findings/Errors.
* **Update Frequency:** After relevant Task/Phase/Component testing activities during execution phases.

**6. Final Instruction for this Phase**
Execute the sequential Tasks and Steps (1.1 through 1.7) defined exhaustively in Section 4. Produce the consolidated architectural blueprint and strategic build plan as per Task 1.7. Your output must demonstrate thorough analysis and adherence to all instructions and standards. Await user review and explicit confirmation of this Phase 1 output before proceeding to Phase 2 (building the first component in the sequence).

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: 2025-04-10 HH:MM UTC+/-Offset]. Location context: Menasha, Wisconsin, United States)*