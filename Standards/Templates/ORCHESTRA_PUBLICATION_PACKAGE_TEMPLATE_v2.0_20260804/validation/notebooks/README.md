# Reviewer Notebooks

Generate a claim notebook with:

```bash
python tools/new_claim_notebook.py --claim-id C001 --output validation/notebooks/C001_audit.ipynb
```

Strict notebook contract:

- no markdown or infrastructure-only cells;
- one executable code cell per claim or proof unit;
- no file I/O;
- declared numeric threshold;
- explicit negative control;
- numeric results;
- at least one rendered decision figure;
- explicit PASS or FAIL in output;
- individual matching figure archived in top-level `figures/` by an external deterministic packaging script.
