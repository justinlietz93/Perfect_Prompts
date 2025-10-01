# Physics Rules Distilled from the NIST Digital Library of Mathematical Functions and Associated Documents

**BOOK:** *NIST Digital Library of Mathematical Functions (DLMF)* and related technical physics documents.
**COVERAGE:** Throughout the text, focusing on foundational mathematics, special functions (Struve, Bessel, Lommel, Heun, Mathieu), integral representations, and general mathematical conventions (pages 3-785).
**NOTES:** Mathematical symbols and function notations are precisely defined. Vector calculus adheres to Einstein summation convention and the right-hand rule for cross products. Many functions specify principal branches or values. Numerical computations must adhere to the IEEE Standard for Binary Floating-Point Arithmetic (ANSI/IEEE Std 754-1985).

**Generated on:** September 30, 2025 at 9:38 PM CDT

---

## I. Units, Conventions & Signatures

1. **Standard Mathematical Notation:** All standard mathematical symbols, operators, and functions (e.g., `C`, `D`, `det`, `δ`, `Δ`, `∇`, `D_k`, `∈`, `∉`, `∀`, `⇒`, `⇔`, `!`, `!!`, `⌊x⌋`, `⌈x⌉`, `C(C)`, `<∞`, `≫`, `ℑ`, `inf`, `sup`, `∩`, `∪`, interval notations, `lim inf`, matrix operations, `mod`, `N`, `(a)n`, `Q`, `R`, `ℜ`, `Res`, `S`, `sign x`, `\`, `Z`, `nZ`, `~` for asymptotic equality, `| |` for modulus, vector norms `||.||`, limits `f(c±)`, q-derivatives, factorials, Cauchy principal value `P_v`, loop integrals `∫_C(a,b)`, Pochhammer’s loop integral `P_b(a)`, q-integrals, Jacobi/Legendre Symbols `(a/p)`, q-shifted factorials, Clebsch-Gordan coefficients, binomial/multinomial coefficients, distribution notations, and various named functions like Appell functions, Dawson's integral, Dirac delta, Euler numbers, Fibonacci numbers, Fresnel integrals, Gauss sums, Glaisher’s constant, Gudermannian function, Heaviside function, Hilbert transform, Ince polynomials, inversion numbers, Jacobi's amplitude function, Jordan's function, Kelvin functions, Klein’s complete invariant, Lambert W-function, Lamé functions/polynomials, Lebesgue Constant, Lerch’s transcendent, Levi-Civita symbol, Liouville’s function, Lommel functions, Mangoldt’s function, Meijer G-function, Meixner-Pollaczek polynomial, Mills’ ratio, Möbius function, Motzkin number, Narayana number, Neumann’s polynomial, Neumann series, Neumann boundary conditions, nome, Nörlund polynomials, Olver’s hypergeometric function, partition functions, Pearcey integral, permutations, phase function, Planck's constant (reduced), Pochhammer symbol, polygamma functions, polylogarithm, q-hypergeometric functions, q-Stirling numbers, Racah polynomial, Ramanujan’s sum/tau function, Rayleigh function, Riemann’s P-symbol, Riemann zeta function, Scorer function, Schrödinger number, sinc function, spheroidal wave functions, Stirling numbers, Stokes numbers, Stieltjes polynomials, Stieltjes transform, Struve functions, sum of powers of divisors, symmetric elliptic integrals, tangent numbers, theta functions, 3j/6j/9j/3nj symbols, Chebyshev polynomials, ultraspherical polynomials, Vandermondian, Voigt functions, Weierstrass elliptic functions/sigma/zeta functions, Whittaker confluent hypergeometric function, Wigner symbols, Wilson polynomials, Wronskian, zeros of Bessel/cylinder functions, Zonal polynomials) must be used as defined in the source material.
2. **Principal Values:** Unless indicated otherwise, assume principal values for all mathematical functions (e.g., logarithms, powers, inverse trigonometric functions, inverse hyperbolic functions, fractional powers). Specifically, for `Hν(z)`, `Kν(z)`, `Lν(z)`, `Mν(z)`, ensure principal values correspond to the principal value of `(½z)ν+1`.
3. **Derivative Notation:** Interpret primes (e.g., `f′(x)`) as derivatives with respect to the argument unless otherwise indicated. Differentials (e.g., `d/dx`) may also denote derivatives.
4. **Empty Sums and Products:** Define empty sums as zero and empty products as unity.
5. **Graphical Depiction:**
    * Special functions with one real variable must be depicted using conventional two-dimensional (2D) line graphs.
    * Special functions with two real variables must be depicted as 3D surfaces, with vertical height corresponding to the function value and coloring emphasizing 3D nature.
    * Special functions with a complex variable must be depicted as colored 3D surfaces, with vertical height corresponding to the modulus (absolute value) of the function.
    * When a 4D effect is desired for complex variable functions, use coloring of the surface to indicate the quadrant of the plane to which the phase of the function belongs.
    * For 4D effect graphics, arrange phase colors for the 1st, 2nd, 3rd, and 4th quadrants as blue, green, red, and yellow, respectively, and include a "Quadrant Colors" icon.
6. **Integration Paths:** Define the integration path for orthogonality in specific contexts (e.g., for (31.9) as a Pochhammer double-loop contour, beginning at `z = C`, encircling `z = 1` once in the positive sense, then `z = 0` once in the positive sense, and finally returning to `z = C`).
7. **Mathieu Function Conventions:**
    * The principal value of `v` as a characteristic exponent of Mathieu's equation must ensure `0 < R(v) < 1`.
    * Mathieu functions `ce_2n(z,q)` and `se_(2n+2)(z,q)` must be `pi`-periodic.
    * Mathieu functions `ce_(2n+1)(z,q)` and `se_(2n+1)(z,q)` must be `pi`-antiperiodic.
    * `ce_0(z,0)` must equal `1/sqrt(2)`.
    * For associated functions `fe_n(z,q)` and `ge_n(z,q)`, `fe_2n(z,q)` and `ge_(2n+2)(z,q)` must be `pi`-periodic.
    * `fe_(2n+1)(z,q)` and `ge_(2n+1)(z,q)` must be `pi`-antiperiodic.
    * Normalize `fe_n(z,q)/C_n(q)` to `sin(nz)` as `q -> 0` (for `n != 0`).
    * Normalize `ge_n(z,q)/S_n(q)` to `cos(nz)` as `q -> 0` (for `n != 0`).
    * `a_2n(0)` must equal `n^2` for `n=0,1,2,...`.
    * `b_n(0)` must equal `n^2` for `n=1,2,3,...`.
    * `fe_n(z,0)` must equal `z*cos(nz)`.
    * `ge_n(z,0)` must equal `z*sin(nz)` for `n=1,2,3,...`.
    * Mathieu functions Fourier coefficients must be normalized (p. 657, 666).
    * Mathieu’s equation algebraic form (p. 652) and standard form (p. 652) must be standardized.
    * Modified Mathieu’s equation algebraic form must be standardized (p. 667).
8. **Vector Calculus Conventions:**
    * Define `∇` as the del operator, `∇f` as the gradient, `∇ × F` as the curl, `∇ · F` as the divergence, and `∇²` as the Laplacian.
    * Vectors must follow Einstein summation convention (p. 10).
    * Vectors must follow the right-hand rule for cross products (p. 10).
    * Vector notation must be specified (p. 9, 10).
    * The Levi-Civita symbol `ε_ijk` must be defined.
9. **Matrix Conventions:** Define matrix notation (`[ajk]`, `A−1`, `trA`, `AT`, `I`) as specified.
10. **Coordinate Systems for Laplacian:** The Laplacian `∇²` must be specified for cylindrical, ellipsoidal, polar, spherical, oblate spheroidal, and prolate spheroidal coordinates. Metric coefficients for spheroidal coordinates must also be specified.
11. **Fundamental Constants:** Reduced Planck's constant is specified as a fundamental constant (p. 379, 479, 753).
12. **Error and Precision:** Relative error (p. 73) and relative precision (p. 73) must be specified.
13. **Branch Conventions:** Hankel functions branch conventions must be followed (p. 218). Modified Bessel functions branch conventions must be standardized (p. 249).
14. **Multivalued Functions:** When dealing with multivalued functions, other branches must be clearly identified if not the principal branch (p. 111).

### II. PDE Type, Regularity & Well-Posedness

1. **Function Spaces:** Define `C(I)` or `C(a,b)` as continuous on an interval, `C^n(I)` as continuously differentiable `n` times, `C^∞(I)` as infinitely differentiable, and `D(I)` as a test function space.
2. **Convergence of Series:** Series expansions for `Jν(z)`, `Eν(z)`, `Aν(z)`, `z−ν−1Hν(z)`, and `z−ν−1Lν(z)` must converge absolutely for all finite values of `z`.
3. **Entire Functions:** `z−ν−1Hν(z)` and `z−ν−1Lν(z)` must be treated as entire functions of `z` and `ν`. The Anger function `Jν(z)` and Weber function `Eν(z)` must be entire functions of `z` and `ν`. Solutions of Mathieu's equation `w'' + (a - 2qcos(2z))w = 0` must be entire functions of `z` and, given initial constants, must be entire functions of `z`, `a`, and `q`.
4. **Defining Differential Equations:**
    * Struve functions (`Hν(z)`, `Kν(z)`) are particular solutions of Struve’s Equation (11.2.7).
    * Modified Struve functions (`Lν(z)`, `Mν(z)`) are particular solutions of Modified Struve’s Equation (11.2.9).
    * The Anger function `Jν(z)` and Weber function `Eν(z)` satisfy the inhomogeneous Bessel differential equation (11.10.5).
    * The Lommel inhomogeneous Bessel differential equation (11.9.1) has the general solution (11.9.2).
    * If `φ = π/2`, then the differential equations for `K(k)` and `E(k)` must reduce to hypergeometric differential equations (15.10.1).
    * Use `w'' + (a - 2qcos(2z))w = 0` as the standard form of Mathieu's equation. Algebraic forms are also specified: `4c(1 - c)w'' + 2(1 - 2c)w' + (a - 2q(1 - 2c))w = 0` (for `c = sin^2 z`) and `(1 - c)w'' - cw' + (a + 2q - 4qc^2)w = 0` (for `c = cos^2 z`).
5. **Kernel Differential Equations:**
    * The kernel `K(z,t)` in integral representation (31.10.1) must be a solution of `(D_z - D_t)K = 0` (31.10.3), where `D_z` is Heun's operator (31.10.4).
    * The kernel `K` must satisfy `(31.10.8)` derived from `D_theta K = D_phi K`.
    * The kernel `K(z;s,t)` in integral representation (31.10.12) must be a solution of `((t-z)D_s + (z-s)D_t + (s-t)D_z)K = 0` (31.10.14).
    * The kernel `K` must satisfy `(31.10.18)` derived from `D_u K = D_v K = D_w K`.
    * The kernel equation after spherical coordinate transformation must satisfy Equation (31.10.21), derived from `D_r K = D_theta K = D_phi K`.
6. **Singularities and Analyticity:**
    * Mathieu's algebraic forms have regular singularities at 0 and 1 (with exponents 0 and 1/2), and an irregular singular point at infinity.
    * Confluence of singularities must be identified in the generalized hypergeometric differential equation (p. 410).
    * Singularities must be identified in the generalized hypergeometric differential equation (p. 409).
    * Branch points must be defined for the hypergeometric function (p. 384).
    * Singularities must be defined for the hypergeometric differential equation (p. 395).
    * Branch cuts must be defined for inverse hyperbolic/trigonometric functions (p. 119, 127) and the logarithm (p. 104).
    * Poles must be identified for hyperbolic/trigonometric functions (p. 123) and Weierstrass elliptic functions (p. 570).
    * Singularities must be identified for Lamé’s equation (p. 684) and modified Bessel’s equation (p. 248).
    * A pole (p. 19), essential singularity (p. 19), isolated singularity (p. 19), isolated essential singularity (p. 19), and removable singularity (p. 4, 19) must be defined. The order of a pole must be defined (p. 19).
    * Singularities must be defined for Riemann’s differential equation (p. 396).
    * A Stokes line must be defined (p. 68). Transition points (p. 58, 63) and turning points (p. 58, 63) must be defined, including as fractional or multiple (p. 61).
    * Singularities must be defined for the spheroidal differential equation (p. 698).
    * A movable pole/singularity must be defined (p. 724).
    * Analyticity must be defined for the Laplace transform (p. 28), Mellin transform (p. 29), and Stieltjes transform (p. 30).
    * Characteristic exponents must be defined for Mathieu’s equation (p. 653) and Heun’s equation (p. 710). Branch points must be identified for Mathieu’s equation eigenvalues (p. 661).

### III. Variational Principles & Equations of Motion

1. **Special Function Differential Equations:** Special functions, including the gamma function, generalized hypergeometric functions, Hankel functions, Heun functions, hyperbolic functions, hypergeometric function, incomplete gamma functions, Kelvin functions, Kummer functions, Laguerre polynomials, Legendre polynomials, Legendre’s elliptic integrals, logarithm function, Lommel functions, Mathieu functions, modified Bessel functions, parabolic cylinder functions, repeated integrals of the complementary error function, Scorer functions, spherical Bessel functions, Struve functions, symmetric elliptic integrals, trigonometric functions, ultraspherical polynomials, Weierstrass elliptic functions, and Whittaker functions, must satisfy their specified differential equations.
2. **Floquet Solutions:** For any nontrivial solution `w(z)` of Mathieu's equation, `w(z + pi) = e^(i*v)w(z)` must hold. The coefficients `C_n` of a Floquet solution must satisfy `(a - (v + 2n)^2)Cn + q(Cn-1 + Cn+1) = 0` for `n` in `Z`.
3. **Wronskians:** `W` must be defined as a Wronskian. Explicit forms must exist for Wronskians of Hankel functions, Kummer functions, Mathieu functions, modified Bessel functions, modified Mathieu functions, parabolic cylinder functions, and Whittaker functions.
4. **Recurrence Relations:** Special functions, including the gamma function, generalized exponential integral, incomplete gamma functions, incomplete beta functions, Hankel functions, the hypergeometric function, Jacobi polynomials, Kelvin functions, Kummer functions, Laguerre polynomials, polynomials orthogonal on the unit circle, parabolic cylinder functions, plane partitions, the psi function, repeated integrals of the complementary error function, restricted integer partitions, the Riemann zeta function, spherical Bessel functions, Stirling numbers, Struve functions, 3j symbols, 6j symbols, ultraspherical polynomials, and Whittaker functions, must satisfy their specified recurrence relations.

### IV. Symmetry & Conservation Laws

1. **Equation Invariance:** Mathieu's equation `w'' + (a - 2qcos(2z))w = 0` must remain unchanged under the transformations `z -> -z`, `z -> z + pi`, and `z -> z + pi/2`.
2. **Reflection and Multiplication Formulas:**
    * Special functions (gamma function, Gaussian hypergeometric function, Lommel functions, Mathieu functions, modified Bessel functions, psi function, Riemann zeta function, spherical Bessel functions, Struve functions) must exhibit specified reflection and multiplication formulas.
    * Specifically, `Hν(ze±iπ) = e±iπν Hν(z)` and `Lν(ze±iπ) = e±iπν Lν(z)`.
3. **Symmetry and Parity:**
    * For `n = 0,1,2,...`, `H-n-1/2(z) = (−1)n Jn+1/2(z)` and `L-n-1/2(z) = In+1/2(z)`.
    * `S−μ,ν(z) = Sμ,ν(z)` and `Sμ,−ν(z) = Sμ,ν(z)`.
    * `Jν(−z) = J−ν(z)` and `Eν(−z) = −E−ν(z)`.
    * For Mathieu functions, `w1(z;a,q)` must be an even function, and `w2(z;a,q)` must be an odd function. The Wronskian `W{w1,w2}` must equal `1`.
    * Eigenvalues `a_n(q)` and `b_n(q)` must satisfy `a_n(-q) = a_n(q)` and `b_n(-q) = b_n(q)`.
    * `ce_2n(z,-q)` must be expressed as `(-1)^n ce_2n(pi - z,q)`.
    * `ce_(2n+1)(z,-q)` must be expressed as `(-1)^n se_(2n+1)(pi - z,q)`.
    * `se_(2n+1)(z,-q)` must be expressed as `(-1)^n ce_(2n+1)(pi - z,q)`.
    * `se_(2n+2)(z,-q)` must be expressed as `(-1)^n se_(2n+2)(pi - z,q)`.
    * The Fourier coefficients for Mathieu functions must satisfy specific symmetry relations (e.g., `A_m^(2n)(-q) = (-1)^m A_m^(2n)(q)`).
    * `C_n(-q)` must equal `C_n(q)`. `S_(2n+1)(-q)` must equal `C_(2n+1)(q)`. `S_(2n+2)(-q)` must equal `S_(2n+2)(q)`.
    * The sum of eigenvalues must satisfy `sum( (a_m(q) - m^2) ) = 0`, `sum( (a_(2n+1)(q) - (2n+1)^2) ) = q`, `sum( (b_n(q) - n^2) ) = -q`, `sum( (b_(2n+2)(q) - (2n+2)^2) ) = 0`.
    * The function `R_μ(b_1,b_2,...,b_ν; z_1,z_2,...,z_ν)` must reveal full permutation symmetry.
4. **Orthogonality:**
    * Eigenfunctions must be orthogonal. Specifically: `Integral[0 to pi] ce_n(z,q)ce_m(z,q) dz = 0` if `n != m`, `Integral[0 to pi] se_n(z,q)se_m(z,q) dz = 0` if `n != m`, and `Integral[0 to pi] ce_n(z,q)se_m(z,q) dz = 0`.
    * Other functions that must satisfy orthogonality properties include Jacobi polynomials, Laguerre polynomials, Lamé functions/polynomials, Legendre polynomials, Mathieu functions, orthogonal polynomials on the unit circle (biorthogonal), paraboloidal wave functions, q-Hahn class orthogonal polynomials, radial spheroidal wave functions, scaled spheroidal wave functions, Stieltjes polynomials, 3nj symbols, trigonometric functions, ultraspherical polynomials, Wilson class orthogonal polynomials, and Zonal polynomials.
5. **Transformations and Identities:**
    * Kummer’s transformations must be applied for confluent hypergeometric functions and 3F2 hypergeometric functions of matrix argument.
    * Legendre’s relation must be used for Legendre’s elliptic integrals.
    * The Liouville transformation must be applied for differential equations.
    * Matrices can undergo symmetric tridiagonalization.
    * Modular functions must exhibit modular transformations.
    * Parseval’s formula must be defined for Fourier cosine and sine transforms, Fourier series, and Fourier transforms.
    * Partitions are symmetric.
    * The quadratic reciprocity law must be applied.
    * Regge symmetries must be applied for 3j and 6j symbols.
    * The Riemann identity must be applied for Riemann theta functions.
    * Riemann theta functions must exhibit modular transformations, quasiperiodicity, and symmetry. Riemann theta functions with characteristics must exhibit quasiperiodicity and symmetry.
    * The SL(2,Z) bilinear transformation must be applied.
    * Symmetric elliptic integrals must leverage advantages of symmetry and are defined by permutation symmetry. Transformations replaced by symmetry must be utilized.
    * Canonical integrals must possess symmetries.
    * Theta functions must exhibit periodicity and quasiperiodicity, have a duplication formula, Jacobi’s identity, Jacobi’s triple product, the Landen transformation, and transformation of lattice parameter.
    * 3j symbols must exhibit Regge symmetries and symmetry. 6j symbols must exhibit Regge symmetries and symmetry.
    * Trigonometric functions must have addition formulas, identities, orthogonality, and periodicity.
    * Ultraspherical polynomials must have an addition theorem.
    * Weierstrass elliptic functions must exhibit homogeneity, periodicity, and quasiperiodicity.
    * Whittaker functions must have addition theorems and multiplication theorems.
    * Wilson class orthogonal polynomials transformations of variable must be applied.

### V. Locality, Causality & Constraints

1. **Function Positivity and Conditions:**
    * `Hν(z) > 0` when `z > 0` and `Rν > −1/2`.
    * For products of Struve functions, (11.7.12) applies when `R(ρ+ν) > 0`.
    * If `1 < k_e < 1/sinφ`, then `k_e` must be pure imaginary for Bulirsch's integrals.
    * The infinite series for `ln K(k)` must be equivalent to the infinite product.
2. **Solution Uniqueness and Existence:**
    * If `q != 0`, then for a given value of `v`, the corresponding Floquet solution must be unique (up to a constant factor).
    * A nontrivial solution `C_n` of `(a - (v + 2n)^2)Cn + q(Cn-1 + Cn+1) = 0` that satisfies `lim(n->infinity) |Cn|^(1/|n|) = 0` must lead to a Floquet solution.
3. **Eigenvalue Ordering and Zeros:**
    * For `q>0`, eigenvalues must be ordered as `a_0 < b_1 < a_1 < b_2 < a_2 < b_3 < ...`.
    * For `q<0`, eigenvalues must be ordered as `a_0 < a_1 < b_1 < b_2 < a_2 < a_3 < ...`.
    * For real `q`, `ce_2n(z,q)`, `se_2n+1(z,q)`, `ce_2n+1(z,q)`, and `se_2n+2(z,q)` each must have exactly `n` zeros in `0 < z < pi`.
    * Zeros of Mathieu functions must be continuous in `q`.
    * `W{ce_n, fe_n}` must equal `ce_n(0,q)fe_n'(0,q)`.
    * `W{se_n, ge_n}` must equal `-se_n'(0,q)ge_n(0,q)`.
4. **Integral Representation Conditions:**
    * The integration contour `C` for integral representation (31.10.1) of Type I must be "suitable".
    * The contour `C` for (31.10.1) must satisfy the boundary condition: `p(t) { w(t) (dK/dt) - K (dw/dt) } = 0` (31.10.5).
    * The integration contours `C1` and `C2` for integral representation (31.10.12) of Type II must be "suitable".
    * The contour `C1` for (31.10.12) must satisfy the boundary condition: `p(s) { (s-z) w(s) (dK/ds) - (s-z) K (dw/ds) - K w(s) } = 0` (31.10.15).
    * The contour `C2` for (31.10.12) must satisfy the boundary condition: `p(t) { (t-z) w(t) (dK/dt) - (t-z) K (dw/dt) - K w(t) } = 0` (31.10.16).
    * Parameters `R_gamma_t` and `R_delta_t` must be `> 0` for (31.10.10) (Example 1).
5. **Parameter and Structural Constraints:**
    * Define `Λ` as a lattice in C and `N` as the winding number.
    * Applications of Gauss quadrature must be specified for contour integrals (p. 83).
    * Generalized hypergeometric function arguments must be strictly balanced, k-balanced, Saalschiltzian, very well-poised, or well-poised (p. 405).
    * Hill’s equation properties in the real case and symmetric case must be observed (p. 675).
    * Inverse hyperbolic/trigonometric functions must respect branch cuts and branch points (p. 119, 127).
    * Jacobi, Laguerre, Ultraspherical, and Legendre polynomials must adhere to specific parameter constraints (p. 439, 443).
    * The Jacobi symbol is restricted to prime numbers (p. 642).
    * Kelvin functions usage is restricted to orders ±5 (p. 268).
    * The logarithm function must respect its branch cut (p. 104).
    * Series convergence must be ensured via the M-test for uniform convergence (p. 21).
    * Mathieu’s equation parameters must be classified (p. 710).
    * The Mellin transform must satisfy convergence conditions (p. 29).
    * Permutations are restricted to specific positions (p. 633).
    * Power series must meet convergence conditions (p. 17) and define a radius of convergence (p. 17).
    * The q-hypergeometric function must be balanced, k-balanced, nearly-poised, well-poised, or very-well-poised (p. 423).
    * Riemann theta functions must respect the fundamental parallelogram (p. 524) and define rate-period characteristics (p. 539).
    * Stable polynomials must satisfy the Hurwitz criterion (p. 23).
    * The Stieltjes transform must satisfy convergence conditions (p. 30).
    * Tempered distributions must meet convergence conditions (p. 36).
    * 3j symbols must adhere to triangle conditions (p. 758).
6. **Compatibility Conditions:**
    * Heun’s equation compatibility conditions must be met (p. 728-729).
    * Painlevé equations' isomonodromy problems must meet compatibility conditions (p. 728).
    * Modified Mathieu functions and radial Mathieu functions joining factors must be specified (p. 652, 669).

### VI. Thermodynamics & Entropy Production

*(No explicit rules provided in the source material for this category.)*

### VII. Scaling, Dimensional Analysis & RG

1. **Scaling Laws:**
    * `Ro(x,z)` scales as `x^-1/2`.
    * `Ro(x,y)` scales as `λ^-1` for `λ^2` scaling of arguments.
    * When `y = 1`, the multiplier of `Re` determines the asymptotic behavior of the LHS as LHS tends to 0.
    * Scaling laws must be confirmed for diffraction catastrophes (p. 785).
2. **Asymptotic Expansions:**
    * Asymptotic approximations must be utilized for the Re-function (p. 496) and Stieltjes-Wigert polynomials (p. 474).
    * Watson's lemma must be applied for asymptotic expansions of integrals (p. 44, 46).
    * Stirling’s formula and Stirling’s series must be defined (p. 141).

### VIII. Boundary & Initial Conditions

1. **Elliptic Integral Specific Values:**
    * `K(0) = π/2`, `E(0) = π/2`, `K'(1) = π/2`, `E'(1) = π/2`.
    * `K(1) = ∞`, `K'(0) = ∞`, `E(1) = 1`, `E'(0) = 1`.
    * `D(0) = π/4`, `D(1) = ∞`.
    * `Π(α²,0) = π/(2√(1-α²))` if `0 < α² < 1`; `Π(α²,0) = ∞` if `α² < 0` or `α² > 1`.
    * `F(0,k) = 0`, `F(φ,0) = φ`, `F(π/2,1) = ∞`.
    * `E(0,k) = 0`, `E(φ,0) = φ`, `E(π/2,1) = 1`.
2. **`Ro(x,y)` Limits:**
    * `Ro(x,y)` tends to `+∞` if `y → 0±` and `x > 0`.
    * `Ro(0,y) = ∞` if `|ph y|<π`.
    * `Ro(0,y) = 0` if `y < 0`.
3. **Mathieu Function Initial and Boundary Conditions:**
    * Define basic solutions `w1(z;a,q)` and `w2(z;a,q)` such that `w1(0;a,q) = 1`, `w1'(0;a,q) = 0`, `w2(0;a,q) = 0`, `w2'(0;a,q) = 1`.
    * `w1(pi/2;a,q)` must equal `w1'(pi/2;a,q)`.
    * `w2(pi/2;a,q)` must equal `w2'(pi/2;a,q)`.
    * The eigenvalues `a` of Mathieu's equation are determined by `cos(pi*v) = w1(pi;a,q)`.
    * `a_2n(q)` is the eigenvalue with boundary condition `w'(0)=w(pi)=0`.
    * `a_(2n+1)(q)` is the eigenvalue with boundary condition `w(0)=w'(pi)=0`.
    * `b_(2n+1)(q)` is the eigenvalue with boundary condition `w(0)=w'(pi)=0`.
    * `b_(2n+2)(q)` is the eigenvalue with boundary condition `w'(0)=w(pi)=0`.
    * Normalize eigenfunctions such that `Integral[0 to pi] ce_n(z,q)^2 dz = pi` and `Integral[0 to pi] se_n(z,q)^2 dz = pi`.
    * Normalize `C_n(q)` and `S_n(q)` such that `Integral[0 to pi] (fe_n(z,q)/C_n(q))^2 dz = pi` and `Integral[0 to pi] (ge_n(z,q)/S_n(q))^2 dz = pi`.
4. **Parabolic Cylinder Functions:** Parabolic cylinder functions must satisfy initial values (p. 204) and specified values at `z=0` (p. 304, 314).

### IX. Constitutive Relations & Material Laws

1. **Special Function Definitions and Relations:**
    * For `n = 0,1,2,..., Hn+1/2(z)` is defined by (11.4.1) and `Kn+1/2(z)` by (11.4.2).
    * `Jν(z)` is expressed by (11.10.8) using `S1(ν,z)` and `S2(ν,z)`. `Eν(z)` is expressed by (11.10.9) using `S1(ν,z)` and `S2(ν,z)`. `S1(ν,z)` and `S2(ν,z)` are defined by (11.10.10) and (11.10.11).
    * `sin(πν)Jν(z) = cos(πν)Eν(z) − E−ν(z)`. (11.10.13)
    * `sin(πν)Eν(z) = J−ν(z) − cos(πν)Jν(z)`. (11.10.14)
    * `Jν(z) = Jν(z) + sin(πν)Aν(z)`. (11.10.15)
    * `Eν(z) = −Yν(z) − cos(πν)Aν(z) − A−ν(z)`. (11.10.16)
    * `Jν(z) = −Hν(z) + Jν(z)`. (11.10.17)
2. **Mathieu Function Relations:**
    * `w1(z + pi;a,q)` must be expressed as `w1(pi;a,q)w1(z;a,q) + w1'(pi;a,q)w2(z;a,q)`.
    * `w2(z + pi;a,q)` must be expressed as `w2(pi;a,q)w1(z;a,q) + w2'(pi;a,q)w2(z,q)`.
    * `ce_2n(z,q)` must be expressed as `w1(z;a_2n(q),q) / ce_2n(0,q)`.
    * `ce_(2n+1)(z,q)` must be expressed as `w1(z;a_(2n+1)(q),q) / ce_(2n+1)(0,q)`.
    * `se_(2n+1)(z,q)` must be expressed as `w2(z;b_(2n+1)(q),q) / se_(2n+1)'(0,q)`.
    * `se_(2n+2)(z,q)` must be expressed as `w2(z;b_(2n+2)(q),q) / se_(2n+2)'(0,q)`.
    * `fe_n(z,q)` must be expressed as `C_n(q) * (z * ce_n(z,q) + f_n(z,q))` when `a = a_n(q)`.
    * `ge_n(z,q)` must be expressed as `S_n(q) * (z * se_n(z,q) + g_n(z,q))` when `a = b_n(q)`.

### X. Stochastic Processes & Noise Models

*(No explicit rules provided in the source material for this category.)*

### XI. Numerical Methods & Discretization Assumptions

1. **IEEE Standard Adherence:** All numerical computations must adhere to the IEEE Standard for Binary Floating-Point Arithmetic (ANSI/IEEE Std 754-1985).
2. **Asymptotic Approximations for Computation:**
    * For computation, avoid using power series (11.2.1), (11.2.2), and Bessel function expansions of §11.4(iv) when `|z|` is large, due to slow convergence and cancellation.
    * For large `|z|` and/or `|ν|`, asymptotic expansions of §11.6 should be used for computation.
    * For large positive real `ν`, uniform asymptotic expansions of §§10.20(i) and 10.20(ii) can be used for computation. These expansions can also be used for large `|z|` (whether or not `ν` is large).
    * For large `h = sqrt(q)` and `s = 2m+1`, `a_s(h)` must be approximated by `2h^2 - (s^2+1)/2 - (s^2+3s)/(8h) - ...`.
    * For large `h`, `ce_n(z,h^2)` must be approximated by `(pi*h)^(1/2) * e^(h*cos(z)) * Dn(sqrt(2h)*cos(z)) * ...`.
    * Use Barrett's expansions to obtain asymptotic approximations for solutions of Mathieu's equation when `a` and `q` are real and large. The approximants can be elementary functions, Airy functions, Bessel functions, or parabolic cylinder functions.
    * Use Dunster's approximations to obtain uniform asymptotic approximations for solutions of Mathieu's equation when `q` and `a` are real and `q -> infinity`, with `(-2q < a < (2-delta)q)`. The approximations are expressed in terms of Whittaker functions.
3. **Stable Computation Techniques:**
    * For stable computation of `Hν(z)` and `Lν(z)` sequences, forward recurrence, backward recurrence, or boundary-value methods may be necessary.
    * `Hν(z)` and `Lν(z)` can be computed stably by integrating forwards (from the origin toward infinity).
    * `Kν(z)` must be integrated backwards for small `z`. `Kν(z)` can be integrated either forwards or backwards for large `z`, depending on whether `Rν` exceeds 1/2.
    * For `Mν(z)`, both forward and backward integration are unstable, requiring boundary-value methods.
4. **Approximations for Elliptic Integrals:**
    * The lower bound in (19.9.4) is sharper than `π/2` when `0 < k² < 0.9960`.
    * Prefer (19.9.15) when `k²` and `sin²φ` are close to 1 for `F(φ,k)` approximation.
    * Prefer (19.9.14) when `k²` and `sin²φ` are not both close to 1 for `F(φ,k)` approximation.
5. **Mathieu Eigenvalue and Function Approximations (Small `q`):**
    * For small `q`, Mathieu eigenvalues `a_m(q)` and `b_m(q)` must be approximated by power series (e.g., `a_0(q) ≈ -q^2/2 - 7q^4/128 + ...`, `a_1(q) ≈ 1 + q - q^2/8 - q^3/64 - q^4/3072 + ...`, etc.).
    * For `m >= 7`, `a_m(q)` and `b_m(q)` must be approximated using `m^2 + q^2/(2(m^2-1)) + ...` for small `q`.
    * `a_m(q) - b_m(q)` can be approximated by `2q^m / ((m-1)!)`.
    * Use continued-fraction equations (28.6.16-28.6.19) to find higher coefficients of `a_n(q)` and `b_n(q)`.
    * For small `q`, Mathieu functions `ce_m(z,q)` and `se_m(z,q)` must be approximated by their respective Fourier series expansions (e.g., `ce_0(z,q) ≈ 1 - qcos(2z) + (q^2/8)(cos(4z) - 2) + ...`, `ce_1(z,q) ≈ cos(z) - (q/4)cos(3z) + ...`, etc.).
    * For `m >= 3`, `se_m(z,q)` must be approximated by changing `cos` to `sin` in the `ce_m` expansion.
6. **Integral Representations for Mathieu Functions:**
    * `ce_n(z,q)` can be expressed by `Integral[0 to pi/2] cos(2h cos(z)cos(t)) ce_n(t,h^2) dt`.
    * `ce_n(z,q)` can be expressed by `Integral[0 to pi/2] cosh(2h sin(z)sin(t)) ce_n(t,h^2) dt`.
    * `se_n(z,q)` can be expressed by `Integral[0 to pi/2] sin(2h cos(z)cos(t)) se_n(t,h^2) dt`.
    * `se_n(z,q)` can be expressed by `Integral[0 to pi/2] sinh(2h sin(z)sin(t)) se_n(t,h^2) dt`.
    * `ce_n(z,q)` can be expressed by `Integral[0 to pi] J_0(2*sqrt(q)*(cos(z)+cos(t))) ce_n(t,q) dt`.
    * `se_n(z,q)` can be expressed similarly with `J_1` Bessel function and `se_n` function.
7. **Numerical Integration and Root Finding:**
    * Gauss quadrature must be utilized (p. 80-83) with Christoffel coefficients, nodes, and weight functions, and remainder terms must be accounted for (p. 80).
    * Gaussian elimination must be applied (p. 73-74) using back substitution, forward elimination, and a pivot element.
    * Lagrange interpolation remainder terms must be accounted for (p. 75-76).
    * Filon’s rule must be applied for oscillatory integrals (p. 82).
    * Simpson’s rule (composite, elementary) must be applied for quadrature (p. 78, 79).
    * The trapezoidal rule (composite, elementary, improved) must be applied for quadrature (p. 78, 79, 84).
    * Runge-Kutta methods must be used for ordinary differential equations (p. 89-90).
    * The secant method (p. 91) and Steffensen’s method (p. 91) must be applied.
    * Newton's rule (or method) must exhibit convergence (p. 90).
8. **Sequence and Series Acceleration/Stability:**
    * The quotient-difference algorithm stability must be ensured (p. 95) using the rhombus rule (p. 95).
    * Shanks’ transformation must be applied for sequences (p. 93).
    * The Stokes phenomenon must be smoothed (p. 67).
    * Abel, Borel, Cesaro, and general summability methods must be applied for series (p. 33). Abel and Cesaro summability methods must be applied for integrals (p. 34).
    * Wynn's cross rule must be applied for Padé approximations (p. 98).
    * Wynn's epsilon algorithm must be applied for sequences (p. 93).
9. **Approximation and Regularization:**
    * Minimax rational approximations must be defined by their weight function (p. 97).
    * Regularization must be defined using distributional methods (p. 55).
    * The partition function must be computed (p. 646).
10. **Validation:** Computations must be validated (p. 72).

### XII. Measurement, Operational Definitions & Protocols

1. **Elliptic Integral Classifications:**
    * Define an elliptic integral as an integral of `r(s,t)/s(t) dt` where `s(t)` is a cubic or quartic polynomial with simple zeros, and `r(s,t)` is a rational function containing at least one odd power of `s`.
    * Classify `Π(φ, α², k)` as a circular case if `α²(α² - k²)(α² - 1)` is negative (for real `k², α²`).
    * Classify `Π(φ, α², k)` as a hyperbolic case if `α²(α² - k²)(α² - 1)` is positive (for real `k², α²`).
    * Define Bulirsch's integrals as complete if `x = ∞`.
    * If `z, y > 0`, classify `Ro(z,y)` as an inverse circular function if `z < y`.
    * If `z, y > 0`, classify `Ro(z,y)` as an inverse hyperbolic function (or logarithm) if `z > y`.
2. **Specific Elliptic Integral Definitions:**
    * Define `D(k) = (K(k) - E(k))/k²`.
    * Define `Π(φ,1,k) = k² D(φ,k) + F(φ,k)`.
    * Define the perimeter of an ellipse `L(a,b)` as `4a E(k)` where `k²=1- (b²/a²)` and `a>b`.
3. **Asymptotic Behavior Determination:** Use specified convergent series to determine asymptotic behavior of `K(k)` and `E(k)` near `k = 1`.
4. **Integral Representation Protocols:**
    * For functions in the orthogonality integral, the branches of the many-valued functions must be continuous on the path and assume their principal values at the beginning of the path.
    * To obtain integral equations satisfied by Heun functions or integral representations of distinct solutions, suitable choices must be made for the branches of the Riemann P-symbols in (31.10.9) and the contour `C`.
    * For Example 1, the integral equation (31.10.1) is satisfied by `w(z) = w_p,m(z)` and `W(z) = lambda_p,m w(z)`, where `w_p,m(z)` is a Heun function and `lambda_p,m` is the corresponding eigenvalue.
    * For Example 1, the contour `C` must be the Pochhammer double-loop contour about 0 and 1, as defined in §31.9(i).
    * Fuchs-Frobenius solutions are represented in terms of Heun functions using (31.10.1) with `W(z)` being the Fuchs-Frobenius solution, `w(z)` being the Heun function, and `K(z,t)` chosen from (31.10.11).
    * For the representation of Fuchs-Frobenius solutions, `nu_p,m` (in 31.10.11) is a normalization constant, and the contour `C` must be the contour of Example 1.

### XIII. Assumptions, Domains of Validity & Prohibitions

1. **Fundamental Mathematical Definitions:**
    * Strictly decreasing and strictly increasing functions must be defined (p. 4).
    * Strictly monotonic integrals must be defined (p. 4).
    * Functions of matrix argument must be defined (p. 768).
    * The fundamental theorem of arithmetic (p. 638) and calculus (p. 6) must be defined.
    * The gamma function must be defined (p. 136).
    * Gauss’s theorem must be defined for vector-valued functions (p. 12).
    * The generalized exponential integral must be defined (p. 185).
    * The generalized hypergeometric function must be defined (p. 404, 408).
    * Generalized sine and cosine integrals (general values) must be defined (p. 188).
    * Green’s theorem must be defined for vector-valued functions (three dimensions, two dimensions) (p. 12, 11).
    * Hadamard’s inequality must be defined for determinants (p. 3).
    * Hankel functions must be defined (p. 217).
    * Heaviside function must be defined (p. 36, 54).
    * Heun functions, Heun polynomials, and Heun’s equation must be defined (p. 710, 712).
    * The Hilbert transform must be defined (p. 29).
    * Hill’s equation must be defined (p. 674) and can have antiperiodic, periodic, and pseudoperiodic solutions (p. 675, 674), applying Floquet’s theorem (p. 674).
    * Hölder’s inequalities must be defined for sums and integrals (p. 12, 13).
    * A holomorphic function must be defined (p. 19).
    * The Hurwitz zeta function must be defined (p. 607).
    * Hyperbolic functions must be defined (p. 123).
    * The hypergeometric function and hypergeometric R-function must be defined (p. 384, 498).
    * The implicit function theorem must be defined (p. 7).
    * Incomplete Airy functions, beta functions, and gamma functions must be defined (p. 208, 183, 174).
    * Functions must be square-integrable (p. 6).
    * Inverse hyperbolic functions (p. 127, general values) and inverse trigonometric functions (p. 118, general values) must be defined.
    * The Jacobi function, Jacobi polynomials, Jacobi’s epsilon function, and Jacobi’s zeta function must be defined (p. 304, 439, 562).
    * Jacobian elliptic functions must be defined (p. 550).
    * Jensen's inequality must be defined for integrals (p. 13).
    * The Jordan curve theorem must be defined (p. 16). Jordan's inequality must be defined for the sine function (p. 116).
    * Kelvin functions must be defined (p. 267).
    * Kummer functions must be defined (p. 322).
    * L'Hôpital’s rule must be defined for derivatives (p. 5).
    * The Lagrange inversion theorem must be defined (p. 21).
    * Laguerre polynomials must be defined (p. 439).
    * Lamé functions and Lamé polynomials must be defined (p. 685, 690).
    * The Lambert W-function must be defined (p. 111).
    * The Laplace transform must be defined (p. 28) and for functions of matrix argument (p. 768).
    * A Laurent series must be defined (p. 19).
    * Legendre polynomials and Legendre’s elliptic integrals must be defined (p. 439, 486).
    * Leibniz’s formula must be defined for derivatives (p. 5).
    * Lerch’s transcendent must be defined (p. 612).
    * Limit points (or limiting points) must be defined (p. 15). Limits of functions (of one variable, two variables, complex variable, two complex variables) must be defined (p. 4, 7, 15).
    * A linear functional must be defined (p. 35).
    * Liouville’s theorem must be defined for entire functions (p. 16).
    * Locally analytic (p. 24) and locally integrable (p. 48) must be defined.
    * The logarithm function (p. 104, general base, general value) and the logarithmic integral must be defined (p. 150).
    * Lommel functions must be defined (p. 294-295).
    * Mathieu functions must be defined (p. 664), applying Floquet’s theorem to Mathieu’s equation (p. 653).
    * Matrix concepts (characteristic polynomial, eigenvalues, eigenvectors, Jacobian, monic, nonsingular, orthogonal, symplectic, tridiagonal, Hermitian) must be defined (p. 74).
    * The maximum modulus principle (analytic functions, harmonic functions) must be defined (p. 20). The mean value property must be defined for harmonic functions (p. 16). Mean value theorems must be defined for integrals (p. 6).
    * The Mellin transform must be defined (p. 29, 48).
    * A meromorphic function must be defined (p. 19).
    * Minkowski’s inequalities must be defined for sums and series (p. 12, 13).
    * Modified Bessel functions and Modified Mathieu functions must be defined (p. 248, 667).
    * Modular functions (p. 579) and modular forms (p. 579) must be defined.
    * Monotonic functions must be defined (p. 4).
    * A multivalued function (p. 20, 104) and its branch (p. 20, 104), and branch cut (p. 104) must be defined.
    * The multivariate gamma function (p. 769) and its properties (p. 769) must be defined. The multivariate hypergeometric function (p. 769) and its properties (p. 769) must be defined.
    * A neighborhood (p. 11, 15), of infinity (p. 16), and punctured (p. 19) must be defined.
    * Normal probability functions must be defined (p. 160).
    * Number theory functions: completely multiplicative functions (p. 640), Dirichlet series (p. 640), Euler product (p. 640), multiplicative functions (p. 640), primitive Dirichlet characters (p. 642), induced modulus (p. 642), and principal (p. 642) must be defined.
    * Open disks around infinity (p. 16) and an open point set (p. 11, 15) must be defined.
    * Orthogonal matrix polynomials and orthogonal polynomials on the unit circle must be defined (p. 477, 475).
    * The Painlevé Property must be defined (p. 724).
    * Parabolic cylinder functions must be defined (p. 304, 305, 314).
    * The partition function (p. 645) and its generating function (p. 646) must be defined. Partitions (p. 618, of a set, of integers) and conjugate partitions (p. 626) must be defined.
    * Permutations (p. 618), generating function (p. 632), inversion numbers (p. 631-634), transposition (p. 631), and twelvefold way (p. 634) must be defined.
    * The phase principle must be defined (p. 20, 92).
    * Picard’s theorem must be defined (p. 19).
    * A piecewise continuous (p. 4) and piecewise differentiable curve (p. 11) must be defined.
    * Plane partitions (p. 629) and their generating functions (p. 630) must be defined.
    * Polygamma functions (p. 144) and their properties (p. 144) must be defined.
    * Polylogarithms must be defined (p. 611).
    * The power function (p. 105, general base, general value) must be defined. A power series must be defined (p. 18).
    * Pringsheim’s theorem must be defined for continued fractions (p. 25).
    * Probability functions (Gaussian, normal) must be defined (p. 160).
    * The psi function (p. 136) and its properties (p. 144) must be defined.
    * q-functions: q-beta function (p. 145), q-factorials (p. 145), q-gamma function (p. 145), q-binomial coefficient (p. 421, 627), q-calculus (p. 420-422), q-derivatives (p. 421), q-exponential function (p. 422), q-hypergeometric function (p. 423), q-Leibniz rule (p. 421), q-Racah polynomials (relation to q-hypergeometric function) (p. 474), q-series (classification) (p. 423), and q-Stirling numbers (p. 422) must be defined. The q-binomial theorem must be defined (p. 421, 424).
    * Raabe’s theorem must be defined for Bernoulli polynomials (p. 590).
    * Radial Mathieu functions and radial spheroidal wave functions must be defined (p. 668, 699, 700).
    * A scaled gamma function must be defined (p. 185).
    * Schrödinger numbers must be defined (p. 622).
    * The Schwarz reflection principle and Schwarz’s lemma must be defined (p. 19, 20).
    * The Schwarzian derivative must be defined (p. 27).
    * A separable Gauss sum must be defined (p. 643).
    * A simple closed contour (p. 16) and simple closed curve (p. 11) must be defined. A simple discontinuity (p. 4) and simple zero (p. 19) must be defined.
    * A simply-connected domain must be defined (p. 25).
    * The sinc function must be defined (p. 77).
    * Sine integrals must be defined (p. 150).
    * 3j symbols (p. 758), 6j symbols (p. 761), and 3nj symbols (p. 763) must be defined.
    * Sobolev polynomials must be defined (p. 477).
    * Spherical Bessel functions must be defined (p. 262).
    * Spherical harmonics must be defined (p. 378), represented using the Dirac delta (p. 379), and exhibit distributional completeness (p. 379).
    * The spheroidal differential equation (eigenvalues) must be defined (p. 698-699). Spheroidal wave functions must be defined (p. 699, 700) and can be of Coulomb type (p. 704).
    * Spline functions (Bernoulli monosplines, cardinal monosplines, cardinal splines, Euler splines) must be defined (p. 597).
    * A square-integrable function must be defined (p. 6).
    * The Stieltjes fraction (S-fraction) must be defined (p. 95). Stieltjes polynomials must be defined (p. 718). The Stieltjes transform must be defined (p. 30, 52).
    * Stirling numbers (first and second kinds) (p. 624) and their generating functions (p. 624) must be defined.
    * The Stokes phenomenon (p. 67) and Stokes numbers (p. 68) must be defined. Stokes sets must be defined (p. 782). Stokes’ theorem must be defined for vector-valued functions (p. 12).
    * Struve functions and modified Struve functions must be defined (p. 288) and have numerically satisfactory solutions (p. 288).
    * Summability methods (general) must be defined for series (p. 33). The support of a function must be defined (p. 35).
    * Symmetric elliptic integrals must be defined (p. 497).
    * A Taylor series must be defined (p. 18). Taylor’s theorem (one variable, two variables) must be defined (p. 6, 8, 18).
    * Tempered distributions must be defined (p. 36, 52). Test functions (space) must be defined (p. 35).
    * The Theorem of Ince must be defined for Mathieu’s equation (p. 653, 657).
    * Theta functions must be defined (p. 524). Theta functions with characteristics must be defined (p. 539).
    * Toroidal functions (p. 371) and Whipple's formula (p. 372) must be defined.
    * Transcendental functions must be defined (p. 724).
    * The triangle inequality must be defined (p. 15).
    * Trigonometric functions must be defined (p. 112). Triple integrals must be defined (p. 8).
    * Ultraspherical polynomials must be defined (p. 439). Roots of unity must be defined (p. 23).
    * Van Vleck polynomials must be defined (p. 718). Van Vleck's theorem must be defined for continued fractions (p. 25).
    * A Vandermondian must be defined (p. 3).
    * Variation of real or complex functions (bounded, total) must be defined (p. 6). A variational operator must be defined (p. 44).
    * Vector-valued functions (curl, del operator, divergence, gradient, line integral, path integral) must be defined (p. 10, 11). Vectors (angle, cross product, dot product, magnitude) must be defined (p. 9).
    * Voigt functions (p. 167) and their properties (p. 168) must be defined.
    * The von Staudt-Clausen theorem and Voronoi’s congruence must be defined for Bernoulli numbers (p. 593).
    * Waring’s problem must be defined (p. 645). Watson's 3F2 sum (Gasper-Rahman q-analog) must be defined (p. 426).
    * Weierstrass elliptic functions must be defined (p. 570). The Weierstrass product must be defined (p. 22).
    * Whittaker functions must be defined (p. 334). The Whittaker-Hill equation must be defined (p. 676). Wigner 3j, 6j, 9j symbols must be defined (p. 765).
    * Wilkinson's polynomial must be defined (p. 92). Wilson class orthogonal polynomials must be defined (p. 467-468).
    * The winding number of a closed contour must be defined (p. 16). The WKB or WKBJ approximation must be defined (p. 57).
    * Zeros of analytic functions (multiplicity, simple) must be defined (p. 19, 90). Zeros of Bessel functions (analytic properties, interlacing, monotonicity, purely imaginary) must be defined (p. 235, 236). Zeros of cylinder functions (analytic properties, interlacing, monotonicity) must be defined (p. 235, 285, 236). Descartes’ rule of signs must be applied for zeros of polynomials (p. 22). The discriminant must be defined for zeros of polynomials (p. 22) and elementary symmetric functions (p. 22).
    * Zonal polynomials (p. 769) and their properties (p. 769) must be defined.
2. **Domains of Validity and Prohibitions for Specific Functions/Operations:**
    * Mathieu's equation has no finite singularities.
    * For a given value of `v` and `q`, the values of `a` are discrete.
    * For the Lommel inhomogeneous Bessel differential equation (11.9.1) to have the general solution (11.9.2), `ρ+ν ≠ −1, −3, −5, ...`.
    * The condition `|g| < ...` in (11.4.14) applies when `ν ≠ −3/2, −5/2, −7/2, ....`
    * In (11.4.15), `|ν+3/2|` must be the smallest of `|ν+3/2|, |ν+5/2|, ...`.
    * `Hν(z)` is expressed by (11.4.18) when `ν ≠ −1, −2, −3, ....`.
    * For `d/dz(zνHν(z))` in (11.4.27), `Rν > 1/2` is required.
    * `Hν(z)` is defined by (11.5.1) and (11.5.2) when `Rν > −1/2`.
    * `Kν(z)` is defined by (11.5.3) when `Rz > 0`.
    * `Lν(z)` is defined by (11.5.4) and (11.5.6) when `Rν > −1/2`.
    * `Mν(z)` is defined by (11.5.5) when `Rz > 0`.
    * `I−ν(z) − Lν(z)` is defined by (11.5.7) when `Rz > 0` and `Rν < 1/2`.
    * `Hν(z)` is defined by (11.5.8) when `Rν > −1/2` and `|ph z| < 3π/4`. The contour for (11.5.8) must separate poles at `s = 0,1,2,...` from poles at `s = −1/2−ν−k`.
    * `Lν(z)` is defined by (11.5.9) when `Rν > −1/2` and `|ph z| < 3π/4`. The contour for (11.5.9) must separate poles at `s = 0,1,2,...` from poles at `s = −1/2−ν−k`.
    * When `Aν(z)` is defined by (11.10.4), `Rz > 0` is required. It also applies when `Rz = 0` and `Rν > 0`.
    * Laplace transforms of `Hν(t)` require `Rα > 0` for convergence. Laplace transforms of `Lν(t)` require `Rα > 1` for convergence.
    * `Sμ,ν(z)` is expressed by (11.9.7) when `ρ+ν ≠ −1, −2, −3, ....`.
    * Asymptotic approximations for `Kν(z)` (11.6.1), `Mν(z)` (11.6.2), `Kν(νλ)` (11.6.6), `Lν(νλ)` (11.6.7), `Jν(z)` (11.11.2), `Eν(z)` (11.11.3), `Aν(z)` (11.11.4), `Jν(z)` (11.11.5), `Eν(z)` (11.11.6), `Aν(λν)` (11.11.8, 11.11.10, 11.11.11), `A−ν(ν)` (11.11.14), `Aν(ν)` (11.11.16), `Aν(ν+a)` (11.11.17), `Jν(λν)` (11.11.18), `Eν(λν)` (11.11.19) are subject to specific `ph z`, `ph ν`, `z` or `ν` tending to infinity conditions as detailed in the source.
    * Integrals `∫0π/2 Hν(z sin θ)(sin θ)νdθ` (11.7.7) applies when `−1/2 < Rν < 1/2`.
    * `∫0∞ Hν(t)dt = cot(½πν)` applies when `−2 < Rν < 0`.
    * `∫0∞ tHν(t)dt` (11.7.10) applies when `Rν > −3/2`.
    * `∫0∞ t−νHν(t)dt` (11.7.11) applies when `Rν > −1/2`.
    * For Struve's and modified Struve's equations (11.2.7), (11.2.9), applications of (11.2.11)-(11.2.17) require specific conditions on `z` (real/complex), `Rν`, `ph z`, and `|z|` (bounded or bounded away from origin).
    * For Legendre's integrals: ensure `1 - sin²φ ∈ C\(-∞,0]` and `1 - k²sin²φ ∈ C\(-∞,0]`. Allow `1 - sin²φ` or `1 - k²sin²φ` to be zero. Ensure `1 - α²sin²φ ∈ C\{0}`.
    * For `Ro(z,y)`: ensure `z ∈ C\(-∞,0)` and `y ∈ C\{0}`. Ensure the line segment with endpoints `z` and `y` lies in `C\(-∞,0]` for its integral representation. Assume `y > 0` to express it in terms of elementary functions. Apply asymptotic approximation only if `z > 0` and `y > 0`.
    * Apply Maclaurin expansion for `K(k)`, `E(k)`, and `D(k)` only if `|k| < 1` and `|φ| < 1`.
    * If `φ` is small: `lim F(φ,1)/φ = 1`, `lim E(φ,1)/φ = 1`, and if `α² ≠ 0,k²`, then `lim φ→0 Π(φ,α²,k)/φ = 1`.
    * Apply inequalities for complete integrals only if `0 < k < 1`, unless for (19.9.4). Apply inequalities for incomplete integrals only if `0 < k < 1`, `0 < φ < π/2`, `α² ≠ 0, k², sin²φ`, and `A = √(1-k²sin²φ) > 0`.
    * Apply duplication formulas only if `φ_1 = φ_2`. Apply (19.12.1) for `K(k)` and (19.12.2) for `E(k)` if `0 < k'² < 1`.
    * Use asymptotic approximations for `Π(φ,α²,k)` primarily when `(1-k)/(1-sin²φ)` is small or large compared with 1.
    * Assume both the integrand and `cos φ` are nonnegative for reduction formulas (19.14.1)-(19.14.3).
    * For (19.14.4): ensure `0 < y < z`, ensure each quadratic polynomial is positive on the interval `(y, z)`, and ensure `α, β, γ` is a permutation of `α_0, α_1, α_2, α_3` (not all 0 by assumption) such that `α < β < γ`.
    * Apply AGM definition only when `a_0` and `g_0` are positive numbers.
    * Ensure `0 < k < 1` and `0 < φ < π/2` for ascending Landen transformation to imply given bounds on `k_s` and `φ_1`. Ensure `0 < k < 1` and `0 < φ < π/2` for descending Gauss transformation to imply given bounds on `k_s` and `φ_1`.
    * `e^(i*v)` must be an eigenvalue of the matrix `[[w1(pi;a,q), w2(pi;a,q)], [w1'(pi;a,q), w2'(pi;a,q)]]`.
    * `cos(pi*v)` must be an entire function of `a`, `q^2`.
    * `v` must be a characteristic exponent of Mathieu's equation. If `v = n` (integer), then `v` is a double root of the characteristic equation; otherwise it is a simple root.
    * `w1(pi;a,q) - 1 = 2w1(pi/2;a,q)w2(pi/2;a,q)`.
    * `w1(pi;a,q) + 1 = 2w1(pi/2;a,q)w1'(pi/2;a,q)`.
    * `w2(pi;a,q) = 2w1(pi/2;a,q)w1'(pi/2;a,q)`.
    * `n` must be `0,1,2,...` for various definitions and expansions.
    * `C` must be an arbitrary point in the interval `(0,1)` for the orthogonality integral (31.9). The right-hand side of Equation (31.9.3) must be independent of `C` for its evaluation.
    * For Heun polynomials, the separation constant `sigma` in (31.10.9) must be `(1-gamma_t-alpha_t), i=0,1,...,n`.
    * Eigenvalues `a_n(q)` and `b_n(q)` are determined by analytic continuation. Near `q=0`, `a_n(q)` and `b_n(q)` must be expanded in power series in `q`.
    * Resolve ambiguities in sign for eigenfunctions using `ce_n(0,q) > 0` and `ce_n'(0,q) > 0` when `q=0`, and by continuity for other `q`. Resolve ambiguities in sign for Fourier coefficients (e.g., `A_m^(2n)(q)`) using their known values at `q=0` (e.g., `A_0^(2n)(0) = 1/sqrt(2)`) and by continuity for other `q`.
    * If `q != 0`, a nontrivial solution of Mathieu's equation with period `pi` or `2pi` cannot have either period (Theorem of Ince).
    * `fe_n(z,q)` and `ge_n(z,q)` must be unique.
    * There are no zeros within the strip `|Rz| < pi/2` other than those on the real and imaginary axes.
    * `w1(pi;a,q) = 1` for `a=a_2n(q)`, `w1'(pi;a,q) = 0` for `a=a_2n(q)`.
    * `w1(pi;a,q) = -1` for `a=a_(2n+1)(q)`, `w1'(pi;a,q) = 0` for `a=a_(2n+1)(q)`.
    * `w2(pi;a,q) = 0` for `a=b_n(q)`, `w2'(pi;a,q) = 1` for `a=b_n(q)`.
    * `w2(pi;a,q) = 0` for `a=b_(2n+1)(q)`, `w2'(pi;a,q) = -1` for `a=b_(2n+1)(q)`.
    * `w2(pi;a,q) = 0` for `a=b_(2n+2)(q)`, `w2'(pi;a,q) = 1` for `a=b_(2n+2)(q)`.
    * `fe_n(z,q)` and `ge_n(z,q)` must not be bounded as `z -> infinity` on `R`.
    * Radii of convergence `rho^2` for power series of `a_n(q)` and `b_n(q)` are given in Table 28.6.1. For large `n`, `lim inf rho_n^2 / n^2` equals `2.041834...`.
    * Singularities of `a_n(q)` and `b_n(q)` must be algebraic branch points and must not have finite limit points.
    * Define `a_n(q)` and `b_n(q)` uniquely by introducing suitable cuts in the `q`-plane. All real values of `q` are normal values.
    * Zeros of `ce_n(z,q)` and `se_(n+1)(z,q)` approach asymptotically the zeros of `He_n(sqrt(2q)cos(z))` and `He_(n+1)(sqrt(2q)cos(z))` respectively as `q -> infinity`.
    * For `q > 0`, `ce_n(z,q)` and `se_n(z,q)` also have purely imaginary zeros.
3. **Integral Representations and Existence:** Integral representations must exist for the gamma function, generalized exponential integral, generalized hypergeometric function, generalized sine and cosine integrals, Hankel functions, hyperbolic functions, hypergeometric function, incomplete gamma functions, Kelvin functions, Kummer functions, Legendre’s elliptic integrals, logarithm function, Lommel functions, modified Bessel functions, modified Mathieu functions, parabolic cylinder functions, polylogarithms, radial Mathieu functions, repeated integrals of the complementary error function, Riemann zeta function, Scorer functions, spherical Bessel functions, Struve functions, symmetric elliptic integrals, theta functions, toroidal functions, Weierstrass elliptic functions, and Whittaker functions.
4. **Behavioral Properties and Requirements:**
    * Lamé functions must exhibit interlacing eigenvalues, parity, order, and portions (p. 685). Lamé polynomials must exhibit periodicity (p. 690).
    * Lebesgue constants must exhibit asymptotic behavior (p. 13).
    * Local maxima and minima must be identified for functions (p. 450).
    * Modified Bessel functions must exhibit monotonicity (p. 254).
    * Hill’s equation must have characteristic exponents (p. 675). Heun’s equation must have characteristic exponents (p. 710) and a singularity parameter (p. 710).
    * Jacobi’s epsilon function must have quasi-periodicity (p. 562). Jacobi’s zeta function must have a quasi-addition formula (p. 562).
    * Jacobian elliptic functions must have a modulus (p. 550), periodicity (p. 553), and poles (p. 553-554).
    * Kelvin functions must respect orders ±5 (p. 268). Kummer functions must have zeros (p. 331).
    * Lamé functions must have zeros (p. 685) and parity (p. 686). Lamé polynomials must have zeros (p. 690).
    * Legendre’s elliptic integrals must have a modulus (p. 486). The logarithm function must have zeros (p. 104). Mathieu functions must have zeros (p. 663). Mathieu’s equation must have eigenvalues (analytic continuation, branch points) (p. 661).
    * A matrix must be Hermitian (p. 74), invertible (p. 74), nonsingular (p. 74), orthogonal (p. 74), symplectic (p. 74), or tridiagonal (p. 74).
    * Modified Bessel functions must have zeros (p. 258). Modified Mathieu functions must have zeros (p. 680).
    * Nonlinear equations must have fixed points (p. 90). Paraboloidal wave functions must have orthogonality properties (p. 677).
    * Radial spheroidal wave functions must have zeros (p. 699). The Rayleigh function must have applications (p. 276).
    * The Re-function must have limiting values (p. 491) and special values (p. 491). Repeated integrals of the complementary error function must have applications (p. 169). Riccati-Bessel functions must have zeros (p. 240).
    * The Riemann zeta function must have a critical line (p. 606), critical strip (p. 606), and trivial zeros (p. 606).
    * Scorer functions must have analytic properties (p. 204), connection formulas (p. 205), numerically satisfactory solutions (p. 204), standard solutions (p. 204), and zeros (p. 206).
    * Sine integrals must have zeros (p. 154). Spherical Bessel functions must have zeros (p. 266). Spherical harmonics must have zeros (p. 379).
    * The spheroidal differential equation must have eigenvalues (p. 698-699). Spheroidal wave functions must have eigenvalues (p. 698).
    * Stieltjes polynomials must have zeros (p. 718). Struve functions must have zeros (p. 292). 3j symbols must have zeros (p. 760).
    * Theta functions must have zeros (p. 525). Toroidal functions must have applications (p. 379) and hypergeometric representations (p. 371). A torus must be complex (p. 533).
    * Transcendental functions (p. 724) must have transition points (p. 58, 63) and turning points (p. 58, 63).
    * Trigonometric functions must have special values (p. 116) and zeros (p. 112). Unity must have roots (p. 23).
    * Voigt functions must have properties (p. 168). Weierstrass elliptic functions must have a discriminant (p. 571), invariants (p. 570), poles (p. 570), and zeros (p. 570, 579). Whittaker functions must have zeros (p. 342). Zonal polynomial properties (p. 769).

### XIV. Verification & Content Standards

1. **Proof and Referencing:** Provide references to literature for proof or describe steps to construct a proof for all equations and technical information.
2. **Organization of Verification Information:** Group verification information at the section level under the "Sources" heading in the "References" section of the Handbook.
3. **Digital Library of Mathematical Functions (DLMF) Specifics:** Provide verification information in pop-up windows at the subsection level in the DLMF.
4. **Prohibited Proof Sources:** Do not regard citations to AMS 55 (Abramowitz and Stegun) as supplying proofs.

### XV. Usage & Publication Policies

1. **Commercial Use Restrictions:** Prohibit reproduction, copying, or distribution for any commercial purpose.
2. **Bulk Reproduction Prohibition:** Prohibit bulk copying, reproduction, or redistribution in any form.
3. **Permission Requirement:** Prohibit reproduction of any part without the written permission of Cambridge University Press, subject to statutory exception and collective licensing agreements.
4. **Liability Release:** Require users to explicitly release NIST and Cambridge University Press from any and all liability for damage resulting from errors or omissions.
5. **Permitted Uses:** Permit limited copying and internal distribution of content for research and teaching.
6. **User Responsibility:** Require users to be aware that neither individuals nor NIST assume responsibility for consequences of errors in the publication.

## Key Highlights

* All numerical computations must strictly adhere to the IEEE Standard for Binary Floating-Point Arithmetic (ANSI/IEEE Std 754-1985), and principal values should be assumed for mathematical functions unless otherwise specified.
* Precise definitions of standard mathematical notation, symbols, operators, and conventions, including vector calculus (Einstein summation, right-hand rule) and matrix operations, are mandatory throughout the text.
* Special functions, such as Struve, Bessel, Lommel, Heun, and Mathieu functions, must satisfy their specified differential equations, recurrence relations, symmetry properties, and orthogonality conditions.
* For stable and accurate computation, specific techniques like asymptotic expansions, uniform asymptotic expansions, and careful integration strategies (forward/backward recurrence) are required, especially for functions with large arguments or orders.
* The document mandates identifying and adhering to domains of validity, branch cuts, poles, and singularity conditions for all functions, alongside the explicit classification of elliptic integrals and Mathieu function properties.
* All technical information and equations require references to literature for proof or detailed steps to construct a proof, and citations to AMS 55 are explicitly not considered sufficient proof.
* Commercial reproduction, bulk copying, or redistribution of any part of this document is strictly prohibited without explicit written permission, though limited internal use for research and teaching is permitted.

## Example ideas

* Develop a reference implementation library that rigorously adheres to all specified mathematical conventions, principal values, branch cuts, and IEEE 754 floating-point standards, as detailed in the summary.
* Design and implement a comprehensive validation and testing framework to verify all defined function properties, convergence criteria, Wronskians, recurrence relations, and domain restrictions, with a focus on boundary conditions and asymptotic behaviors.
* Prioritize and implement performance optimization strategies for computationally intensive special functions, leveraging specified asymptotic expansions and stable numerical methods (e.g., forward/backward recurrence) to handle large arguments and avoid cancellation.
* Conduct a feasibility study to investigate how the existing foundational mathematical framework could be extended to develop explicit rules for Thermodynamics & Entropy Production and Stochastic Processes & Noise Models, addressing the current gaps in the summary.
* Create standardized internal documentation and training modules to ensure consistent understanding and application of the precise conventions, definitions, and computational guidelines across all relevant development and research teams.
