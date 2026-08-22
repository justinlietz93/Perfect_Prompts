# CRAFT Standard v3  
**Credibility • Rigor • Assumption • Falsifiability • Terminology**

**BASS Score**  
**Bayesian Audit of Scientific Substance**

---

### Claim Ontology (C0–C9)

| Class | Name                        | Description |
|-------|-----------------------------|-----------|
| C0    | Framing                     | Scope, problem, or intent |
| C1    | Descriptive                 | What exists or was observed |
| C2    | Method                      | Method is valid or appropriate |
| C3    | Derivational                | X follows from Y by proof or argument |
| C4    | Empirical                   | Experimental or simulation results |
| C5    | Causal / Mechanistic        | X causes or generates Y |
| C6    | Generalization              | Result holds beyond shown case |
| C7    | Novelty                     | New, stronger, or first |
| C8    | Significance                | Importance or impact |
| C9    | Falsifiability              | Work is testable or predictive |

---

### Core Dimensions (A–T)

**A.** Total claims touched (latent epistemic footprint)  
**B.** Claims explicitly stated  
**C.** Claims with direct support attempt  
**D.** Handwaved or imported claims  
**E.** Domains touched  
**F.** Domains directly necessary  
**G.** Falsifiable claims  
**H.** Claims with explicit falsification instructions  
**I.** Immediately falsifiable claims  
**J.** Falsifiability latency (J0 = immediate … J5 = >10 years)  
**K.** Novel claims  
**L.** Novelty character & depth (L1 cosmetic … L7 foundational)  
**M.** Significance / impact (weighted)  
**N.** Coherence & followability  
**O.** Assumption transparency  
**P.** Dependency traceability  
**Q.** Evidence-role integrity  
**R.** Boundary-condition honesty  
**S.** Reproducibility / auditability  
**T.** Scope-to-evidence ratio

---

### Computational Artifacts Audit (U–Z)

**U.** Code reproducibility & provenance (container, exact dependencies, SHA256)  
**V.** Lean4 formalization integrity (axioms minimal, proofs match claims)  
**W.** Data artifact auditability (raw → processed → result provenance)  
**X.** Figure honesty & evidential support (reproducible, no misleading scales)

**Y–Z. Notebook Reviewer-Friendliness** (new in v3)

**Y1.** Narrative-to-Code Balance (≥40 % explanatory markdown cells)  
**Y2.** Section Self-Containment (each major section has purpose statement + metrics)  
**Y3.** Output Clarity (structured JSON/tables, titled/labelled plots)  
**Y4.** Validation Gate Density (explicit guards, assertions, tripwires)  
**Y5.** Reproducibility Readiness (fixed seeds, policy/commit references, final validation summary)

**Z.** Notebook Reviewer-Friendliness Composite (0–100)

---

### Terminology Quality Index (TQI)

\[
\text{TQI} = 0.20T_1 + 0.20T_2 + 0.15T_3 + 0.20T_4 + 0.25T_6 - 0.30T_5
\]

---

### Bayesian Metascores

Beta posteriors on all proportion-like metrics + extraction confidence, support confidence, novelty confidence, falsifiability confidence, composite confidence.

---

### BASS Composite Score (0–100)

\[
\text{BASS} = 100 \times \Bigl(
0.12S_{\text{sup}} + 0.12S_{\text{antiHW}} + 0.11S_{\text{fals}} + 0.10S_{\text{test}} + 0.08S_{\text{imm}} 
+ 0.09S_{\text{coh}} + 0.08S_{\text{term}} + 0.07S_{\text{nov}} + 0.06S_{\text{impact}} 
+ 0.05S_{\text{exp}} + 0.05S_{\text{dom}} + 0.05S_{\text{comp}} + 0.02S_{\text{lat}}
\Bigr)
\]

(S_comp includes the Z notebook score; S_lat is the latency modifier.)

---

### Verdict Bands

- **90–100**: Exceptional rigor and reviewer-friendliness  
- **80–89**: Strong, credible, high-substance work  
- **70–79**: Solid but with notable weaknesses  
- **60–69**: Mixed; useful but unreliable in places  
- **45–59**: Weak rigor / serious handwave or artifact issues  
- **<45**: Credibility hazard / prestige theater

---

### Operational Review Workflow (30–45 min)

1. Claim extraction (A)  
2. Explicitness & support (B–D)  
3. Domain map (E–F)  
4. Falsifiability ladder (G–J)  
5. Novelty & significance (K–M)  
6. Coherence & terminology (N + TQI)  
7. Assumption & dependency audit (O–R)  
8. Computational artifacts audit (U–Z)  
9. Bayesian metascores & BASS calculation  
10. Diagnostic verdict

---

### One-Page Quick Audit Sheet

**Work:**  
**Reviewer:**  
**Date:**

**Core Counts** (A–T)  
A: ___ B: ___ C: ___ D: ___ E: ___ F: ___ G: ___ H: ___ I: ___ K: ___  

**Notebook Reviewer-Friendliness**  
Y1: ___/4 Y2: ___/4 Y3: ___/4 Y4: ___/4 Y5: ___/4 **Z:** ___/100  

**BASS:** ___ **Confidence:** ___  

**Diagnostic Verdict**  
Strongest feature:  
Weakest feature:  
Biggest hidden assumption:  
Fastest falsifier:  
Recommendation:

---

### Anti-Gaming Rules

1. More claims do not help unless support grows proportionally.  
2. Fancy terminology without definitions lowers TQI.  
3. Novelty penalized without prior-art comparison.  
4. Notebooks that are “mostly code + meta-comments” are heavily penalized on Y1–Y3.  
5. Computational artifacts without reproducibility are penalized in Z.

