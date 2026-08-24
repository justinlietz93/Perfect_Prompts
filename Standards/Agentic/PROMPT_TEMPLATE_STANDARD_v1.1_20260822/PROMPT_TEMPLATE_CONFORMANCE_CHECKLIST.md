# Prompt Template Conformance Checklist

Use this before promoting a prompt template to canonical status.

## Identity

- [ ] Stable template ID exists.
- [ ] Human-readable title exists.
- [ ] Version is explicit.
- [ ] Status is explicit.
- [ ] Task class is explicit.
- [ ] Purpose and semantic scope are explicit.

## Applicability and routing

- [ ] `Use when` conditions identify observable task properties.
- [ ] `Do not use when` conditions prevent obvious misuse.
- [ ] The template is narrower than any general fallback that might overlap it.
- [ ] Overlap with other canonical templates is either absent or explicitly routed.
- [ ] Multi-stage use declares predecessor/successor stages when relevant.

## Authority

- [ ] Governing standards are named when relevant.
- [ ] Required project/domain authority inputs are named.
- [ ] Generic template rules cannot silently override project canon.
- [ ] Current implementation/state is not confused with semantic authority.
- [ ] Any intentional deviation from a governing standard is explicit and scoped.

## Inputs and context

- [ ] Required semantic inputs are identified.
- [ ] Required operational inputs are identified.
- [ ] Optional context is distinguished from required context.
- [ ] Safe defaults are bounded.
- [ ] Missing-input behavior is explicit.
- [ ] Material requirements cannot be invented by defaulting.
- [ ] State/context inputs are scoped to what can change the result.
- [ ] Accepted decisions, rejected paths, assumptions, and unknowns remain distinct when relevant.

## Neighboring instruction layers

- [ ] Methodology requirements are declared when relevant.
- [ ] Ruleset dependencies are declared when relevant.
- [ ] Persona use is required/optional/forbidden explicitly when material.
- [ ] The template does not absorb unrelated standards, rules, personas, or methods merely for completeness.
- [ ] Skill outputs or handoff artifacts are treated as separate artifact classes when applicable.

## Execution and tools

- [ ] Interaction mode is clear when material.
- [ ] Mutation authority is clear when material.
- [ ] Required tools/capabilities are explicit.
- [ ] Runtime/provider-specific tool semantics are kept at the boundary.
- [ ] Consequential work requires appropriate ground-truth inspection rather than ritual full scans.

## Output and validation

- [ ] Output artifact/format is explicit.
- [ ] Structured output is used only when it serves a real consumer.
- [ ] Validation channel is defined when correctness requires evidence.
- [ ] A successor reviewer/validator is declared if validation is staged.
- [ ] Completion condition is observable.
- [ ] Partial completion and failure behavior are explicit.

## Portability

- [ ] If multiple language/runtime bindings share this template ID, their semantic contracts are equivalent.
- [ ] Runtime wrappers may vary without changing task meaning.
- [ ] A semantic change triggers a version change or a new template identity.

## Lifecycle and provenance

- [ ] Source lineage is recorded.
- [ ] Historical source material is not treated as authority by location alone.
- [ ] Superseded/deprecated predecessors are identified.
- [ ] Representative normal, boundary, misuse, and failure cases have been tested before canonical promotion.
- [ ] Evidence from observed model behavior supports canonical status.

## Final gate

- [ ] A reviewer can explain what the template does, why it is selected, what controls it, what state it needs, what it may change, what it must produce, how it is checked, and when it is finished without guessing.
