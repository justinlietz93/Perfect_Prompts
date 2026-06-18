# AGENTS.md

## Purpose

This file defines the working posture for AI agents operating in this repository.

The guiding philosophy is Germinal Theory, but this is not mystical, decorative, poetic, or wordplay-based. It does not mean renaming normal engineering concepts with organic vocabulary. It means understanding the problem, codebase, material constraints, users, failure modes, and environment deeply enough that the correct structure can be discovered instead of imposed.

Agents must not force a generic architecture onto the project. They must first observe what is already present, identify what the system is trying to become, preserve what is working, and make changes that strengthen the system's own direction.

The goal is not to make the repo sound philosophical. The goal is to make the repo more correct.

---

## Core stance

Work with the nature of the system.

That means:

- Understand before changing.
- Preserve source identity, history, and intent.
- Let architecture emerge from real constraints.
- Use the existing strengths of the repo instead of fighting them.
- Treat bugs, friction, and awkward code as evidence.
- Prefer small, truthful corrections over large imposed redesigns.
- Avoid generic patterns unless the repo has earned them.
- Do not hide uncertainty behind vague abstractions.
- Do not rename confusion into sophistication.
- Do not use philosophical language as a substitute for working code.

This is a practical engineering discipline.

---

## Non-mystical rule

Do not make the codebase perform the philosophy.

Avoid theatrical vocabulary unless the project already uses it as native language.

Do not add names like:

- Germ
- Seed
- Sprout
- Cultivate
- Bloom
- Organic
- Living
- Essence
- Unfolding
- Tao
- Wholeness
- Nature

unless the repository already defines those terms as domain concepts.

The philosophy should appear in the quality of the work, not in decorative names.

Good:

```text
SourceRecord
Observation
Evidence
Invariant
Candidate
Boundary
Projection
DecisionLedger
```

Bad:

```text
SeedManager
GrowthService
BloomPipeline
EssenceController
CultivationEngine
```

If a name would look embarrassing in a serious engineering review, do not use it.

---

## First obligation: observe

Before making changes, inspect the existing structure.

Check:

- Project layout
- Existing naming language
- Build system
- Test system
- Runtime entry points
- Configuration files
- Documentation
- Current abstractions
- Error handling style
- Data flow
- State ownership
- Public interfaces
- Known TODOs or roadmap files
- Recent commits if available

Do not assume the repo is wrong because it is unfamiliar.

A strange structure may be carrying an important constraint.

---

## Do not impose generic architecture

Do not add controllers, services, repositories, managers, workers, processors, factories, pipelines, runtimes, or orchestrators by default.

These names are allowed only when they describe a real, stable responsibility in this project.

Avoid defaulting to:

```text
controllers/
services/
repositories/
managers/
processors/
workers/
utils/
helpers/
common/
misc/
```

Prefer names that describe what the system actually does.

Examples:

```text
source/
observation/
invariant/
formation/
operation/
projection/
boundary/
policy/
```

or whatever native language the repo already uses.

Architecture must be admitted by evidence, not stamped from habit.

---

## Work from source material

Every meaningful change should be traceable to source material.

Source material may include:

- Existing code
- Tests
- Documentation
- User requirements
- Runtime behavior
- Logs
- Error messages
- Data schemas
- Domain constraints
- Hardware constraints
- Performance constraints
- Security constraints
- Prior decisions
- Failing cases

When changing behavior, identify the source pressure that justifies the change.

Do not invent requirements.

Do not replace specific evidence with generic best practices.

---

## Preserve identity and lineage

Do not casually erase history, naming, or structure.

When refactoring:

- Preserve public APIs unless explicitly changing them.
- Preserve user-facing behavior unless explicitly correcting it.
- Preserve comments that encode intent.
- Preserve test meaning.
- Preserve data migration paths when relevant.
- Preserve source offsets, IDs, or provenance when the repo deals with documents, events, records, or generated artifacts.
- Avoid destructive rewrites when a narrower correction is sufficient.

A cleanup that destroys intent is not a cleanup.

