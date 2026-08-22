# Publication Package Requirements

## Governing principle

The paper is the load-bearing source. Formal, symbolic, numerical, and figure artifacts attack its claims and make them reproducible; they do not hide missing derivations.

## Claim requirements

Every primary claim must have:

- stable ID;
- exact statement;
- paper location;
- assumptions;
- scope;
- decisive metric or proof condition;
- falsifier;
- required burden classification;
- supporting and contradicting artifacts;
- current status.

## Burden classes

- **Formal:** theorem-shape statements, exact equivalences, implication chains, closures, impossibility results, and normal forms.
- **Symbolic:** algebraic, differential, projection, bracket, duality, tensor, and operator identities.
- **Numerical:** simulation, robustness, convergence, statistical, geometric, and thresholded computational claims.
- **Figure:** reviewer-facing visual evidence or exact explanatory geometry.

Do not force a cosmetic tool artifact where no burden exists. Use `NOT_APPLICABLE` with a scientific reason.

## Notebook contract

- no file I/O;
- no network access;
- no infrastructure-only cells;
- one claim or proof unit per code cell;
- declared threshold;
- negative control;
- numeric results;
- at least one rendered decision figure;
- explicit PASS or FAIL;
- matching individual figure archived in top-level `figures/`.

## Figure standard

Figures must be publication-legible and mathematically meaningful. Avoid default plots, unreadable labels, overlapping annotations, decorative boxes, and abstract imagery that conceals the claim.

## Closure

A draft can close with open claims only when those claims are explicit throughout the paper and release records. A preprint or final release cannot close while a required burden for a primary claim is missing or failed.
