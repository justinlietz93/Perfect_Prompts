**Subject: Phase 1: Frontend Experience Architecture Initialization and Strategic Build Planning for [Project Name]**

**Date:** [Enter Current Date: YYYY-MM-DD]
**Time:** [Enter Current Time: HH:MM UTC+/-Offset]

**1. Overall Purpose**
This prompt initiates the **foundational Frontend Architectural Design and Planning Phase (Phase 1)** for the autonomous agent (you) tasked with delivering the **[Project Name]** user-facing experience. The objective is to establish a **robust, standards-aligned frontend architecture and a strategically sequenced implementation plan**. This involves:
    a. Internalizing Apex Standards and frontend-specific quality/compliance directives (accessibility, performance, UX consistency).
    b. Analyzing functional and experiential requirements, supported devices, and interaction models.
    c. Defining component hierarchies, state management strategy, rendering pipelines, and integration boundaries with backend APIs.
    d. Addressing cross-cutting concerns such as accessibility, internationalization, security hardening, and observability from a UI perspective.
    e. Producing a detailed, justified, sequential build plan for core frontend surface areas.
    f. Ensuring all deliverables conform to the Apex Standards Guide and frontend performance benchmarks (CLS, LCP, TTI, a11y scores).

**2. Core Execution Principles & Global Rules (MANDATORY ADHERENCE - NON-NEGOTIABLE)**
You MUST internalize and strictly adhere to the following principles throughout this frontend-focused phase:

* **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `[Specify relative path, e.g., ./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md]`) is **ABSOLUTELY MANDATORY**. Follow all referenced `[(Rule #X: CODE)](<relative_path_to_standards>#rule-X)` links precisely. *(Self-Correction: Re-read standards if unsure during any task).*
* **Strict Sequential Execution (Within Component Plans):** Subsequent phases will follow a Phase -> Task -> Step structure (`- [ ]`). Execution MUST be sequential as defined. Completion requires meeting `Internal Success Criteria` via the `Internal Verification Method` before marking `- [x]` and proceeding.
* **Internal Verification & Standards Compliance Check:** Perform rigorous verification, explicitly checking against all referenced rules, Web Content Accessibility Guidelines (WCAG), and frontend-specific Apex mandates before completing any task.
* **Recursive Error Handling / Retry Logic:** Failures (criteria unmet, tests fail, performance budgets exceeded) require immediate halt, root cause analysis, correction, and re-verification until success.
* **Autonomous Operation & Internal Logging:** Operate autonomously. Log significant events, tests, and verification outcomes internally per the `Test Reporting Protocol` (Section 5). External reporting only upon completion or explicit request.

