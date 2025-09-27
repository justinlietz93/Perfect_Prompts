# Rules Distilled from Formal Logic, Set Theory, and Discrete Mathematics

***This document consolidates and synthesizes technical rules, syntax requirements, and constraints from various segments of a larger mathematical treatise, forming a comprehensive guide for logical construction, proof methodology, and definitional precision.***

**Generated on:** September 25, 2025 at 11:06 PM CDT

---

## I. Syntax and Notation

1.  **Logical Connectives:**
    *   `V` represents "or" (disjunction).
    *   `Λ` represents "and" (conjunction).
    *   `¬` represents "not" or "is false" (negation).
    *   `→` represents "If...then..." (conditional).
    *   `↔` represents "P if and only if Q" (`P iff Q`), abbreviating `(P → Q) ∧ (Q → P)`.
2.  **Operator Precedence and Placement:**
    *   The negation symbol (`¬`) must apply only to the statement immediately following it (e.g., `¬P ∧ Q` means `(¬P) ∧ Q`).
    *   The conjunction (`Λ`) and disjunction (`V`) symbols must only be used *between* two statements.
    *   The negation symbol (`¬`) must only be used *before* a statement.
    *   Expressions like `P ¬ ∧ Q`, `P ∧ ¬ V Q`, and `P = Q` are ungrammatical.
3.  **Quantifier Syntax:**
    *   `∀x P(x)` represents "For all x, P(x)".
    *   `∃x P(x)` represents "There exists an x such that P(x)".
    *   `∀x` and `∃x` must apply only to the statement immediately following them (e.g., `∀x P(x) → Q(x)` means `(∀x P(x)) → Q(x)`).
    *   `∃!x P(x)` represents "There is exactly one x such that P(x) is true", abbreviating `∃x (P(x) ∧ ¬∃y (P(y) ∧ y ≠ x))`.
    *   Bounded quantifiers must specify the universe: `∀x ∈ U P(x)` and `∃x ∈ U P(x)`.