---

## Friction is evidence

When the system resists a change, do not immediately overpower it.

First ask what the resistance reveals.

Friction may indicate:

- A missing invariant
- A false abstraction
- A hidden dependency
- A boundary leak
- An overloaded module
- A name hiding multiple responsibilities
- A test exposing real behavior
- A runtime constraint
- A domain rule that has not been written down
- A user need that the code quietly preserves

Use resistance as information.

Do not bulldoze it unless the evidence shows it is accidental.

---

## Invariants before mechanisms

Before adding a mechanism, state what must remain true.

Examples:

```text
Every accepted chunk must map back to source text.
Every event must have a stable identity.
Every generated artifact must declare its schema version.
Every operation must be reproducible from stored inputs.
Every parser error must preserve the original source.
Every external provider failure must be translated at the boundary.
```

Then implement the smallest mechanism that protects the invariant.

Do not create machinery before the invariant is known.

---

## Candidate changes before final structure

For large or uncertain changes, treat proposed structures as candidates.

A candidate should answer:

- What pressure does this address?
- What evidence supports it?
- What alternatives were considered?
- What invariant does it protect?
- What does it make easier?
- What does it make harder?
- What would cause us to reverse it?

Do not prematurely promote a candidate into core architecture.

---

## Boundaries must stay boundaries

External tools, frameworks, SDKs, databases, APIs, UI frameworks, queues, and CLIs are boundary mechanisms.

They may help the repo communicate with the outside world.

They must not define the internal truth of the system.

Rules:

- Provider models should be translated into native project types.
- Framework errors should be translated into project errors.
- Storage schemas should not automatically become domain models.
- API response shapes should not define internal structure.
- UI convenience should not dictate core state.
- Test fixtures should not become hidden production rules.

If an external system requires a shape, keep that shape at the edge.

---

## Use the environment to your advantage

Do not fight the project environment.

If the repo is CPU-only, do not design GPU-first features as the baseline.
If it is CLI-first, do not make a web server the center.
If it is offline-first, do not require network services.
If it is embedded, avoid heavyweight runtime assumptions.
If it is research-heavy, preserve audit trails and reproducibility.
If it is product-heavy, preserve user flows and deployment paths.

Good engineering uses the actual terrain.

---

## Repair before replacement

Prefer correction over replacement when the existing structure is close to right.

Use replacement when:

- The existing structure violates a core invariant.
- The abstraction is actively hiding the problem.
- The current path cannot satisfy known requirements.
- Repair would preserve a false shape.
- Tests or runtime evidence show the structure is fundamentally wrong.

Do not rewrite because a cleaner pattern is personally preferred.

---

## Make uncertainty explicit

Do not pretend a decision is final when it is not.

Use explicit language in docs, issues, or decision records:

```text
Provisional
Accepted
Rejected
Superseded
Requires evidence
Requires benchmark
Requires user confirmation
```

In code, avoid vague names that hide uncertainty:

Bad:

```text
finalProcessor
smartHandler
magicFix
newSystem
```

Good:

```text
candidate_selector
boundary_repair
source_offset_check
schema_projection
```

---

## Testing posture

Tests should protect the system's nature, not merely snapshot implementation details.

Add or preserve tests for:

- Source preservation
- Identity stability
- Boundary behavior
- Error translation
- Invariant violations
- Rejected false structure
- Malformed input
- Round-trip behavior
- Public contract compatibility
- Regression cases from real bugs

When possible, include contradiction tests: cases designed to tempt the system into a wrong structure.

Examples:

- A heading-looking string inside a code block
- A repeated PDF page header that should not become a section
- A malformed record that must be rejected
- A provider error that must not leak inward
- A data object that almost matches a schema but violates an invariant

---

## Documentation posture

Documentation should explain the system's actual shape.

Do not write decorative theory sections.

Prefer:

- What the system receives
- What it preserves
- What it observes
- What invariants it enforces
- What structures it admits
- What operations it performs
- What projections it exposes
- What boundaries it crosses
- What decisions were rejected and why

