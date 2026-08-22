from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    "README.md",
    "REVIEW.md",
    "CLAIMS.md",
    "ARTIFACT_MANIFEST.md",
    "CLOSURE_CERTIFICATE.md",
    "Audit/flagship-theorems.txt",
    "Audit/AxiomAudit.lean",
    "sympy/claim_check.py",
    "notebooks/01_claim_check.ipynb",
]

for rel in TARGETS:
    path = ROOT / rel
    if not path.exists():
        print(f"MISSING  {rel}")
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"{digest}  {rel}")
