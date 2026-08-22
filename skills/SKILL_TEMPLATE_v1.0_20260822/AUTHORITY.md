# Authority

## Controlling sources

1. `SKILL_STANDARD_v1.0_20260822` controls whether an instantiated package conforms to the canonical Skill Standard.
2. The instantiated skill's own `SKILL.md` controls its task-specific procedure inside its declared capability boundary.
3. Imported standards, methodologies, prompt templates, rulesets, personas, and state packages retain their own authority and are not silently rewritten by the skill.

## Conflict rule

When sources conflict, identify which source controls the disputed semantic layer. Do not silently merge incompatible requirements.

## Template boundary

This template standardizes package anatomy and control surfaces. It does not prescribe one workflow for all skills.
