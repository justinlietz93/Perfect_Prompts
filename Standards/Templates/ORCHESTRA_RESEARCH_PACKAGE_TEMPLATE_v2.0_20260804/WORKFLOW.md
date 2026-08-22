# Orchestra Research Package Workflow

## Role and version law

- Operator work occurs inside the active version.
- Guardian PASS or FAIL is written into the same version and never advances `v#`.
- Auditor PASS or FAIL closes the adjudication and advances the next package version.
- A successor records the parent package ID and parent manifest SHA-256.
- Reviewers do not silently rewrite the evidence they adjudicate.

## Terminal rule

The branch remains active until its declared terminal condition is met. Intermediate repairs, infrastructure work, negative controls, and partial lemmas are not terminal unless explicitly declared so.

Normal terminal outcomes are:

- a nontrivial positive internally generated result;
- a proof that the branch hypothesis is false;
- an exact external dependency that makes further work impossible, recorded as `BLOCKED`, not `PASS`.

## Evidence classes

- `RULE`
- `CURRENT-CANON RESULT`
- `RECOVERED`
- `PROVISIONAL`
- `CONDITIONAL DOWNSTREAM`

## Working statuses

- `UNTESTED`
- `IN_PROGRESS`
- `PASS`
- `FAIL`
- `BLOCKED`
- `SUPERSEDED`
- `NOT_APPLICABLE`

`NOT_APPLICABLE` requires a scientific reason.

## Closure

1. Remove all active placeholder markers.
2. Confirm every claim has a burden, falsifier, and exact artifact references.
3. Confirm each notebook satisfies the no-I/O, one-cell-per-claim contract.
4. Confirm each decision figure also exists in top-level `figures/`.
5. Run `tools/finalize_package.py`.
6. Preserve the ZIP and external `.sha256` together.
7. Never alter a closed ZIP; create a successor version.
