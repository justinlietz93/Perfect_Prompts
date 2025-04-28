# Meta-Structure Definition - Medium Complexity Tasks v0.8.0

**Date:** [YYYY-MM-DD]
**Time:** [HH:MM UTC+/-Offset]

## 1. Overall Purpose
This document defines a structured template for prompts intended to guide an LLM agent in executing moderately complex, sequential tasks. It balances the need for clear instructions and verification with reduced overhead compared to the full autonomous execution template, making it suitable for feature implementation, configuration setups, or significant refactoring tasks.

## 2. Core Execution Principles
* **Sequential Execution:** Tasks and Steps MUST be executed in the listed order. Each item MUST begin with `- [ ]` and be marked complete `- [x]` before proceeding to the next.
* **Task-Level Verification:** Each Task includes a `Task Verification` section outlining expected outcomes and checks. The agent MUST perform these checks upon completing the Task's steps.
* **Error Handling:** If `Task Verification` fails or a significant error occurs during a step:
    * Attempt **one** cycle of identifying the issue, correcting the relevant step(s), and re-running the verification.
    * If verification still fails after the correction attempt, STOP execution and report the error and the state of the task. Do not proceed.
* **Autonomous Operation & Reporting:** Execution should be autonomous. Report only upon successful completion of all tasks or when an unrecoverable error (per the rule above) occurs. Internal logging should be minimal unless specified.
* **Quality & Best Practices:** Adhere to general software development best practices (e.g., clarity, modularity, security considerations) and any project-specific guidelines mentioned within the prompt or readily available (e.g., a `CONTRIBUTING.md` or style guide). Explicit linked rule adherence like in the Full template is *not* required unless specifically stated for a critical step.

## 3. Prompt Template Structure

* **A. Overall Formatting:**
    * Enclose the entire prompt in ```markdown ... ```.  *(Note: This instruction refers to how the prompt *instance* should be formatted when used, not this template definition itself)*
    * All Task and Step items MUST begin with `- [ ]`.

* **B. Subject Line:**
    * Format: `Subject: [ACTION-ORIENTED TITLE for Medium Task]`

* **C. Directive Section:**
    * Clearly state the overall goal of the prompt.
    * Mention the requirement for sequential execution, completion marking (`- [x]`), adherence to best practices, the task-level verification process, and the reporting conditions (completion or error after retry).
    * Example: "Execute the following tasks sequentially to [overall goal]. Mark checkboxes upon completion. Adhere to standard coding practices. Verify each task using the provided checks, attempting one correction cycle if needed. Report final status or any unrecoverable errors."

* **D. Execution Blocks:**
    * Uses a `Task -> Step` hierarchy. Markdown headings/lists. Separated by `---` between Tasks is recommended for clarity.
    * **Every Task and Step MUST start with `- [ ]`.**

    * **D.1. Task Block (`- [ ] **Task X: Name**`)**
        * Content: `* **Objective:**`, a list of Step items, and `* **Task Verification:**`.

    * **D.2. Step (`- [ ] * **Step X.Y [(Optional Guideline/Best Practice)]:** Action`)**
        * Content: Begins with an explicit **action verb**. Describes a single, logical action. May include optional, non-linked references to key guidelines or best practices like `(Best Practice: Modularity)` or `(Guideline: Use Config File)` if helpful.

    * **D.3. Task Verification (within Task Block)**
        * Content: Defines clear, checkable conditions for task success and the method to verify them. This combines the intent of `Internal Success Criteria` and `Internal Verification Method` from the Full template but is less formal. It MUST confirm that the steps were completed correctly and align with the Task Objective and mentioned best practices.
        * Example: `* **Task Verification:** Check that the file 'src/new_module.py' exists and contains the 'NewClass' definition. Confirm basic linting passes on the new file. Verify the configuration file 'config/settings.yaml' includes the 'new_module_enabled: true' setting.`

* **E. Final Instruction:**
    * Explicitly command the start of execution.
    * Example: `Begin execution starting with Task 1, Step 1.1. Follow all instructions sequentially.`

* **F. Contextual Footer:**
    * Optional: Include generation timestamp or other relevant metadata.
    * `*(Generated: [YYYY-MM-DD HH:MM UTC+/-Offset]. Location: [Location])*`

## 4. Example Snippet (Illustrates how to *use* the template)

```markdown
Subject: Add User Profile Endpoint

Directive: Execute the following tasks sequentially to add a new API endpoint for retrieving user profiles. Mark checkboxes upon completion. Adhere to standard REST API and Python coding practices. Verify each task using the provided checks, attempting one correction cycle if verification fails. Report final status or any unrecoverable errors.

- [ ] **Task 1: Define API Route and Handler**
    * **Objective:** Create the basic API route and a placeholder handler function for fetching user profiles.
    - [ ] * **Step 1.1 (Guideline: REST Naming):** **Define** a GET route `/api/v1/users/{user_id}/profile` in the main router file (`app/routes.py`).
    - [ ] * **Step 1.2 (Best Practice: Separation of Concerns):** **Create** a new handler function `get_user_profile(user_id)` in the user controller module (`app/controllers/user_controller.py`).
    - [ ] * **Step 1.3:** **Implement** a placeholder response in `get_user_profile` that returns a dummy user profile JSON object (e.g., `{'user_id': user_id, 'name': 'Placeholder User', 'email': 'placeholder@example.com'}`).
    - [ ] * **Step 1.4:** **Connect** the route defined in Step 1.1 to call the handler function created in Step 1.2.
    * **Task Verification:**
        * Check that the `/api/v1/users/{user_id}/profile` route is registered correctly in `app/routes.py`.
        * Verify the `get_user_profile` function exists in `app/controllers/user_controller.py` and returns a valid JSON structure.
        * Manually test the endpoint (e.g., using curl or a test client) with a sample `user_id` and confirm it returns the placeholder 200 OK response.

---

- [ ] **Task 2: Implement Profile Data Retrieval**
    * **Objective:** Replace the placeholder logic with actual data retrieval from a simulated database service.
    - [ ] * **Step 2.1 (Guideline: Use Service Layer):** **Import** the `UserService` (assuming it exists at `app/services/user_service.py`).
    - [ ] * **Step 2.2:** **Modify** the `get_user_profile` handler to call a method like `UserService.find_profile_by_id(user_id)`.
    - [ ] * **Step 2.3:** **Add** basic error handling: if the user profile is not found by the service, return a 404 Not Found response.
    - [ ] * **Step 2.4 (Best Practice: Data Transfer Objects):** Ensure the data returned from the service is formatted into the expected API response structure (if different).
    * **Task Verification:**
        * Review the `get_user_profile` function code to confirm it calls the `UserService` and handles the 'not found' case correctly.
        * Manually test the endpoint with a known existing `user_id` (assuming test data exists) and verify correct profile data is returned.
        * Manually test the endpoint with a non-existent `user_id` and verify a 404 status code is returned.

Begin execution starting with Task 1, Step 1.1. Follow all instructions sequentially.
*(Generated: 2025-04-10 22:43 UTC-5. Location: Menasha, Wisconsin, United States)*