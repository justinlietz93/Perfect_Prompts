# Orchestra Publication Package Template v2.0

This is the canonical seed for one **reader-facing, immutable publication release** derived from accepted Orchestra research evidence.

It is not a research workbench. Iteration, role adjudication, branch exploration, and mutable evidence belong in `p#-b#-v#` research packages. This package freezes selected accepted claims, the exact paper, validation coverage, provenance, arXiv source, and Zenodo release bytes.

## Core distinction

```text
accepted Orchestra research package(s)
                  ↓
claim and artifact selection
                  ↓
publication-specific proof and validation
                  ↓
compiled paper + clean arXiv source
                  ↓
immutable Zenodo release package
```

A publication package must identify every source research package by package ID and exact manifest SHA-256. Publication acceptance does not rewrite the upstream research record.

## Create an active publication package

```bash
python tools/init_publication.py \
  --title "Paper title" \
  --short-title "Short title" \
  --slug paper-slug \
  --version 1.0.0 \
  --release-level draft \
  --license cc-by-4.0 \
  --source-package-id p5-b3-v19 \
  --source-manifest-sha256 <64-hex-sha256> \
  --output /path/to/publications
```

The initializer creates a new directory. Do not rename this template manually and treat it as active.

## Publication workflow

1. Record exact source packages and accepted claim mappings in `SOURCE_RESEARCH_LINEAGE.json`.
2. State every primary claim in `claims/claims.json` and `claims/CLAIM_LEDGER.md`.
3. State assumptions and non-claims before writing the conclusions.
4. Write the paper in `paper-source/`; keep the full load-bearing argument in the manuscript.
5. Put publication figures in top-level `figures/` and explicitly list paper figures in `paper-source/ARXIV_FIGURES.txt`.
6. Map each claim burden to exact proof, symbolic, numerical, and figure artifacts in `validation/coverage.json`.
7. Use `NOT_APPLICABLE` only with an exact scientific reason.
8. Compile with `python tools/compile_paper.py .`.
9. Close the release honestly in `CLOSURE_CERTIFICATE.md`.
10. Freeze with `python tools/finalize_publication.py .`.

## Release levels

- `draft`: may contain unresolved or failed claims, but they must remain explicit in the paper, ledgers, coverage map, and closure certificate.
- `preprint`: every primary claim must pass every required burden; exclusions require reasons.
- `final`: same validation rule as preprint, plus final publication metadata and identifiers.

## Non-negotiable rules

- No historical experiment content in the template.
- No fake `.csv`, `.db`, `.h5`, `.json`, `.ipynb`, proof, result, or figure placeholders.
- No handwritten final manifest or checksum file.
- The paper carries the full formal burden; companion artifacts attack it rather than substitute for it.
- Every primary claim has a stable ID, exact statement, falsifier, scope, burden map, and paper location.
- Notebook runtime performs no file I/O.
- Each notebook code cell attacks one claim and emits numeric results, a declared threshold, a negative control, a decision figure, and explicit PASS/FAIL.
- Notebook figures do not replace files in top-level `figures/`.
- arXiv source contains only compilation inputs selected by the package.
- A closed release is never edited in place. Create a new publication version.

## Validate

Template structure:

```bash
python tools/validate_publication.py .
```

Active release closure:

```bash
python tools/validate_publication.py . --strict
```
