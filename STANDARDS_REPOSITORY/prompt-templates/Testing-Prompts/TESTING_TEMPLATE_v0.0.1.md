# Meta-Structure Definition for Autonomous LLM Execution Prompts v0.0.1 (Testing & Finalization Focus)

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM UTC+/-Offset]

## 1. Overall Purpose
This document defines a standardized template structure for prompts intended to guide a Large Language Model (LLM) agent (e.g., SE-Apex) in executing the final stages of a project lifecycle autonomously. The structure emphasizes comprehensive **testing**, systematic **bug identification and resolution**, final code/documentation **cleanup**, and strict adherence to **compliance standards** to ensure the project is stable, correct, and ready for deployment or handoff.

## 2. Core Execution Principles & Global Rules
The agent executing a prompt based on this template MUST adhere to the following core principles:

* **Mandatory Initial Sweep:** The **VERY FIRST ACTION** before any testing or modification MUST be the `Phase 0: Initial Codebase Exploration` defined below. This involves a deep, meticulous sweep executing `ls` (or equivalent recursive directory listing) in every directory of the project root to understand the existing state before final validation begins.
* **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the project root where the plan file resides) is **MANDATORY** for all steps and deliverables, particularly rules related to Testing (`TEST-*`), Documentation (`DOC-*`), Implementation Correctness (`IMPL-*`), and Final Validation (`FINAL-*`). Specific rules referenced as `[(Rule #X: CODE)](<relative_path_to_standards>#rule-X)` MUST link to the corresponding rule anchor in the standards document using the correct relative path. The Standards Guide takes precedence over potentially conflicting prompt details unless a deviation is explicitly stated and justified within the prompt itself.
* **Strict Sequential Execution:**
    * The prompt defines work hierarchically: **Phase -> Task -> Step**. Each item MUST begin with an unchecked Markdown checkbox (`- [ ]`).
    * Execution MUST proceed sequentially: start with `Phase 0`, then complete all Steps within a Task before the next Task; complete all Tasks within a Phase before the next Phase.
    * Do NOT proceed to the next item until the current item is fully completed, its `Internal Success Criteria` are met (verified via `Internal Verification Method`), and its checkbox is marked complete (`- [x]`).
* **Internal Success Criteria & Verification:**
    * Each Task defines `Internal Success Criteria` and `Internal Verification Method`.
    * The agent MUST perform the internal verification upon completing the steps for a Task/Phase. Verification MUST include confirming compliance with all `(Rule #X: CODE)` references within the completed Task/Steps.
* **Recursive Error Handling / Retry Logic (Bug Fixing Loop):**
    * If `Internal Verification` fails (criteria unmet, tests fail, rule violations detected, bugs identified), the agent MUST NOT proceed to the *next* Phase/Task outside the bug-fixing loop.
    * It MUST cycle through bug identification, implementation of corrections, re-testing/re-verification (`Internal Verification Method`), and re-checking rule compliance.
    * This cycle repeats within the defined bug-fixing phases until verification succeeds and tests pass.
* **Autonomous Operation & Reporting:**
    * Execution is fully autonomous unless specified otherwise.
    * Intermediate reporting is DISABLED unless explicitly required (e.g., detailed bug reports).
    * Progress/test results are logged internally per `Test Reporting Protocol`. Checkbox state visually tracks progress.
    * External reporting occurs ONLY upon completion of the entire sequence.

## 3. Mandatory Quality & Finalization Rules (Reference `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`)
Regardless of specific Step instructions, the agent MUST continuously enforce and finally verify adherence to **all** applicable rules within the **Apex Software Compliance Standards Guide** (`./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`), placing particular emphasis on:
* **Testing & Verification:** Thorough execution and analysis (See Section 14: `TEST-*` rules).
* **Implementation Correctness:** Ensuring code behaves as intended (See Section 19: `IMPL-*` rules).
* **Code Quality & Structure:** Readability, maintainability, linting/formatting (See Section 8: `QUAL-*` rules).
* **Documentation:** Completeness and accuracy of comments and external docs (See Section 18: `DOC-*` rules).
* **Security:** Verification of security best practices (See Section 13: `SEC-*` rules).
* **Final Validation:** Comprehensive final checks (See Section 21: `FINAL-*` rules, especially `FINAL-SWEEP`).

