# Rules for MMIX Architecture, Algorithms, and Advanced Computing Concepts

This document presents a consolidated, de-duplicated, and categorized master list of technical rules, constraints, and operational guidelines, synthesized from various segments of the original documentation.

**Generated on:** October 27, 2025 at 4:21 PM CDT

---

## I. General Mathematical Principles

1.  **Equivalence Relations:** An equivalence relation on a set `S` must satisfy transitivity, symmetry, and reflexivity, and must partition its set `S` into disjoint equivalence classes.
2.  **Linear Ordering:** An ordering relation "<" on key values `a`, `b`, `c` must satisfy the law of trichotomy (exactly one of `a < b`, `a = b`, `b < a` is true) and the law of transitivity (if `a < b` and `b < c`, then `a < c`).
3.  **Algebraic Systems:**
    *   A coefficient system `S` must be a commutative ring with identity.
    *   In a field `S`, exact division must be possible for any `u, v` in `S` where `v ≠ 0`; there must be an element `w` in `S` such that `u = vw`.
    *   A unit must be an element `u` such that `uv = 1` for some `v` in `S`.
    *   A prime `p` must be a nonunit element such that `p = qr` implies either `q` or `r` is a unit.
    *   A Unique Factorization Domain (UFD) `S` must be a commutative ring with identity where, for any nonzero `u, v` in `S`, `uv` must not be zero.
    *   Every nonzero element `u` of a UFD `S` must either be a unit or have a unique representation as a product of primes `u = p_1 ... p_t` (`t >= 1`), unique except for unit multiples and factor order.
4.  **Entropy:** Entropy `H` is defined as the sum of `pk * lg(1/pk)`. If `pk = 0`, then `pk * lg(1/pk)` must be defined as 0.
5.  **Torus Algebra:**
    *   When applying Theorem W, the moduli of the discrete torus `T(m_1, ..., m_n)` must be sorted non-decreasingly (`m_1 ≤ ... ≤ m_n`).
    *   For an n-dimensional torus `T(m_1, ..., m_n)`, integer vector elements `x = (x_1, ..., x_n)` must satisfy `0 ≤ x_1 < m_1, ..., 0 ≤ x_n < m_n`.
    *   Vector sum `(x + y)` must be calculated as `((x_1 + y_1) mod m_1, ..., (x_n + y_n) mod m_n)`.
    *   Vector difference `(x - y)` must be calculated as `((x_1 - y_1) mod m_1, ..., (x_n - y_n) mod m_n)`.
    *   The cross order `(x < y)` for vectors must be defined such that `v(x) < v(y)` OR (`v(x) = v(y)` AND `x > y` lexicographically).
    *   The complement of a vector `x = (x_1, ..., x_n)` in `T(m_1, ..., m_n)` must be `(m_1 - 1 - x_1, ..., m_n - 1 - x_n)`.
    *   The sets `S` used in equation (83) must be standard in the `(n-1)`-dimensional torus `T'(m_1, ..., m_k-1, m_k+1, ..., m_n)`.
    *   When representing multicombinations of `U={s₀·0, ..., s_d·d}` as points in `T(m_1, ..., m_n)`, `n` must be `d+1`, `m_j` must be `s_n-j + 1`, and `x_j` must represent the number of occurrences of `n-j`.

## II. Naming & Notation Conventions

1.  **General Naming:**
    *   Small named constants and offsets of fields within records (e.g., `FACEUP`, `NEXT`, `TAG`) and symbols for plain values must use all uppercase names.
    *   Addresses must be associated with names that start with an uppercase letter and continue with uppercase or lowercase letters (e.g., `TOP OCTA 1F`, `Main SET i, 0`).
    *   Names for registers must use only lowercase letters (e.g., `x`, `t`, `new`).
    *   The special register for temporary variables must be named `t`.
2.  **Mathematical Notation & Symbols:**
    *   The base `b` subscript must be omitted in positional notation when `b = 10`.
    *   In the standard hexadecimal system, digits 10 through 15 must be denoted by `a` through `f` (or `A` through `F`).
    *   Floating point addition must use `⊕`, subtraction `⊖`, multiplication `⊗`, and division `⊘`.
    *   In tree nodes, unary negation must be labeled "neg".
    *   Bracket notation `[A]` must be used such that `[A] = 1` if event `A` is true, and `[A] = 0` otherwise.
    *   `P_N` must denote the `N` lexicographically smallest combinations `c_1 ... c_t` satisfying condition (3). `Q_N` must denote the `N` lexicographically largest combinations.
    *   `P_N'` must denote the `N` lexicographically smallest multicombinations `d_1 ... d_t` satisfying condition (6). `Q_N'` must denote the `N` lexicographically largest multicombinations.
    *   When referring to random variables, uppercase letters should typically be used. When referring to values that random variables might assume, lowercase letters should typically be used.
    *   The number sign (`#`) must be used to indicate 5-letter English words or hexadecimal constants (e.g., `#coffee`).
    *   Logical equivalence must be denoted by `<=:`.
    *   The empty set must be denoted by `0`.
    *   The null link must be denoted by `Λ`.
    *   The "1s count" (sum of binary digits) must be denoted by `v_x`.
    *   The ruler function must be denoted by `p_n`.
    *   The median function must be denoted by `(xyz)`.
    *   The monus operation (`max{0, x-y}`) must be denoted by `x . y`.
    *   The if-then-else operation must be denoted by `u ? v : w`.
    *   Bitwise AND operations must use `x & y`.
    *   Bitwise OR operations must use `x | y`.
    *   Bitwise XOR operations must use `x ^ y`.
    *   0-origin indexing must be employed.

## III. MMIX Architecture & Programming Model

1.  **Core Behavior:**
    *   MMIX deals only with two's complement binary arithmetic.
    *   Unsigned arithmetic operations never cause overflow.
    *   Result of addition and multiplication is usually given modulo the word size (`w`).
    *   `MULU` instruction delivers a 128-bit result (high bits in `rH`).
    *   `DIVU` instruction requires the dividend in `rD` to be less than the divisor (`v_l`) for proper quotient/remainder calculation.
    *   `DIV t,y,m` instruction computes `y mod m` into register `rR`.
2.  **Memory & Addressing:**
    *   An OCTA must start at an address that is a multiple of 8.
    *   A TETRA must start at an address that is a multiple of 4.
    *   A WYDE must start at an even address.
    *   MMIX absolute addresses must always require eight bytes in memory.
    *   MMIX relative addresses can be stored using four, two, or one byte.
    *   MMIX load and store instructions must ignore the low-order bits of an address when those bits are used as tags.
    *   Before MMIX can work with the address of a top card (or similar reference), it needs to load this address into a register.
3.  **Registers:**
    *   Register `$255` must be used as the parameter register for `TRIP` and `TRAP` instructions.
    *   A function's principal return value must be in register `$0` just before the final `POP` instruction.
    *   At the start of a subroutine, the special register `rJ` contains the return address for the `POP` instruction.
    *   Avoid using aliases for register `$255` when it serves as a parameter to `TRAP` or `TRIP`.
    4.  Identify register `$0` by its number when it is used for a function's return value.
4.  **Instruction Usage:**
    *   An `INCL` instruction can be used instead of `ADDU` if the constant `c < 2^16`.
    *   `CSN` instruction for subtraction will not work with negative constants.
    *   `DIVU` instruction requires `rD` to form a 128-bit dividend.
    *   When multiplying by 10, use `4ADDU u,u,u; SL u,u,1` for efficiency.
    *   `LDBU` instruction extracts the next digit from the key in radix list sort.
    *   `ZSN` instruction computes the offset of the next link in binary tree search.
    *   `ZSN` instruction computes `LINK(a)` from `a != 0` in balanced tree search.

## IV. Numeric Representation & General Arithmetic

1.  **Numeric Representation Principles:**
    *   All numbers dealt with are generally assumed to be nonnegative to simplify exposition; sign handling is a separate concern.
    *   Arithmetic algorithms must support integers expressed in radix `b` notation, where `b` is an integer `2` or greater.
    *   An "n-place integer" means any nonnegative integer less than `b^n`. Such numbers must be written using at most `n` "places" in radix `b` notation.
    *   Positional notation to base `b` must be defined as `... + a_3 * b^3 + a_2 * b^2 + a_1 * b^1 + a_0 + a_-1 * b^-1 + a_-2 * b^-2 + ...`.
    *   For standard b-ary number systems, the base `b` must be an integer greater than 1, and digits `a` must be integers in the range `0 <= a < b`.
    *   For simple mixed-radix integer systems, each base `b_n` must be an integer greater than one, and each digit `a_n` must be an integer in the range `0 <= a_n < b_n`.
2.  **Special Radix Systems:**
    *   In the negadecimal (base -10) system, digits `a_j` must be integers in the range `0 <= a_j <= 9`.
    *   In the quater-imaginary system (base 2i), digits must be `0, 1, 2, 3`.
    *   In balanced ternary notation, digits ("trits") must be -1, 0, or +1.
3.  **Complement Notation:**
    *   For two's complement and one's complement notations, the radix `b` should be one half of the computer's word size (e.g., `b = 2^31` for a 32-bit word).
    *   The sign bit of all but the most significant word of a multiple-precision number must be zero.
    *   All but the most significant word of a multiple-precision number must be considered nonnegative.
    *   When one's complement notation is used, special attention must be given to the leftmost carry; it must be added into the least significant word and possibly propagated further to the left.
    *   Multiplication and division of signed numbers are most easily done by converting operands to nonnegative quantities via complementation operations beforehand.
4.  **Modular Arithmetic:**
    *   When computing `(u_j + v_j) mod m_j`, `(u_j - v_j) mod m_j`, and `u_j v_j mod m_j`, `0 <= u_j, v_j < m_j` must hold.
    *   For modulo `2^e - 1` operations, `0 <= u_j < 2^e` is allowed (meaning `u_j = m_j = 2^e - 1` is an alternative to `u_j = 0`).
    *   Modular addition modulo `2^e - 1`: `u_j (+) v_j = ((u_j + v_j) mod 2^e) + [u_j + v_j >= 2^e]`.
    *   Modular multiplication modulo `2^e - 1`: `u_j (*) v_j = ((u_j v_j) mod 2^e) + [u_j v_j / 2^e]`.
    *   Modular subtraction modulo `2^e - 1`: `u_j (-) v_j = (u_j - v_j) mod 2^e - [u_j < v_j]`.
    *   When moduli `m_1, ..., m_r` are odd, integers are conveniently represented in the range `-m/2 < u < m/2`.
    *   For modular addition `u+v` where `0 < u, v < m`, overflow occurs if and only if the sum is less than `u`.
    *   For `(aX) mod (w-1)` calculation, `0` and `w-1` must be treated as equivalent in input and output.
5.  **Radix Conversion:**
    *   For integer conversion from radix `b` to `B`: The least significant digit `U_0` must be `u mod B`, and the next digit `U_1` must be `[u/B] mod B`. The process must stop when `[... [[u/B]/B] ... /B] = 0`.
    *   For fractional conversion from radix `b` to `B`: The most significant fractional digit `U_-1` must be `[uB]`, and the next digit `U_-2` must be `[{uB}B]`. If rounding to `M` places is desired, computation must stop after `U_-M` is calculated, and `U_-M` should be increased by unity if `{{... {{uB}B} ... B}` is greater than `0.5`.
    *   Binary-Coded Decimal (BCD) doubling requires specific bitwise operations (add 5, extract high bit, shift right 2 and subtract, add original number) performed on each digit.
    *   Conversion to modular representation can be done by dividing `u` by `m_1, ..., m_r` and saving remainders, or by evaluating `(... ((u_t b + u_t-1) b + ...) b + u_0)` using modular arithmetic.
    *   If `b = 2` and `m_j = 2^e - 1` for modular conversion, binary bits of `u` can be grouped into `e_j`-bit blocks `a_k`, then `u = a_0 + a_1 + ... + a_p (modulo 2^e - 1)`.
    *   Conversion from modular to positional representation must use constants `c_ij` (where `c_ij m_i = 1 (modulo m_j)`) for computational efficiency.
    *   For magnitude comparison in mixed-radix systems, if `0 < u < m` and `0 < u' < m`, `u < u'` can be determined by comparing `v_r` and `v'_r`, or if equal, `v_r-1` and `v'_r-1`, etc., according to lexicographic order.
6.  **Multi-Precision Arithmetic (General):**
    *   Arrays are assumed to be in `little-endian` order. `b = 2^64`, so each digit `u_i` fits in one octabyte.
    *   `Program A` (Additive Number Generator) for `k`-bit words: uses global registers `j = 8i`, `k = 8k`, and `y = LOC(Y[1]) - 8`. Global register `a` is a `λ`-bit binary constant `(a1 ... a_λ)` shifted left by `64-k` bits.

## V. Floating Point Arithmetic

1.  **Representation Details:**
    *   MMIX floating point numbers use base `b=2`, excess `e=1023`, and `p=53` bits of precision.
    *   The floating point sign bit is the leftmost bit (1 for negative, 0 otherwise).
    *   The floating point exponent `e` is stored in 11 bits, in the range `0 < e < 2047`.
    *   The floating point fraction part `f'` is 52 bits, `0 < f' < 2^52`, with `f = 1 + f'/2^52`.
    *   A floating point number is normalized if `0 < e < 2047` and the most significant digit of `f` is nonzero (`1 <= f < 2`).
    *   A floating point number represents `0.0` if `f=e=0`.
    *   For radix 16 floating-point numbers, normalization allows for up to three leading zero bits in the fraction part of a positive normalized number.
    *   Double-precision floating point numbers use 128 bits: 2 bytes for sign/exponent, 14 bytes for the fraction part. Double-precision numbers use base `b=2`, excess `e = 2^14 - 1 = 16383`, and precision `p=113`.
