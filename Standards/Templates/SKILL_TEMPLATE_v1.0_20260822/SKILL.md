---
name: "{{SKILL_ID}}"
description: "{{ONE_SENTENCE_ACTIVATION_DESCRIPTION}}"
version: "0.1.0"
status: "DRAFT"
---

# {{SKILL_TITLE}}

## Purpose

State the reusable capability this skill provides. Define the semantic job, not the implementation mechanism.

## Capability Boundary

### Use when

- {{OBSERVABLE_TASK_CONDITION_1}}
- {{OBSERVABLE_TASK_CONDITION_2}}

### Do not use when

- {{NEGATIVE_SCOPE_CONDITION_1}}
- {{NEGATIVE_SCOPE_CONDITION_2}}

### Neighboring artifact classes

State which standards, prompt templates, methodologies, rulesets, personas, state packages, or other skills may be composed with this skill. Do not silently absorb their authority.

## Inputs

### Required inputs

- {{REQUIRED_INPUT_1}}

### Optional inputs

- {{OPTIONAL_INPUT_1}}

### Insufficient-input behavior

State what the agent should do when a genuinely required input is absent.

## Modes

Delete this section if the skill has only one mode.

### {{MODE_A}}

**Select when:** {{MODE_SELECTION_RULE}}

Describe what changes in this mode.

## Supporting Artifacts

List only load-bearing artifacts and explain why they exist.

| Artifact | Role | Required? |
|---|---|---|
| `references/README.md` | Domain/reference index | No |
| `scripts/README.md` | Helper-script index | No |
| `schemas/README.md` | Machine-readable contract index | No |
| `agents/README.md` | Runtime-binding notes | No |

If a supporting artifact is required for correct execution, explicitly instruct the agent when to read or invoke it.

## Procedure

Describe the actual reusable workflow. The procedure may differ completely from other skills.

### Step 1 — {{STEP_NAME}}

{{LOAD_BEARING_ACTION}}

### Step 2 — {{STEP_NAME}}

{{LOAD_BEARING_ACTION}}

### Step 3 — Validate and close

Apply the skill's declared quality gates and verify that the output contract has been satisfied.

## Output Contract

The skill must state exactly what it produces.

### Primary output

- {{PRIMARY_OUTPUT}}

### Additional artifacts

- {{OPTIONAL_OR_REQUIRED_ARTIFACT}}

### Output location

State any required output directory or packaging convention. Delete if irrelevant.

## Validation and Quality Gates

Completion requires all applicable gates to pass.

- [ ] {{QUALITY_GATE_1}}
- [ ] {{QUALITY_GATE_2}}
- [ ] Output contract is complete.
- [ ] No required supporting artifact was skipped.

When correctness is machine-checkable, place the validator in `scripts/` or `tests/` and reference it here.

## Failure and Escalation Behavior

Define what happens when:

- required input is missing;
- a dependency is unavailable;
- validation fails;
- the task falls outside scope;
- another canonical skill is a better fit.

## Runtime and Dependencies

### Required dependencies

- {{DEPENDENCY_OR_NONE}}

### Runtime bindings

Runtime-specific metadata belongs under `agents/` or another clearly named adapter layer. Runtime wrappers may adapt presentation but must preserve the semantic capability.

## Anti-Patterns

- Do not broaden the skill beyond its declared capability because adjacent work is convenient.
- Do not hide critical procedure in an unreferenced side file.
- Do not treat trigger keywords as stronger than the semantic task.
- Do not let a binary distribution replace inspectable canonical source.
- Add skill-specific anti-patterns here.

## Provenance and Lifecycle

**Source lineage:** {{SOURCE_LINEAGE_OR_NONE}}  
**Supersedes:** {{SUPERSEDES_OR_NONE}}  
**Promotion evidence:** {{USAGE_AND_VALIDATION_EVIDENCE}}
