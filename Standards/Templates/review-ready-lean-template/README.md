# ReviewReadyTemplate

A reviewer-grade Lean 4 package template.

This template is meant for projects that want skeptical reviewers to answer, quickly and independently:

- What does this package claim?
- What exactly is proved?
- What is trusted?
- How do I reproduce it?
- Where would it fail if the claim were wrong?

## What is included

- A real Lake package with pinned `lean-toolchain` and checked-in `lake-manifest.json`
- A theorem-bearing library with module docs and declaration docs
- A test library wired into `lake test`
- A lightweight `lake lint` driver for placeholder and repository-hygiene checks
- Reviewer-facing files: `REVIEW.md`, `CLAIMS.md`, `ARTIFACT_MANIFEST.md`, `CLOSURE_CERTIFICATE.md`
- Axioms audit scaffolding in `Audit/`
- A nested `docbuild/` project for `doc-gen4`
- GitHub Actions workflows for CI and scheduled `lean4checker`
- Companion `sympy/` and `notebooks/` scaffolding for non-Lean validation layers

## Trust boundary

Inside Lean:

- the theorem statements in `ReviewReadyTemplate/*.lean`
- the proofs accepted by Lean during `lake build`
- the axiom dependencies printed by `#print axioms`
- the replay checks run by `lake exe lean4checker --fresh ...`

Outside Lean:

- Markdown manifests and closure certificates
- CI wiring and shell/Python scripts
- SymPy and notebook companions

Treat the outside-Lean layers as reviewer aids, not theorem-bearing evidence.

## Quick start

```bash
lake build
lake test
lake lint
bash scripts/audit_axioms.sh
lake exe lean4checker --fresh ReviewReadyTemplate
```

## Documentation build

```bash
bash scripts/build_docs.sh
```

The generated site is written to:

```text
docbuild/.lake/build/doc/index.html
```

## Where the sample theorems live

- Root import surface: `ReviewReadyTemplate.lean`
- Main theorem-bearing module: `ReviewReadyTemplate/Basic.lean`
- Test mirror: `ReviewReadyTemplateTest/Smoke.lean`
- Reviewer-facing theorem index: `docs/TheoremIndex.md`
- Flagship page example: `docs/flagship/add_zero_right.md`

## For mathlib-based projects

This template is intentionally dependency-light. If your project adds `mathlib`, pin it in `lakefile.lean`, run `lake update`, commit the new `lake-manifest.json`, and run `lake exe cache get` before the first full build after adding or updating `mathlib`.

## Rename checklist

Before first real use, rename:

- package name in `lakefile.lean`
- root library file and directory
- theorem names, claims table, and closure certificate rows
- homepage, authorship, and license fields
