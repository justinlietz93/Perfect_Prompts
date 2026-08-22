# Notebooks

Notebooks are claim-level reviewer artifacts, not scratchpads.

- No file I/O in notebook runtime.
- One executable cell per claim or proof unit.
- Every claim cell declares thresholds and a negative control.
- Every claim cell prints numeric results and explicit PASS/FAIL.
- Every claim cell displays at least one decision figure.
- Infrastructure-only cells are prohibited.
- The same figures must be exported separately into top-level `figures/` by code outside the notebook.
- Avoid large embedded HTML and excessive outputs.

Create a neutral shell with:

```bash
python tools/new_claim_notebook.py --claim-id C001 --title "..." --output notebooks/C001.ipynb
```

The shell intentionally fails strict validation until implemented and executed.
