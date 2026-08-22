# Flagship theorem: `ReviewReadyTemplate.add_zero_right`

## Informal statement

For every natural number `n`, adding zero on the right does not change `n`.

## Exact Lean statement

```lean
theorem ReviewReadyTemplate.add_zero_right (n : Nat) : n + 0 = n
```

## Module path

`ReviewReadyTemplate.Basic`

## Supporting declarations

- `Nat.add_zero`

## Axiom audit

Run:

```bash
bash scripts/audit_axioms.sh
```

Then inspect `Audit/axioms-report.txt` for the line corresponding to
`ReviewReadyTemplate.add_zero_right`.

## Checker replay

```bash
lake exe lean4checker --fresh ReviewReadyTemplate
```

## Notes for adaptation

Replace this page with a real flagship theorem page for each load-bearing theorem in your
package.