2.  **General Floating Point Routine Design:**
    *   Floating point routine inputs and outputs must be normalized.
    *   Floating point operations must implement `round(true_operation(operands))`.
    *   Floating point addition `u ⊕ v` must implement `round(u + v)`.
    *   Do not check the size of `e_w` for exponent underflow or overflow until after rounding and normalization.
    *   Test for exponent underflow and overflow for every floating point operation (addition, subtraction, multiplication, division).
    *   Retain the appropriate number of significant digits throughout floating point computations, as specified in Algorithms A and M.
    *   Normalizing floating point routines must always deliver a properly rounded result to the maximum possible accuracy.
    *   For unnormalized floating point addition/subtraction, follow Algorithm 4.2.1A, but suppress all left scaling.
    *   For unnormalized floating point multiplication/division, follow Algorithm 4.2.1M, but scale the answer to have precisely `max(l_u, l_v)` leading zeros.
3.  **Rounding Rules (Algorithm N):**
    *   The rounding function must satisfy `round(-x) = -round(x)`.
    *   The rounding function must satisfy `x < y` implies `round(x) <= round(y)`.
    *   The rounding function must satisfy `round(b * x) = b * round(x)` when `b` is the floating point radix.
    *   When rounding `f` to `p` places, `f` must be changed to the nearest multiple of `b^(-p)`.
    *   When rounding `f` to `p` places and `b` is even, if `b^p * f` is exactly midway between two integers, `f` must be changed to the nearest multiple `f'` of `b^(-p)` such that `(b^p * f') + 1` is odd.
    *   When an ambiguous value is rounded, make the least significant digit even (or odd).
    *   For even radices `b`: if `b/2` is odd, round to even; if `b/2` is even, round to odd.
    *   Avoid premature rounding in floating point calculations; do not round during the scaling-right operation (Algorithm A, step A5), except as specified by exercise 5.
    *   The choice of tie-breaking rule for rounding does not affect the validity of Theorems A, B, and C.
4.  **Normalization Process (Algorithm N):**
    *   Algorithm N input `f` must satisfy `|f| < b`.
    *   If `|f| > 1`, proceed to step N4.
    *   If `f = 0`, set `e` to its lowest possible value.
    *   If `|f| >= 1/b`, proceed to step N5.
    *   If `|f| < 1/b`, shift `f` left by one digit (multiply by `b`) and decrease `e` by 1.
    *   When scaling floating point numbers to the left, only introduce zeros at the rightmost positions.
    *   If `|f| > 1` (fraction overflow) or after rounding overflow, shift `f` right by one digit (divide by `b`) and increase `e` by 1.
    *   Rounding can cause `|f| = 1` ("rounding overflow"), in which case Algorithm N must return to step N4.
    *   `e` and `f` must be packed into the output representation.
5.  **Floating Point Error Handling:**
    *   Sense an exponent overflow condition if `e` is greater than its allowed range.
    *   Sense an exponent underflow condition if `e` is smaller than its allowed range.
    *   Ensure the sign is preserved when minus zero is present.
    *   Retain sufficient information to allow meaningful corrective actions after exponent overflow or underflow.
    *   Setting underflowed floating point results to zero is only appropriate when the result is to be added to a significantly larger quantity.
    *   Report exponent underflow to the programmer.
    *   When an unnormalized floating point calculation yields zero, an unnormalized zero must be given as the answer.
6.  **Floating Point Comparison:**
    *   `u` is "definitely less than" `v` (`u < v (ε)`) if `u < v − ε max(b^(e_u−q), b^(e_v−q))`.
    *   `u` is "approximately equal to" `v` (`u ~ v (ε)`) if `|u − v| < ε max(b^(e_u−q), b^(e_v−q))`.
    *   `u` is "definitely greater than" `v` (`u > v (ε)`) if `u > v + ε max(b^(e_u−q), b^(e_v−q))`.
    *   `u` is "essentially equal to" `v` (`u ≈ v (ε)`) if `|u − v| < ε min(b^(e_u−q), b^(e_v−q))`.
    *   For any `u,v`, exactly one of `u < v (ε)`, `u ~ v (ε)`, or `u > v (ε)` must hold.
7.  **Floating Point Algebraic Laws:**
    *   Floating point addition must be commutative (`u ⊕ v = v ⊕ u`).
    *   Floating point subtraction must be equivalent to `u ⊕ (−v)` (`u ⊖ v = u ⊕ (−v)`).
    *   Negation of a floating point number must satisfy `−(−u) = u`.
    *   Floating point addition `u ⊕ v = 0` if and only if `v = −u`.
    *   Floating point addition of zero must satisfy `u ⊕ 0 = u`.
    *   Floating point multiplication by zero must be commutative (`u ⊗ 0 = 0 ⊗ u`).
    *   Floating point multiplication must satisfy `(−u) ⊗ v = −(u ⊗ v)`.
    *   Floating point multiplication `u ⊗ v = 0` if and only if `u = 0` or `v = 0`.
    *   Floating point division must satisfy `(u ⊘ v) = u ⊗ (1 ⊘ v) = −(u ⊘ (−v))`.
    *   Floating point division of zero by `v` must be `0` (for `v != 0`).
    *   Floating point division by one must satisfy `u ⊘ 1 = u`.
    *   Floating point division of `u` by itself must be `1` (for `u != 0`).
    *   Floating point multiplication and division by a positive number must preserve order (`u < v` and `w > 0` implies `u ⊗ w < v ⊗ w` and `u ⊘ w < v ⊘ w`).
    *   Floating point division of `w` by `u` or `v` must preserve order (`w > 0` and `v > u > 0` implies `w ⊘ u > w ⊘ v`).
    *   If floating point addition `u ⊕ v` is exact, then `(u ⊕ v) ⊖ v = u`.
    *   If floating point multiplication `u ⊗ v` is exact and non-zero, then `(u ⊗ v) ⊘ v = u`.

## VI. Polynomial Arithmetic

1.  **Polynomial Definitions:**
    *   Polynomials are defined as either a constant or a sum `sum(g_j * z^e_j)` with specified constraints.
    *   The degree of the zero polynomial `deg(0)` must be defined as `-infinity`.
    *   The leading coefficient of the zero polynomial `lc(0)` must be defined as `0`.
    *   A polynomial `u(x)` is monic if its leading coefficient `lc(u)` is `1`.
    *   A polynomial that is prime in its domain must be called an irreducible polynomial.
    *   A polynomial over a UFD is primitive if its coefficients are relatively prime.
    *   For any nonzero polynomial `u(x)`, `cont(u)` (content of `u`) must be an element of `S`, and `pp(u(x))` (primitive part of `u(x))`) must be a primitive polynomial over `S`, such that `u(x) = cont(u) * pp(u(x))`.
    *   If `u(x) = 0`, `cont(u)` and `pp(u(x))` must be defined as `0`.
    *   The notation `u(x) mod v(x)` shall be used for the remainder `r(x)` in polynomial division.
    *   The greatest common divisor (GCD) of polynomials is a set of unit multiples, not a single unique value.
2.  **Polynomial Operations:**
    *   For polynomial multiplication, `w_k` must be `u_k v_0 + u_k-1 v_1 + ... + u_1 v_k-1 + u_0 v_k`. `u_i` or `v_j` must be treated as zero if `i` is greater than the degree of `u` or `j` is greater than the degree of `v`, respectively.
    *   Multivariate polynomials over the integers or any field must be uniquely factored into irreducible polynomials.
3.  **Polynomial Division:**
    *   Given polynomials `u(x)` and `v(x)` over a field, `v(x)` must not be zero.
    *   Polynomial division must yield a quotient `q(x)` and a remainder `r(x)` such that `u(x) = q(x)v(x) + r(x)`.
    *   The remainder polynomial `r(x)` must satisfy `deg(r) < deg(v)`.
    *   For a given `u(x)` and `v(x)`, at most one pair of polynomials `(q(x), r(x))` can satisfy the division relations.
    *   **Algorithm D (Division of Polynomials over a Field):** Input polynomials `u(x)` and `v(x)` must be over a field `S`. The leading coefficient `v_n` of `v(x)` must not be zero. The degree `m` of `u(x)` must be greater than or equal to the degree `n` of `v(x)`, and `n` must be non-negative (`m >= n >= 0`). The algorithm terminates after iterating `k` from `m-n` down to `0`. `q_k` must be set to `u_m+k / v_n`. `u_j` must be updated by `u_j - q_k v_j` for `j` from `n+k-1` down to `k`. If `v(x)` is a monic polynomial (i.e., `v_n = 1`), no explicit division of coefficients is performed.
    *   **Algorithm R (Pseudo-division of Polynomials):** Input polynomials `u(x)` and `v(x)` must have `v_n ≠ 0` and `m ≥ n ≥ 0`. Iteration in step R1 must be for `k = m-n, m-n-1, ..., 0`. Coefficients `v_-1, v_-2, ...` must be treated as zero. Polynomials `g(x)` and `r(x)` found by pseudo-division over a UFD must be unique. To perform pseudo-division over a UFD, one may multiply `u(x)` by `v_n^(m-n+1)` and apply Algorithm D.
