# Research & Evidence Standard v1.0.1

This package contains the first consolidated research-level standard synthesized from the existing user-supplied `Standards.zip`, `Templates.zip`, and aligned Phase Calculus / VDM curriculum research-method rules.

## Files

- `RESEARCH_AND_EVIDENCE_STANDARD_v1.0.1_20260821.md` — canonical-source candidate in Markdown.
- `RESEARCH_AND_EVIDENCE_STANDARD_v1.0.1_20260821.docx` — formatted human-readable rendition of the same standard.
- `SOURCE_MAP.md` — rule lineage, source roles, conflict handling, and precedence decisions.
- `CHANGELOG.md` — version history.
- `MANIFEST.json` — generated file inventory with SHA-256 hashes.
- `SHA256SUMS` — checksum list corresponding to the manifest.

## Authority

The standard deliberately labels itself **WORKING STANDARD — candidate for canonical adoption**. It does not self-promote above the source standards or templates. Explicit adoption into the user's standards library is required for canonical authority.

## Important preserved distinction

The existing Orchestra research package template is treated as a concrete implementation of the standard, not replaced by it. Where a template validator contradicts the clarified semantic intent, the contradiction is recorded as an implementation defect rather than promoted into a new standard. The publication package remains a stronger downstream release gate.

## Notebook model

Each paper's notebook is a reviewer-facing “tutorial island”: it follows the paper's claims in presentation order, explains each one in prose, then demonstrates the claim with well-commented executable evidence, readable text/numeric outputs, figures, and explicit links to companion Lean 4, SymPy, data, source-code, or other evidence artifacts.
