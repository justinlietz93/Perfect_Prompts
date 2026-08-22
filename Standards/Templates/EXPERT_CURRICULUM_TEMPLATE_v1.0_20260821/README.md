# Expert Curriculum Template

Version 1.0  
Built 21 August 2026

This package is a reusable architecture for building a serious, dependency-aware curriculum around a defined capability goal, research program, professional domain, or body of knowledge.

It is derived from the working architecture of the Phase Calculus / VDM curriculum. The template preserves the useful invariants of that system without assuming mathematics, physics, Brilliant, Phase Calculus, VDM, or any particular subject.

## Core design rule

A curriculum is not a reading list.

It must define:

1. the target capability;
2. the dependency graph;
3. the order that controls progression;
4. exact start gates for material that can run in parallel;
5. what counts as a core pass versus deepening, reference, or optional material;
6. observable exit gates that establish readiness to advance;
7. how gaps are diagnosed and repaired;
8. how current projects or research can activate targeted learning without silently rewriting the prerequisite structure;
9. how independent work, proof, derivation, implementation, experiment, or other domain-appropriate reconstruction establishes command;
10. how progress and transfer are recorded.

## What this template prevents

- multiple contradictory study orders;
- treating acquisition order as a separate curriculum;
- reading every resource linearly because it is present;
- forcing already-mastered elementary material;
- using passive exposure as evidence of mastery;
- allowing advanced branches to import prerequisites that have not been earned;
- turning every missing prerequisite into a demand to complete an entire course before returning to the active problem;
- letting research/application urgency silently erase prerequisite dependencies;
- letting temporary current work redefine the durable curriculum spine;
- mixing generated work products into the source-resource library.

## Instantiate in this order

1. Fill `CURRICULUM_SPEC.json` from `examples/CURRICULUM_SPEC.example.json`.
2. Define the target and mastery model in `AUTHORITY.md`.
3. Write the actual dependency graph in `00_MASTER_ROADMAP/DEPENDENCY_GRAPH.md`.
4. Write the controlling order and gates in `00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md`.
5. Build the resource inventory and acquisition queue from that same order.
6. Create one group folder per curriculum group using `_GROUP_TEMPLATE/`.
7. Define a capability-based exit gate for every core group.
8. Add current-work/research alignment only after the durable curriculum exists.
9. Run `python tools/validate_curriculum.py .`.
10. Hash the package with `python tools/build_manifest.py .`.

## Canonical precedence inside an instantiated curriculum

1. `AUTHORITY.md`
2. `CURRICULUM_SPEC.json`
3. `00_MASTER_ROADMAP/STRICT_ORDER_AND_START_GATES.md`
4. the numbered order inside each group `README.md`
5. group `PROGRESS.md` files
6. current-work alignment files

Current-work files can activate or prioritize learning. They do not silently rewrite the durable prerequisite graph.