4.  **Unique Factorization Domains (UFDs) - Polynomials:**
    *   Any field is a Unique Factorization Domain, where each nonzero element is a unit and there are no primes. The integers form a Unique Factorization Domain, with units `+1` and `-1`, and primes `±2, ±3, ±5, ±7, ±11`, etc. Polynomials over a Unique Factorization Domain must form a Unique Factorization Domain.
    *   The product of primitive polynomials over a UFD must be primitive (Gauss's Lemma).
    *   Any nonzero polynomial `u(x)` over a UFD `S` must be factorable as `u(x) = c * v(x)`, where `c` is in `S` and `v(x)` is primitive.
    *   If `u = c_1 * v_1(x) = c_2 * v_2(x)`, then `c_1` must be `alpha * c_2` and `v_1(x)` must be `alpha * v_2(x)` for some unit `alpha` in `S`.
    *   The content and primitive part of polynomials must satisfy `cont(uv) = a * cont(u) * cont(v)` and `pp(u(x)v(x)) = b * pp(u(x)) * pp(v(x))`, where `a` and `b` are units, and `a*b = 1`.
    *   Conventionally, for polynomials over the integers, `pp(u(x))` should be defined so its leading coefficient is positive; in this case, `a = b = 1`.
    *   Conventionally, for polynomials over a field, `cont(u)` may be taken as `lc(u)`, so `pp(u(x))` is monic; in this case, `a = b = 1`.
    *   When factoring polynomials over the integers, one must first divide by the greatest common divisor of coefficients to obtain a primitive polynomial.
    *   When factoring polynomials over the integers, `u(x)` must be squarefree; this is achieved by dividing out `gcd(u(x), u'(x))`.
    *   If `|u_0| < |u_n|`, it is preferable to perform factorization on the reverse polynomial `x^n * u(1/x)`.
5.  **Polynomial Greatest Common Divisor (GCD):**
    *   The leading coefficient of any common divisor of `u(x)` and `v(x)` must be a divisor of `gcd(lc(u), lc(v))`.
    *   `cont(gcd(u,v)) = a * gcd(cont(u), cont(v))` for some unit `a`.
    *   **Euclid's Algorithm for Polynomials over a Field:** If `v(x) = 0`, then `gcd(u(x), v(x))` is `u(x)`. Otherwise, `gcd(u(x), v(x))` is `gcd(v(x), r(x))`, where `r(x)` is the remainder from `u(x) = q(x) v(x) + r(x)`. The result of Euclid's algorithm should be divided by its leading coefficient to produce a monic polynomial. If `deg(v) = 0`, then `gcd(u(x), v(x))` must be `1`.
    *   **Algorithm E (Generalized Euclidean Algorithm):** Input polynomials `u(x)` and `v(x)` must be nonzero and over a UFD `S`. Auxiliary algorithms must exist to calculate greatest common divisors of elements of `S` and to divide `a` by `b` in `S` when `b ≠ 0` and `a` is a multiple of `b`. `cont(u)` must be a greatest common divisor of the coefficients of `u(x)`. In step E1, `u(x)` must be replaced by `pp(u(x))`, and `v(x)` by `pp(v(x))`. If `r(x) = 0` in step E2, the algorithm must proceed to E4. If `deg(r) = 0` in step E2, `v(x)` must be replaced by the constant polynomial "1", and the algorithm must proceed to E4. In step E3, `u(x)` must be replaced by `v(x)`, and `v(x)` by `pp(r(x))`. Algorithm E must terminate by returning `d * v(x)` as the answer. For primitive polynomials `u(x)` and `v(x)`, `gcd(u(x), v(x))` must equal `gcd(v(x), pp(r(x)))`, where `r(x)` is the pseudo-remainder of `u(x)` by `v(x)`.
    *   **Algorithm C (GCD over UFD - Subresultant Algorithm):** Algorithm C shares the same input and output assumptions as Algorithm E. In step C1, `d` must be set to `gcd(cont(u), cont(v))`, and `(u(x), v(x))` must be replaced by `(pp(u(x)), pp(v(x)))`. If `r(x) = 0` in step C2, the algorithm must proceed to C4. If `deg(r) = 0` in step C2, `v(x)` must be replaced by the constant polynomial "1", and the algorithm must proceed to C4. In step C3, `u(x)` must be replaced by `v(x)`. `v(x)` must be replaced by `r(x) / (g * h^delta)`. At the beginning of step C3, all coefficients of `r(x)` must be multiples of `g * h^delta`. In step C3, `g` must be set to `lc(u)`. `h` must be set to `h^(delta + 1)`. Algorithm C must return `d * pp(v(x))` as the answer.
6.  **Polynomial Factoring Modulo p:**
    *   If `gcd(u(x), u'(x)) ≠ 1`, the problem of factoring `u(x)` must be reduced. If `d(x) = gcd(u(x), u'(x))` is equal to 1, then `u(x)` is squarefree. If `d(x)` is not 1 and not `u(x)`, then `d(x)` is a proper factor of `u(x)`. If `d(x) = u(x)`, then `u'(x)` must be 0.
    *   If `u'(x) = 0`, then the coefficient `u_k` of `x^k` must be nonzero only when `k` is a multiple of `p`. If `u(x)` can be written as `v(x^p)`, then `u(x) = (v(x))^p`. For any polynomials `v_1(x)` and `v_2(x)` modulo `p`, `(v_1(x) + v_2(x))^p = v_1(x)^p + v_2(x)^p`. The identity `x^p - x = (x-0)(x-1)...(x-(p-1)) (modulo p)` must hold.
    *   If `v(x)` satisfies `v(x)^p = v(x) (modulo u(x))` and `deg(v) < deg(u)`, then `u(x)` must divide `(v(x)-0)(v(x)-1)...(v(x)-(p-1))`. All solutions to `v(x)^p = v(x) (modulo u(x))` with `deg(v) < deg(u)` must have the form `v(x) = s_1 (modulo p_1(x)), ..., v(x) = s_r (modulo p_r(x))`. `u(x) = product_0<=s<p gcd(v(x) - s, u(x))` must hold whenever `v(x)` satisfies `v(x)^p = v(x) (modulo u(x))`.
    *   **Algorithm B (Berlekamp's Factoring Algorithm):** Step B1 must ensure that `u(x)` is squarefree.
    *   **Algorithm D (Distinct-degree factorization):** Algorithm D1 must rule out squared factors. Algorithm D1 must initialize `v(x)` to `u(x)`, `w(x)` to `x`, and `d` to 0. The procedure must terminate if `d+1 > deg(v)/2`. Otherwise, `d` must be increased by 1, and `w(x)` must be replaced by `w(x)^p mod v(x)`. `g_d(x)` must be `gcd(w(x) - x, v(x))`. If `g_d(x) ≠ 1`, `v(x)` must be replaced by `v(x) / g_d(x)`. If `g_d(x) ≠ 1`, `w(x)` must be replaced by `w(x) mod v(x)`.
    *   **Algorithm F (Factoring modulo a prime power):** The prime power `p^e` must be sufficiently large. The factorization `u(x) = v_1(x) ... v_r(x) (modulo p^e)` must be squarefree, and the factors `v_i(x)` must be monic. For every combination of `d` factors `v(x) = v_i1(x) ... v_id(x)`, the unique polynomial `v'(x) = lc(u)v(x) (modulo p^e)` whose coefficients lie in `[-p^e/2, p^e/2)` must be formed. If `v'(x)` divides `lc(u)u(x)`, then `pp(v'(x))` must be output as a factor. If `v'(x)` divides `lc(u)u(x)`, then `u(x)` must be divided by `pp(v'(x))`, and the corresponding `v_i(x)` removed from the list of factors modulo `p^e`. The algorithm must loop on `d` until `d >= r/2`. The final `u(x)` must be the final irreducible factor of the original polynomial.

## VII. Graph & Hypergraph Theory

1.  **Graph Definitions & Properties (General):**
    *   A graph `G` consists of a set `V` of vertices and a set `E` of edges, which are pairs of distinct vertices. `V` and `E` are assumed to be finite sets unless otherwise specified.
    *   `u — v` denotes that `u` and `v` are vertices with `{u,v} ∈ E`. `u — v` if and only if `v — u`. No vertex is adjacent to itself (`v != v` for all `v ∈ V`).
    *   A multigraph `(V, E)` allows `E` to be a multiset of pairs `{u,v}`, including loops `v — v` (multipairs `{v,v}`). Each loop `v — v` contributes `2` to the degree of its vertex.
    *   `G' = (V', E')` is a subgraph of `G = (V, E)` if `V' ⊆ V` and `E' ⊆ E`.
    *   `G'` is a spanning subgraph of `G` if `V' = V`.
    *   `G'` is an induced subgraph of `G` (denoted `G'|V'`) if `V' ⊆ V` and `E'` contains all edges `{u,v}` from `E` where `u,v ∈ V'`. `G\v` abbreviates `G|(V \ {v})`. `G\e` denotes `(V, E \ {e})`.
    *   A graph with `n` vertices and `e` edges has order `n` and size `e`.
    *   A cycle graph `C_n` is a graph only when `n > 3` (for `n=1,2`, it's a multigraph).
    *   `G` and `G'` are isomorphic if a one-to-one correspondence `φ` from `V` to `V'` exists such that `u — v` in `G` iff `φ(u) — φ(v)` in `G'`.
    *   Lines in a graph diagram are allowed to cross at non-vertex points. A graph is planar if it can be drawn without any edge crossings.
    *   The degree of a vertex is its number of neighbors. A graph is regular if all vertices have the same degree.
    *   An automorphism of `G` is a permutation `φ` of its vertices that preserves adjacency (`φ(u) — φ(v)` whenever `u — v` in `G`).
    *   A spanning path `P_n` is a Hamiltonian path. A spanning cycle `C_n` is a Hamiltonian cycle. A graph is Hamiltonian if it has a Hamiltonian cycle.
    *   The girth is the length of its shortest cycle; it is infinite if the graph is acyclic.
    *   `d(u,v)` is the minimum path length from `u` to `v`. `d(v,v) = 0`, `d(u,v) = d(v,u)`. The triangle inequality `d(u,v) + d(v,w) >= d(u,w)` must hold.
    *   A graph is connected if its diameter is finite.
    *   A graph is k-partite/k-colorable if its vertices can be partitioned into `k` or fewer parts, with endpoints of each edge in different parts.
    *   A graph is bipartite if and only if it contains no cycle of odd length (Theorem B).
    *   A complete bipartite graph `K_m,n` is defined on `{1,...,m+n}` where `u — v` iff `1 <= u <= m < v <= m+n`. It has `mn` edges.
    *   A complete k-partite graph `K_n1,...,nk` consists of `N = n1+...+nk` vertices partitioned into parts `{n1,...,nk}`, with edges between any two vertices not in the same part.
    *   `K_1,n` is a free tree, called the star graph of order `n+1`.
2.  **Directed Graphs (Digraphs):**
    *   A digraph `D = (V, A)` has a set `V` of `n` vertices and a multiset `A` of `m` ordered pairs `(u,v)` (arcs). The term "digraph" must be used instead of "directed graph".
    *   `u — v` denotes `(u,v) ∈ A`. Digraphs are allowed to have self-loops `v — v`. More than one arc `u — v` may be present.
    *   A digraph is simple if `A` is a set (at most one arc `(u,v)` for all `u,v`).
    *   An arc `(u,v)` has initial vertex `u` and final vertex `v` (its "tip"). Two arcs are consecutive if the tip of the first is the initial vertex of the second.
    *   `d+(v)` is the out-degree (number of arcs where `v` is initial). `d-(v)` is the in-degree (number of arcs where `v` is final). `∑_v d+(v) = ∑_v d-(v) = m`.
    *   A vertex with `d-(v)=0` is a source. A vertex with `d+(v)=0` is a sink.
    *   `D` and `D'` are isomorphic if a one-to-one correspondence `φ` from `V` to `V'` exists such that the number of `u — v` arcs in `D` equals the number of `φ(u) — φ(v)` arcs in `D'`.
    *   `J_n` is the largest simple digraph on `n` vertices; has `n^2` arcs.
    *   A sequence of consecutive arcs is a walk. An oriented path has distinct vertices. An oriented cycle has distinct vertices except `v0 = vk`.
    *   `d(u,v)` is the number of arcs in the shortest oriented path from `u` to `v`. The directed triangle inequality `d(u,v) + d(v,w) >= d(u,w)` must hold.
    *   An undirected edge `u — v` is equivalent to a matched pair of arcs `u — v` and `v — u`. This conversion retains graph properties.
    *   A directed acyclic graph (DAG) is a digraph that contains no oriented cycles.
    *   `ARCS(v)` must denote the first arc of vertex `v`.
    *   `NEXT(a)` must denote the next arc with the same initial vertex as `a`.
    *   `TIP(a)` must denote the final vertex of arc `a`.
3.  **Hypergraphs:**
    *   In a hypergraph, edges are arbitrary subsets of vertices.
    *   An `r`-uniform hypergraph: Every edge contains exactly `r` vertices.
    *   A complete `r`-uniform hypergraph `K_n^(r)` has `n` vertices and `(n choose r)` edges.
    *   An induced subhypergraph `H|U` has edges `{e | e ∈ E and e ⊆ U}`.
    *   The hypergraph complement `H` has edges of `K_n^(r)` not in `H`.
    *   A `k`-coloring assigns `k` or fewer colors to vertices such that no edge is monochromatic.
    *   A hypergraph `H` is equivalent to a `0-1` matrix `B` (rows for vertices, columns for edges), where `b_ve = [v ∈ e]`. `v` is "incident with `e`" if `v ∈ e`.
    *   A hypergraph is equivalent to a bipartite graph with vertex set `V ∪ E` and edge `v — e` iff `v` is incident with `e`.
    *   A hypergraph is connected iff its corresponding bipartite graph is connected.
    *   A cycle of length `k` in a hypergraph is a cycle of length `2k` in its corresponding bipartite graph.
    *   The dual hypergraph `H^d` must interchange the roles of vertices and edges, retaining incidence; it corresponds to transposing the incidence matrix. The dual of an `r`-regular graph is an `r`-uniform hypergraph.
    *   If `H` has no repeated edges, it's equivalent to Boolean function `h(x1,...,xn) = [{j|xj=1} ∈ E]`.
    *   A set `U` of vertices covers `H` if every edge contains at least one member of `U`. `U` is minimal if `U\u` fails to be a cover for any `u ∈ U`. `U` is minimum if it has the smallest possible size.
    *   A set `W` of vertices is independent in `H` if no edge is completely contained in `W`. `W` is maximal if `W ∪ w` fails to be independent for any `w ∉ W`. `W` is maximum if it has the largest possible size.
    *   `U` covers `H` iff `V\U` is independent. `W` is independent iff `V\W` covers `H`. `U` covers `H` iff `H|(V\U)` has no edges.
    *   The independence number `α(H)` is the maximum size of an independent set of vertices in `H`.
    *   The chromatic number `χ(H)` is the minimum `k` for which `H` is `k`-colorable. `χ(H)` is the size of a minimum covering of `H` by independent sets.
    *   The clique number `ω(G)` is the maximum size of a clique in `G`. `ω(G) = α(Ḡ)`.
    *   `χ(G)` is the minimum size of a set of cliques that exactly covers all vertices.
    *   An exact cover is a set of rows whose sum is `(11...1)`, or a set of vertices that touches each hyperedge exactly once.

## VIII. General Data Structure Principles

1.  **Node Fields:**
    *   Nodes must contain a `KEY` field to store a key.
    *   Nodes must contain a `RECORD` field, which stores the record associated with a key (including `KEY` as a subfield).
    *   Tree nodes must have an `LLINK` field pointing to their left subtree.
    *   Tree nodes must have an `RLINK` field pointing to their new right subtree.
2.  **Tree Representation:**
    *   Null subtrees must be represented by a null pointer (Λ).
    *   A `ROOT` variable must point to the root of a tree.
    *   For general Binary Search Tree (BST) operations, the tree is assumed not to be empty (`ROOT ≠ Λ`) for convenience in description.
    *   A tree must always have a root node and is never empty; each node can have 0 to N children.
    *   A binary tree can be empty; each node can have 0, 1, or 2 children, with left/right distinction.
    *   A forest is an ordered set of zero or more trees.
    *   Two binary trees T and T' are similar if they are both empty, or both nonempty with similar left and right subtrees (`n = n'` and `l(u_j) = l(u'_j), r(u_j) = r(u'_j)` for all nodes).
    *   Two binary trees T and T' are equivalent if they are similar and corresponding nodes contain the same information (`info(u_j) = info(u'_j)`).
    *   If the INFO value set has only one element, equivalence is the same as similarity.
    *   Every node except the root must have exactly one parent. Parent-only links are generally insufficient for typical tree operations.

## IX. Specific Data Structures & Layout

1.  **MMIX Data Layout (General):**
    *   Data items in a sequential structure must occupy 8 bytes if `A + 8i` is used for addressing `a_i`.
    *   Data structures are typically octabyte-aligned if they contain one or more OCTA-fields.
    *   When using low-order bits as tags, those bits must be masked to zero on CPU architectures that do not ignore them before using link fields as addresses. The LSB of a `LINK` field must be ignored when using it as an address in load or store instructions.
    *   Values of link variables must be put into registers, and field-offsets (defined as constants) must be used in load and store instructions.
    *   In `MMIXAL` programs, symbols mostly stand for addresses and registers, not values, unless explicitly defined as a plain value (e.g., `FACEUP Is 0`).
    *   The three least significant bits `H`, `M`, and `A` are freely available as tag bits in list manipulation nodes for OCTA-aligned data.
    *   A tagged tetrabyte must occur before and after the memory area used to limit `Algorithm C` activities.
    *   Compact one-word format uses 32-bit relative addresses, implying a maximum 4 GByte pool size.
2.  **Node Field Definitions (MMIX General):**
    *   `LLINK` field is defined as `1:2` (Program T), `4:5` (MIX Algebraic Formulas), and can also be called LCHILD.
    *   `RLINK` field is defined as `1:2` (Program T), `1:2` (MIX Algebraic Formulas).
    *   `LLINKT` field is defined as `0:2` (Program S). `RLINKT` field is defined as `0:2` (Program S), `0:2` (MIX Algebraic Formulas).
    *   `LTAG/RTAG` meaning: `l(u)` (LTAG) is 1 if node `u` has a nonempty left subtree, 0 otherwise. `r(u)` (RTAG) is 1 if node `u` has a nonempty right subtree, 0 otherwise. `RTAG` must be negative for thread links (corresponding to RTAG = 1 in algorithm statements).
    *   `TYPE` field is defined as `3:3` (MIX Algebraic Formulas). `TYPE` field must distinguish different kinds of nodes: 0=constant (INFO its value), 1=variable (INFO its five-letter alphabetic name), >2=operator (INFO its alphabetic name, TYPE value distinguishes operators).
    *   `LLINK` and `INFO` fields can be mutually exclusive and share the same field for memory efficiency.
    *   `RLINK(P)` and `RTAG(P)` will be meaningless concerning a tree when "P points to a tree" (meaning NODE(P) is the root of a right-threaded binary tree).
3.  **Specific MMIX Node Layouts:**
    *   **Playing Cards:** `TAG` field is one `BYTE` (`#80` face down, `#90` face up). `SUIT` field is a `BYTE` (1=clubs, 2=diamonds, 3=hearts, 4=spades). `RANK` field is a `BYTE` (1=ace, ..., 13=king). `NEXT` field is a link to the card below.
    *   **Linked Lists:** A node often has the `LINK` field as the first octabyte and `INFO` as the second.
    *   **Topological Sort:** `TOP[k]` and `NEXT` link fields must fit into one tetrabyte. Object numbers must be scaled by 8 to transform object number `k` into the relative address of `X[k]`.
    *   **Subroutine Allocation:** `SPACE` field must be `0 < SPACE < 2^31`. Links must be relative addresses. `LINK` fields are normally even. The last `LINK` field of a node must have its least significant bit set to 1 to indicate the end of the node.
    *   **Circular Lists:** The `ABC` field must always be zero, except for a special node at the end of every polynomial which has `ABC = -1` and `COEF = 0`.
    *   **Elevator Nodes:** Typically structured with `LLINK1` at offset 0, `RLINK1` at 8, etc. `WAIT` list head contains only the first four octabytes of a node. `QUEUE` and `ELEVATOR` list heads require only the last two octabytes of a node. `USER1`, `ELEV1`, `ELEV2`, `ELEV3` nodes contain only four octabytes.
    *   **Matrix Nodes:** Consist of four octabytes and five fields: `LEFT`, `UP`, `VAL`, `ROW`, `COL`. Matrix list heads `BASEROW[i]` and `BASECOL[j]` are identified by odd links pointing to them.
    *   **Differentiation Trees:** Node structure: `RLINK | RTAG`, `LLINK`, `DIFF | INFO`. `RTAG` is 1 for thread links. `DIFF` address must squeeze into a single `WYDE` (given relative to `DIFF[0]`).
    *   **Dynamic Storage Allocation:** `SIZE-8` bytes reserved for application use must be `OCTA-aligned`. Node itself starts and ends with a `SIZE` field that is `TETRA-aligned`. `TAG` bit (LSB in `SIZE` field) is used to control the collapsing process. Links are stored as relative addresses in a `TETRA`. `LOC(AVAIL)` is used as the base address for relative links, making the list head's relative address zero. For an available block `P`, `LLINK(RLINK(P)) = P = RLINK(LLINK(P))` must always hold. List head: `RLINK` points to the first block, `LLINK` to the last block.
    *   **Polynomial Tree Nodes:** Must have six fields: `[UP]`, `[LEFT]`, `[CV]`, `[DOWN]`, `[EXP]`, `[RIGHT]`. `LEFT, RIGHT, UP, DOWN` fields must be used as links. `EXP` field must be an integer. `CV` field must be a constant or variable name.
4.  **MMIX Binary Tree Specifics:**
    *   `TAG`s are stored in the least significant bit of the link fields.
    *   An empty threaded tree must satisfy: `LLINK(HEAD) = HEAD`, `LTAG(HEAD) = 1`.
    *   In a threaded-tree representation, each node except the list head has exactly one link pointing to it from above (from its parent).
    *   For insertion Algorithm I, nodes must have `LLINK`, `RLINK`, and `RTAG`.
    *   For tree comparison algorithms, nodes must have `LLINK`, `RLINK`, `RTAG`, and `INFO`.
    *   For erase algorithms, nodes must have `LLINK`, `RLINK`, and `RTAG`.
    *   For SUC/PRED algorithms, each binary tree node must have four link fields: `LLINK`, `RLINK` (for subtrees or Λ), and `SUC`, `PRED` (for symmetric order successor/predecessor).
    *   In the threaded tree variant: `LTAG(P)` standard, `LLINK(P)` must always be `Px`, `RLINK(P)` unthreaded.
    *   For the removal/attachment algorithm, all binary trees must be right-threaded, with fields `LLINK`, `RTAG`, `RLINK`.
    *   In preorder sequential representation, nodes must have `INFO`, `RLINK`, and `LTAG` fields. `LTAG = 1` (for terminal nodes) is indicated by "|".
    *   In SCOPE representation, `LTAG(X) = "|"` must be characterized by `SCOPE(X) = X+c`.
    *   In representation (6), "+" must indicate special link nodes whose INFO characterizes them as links.
    *   In family order sequential representation, `RTAG` entries must serve to delimit families.
5.  **Fibonacci Tree:**
    *   **Base Cases (Order 0 or 1):** If the order `k` of a Fibonacci tree is 0 or 1, its representation must be `[0]`.
    *   **Root (Order > 2):** If the order `k` of a Fibonacci tree is greater than 2, its root must be `Fk`.
    *   **Left Subtree (Order > 2):** If the order `k` of a Fibonacci tree is greater than 2, its left subtree must be the Fibonacci tree of order `k-1`.
    *   **Right Subtree (Order > 2):** If the order `k` of a Fibonacci tree is greater than 2, its right subtree must be the Fibonacci tree of order `k-2`, with all numbers increased by `Fk-1`.
    *   **Internal Node Children Difference:** For internal nodes, the numbers on the two children must differ from their parent's number by the same amount. The difference amount must be a Fibonacci number (`Fj`).
    *   **Next Left Branch Difference:** If the difference amount is `Fj`, the Fibonacci difference for the next left branch must be `Fj-1`.
    *   **Next Right Branch Difference:** If the difference amount is `Fj`, the Fibonacci difference for the next right branch must be `Fj-2`.
6.  **Balanced Tree (AVL/Weight-Balanced):**
    *   **Balance Property:** A binary tree is balanced if, for every node, the absolute difference between the height of its left subtree and the height of its right subtree is at most 1.
    *   **Node Field - Balance Factor (`B(P)`):** Nodes must have a `B(P)` (balance factor) field, which must always contain either +1, 0, or -1. `B(P)` must represent (height of right subtree - height of left subtree).
    *   **Special HEAD Node:** A special `HEAD` node must exist. `RLINK(HEAD)` must point to the root of the tree. `LLINK(HEAD)` must track the overall height of the tree.
    *   **LINK Macro:** `LINK(a,P)` means `LLINK(P)` if `a = -1`, and `RLINK(P)` if `a = +1`.
    *   **Triply Linked Tree:** For general purposes, a triply linked tree must be used, including `UP`, `LLINK`, and `RLINK` fields. Triply linked nodes must include a one-bit field specifying left or right child status.
    *   **Weight-Balanced Property:** For a weight-balanced tree, the ratio of `left weight / right weight` of all subtrees must be between `α` and `1/α`.
7.  **2-3 Tree:**
    *   **Branching Factor:** Each node must have either 2-way or 3-way branching.
    *   **External Node Level:** All external nodes must appear on the same level.
    *   **Internal Node Keys:** Every internal node must contain either one or two keys.
    *   **Binary Representation:** In the binary tree representation, one bit in each node must distinguish horizontal from vertical `RLINK`s. Keys must appear in strict alphabetic order from left to right when traversing the tree symmetrically.
8.  **Binary Decision Diagram (BDD):**
    *   **Acyclic Property:** All decision diagrams (BDD, QDD, ZDD) must be acyclic.
    *   **Reduced Property:** Decision diagram bases must be reduced, ensuring no redundant nodes.
    *   **Uniqueness:** Two functions or subfunctions in a decision diagram base must be equal if and only if they correspond to the same node (uniqueness criterion).
    *   **Node Identification:** Nodes must be identifiable by their content (`V`, `LO`, `HI` fields), not solely by memory address.
    *   **Variable Order:** Internal branch variables must retain their natural order (1, 2, ..., n) from top to bottom.
    *   **Function Representation:** All non-constant Boolean functions `f(x_1, ..., x_n)` must be represented in the form `(x_v ? f_1 : f_0)`, where `v` is the index of the first variable `f` depends on (`f_v`). `f_1` must be defined as `f(x_v = 1)` and `f_0` as `f(x_v = 0)`.
    *   **Composition Variable:** When combining two non-constant functions `f` and `g`, the variable `v` must be `min(f_v, g_v)`. When combining three non-constant functions `f, g, h`, the variable `v` must be `min(f_v, g_v, h_v)`.
    *   **BDD Node Fields:** Every BDD node must have `V`, `LO`, `HI`, and `REF` fields.
    *   **Sink Nodes:** `I_0`, `I_1`, `I'_0`, and `I'_1` must be designated as sink nodes. Sink nodes ([0] and [1]) must be represented as nodes 0 and 1. Sink nodes must have nonnegative `LO` and `HI` fields. Sink nodes must not be deleted by Algorithm R.
    *   **Variable Ordering (Ordered BDDs):** When an arc goes from a branch node associated with variable `i` to a branch node associated with variable `j`, the variable index `i` must be less than `j`. The variable index of a node (`V(k)`) must be greater than the variable indices of its LO and HI branches (`V(l_k)`, `V(h_k)`). `V` fields of branch nodes must be in increasing order from `V(ROOT)` up to `Vmax` (from top downwards).
    *   **Reduced BDDs:** A branch node's LO and HI pointers must not be equal. No two nodes are allowed to have the same triple of values (V, LO, HI).
    *   **Bead Correspondence:** Every bead of a Boolean function must correspond to a branch node in its BDD.
    *   **Branch Node Representation:** A branch node (j) for truth table `T' = T0T1` must have its LO branch point to the root of `T0` and its HI branch point to the root of `T1`.
    *   **BDD Size (`B(f)`):** `B(f)` is defined as the number of beads `f` has (total nodes, including sinks). `B*(f)` is the number of BDD nodes when the sink `[L]` (FALSE) is forced to be present (`B(f) + 1` if `f` is identically 1, `B(f)` otherwise).
9.  **QDD Node & Structure:**
    *   Every function must have a unique QDD.
    *   A QDD's root node must always be `(1)`.
    *   Every `(k)` node in a QDD for `k < n` must branch to two nodes.
    *   Every path from a QDD's root to a sink must have length `n`.
    *   `LO` and `HI` pointers of a QDD node may be identical.
    *   In a QDD, different nodes cannot have the same `(LO, HI)` pair.
    *   `V` fields are redundant in a QDD and need not be present in memory.
10. **ZDD Node & Structure:**
    *   A ZDD's root node must name the smallest element present in at least one represented set.
    *   A ZDD's HI branch must represent residual subfamilies containing the root's element.
    *   A ZDD's LO branch must represent residual subfamilies not containing the root's element.
    *   `[L]` must represent the empty family `0`. `[T]` must represent the unit family `{0}`.
    *   `LO` and `HI` pointers may be identical in a ZDD.
    *   A unique ZDD must be constructible from a function's truth table.
    *   When representing words using ZDDs (e.g., with variables `a_1, ..., z_5`), the function `F` must be true when the corresponding letter variables are 1 and others are 0.
    *   The memo cache must distinguish BDD facts from ZDD facts when sharing nodes.
11. **Tableaux:**
    *   A Young Tableau is an arrangement of `n_1 + ... + n_m` distinct integers in left-justified rows of lengths `n_1 >= ... >= n_m > 0`, where row entries increase left-to-right and column entries increase top-to-bottom.
    *   Tableaux are conceptually bordered by `0`s (top/left) and `infinity`s (right/below).
    *   The relation `a <= b` is true if `a < b`, or `a = b = 0`, or `a = b = infinity`.
    *   Tableau inequalities `P_{i,j} <= P_{i,j+1}` and `P_{i,j} <= P_{i+1,j}` for `i,j > 0` must hold.
12. **Loser Trees:**
    *   In a loser tree representation for multiway merging, the loser of a match must be stored in each internal node of the tree.
    *   An extra node (number 0) must be appended at the top of a loser tree to indicate the champion.
    *   In a loser tree, each key (except the champion) must appear exactly once in an external node and once in an internal node.
13. **SGB Digraph Structure:**
    *   SGB digraphs must use a sequential array of `n` vertex nodes (for `0 <= k < n`) and `m` arc nodes linked in a memory pool.
    *   Node field types: fixed "standard fields" and multipurpose "utility fields."
    *   Vertex node standard fields: `NAME` (pointer to a character string for identification) and `ARCS` (pointer to the first arc node in a singly linked list).
    *   Arc node standard fields: `TIP` (pointer to the tip vertex node) and `NEXT` (pointer to the next arc node with the same initial vertex).
    *   Out-degree zero representation: `ARCS(v) = Λ` (null pointer) represents an out-degree of 0.
    *   Graph node standard fields: `M(g)` (total arcs), `N(g)` (total vertices), `VERTICES(g)` (pointer to first vertex node), and `ID(g)` (graph identification string).

## X. Algorithm Design & Control Flow (General)

1.  **General Design Principles:**
    *   Recursive algorithms must terminate for sufficiently simple base cases.
    *   Auxiliary data structures (memos, unique tables) must be maintained to support algorithms. Memoization must be used to store and retrieve results for previously solved subproblems.
    *   An algorithm traversing an unthreaded binary tree in inorder without an auxiliary stack must ensure the tree retains its conventional representation both before and after traversal.
    *   To evaluate a top-down function efficiently, the algorithm should work on trees stored in postorder with degrees.
    *   The algorithm for filling links must initially have the `LCHILD` field of each node as Λ, `RLINK` fields forming a linear list, `FIRST` pointing to the first node, and the last node having `RLINK = Λ`.
    *   A top-down locally defined function `f` is one in which the value of `f` at a node `x` depends only on `x` and the value of `f` at the parent of `x`.
    *   If non-shortening transformations are allowed (e.g., in `h^2 + p^2` contexts), the rounding rule must be asymmetric with respect to sign.
    *   The `p`-fold truncation operator on a vector is defined as repeating the following operation `p_u` times: "Let `j` be minimal such that `p(u_j) > 1`, and replace `u_j` by `trunc(u_j)`; if `p(u_j) = 1` for all `j`, do nothing."
    *   The output of the linear iterative array is the `z_0` component of machine `M_0`. The leftmost machine `M_0` must act as if there is a machine to its left in state `(3,0,0,0,0, u,v,q,0,0)` when receiving inputs `(u,v,q)`.
    *   Automaton state `c` must be in the range `0 <= c <= 3`. Automaton states `z`, `y`, and `q` must be `0` or `1`.
2.  **Preconditions & Postconditions:**
    *   `Algorithm I` (for trees) precondition: The binary tree must be threaded as in (10).
    *   `Algorithm D` (differentiation) preconditions: `Y` must be the address of a list head pointing to a formula, and `DY` must be the address of the list head for an empty tree.
    *   `Algorithm E` (equivalence) preconditions: `S` must be the set of numbers `{1,2,...,n}`, and `PARENT[1...n]` must be integer variables.
    *   `Algorithm A` (Polynomial addition) preconditions: `P` and `Q` must be pointer variables linking to the roots of distinct polynomial trees.
    *   `Algorithm A` (Polynomial addition) postconditions: Upon conclusion, `polynomial(P)` must be unchanged, and `polynomial(Q)` must contain the sum.
    *   After array equivalence processing, if `PARENT(P) = A`, locations `X[LBD(P)]...X[UBD(P)]` must be reserved in memory for that equivalence class. If `PARENT(P) = Q # A`, location `X[k]` must equal location `Y[k + DELTA(P)]`, where `NAME(Q) = "Y"`.
    *   For Algorithm N (Null Space), input `A` must be an n x n matrix over a field.
    *   For Algorithm A (exponentiation), `x` must belong to an algebraic system in which an associative multiplication, with identity element `1`, has been defined.
    *   Input polynomials for Algorithms D (polynomial), R, E, C must satisfy specific degree and leading coefficient constraints (e.g., `v(x)` not zero, `v_n ≠ 0`, `m >= n`).
    *   Input key ordering (Fibonaccian Search): The input table of records (R1 to RN) must have keys (K1 to KN) in increasing order (K1 < K2 < ... < KN).
    *   Perfect Fibonacci Number Assumption (Fibonaccian Search): For simplified description, assume `N+1` is a perfect Fibonacci number (`Fk`).
    *   Nonnegative Input Weights (Algorithm K, G): All input weights (`p1` to `pn`, `q0` to `qn` for Algorithm K; `w0` to `wn` for Algorithm G) must be nonnegative.
    *   Array Indexing (Algorithm K): `c`, `r`, `w` arrays must be indexed for `0 ≤ i ≤ j ≤ n`.
    *   Non-empty Tree Assumption (Algorithm T): The tree is assumed not to be empty (`ROOT ≠ Λ`).
    *   Valid BST Postcondition (Algorithm D): Algorithm D must leave a valid binary search tree.
    *   Non-empty Tree Precondition (Algorithm C): The tree must be non-empty for Algorithm C.
    *   Sum of Probabilities: When dealing with probabilities of searching for elements (`pk`), their sum must equal 1 (`p1 + ... + pN = 1`).
    *   Key/Interval Probabilities: When probabilities are given for keys (`pi`) and intervals (`qk`), their sum must equal 1 (`p1 + ... + pn + q0 + ... + qn = 1`).
3.  **Initialization:**
    *   In Algorithm M (multiplication), all product digits `w_m+n-1, ..., w_0` must be set to zero initially.
    *   All devices in a linear iterative array must start in state `(0,0,0,0,0,0,0,0,0,0)`.
    *   In Algorithm D (distinct-degree factorization), `v(x)` must be initialized to `u(x)`, `w(x)` to `x`, and `d` to 0.
    *   `Algorithm F` initialization: Set the stack empty and set P to point to the first node of the forest in postorder.
4.  **Iteration & Control Flow:**
    *   `Algorithm C` loop: If `Algorithm C` does not terminate at step C6, it must return to step C2.
    *   `Algorithm D` loop: If `P # Y`, `Algorithm D` must return to step D2.
    *   `Algorithm F` loop: If `Algorithm F` does not terminate at step F4, set `P` to its successor in postorder and return to step F2.
    *   `Algorithm E` root finding loop: If `PARENT[j] > 0`, set `j = PARENT[j]` and repeat this step.
    *   `Algorithm E` loop: After merging (or if `j=k`), return to step E2.
    *   `Algorithm E` termination: `Algorithm E` terminates if the input is exhausted.
    *   Loops must continue and terminate according to specified conditions (e.g., `j < n` false for addition, `k` from `m-n` down to `0` for polynomial division).
    *   An algorithm that incorporates transformations that can increase the length of a vector must be careful to avoid infinite looping.
    *   When `m = 10^9` for multiplier calculation, solutions must be continuously attempted until `x_1 = 0` (modulo 10) is achieved.
    *   In Algorithm A (exponentiation), when `N = 0`, the algorithm must terminate with `Y` as the answer. `Z` must be updated to `Z * Z`.
    *   For Algorithm D (distinct-degree factorization), the procedure must terminate if `d+1 > deg(v)/2`.
    *   Differentiation routines (DIFF[0], etc.) must return control to step D3 after processing a binary operator; otherwise, they must return to step D4.
5.  **Algorithm Invariants & Properties:**
    *   In Algorithm D (specific process), `p_p' < 0` must hold throughout the calculation.
    *   In Algorithm S (specific process), `v_1 <= v_sqrt(2)` is implicitly used.
    *   In calculations involving `u_1*y_2 - u_2*y_1 = m`, `u_1 + q*y_1` must be `0` (modulo `m`) if `y_2` is relatively prime to `m`.
    *   The sum `u_1*y_1 + u_2*y_2` must satisfy `2 * |u_1*y_1 + u_2*y_2| < y_1^2 + y_2^2`.
    *   `Program T` stack invariance: The number of insertions onto the stack must equal the number of deletions.
    *   `Program S` node examination: The `LLINK` and `RLINK` of each node must be examined precisely once.
    *   `Algorithm D` temporarily destroys the structure of tree Y; the missing links must be restored later in step D3.
    *   `Function F` (Evaluate Locally Defined Function): The value of function `f` at a node `x` must depend only on `x` and the values of `f` on its children.
    *   `Algorithm F` stack update: After evaluating `f(NODE(P))`, remove the top `d` items from the stack and then push `f(NODE(P))` onto the stack.

## XI. Sorting & Merging Algorithms

1.  **General Sorting Strategies:**
    *   Internal sorting requires records to be kept entirely in the computer's high-speed random-access memory.
    *   Address table sorting involves manipulating link addresses (pointers to records) instead of moving records.
    *   Keysorting involves placing short keys with link addresses for speed when satellite information is long.
    *   List sorting utilizes auxiliary link fields within each record to link records into a linear list.
    *   Records can be rearranged into increasing order after link or address table sorting.
    *   Some sorting methods optionally assume the existence of `-infinity` and `+infinity` such that `-infinity < K_j < +infinity` for all `j`.
2.  **Comparison Counting (Algorithm C):**
    *   Purpose: Sort records `R_1,...,R_N` by counting keys less than a given key; `COUNT[j]+1` gives the final position of `R_j`.
    *   Steps: C1: Initialize `COUNT[1...N]` to zero. C2-C3: Loop `i` from `N` down to `2`, then `j` from `i-1` down to `1`. C4: If `K_i < K_j`, increment `COUNT[j]`; else increment `COUNT[i]`.
    *   Algorithm C works properly even with equal keys.
3.  **Distribution Counting (Algorithm D):**
    *   Assumptions: Keys are integers in range `u <= K_j <= v`.
    *   Purpose: Sort records `R_1,...,R_N` into `S_1,...,S_N` using a `COUNT[u...v]` table.
    *   Steps: D1: Initialize `COUNT[u...v]` to zero. D2-D3: Loop `j` from `1` to `N`, increment `COUNT[K_j]`. D4: Accumulate: `COUNT[i] <- COUNT[i] + COUNT[i-1]` for `i = u+1...v`. D5-D6: Loop `j` from `N` down to `1`, set `S_{COUNT[K_j]} <- R_j`, then `COUNT[K_j] <- COUNT[K_j]-1`.
4.  **Straight Insertion Sort (Algorithm S):**
    *   Purpose: Rearrange records `R_1,...,R_N` in place to `K_1 <= ... <= K_N`. Records must be 64-bit signed integers.
    *   Steps: S1: Loop `j` from `2` to `N`. S2: Set `i <- j-1`, `K <- K_j`, `R <- R_j`. S3: If `K > K_i`, go to S5. S4: Set `R_{i+1} <- R_i`, then `i <- i-1`. If `i > 0`, go to S3. S5: Set `R_{i+1} <- R`.
5.  **Shellsort (Algorithm D):**
    *   Purpose: Rearrange records `R_1,...,R_N` in place using a sequence of increments `h_{t-1}, ..., h_0`. The last increment `h_0` must equal `1`.
    *   Steps: D1: Loop `s` from `t-1` down to `0`. D2 (h-sorting): Set `h <- h_s`, loop `j` from `h+1` to `N`. D3: Set `i <- j-h`, `K <- K_j`, `R <- R_j`. D4: If `K > K_i`, go to D6. D5: Set `R_{i+h} <- R_i`, `i <- i-h`. If `i > 0`, go to D4. D6: Set `R_{i+h} <- R`.
    *   If a `k`-ordered file is `h`-sorted, it remains `k`-ordered.
    *   If `(x_1,...,x_m)` and `(y_1,...,y_n)` are sequences such that `x_i <= y_{i+r}` and are then sorted independently, the relations `x_i <= y_{i+r}` will still be valid.
6.  **Multiway Merging:**
    *   When merging runs, the record with the smallest key must always be selected from the current first records of each input run. The selected record must be transferred to the output and removed from the input.
    *   During multiway merging, only one key from each input run must be considered at a time for selection. If multiple keys are smallest during selection, any one may be selected arbitrarily.
    *   To gracefully terminate merging, an "infinity" (∞) key must be placed at the end of each run. Sentinel records (e.g., "infinity" keys) must be used to delimit runs on a file.
    *   `P`-way merging requires exactly `P` external nodes and `P` internal nodes.
    *   To reconstitute a run with `m` degrees of freedom, the first `m` blocks must be read into `m` buffers, an `m`-way merge performed on these buffers, and when a buffer is exhausted, it must be replaced with the next block from the run.
7.  **Replacement Selection (Algorithm R):**
    *   When forming initial runs, if a new record's key is smaller than the last output key, it must not be included in the current run. If a new record's key is not smaller than the last output key, it must be entered into the selection tree for the current run.
    *   Algorithm R produces runs of length `P` or more (excluding the final run). Algorithm R reads records sequentially from an input file and writes records sequentially onto an output file. `P` must be greater than or equal to 2.
    *   **Key Definition:** Each key must be considered as a pair `(S, K)`, where `S` is the run number and `K` is the original key. Extended keys must be lexicographically ordered with `S` as the major key and `K` as the minor key.
    *   **Node Structure (`X[j]`):** The `j`-th node `X[j]` must contain `t` words starting at `LOC(X[j]) = Lg + tj` for `0 <= j < P`.
    *   **Node Fields:** Each node `X[j]` must contain a `LOSER` field, which is a pointer to the "loser" stored in this internal node. An `RN` (run number) field, which stores the run number of the record in this external node. A `PE` field, which is a pointer to the internal node above this external node in the tree. A `PI` field, which is a pointer to the internal node above this internal node in the tree. `PE` and `PI` fields need not appear explicitly in memory if their values are constant.
    *   **R1 (Initialization):** `RMAX` to 0; `RC` to 0; `LASTKEY` to infinity (∞) (must be greater than any possible key). `Q` to `LOC(X[0])`. For each node `J` (0 <= `j` < `P`): `LOSER(J)` to `J`; `RN(J)` to 0; `PE(J)` to `LOC(X[[(P+j)/2]])`; `PI(J)` to `LOC(X[[j/2]])`.
    *   **R2 (End of run check):** If `RN(Q)` equals `RC`, proceed to step R3. If `RN(Q)` is not equal to `RC` (implying `RN(Q) = RC + 1`), it indicates the completion of run `RC`. If `RC` equals `RMAX`, terminate the algorithm. If `RC` is not equal to `RMAX`, increment `RC` by 1.
    *   **R3 (Output champion):** If `RC` is not 0, output `RECORD(Q)` and set `LASTKEY` to `KEY(Q)` after output.
    *   **R4 (Input new record):** If the input file is exhausted, set `RN(Q)` to `RMAX + 1`. If the input file is not exhausted, set `RECORD(Q)` to the next input record. If `KEY(Q)` is less than `LASTKEY`, set `RMAX` to `RC + 1`.
    *   **R5 (Prepare to update):** Set `T` to `PE(Q)`.
    *   **R6 (Set new loser):** Set `L` to `LOSER(T)`. If `RN(L)` is less than `RN(Q)` OR (`RN(L)` equals `RN(Q)` AND `KEY(L)` is less than `KEY(Q)`), then: Set `LOSER(T)` to `Q`. Set `Q` to `L`.
    *   **R7 (Move up):** If `T` equals `LOC(X[1])`, return to step R2. If `T` does not equal `LOC(X[1])`, set `T` to `PI(T)`. After updating `T`, return to step R6.
8.  **Delayed Reconstitution of Runs:**
    *   Records within individual blocks must be ordered in nondecreasing order.
    *   For ordinary replacement selection (one degree of freedom), the lowest element of each block within a run must never be less than the highest element of the preceding block in that run.
    *   For `m` degrees of freedom, the lowest element of each block may be less than the highest element of the preceding block, provided it is not less than the highest elements in `m` different preceding blocks of the same run.
    *   During reconstitution, the first word of every newly read block must be greater than or equal to the last word of the just-exhausted block.
9.  **Natural Selection Rules:**
    *   If a new record's key is less than `LASTKEY`, it must not be placed in the selection tree; instead, it must be output to an external reservoir, and another new record must be read in.
    *   This process must continue until the reservoir is filled with `P'` records.
    *   Once the reservoir is filled, the remainder of the current run must be output from the selection tree.
    *   After the current run is output, the reservoir items must be used as input for the next run.
10. **Polyphase Merge Algorithms:**
    *   **Generalized Polyphase Merge:** Requires `T` tapes (`T >= 3`). Must use `(T-1)`-way merging. Requires a "perfect Fibonacci distribution" of runs on tapes after each phase to operate as described.
    *   **Algorithm D (Polyphase Merge):** Requires `T` tape units, where `T = P + 1` and `T >= 3`. Must use `P`-way merging. Tape `T` must not receive any initial runs.
        *   **D1 Initialization:** Set `A[j]` to 1, `D[j]` to 1, and `TAPE[j]` to `j` for `1 <= j < T`. Set `A[T]` to 0, `D[T]` to 0, and `TAPE[T]` to `T`. Set `I` to 1 and `j` to 1.
        *   **D2 Input to Tape:** Write one run on tape number `j`. Decrease `D[j]` by 1. If input is exhausted, rewind all tapes and go to step D5.
        *   **D3 Advance `j`:** If `D[j] < D[j+1]`, increment `j` by 1 and return to D2. Otherwise, if `D[j] = 0`, proceed to D4. Otherwise, set `j` to 1 and return to D2.
        *   **D4 Up a Level:** Increment `I` by 1. Set `a` to `A[1]`. For `j` from 1 to `P` (in this order): Set `D[j]` to `a + A[j+1] - A[j]`. Set `A[j]` to `a + A[j+1]`. `A[P+1]` must always be zero. Set `j` to 1 and return to D2. The condition `D[1] >= D[2] >= ... >= D[T]` must hold at the conclusion of step D4.
        *   **D5 Merge:** If `I = 0`, sorting is complete, and the output is on `TAPE[1]`. Otherwise, merge runs from `TAPE[1]` to `TAPE[P]` onto `TAPE[T]` until `TAPE[P]` is empty and `D[P] = 0`. For each run merged: If `D[j] > 0` for all `j` from 1 to `P`, then increment `D[T]` by 1 and decrement each `D[j]` by 1 for `j` from 1 to `P`. Otherwise, merge one run from each `TAPE[j]` such that `D[j] = 0`, and decrement `D[j]` by 1 for each other `j`.
        *   **D6 Down a Level:** Decrement `I` by 1. Rewind `TAPE[P]` and `TAPE[T]`. Cyclically shift physical tape assignments: `TAPE[1]` becomes `TAPE[T]`, `TAPE[2]` becomes `TAPE[1]`, ..., `TAPE[T]` becomes `TAPE[T-1]`. Cyclically shift dummy run counts: `D[1]` becomes `D[T]`, `D[2]` becomes `D[1]`, ..., `D[T]` becomes `D[T-1]`. Return to step D5.
    *   **Caron's Polyphase Merge:** This modified polyphase procedure requires at least five tapes. Each phase must merge runs from `T-3` tapes onto another tape, while the remaining two tapes are rewinding.
    *   **McAllester's Tape Splitting Polyphase Merge:** This method requires four or more tapes. This method must use `(T-2)`-way merging. To achieve the specified output state (one run on T4, others empty), the sequences `un` and `vn` must satisfy the recurrence `un + vn+1 = un-1 + vn-1 + un-2 + vn-2 + un-3 + vn-3 + un-4 + vn-4` for `n >= 0`, with `uj=vj=0` for `j<0`.
        *   **Recommended Sequences (`T >= 5`):** Set `P = T-2`. The sequences `un` and `vn` must be defined by `un+1 = Sum(un-k + vn-k)` for `k=1` to `r` and `un = Sum(un-k + vn-k)` for `k=r+1` to `P`, where `r = floor(P/2)`, `v0 = 1`, and `uj=vj=0` for `j<0`.
        *   **Initial Distribution (`T >= 5`):** For level `n+1`, place `wn + wn-1 + ... + wn-p+1` runs on tape `k` (for `1 <= k <= P`), and `wp + ... + wn-p` runs on tape `T`. Tape `T-1` must be used for input during initial distribution for level `n+1`.
        *   **Specific Sequences (`T=4`):** Set `v2=0, u1=1, v1=0, u0=0, v0=1` and `vn+1 = un-1 + vn-1`, `un = un-2 + vn-2` for `n >= 2`.

## XII. Searching & Tree Manipulation Algorithms

1.  **General Tree Traversal & Management:**
    *   To traverse a nonempty forest in preorder: first, visit the root of the first tree; second, traverse the subtrees of the first tree; third, traverse the remaining trees.
    *   To traverse a nonempty forest in postorder: first, traverse the subtrees of the first tree; second, visit the root of the first tree; third, traverse the remaining trees.
    *   For unthreaded trees, calculate preorder successors using an auxiliary stack.
    *   For threaded trees, perform attaching operations (in copying or insertion) using Algorithm I.
    *   A right-threaded binary tree must use threaded `RLINK`s and represent empty left subtrees with `LLINK = Λ`.
    *   A left-threaded binary tree must thread only null `LLINK`s.
    *   Right thread links must go from the rightmost child of a family to the parent in a threaded binary tree representation of a forest.
    *   `Algorithm S` adaptation: To traverse right-threaded binary trees in symmetric order using `Algorithm S`, change the test "LTAG = 0" in step S2 to "LLINK # Λ".
    *   No auxiliary stack must be used for algorithms testing tree comparison (T < T', T > T', T equivalent to T').
    *   No auxiliary stack must be used for an algorithm to erase a right-threaded binary tree.
    *   `Algorithm I` step I2 is necessary only when inserting into the midst of a threaded tree (not merely inserting a new leaf).
    *   `Algorithm C` termination: Terminates if `P = HEAD` (or equivalently if `Q = RLINK(U)`, assuming `NODE(U)` has a nonempty right subtree).
2.  **Fibonaccian Search (Algorithm F):**
    *   **F1 Initialization:** Initialize `i` to `Fk-1`, `p` to `Fk-1`, and `q` to `Fk-2`.
    *   **F2 Consecutive Fibonacci Numbers:** Ensure `p` and `q` remain consecutive Fibonacci numbers throughout the algorithm.
    *   **F2 Key Comparison:** If `K < Ki`, transition to step F3. If `K > Ki`, transition to step F4. If `K = Ki`, terminate the algorithm successfully.
    *   **F3 Key Less Than `Ki`:** If `q` equals 0, terminate the algorithm unsuccessfully. Otherwise (if `q` is not 0), update `i` to (`i - q`), update `p` to `q` and `q` to (`p` - `q`) (using the *old* `p` value). After updates in F3, return to step F2.
    *   **F4 Key Greater Than `Ki`:** If `p` equals 1, terminate the algorithm unsuccessfully. Otherwise (if `p` is not 1), update `i` to (`i + q`), update `p` to (`p - q`) (using the *old* `p` value), and update `q` to (`q - p`) (using the *old`p` and `q` values). After updates in F4, return to step F2.
3.  **Binary Search Tree Operations (Algorithms T & D):**
    *   **Algorithm T - T1 Initialization:** Initialize P to `ROOT`.
    *   **Algorithm T - T2 Key Comparison:** If `K < KEY(P)`, transition to step T3. If `K > KEY(P)`, transition to step T4. If `K = KEY(P)`, terminate the algorithm successfully.
    *   **Algorithm T - T3 Left Subtree Traversal:** If `LLINK(P)` is not null (Λ), update P to `LLINK(P)` and return to step T2. Otherwise (if `LLINK(P)` is null), transition to step T5.
    *   **Algorithm T - T4 Right Subtree Traversal:** If `RLINK(P)` is not null (Λ), update P to `RLINK(P)` and return to step T2. Otherwise (if `RLINK(P)` is null), transition to step T5.
    *   **Algorithm T - T5 New Node Allocation:** Allocate a new node and set Q to its address (from `AVAIL`). Set `KEY(Q)` to `K`. Set `LLINK(Q)` to null (Λ). Set `RLINK(Q)` to null (Λ). If `K` was less than `KEY(P)`, set `LLINK(P)` to Q. Otherwise (if `K` was not less than `KEY(P)`), set `RLINK(P)` to Q.
    *   **Algorithm T - Stable Sorting Modification:** When using Algorithm T for sorting, if `K = KEY(P)` in step T2, treat it as if `K > KEY(P)` to achieve stable sorting. Avoid this modification if many duplicate keys are present, as it can lead to unbalanced trees and slower sorting.
    *   **Algorithm D - D1 Initialization:** Initialize T to Q.
    *   **Algorithm D - D2 Right Subtree Check:** If `RLINK(T)` is null (Λ), update Q to `LLINK(T)` and transition to step D4.
    *   **Algorithm D - D3 Successor Finding and Relinking:** Set R to `RLINK(T)`. If `LLINK(R)` is null (Λ), set `LLINK(R)` to `LLINK(T)` and set Q to R. Then transition to step D4. Otherwise, set S to `LLINK(R)`. If `LLINK(S)` is not null (Λ), update R to S and repeat step D3 until `LLINK(S)` is null. After loop, set `LLINK(S)` to `LLINK(T)`, set `LLINK(R)` to `RLINK(S)`, set `RLINK(S)` to `RLINK(T)`, and set Q to S.
    *   **Algorithm D - D4 Node Return:** Return the node pointed to by T to the free storage pool (by setting `AVAIL` to T).
    *   **Algorithm D - Optional Modification:** Between D1 and D2, if `LLINK(T)` is null (Λ), set Q to `RLINK(T)` and transition to D4.
4.  **Optimal BST Construction (Algorithm K):**
    *   **Algorithm K - K1 Initialization (Base Cases):** For `0 ≤ i ≤ n`, initialize `c[i,i]` to 0. For `0 ≤ i ≤ n`, initialize `w[i,i]` to `qi`.
    *   **Algorithm K - K1 Weight Calculation:** For `j` from `i+1` to `n`, set `w[i,j]` to `w[i,j-1] + pj + qj`.
    *   **Algorithm K - K2 Initialization (Length 1):** For `1 ≤ j ≤ n`, set `c[j-1,j]` to `w[j-1,j]`. For `1 ≤ j ≤ n`, set `r[j-1,j]` to `j`.
    *   **Algorithm K - K3 Length Loop:** Execute step K3 for `d` values from 2 to `n`. After the `d` loop, terminate the algorithm.
    *   **Algorithm K - K4 Range Loop:** Execute step K4 for `j` values from `d` to `n`.
    *   **Algorithm K - K4 Index Setting:** Set `i` to `j - d`.
    *   **Algorithm K - K4 Cost Calculation:** Calculate `c[i,j]` as `w[i,j] + min(c[i,k-1] + c[k,j])` for `k` in the range `r[i,j-1]` to `r[i+1,j]`.
    *   **Algorithm K - K4 Root Selection:** Set `r[i,j]` to a `k`-value that achieves this minimum.
    *   **Algorithm K - Tree Construction:** If `i` equals `j`, the tree `t(i,j)` must be null. Otherwise, the left subtree of `t(i,j)` must be `t(i, r[i,j]-1)`, and the right subtree must be `t(r[i,j], j)`.
5.  **Balanced Tree Operations (Algorithms A & C):**
    *   **Algorithm A (AVL Tree Insertion):**
        *   **Precondition:** The input must be a table of records forming a balanced binary tree. **Postcondition:** If `K` is inserted, the tree must be rebalanced to maintain its balanced property.
        *   **A1 Initialization:** Initialize T to `HEAD`. Initialize S and P to `RLINK(HEAD)`.
        *   **A2 Key Comparison:** If `K < KEY(P)`, transition to A3. If `K > KEY(P)`, transition to A4. If `K = KEY(P)`, terminate successfully.
        *   **A3 Left Subtree Traversal/Insertion:** Set Q to `LLINK(P)`. If Q is null (Λ), allocate a new node from `AVAIL` to Q, set `LLINK(P)` to Q, and transition to A5. Otherwise (if Q is not null), if `B(Q)` is not 0, set T to P and S to Q. Finally, set P to Q and return to A2.
        *   **A4 Right Subtree Traversal/Insertion:** Set Q to `RLINK(P)`. If Q is null (Λ), allocate a new node from `AVAIL` to Q, set `RLINK(P)` to Q, and transition to A5. Otherwise (if Q is not null), if `B(Q)` is not 0, set T to P and S to Q. Finally, set P to Q and return to A2.
        *   **A5 New Node Setup:** Set `KEY(Q)` to `K`. Set `LLINK(Q)` to null (Λ). Set `RLINK(Q)` to null (Λ). Set `B(Q)` to 0.
        *   **A6 Path Traversal & Balance Factor Update:** If `K < KEY(S)`, set `a` to -1; otherwise, set `a` to +1. Initialize R and P to `LINK(a,S)`. Loop: While P is not equal to Q: If `K < KEY(P)`, set `B(P)` to -1 and P to `LLINK(P)`. If `K > KEY(P)`, set `B(P)` to +1 and P to `RLINK(P)`.
        *   **A7 Rebalancing (Cases):** If `B(S)` is 0, set `B(S)` to `a`, increment `LLINK(HEAD)` by 1, and terminate. If `B(S)` is -`a`, set `B(S)` to 0 and terminate. If `B(S)` is `a`: If `B(R)` is `a`, transition to A8. If `B(R)` is -`a`, transition to A9.
        *   **A8 Single Rotation:** Set P to R. Set `LINK(a,S)` to `LINK(-a,R)`. Set `LINK(-a,R)` to S. Set `B(S)` and `B(R)` to 0. Transition to A10.
        *   **A9 Double Rotation:** Set P to `LINK(-a,R)`. Set `LINK(-a,R)` to `LINK(a,P)`. Set `LINK(a,P)` to R. Set `LINK(a,S)` to `LINK(-a,P)`. Set `LINK(-a,P)` to S. Adjust `B(S)` and `B(R)` based on `B(P)` as per the provided table. Set `B(P)` to 0.
        *   **A10 Finishing Touch:** If S equals `RLINK(T)`, set `RLINK(T)` to P. Otherwise, set `LLINK(T)` to P.
    *   **Algorithm B (Ranked Tree Search):**
        *   **Preconditions:** Input `k` (the desired position) and the tree must have `LLINK`, `RLINK` fields, a `HEAD` node, and a `RANK` field.
        *   **B1 Initialization:** Initialize M to `k`. Initialize P to `RLINK(HEAD)`.
        *   **B2 Null Tree Check/Position Comparison:** If P is null (Λ), terminate unsuccessfully. If `M < RANK(P)`, transition to B3. If `M > RANK(P)`, transition to B4. If `M = RANK(P)`, terminate successfully (P points to the node).
        *   **B3 Left Subtree Traversal:** Set P to `LLINK(P)`. Return to B2.
        *   **B4 Right Subtree Traversal:** Set M to (`M - RANK(P)`). Set P to `RLINK(P)`. Return to B2.
    *   **Algorithm C (Ranked Tree Insertion):**
        *   **Preconditions:** Input `k` (insertion position) and Q (pointer to new node). The tree must be non-empty, have `LLINK`, `RLINK`, `B` fields, a `HEAD` node, and a `RANK` field.
        *   **C1 Initialization:** Initialize T to `HEAD`. Initialize S and P to `RLINK(HEAD)`. Initialize U and M to `k`.
        *   **C2 Position Comparison:** If `M < RANK(P)`, transition to C3; otherwise transition to C4.
        *   **C3 Left Subtree Traversal/Insertion:** Increment `RANK(P)` by 1. Set R to `LLINK(P)`. If R is null (Λ), set `LLINK(P)` to Q and transition to C5. Otherwise (if R is not null), if `B(R)` is not 0, set T to P, S to R, and U to M. Finally, set P to R and return to C2.
        *   **C4 Right Subtree Traversal/Insertion:** Set M to (`M - RANK(P)`). Set R to `RLINK(P)`. If R is null (Λ), set `RLINK(P)` to Q and transition to C5. Otherwise (if R is not null), if `B(R)` is not 0, set T to P, S to R, and U to M. Finally, set P to R and return to C2.
        *   **C5 New Node Setup:** Set `RANK(Q)` to 1. Set `LLINK(Q)` to null (Λ). Set `RLINK(Q)` to null (Λ). Set `B(Q)` to 0.
        *   **C6 Path Traversal & Balance Factor Update:** Set M to U. If `M < RANK(S)`, set R and P to `LLINK(S)` and set `a` to -1. Otherwise, set R and P to `RLINK(S)`, set `a` to +1, and set M to (`M - RANK(S)`). Loop: While P is not equal to Q: If `M < RANK(P)`, set `B(P)` to -1 and P to `LLINK(P)`. If `M > RANK(P)`, set `B(P)` to +1, M to (`M - RANK(P)`), and P to `RLINK(P)`.
        *   **C7 Rebalancing (Cases):** If `B(S)` is 0, set `B(S)` to `a`, increment `LLINK(HEAD)` by 1, and terminate. If `B(S)` is -`a`, set `B(S)` to 0 and terminate. If `B(S)` is `a`: If `B(R)` is `a`, transition to C8. If `B(R)` is -`a`, transition to C9.
        *   **C8 Single Rotation:** Set P to R. Set `LINK(a,S)` to `LINK(-a,R)`. Set `LINK(-a,R)` to S. Set `B(S)` and `B(R)` to 0. If `a` is +1, set `RANK(R)` to (`RANK(R) + RANK(S)`). If `a` is -1, set `RANK(S)` to (`RANK(S) - RANK(R)`). Transition to C10.
        *   **C9 Double Rotation:** Perform all operations of Algorithm A, step A9. If `a` is +1, set `RANK(R)` to (`RANK(R) - RANK(P)`) and `RANK(P)` to (`RANK(P) + RANK(S)`). If `a` is -1, set `RANK(P)` to (`RANK(P) + RANK(R)`) and `RANK(S)` to (`RANK(S) - RANK(P)`).
        *   **C10 Finishing Touch:** If S equals `RLINK(T)`, set `RLINK(T)` to P. Otherwise, set `LLINK(T)` to P.
    *   **General Deletion in Balanced Trees:**
        *   A deletion algorithm must construct a path list `(P0,a0), ..., (Pl,al)`. `P0` must be `HEAD`. `a0` must be `+1`. `LINK(ai, Pi)` must equal `Pi+1` for `0 ≤ i < l`. `Pl` must equal P. `LINK(al, Pl)` must be null (Λ).
        *   When deleting P, set `LINK(aj-1,Pj-1)` to `LINK(-aj, Pj)`.
        *   Adjust the balance factor at node `Pj-1`.
        *   If `k` is 0, decrement `LLINK(HEAD)` by 1 and terminate.
        *   **Rebalancing Cases:** If `B(Pj)` equals `aj`, set `B(Pj)` to 0, decrement `k` by 1, and repeat the adjustment procedure. If `B(Pj)` equals 0, set `B(Pj)` to `-aj` and terminate. If `B(Pj)` equals `-aj`, rebalancing is required.
    *   **Concatenation in Balanced Trees:**
        *   When concatenating L1 and L2, all keys in L1 must be greater than all keys in L2.
        *   If `height(L1) > height(L2)` (or symmetrically for L2), delete the first node of L1 as juncture node J.
        *   From the modified L1 (`L'1`), traverse down the right links until a node P is found where `height(P) - height(L2)` is 0 or 1. Adjust `L'1` as if J was inserted by Algorithm A.
6.  **Garsia-Wachs Algorithm (Algorithm G):**
    *   **Input Preconditions:** Input weights (`w0` to `wn`) must be nonnegative.
    *   **Node Storage:** Nodes must be stored in an an array `X` of size `2n+2`, indexed 0 to `2n+1`.
    *   **Node Fields:** Each node must have `WT`, `LLINK`, `RLINK`, and `LEVEL` fields.
    *   **Node Range:** `X0` to `Xn` must represent leaves. `Xn+1` to `X2n` must represent internal nodes. `X2n` must be the root.
    *   **Sentinel Node:** `X2n+1` must be used as a temporary sentinel.
    *   **Working Array:** A working array of pointers `P0` to `Pt` must be maintained.
    *   **G1 Initialization:** For `0 ≤ k ≤ n`, set `WT(Xk)` to `wk`, and `LLINK(Xk)` and `RLINK(Xk)` to null (Λ). Set `P0` to `X2n+1`, `WT(P0)` to infinity (∞). Set `P1` to `X0`. Set `t` to 1 and `m` to `n`.
    *   **G2 Main Loop:** Perform step G2 for `i` from 1 to `n`. After the `i` loop, transition to G3. The condition `WT(Pi-1) > WT(Pi)` must hold for `1 < i ≤ t`. If `WT(Pt-1) < wi`, set `k` to `t`, perform Subroutine C, and repeat step G2. Otherwise, increment `t` by 1. Otherwise, set `Pt` to `Xi`.
    *   **G3 Final Combination:** While `t` is greater than 1, set `k` to `t` and perform Subroutine C. `P1` must be `X2n` (the root) after phase 1. `WT(P1)` must equal the sum of all weights (`w0 + ... + wn`).
    *   **G4 Level Number Calculation:** Calculate and set `lk` to the distance of node `Xk` from node `P1` for `0 ≤ k ≤ n`. Construct a new binary tree by changing links `Xn+1` to `X2n`. The new tree must have the same level numbers `lk`. The leaf nodes must be in symmetric order (X0 to Xn).
    *   **Subroutine C:** Purpose: Combine two weights and shift weights left as appropriate, maintaining the 2-descending condition (31). Precondition: `k` must be greater than 2 at the start of C1.
        *   **C1 Increment `m`:** Increment `m` by 1. Set `LLINK(Xm)` to `Pt-1`. Set `RLINK(Xm)` to `Pt`. Set `WT(Xm)` to the sum of `WT(Pt-1)` and `WT(Pt)`, and store this sum in `w`.
        *   **C2 Decrement `t`:** Decrement `t` by 1.
        *   **C3 Shift Pointers:** For `j` from `k` to `t-1`, set `Pj` to `Pj+1`.
        *   **C4 Find Insertion Point:** Set `j` to `k - 2`. While `WT(Pj)` is less than `w`, set `Pj+1` to `Pj` and decrement `j` by 1. Set `Pj+1` to `Xm`.
        *   **C5 Exit/Recursive Call:** If `j` equals 0 OR `WT(Pj-1)` is greater than `w`, exit the subroutine. Otherwise, set `k` to `j`. Set `j` to (`t - j`). Call Subroutine C recursively. Reset `j` to (`t - j`) (accounting for possible changes in `t`). Return to step C5.

## XIII. Exact Cover & Backtracking Algorithms

1.  **General Backtracking Principles:**
    *   **Cutoff Property Validity:** A cutoff property `P_l(x_1,...,x_l)` must be true whenever its predecessor `P_l-1(x_1,...,x_l-1)` is true.
    *   **Cutoff Property Testability:** A cutoff property `P_l(x_1,...,x_l)` must be fairly easy to test if `P_l-1(x_1,...,x_l-1)` holds.
    *   **Initial Property Assumption:** The initial property `P_0()` must always be true.
    *   **Downdate Order:** When backtracking, downdate operations must undo changes in precisely the reverse order they were made.
2.  **Algorithm Execution & Control Flow:**
    *   **General Initialization:** At the start of an algorithm (e.g., General Backtrack, Algorithm B, Algorithm W, Algorithm M), the current level `l` must be set to 1, and all necessary data structures must be initialized.
    *   **Solution Identification:** If the current level `l` is greater than `n`, the sequence `x_1...x_n` must be visited as a solution.
    *   **Level Entry - First Choice:** When entering a new level `l`, `x_l` must be set to the smallest element of its domain `D_l`, or the minimum valid choice from the determined set of choices `S_l`.
    *   **Property Check and Advance:** If `P_l(x_1,...,x_l)` holds, data structures must be updated, `l` incremented, and the algorithm must re-enter the level entry step.
    *   **Next Element Trial:** If `x_l` is not the maximum element of `D_l` (or `x_l` is not the last element removed from `S_l`), `x_l` must be set to the next larger element in `D_l` (or removed from `S_l`), and the property must be re-evaluated.
    *   **Backtrack Condition:** If `l` is greater than 0, data structures must be downdated, and the algorithm must return to the "Try again" (or "Try to advance") step. Otherwise, the algorithm terminates.
    *   **Database Compression:** If `up` is not equal to 0 at the beginning of step `N4`, the database must be compressed.
    *   **Deletion Mechanism:** To delete an entry `(sj, cj)`, it must be replaced by `(sN, cN)`, and `N` must be decremented by 1.
    *   **Clause Generator Restart:** If no items are selected (with a probability of `(1-p)^m`), the clause generator must restart.
3.  **Data Structures & Operations (Dancing Links):**
    *   **Doubly Linked List Deletion:** To delete node `X` from a doubly linked list, set `RLINK(LLINK(X)) := RLINK(X)` and `LLINK(RLINK(X)) := LLINK(X)`.
    *   **Doubly Linked List Undeletion (Dancing Links):** To undo the deletion of node `X`, set `RLINK(LLINK(X)) := X` and `LLINK(RLINK(X)) := X`.
    *   **Node Persistence:** In backtrack applications, `LLINK(X)` and `RLINK(X)` must remain unchanged after deletion (no garbage collection or clearing).
    *   **Item Records:** Item records must have `NAME`, `LLINK`, and `RLINK` fields.
    *   **Nodes:** Nodes must have `TOP`, `ULINK`, and `DLINK` fields.
    *   **Option Traversal:** Options must be traversable cyclically in both directions. Options cannot be empty.
4.  **Exact Cover Problem & Algorithms (Dancing Links):**
    *   **Problem Definition:** An exact cover problem involves options (sets of items) and items, where the goal is to find disjoint options that cover all primary items exactly once and secondary items at most once.
    *   **Primary Item Constraint:** Every primary item must be covered exactly once.
    *   **Secondary Item Constraint:** Secondary items must be covered at most once.
    *   **Option Inclusion:** Every option must include at least one primary item. Purely secondary options are excluded.
    *   **Active List Contents:** Only primary items appear in the algorithm's active list.
    *   **Item Header `LEN` Field:** The `TOP` field in item headers is used as `LEN` to store the count of active options for that item.
    *   **Spacer Node Identification:** Spacer nodes are identified by `TOP(x) < 0`.
    *   **Spacer Fields:** `ULINK(x)` must store the address of the first node in the option *before* `x`. `DLINK(x)` must store the address of the last node in the option *after* `x`.
    *   **Strict Exact Cover Definition:** An exact cover problem is strict if no two rows of the matrix are identical, and no two columns are identical.
5.  **Exact Covering with Colors (XCC):**
    *   **Color Assignment:** A color must be assigned to the secondary items of each option. A secondary item not followed by a colon is implicitly assigned a unique color that does not match any other option's color.
    *   **Secondary Item Color Constraint:** Every secondary item must be assigned at most one color.
    *   **Node `COLOR` Field:** Nodes representing items explicitly assigned a color must have a `COLOR` field set to that positive color value. Header `COLOR` fields need not be initialized. Spacer `COLOR` fields must be non-negative.
    *   **`hide'(p)` Behavior:** When hiding an option node `q`, if `COLOR(q)` is less than 0, it must be ignored.
    *   **`unhide'(p)` Behavior:** When unhiding an option node `q`, if `COLOR(q)` is less than 0, it must be ignored.
    *   **`commit(p, j)` Behavior:** If `COLOR(p)` is 0, `cover'(j)` must be called. If `COLOR(p)` is positive, `purify(p)` must be called.
    *   **`purify(p)` Definition:** Set `COLOR` of item header `TOP(p)` to `COLOR(p)`. Iterate through options for item `TOP(p)`. If an option's `COLOR` matches `COLOR(p)`, set its `COLOR` to -1. Otherwise, `hide'(q)`.
    *   **`uncommit(p, j)` Behavior:** If `COLOR(p)` is 0, `uncover'(j)` must be called. If `COLOR(p)` is positive, `unpurify(p)` must be called.
    *   **`unpurify(p)` Definition:** Iterate through options for item `TOP(p)`. If `COLOR(q)` is less than 0, restore it to its original color. Otherwise, `unhide'(q)`.
    *   **Algorithm C `commit`/`uncommit` Calls:** The `commit` and `uncommit` operations in Algorithm C must use the color-aware `cover'`, `hide'`, `uncover'`, and `unhide'` operations.
6.  **Multiple Covering with Multiplicities and Colors (MCC):**
    *   **Primary Item Multiplicity:** Each primary item `j` must occur at least `u_j` times and at most `v_j` times, where `0 <= u_j <= v_j` and `v_j > 0`.
    *   **Primary Item `SLACK` Field:** The `SLACK` field must be set to `v - u` at initialization, and its value must never be changed.
    *   **Primary Item `BOUND` Field:** The `BOUND` field must be set to `v` at initialization, will decrease dynamically, and must never be exceeded.
    *   **`tweak(x, p)` Preconditions:** This operation must only be called when `x = DLINK(p)` and `p = ULINK(x)`.
    *   **0-or-1 Multiplicity Constraint:** If an item `p` has 0-or-1 multiplicity, `cover'(p)` must be invoked instead of hiding options individually.
    *   **`tweak'(x, p)` Operation:** Must be like `tweak(x, p)` but omit the `hide'(x)` operation.
    *   **`untweak'(l)` Operation:** Must be like `untweak(l)` but omit `unhide'(x)` and call `uncover'(p)` after restoring `LEN(p)`.
    *   **MCC Initialization:** Problems must be initialized with MCC memory setup including multiplicity specifications.
    *   **Branching Degree Check:** If the branching degree of a chosen item `i` is zero, the algorithm must leave the current level.
    *   **Bound Decrement & Cover:** When preparing to branch on `i`, `BOUND(i)` must be decremented. If `BOUND(i)` becomes zero, `cover'(i)` must be called.
    *   **Primary Item Update in Option Loop:** When iterating through items `j` in an option (`p`), if `j` is a primary item, `BOUND(j)` must be decremented. If `BOUND(j)` becomes zero, `cover'(j)` must be called.
    *   **Primary Item Rollback in Option Loop:** When un-iterating through items `j` in an option (`p`), if `j` is a primary item, `BOUND(j)` must be incremented. If `BOUND(j)` becomes one, `uncover'(j)` must be called.
    *   **Item Restoration:** If an item was processed with 0-or-1 multiplicity, `uncover'(i)` must be called. Otherwise, `untweak(l)` or `untweak'(l)` must be called. In all cases, `BOUND(i)` must be incremented.
    *   **Chosen Option Level Exit:** If an option `x_I` was chosen at level `l`, the item `i` associated with `x_I` must be reactivated, and the algorithm must return to the item restoration step.

## XIV. Combinatorial Problem Definitions & Constraints

1.  **General Problem Formulation:**
    *   Problems stated for directed graphs are applicable to undirected graphs, unless the digraph *must* be acyclic. (An undirected edge `u—v` is equivalent to directed arcs `u—>v` and `v—>u`).
    *   When presenting problems, the goal is usually to find at least one explicit solution, count the number of solutions, visit all solutions, or find an optimum solution.
    *   Utilize specific internal data structures and variables as defined (e.g., `AVAIL stack`, `HEAP array`, `MEM array`, `VAL array`, `AGILITY variable`, `BSTAMP counter`, `ISTAMP counter`, `TIMP tables`, `BINP tables`, `ISTACK array`, `VAR array`, `UNDO stack`, `DLINK`, `ULINK`, `LEN` fields for dancing links). Adhere to their defined usage within relevant algorithms.
    *   Arithmetic overflow must be avoided in calculations.
    *   Implement logic to avoid adjacent pairs of letters in certain problems.
    *   Implement logic to avoid specific submatrices (quad-free matrices).
    *   The agility threshold must be denoted by `A`.
    *   The confidence level must be denoted by `f`.
2.  **Boolean Function Problems:**
    *   **kSAT Problem:** The Boolean function `f` must be a conjunction of clauses. Each clause must be a disjunction of at most `k` literals (e.g., `x_i` or `~x_i`). (Horn Clauses variant): Each clause must have at most one nonnegated literal.
    *   **Boolean Chain Problem:** Each `a_k` (for `n < k < N`) must be a Boolean function of `x_i` and `a_j` (for some `i < k` and `j < k`). Each given function must be either a constant or equal to `x_l` (for some `l < N`). The goal is usually to minimize `N`.
    *   **Broadword Chain Problem:** Must use bitwise AND/OR or arithmetic operations on integers modulo `2^d`. The value of `d` can be arbitrarily large.
    *   **Boolean Programming Problem:** Find Boolean values `x_1, ..., x_n` such that `f(x_1,...,x_n) = 1`. The weighted sum `w_1x_1 + ... + w_nx_n` must be maximized.
3.  **Graph & Network Problems:**
    *   **Matching Problem:** Find a set of disjoint edges. (Bipartite Graph variant): Select a set of 1s in an `m x n` matrix of 0s and 1s, with at most one selected in each row and at most one selected in each column.
    *   **Assignment Problem:** Maximize the total weight of the matching. (Matrix equivalence): Select elements of an `m x n` matrix, at most one per row and at most one per column, such that the sum of selected elements is as large as possible.
    *   **Covering Problem:** Given a 0-1 matrix `A_jk`, find a set of rows `R` such that `sum_{j in R} A_jk > 0` for all `k`. The goal is usually to minimize `|R|`.
    *   **Independent Set Problem:** Find a set of vertices `U` such that the induced graph `G | U` has no edges. The goal is usually to maximize `|U|`.
    *   **Clique Problem:** Find a set of vertices `U` such that the induced graph `G | U` is complete. The goal is usually to maximize `|U|`.
    *   **Vertex Cover Problem:** Find a set of vertices `U` such that every edge includes at least one vertex of `U`. The goal is usually to minimize `|U|`.
    *   **Dominating Set Problem:** Find a set of vertices `U` such that every vertex not in `U` is adjacent to some vertex of `U`.
    *   **Kernel Problem (Directed Graph):** Find an independent set of vertices `U` such that every vertex not in `U` is the predecessor of some vertex of `U`. (Undirected Graph variant): A kernel is equivalent to a maximal independent set and to a dominating set that is both minimal and independent.
    *   **Coloring Problem:** Partition the graph's vertices into `k` independent sets. Never assign the same color to adjacent points. The goal is usually to minimize `k`.
    *   **Shortest Path Problem:** Find the smallest total weight of an oriented path from `u` to `v`.
    *   **Longest Path Problem:** Find the largest total weight of a simple oriented path from `u` to `v`.
    *   **Reachability Problem:** Find all vertices `v` such that `u—* v` for some `u ∈ U`.
    *   **Spanning Tree Problem:** Find a free tree `F'` on the same vertices, such that every edge of `F'` is an edge of `G`. (Minimum Spanning Tree variant): A spanning tree of smallest total weight.
    *   **Hamiltonian Path Problem:** Find a path `P` on the same vertices, such that every edge of `P` is an edge of `G`. The path `P` must encounter every vertex exactly once.
    *   **Hamiltonian Cycle Problem:** Find a cycle `C` on the same vertices, such that every edge of `C` is an edge of `G`. The cycle `C` must encounter every vertex exactly once and return to the starting point.
    *   **Traveling Salesrep Problem:** Find a Hamiltonian cycle of smallest total weight. If the graph has no Hamiltonian cycle, extend it to a complete graph by assigning a very large weight `W` to every nonexistent edge.
    *   **Topological Sorting Problem:** Label each vertex `x` with a distinct number `I(x)` such that `x—>y` implies `I(x) < I(y)`. Such a labeling is possible if and only if the given digraph is acyclic.
    *   **Optimum Linear Arrangement Problem:** Label each vertex `x` with a distinct integer `I(x)` such that `sum |I(u) - I(v)|` is as small as possible.
    *   **Nearest Common Ancestor Problem:** Find `w` such that every inclusive ancestor of `u` and of `v` is also an inclusive ancestor of `w`.
    *   **Range Minimum Query Problem:** Find the minimum elements of each subinterval `a_i, ..., a_j` for `1 ≤ i ≤ j ≤ n`.
4.  **Optimization & Arrangement Problems:**
    *   **Knapsack Problem:** Find `K ⊆ {1,...,n}` such that `sum_{i ∈ K} w_i ≤ W`. The sum `sum_{k ∈ K} v_k` must be maximized.
    *   **Orthogonal Array Problem:** Find an `m x n^2` array with entries `A_jk ∈ {0,1,...,n-1}`. The array must have the property that if `j ≠ j'` and `k ≠ k'`, then `(A_jk, A_j'k') ≠ (A_jk', A_j'k)`.
    *   **Universal Cycle Problem:** Find a cyclic sequence of elements (of `b`-ary digits) with the property that all combinatorial arrangements of a particular kind are given by consecutive `k`-tuples.
        *   (De Bruijn Cycle): `N` must equal `b^k`, and all possible `k`-tuples must appear.
        *   (Universal Cycle of Combinations): `N` must equal `(b choose k)`, and all `k`-combinations of `b` things must appear.
        *   (Universal Cycle of Permutations): `N` must equal `b!`, `k` must equal `b-1`, and all `(b-1)`-variations must appear as `k`-tuples.
5.  **Boolean Function Specifics:**
    *   A truth table of order `n` is a binary string of length `2^n`.
    *   A bead of order `n` is a truth table `B` of order `n` that is not a square (i.e., `B` doesn't have the form `aa` for any string `a` of length `2^(n-1)`).
    *   Boolean Difference: `(Delta_j) f` must be defined as `f_0 XOR f_1`.
    *   Existential quantification `(Ex_j) f` must be defined as `f_0 V f_1`.
    *   Universal quantification `(All_j) f` must be defined as `f_0 A f_1`.
    *   `f_c` must denote `f` with `x_j` replaced by `c`.
    *   `(ExistsNot_j) f` must be defined as `f_0 AND (NOT f_1)`.
    *   `(NotExists_j) f` must be defined as `(NOT f_0) AND f_1`.
    *   Monotonicity: A Boolean function `f` is monotone if and only if `(OR_j (NotExists_j) f) = 0`, or equivalently, `(NotExists_j) f = 0` for all `j`. If `f` is monotone, then `f = f_0 V (x_1 AND f_1)`.
    *   Prime Implicants: `PI(f)` must be defined as `PI(f_0) U (e_1 U (PI(f_1) \ PI(f_0)))`. The ZDD for `PI(0)` is `[L]`, and for `PI(1)` is `[T]`.
    *   Sweet Functions: A Boolean function `f` depending on `x_1` is "sweet" if its prime implicants are `P U (e_1 U Q)`, where `P` and `Q` are sweet, independent of `x_1`, and every member of `P` is absorbed by some member of `Q`. The connectedness function of any graph must be considered sweet.
6.  **Permutations & Combinatorics:**
    *   Combinatorics is the study of the ways discrete objects can be arranged into various kinds of patterns.
    *   Multisets are like sets but allow repetitions of identical elements.
    *   Optimality Terminology: Locally optimal combinatorial configurations must be described with "-al" words (e.g., minimal, optimal). Globally optimal configurations must be described with "-um" words (e.g., minimum, optimum).
    *   An inversion in a permutation `a_1 a_2 ... a_n` is a pair `(a_i, a_j)` where `i < j` and `a_i > a_j`.
    *   The inversion table `b_1 b_2 ... b_n` of `a_1 a_2 ... a_n` is where `b_j` is the number of elements to the left of `j` that are greater than `j`.
    *   The inverse permutation `a'_1 a'_2 ... a'_n` of `(1 2 ... n / a_1 a_2 ... a_n)` is such that `a'_k = j` if and only if `a_j = k`.
    *   A permutation is an involution if it is its own inverse.
    *   The index of permutation `a_1 a_2 ... a_n` is the sum of all `j` such that `a_j > a_{j+1}` for `1 <= j < n`.
    *   Runs in a permutation `a_1 a_2 ... a_n` are segments between vertical lines placed at the ends and between `a_j` and `a_{j+1}` whenever `a_j > a_{j+1}`.
    *   Eulerian Numbers `(_k^n_)` represent the number of permutations of `{1,2,...,n}` with `k` descents (or `k` ascents).
    *   A multiset permutation is prime if and only if it is a cycle with no repeated elements.
    *   The two-line notation `(abcdef / cdfbea)` means "the top element becomes the bottom element" (e.g., 'a' becomes 'c').
    *   A cycle `(x1 x2 ... xn)` means "x1 becomes x2, ..., xn-1 becomes xn, xn becomes x1".
    *   Singleton cycles (elements fixed by the permutation) must not be explicitly written in cycle notation.
    *   The identity permutation must be denoted by `()`.
    *   Permutation multiplication means applying one permutation after the other. The multiplication sign `x` must be conventionally dropped.
    *   The document uses `π1 π2` to denote transformation `π1` followed by `π2`.
    *   For ideal output, singleton cycles must be removed from the final product of disjoint cycles.
    *   The canonical cycle form must be unique. To obtain canonical cycle form, explicitly write all singleton cycles, place the smallest number first within each cycle, and order the cycles in decreasing order of their first number.
    *   To reconstruct canonical cycle form from a parenthesis-less sequence, insert a left parenthesis immediately before each left-to-right minimum.
    *   The multiplication of signed permutations must be performed by multiplying their cycles in the normal way, as specified in Section 1.3.3.
    *   A signed involution is a signed permutation of order 1 or 2, which occurs if and only if `o^2 = 1`.
    *   When writing a signed involution `o` in cycle form `(pi ±pj)(...)`, the indices must satisfy `i1 < j1`, `i2 < j2`, ..., `bp < jp`, and `0 < d1 < ... < dp`. The cycle `(pi, ±pj)` must be omitted if `i = j`.
    *   If `o` is an ordinary signless involution, all signs must be eliminated from its cycle form representation.
    *   Cardinality Constraints: `All-different`, `At-most-one`, and `At-least-one` constraints must be implemented where specified.

## Key Highlights

* The document provides a consolidated, de-duplicated, and categorized master list of technical rules, constraints, and operational guidelines for the MMIX Architecture, Algorithms, and Advanced Computing Concepts.
* MMIX architecture mandates two's complement binary arithmetic; unsigned operations never overflow, while signed operations are usually modulo word size, requiring specific instructions for wider results.
* Robust floating point operations must implement `round(true_operation(operands))`, test for exponent underflow/overflow post-rounding, and maintain significant digits for maximum accuracy.
* MMIX data structures require strict octabyte-alignment and utilize low-order bits as tags, which must be masked to zero before using link fields as addresses in load or store instructions.
* Balanced tree algorithms, such as AVL insertion, strictly maintain a height difference of at most one between subtrees for every node, often requiring rebalancing rotations after modifications.
* Solving exact cover problems with Dancing Links involves efficiently covering primary items exactly once and secondary items at most once, utilizing specialized doubly linked list operations for deletion and undeletion.
* All algorithms must specify clear preconditions and postconditions, ensuring valid input states and verifiable output properties, and consistently follow defined initialization and control flow rules.
* A consistent set of naming and mathematical notation conventions, including specific rules for constants, registers, and symbols, is mandated to enhance clarity and uniformity across all technical specifications.
