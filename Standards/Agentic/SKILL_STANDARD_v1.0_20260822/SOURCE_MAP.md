# Source Map

## Primary evidence base

Holistic audit of the supplied `Perfect_Prompts-main` repository, especially:

- `skills/GAP_prompting_skill/`
- `skills/session_handoff_skill/`
- `skills/comprehensive-data-analysis/`
- `skills/pdf/`
- `skills/rigorous_research/`
- `skills/repository-build-orchestrator.md`
- `skills/audit-and-instruct.md`
- `skills/Game-Visual-Asset-Creation-Skill-Prompt.md`
- runtime-side `agents/*.yaml`
- distribution forms `*.zip`, `*.skill`

## Key retained conclusions

1. Skills are a distinct artifact class and cannot be reduced to prompt templates.
2. `SKILL.md`-style entrypoints are functioning as canonical control documents.
3. Supporting artifacts (schemas, scripts, assets, validators, bindings) are load-bearing parts of the capability.
4. Different skills legitimately use different internal workflows.
5. Runtime bindings and binary distributions should remain secondary to inspectable canonical source.
6. The package boundary between standards, methodologies, rulesets, personas, prompt templates, skills, and state must remain explicit.

## Important non-promotions / exclusions

The following were treated as evidence, not directly canonized as evergreen rules:

- fixed “3 attempts max” style tactical heuristics from particular skills;
- domain-specific workflow details unique to VDM publication or PDF handling;
- provider/runtime-specific UI metadata fields;
- project-specific artifact names where the pattern matters more than the literal filenames;
- any implication that every skill needs every subdirectory or every helper type.

## Companion standards

- `PROMPT_TEMPLATE_STANDARD_v1.1_20260822`

The Skill Standard deliberately does not restate the full prompt-template contract; it focuses on procedural capability packaging.