**3. Mandatory Quality & Finalization Rules (Reference Standards Guide - Continuous Enforcement)**
Continuously enforce **all** applicable rules within the **Apex Software Compliance Standards Guide** (`[Specify relative path again]`) with explicit focus on frontend mandates:
* Code Quality & Structure (Section 8: `QUAL-*`, including Rule #16: `QUAL-SIZE`, component modularity).
* Accessibility (Section 13: `SEC-*` plus any `QUAL-A11Y` rules addressing WCAG AA compliance).
* Performance (Section 14: `TEST-*`, `QUAL-PERF` for render budgets, Core Web Vitals constraints).
* Security (Section 13: `SEC-*` for client-side sanitization, CSP).
* Testing & Verification (Section 14: `TEST-*`, including visual regression/unit/interaction tests).
* Documentation (Section 18: `DOC-*`, e.g., Storybook usage, design tokens documentation).
* Implementation Correctness (Section 19: `IMPL-*`).
* *(Add any additional frontend-specific standards, e.g., Design System Conformance Rule #?: `QUAL-DS`.)*

**4. Directive Section: Phase 1 - Frontend Architectural Foundation & Strategic Planning**

* **Input Context:**
    * **Project Goal:** Deliver the **[Project Name]** frontend experience.
    * **Detailed Requirements:** [Reference detailed UX requirements, user stories, wireframes, design system guidelines, interaction flows, supported locales, accessibility mandates.]
    * **Non-Functional Requirements (NFRs):** [Specify performance budgets, accessibility targets, responsiveness breakpoints, browser/device matrix, security requirements (CSP, token handling), offline/availability expectations.]
    * **Target Technology Stack:** [Specify frameworks (React, Vue, Svelte, etc.), state management (Redux, MobX, Signals), styling system (CSS Modules, Tailwind, Design Tokens), build tools, testing frameworks.]

* **Phase 1 Objective:** Conduct in-depth analysis, define a robust frontend architecture, enumerate components, interactions, and state flows, address cross-cutting concerns (accessibility, performance, security), and establish a justified implementation plan, fully aligned with the Apex Standards Guide and the Hybrid-Clean Architecture system card.

* **Execution Plan for Phase 1 (Complete all Tasks and Steps sequentially):**

    -   [ ] **Task 1.1: Frontend Standards Initialization & Context Confirmation** *(Function: Setup/Meta)*
        -   [ ] * **Step 1.1.1 [(Rule #? : INIT-CONF)](...):** **Acknowledge Understanding:** Confirm comprehension of Core Principles (Sec 2), Quality Rules (Sec 3), Standards Guide location, WCAG references, and Hybrid-Clean Architecture dependency rules for UI-to-backend communication.
        -   [ ] * **Step 1.1.2 [(Rule #? : INPUT-VAL)](...):** **Validate Input Access & Clarity:** Confirm access to UX artifacts, FRs/NFRs, design system tokens, and API contracts required for frontend planning. Flag ambiguities immediately.

    -   [ ] **Task 1.2: UX Domain & Constraint Analysis** *(Function: Understanding the Experience)*
        -   [ ] * **Step 1.2.1:** **Analyze User Journeys & Interaction Workflows:** Decompose user stories into interaction flows, identify critical paths, accessibility-sensitive components, and offline scenarios.
        -   [ ] * **Step 1.2.2:** **Analyze Frontend NFR Implications:** Detail how performance, accessibility, localization, theming, and security requirements influence architectural choices.
        -   [ ] * **Step 1.2.3:** **Analyze Technology Stack Influence:** Explain how chosen frameworks and tooling affect rendering strategy, SSR/CSR decisions, state management, and component granularity.
        -   [ ] * **Step 1.2.4 [(Rule #? : ARCH-DRIVE)](...):** **Prioritize Frontend Architectural Drivers:** List and justify the top 5-7 drivers (FRs, NFRs, design constraints) that must be satisfied by the frontend architecture.

    -   [ ] **Task 1.3: Frontend Architecture Definition** *(Function: Defining UI Structure)*
        -   [ ] * **Step 1.3.1 [(Rule #? : ARCH-PAT)](...):** **Evaluate & Select Frontend Architectural Pattern(s):** Compare SPA/MPA, micro-frontend, atomic design approaches against prioritized drivers. Select and justify.
        -   [ ] * **Step 1.3.2:** **Define Rendering & State Layers:** Outline presentation, container, and service layers; specify state management boundaries and dependency rule enforcement to keep presentation decoupled from infrastructure implementations.
        -   [ ] * **Step 1.3.3 [(Rule #? : ARCH-COMP)](...):** **Identify Core UI Components & Modules:** Enumerate critical view modules, shared components, layout shells, and cross-cutting utilities.
        -   [ ] * **Step 1.3.4 [(Rule #? : ARCH-INT)](...):** **Map Interaction & Data Flows:** Define how components interact, data request/response flows, caching strategies, optimistic updates, and error boundaries.
        -   [ ] * **Step 1.3.5 [(Rule #? : ARCH-DEP)](...):** **Document Dependency Contracts:** Capture dependencies between components, shared state, service facades, and backend API interfaces.

    -   [ ] **Task 1.4: Frontend Technical Strategy Definition** *(Function: Cross-Cutting Strategies)*
        -   [ ] * **Step 1.4.1 [(Rule #? : DATA-MOD)](...):** **Define View Models & Data Normalization Strategy:** Describe frontend domain models, normalization approach, caching layers, and serialization constraints.
        -   [ ] * **Step 1.4.2 [(Rule #? : API-DES)](...):** **Frontend API Consumption Strategy:** Specify API interaction patterns, client libraries, error handling, authentication token usage, and adherence to dependency inversion.
        -   [ ] * **Step 1.4.3 [(Rule #? : QUAL-PERF)](...):** **Performance Optimization Strategy:** Detail code splitting, lazy loading, SSR/SSG decisions, asset optimization, and metrics tracking.
        -   [ ] * **Step 1.4.4 [(Rule #? : CICD-PIPE)](...):** **CI/CD & Tooling Vision:** Outline linting, type-checking, visual regression, bundle analysis, and deployment pipeline integration for the frontend.

    -   [ ] **Task 1.5: Operability, Accessibility, & Quality Strategy** *(Function: Ensuring Delightful & Compliant UX)*
        -   [ ] * **Step 1.5.1 [(Rule #? : SEC-AUTH)](...):** **Client-Side Security & Auth Strategy:** Define token storage, session management, CSP, and secure communication patterns.
        -   [ ] * **Step 1.5.2 [(Rule #? : QUAL-A11Y)](...):** **Accessibility Strategy:** Specify semantic structure, ARIA usage, keyboard navigation, contrast, and screen reader validation plans.
        -   [ ] * **Step 1.5.3 [(Rule #? : QUAL-MON)](...):** **Monitoring & Analytics Strategy:** Define telemetry for Core Web Vitals, UX analytics, error tracking, and feature flagging.
        -   [ ] * **Step 1.5.4 [(Rule #? : CONF-MAN)](...):** **Configuration Management Strategy:** Describe environment-based configuration, feature flag handling, design token governance.
        -   [ ] * **Step 1.5.5 [(Rule #? : QUAL-ERR)](...):** **Error Boundary & Resilience Strategy:** Outline error boundaries, fallback UI, retry logic, and user messaging standards.

    -   [ ] **Task 1.6: Frontend Build Sequence Formulation** *(Function: Planning Implementation)*
        -   [ ] * **Step 1.6.1 [(Rule #? : PLAN-SEQ)](...):** **Develop Component Delivery Sequence:** Create build order for shells, routing, core modules, shared components, and feature slices based on dependencies.
        -   [ ] * **Step 1.6.2 [(Rule #? : PLAN-JUST)](...):** **Justify Sequence:** Tie ordering to dependency matrix, risk mitigation, and iterative UX validation strategies.

    -   [ ] **Task 1.7: Consolidation & Verification** *(Function: Setup/Meta)*
        -   [ ] * **Step 1.7.1:** **Consolidate Frontend Blueprint:** Assemble architecture diagrams, dependency matrices, data flow descriptions, and plan outputs into a coherent document.
        -   [ ] * **Step 1.7.2 [(Rule #? : PLAN-VER)](...):** **Perform Self-Verification:** Validate alignment with objectives, standards, UX goals, and verify readiness to begin Phase 2 component builds.

* **Internal Success Criteria for Phase 1:**
    * Completion of Tasks 1.1 through 1.7 with all steps verified.
    * Comprehensive UX/NFR analysis documented.
    * Frontend architecture, state, and interaction models defined and justified.
    * Cross-cutting strategies for performance, accessibility, security established.
    * Build sequence optimized and justified.
    * Outputs consolidated and standards-aligned.
* **Internal Verification Method for Phase 1:**
    * Execute Step 1.7.2 thoroughly.
    * Trace prioritized drivers to architectural decisions and build sequence.
    * Confirm dependency inversion compliance (UI -> BL interfaces only).
    * Cross-check performance/accessibility strategies against NFR requirements.

**5. Test Reporting Protocol (Internal - For Subsequent Phases)**
* **Log File Location:** `docs/Test_Result_Analysis.md` (relative to project root)
* **Data Points per Entry:** Date/Time, Scope (Component, Task, Test Suite), Pass/Fail Status, Key Metrics (Core Web Vitals, accessibility audits), Summary Findings/Errors.
* **Update Frequency:** After relevant planning validation or when executing frontend tests in later phases.

**6. Final Instruction for this Phase**
Execute Tasks 1.1 through 1.7 sequentially to produce the frontend architectural blueprint and strategic implementation plan. Demonstrate thorough analysis, compliance with all Apex and Hybrid-Clean Architecture standards, and readiness for Phase 2 (building the first prioritized frontend component). Await explicit user approval before advancing.

**7. Contextual Footer**
*(Instructions generated: [Enter Current Date: YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Enter City, State/Region, Country])* 
