# Rules for Rigorous Mathematical Inquiry and Presentation

**Generated on:** September 26, 2025 at 1:23 AM CDT

---

## Generated Summary

This document synthesizes core technical rules, methodological guidelines, and stylistic constraints for mathematical inquiry, proof, and presentation, distilled from various segments of a larger foundational text.

---

## 1. Methodology & Discovery

*   Always set out to both prove and refute a conjecture.
*   Utilize deductive guessing to uncover deeper theorems, especially when counterexamples arise.
*   Formulate naive conjectures through trial and error, conjectures, and refutations, but prioritize commencing with a rigorous proof via deductive guessing.
*   Strive to ascertain the truth of a statement before attempting to formally prove it.
*   Recognize intellectual problems as objective, discoverable entities existing independently.
*   Apply human ingenuity consistently for problem solutions.
*   Study heuristic principles through historical analysis and the rational reconstruction of historical development.
*   Decompose complex conjectures into non-conjectural lemmas or "intuitions."
*   Allow true intuition and interpretation to mature slowly, systematically purging conjectures over time.
*   Actively create new problems, discarding old or obscure ones.
*   Employ mathematical critics to foster mathematical taste and rigor through public criticism.

## 2. Definitions & Axioms

*   Use only the clearest possible concepts.
*   Define any term that is in the least obscure using perfectly known primitive terms.
*   Do not define terms about which there cannot possibly be disagreement.
*   Exclude conjectures from judgments regarding the truth of things.
*   Avoid raising questions about vague or superfluous notions that are irrelevant to the immediate purpose.
*   Derive definitions and axioms initially through intuition.
*   Treat definitions as either additional axioms or axioms as implicit definitions, recognizing their interchangeability.
*   Register only terms specific to the theory being developed, deliberately excluding underlying logical, set-theoretical, or arithmetical terms assumed to be perfectly familiar.
*   Acknowledge that perfectly known concepts cannot be altered by experience.
*   Do not attempt to prove indubitably true axioms.
*   When defining a vague term, replace it with a new, more precise one; the old term then serves merely as an abbreviation. Definitions, when serving as abbreviations, must not introduce falsehoods.
*   Ensure definitions preserve relevant aspects of the old meaning and effectively transfer essential elements of meaning to the new term.
*   Employ startling definitions strategically to provide rigid demonstrations and protect mathematical rigor from skeptical challenges.
*   **Specific Mathematical Definitions:**
    *   A function `f` is of **bounded variation** on an interval `[a, b]` if its total variation, `V(f)`, is finite.
    *   The **Dirichlet function** `f(x)` is defined as `0` when `x` is rational and `1` when `x` is irrational.
    *   A set `E` in an hereditary σ-ring `H` is **φ*-measurable** if, for every set `A` in `H`, `φ*(A) = φ*(A ∩ E) + φ*(A ∩ Eᶜ)`, where `φ*` is an outer measure on `H`.
    *   A function `y` of `x` is defined if, for each value of `x` within a certain interval, there corresponds a definite value of `y`, regardless of whether `y` depends on `x` according to the same law throughout the interval, or whether this dependence can be expressed by mathematical operations.

## 3. Proof & Validation

*   Inspect proofs meticulously to identify and list all non-trivial lemmas through proof-analysis.
*   Ensure that the logical truth of any conditional statement (incorporating all relevant lemmas) remains unimpugned by counterexamples.
*   If a theorem is found not to be universally valid, subject its proof to detailed analysis to uncover any extra hidden assumptions.
*   Upon discovering a hidden hypothesis, infer backwards that its condition is not met by the counterexamples to restore agreement with the proof sequence.
*   Conduct proof analysis to systematically shift all doubt from the proof itself to its axioms or antecedents, thereby making all assumptions for validity explicitly clear.
*   Combine the rigor of formal proof with the analytical rigor of proof-analysis.
*   Ensure that valid inference is essentially infallible, particularly concerning the characterization of logical terms.
*   Proofs must ultimately achieve indubitable certainty.
*   Proof checking must be a completely mechanical process, yielding an answer in a finite number of steps.
*   Irrefutable proofs must not depend on the specific meaning of particular terms; their burden must be fully borne by the universally accepted meaning of non-specific (formative) terms.
*   Precisely define the meaning of formative terms to effectively regulate the generation and interpretation of counterexamples.
*   Proofs should be expressible within a system where logic is the dominant theory, ensuring that no counterexamples exist for statements proved in such a system, relative to its formative logical terms.
*   Formal proofs must serve as accurate translations of their informal counterparts.
*   Exercise circumspection when utilizing propositions accepted without rigorous proof.
*   Strive to eliminate all uncertainty as a fundamental goal for rigorous mathematics.
*   Ensure that logical truth does not depend on the meaning of distinguished constituents whose concepts have been stretched.

## 4. Critique & Refinement

*   Diligently seek counterexamples for both the main conjecture (global counterexamples) and any suspect lemmas (local counterexamples).
*   If a global counterexample is discovered:
    *   Discard the original conjecture.
    *   Add the suitable lemma (refuted by the counterexample) to the proof-analysis.
    *   Replace the discarded conjecture with an improved version that incorporates that lemma as a new condition.
