# Source Map

## Controlling synthesis

This standard extracts evergreen documentation rules while avoiding project-specific folder names or site-generator requirements.

## Primary sources

- `Standards/architecture_standards/SGDA_DOCUMENTATION_ARCHITECTURE_STANDARDS.md` - authority classes, current/draft/archive/generated separation, duplicate-authority rule, generated-artifact discipline, links/contracts/governance.
- `Standards/PROMPT_TEMPLATE_STANDARD_v1.1_20260822/` - authority, state, projection, provenance, lifecycle distinctions.
- `Standards/SKILL_STANDARD_v1.0_20260822/` - canonical source versus runtime/distribution representations.
- `Templates/ORCHESTRA_RESEARCH_PACKAGE_TEMPLATE_v2.0_20260804/AUTHORITY.md` and related package files - explicit authority precedence, source maps, manifests, handoff separation.
- VDM_RT documentation history and walker-consolidation failure analysis - source-folder docs must remain durable anatomy/rationale; implementation work must not rewrite canon and then validate against the rewrite.

## Retained project-specific lessons, generalized

- Durable resident docs are not change receipts.
- Snapshots/history cannot replace canonical anatomy.
- Tooling and generated projections do not outrank semantics.
- Documentation changes need custody and provenance.

## Explicit non-promotions

- MkDocs-specific directory shapes and commands are examples only.
- VDM_RT folder names are not universal requirements.
- One project's status vocabulary is not imposed where another repository already has an explicit compatible vocabulary.
