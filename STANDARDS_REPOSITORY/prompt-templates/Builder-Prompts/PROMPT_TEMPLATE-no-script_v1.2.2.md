# Meta-Structure Definition for Autonomous LLM Execution Prompts v1.2.2 (Unified - Initial Sweep)

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM UTC+/-Offset]

## 1. Overall Purpose

This document defines a standardized template structure for prompts intended to guide a Large Language Model (LLM) agent (e.g., SE-Apex) in executing complex, multi-step projects autonomously. The structure emphasizes absolute explicitness, sequential task execution including a **mandatory initial codebase exploration**, integrated quality checks referencing the **Apex Software Compliance Standards Guide**, ensuring initial project setup, and minimizes ambiguity to ensure reliable completion according to predefined rules and requirements.

## 2. Core Execution Principles & Global Rules

The agent executing a prompt based on this template MUST adhere to the following core principles:

- **Mandatory Initial Sweep:** The **VERY FIRST ACTION** before any other task execution MUST be the `Phase 0: Initial Codebase Exploration` defined below. This involves a deep, meticulous sweep executing `ls` (or equivalent recursive directory listing) in every directory of the project root to understand the existing state.
- **Apex Standards Adherence:** Compliance with the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the project root where the plan file resides) is **MANDATORY** for all steps and deliverables. Specific rules referenced as `[(Rule #X: CODE)](<relative_path_to_standards>#rule-X)` MUST link to the corresponding rule anchor in the standards document using the correct relative path. The Standards Guide takes precedence over potentially conflicting prompt details unless a deviation is explicitly stated and justified within the prompt itself.
- **Strict Sequential Execution:**
  - The prompt defines work hierarchically: **Phase -> Task -> Step**. Each item MUST begin with an unchecked Markdown checkbox (`- [ ]`).
  - Execution MUST proceed sequentially: start with `Phase 0`, then complete all Steps within a Task before the next Task; complete all Tasks within a Phase before the next Phase.
  - Do NOT proceed to the next item until the current item is fully completed, its `Internal Success Criteria` are met (verified via `Internal Verification Method`), and its checkbox is marked complete (`- [x]`).
- **Internal Success Criteria & Verification:**
  - Each Task defines `Internal Success Criteria` and `Internal Verification Method`.
  - The agent MUST perform the internal verification upon completing the steps for a Task/Phase. Verification MUST include confirming compliance with all `(Rule #X: CODE)` references within the completed Task/Steps.
- **Recursive Error Handling / Retry Logic:**
  - If `Internal Verification` fails (criteria unmet, tests fail, rule violations detected), the agent MUST NOT proceed.
  - It MUST re-execute the failed Step(s)/Task(s), identify and implement corrections, and re-run the `Internal Verification Method` (including rule compliance checks).
  - This cycle repeats until verification succeeds.
- **Autonomous Operation & Reporting:**
  - Execution is fully autonomous unless specified otherwise.
  - Intermediate reporting is DISABLED unless explicitly required.
  - Progress/test results are logged internally per `Test Reporting Protocol`. Checkbox state visually tracks progress.
  - External reporting occurs ONLY upon completion of the entire sequence.

## 3. Mandatory Quality & Finalization Rules (Reference `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`)

Regardless of specific Step instructions, the agent MUST continuously enforce and finally verify adherence to **all** applicable rules within the **Apex Software Compliance Standards Guide** (`./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`), particularly including but not limited to:

- **Code Quality & Structure:** See Section 8 (`QUAL-*` rules).
- **Line Limit & Modularization:** Adhere to the 500-line limit per file, refactoring as needed (See Section 8, specifically Rule #16: `QUAL-SIZE`).
- **Configuration Management:** See Section 12 (`CONF-*` rules).
- **Security:** See Section 13 (`SEC-*` rules).
- **Testing & Verification:** See Section 14 (`TEST-*` rules).
- **Documentation:** See Section 18 (`DOC-*` rules).
- **Implementation Correctness:** See Section 19 (`IMPL-*` rules).
- **Final Validation:** See Section 21 (`FINAL-*` rules), especially `FINAL-SWEEP`.

## 4. Prompt Template Structure (Section by Section)

- **A. Overall Formatting:**

  - Enclose entire prompt in `markdown ... `.
  - All Phase, Task, Step items MUST begin with `- [ ]`.

- **B. Subject Line:**

  - Format: `Subject: [CONCISE, ACTION-ORIENTED TITLE]`

- **C. Directive Section:**

  - Establishes context, execution mode, **explicit instruction for the mandatory `Phase 0` initial sweep**, sequential rule, **explicit reference to mandatory adherence to `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md`**, reporting constraints, internal logging instructions.

- **D. Test Reporting Protocol (Internal):**

  - Defines standard for internal test log (e.g., `docs/Test_Result_Analysis.md`).
  - Specifies location, data points (Date, Scope, Pass %, Coverage %, Findings), update frequency.

- **E. Hierarchical Execution Blocks:**

  - Core of the prompt, sequential. Uses Markdown headings/lists. Separated by `---`.
  - **Every Phase, Task, Step MUST start with `- [ ]`.**

  - **E.0. MANDATORY FIRST PHASE: Initial Exploration**
    - [ ] **Phase 0: Initial Codebase Exploration**
      - **Objective:** To perform a comprehensive, deep, and meticulous sweep of the _entire existing project directory structure_ before any other tasks are initiated. This establishes a baseline understanding of the current state.
      * [ ] **Task 0.1: Full Directory Listing Sweep**
        - **Task Objective:** Execute a recursive directory listing (`ls -R` or equivalent command appropriate for the environment) starting from the project root directory to capture the structure and contents of _every_ subdirectory.
        * [ ] - **Step 0.1.1 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63):** **Execute Recursive Listing:** Run the command to list all files and directories recursively within the project root. Ensure the output captures the full path for each item.
        * [ ] - **Step 0.1.2 [(Rule #63: DIAG-LOG)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-63):** **Log Output:** Save the complete, raw output of the recursive listing command to a dedicated log file (e.g., `logs/initial_codebase_sweep.log`). This log serves as the baseline reference.
        - **Internal Success Criteria:**
          - A recursive directory listing command was executed successfully starting from the project root.
          - The complete output, showing all files and directories, is saved to `logs/initial_codebase_sweep.log`.
          - Compliance with all referenced Apex Standards Rules.
        - **Internal Verification Method:**
          - Confirm the successful execution of the listing command (e.g., exit code 0).
          - Verify the existence and non-emptiness of the `logs/initial_codebase_sweep.log` file.
          - Briefly review the log file content to ensure it appears to be a comprehensive directory listing.
          - Verify compliance with referenced Apex Standards Rules for this Task and its Steps.
        - **Task Completion Testing (Internal):** N/A (Exploration Task). Update internal development log.

  ***

  - **E.1. Phase Block (`- [ ] **Phase 1: Name**`)** _(Renumber subsequent Phases and Tasks accordingly, starting from 1)_

    - Content: High-level `* **Objective:**`. Contains Task Blocks.

  - **E.2. Task Block (`- [ ] **Task 1.1: Name**`)** _(Renumber subsequent Tasks accordingly, starting from 1.1)_

    - Content: `* **Task Objective:**`, Step list items, `Internal Success Criteria`, `Internal Verification Method`, `Task Completion Testing (Internal)`.
    - _(Example incorporating the **rephrased conditional** setup task, now renumbered):_

    * [ ] **Task 1.1: Ensure Project Structure Conforms to Plan**
      - **Task Objective:** Ensure the necessary project directory structure and essential blank files exist _based on the established plan AND informed by the initial sweep in Phase 0_. **If the project root already exists (confirmed during Phase 0), this task will only ensure the specific folders and files planned for the current execution phase exist, avoiding modification of pre-existing unrelated structures.** If the project root does not exist, it will ensure the initial full structure is created.
      * [ ] - **Step 1.1.0 [(Rule #1: PLAN-CHK)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-1):** **Analyze Initial Sweep Log:** Review `logs/initial_codebase_sweep.log` to confirm if the project root and key planned directories/files already exist.
      * [ ] - **Step 1.1.1 [(Rule #1: PLAN-CHK)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-1):** **Identify Required Structure:** Based on the overall project plan and the analysis in Step 1.1.0, determine the list of directories and files that are required for the current execution plan but do not yet exist.
      * [ ] - **Step 1.1.2 [(Rule #26: CONF-EXT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-26):** **Create Missing Directories:** Create all directories identified in Step 1.1.1 as missing. Ensure correct nesting (e.g., `src/`, `tests/`, `docs/`, `config/`, `scripts/`, `logs/`).
      * [ ] - **Step 1.1.3 [(Rule #59: IMPL-PLACE)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-59), [(Rule #56: DOC-INT)](./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md#rule-56):** **Create Missing Files:** Create all blank files identified in Step 1.1.1 as missing (e.g., `src/main.js`, `README.md`, `config/default.json`, `.gitignore`).
        - Place files in their correct, newly created or pre-existing directories.
        - For _newly created_ files that support comments (e.g., `.js`, `.py`, `.md`), inject relevant high-level plan comments (e.g., file purpose, related Phase/Task objective). Skip injection for non-commentable types or pre-existing files.
      - **Internal Success Criteria:**
        - Analysis of the initial sweep log is completed.
        - The required directory structure (either full initial or specific additions based on the plan and initial state) exists in the workspace.
        - Essential blank files (either full initial set or specific additions based on the plan and initial state) exist in the correct locations, without overwriting pre-existing files unless explicitly intended by the plan.
        - Newly created commentable files contain injected plan-related comments.
        - Compliance with all referenced Apex Standards Rules.
      - **Internal Verification Method:**
        - Verify the list of required vs. existing directories/files was correctly determined based on the plan and the initial sweep log.
        - List the directory structure _again_ and verify it matches the requirements identified in Step 1.1.1.
        - Check for the existence of the specified blank files in their correct locations.
        - Inspect the content of newly created files to verify comment injection (where applicable).
        - Verify compliance with referenced Apex Standards Rules for this Task and its Steps.
      - **Task Completion Testing (Internal):** N/A (Setup Task). Update internal development log.

  - **E.3. Step (`- [ ] \* **Step X.Y.Z [[(Rule #N: CODE)](<relative_path_to_standards>#rule-N), ...]:** Action`)**

    - Content: Begins with explicit **action verb**. Describes single action. **MUST** reference all applicable rules from `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` using the linked format `[(Rule #N: CODE)](<relative_path_to_standards>#rule-N)`, where `<relative_path_to_standards>` is the correct relative path from the plan file to the standards file (e.g., `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` if the plan is in the root).

  - **E.3.1. Optional: Sub-Step (`- [ ] \* **Sub-Step X.Y.Z.# [[(Rule #N: CODE)](<relative_path_to_standards>#rule-N), ...]:** Action`)**

    - Content: Begins with explicit **action verb**. Describes absolute atomic action. **MUST** reference all applicable rules from `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` using the linked format `[(Rule #N: CODE)](<relative_path_to_standards>#rule-N)`, where `<relative_path_to_standards>` is the correct relative path from the plan file to the standards file (e.g., `./STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` if the plan is in the root).

  - **E.4. Internal Success Criteria (within Task Block)**

    - Defines measurable conditions for Task completion. MUST implicitly include "Compliance with all referenced and linked Apex Standards Rules".

  - **E.5. Internal Verification Method (within Task Block)**

    - Defines agent actions to check Success Criteria. MUST include "Verify compliance with all referenced and linked Apex Standards Rules for this Task and its Steps".

  - **E.6. Task Completion Testing (Internal - within Task Block)**

    - Instructs agent to run relevant tests and update internal test log.

  - **E.7. Phase Completion Testing (Internal - end of Phase Block)**
    - Instructs agent to run cumulative Phase tests, check metrics, update internal test log.

- **F. Final Instruction:**

  - Explicitly commands start of execution, beginning with the **mandatory `Phase 0` sweep**, then proceeding sequentially through the subsequent phases/tasks, marking checkboxes, **adhering strictly to the linked `APEX_STANDARDS.md`**, and following the final reporting constraint.
  - Final explicit requirements to perform a last sweep over the tasks performed to look for gaps or missed areas.

- **G. Contextual Footer:**
  - Metadata: Timestamp, location. `*(Instructions generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location context: [Location])*`

## 5. Summary

This enhanced template mandates an **initial, comprehensive codebase sweep (Phase 0)** before other work begins. It requires strict adherence to the **Apex Software Compliance Standards Guide** (located at `STANDARDS_REPOSITORY/apex/APEX_STANDARDS.md` relative to the plan file) by requiring explicit, linked rule references in steps and verification checks. It includes an early task (Task 1.1) for ensuring the project structure conforms to the plan based on conditional logic informed by the initial sweep. It enforces sequential, verifiable, and high-quality autonomous execution.

_(Meta-structure v1.2.1 explanation updated [2025-04-19])_