4.  **Set Notation:**
    *   The empty set is denoted `∅` or `{}`. The notation `{∅}` is distinct from `∅`.
    *   Set-builder notation `{x | P(x)}` names a set and binds the variable `x`.
    *   Set operations (`∩`, `∪`, `\`) must only be used to combine sets; expressions like `A ∧ B` are meaningless.
    *   The intersection of a family of sets `∩F` must only be used when `F` is not the empty set (`F ≠ ∅`).
    *   Power set notation `P(A)` denotes the set of all subsets of `A`.
5.  **Relation and Function Notation:**
    *   Ordered pairs `(a,b)` are distinct from `(b,a)` unless `a=b`.
    *   `x | y` denotes "x divides y".
    *   `R^n` denotes the n-th power of a relation `R`.
    *   `f: A → B` indicates a function `f` from domain `A` to codomain `B`.
    *   `f(a)` denotes the value of function `f` at `a`.
    *   `g ∘ f` denotes function composition.
    *   `f(X)` denotes the image of a set `X` under `f`.
    *   `f⁻¹(Y)` denotes the inverse image of a set `Y` under `f`, and is valid even if `f⁻¹` is not a function.
6.  **Number Theory Notation:**
    *   `x ≡ y (mod m)` denotes "x is congruent to y modulo m".
    *   `[a]_m` denotes the equivalence class of `a` modulo `m`.
    *   `Z/mZ` denotes the set of all equivalence classes modulo `m`.
    *   `D(a)` denotes the set of positive divisors of `a`.
    *   `gcd(a,b)` denotes the greatest common divisor of `a` and `b`.
    *   `lcm(a,b)` denotes the least common multiple of `a` and `b`.
    *   `phi(m)` denotes Euler's phi (totient) function.
    *   `(Z/mZ)*` denotes the set of invertible elements in `Z/mZ`.
7.  **Cardinality and Sequence Notation:**
    *   `I_n` denotes the set `{i ∈ Z+ | i ≤ n}`.
    *   `|A|` denotes the cardinality (number of elements) of a finite set `A`.
    *   `A ~ B` indicates that sets `A` and `B` are equinumerous.
    *   `A ≤ B` indicates that set `B` dominates set `A`.
    *   `A < B` indicates that `B` strictly dominates `A`.
    *   A finite sequence of elements of `A` must be defined as a function `f: I_n → A`.
8.  **General Formatting:**
    *   The use of "..." in formulas indicates an unstated pattern in calculation, which may require a more rigorous proof (e.g., by induction).
    *   Summation notation `Σ(i=m to n) a_i` represents the sum `am + am+1 + ... + an`.
    *   `n!` denotes n factorial.
    *   `(n choose k)` denotes the binomial coefficient `n! / (k!(n-k)!)`.

## II. Logical Semantics and Interpretation

1.  **Statement Validity:** An argument is valid if the premises cannot all be true without the conclusion being true as well.
2.  **Statement Representation:**
    *   Only use letters to represent unambiguous statements that are either true or false.
    *   Do not use letters to represent questions, exclamations, or vague statements.
    *   Determine the logical form of a statement by its meaning, not by word-for-word translation.
3.  **Truth Values:**
    *   A conjunction (`P ∧ Q`) is true if and only if both `P` and `Q` are true.
    *   A negation (`¬P`) is true if and only if `P` is false.
    *   The disjunction symbol (`V`) must always be interpreted as inclusive or, unless explicitly specified otherwise. A disjunction (`P V Q`) is true if `P` is true, or `Q` is true, or both are true.
    *   A conditional statement (`P → Q`) is false if and only if `P` is true and `Q` is false.
4.  **Equivalent Formulas:**
    *   Equivalent formulas always have the same truth value.
    *   Logical equivalences apply to sub-formulas; a sub-formula can be substituted for a letter in an equivalence.
    *   Equivalent formulas may always be substituted for one another in any expression.
    *   **Conditional Laws:** `P → Q` is equivalent to `¬P V Q`, and to `¬(P ∧ ¬Q)`.
    *   **Contrapositive Law:** `P → Q` is equivalent to `¬Q → ¬P`.
    *   **Quantifier Negation Laws:** `¬∃x P(x)` is equivalent to `∀x ¬P(x)`, and `¬∀x P(x)` is equivalent to `∃x ¬P(x)`.
    *   **Bounded Quantifier Expansion:** `∃x ∈ A P(x)` is equivalent to `∃x (x ∈ A ∧ P(x))`, and `∀x ∈ A P(x)` is equivalent to `∀x (x ∈ A → P(x))`.
5.  **Quantifier Meaning and Order:**
    *   "There are objects `x` and `y`" or "for all objects `x` and `y`" does not preclude `x` and `y` being the same object.
    *   The order of mixed quantifiers (`∀x∃y` vs. `∃y∀x`) can change the meaning of a statement.
    *   The order of two universal quantifiers (`∀x∀y` vs. `∀y∀x`) can always be switched without changing the meaning of the formula.
    *   The order of two existential quantifiers (`∃x∃y` vs. `∃y∃x`) can always be switched without changing the meaning of the formula.
6.  **Vacuously True/False Statements:**
    *   If `A` is the empty set (`∅`), then `∃x ∈ A P(x)` is always false.
    *   If `A` is the empty set (`∅`), then `∀x ∈ A P(x)` is always true.

## III. Fundamental Definitions

1.  **Logical Formulas:**
    *   **Well-formed Formula (Formula):** A grammatical expression in the language of logic.
    *   **Tautology:** A formula that is always true.
    *   **Contradiction:** A formula that is always false.
2.  **Sets and Elements:**
    *   **Universe of Discourse:** The set of all possible values for the variables in a statement.
    *   **Truth Set of P(x):** `{x | P(x)}`.
    *   **Empty Set (Null Set):** The unique set with no elements, denoted `∅` or `{}`.
    *   **Intersection of A and B:** `A ∩ B = {x | x ∈ A ∧ x ∈ B}`.
    *   **Union of A and B:** `A ∪ B = {x | x ∈ A ∨ x ∈ B}`.
    *   **Difference of A and B:** `A \ B = {x | x ∈ A ∧ x ∉ B}`.
    *   **Subset:** `A ⊆ B` if every element of `A` is also an element of `B`.
    *   **Disjoint Sets:** Sets `A` and `B` are disjoint if `A ∩ B = ∅`.
    *   **Power Set of A:** `P(A) = {X | X ⊆ A}`.
3.  **Relations:**
    *   **Cartesian Product:** `A × B = {(a,b) | a ∈ A ∧ b ∈ B}`.
    *   **Relation from A to B:** Any subset `R ⊆ A × B`.
    *   **Relation on A (Binary Relation on A):** A relation `R` from `A` to `A`.
    *   **Domain of R:** `Dom(R) = {a ∈ A | ∃b ∈ B ((a,b) ∈ R)}`.
    *   **Range of R:** `Ran(R) = {b ∈ B | ∃a ∈ A ((a,b) ∈ R)}`.
    *   **Inverse of R:** `R⁻¹ = {(b,a) ∈ B × A | (a,b) ∈ R}`.
    *   **Composition of S and R:** `S ∘ R = {(a,c) ∈ A × C | ∃b ∈ B ((a,b) ∈ R ∧ (b,c) ∈ S)}`.
    *   **R-path:** A function `f: I_n → A` is an R-path from `a` to `b` of length `n` if `f(0) = a`, `f(n) = b`, and `(f(i), f(i+1)) ∈ R` for all `i < n`.
    *   **Distance:** `d(a,b)` is the smallest positive integer `n` such that `(a,b) ∈ R^n`.
4.  **Types of Relations (on a set A):**
    *   **Reflexive Relation:** `∀x ∈ A (xRx)`.
    *   **Irreflexive Relation:** `∀x ∈ A ((x,x) ∉ R)`.
    *   **Symmetric Relation:** `∀x ∈ A ∀y ∈ A (xRy → yRx)`.
    *   **Antisymmetric Relation:** `∀x ∈ A ∀y ∈ A ((xRy ∧ yRx) → x = y)`.
    *   **Transitive Relation:** `∀x ∈ A ∀y ∈ A ∀z ∈ A ((xRy ∧ yRz) → xRz)`.
    *   **Partial Order:** A relation that is reflexive, transitive, and antisymmetric.
    *   **Strict Partial Order:** A relation that is irreflexive and transitive. A strict partial order must not be considered a partial order.
    *   **Total Order:** A partial order `R` such that `∀x ∈ A ∀y ∈ A (xRy ∨ yRx)`.
    *   **Strict Total Order:** A strict partial order `R` such that `∀x ∈ A ∀y ∈ A (xRy ∨ yRx ∨ x=y)`.
    *   **Equivalence Relation:** A relation that is reflexive, symmetric, and transitive.
5.  **Bounds and Elements in Ordered Sets:**
    *   **R-Smallest Element (of B):** An element `b ∈ B` such that `∀x ∈ B (bRx)`.
    *   **R-Minimal Element (of B):** An element `b ∈ B` such that `¬∃x ∈ B (xRb ∧ x ≠ b)`.
    *   **Lower Bound (for B):** An element `a` (not necessarily in B) such that `∀x ∈ B (aRx)`.
    *   **Upper Bound (for B):** An element `a` (not necessarily in B) such that `∀x ∈ B (xRa)`.
    *   **Least Upper Bound (Lu.b.):** The smallest element of the set of all upper bounds for B.
    *   **Greatest Lower Bound (Gl.b.):** The largest element of the set of all lower bounds for B.
6.  **Number Properties:**
    *   **Bound Variable:** A variable subject to a quantifier (e.g., `x` in `∀x P(x)`).
    *   **Even Integer:** An integer `x` is even if `∃k ∈ Z (x = 2k)`.
    *   **Odd Integer:** An integer `x` is odd if `∃k ∈ Z (x = 2k + 1)`.
    *   **Divisors of a:** `D(a) = {d ∈ Z+ | d | a}`.
    *   **Greatest Common Divisor (gcd):** The largest element of the set of common divisors `D(a) ∩ D(b)`.
    *   **Least Common Multiple (lcm):** The smallest positive integer `m` such that `a | m` and `b | m`.
    *   **Relatively Prime:** Two positive integers `a` and `b` are relatively prime if `gcd(a,b) = 1`.
    *   **Congruence Modulo m:** An integer `x` is congruent to an integer `y` modulo `m` (`x ≡ y (mod m)`) if and only if `m | (x - y)`.
    *   **Fermat Pseudoprime:** A composite number `n` that passes the Fermat primality test for a base `a` (i.e., `a^(n-1) ≡ 1 (mod n)`).
    *   **Carmichael Number:** An integer `n > 2` that is composite and a Fermat pseudoprime to the base `a` for all `a` in `{2,3,...,n-1}` that are relatively prime to `n`.
    *   **Miller-Rabin Witness:** For an odd `n > 1` and `n-1 = 2^s * d` (d odd), a value `a` is a Miller-Rabin witness for `n` if `2 ≤ a ≤ n-1`, `a^d <binary data, 1 bytes><binary data, 1 bytes> 1 (mod n)`, and for all `i < s`, `a^(2^i * d) <binary data, 1 bytes><binary data, 1 bytes> -1 (mod n)`.
7.  **Functions:**
    *   **Function Definition:** A relation `F` is a function from `A` to `B` if `∀a ∈ A ∃!b ∈ B ((a,b) ∈ F)`.
    *   **Identity Function:** The identity relation `iA` (from `A` to `A`) is the identity function on `A`.
    *   **One-to-one (Injection):** A function `f: A → B` is one-to-one if `∀a1, a2 ∈ A (f(a1) = f(a2) → a1 = a2)`.
    *   **Onto (Surjection):** A function `f: A → B` is onto if `Ran(f) = B` (i.e., `∀b ∈ B ∃a ∈ A (f(a) = b)`).
    *   **One-to-one Correspondence (Bijection):** A function that is both one-to-one and onto.
    *   **Binary Operation:** A function from `A × A` to `A`, often written between its arguments (e.g., `x * y`).
8.  **Cardinality:**
    *   **Equinumerous:** Two sets `A` and `B` are equinumerous if `∃` a bijection `f: A → B`.
    *   **Finite Set:** A set `A` is finite if `∃n ∈ N (A ~ I_n)`. The cardinality `|A|` is this unique `n`. The empty set is finite with cardinality 0.
    *   **Infinite Set:** A set `A` is infinite if it is not finite.
    *   **Denumerable Set:** A set `A` is denumerable if `A ~ Z+`.
    *   **Countable Set:** A set `A` is countable if it is either finite or denumerable.
    *   **Uncountable Set:** A set `A` is uncountable if it is not countable.
    *   **Dominance:** `B` dominates `A` (`A ≤ B`) if `∃` a one-to-one function `f: A → B`.
    *   **Strict Dominance:** `B` strictly dominates `A` (`A < B`) if `A ≤ B` and `A` is not equinumerous with `B`.
9.  **Recursive Definitions:**
    *   A recursive definition for a function `f` with domain `N` must specify `f(k)` (base case) and provide a rule to compute `f(n+1)` from `f(n)`.
    *   **Factorial:** `n!` is defined by `0! = 1` and `(n+1)! = (n+1)n!`.
    *   **Recursive Summation:** `Σ(i=m to m) a_i = a_m`; `Σ(i=m to n+1) a_i = (Σ(i=m to n) a_i) + a_(n+1)`.
    *   **Relation Power:** `R^1 = R`; `R^(n+1) = R^n ∘ R`.
    *   **Fibonacci Numbers:** `F0 = 0`; `F1 = 1`; `F_n = F_(n-1) + F_(n-2)` for `n ≥ 2`.

## IV. Set Theory and Relations (Properties & Usage)

1.  **Set Membership Equivalences:**
    *   `y ∈ {x | P(x)}` is equivalent to `P(y)`.
    *   `y ∉ {x | P(x)}` is equivalent to `¬P(y)`.
    *   `y ∈ {x ∈ A | P(x)}` is equivalent to `y ∈ A ∧ P(y)`.
    *   `x ∈ A ∩ B` is equivalent to `x ∈ A ∧ x ∈ B`.
    *   `x ∈ A ∪ B` is equivalent to `x ∈ A ∨ x ∈ B`.
    *   `x ∈ A \ B` is equivalent to `x ∈ A ∧ x ∉ B`.
    *   `x ∈ P(A)` is equivalent to `x ⊆ A`.
2.  **Set Equality and Subset:**
    *   `A = B` is equivalent to `(A ⊆ B) ∧ (B ⊆ A)`.
    *   `A ⊆ B` is equivalent to `∀x (x ∈ A → x ∈ B)`.
    *   The empty set is a subset of every set (`∅ ⊆ A`).
3.  **Disjoint Sets:**
    *   Sets `X` and `Y` are disjoint is equivalent to `¬∃x (x ∈ X ∧ x ∈ Y)`.
    *   A family of sets `F` is pairwise disjoint if for every pair of distinct elements `X, Y ∈ F`, their intersection is the empty set.
4.  **Relation Properties:**
    *   `R⁻¹⁻¹ = R`.
    *   `Dom(R⁻¹) = Ran(R)`.
    *   `Ran(R⁻¹) = Dom(R)`.
    *   Composition is associative: `T ∘ (S ∘ R) = (T ∘ S) ∘ R`.
    *   Inverse of composition: `(S ∘ R)⁻¹ = R⁻¹ ∘ S⁻¹`.
    *   A relation `R` on `A` is reflexive if and only if `iA ⊆ R`.
    *   A relation `R` on `A` is symmetric if and only if `R = R⁻¹`.
    *   A relation `R` on `A` is transitive if and only if `R ∘ R ⊆ R`.
    *   A relation `R` is both antisymmetric and symmetric if and only if `R ⊆ iA`.
5.  **Relation Closures:**
    *   The **symmetric closure** of `R` on `A` is `R ∪ R⁻¹`. It is the smallest symmetric relation on `A` that contains `R`.
    *   The **transitive closure** of `R` on `A` is the smallest transitive relation on `A` that contains `R`. It can be defined as the set of all ordered pairs `(a,b)` such that there is an R-path from `a` to `b`.
6.  **Partitions and Equivalence Relations:**
    *   A family of sets `F` is a **partition** of `A` if: `∪F = A`, `F` is pairwise disjoint, and every set `X ∈ F` is non-empty.
    *   The **equivalence class** of `x` with respect to `R`, `[x]R`, is `{y ∈ A | yRx}`.
    *   The set of all equivalence classes of elements of `A` is called **A modulo R** (`A/R`).
    *   For any equivalence relation `R` on `A`, every element `x ∈ A` is in its own equivalence class `[x]R`.
    *   For any equivalence relation `R` on `A`, `y ∈ [x]R` if and only if `[y]R = [x]R`.
    *   If `R` is an equivalence relation on `A`, then `A/R` is a partition of `A`.
    *   For every partition `F` of `A`, there exists an equivalence relation `R` on `A` such that `A/R = F`. This `R` is defined as `∪(X × X)` for all `X ∈ F`. For such an `R`, `[x]R = X` for any `X ∈ F` and `x ∈ X`.
7.  **Order Properties:**
    *   If a set `B` has an R-smallest element (with respect to a partial order `R`), then this element is unique.
    *   If `b` is the smallest element of a set `B`, then `b` must also be a minimal element of `B`, and it is the only minimal element.
    *   If `R` is a total order and `b` is a minimal element of `B`, then `b` must be the smallest element of `B`.
    *   A smallest element or a minimal element of a set `B` must actually be an element of `B`.
    *   A lower bound for a set `B` need not be an element of `B`; a smallest element of `B` is a lower bound that is also an element of `B`.

## V. Functions (Properties & Usage)

1.  **Function Definition and Equality:**
    *   If a function `f: A → B` is defined by a rule for `f(a)`, that rule must determine `f(a)` for every `a ∈ A`.
    *   If a function's rule is given without explicit scope, it is understood to apply to all elements in its domain.
    *   The domain of a function `f: A → B` is the entire set `A`. The range `Ran(f)` is `f(A)`.
    *   Two functions `f` and `g` from `A` to `B` are equal if and only if `f(a) = g(a)` for all `a ∈ A`.
2.  **Composition and Inverses:**
    *   The composition of two functions `f: A → B` and `g: B → C` results in a function `g ∘ f: A → C`, with `(g ∘ f)(a) = g(f(a))`.
    *   Function composition must be associative.
    *   If `f` is one-to-one and onto, its inverse relation `f⁻¹` is a function from `B` to `A`. `f⁻¹(b)` is the unique `a` such that `f(a) = b`.
    *   If `f: A → B` and `f⁻¹: B → A` are functions, then `f⁻¹ ∘ f` is `iA`, and `f ∘ f⁻¹` is `iB`.
3.  **Properties via Composition:**
    *   If `∃g: B → A` such that `g ∘ f = iA`, then `f` must be one-to-one.
    *   If `∃g: B → A` such that `f ∘ g = iB`, then `f` must be onto.
    *   The following statements for a function `f: A → B` are equivalent:
        *   `f` is one-to-one and onto.
        *   `f⁻¹` is a function from `B` to `A`.
        *   `∃g: B → A` such that `g ∘ f = iA` and `f ∘ g = iB`.
    *   If `g ∘ f = iA` and `f ∘ g = iB`, then `g` must be equal to `f⁻¹`.
    *   If two functions `f` and `g` are both one-to-one, their composition `g ∘ f` must also be one-to-one.
    *   If two functions `f` and `g` are both onto, their composition `g ∘ f` must also be onto.
4.  **Set Closure Under Functions:**
    *   A set `C` is **closed** under a function `f: A → A` if `∀x ∈ C (f(x) ∈ C)`.
    *   A set `C` is **closed** under a function `f: A × A → A` if `∀x,y ∈ C (f(x,y) ∈ C)`.
    *   The **closure** of a set `B` under a function `f` is the unique smallest set `C ⊆ A` such that `B ⊆ C` and `C` is closed under `f`.
    *   The closure of `B` under `f` must exist for any `f: A → A` and `B ⊆ A`.
    *   For `f: A → A` and `C ⊆ A`, `C` is closed under `f` if and only if `f(C) ⊆ C`, which is equivalent to `C ⊆ f⁻¹(C)`.
    *   The constructive definition of closure for `f: A → A` and `B ⊆ A` is `∪_(n∈N) B_n`, where `B0 = B` and `B_(n+1) = f(B_n)`.
5.  **Images and Inverse Images:**
    *   For any function `f` and subsets `W, X` of its domain, `f(W ∩ X) ⊆ f(W) ∩ f(X)`.
    *   If a function `f` is one-to-one, then for any subsets `W, X` of its domain, `f(W ∩ X) = f(W) ∩ f(X)`.

## VI. Number Theory and Modular Arithmetic (Properties & Usage)

1.  **Divisibility and Primes:**
    *   For `y = (x + √(x^2 - 4))/2` to be defined in the real numbers, `x^2 - 4` must be greater than or equal to `0`. If `x^2 - 4 = 0`, the expression is `x/2`. If `x^2 - 4 > 0`, `√(x^2 - 4)` is a real number.
    *   The greatest common divisor function `gcd` must be commutative: `gcd(a,b) = gcd(b,a)`.
    *   If `b | a`, then `gcd(a,b) = b`.
    *   **Euclidean Algorithm:** For positive integers `a > b`, let `r` be the remainder of `a` divided by `b`. If `r = 0`, then `gcd(a,b) = b`. If `r > 0`, then `gcd(a,b) = gcd(b,r)`.
    *   **Bezout's Identity:** For any positive integers `a` and `b`, there must exist integers `s` and `t` such that `gcd(a,b) = s*a + t*b`.
    *   For any positive integers `a, b, d`, if `d | a` and `d | b`, then `d | gcd(a,b)`.
    *   **Prime Divisor Property (Gauss's Lemma):** For any positive integers `a, b, c`, if `c | ab` and `gcd(a,c) = 1`, then `c | b`.
    *   **Prime Divisor Property:** If a prime `p | ab`, then `p | a` or `p | b`. (Generalized: If `p | (a1*...*ak)`, then `p | ai` for at least one `i`.)
    *   **Unique Prime Factorization:** Every integer `n > 1` must have a unique prime factorization when primes are listed in nondecreasing order. The number `1` is factored as the product of the empty list of prime numbers.
    *   The divisors of an integer `n` (with prime factorization `p1^e1 * ... * pk^ek`) are precisely the numbers of the form `p1^f1 * ... * pk^fk`, where `0 ≤ fi ≤ ei`.
    *   For `a = p1^e1 * ... * pk^ek` and `b = p1^f1 * ... * pk^fk`, `gcd(a,b) = p1^min(e1,f1) * ... * pk^min(ek,fk)`.
    *   For `a = p1^e1 * ... * pk^ek` and `b = p1^f1 * ... * pk^fk`, `lcm(a,b) = p1^max(e1,f1) * ... * pk^max(ek,fk)`.
    *   **gcd-lcm Product Identity:** `gcd(a,b) * lcm(a,b) = ab`. Thus, `lcm(a,b) = (a * b) / gcd(a,b)`.
2.  **Modular Arithmetic (Properties of Z/mZ):**
    *   For every positive integer `m`, the congruence relation `≡_m` is an equivalence relation on `Z`.
    *   For any positive integer `m` and integer `a`, there exists exactly one integer `r` such that `0 ≤ r < m` and `a ≡ r (mod m)`. The set `{0, 1, ..., m-1}` is a complete residue system modulo `m`.
    *   `Z/mZ` is equal to the set of equivalence classes `{[0]_m, [1]_m, ..., [m-1]_m}`.
    *   **Arithmetic Operations:** `[a]_m + [b]_m = [a+b]_m` and `[a]_m * [b]_m = [a*b]_m`.
    *   **Properties of Z/mZ Arithmetic:**
        *   Addition and multiplication are commutative and associative.
        *   `[0]_m` is the unique additive identity.
        *   Every `X ∈ Z/mZ` has a unique additive inverse `-X`.
        *   `[1]_m` is the unique multiplicative identity.
        *   `X * [0]_m = [0]_m`.
        *   Multiplication distributes over addition.
    *   An equivalence class `[a]_m` has a multiplicative inverse in `Z/mZ` if and only if `m` and `a` are relatively prime. If an inverse exists, it is unique.
    *   For positive integers `m, a` and `d = gcd(m,a)`, if `d` does not divide `b`, then the congruence `ax ≡ b (mod m)` has no integer solutions for `x`.
    *   For positive integers `n, m` and any integers `a, b`, `na ≡ nb (mod nm)` is equivalent to `a ≡ b (mod m)`.
    *   For relatively prime positive integers `m, n` and any integers `a, b`, `a ≡ b (mod mn)` is equivalent to `(a ≡ b (mod m) ∧ a ≡ b (mod n))`.
    *   `gcd(ab,c) = 1` if and only if `(gcd(a,c) = 1 ∧ gcd(b,c) = 1)`.
    *   **Chinese Remainder Theorem:** For relatively prime positive integers `m, n` and any integers `a, b`, there exists a unique integer `r` such that `1 ≤ r < mn`, `r ≡ a (mod m)`, and `r ≡ b (mod n)`.
3.  **Euler's Theorem and RSA:**
    *   **Euler's Phi Function:** `phi(m)` is the number of positive integers `a` (`1 ≤ a ≤ m`) such that `gcd(m,a) = 1`.
    *   For `X ∈ (Z/mZ)*`, its multiplicative inverse `X⁻¹` is also in `(Z/mZ)*`.
    *   For `X, Y ∈ (Z/mZ)*`, their product `X * Y` is also in `(Z/mZ)*`.
    *   **Euler's Theorem:** For any positive integer `m` and any `X ∈ (Z/mZ)*`, `X^phi(m) = [1]_m`. (Equivalently: `a^phi(m) ≡ 1 (mod m)` if `gcd(a,m)=1`).
    *   For any prime number `p`, `phi(p) = p-1`.
    *   For any prime `p` and positive integer `k`, `phi(p^k) = p^k - p^(k-1) = p^(k-1)(p-1)`.
    *   Euler's phi function is multiplicative: `phi(mn) = phi(m)phi(n)` for `gcd(m,n)=1`.
    *   For `m = p1^e1 * ... * pk^ek`, `phi(m) = p1^(e1-1)(p1-1) * ... * pk^(ek-1)(pk-1)`.
    *   **Fermat's Little Theorem:** If `p` is a prime number, then for every positive integer `a`, `a^p ≡ a (mod p)`.
    *   **RSA Key Generation:** Bob must choose two distinct prime numbers `p` and `q`; compute `n = pq`; compute `phi(n) = (p-1)(q-1)`; choose a positive integer `e` such that `e` is relatively prime to `phi(n)` and `e < phi(n)`; and compute a positive integer `d` such that `d < phi(n)` and `ed ≡ 1 (mod phi(n))`.
    *   The pair `(n,e)` is the public encryption key; `p, q, d` must be kept secret; `d` is the decryption key.
    *   An RSA message `m` must be a natural number less than `n`.
    *   To encrypt message `m`, Alice computes the unique `c < n` such that `[m]^e_n = [c]_n`. To decrypt `c`, Bob computes `[c]^d_n`.
    *   **RSA Core Property:** `[c]^d_n = [m]_n`.
    *   RSA security depends on the infeasibility of factoring large `n`. RSA implementations must use sufficiently large prime numbers.
    *   Probabilistic primality tests are not guaranteed to be accurate; they must be repeated multiple times to reduce error.
    *   Efficient exponentiation `X^a` (for large `a`) should use recursive formulas: if `a = 2k`, `X^a = (X^k)^2`; if `a = 2k+1`, `X^a = (X^k)^2 * X`.
    *   If `a^(n-1) <binary data, 1 bytes><binary data, 1 bytes> 1 (mod n)`, then `a` is a Fermat witness for `n`, and `n` is composite.
    *   If a Miller-Rabin witness exists for `n`, then `n` must not be prime. If `n` is prime, it passes; if `n` is composite, it will fail with probability at least `3/4`.

## VII. Cardinality and Infinite Sets (Properties & Usage)

1.  **Equinumerosity Properties:**
    *   Equinumerosity is reflexive (`A ~ A`), symmetric (`A ~ B → B ~ A`), and transitive (`A ~ B ∧ B ~ C → A ~ C`).
    *   If `A ~ B` and `C ~ D`, then `A × C ~ B × D`.
    *   If `A ~ B` and `C ~ D`, and `A` and `C` are disjoint, and `B` and `D` are disjoint, then `A ∪ C ~ B ∪ D`.
    *   **Cantor-Schroder-Bernstein Theorem:** If `A ≤ B` and `B ≤ A`, then `A ~ B`.
2.  **Countability and Uncountability:**
    *   The following statements for a set `A` are equivalent:
        *   `A` is countable.
        *   (`A` is the empty set OR there exists an onto function `f: Z+ → A`).
        *   There exists a one-to-one function `f: A → Z+`.
    *   The set of rational numbers `Q` is denumerable.
    *   The power set of positive integers `P(Z+)` is uncountable.
    *   The set of real numbers `R` is uncountable.
    *   For any set `A`, `A` is strictly dominated by `P(A)` (`A < P(A)`).
    *   The set of real numbers `R` is equinumerous with `P(Z+)`.
    *   **Continuum Hypothesis:** The conjecture that there is no set `X` such that `Z+ < X < R`.
3.  **Cardinality of Finite Sets:**
    *   If `A` and `B` are disjoint finite sets, `|A ∪ B| = |A| + |B|`.
    *   For a finite set `A` and subset `B`, `|A \ B| = |A| - |B|`.
    *   For finite sets `A` and `B`, `|A × B| = |A| * |B|`.
    *   For finite sets `A` and `B`, the cardinality of the set of all functions from `A` to `B` is `|B|^|A|`.
    *   For a set `A` with `|A|=n`, the number of bijections from `I_n` to `A` is `n!`.
    *   For a set `A` with `|A|=n`, the number of total orders on `A` is `n!`.
    *   For a finite set `A` with equivalence relation `R`, if all equivalence classes have cardinality `n`, then `|A/R| = |A|/n`.
    *   **Inclusion-Exclusion Principle:**
        *   `|A ∪ B| = |A| + |B| - |A ∩ B|`.
        *   `|A ∪ B ∪ C| = |A|+|B|+|C|-|A∩B|-|A∩C|-|B∩C|+|A∩B∩C|`.
4.  **Operations on Countable Sets:**
    *   If `A` and `B` are countable sets, then `A × B` must be countable.
    *   If `A` and `B` are countable sets, then `A ∪ B` must be countable.
    *   The union of a countable family of countable sets must be countable.
    *   If `A` is a countable set, then the set of all finite sequences of elements of `A` must also be countable.

## VIII. Proof Methodology and General Principles

1.  **Purpose and Correctness:**
    *   A proof must justify the claim that the conclusion follows from the hypotheses.
    *   For a theorem to be correct, its conclusion must be true for every instance where its hypotheses are true.
    *   A single counterexample (an instance where hypotheses are true but the conclusion is false) disproves a theorem.
2.  **Justification and Clarity:**
    *   All assertions in a proof must be completely justified by hypotheses or previously established conclusions.
    *   Clearly distinguish between assertions (claims of truth) and assumptions (statements taken as true for argument's sake) in a proof.
    *   Proofs should justify conclusions, not explain thought processes or how ideas were conceived.
    *   Proof by cases may not explicitly label each case, but the structure must still be clear.
3.  **Logical Analysis:**
    *   Discover the logical form of a statement by writing out definitions of mathematical terms or symbols within it.
    *   Limit logical analysis of givens and goals to what is necessary for determining the next proof step.
    *   For complex logical statements, writing them out in logical symbols is advisable for scratch work to clarify the proof direction.
    *   When analyzing complex mathematical statements, start by analyzing the "outermost" symbol.
4.  **Variable Management:**
    *   Variables must always be introduced and explained before they are used in a proof.
    *   When introducing a new variable, specify the type of object it represents (e.g., number, set, function).
    *   A variable cannot be defined in terms of another variable if the latter has not yet been introduced into the proof.
    *   When introducing an arbitrary variable for a `∀x P(x)` goal, it must be a new variable, and no assumptions about it other than its type/set should be made.
    *   When proving a statement of the form `∃x ∈ R∀y ∈ R(P(x,y))`, the variable `x` must be introduced into the proof before the variable `y`.
    *   When determining a specific value for an existentially quantified variable, algebraic manipulation of the predicate can be used to derive the necessary value (this reasoning should not appear in the final proof).
5.  **Proof Construction:**
    *   Any proof may be broken into cases at any time, provided the cases are exhaustive (cover all possibilities). Cases need not be exclusive (can overlap). Case analysis can be nested for complex conditions.
    *   When proving a conjunction (`P ∧ Q`), ensure that both `P` and `Q` are established separately.

## IX. Proof Strategies (Goals)

1.  **Goal `P → Q`:**
    *   **Method 1:** Assume `P` is true and then prove `Q`.
    *   **Method 2 (Contrapositive):** Assume `¬Q` is true and then prove `¬P`.
2.  **Goal `¬P`:**
    *   **Method 1 (Reexpression):** If possible, reexpress the goal in an equivalent positive form and use a strategy for that form.
    *   **Method 2 (Contradiction):** Assume `P` is true and derive a contradiction. Conclude `¬P` once a contradiction is reached.
3.  **Goal `∀x P(x)`:** Let `x` stand for an arbitrary object (a new variable), and prove `P(x)`. No assumptions about `x` other than its type should be made.
4.  **Goal `∃x P(x)`:** Find a specific value for `x` for which `P(x)` is true, state "Let x = (value)", and then prove `P(x)` for that specific `x`. `x` must be a new variable.
5.  **Goal `P ∧ Q`:** Prove `P` and `Q` separately.
6.  **Goal `P ↔ Q`:** Prove `P → Q` and `Q → P` separately. When using a string of equivalences, begin with justified equivalences leading to the conclusion `P ↔ Q`. Do not start the proof with `P ↔ Q` if it is not yet justified.
7.  **Goal `P V Q`:**
    *   **Method 1 (Cases):** Break the proof into cases. In each case, either prove `P` or prove `Q`.
    *   **Method 2 (`¬P → Q`):** Assume `¬P` is true and then prove `Q`. (Alternatively, assume `¬Q` and prove `P`).
8.  **Goal `∃!x P(x)` (Existence and Uniqueness):**
    *   Prove `∃x P(x)` (existence).
    *   Prove `∀y∀z((P(y) ∧ P(z)) → y = z)` (uniqueness) separately.
    *   Alternatively, prove `∃x (P(x) ∧ ∀y (P(y) → y = x))`.
9.  **Goal `x ∈ ⋃G`:** Find some set `A ∈ G` such that `x ∈ A`.
10. **Goal involving Absolute Value `|E|`:** Use cases based on the sign of the expression `E` (e.g., `E > 0`, `E < 0`).
11. **Goal involving Set Difference `x ∈ A \ C`:** Break the proof into cases depending on the inclusion or exclusion of an intermediate set (e.g., `x ∈ B` or `x ∉ B`).
12. **Goal of Uniqueness (general):** To prove the uniqueness of an object `y` satisfying a condition, assume there are two such objects (e.g., `y` and `z`) and demonstrate that they must be identical (`y = z`).

## X. Proof Strategies (Givens)

1.  **Given `¬P`:**
    *   If doing a proof by contradiction, proving `P` will result in a contradiction.
    *   If possible, reexpress this given in an equivalent positive form.
2.  **Given `P → Q`:**
    *   **Modus Ponens:** If `P` is also a given or proven, conclude `Q` is true.
    *   **Modus Tollens:** If `¬Q` is also a given or proven, conclude `¬P` is true.
    *   *Guidance:* Use immediately if `P` or `¬Q` is known; otherwise, wait until a relevant object appears.
3.  **Given `∃x P(x)` (Existential Instantiation):** Introduce a new variable (e.g., `x0`) to represent an object for which `P(x0)` is true, and assume `P(x0)` is true for the rest of the proof. The variable `x0` must be new to the proof.
    *   *Guidance:* Give the existing object a name immediately.
4.  **Given `∀x P(x)` (Universal Instantiation):** Plug in any relevant value (e.g., `a`) for `x` and conclude `P(a)` is true.
    *   *Guidance:* Wait until a likely value `a` pops up in the proof for which `P(a)` might be useful.
5.  **Given `P ∧ Q`:** Treat `P` and `Q` as separate givens.
6.  **Given `P ↔ Q`:** Treat `P → Q` and `Q → P` as separate givens.
7.  **Given `P V Q`:**
    *   **Proof by Cases:** Break the proof into cases: assume `P` is true in Case 1 and prove the goal; assume `Q` is true in Case 2 and prove the goal.
    *   **Disjunctive Syllogism:** If `¬P` is also a given or proven, conclude `Q` is true. If `¬Q` is also a given or proven, conclude `P` is true.
8.  **Given `∃!x P(x)`:** Treat it as two separate givens: `∃x P(x)` and `∀y∀z((P(y) ∧ P(z)) → y = z)`.
    *   For the `∃x P(x)` part, choose a new variable (e.g., `x0`) to represent the unique object for which `P(x0)` is true and assume `P(x0)`.
    *   For the uniqueness part, if two objects (`y`, `z`) are found such that `P(y)` and `P(z)` are true, conclude `y = z`.
9.  **Given `∀A ∈ F∀B ∈ G(A ⊆ B)`:** If `A ∈ F` and `B ∈ G` are encountered in the proof, you must conclude `A ⊆ B`.

## XI. Mathematical Induction and Recursion

1.  **Ordinary Induction:**
    *   To prove a statement `P(n)` for all natural numbers `n ≥ k`:
        *   **Base Case:** Prove `P(k)`. (The base case may start at any integer `k`, not necessarily `0`).
        *   **Induction Step:** Prove that for any natural number `n ≥ k`, if `P(n)` is true (the inductive hypothesis), then `P(n+1)` is also true.
2.  **Strong Induction:**
    *   To prove a statement `P(n)` for all natural numbers `n ≥ k`:
        *   Prove that for any natural number `n ≥ k`, if `P(j)` is true for all `j` such that `k ≤ j < n` (the inductive hypothesis), then `P(n)` is also true.
        *   A separate base case is not explicitly necessary (it's covered by the inductive hypothesis when `n=k`).
3.  **Fundamental Theorems/Identities (Example Applications):**
    *   **Division Algorithm:** For any natural numbers `n` and `m` (where `m > 0`), there exist unique natural numbers `q` and `r` such that `n = qm + r` and `r < m`.
    *   **Fundamental Theorem of Arithmetic:** Every integer `n > 1` is either prime or a unique product of two or more primes.
    *   **Well-ordering Principle:** Every nonempty set of natural numbers must have a smallest element.

## XII. Cautions and Best Practices

1.  **Rigour and Justification:**
    *   Never accept a mathematical rule as correct without a proof, even if examples suggest it.
    *   Stating that a proof is "similar" to another does not constitute a proof; the details must still be verifiable.
    *   Do not let informal reasoning convince you; always reformulate it as a formal proof.
    *   Do not assume common sense or intuitive understanding is sufficient for a proof; precise application of logical laws is required.
2.  **Precision and Clarity:**
    *   Do not confuse a conditional statement (`P → Q`) with its converse (`Q → P`).
    *   Never interpret an "if-then" statement in mathematics as a biconditional statement.
    *   Do not blur the distinction between "if" (conditional) and "iff" (biconditional) in mathematics.
    *   When specifying "two different objects," explicitly state that they are not equal (e.g., `y ≠ z`).
    *   Do not assume that `x` and `y` are distinct unless explicitly stated.
    *   In proofs, avoid using logical symbols (`Λ`, `V`, `¬`, `→`, `↔`, `∀`, `∃`) in the final write-up as much as possible, sticking to ordinary English. However, they are useful in scratch work.
3.  **Preconditions and Assumptions:**
    *   Ensure any expression used as a divisor is explicitly known to be non-zero.
    *   When representing an odd integer in a proof, it must be expressed in the form `2j + 1` for some integer `j`.
    *   Pay attention to free and bound variables when translating between English and symbolic logic; all variables that are not free in the English statement must be bound in the symbolic form.

## Key Highlights

* All assertions in a proof must be completely justified by hypotheses or previously established conclusions; never accept a mathematical rule without proof or assume common sense is sufficient.
* The negation symbol (`¬`) and quantifiers (`∀x`, `∃x`) must apply only to the statement immediately following them to maintain clarity and prevent ambiguity.
* When interpreting logical statements, remember that the order of mixed quantifiers (`∀x∃y` vs. `∃y∀x`) can change the meaning of a statement, unlike universal or existential quantifiers alone.
* Variables must always be introduced and explained before they are used in a proof, specifying the type of object they represent.
* To prove a conditional statement (`P → Q`), assume `P` is true and then prove `Q`; for `¬P`, a common strategy is to assume `P` is true and derive a contradiction.
* When a statement `∃x P(x)` is given, introduce a new variable (e.g., `x0`) to represent an object for which `P(x0)` is true, and assume `P(x0)` for the remainder of the proof.
* To prove a statement `P(n)` for all natural numbers `n ≥ k` using ordinary induction, establish a base case by proving `P(k)` and an induction step by proving that `P(n)` implies `P(n+1)` for `n ≥ k`.
* Do not confuse a conditional statement (`P → Q`) with its converse (`Q → P`), and always distinguish precisely between 'if' (conditional) and 'iff' (biconditional) in mathematical contexts.

## Insightful Ideas

* Develop an automated grammar or linter for mathematical expressions and proofs based on Section I (Syntax and Notation) to enforce structural correctness.
* Conduct a comprehensive cross-sectional consistency and completeness review of all defined rules and properties to identify any ambiguities or potential contradictions across different mathematical domains.
* Create a curated set of illustrative examples and common error cases for each major section (e.g., quantifier scope, relation types, function properties) to enhance clarity and aid practical application.
* Investigate the feasibility of translating these distilled rules and definitions into a machine-readable format suitable for integration with formal proof assistants or automated theorem provers.
