# Publication Release Workflow

## Authority and immutability

The publication package is a frozen projection of accepted research evidence. It does not acquire authority by silently copying files. Authority comes from explicit claim migration, exact source package IDs, source manifest hashes, and identified review verdicts.

## Draft release

A draft release may preserve unresolved, blocked, or failed claims only when:

- the manuscript says so;
- the claim ledger says so;
- the coverage map says so;
- the closure certificate lists the open items;
- metadata never labels the release `VALIDATED`.

## Preprint release

A preprint release requires:

- every primary claim has passed every required burden;
- every `NOT_APPLICABLE` burden has a scientific reason;
- all paper figures are archived individually;
- the paper compiles from clean staged source;
- arXiv source passes the same compile test;
- manifest and checksums describe the final bytes exactly;
- the closure certificate is complete.

## Version law

- Never alter a closed release ZIP.
- Metadata-only repository edits do not alter the package bytes.
- Changed files require a new publication package version.
- The new version records the superseded publication ID and prior release SHA-256.

## DOI timing

Keep DOI fields empty until a DOI exists or has been reserved for the exact release. Insert the reserved DOI into metadata and the manuscript before final compilation. Never retain a DOI copied from another publication or from this template's history.