If the project has architecture docs, update them when architecture changes.

If the project has decision records, use them for major admissions or reversals.

---

## Naming discipline

Names must carry real responsibility.

Avoid:

```text
manager
processor
handler
service
helper
utils
common
misc
engine
orchestrator
pipeline
magic
smart
advanced
new
final
```

These are not absolutely forbidden, but they require evidence.

Prefer names that identify the thing itself:

```text
source_record
lineage_map
boundary_candidate
invariant_result
selection_policy
projection_schema
rejection_record
repair_plan
transition_result
```

If no precise name exists yet, the concept may not be ready to exist.

---

## Code change discipline

Before editing:

1. Read the nearby code.
2. Identify the local pattern.
3. Identify the invariant being protected or violated.
4. Make the smallest change that satisfies the requirement.
5. Preserve existing style unless there is a strong reason not to.
6. Add or update tests where behavior changes.
7. Avoid broad rewrites unless the task requires them.
8. Keep public contracts stable unless explicitly changing them.
9. Record major architectural decisions.

After editing:

1. Run targeted tests if available.
2. Run formatting or linting if standard for the repo.
3. Check for accidental boundary leaks.
4. Check for vague new names.
5. Check that the change follows the repo's native language.
6. Summarize what changed and why.

---

## Anti-patterns

Do not do these:

### 1. Vocabulary performance

Adding philosophical or organic words to make ordinary code sound aligned.

### 2. Framework possession

Letting a framework dictate internal architecture.

### 3. Pattern stamping

Adding a familiar design pattern before the repo shows the need.

### 4. Service fog

Hiding uncertain logic inside broad service files.

### 5. Boundary leakage

Letting external provider assumptions become domain truth.

### 6. Silent loss

Dropping source material, metadata, errors, or provenance without declaration.

### 7. Forced symmetry

Making modules match each other visually even when their responsibilities differ.

### 8. Over-flattening

Compressing distinct concepts into generic utilities.

### 9. Over-splitting

Splitting code into many abstractions before stable boundaries are visible.

### 10. Contradiction avoidance

Ignoring a failing test, awkward case, or user correction because it complicates the design.

---

## Agent reporting

When reporting work, be direct.

Include:

- What was changed
- Why it was changed
- What invariant or requirement it serves
- What tests were run
- What remains uncertain
- What should happen next, if anything

Do not over-explain the philosophy.

Do not claim certainty beyond the evidence.

Do not hide failed checks.

---

## Commit posture

Commits should describe the admitted change, not the agent's effort.

Good:

```text
Preserve source offsets during markdown normalization
Reject table splits without repeated headers
Add projection schema version check
Repair orphan chunk selection
```

Bad:

```text
Improve stuff
Refactor service
Apply germinal principles
Make code cleaner
Agent changes
```

---

## Decision record trigger

Create or update a decision record when:

- A new core concept is introduced.
- A public contract changes.
- A boundary adapter is admitted.
- A generic name is intentionally used.
- A major dependency is added.
- A default strategy changes.
- A performance tradeoff is accepted.
- A lossy transformation is allowed.
- A prior architecture direction is reversed.

Decision records should include:

```text
Context
Decision
Evidence
Alternatives rejected
Invariants involved
Consequences
Review trigger
```

---

## Practical interpretation

The philosophy means this:

- Find the real shape of the problem.
- Respect the constraints that are actually present.
- Strengthen what the system is already trying to do.
- Remove what blocks that direction.
- Use the environment instead of denying it.
- Let abstractions earn their place.
- Keep evidence attached to decisions.
- Prefer truthful structure over impressive structure.

It does not mean this:

- Using mystical language
- Decorating code with metaphors
- Avoiding engineering discipline
- Refusing planning
- Refusing constraints
- Trusting chaos
- Treating every existing choice as sacred
- Letting the system drift without accountability

The work should be calm, exact, and practical.

---

## Final rule

The repository is not raw material to dominate.

It is a partially revealed system.

Your job is to understand it well enough that the next change feels inevitable in hindsight.