## 4. Prompt Template Structure (Section by Section)

* **A. Overall Formatting:**
    * Enclose entire prompt in ```markdown ... ```.
    * All Phase, Task, Step items MUST begin with `- [ ]`.

* **B. Subject Line:**
    * Format: `Subject: [CONCISE, ACTION-ORIENTED TITLE reflecting Testing/Fixing Goal]`

* **C. Directive Section:**
    * Establishes context (testing/finalization phase), execution mode, **explicit instruction for the mandatory `Phase 0` initial sweep**, sequential rule, **explicit reference to mandatory adherence to `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` (emphasizing TEST, IMPL, DOC, FINAL rules)**, reporting constraints, internal logging instructions.

* **D. Test Reporting Protocol (Internal):**
    * Defines standard for internal test log (e.g., `docs/Test_Result_Analysis.md`).
    * Specifies location, data points (Date, Scope, Test Suite, Pass %, Coverage %, Failures List, Bug IDs), update frequency (e.g., after each test run).

* **E. Hierarchical Execution Blocks:**
    * Core of the prompt, sequential. Uses Markdown headings/lists. Separated by `---`.
    * **Every Phase, Task, Step MUST start with `- [ ]`.**

    * **E.0. MANDATORY FIRST PHASE: Initial Exploration**
        -   [ ] **Phase 0: Initial Codebase Exploration**
            * **Objective:** To perform a comprehensive, deep, and meticulous sweep of the *entire existing project directory structure* before any testing or modifications are initiated. This establishes a baseline understanding of the current state.
            -   [ ] **Task 0.1: Full Directory Listing Sweep**
                * **Task Objective:** Execute a recursive directory listing (`ls -R` or equivalent) starting from the project root to capture the structure and contents of *every* subdirectory.
                -   [ ] * **Step 0.1.1 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63):** **Execute Recursive Listing:** Run the command.
                -   [ ] * **Step 0.1.2 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63):** **Log Output:** Save complete output to `logs/final_sweep_baseline.log`.
                * **Internal Success Criteria:** Command executed; complete output saved to `logs/final_sweep_baseline.log`; Compliance with referenced Rules.
                * **Internal Verification Method:** Confirm command success; verify log file existence and content; Verify Rule compliance.
                * **Task Completion Testing (Internal):** N/A. Update internal dev log.

    ---
    * **E.1. Phase Block (`- [ ] **Phase 1: Comprehensive Testing Execution**`)** *(Example Phases/Tasks follow)*
        * **Objective:** Execute all available test suites to identify failures and regressions.
        -   [ ] **Task 1.1: Execute Unit Tests**
            * **Task Objective:** Run the complete unit test suite and record results.
            -   [ ] * **Step 1.1.1 [(Rule #35: TEST-UNIT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-35):** **Run Unit Test Command:** Execute the configured command (e.g., `npm run test:unit`, `pytest tests/unit`). Capture stdout/stderr.
            -   [ ] * **Step 1.1.2 [(Rule #41: TEST-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-41):** **Log Results:** Parse test output. Update `docs/Test_Result_Analysis.md` with Date, Scope="Unit", Pass %, Coverage %, and a detailed list of specific test failures/errors encountered.
            * **Internal Success Criteria:** Unit test command executed; `Test_Result_Analysis.md` updated accurately with unit test results (including pass/fail status and specific failures). Compliance with referenced Rules.
            * **Internal Verification Method:** Check command exit code; Review `Test_Result_Analysis.md` for new entry and accuracy of reported failures. Verify Rule compliance.
        -   [ ] **Task 1.2: Execute Integration Tests**
            * **Task Objective:** Run the integration test suite and record results.
            -   [ ] * **Step 1.2.1 [(Rule #36: TEST-INT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-36):** **Run Integration Test Command:** Execute (e.g., `npm run test:integration`, `pytest tests/integration`). Capture output.
            -   [ ] * **Step 1.2.2 [(Rule #41: TEST-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-41):** **Log Results:** Parse output. Update `docs/Test_Result_Analysis.md` with Integration test results (Pass %, Failures List).
            * **Internal Success Criteria:** Integration tests executed; `Test_Result_Analysis.md` updated accurately. Compliance with referenced Rules.
            * **Internal Verification Method:** Check exit code; Review log update. Verify Rule compliance.
        * **Phase Completion Testing (Internal):** N/A (Testing phase itself). Ensure test log is fully updated for the Phase.

    ---
    * **E.2. Phase Block (`- [ ] **Phase 2: Bug Analysis and Prioritization**`)**
        * **Objective:** Analyze test failures and system logs to identify, document, and prioritize specific bugs for fixing.
        -   [ ] **Task 2.1: Correlate Failures and Logs**
            * **Task Objective:** Analyze failures listed in `docs/Test_Result_Analysis.md` and relevant system/application logs (`logs/`) from the test runs to pinpoint root causes.
            -   [ ] * **Step 2.1.1 [(Rule #64: DIAG-CAUSE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-64):** **Analyze Test Failures:** For each failed test recorded in the log, examine the failure message and associated stack trace/output.
            -   [ ] * **Step 2.1.2 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63), [(Rule #64: DIAG-CAUSE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-64):** **Analyze System Logs:** Review application logs generated during test execution for errors, warnings, or relevant messages corresponding to the timeframe of test failures.
            -   [ ] * **Step 2.1.3 [(Rule #42: TEST-BUG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-42):** **Document Bugs:** For each distinct issue identified, create a preliminary bug report entry (e.g., in `docs/Bug_Tracker.md` or internal structure) detailing: Failed Test(s), Log Evidence, Suspected Location/Cause, Severity (Estimate: High/Medium/Low). Assign a unique Bug ID (e.g., BUG-001).
            * **Internal Success Criteria:** All test failures from Phase 1 analyzed against logs; Potential bugs documented with necessary details and unique IDs. Compliance with referenced Rules.
            * **Internal Verification Method:** Review the created bug entries; ensure they correlate to test failures and log evidence; check for completeness of required details. Verify Rule compliance.

    ---
    * **E.3. Phase Block (`- [ ] **Phase 3: Targeted Bug Resolution**`)**
        * **Objective:** Implement code corrections for identified bugs and verify fixes. (This Phase might loop or contain multiple Tasks per bug).
        -   [ ] **Task 3.1: Fix Bug [BUG-ID] - [Brief Description]** *(Repeat Task structure for each high/medium priority bug)*
            * **Task Objective:** Address the specific issue documented in BUG-ID.
            -   [ ] * **Step 3.1.1 [(Rule #60: IMPL-MOD)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-60), [(Rule #64: DIAG-CAUSE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-64):** **Locate & Analyze Code:** Identify the specific code module(s)/function(s) responsible for BUG-ID based on analysis in Phase 2.
            -   [ ] * **Step 3.1.2 [(Rule #61: IMPL-FIX)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-61), [(Rule #16: QUAL-SIZE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-16):** **Implement Correction:** Modify the code to fix the bug. Ensure the fix adheres to all code quality, style, and structure rules (e.g., line limits, modularity).
            -   [ ] * **Step 3.1.3 [(Rule #56: DOC-INT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-56):** **Update Code Comments:** Add/update comments explaining the fix if necessary.
            -   [ ] * **Step 3.1.4 [(Rule #39: TEST-REG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-39), [(Rule #35: TEST-UNIT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-35):** **Verify Fix & Run Related Tests:** Execute the specific test(s) that previously failed due to BUG-ID. Also run any closely related unit tests to check for regressions.
            -   [ ] * **Step 3.1.5 [(Rule #42: TEST-BUG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-42):** **Update Bug Tracker:** Mark BUG-ID as 'Resolved' or 'Pending Verification' in `docs/Bug_Tracker.md`.
            * **Internal Success Criteria:** Code correction for BUG-ID implemented; Related tests now pass; Bug tracker updated; Fix adheres to all referenced Standards Rules.
            * **Internal Verification Method:** Review code changes; Confirm previously failing tests now pass; Check bug tracker status; Perform static analysis/linting on changed files; Verify compliance with all referenced Rules.
        * **Phase Completion Testing (Internal):** After attempting fixes for all targeted bugs, **re-run the full test suites** (Unit, Integration - similar to Phase 1 Tasks) to ensure no regressions were introduced. Update `docs/Test_Result_Analysis.md`. If new failures occur, potentially loop back to Phase 2/3.

    ---
    * **E.4. Phase Block (`- [ ] **Phase 4: Final Cleanup and Validation**`)**
        * **Objective:** Perform final code cleanup, documentation checks, and standards validation sweep.
        -   [ ] **Task 4.1: Code Formatting and Linting**
            * **Task Objective:** Ensure all code adheres to project formatting and linting standards.
            -   [ ] * **Step 4.1.1 [(Rule #13: QUAL-LINT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-13):** **Run Linter/Formatter:** Execute tools (e.g., Prettier, ESLint, Black) across the codebase to identify/fix issues.
            * **Internal Success Criteria:** Linter/formatter ran successfully; No outstanding critical linting/formatting errors remain. Compliance with Rule #13.
            * **Internal Verification Method:** Check tool exit codes; Manually review tool output for unaddressed issues. Verify Rule compliance.
        -   [ ] **Task 4.2: Documentation Review**
            * **Task Objective:** Verify code comments and external documentation are complete and accurate.
            -   [ ] * **Step 4.2.1 [(Rule #56: DOC-INT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-56), [(Rule #57: DOC-EXT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-57):** **Review Comments & Docs:** Check key modules for sufficient comments; Review `README.md`, `docs/` for accuracy and completeness against the final code state.
            * **Internal Success Criteria:** Documentation review completed; Major gaps or inaccuracies noted/addressed. Compliance with referenced Rules.
            * **Internal Verification Method:** Sample code files and main documentation files to verify quality. Verify Rule compliance.
        -   [ ] **Task 4.3: Final Standards Compliance Sweep**
            * **Task Objective:** Perform a final verification against all relevant Apex Standards.
            -   [ ] * **Step 4.3.1 [(Rule #71: FINAL-SWEEP)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-71):** **Execute Final Check:** Systematically review the codebase and project state against key requirements in `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`, particularly Sections 8, 13, 14, 18, 19, 21. Document any deviations.
            * **Internal Success Criteria:** Final standards sweep performed; Compliance confirmed or deviations documented. Compliance with Rule #71.
            * **Internal Verification Method:** Review the output/report of the compliance check. Verify Rule compliance.

* **F. Final Instruction:**
    * Explicitly commands start of execution, beginning with the **mandatory `Phase 0` sweep**, then proceeding sequentially through the testing, bug fixing, and cleanup phases/tasks. Emphasize marking checkboxes upon verified completion, **adhering strictly to the linked `APEX_STANDARDS.md` (especially TEST, IMPL, DOC, FINAL rules)**, executing bug-fix loops as needed, and following the final reporting constraint. The ultimate goal is a stable, tested, compliant, and correctly functioning project state. Perform a final review of test results and bug tracker status before concluding.

* **G. Contextual Footer:**
    * Metadata: Timestamp, location. `*(Instructions generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Location])*`

## 5. Summary
This specialized template guides an LLM agent through the critical final stages of project completion, focusing on **stabilization and quality assurance**. It mandates an **initial codebase sweep (Phase 0)**, followed by structured phases for **comprehensive testing, bug analysis, targeted fixing, and final cleanup/validation**. Strict adherence to the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`), particularly testing, implementation, documentation, and final validation rules, is enforced through linked references and verification steps. The process emphasizes sequential execution, meticulous internal logging, and iterative bug fixing until a high-quality, stable state is achieved.

*(Meta-structure v0.0.1 explanation updated [2025-04-19])*