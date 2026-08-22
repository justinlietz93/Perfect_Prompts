# Build Checklist

## Classification
- [ ] This artifact is actually a reusable procedural capability.
- [ ] It is not better represented as a prompt template, methodology, ruleset, persona, AGENTS file, profile, or one-off project instruction.

## Identity
- [ ] Skill ID, title, version, status, purpose, scope, and entrypoint are complete.

## Activation
- [ ] `use_when` is specific.
- [ ] `do_not_use_when` is specific.
- [ ] Any modes have explicit selection rules.

## Package
- [ ] `SKILL.md` is controlling entrypoint.
- [ ] Every load-bearing side artifact is referenced by `SKILL.md`.
- [ ] Unused optional directories were removed.
- [ ] Binary/runtime distributions are secondary to inspectable source.

## Procedure
- [ ] Workflow is executable from the written instructions.
- [ ] Required reads/scripts are explicit.
- [ ] Failure behavior is explicit where needed.

## Output and validation
- [ ] Output contract is named.
- [ ] Completion gates are named.
- [ ] Machine-checkable validation is executable when warranted.
- [ ] Representative success and misuse cases have been tested.

## Lifecycle
- [ ] Provenance/source lineage is recorded.
- [ ] Supersession is recorded when applicable.
