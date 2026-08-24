# Source Map

## Primary sources

- `Standards/apex_software_standards/APEX_STANDARDS.md` - architecture from requirements, modularity, configuration discipline, test/verification, implementation correctness, <=500 LLOC policy.
- `Standards/nasa_software_standards/` - requirements traceability, architecture/design, testing, final validation, safety/complexity concepts where applicable.
- `Standards/architecture_standards/EMERGENCE_BASED_ARCHITECTURE.md` - source preservation, invariants before mechanisms, admission by evidence, native vocabulary, dependency direction, boundary isolation.
- Other `Standards/architecture_standards/*` - evidence that architecture patterns are selectable task/domain fits rather than one universal architecture.
- Perfect Prompts `Methodologies/Germinal_Theory/Emergence_Based_Design_AGENTS.md` - observe before changing, preserve lineage, friction as evidence, external systems as boundaries, repair before replacement.
- Cross-project engineering history - architecture drift, duplicate capability, hardcoded configuration, locality/performance regressions, stale integration tests, transitional-state confusion.

## Explicit non-promotions

- Safety-critical static-memory/loop rules are not imposed on ordinary software unless the project requires them.
- VDM-specific sparse/no-global-scan rules are generalized as respect for declared complexity/locality invariants.
- No single architecture pattern is promoted as default.