*   If a local counterexample is found, always check if it also functions as a global counterexample.
*   If a counterexample is local but not global, enhance the proof-analysis by replacing the refuted lemma with an unfalsified one.
*   Re-examine a proof to specifically identify the "guilty lemma" (a local counterexample) associated with a global counterexample, and explicitly formulate this lemma.
*   Incorporate an explicit guilty lemma into the primitive conjecture as a necessary condition.
*   Supersede primitive conjectures with improved theorems that feature newly generated concepts derived from the proof process.
*   Thoroughly check all previously accepted consequences of any refuted conjecture.
*   Never dismiss a refutation as a mere "monster."
*   Monster-barring should serve to translate existing definitions, not to form genuinely new concepts.
*   Replace naive classifications with theoretical classifications, which are generated by proofs or explanations.
*   Conjectures and concepts alike must pass through the iterative process of proofs and refutations. Naive conjectures and concepts must be superseded by improved (proof-generated or theoretical) versions through this method.
*   Treat refutations arising from naive concept-stretching as valuable prompts for more rigorous, theoretical concept-stretching.
*   View naive counterexamples (freaks) with significant suspicion, as they may not be genuine counterexamples or might belong to a different theoretical framework.
*   Allow concept-stretching only for a distinguished subset of constituents that are explicitly identified as prime targets of criticism.
*   Identify and respect terms whose meaning cannot be stretched without undermining the basic principles of rationality.

## 5. Mathematical Object Properties & Constraints

*   **Polygons:**
    *   For any polygon, the number of vertices minus the number of edges must equal zero (V - E = 0).
    *   For a single edge, the number of vertices minus the number of edges must equal one (V - E = 1).
    *   When fitting new edges to construct a figure, both the number of vertices (V) and edges (E) must increase by one.
    *   To close an open edge system to form a polygon, an edge must be fitted without adding a new vertex, resulting in V - E = 0.
    *   A single vertex counts as V=1.
*   **Polyhedra (General):**
    *   A polyhedron must be defined by three sets: vertices, edges, and faces, coupled with an incidence matrix characterizing their relationships.
    *   The terms: vertices (0-polytopes), edges (1-polytopes), faces (2-polytopes), and polyhedra (3-polytopes) are considered undefined primitives.
*   **Polyhedra (Euler Characteristic Formulas):**
    *   When fitting a new face to an open polygonal system, the excess of edges over vertices (E-V) must increase by one.
    *   For an F-polygonal system constructed by fitting faces, E-V = F-1.
    *   For any closed polygonal system or closed polyhedron constructed by fitting faces, V - E + F = 2.
    *   For all normal open polygonal systems, V - E + F = 1.
    *   A 'normal' polyhedron must be built from a 'perfect' polygon by fitting F-2 faces without altering V-E+F, followed by a last closing face that increases V-E+F by 1.
    *   A 'perfect' polygon must be built from a single vertex by fitting E-1 edges without altering V-E, followed by a last closing edge that decreases V-E by 1.
    *   If `n` cuts are needed to reduce a polyhedron to a simple one, its Euler characteristic must be `2 - 2n`.
    *   For normal n-spheroid polyhedra, V - E + F = 2 - 2(n-1).
    *   For normal n-spheroid polyhedra with multiply-connected faces, V - E + F = 2 - 2(n-1) + sum(e_k).
    *   For polyhedra with cavities, the total V - E + F must be the sum of the characteristics of each disconnected surface: Sum {2 - 2(n_i-1) + sum(e_k_i)}.
    *   For a polyhedron with `k` tunnels and `m` ring-shaped faces, V - E + F = 2 - 2k + m.
*   **Polyhedra (Simplicity and Connectivity):**
    *   A polyhedron is simply connected if all closed loopless systems of edges have a distinct inside and outside, and only one closed loopless system of faces separates its inside from its outside.
    *   The simply-connectedness of a polyhedron implies that all 1-circuits and 2-circuits must bound.
    *   The simply-connectedness of faces implies that all 0-circuits must bound.
    *   For polyhedra with simply connected faces, the Betti number p0 must equal 1.
*   **Polytopes, Chains, and Circuits (Vector Algebra):**
    *   The boundary of a k-polytope is defined as the sum of its (k-1) polytopes that belong to it according to the incidence matrices.
    *   A sum of k-polytopes constitutes a k-chain.
    *   The boundary of a k-chain is defined as the sum modulo 2 of its (k-1) polytopes.
    *   A k-chain is a k-circuit if and only if its boundary is zero.
    *   A k-circuit bounds if it is the boundary of a (k+1)-chain.
    *   The boundary of the boundary of any k-chain must always be zero (Axiom).
    *   The empty set is defined as the -1-dimensional polytope.
    *   The boundary of any vertex is the empty set (Axiom).
    *   The boundary of two vertices must be zero due to modulo 2 algebra (Axiom).
    *   Even numbers of vertices must form circuits; odd numbers of vertices must not.
    *   k-chains must form N_k-dimensional vector-spaces over the field of residue-classes modulo 2.
    *   Circuits must form subspaces of chain spaces, and bounding circuits must form subspaces of circuit spaces.
    *   Circuit space and bounding circuit space are identical if and only if their dimensions are identical (Axiom).
    *   The number of independent solutions for homogeneous linear equations (representing k-circuits) must be N_k - p_k, where p_k is the rank of the incidence matrix for k-polytopes.
    *   The number of independent solutions for inhomogeneous linear equations (representing bounding k-circuits) must be p_{k+1}, where p_{k+1} is the rank of the incidence matrix for (k+1)-polytopes.
