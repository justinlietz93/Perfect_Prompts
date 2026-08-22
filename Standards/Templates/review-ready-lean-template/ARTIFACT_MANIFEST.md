# Artifact manifest

Regenerate hashes with:

```bash
python scripts/recompute_sha256.py
```

| Artifact | Path | SHA256 | Notes |
|---|---|---|---|
| Package README | `README.md` | `cfd576bd347701cd1ec68b59a10e096240f1e37e6c71c54c5c81005605576eb6` | Reviewer landing page |
| Review protocol | `REVIEW.md` | `4219b74ed75caa2e071b4ed1d503a2d68b87b6793dae84b096d12a69b59b2bd8` | Fresh-clone audit steps |
| Claims register | `CLAIMS.md` | `2b74ceca1eecd2c0918e0fba1be7e9d384bfc0b12a40c3cc68747df659d7d845` | Informal-to-formal mapping |
| Closure certificate | `CLOSURE_CERTIFICATE.md` | `df277e374ae84dc7fbb51684293c70152322ecceb3fa4cee7ac7d865f9e670e0` | Final claim disposition |
| Flagship theorem list | `Audit/flagship-theorems.txt` | `2a1adc653069ef5463bb2ce926d89a012656fae43e8f7f4213000ae1063a1d1f` | Inputs to axiom audit |
| Axiom audit entry file | `Audit/AxiomAudit.lean` | `637a195c0e9160a7e8c93447a4513ef4d56022641996761a147e5a4c2f3195f6` | Non-module `#print axioms` file |
| SymPy companion | `sympy/claim_check.py` | `932557f921d7127451b4ba704822b9031602766a6409ec5a385ab2a54d2e84a6` | Symbolic companion layer |
| Notebook companion | `notebooks/01_claim_check.ipynb` | `3d39432df8a4419daf17f5ba3e2f9274edbb8688ac5e252117c27e3d5c04a0cc` | Executable notebook layer |
