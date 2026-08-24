# Skill Conformance Checklist

Use this checklist when reviewing whether a skill package is ready for canonical-candidate or canonical status.

## Identity and scope

- [ ] Stable skill ID exists.
- [ ] Human-readable title exists.
- [ ] Explicit version exists.
- [ ] Status is declared.
- [ ] Purpose is clear.
- [ ] Capability scope is explicit.
- [ ] Primary entry artifact is identified.

## Activation contract

- [ ] `use_when` guidance exists.
- [ ] `do_not_use_when` guidance exists.
- [ ] Trigger language is supportive rather than the only activation mechanism.
- [ ] Multi-mode behavior, if present, is named and scoped.

## Package anatomy

- [ ] Canonical entrypoint exists (normally `SKILL.md`).
- [ ] Supporting artifacts are discoverable.
- [ ] The package structure is semantically organized.
- [ ] Binary delivery forms do not replace inspectable source.

## Procedure

- [ ] The workflow/steps are externally visible.
- [ ] Critical reads/lookups are declared.
- [ ] Supporting scripts/schemas are mentioned where required.
- [ ] The skill is operational, not merely descriptive.

## Output and validation

- [ ] Output contract is explicit.
- [ ] Multi-artifact outputs, if any, are named.
- [ ] Completion conditions are explicit.
- [ ] Quality gates are explicit.
- [ ] Validators/tests/checklists exist where warranted.

## Runtime and portability

- [ ] Runtime-specific bindings are documented if present.
- [ ] Environment/dependency assumptions are documented when relevant.
- [ ] Semantic parity across bindings is preserved.

## Provenance and lifecycle

- [ ] Source lineage is recorded.
- [ ] Supersession/deprecation state is recorded where relevant.
- [ ] Historical artifacts are not confused with current canonical source.

## Promotion recommendation

- [ ] READY for canonical-candidate review.
- [ ] Needs revision before promotion.
- [ ] Useful artifact, but should remain non-canonical for now.
