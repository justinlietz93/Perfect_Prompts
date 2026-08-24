# Prompt Template Standard v1.1.0

Canonical-candidate standard for building and maintaining a family of specialized LLM prompt templates without collapsing them into a universal workflow.

This revision is grounded in a holistic audit of the supplied **Perfect Prompts** repository rather than the historical April 2025 `STANDARDS_REPOSITORY/prompt-templates/` directory alone.

## Package contents

- `PROMPT_TEMPLATE_STANDARD_v1.1_20260822.md` — canonical Markdown source.
- `PROMPT_TEMPLATE_STANDARD_v1.1_20260822.docx` — formatted review copy.
- `PROMPT_TEMPLATE_METADATA.schema.json` — machine-readable metadata schema.
- `examples/PROMPT_TEMPLATE_METADATA.example.json` — schema-valid example contract.
- `PROMPT_TEMPLATE_CONFORMANCE_CHECKLIST.md` — promotion/review gate.
- `PERFECT_PROMPTS_HOLISTIC_AUDIT.md` — repository-wide evidence audit.
- `SOURCE_MAP.md` — evidence strata and authority map.
- `CHANGELOG.md` — revision history.
- `MANIFEST.json` and `SHA256SUMS` — package integrity.

## Core rule

**Standardize the contract around a prompt template, not the job performed inside every template.**

The v1.1 revision also recognizes the larger context-engineering stack around templates: standards, methodologies, AGENTS instructions, rulesets, personas, state packages, tools, validators, handoffs, skills, and runtime bindings remain distinct layers.
