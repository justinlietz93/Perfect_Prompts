# TODO_CHECKLIST.md — TEMPLATE (Replace all `{...}`)

**TEMPLATE NOTICE:** This file is a **template scaffold**. It contains **only placeholders** in `{BRACES}` and example structure. **No real tasks are present.**  
Before using:
- Replace every `{...}` placeholder with project-specific content.
- Duplicate Phase/Task blocks as needed.
- Do **not** modify the header block below.

---

**IMPORTANT!** READ THIS ENTIRE HEADER.

Hierarchical execution plan for the Nexus desktop program. Phases contain Tasks; Tasks enumerate Steps with checkable items. Each Task concludes with explicit validation requirements referencing canonical anchors. Architecture document located at {filepath}

Begin the task by following the instructions below:

- **Set up your environment**, install all required packages, and immediately review any available AGENTS.md or ARCHITECTURE STANDARDS documents.

- Once that's been done, **review the repository** and all the working directories.

- **Check items off as you work on them**. Issues should be prioritized by impact on usability. Mark item CHECKBOXes as [DONE], [STARTED], [RETRYING], [DEBUGGING], [NOT STARTED], as you go and document your work under each item as you work.

- **You should not remain stagnant on an issue for too long**, if you get stuck on an item and it's marked [RETRYING] or [DEBUGGING], put an x# next to it, where # is the number of times you've attempted resolving it, for example [DEBUGGING x2].

- **If you hit x3 then move on** unless it's blocking anything else or if it would introduce significant technical debt if not addressed immediately. If it is a blocker like that, state this clearly in your response including "BLOCKER PREVENTING FURTHER DEVELOPMENT"

- If tests fail because of any missing packages or installations, **you need to install those and try to run the tests again.** Same thing if you run into errors for missing packages.

- **Mention which items you updated** on the checklist in your response, and your ETA or number of sessions until completion of the checklist.

---

## Template Fields (replace all `{...}`)
- `{project_name}` • `{project_root}` • `{filepath}` • `{owner}` • `{reviewers}` • `{ci_provider}`
- `{phase_number}` • `{phase_title}` • `{phase_purpose}`
- `{task_number}` • `{task_title}` • `{task_outcome}`
- `{step_number}` • `{step_description}` • `{notes}`
- `{evidence_a}` • `{evidence_b}` • `{evidence_c}`

## Project Metadata (Template)
- **Project:** `{project_name}`
- **Repo root:** `{project_root}`
- **Architecture doc:** `{filepath}`
- **Owner(s):** `{owner}` • **Reviewer(s):** `{reviewers}`
- **CI provider:** `{ci_provider}`

## Status Legend (use exactly these tags)
`[NOT STARTED]` • `[STARTED]` • `[DEBUGGING xN]` • `[RETRYING xN]` • `[DONE]`

---

## Phase {phase_number} — {phase_title}
> **Purpose (template):** {phase_purpose}

### Task {phase_number}.{task_number} — {task_title}
> **Outcome (template):** {task_outcome}

- [NOT STARTED] **Step {phase_number}.{task_number}.{step_number}** — {step_description}
  - _Notes:_ {notes}
- [NOT STARTED] **Step {phase_number}.{task_number}.{step_number+1}** — {step_description}
  - _Notes:_ {notes}
- [NOT STARTED] **Step {phase_number}.{task_number}.{step_number+2}** — {step_description}
  - _Notes:_ {notes}

#### **Task {phase_number}.{task_number} Validation (Template)**
- [ ] Evidence A — {evidence_a}
- [ ] Evidence B — {evidence_b}
- [ ] Evidence C — {evidence_c}

---

### Task {phase_number}.{task_number+1} — {task_title}
> **Outcome (template):** {task_outcome}

- [NOT STARTED] **Step {phase_number}.{task_number+1}.{step_number}** — {step_description}
  - _Notes:_ {notes}

#### **Task {phase_number}.{task_number+1} Validation (Template)**
- [ ] Evidence A — {evidence_a}
- [ ] Evidence B — {evidence_b}

---

## Additional Phase Block (Duplicate as needed)
> Copy the entire **Phase** and **Task** blocks above and adjust `{phase_number}`/`{task_number}`.

---

## Session Log (Template — append one row per session)
| Date (YYYY-MM-DD) | Items updated (IDs/steps) | Status summary (e.g., 0/XX DONE) | Notes / blockers |
|---|---|---|---|
| {date} | {e.g., 1.1.1, 1.2.2} | {e.g., 0/25 DONE} | {Add “BLOCKER PREVENTING FURTHER DEVELOPMENT” if applicable} |