*   **Counterexample Classification:**
    *   Logical counterexamples are global but not local.
    *   Heuristic counterexamples are either local but not global, or both global and local.
    *   A refutation must occur when substituting specific terms into a theorem renders the theorem false.
*   **Total Variation Calculation:** Calculate `V(f)` (total variation of `f`) as the least upper bound (lub) of the sum `Σ |f(xi) - f(xi-1)|` over all possible partitions of `[a, b]`.

## 6. Presentation & Communication

*   **Deductivist Style (Obligatory):**
    *   Begin with a painstakingly stated list of axioms, lemmas, and/or definitions.
    *   Follow this list with carefully worded theorems.
    *   Present the theorem immediately with its proof.
    *   Portray mathematics as an ever-increasing collection of eternal, immutable truths.
    *   Explicitly exclude counterexamples, refutations, and critical commentary from the main exposition.
    *   Establish an authoritarian tone by beginning with disguised monster-barring and proof-generated definitions, presenting only the fully-fledged theorem, and suppressing the primitive conjecture, refutations, and criticisms of the proof.
*   **Inductivist Style (Scientific Papers):**
    *   Start with a meticulous description of the experimental layout, followed by the experiment's description and result.
    *   Conclude the paper with a generalization.
    *   Conceal the initial problem-situation and the conjecture that the experiment was designed to test.
    *   Ensure counterexamples never appear, operating under the assumption that observations (not theory) are the primary starting point.
*   **Heuristic Style:**
    *   Clearly highlight the problem-situation and the specific logical insights that led to the birth of new concepts.
    *   Omit accidental errors without loss of understanding; dealing with such errors is solely the domain of historical analysis.
*   **Proof-Generated Definition Timing:** Present proof-generated definitions immediately alongside or subsequent to their proof-ancestor; never introduce them significantly before the proof to which they are heuristically secondary.

## 7. Notation & Terminology

*   Examine proofs of other theorems to determine if a newly discovered lemma or proof-generated concept also appears within them, promoting consistent terminology.
*   Ensure that theoretical language consistently supersedes naive language in formal discourse.
*   Use `V(f)` as the standard notation for the total variation of function `f` on an interval `[a, b]`.
*   Employ `R(g)` to denote the class of Riemann-Stieltjes functions integrable with respect to `g`.
*   For piecewise continuous functions, at a point of discontinuity `δ`, use `φ(δ − 0)` for the `y`-coordinate of the portion ending at `δ` and `φ(δ + 0)` for the `y`-coordinate of the portion beginning at `δ`.

## Key Highlights

* Always set out to both prove and refute a conjecture to ensure thoroughness in mathematical inquiry.
* Define any obscure term using perfectly known primitive terms, ensuring maximal clarity and avoiding definitions for self-evident concepts.
* Meticulously inspect proofs to identify all non-trivial lemmas and hidden assumptions through detailed proof-analysis, making all assumptions explicitly clear.
* Diligently seek counterexamples for both main conjectures (global) and suspect lemmas (local), using any refutation to discard, refine, or improve the original conjecture.
* Never dismiss a refutation as a mere 'monster'; instead, use it to prompt more rigorous, theoretical concept-stretching and improve classifications.
* Proof checking must be a completely mechanical process, yielding an answer in a finite number of steps, and proofs must ultimately achieve indubitable certainty.
* For formal presentation, adopt a deductivist style, beginning with explicitly stated axioms, lemmas, and definitions, followed by theorems and their proofs, while excluding counterexamples and critical commentary from the main exposition.
* Conjectures and concepts must pass through an iterative process of proofs and refutations, superseding naive versions with improved, theoretically generated concepts.
* Strive to eliminate all uncertainty as a fundamental goal for rigorous mathematics, ensuring logical truth does not depend on the stretched meaning of distinguished constituents.

## Insightful Ideas

* Develop a standardized 'Proof Analysis Protocol' or toolkit to systematically identify non-trivial lemmas, hidden assumptions, and 'guilty lemmas' as detailed in the Proof & Validation section.
* Create a formal guide or checklist to systematically apply the 'Critique & Refinement' methodology, ensuring consistent handling of global and local counterexamples, and iterative improvement of conjectures and definitions.
* Conduct a pilot study applying the 'Deductivist Style' of presentation to a contemporary complex mathematical theory to evaluate its practical benefits and challenges in terms of clarity, pedagogy, and knowledge dissemination.
* Explore computational approaches or AI-assisted frameworks for 'deductive guessing' to aid in uncovering deeper theorems and formulating new conjectures based on existing axioms and observed counterexamples.