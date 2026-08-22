# Meta-Structure Definition - Mini Version (for Small Tasks) v0.5.0

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM UTC+/-Offset]

## 1. Overall Purpose
Defines a simple structure for guiding an LLM agent through small, sequential tasks.

## 2. Core Execution Principles
* **Sequential Execution:** Tasks and Steps MUST be executed in the order listed. Mark each `- [ ]` as complete `- [x]` before proceeding.
* **Verification:** Briefly check the result of each Step/Task against its objective before moving on.
* **Error Handling:** If a step fails or produces an incorrect result, STOP execution and report the issue. Do not proceed.
* **Autonomous Operation:** Execute autonomously. Report only upon completion or if an error occurs.
* **General Quality:** Apply standard best practices for code quality, clarity, and security appropriate for the task.

## 3. Prompt Template Structure

* **A. Overall Formatting:**
    * Enclose prompt in ```markdown ... ```.
    * Task/Step items MUST begin with `- [ ]`.

* **B. Subject Line:**
    * Format: `Subject: [ACTION-ORIENTED TITLE for Small Task]`

* **C. Directive Section:**
    * Briefly state the overall goal. Mention sequential execution, completion marking (`- [x]`), and reporting on completion or error. Example: "Execute the following steps sequentially to [goal]. Mark checkboxes upon completion. Report final status or any errors."

* **D. Execution Blocks:**
    * Uses simple list format. Tasks are optional for very small prompts; Steps might be sufficient.
    * **Every Task/Step MUST start with `- [ ]`.**

    * **Optional: Task Block (`- [ ] **Task X: Name**`)**
        * Content: `* **Objective:**`, Step list items. Includes simplified `Success Check`.

    * **Step (`- [ ] * **Step X.Y:** Action`)**
        * Content: Begins with an **action verb**. Describes a single, clear action. Conceptual rule references like `(Rule: Formatting)` can be used sparingly if needed.

    * **Success Check (within Task Block or after a Step)**
        * Content: Briefly state how to check if the Task/Step was successful. Example: `* **Success Check:** Verify the file '[filename]' exists and contains '[expected content fragment]'."`

* **E. Final Instruction:**
    * Explicitly command start. Example: `Begin execution with the first step.`

* **F. Contextual Footer:**
    * Optional: `*(Generated: [YYYY-MM-DD HH:MM].)*`

## 4. Example Snippet

```markdown
Subject: Refactor utility function

Directive: Sequentially refactor the `calculate_sum` function. Mark steps complete. Report final status or errors.

- [ ] **Task 1: Refactor `calculate_sum`**
    * **Objective:** Improve clarity and add basic error handling.
    - [ ] * **Step 1.1:** **Modify** function signature in `utils/math.js` to accept an array of numbers instead of two arguments. (Rule: Clarity)
    - [ ] * **Step 1.2:** **Implement** logic to iterate through the array and sum valid numbers.
    - [ ] * **Step 1.3:** **Add** basic type checking to ensure input is an array and elements are numbers. Return `NaN` or throw an error on invalid input. (Rule: Robustness)
    * **Success Check:** Verify `utils/math.js` contains the updated function and it handles array input and non-number elements correctly (manual inspection or simple test case).

- [ ] **Task 2: Update Callers**
    * **Objective:** Update code that uses the old function signature.
    - [ ] * **Step 2.1:** **Identify** all locations where `calculate_sum` is called in the project.
    - [ ] * **Step 2.2:** **Update** each call site to pass an array instead of separate arguments.
    * **Success Check:** Verify all identified call sites have been updated (manual code review or search).

Begin execution with the first step.
*(Generated: 2025-04-10 20:45.)*