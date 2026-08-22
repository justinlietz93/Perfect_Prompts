# Instantiation Guide

## Phase 1 — Define the object before filling folders

Write one sentence that states the actual capability target. If the target is vague, the curriculum will become a pile of respectable resources.

Then identify:

- primitive knowledge / skills;
- load-bearing dependencies;
- capabilities that can develop in parallel;
- specialist branches that should remain dormant until needed;
- what evidence would convince you that each group is usable.

## Phase 2 — Build the dependency graph

Create the graph before choosing the final reading order.

For every edge `A → B`, be able to answer:

> What specifically becomes unreliable in B if A is missing?

Delete dependencies that exist only because conventional university sequences happen to place one course earlier.

Add dependencies when a downstream object genuinely presupposes notation, proof language, physical intuition, implementation skill, or another capability.

## Phase 3 — Create the primary spine

The primary spine should contain the smallest ordered set that supplies the general capabilities required by the target.

Avoid turning every interesting subject into the spine.

## Phase 4 — Add branches

A branch is appropriate when:

- it has its own prerequisite gate;
- it can run alongside later spine work;
- it serves a specialized application or research target;
- forcing it into the main sequence would needlessly serialize the curriculum.

## Phase 5 — Assign resource roles

For every resource, state its job. Good curricula often use different resources for intuition, first formal exposure, exercises, proof depth, visualization, historical context, and reference.

Do not make a resource core merely because it is famous or difficult.

## Phase 6 — Write exit gates

A strong exit gate is capability-based.

Weak:

- finish chapters 1–8;
- watch all lectures;
- spend 30 hours;
- complete a platform level.

Strong:

- derive the governing equations from stated assumptions;
- solve representative problems without hints;
- implement the method from the mathematical description;
- distinguish three commonly conflated structures;
- explain where a theorem fails when a hypothesis is removed;
- complete a research-grade concept-transfer record.

## Phase 7 — Add the diagnostic layer

Use diagnostics to skip what is already usable and expose the exact point at which command breaks.

The diagnostic layer should accelerate the curriculum, not become a second curriculum.

## Phase 8 — Align to current work

Only after the durable structure exists, map current research/projects onto the curriculum.

This preserves a crucial distinction:

- **curriculum dependency:** what must eventually be learned for durable command;
- **current priority:** what is most useful to open now.

## Phase 9 — Validate

Run:

```bash
python tools/validate_curriculum.py .
python tools/build_manifest.py .
```

Do not call the curriculum coherent while the validator reports structural errors or the human-readable order disagrees with `CURRICULUM_SPEC.json`.
