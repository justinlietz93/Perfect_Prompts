# Source Map

## Authority status

This package is a **canonical candidate** for the new canonical standards library. Perfect Prompts is treated as a reference/evidence corpus unless an artifact is separately adopted into the canonical library.

## Primary repository-wide evidence

### Current repository self-description

- `Perfect_Prompts-main/README.md`
  - Defines the repository as a working corpus of prompt engineering, context engineering, agent control, AI-assisted software development, research methodology, and reusable LLM tooling.
  - Explicitly states that there is no single best prompt.
  - Describes prompts as parts of system architecture interacting with instructions, context, tools, state, validation, and handoff behavior.
  - Warns that not every file is canonical or current.

### Persistent agent behavior

- `AGENTS_library/No-Assumptions_AGENTS.md`
  - Think-before-code, simplicity, surgical changes, goal-driven verification.
  - Explicitly notes the caution/speed tradeoff and need for judgment on trivial tasks.

- `Methodologies/Germinal_Theory/Emergence_Based_Design_AGENTS.md`
  - Inspect before changing.
  - Architecture must emerge from evidence/constraints rather than generic patterns.
  - Preserve identity, history, intent, and provenance.
  - Invariants before mechanisms.
  - Friction is evidence.
  - Boundaries must remain boundaries.

### Methodology

- `Methodologies/Guided_Autonomy_Prompting/GAP_Domain_Agnostic.md`
- `Methodologies/Guided_Autonomy_Prompting/GAP_Physics.md`
- `skills/GAP_prompting_skill/SKILL.md`
  - Strong evidence for constrained autonomy as a selectable method.
  - Model-mechanism explanations about “activating chain of thought” are not retained as canonical requirements.

### Durable state and context engineering

- `structured_text/context_builder_prompts/Universal_Context_Synthesis_Engine_prompt.md`
- `plaintext/context_builder_prompts/Session_State_Persistence_Protocol_prompt.md`
- `skills/session_handoff_skill/SKILL.md`
- `skills/session_handoff_skill/state_schema.md`
  - Decisions, assumptions, rejected paths, unresolved questions, state snapshots, next actions, and environment state are first-class artifacts.
  - Handoff is an explicit context-engineering operation rather than a conversational summary.

### Long-running engineering orchestration

- `plaintext/agent_prompts/RooCode-Task.md`
- `skills/repository-build-orchestrator.md`
- `skills/audit-and-instruct.md`
  - Repository-resident state, plans, TODO ledgers, local contracts, dependency ordering, validation, and resumability.
  - Demonstrate later evolution beyond early prompt-only meta-structures.

### Context economy

- `plaintext/agent_prompts/Token_Discipline.txt`
  - Context is a managed resource.
  - Prefer maintained durable state and targeted retrieval when sufficient.
  - Build/reuse tools to reduce repeated prompting.

### Prompt-system composition

- `python/agent_prompts/system/*.py`
  - Separates objective, capabilities, tools, rules, modes, editing behavior, MCP/tool usage, examples, and custom instructions.
  - Strong evidence for compositional system prompts rather than one monolith.

### Prompt harnesses and portability

- `plaintext/agent_prompts/`
- `python/agent_prompts/`, `python/summary_prompts/`
- `typescript/`
- `rust/`
- `go/`
  - Same conceptual prompt families represented in several language/runtime bindings.
  - Supports semantic-contract-first portability.

### Specialized views and transformations

- `plaintext/summary_prompts/`
- `python/summary_prompts/`
- corresponding Go/Rust/TypeScript variants
  - Multiple projections of the same source context: timeline, process flow, risk register, RACI, graph/tree, glossary, decision matrix, walkthrough, etc.
  - Supports the rule that projections do not automatically become authority.

### Personas and multi-agent critique

- `PERSONAS/`
- `python/agent_prompts/critique_*`
- `python/agent_prompts/critique_council/`
- `plaintext/grok_4.20_teams/research_team/`
  - Specialized roles are composable perspectives, not universal truth sources.

### Skills

- `skills/rigorous_research/`
- `skills/comprehensive-data-analysis/`
- `skills/session_handoff_skill/`
- `skills/pdf/`
- `skills/readme-generator.skill`
- `skills/repository-build-orchestrator.md`
- `skills/audit-and-instruct.md`
  - Skills combine instructions with schemas, scripts, validators, references, and output packages.
  - Supports keeping skill architecture distinct from prompt-template architecture.

## Historical evidence stratum

- `STANDARDS_REPOSITORY/prompt-templates/`
  - Primarily April 2025 prompt-template work.
  - Valuable for early meta-structure, task classes, explicit success criteria, phase decomposition, analysis/research/testing distinctions, and prompt specialization.
  - Not treated as the repository's current center of gravity.

- `STANDARDS_REPOSITORY/apex/`
- `STANDARDS_REPOSITORY/nasa/`
  - Early standards synthesis and software-quality lineage.

## Later ruleset evidence

- `rules/` (mostly explicit dates September–December 2025)
  - Shows domain-specific rule modules rather than one global rule corpus.
  - Supports selective loading and scoped standards.

## Non-authoritative / scoped mechanisms

The following are retained only within justified scopes and are not promoted as universal prompt rules:

- Hybrid-Clean as the mandatory default architecture.
- recursive full-repository sweeps for every task.
- runtime-specific completion/tool names.
- fixed output directories tied to one platform.
- fixed attempt counts for every research task.
- mandatory personas.
- mandatory phase/task/step decomposition for atomic work.
- unbounded “professional defaults.”
- chain-of-thought/attention-mechanism explanations as a normative basis.
