# Changelog

## v1.0.0 — 2026-08-22

Initial canonical-candidate release.

Built from a holistic audit of the supplied Perfect Prompts repository, with emphasis on the `skills/` stratum and its surrounding composition layers.

Key decisions:

- defined a skill as a procedural package rather than a long prompt;
- separated skill standards from prompt-template standards;
- required explicit activation, package anatomy, procedure, output, and validation contracts;
- treated runtime wrappers as secondary to inspectable canonical source;
- preserved heterogeneity of internal skill workflows.
