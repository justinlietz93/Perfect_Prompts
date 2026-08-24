# Research & Evidence Standard v1.0.1 — Source Map

This source map records where the v1.0.1 standard came from and the interpretation decisions made during synthesis. It is not a replacement for the original files.

| Standard area | Primary source(s) | Treatment in v1.0.1 |
|---|---|---|
| Curiosity-first research posture | `Standards.zip/curiosity_first_research_note.txt`; `unified_publication_requirements_v3.md §0` | Generalized from publication work to all research. Rigor is treated as completed curiosity rather than an opposing posture. |
| Package identity, branch question, terminal condition | Orchestra research template `README.md`, `PACKAGE.json`, `WORKFLOW.md` | Preserved as the core package discipline. |
| Semantic authority and exclusions | Orchestra `AUTHORITY.md`, `PACKAGE.json` | Promoted to a general custody/source-control requirement. |
| Stable claims, burden, falsifier, artifact links | Orchestra `CLAIMS.md`, claim schema; publication claim ledger | Preserved and expanded with hypotheses, quantifiers, scope, and information-loss risks. |
| Evidence/status ontology | Orchestra `WORKFLOW.md`, claim schema | Preserved. |
| Assumptions and nonclaims | Publication `ASSUMPTION_LEDGER.md`, `NONCLAIMS.md`; reviewer checklist | Preserved, while preventing generic nonclaim hedging from becoming paper clutter. |
| Formal/symbolic/numerical burden split | Unified publication requirements; publication requirements; curriculum research methods | Generalized to research packages and supplemented with architectural, empirical, figure, and historical burdens. |
| Negative controls, thresholds, PASS/FAIL | Orchestra notebook contract; unified publication requirements; curriculum computational experiment standard | Preserved as decisive computational-evidence rules. |
| Notebook executable-cell discipline | Orchestra `notebooks/README.md`; `tools/new_claim_notebook.py`; computational experiment standards | Preserved for executable claim demonstrations: no hidden I/O, explicit decision evidence, controls, figures, and scoped verdicts. |
| Reviewer-facing notebook narrative | User clarification of intended “tutorial island” design + `CRAFT_BASS_Review_Standards_v3.md` + Orchestra `notebooks/README.md` | Promoted to the semantic notebook contract: each paper receives a guided, sequential tutorial notebook with explanatory Markdown, readable outputs, figures, and well-commented executable evidence. |
| Orchestra Markdown rejection | `tools/validate_package.py` | Classified as an implementation defect/drifted validator constraint because it contradicts the intended reviewer-facing notebook contract. It must be repaired rather than used to strip prose. |
| Formal verification | Orchestra `lean/README.md`; `Lean4_Workflow.md`; unified publication requirements | Preserved with an added faithfulness rule: a clean proof only establishes the encoded theorem surface. |
| Figures | Unified publication requirements; figure standards; reviewer checklist | Consolidated into one-message, anti-deception, reproducibility, and epistemic-fidelity requirements. |
| Findings and lab history | Orchestra `FINDINGS.md`, `LAB_JOURNAL.md` | Preserved; negative/unresolved results stay visible and journal history is append-only. |
| Review custody and version law | Orchestra `WORKFLOW.md`, Guardian/Auditor templates | Preserved as the current implementation, generalized to a custody-separation principle. |
| CRAFT/BASS | `CRAFT_BASS_Review_Standards_v3.md` | Retained as a diagnostic review framework, not semantic authority. |
| Research vs publication boundary | Orchestra research template + publication template + reviewer checklist | Made explicit so active research can preserve open/failed branches while publication remains a stronger downstream gate. |
| Concept transfer | Phase Calculus curriculum `CONCEPT_TRANSFER_TEMPLATE.md` and symbolic-dynamics transfer records | Promoted into the general research standard because it prevents analogy from being mistaken for equivalence. |

## Precedence decisions

1. A specific active package's declared semantic authority controls the scientific meaning of that package.
2. A package's own current validator controls technical conformance to that package format.
3. General review metrics do not override more specific package requirements.
4. Research-package closure and publication closure are distinct gates.
5. Source conflicts are documented rather than silently harmonized.

## Source preservation

The original uploaded `Standards.zip` and `Templates.zip` were treated as read-only source material. This synthesis does not edit or replace any source file.
