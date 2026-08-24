# Perfect Prompts Skill Holistic Audit

## Audit objective

Derive evergreen canonical rules for **skill packages** from the supplied Perfect Prompts repository without collapsing skills into prompt templates or overfitting to one historical skill.

## Repository evidence summary

The `skills/` stratum contains a mixed family of capability packages and skill-like artifacts.

Observed top-level items included:

- directory-form skills such as `GAP_prompting_skill`, `session_handoff_skill`, `comprehensive-data-analysis`, `pdf`, and `rigorous_research`;
- single-file skill-like artifacts such as `audit-and-instruct.md`, `repository-build-orchestrator.md`, and `Game-Visual-Asset-Creation-Skill-Prompt.md`;
- runtime/distribution packages such as `*.zip` and `*.skill` bundles;
- runtime metadata such as `agents/openai.yaml`;
- helper scripts such as `validate_snapshot.py` and `render_mermaid.py`;
- reference artifacts such as `state_schema.md` and domain templates.

## Strong recurring patterns

### 1. Controlling entrypoint

Most mature skills use `SKILL.md` as the controlling entrypoint.

This file typically carries:

- purpose;
- activation triggers;
- workflow;
- critical rules;
- references/scripts to read or invoke;
- output expectations;
- anti-patterns or quality gates.

This is strong evidence that a skill must have a visible control document rather than relying on folder osmosis.

### 2. Skills package more than prompts

The strongest skills do not stop at prose instructions. They package:

- reference schemas (`state_schema.md`);
- helper scripts (`validate_snapshot.py`, `render_mermaid.py`);
- runtime UI metadata (`agents/openai.yaml`);
- assets (`pdf/assets/pdf.png`);
- alternate delivery forms (`.zip`, `.skill`).

This is direct evidence for the core rule that a skill is a procedural package rather than merely a prompt.

### 3. Internal workflow heterogeneity is legitimate

No single workflow explains all skills:

- GAP has recognition-driven two-mode behavior.
- Session Handoff emphasizes context capture and manifest generation.
- Comprehensive Data Analysis emphasizes staged analytical execution and package assembly.
- PDF emphasizes environment setup and rendering behavior.
- Rigorous Research emphasizes claim/evidence burden management.

Therefore the evergreen standard must govern the **package contract**, not impose one internal method.

### 4. Runtime wrappers are secondary

The presence of `.zip`, `.skill`, and runtime YAML artifacts shows that skills may be surfaced in multiple environments.

However, these wrappers are poor canonical authorities because they hide structure and are not always inspectable. The canonical source must remain plain-file and navigable.

### 5. Small skill-like artifacts still need boundary clarity

Some top-level Markdown skill files are much flatter than the directory-form skills. This shows that a skill may be small, but it still needs explicit identity, activation contract, and output/procedure clarity.

## Canonical rules derived

The following rules were promoted into the Skill Standard:

1. A skill is a distinct artifact class.
2. A skill must expose a stable identity.
3. A skill must declare activation boundaries.
4. A skill should have a canonical entrypoint.
5. Supporting artifacts are load-bearing when they materially affect execution.
6. Outputs and quality gates must be explicit.
7. Runtime wrappers must preserve semantic parity but not replace canonical source.
8. Canonicalization requires more than a clever prompt; it requires a usable package.

## Non-promoted specifics

The following were intentionally *not* promoted to evergreen universal rules:

- exact file manifests from session-handoff outputs;
- hard-coded iteration counts from analysis skills;
- one provider’s runtime metadata schema;
- any requirement that every skill include scripts, assets, or validators;
- domain-specific burden-scoring systems from one research workflow.

## Resulting repository implication

The canonical standards library should contain a **Skill Standard** that governs what makes a skill package canonical.

The library may then separately contain:

- canonical skill templates;
- individual canonical skills;
- archived or experimental skills;
- runtime packaging adapters.
