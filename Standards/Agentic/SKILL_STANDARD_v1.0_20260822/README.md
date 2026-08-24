# Skill Standard v1.0.0

Canonical-candidate standard for building and maintaining reusable LLM/agent **skill packages**.

This standard is derived from a holistic audit of the supplied **Perfect Prompts** repository, with special emphasis on the `skills/` stratum and its surrounding composition layers.

## Package contents

- `SKILL_STANDARD_v1.0_20260822.md` — canonical Markdown source.
- `SKILL_STANDARD_v1.0_20260822.docx` — formatted review copy.
- `SKILL_PACKAGE_METADATA.schema.json` — machine-readable metadata schema.
- `examples/SKILL_PACKAGE_METADATA.example.json` — schema-valid example contract.
- `SKILL_CONFORMANCE_CHECKLIST.md` — promotion/review gate.
- `PERFECT_PROMPTS_SKILL_HOLISTIC_AUDIT.md` — repository-wide skill evidence audit.
- `SOURCE_MAP.md` — evidence strata and authority map.
- `CHANGELOG.md` — revision history.
- `MANIFEST.json` and `SHA256SUMS` — package integrity.

## Core rule

**A skill is a procedural package, not merely a long prompt.**

The standard separates skills from prompt templates, personas, methodologies, rulesets, AGENTS files, and transient state while allowing skills to compose with all of them.
