# Validation Bundle

Companion validation attacks the claims in the paper. It does not replace derivations that belong in the manuscript.

- `formal/`: exact theorem formalization, normally Lean4 when appropriate.
- `symbolic/`: exact algebraic and operator audits, normally SymPy when appropriate.
- `notebooks/`: reviewer-facing numerical and geometric attacks.
- `reports/`: executed summaries, tool versions, command logs, and validation inventories.
- `coverage.json`: machine-readable burden closure.

Do not create cosmetic artifacts for burdens that do not exist. Mark the burden `NOT_APPLICABLE` with an exact reason.
