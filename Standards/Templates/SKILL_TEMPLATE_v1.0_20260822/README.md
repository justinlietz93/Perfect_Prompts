# Canonical Skill Template v1.0.0

Reusable scaffold for creating LLM/agent skill packages conforming to `SKILL_STANDARD_v1.0_20260822`.

## Core rule

**The template standardizes the package contract, not the procedure inside every skill.**

## Quick start

```bash
python tools/init_skill.py --id my-skill --title "My Skill" --destination /path/to/output
python /path/to/output/my-skill/tools/validate_skill.py /path/to/output/my-skill
```

The initializer creates an instantiated copy and replaces the basic identity placeholders. The author then removes unused optional directories/sections and fills in the actual skill procedure.

## Included structure

- `SKILL.md` — canonical skill entrypoint template.
- `SKILL_METADATA.json` — machine-readable skill contract.
- `AUTHORITY.md` — authority and conflict semantics.
- `PACKAGE.json` — template/package identity.
- `references/`, `scripts/`, `schemas/`, `assets/`, `agents/`, `examples/`, `tests/` — optional support layers with README guidance.
- `tools/init_skill.py` — deterministic instantiation helper.
- `tools/validate_skill.py` — structural/conformance validator.
- `tools/build_manifest.py` — integrity manifest builder.
- `BUILD_CHECKLIST.md` — authoring and promotion checklist.
- `INSTANTIATION_GUIDE.md` — how to specialize the scaffold without turning it into a universal hammer.
- `TEMPLATE_STATUS.md`, `SOURCE_MAP.md`, `CHANGELOG.md` — lifecycle/provenance.

Unused optional directories should be deleted from finished skills rather than kept as empty ceremony.
