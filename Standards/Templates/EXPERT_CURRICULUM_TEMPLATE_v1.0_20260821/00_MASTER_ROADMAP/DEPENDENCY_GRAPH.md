# Dependency Graph

## Ultimate target

`{{CAPABILITY_TARGET}}`

## Primary spine

Record the durable dependency chain here before assigning resources.

| Group | Capability supplied | Why downstream work depends on it | Exit evidence |
|---|---|---|---|
| `01` | `{{FOUNDATIONAL_CAPABILITY}}` | `{{DEPENDENCY_REASON}}` | `{{EXIT_EVIDENCE}}` |

## Parallel branches

| Branch | Depends on | Why the gate exists | Can targeted activation occur? |
|---|---|---|---|
| `{{BRANCH_ID}}` | `{{DEPENDENCIES}}` | `{{REASON}}` | yes / no |

## Dependency-debt rule

If targeted work crosses the systematic order, record:

- the advanced object being used;
- which prerequisites are already usable;
- which prerequisite is missing;
- what exact repair is performed;
- what remains unearned;
- what claims are therefore still out of scope.

Do not convert targeted exposure into silent prerequisite completion.
