# Rules for Solid State Physics

BOOK: Kittel's Introduction to Solid State Physics
COVERAGE: Chapters on Electrons in Periodic Potentials, Superconductivity, and Dielectric Properties (Inferred)
NOTES: Rules are presented with CGS units unless otherwise specified, with SI unit equivalents provided where available. Parenthetical notes refer to original equation numbers or context from source text segments.

**Generated on:** September 30, 2025 at 8:24 PM CDT

---

## Variational Principles & Equations of Motion

* **Solve Wave Equation for Electrons in Crystals:**
  * The wave equation for an electron in a crystal is `(-ħ^2/2m d^2/dx^2 + U(x)) ψ(x) = ε ψ(x)` (Eq. 24, 1D) or `(ℏ²/2m p² + U(r)) Ψ_k(r) = ε_k Ψ_k(r)` (Eq. 16, 3D).
  * Solutions `Ψ_k(r)` must satisfy the Bloch condition `Ψ_k(r + T) = exp(ik · T) Ψ_k(r)`.
  * Express `ψ(x)` as a Fourier series `ψ = Σ_k C(k) e^(ikx)` (Eq. 25).
  * The resulting central equation for Fourier coefficients `C(k)` is `(A_k - ε)C(k) + Σ_G U_G C(k-G) = 0` (Eq. 27), where `A_k = ħ^2 k^2 / (2m)` (Eq. 28).
  * These equations are consistent only if the determinant of the coefficients `C(k-G)` vanishes.
  * The Bloch wave equation for `u_k(r)` is `(ℏ²/2m (p + ℏk)² + U(r)) u_k(r) = ε_k u_k(r)` (Eq. 17).
  * `u_0` must be a solution of `(ℏ²/2m p² + U(r)) u_0(r) = ε_0 u_0(r)` (Eq. 19).
* **Determine Energy Bands:** At a given `k`, each root `ε` (or `ε_n` or `ε_k,n`) of the central equation defines a different energy band, unless there is a coincidence (degeneracy).
* **Derive Kronig-Penney Dispersion Relation (Reciprocal Space):** For a periodic delta-function potential (Eq. 33), the dispersion relation is `(m A a^2 / (2ħ^2 Ka)) sin(Ka) + cos(Ka) = cos(ka)` (Eq. 43), where `K^2 = 2mε/ħ^2`.
* **Determine Energy Roots Near Zone Boundary (Weak Potential):** Near the zone boundary at `1/2 G`, the energy has two roots given by `ε = 1/2(A_k + A_k-G) ± 1/2 sqrt((A_k - A_k-G)^2 + 4U^2)` (Eq. 50), where `A_k = ħ^2 k^2 / (2m)`. The first-order energy gap is `E_g = U` (Eq. 6).
* **Electron Motion in Magnetic Field:**
  * Electrons in a static magnetic field must move on a curve of constant energy, and this curve must lie on a plane normal to the magnetic field `B`.
  * An electron on the Fermi surface must move in a curve on the Fermi surface.
* **Quantum Binding Energy Behavior:**
  * An electron in the state `(ψ_1 + ψ_2)` must have a lower energy than in the state `(ψ_1 - ψ_2)`.
  * For the state `(ψ_1 - ψ_2)`, the probability density must vanish midway between nuclei.
  * If an electron spends time midway between two protons (as in `ψ_1 + ψ_2`), its binding energy must increase due to the attractive potential of both protons.
* **Crystal Formation Energy Levels:** The Coulomb interaction between atom cores and electrons must split energy levels into bands when free atoms form a crystal.
* **Kinetic Energy and Modulation:**
  * Any spatial variation in the state of an electronic system must require extra kinetic energy.
  * Eigenfunction modulation must increase kinetic energy due to an increase in the integral of `d²Ψ/dx²`.
  * The increase of energy required to modulate is `ℏ²kq/2m`.
* **Tight-Binding First-Order Energy Calculation:**
  * Calculate the first-order energy by evaluating the diagonal matrix elements of the crystal Hamiltonian using `(k|H|k) = N^(−1) Σ_j Σ_m exp[ik · (r_j − r_m)] (φ_m|H|φ_j)` (Eq. 7).
  * If `(k|k) = 1`, the first-order energy `ε_k` must be given by `ε_k = −α − γ Σ_ρ exp(−ik · ρ)` (Eq. 10).
  * For a simple cubic structure, `ε_k = −α − 2γ(cos k_x a + cos k_y a + cos k_z a)` (Eq. 13).
  * For fcc structure with 8 nearest neighbors, `ε_k = −α − 8γ cos k_x a cos k_y a cos k_z a` (Eq. 14).
  * For fcc structure with 12 nearest neighbors, `ε_k = −α − 4γ(cos k_x a cos k_y a + cos k_y a cos k_z a + cos k_z a cos k_x a)` (Eq. 15).
* **Electron Flux Quantization:**
  * The momentum path integral must equate to the Bohr-Sommerfeld relation `∫ p · dr = (q/c)Φ = (n + γ)2πℏ` (Eq. 26).
  * Electron orbit flux `Φ` must be quantized according to `Φ = (n + γ)(2πℏc/q)` (Eq. 27).
  * The area `S_k` of an orbit in k-space must satisfy `S_k = (n + γ)(2πq/ℏc)B` (Eq. 30).
  * The area `ΔS` between successive orbits must be given by `ΔS = S_{n+1} − S_n = 2πmeB/ℏc` (Eq. 32).
  * Oscillations of magnetic moment must occur at equal intervals of `1/B` such that `Δ(1/B) = (2πe/ℏc)/S` (Eq. 37).
* **Total Electron Energy in Landau Levels:**
  * Calculate total energy of fully occupied Landau levels using `U_0 = Σ_{n=1}^s D(n − 1/2)ℏω_c = Dℏω_c s(s + 1)/2` (Eq. 35).
  * Calculate total energy of electrons in partly occupied level `s + 1` using `U_s+1 = ℏω_c (s + 1/2)(N − sD)` (Eq. 36).
* **Landau Level Hamiltonian and Wave Equation:**
  * The Hamiltonian for a free electron without spin in a magnetic field is `H = −(ℏ²/2m)(∂²/∂y² + ∂²/∂z²) + (1/2m)[−iℏ∂/∂x − eB_y/c]²`.
  * The corresponding wave equation `χ(y)` must satisfy is `(ℏ²/2m)d²χ/dy² + [ε − (ℏ²k_z²/2m) − (1/2)mω_c²(y − y_0)²]χ = 0`.
  * This equation is analogous to the wave equation of a harmonic oscillator with frequency `ω_c`.
  * The energy eigenvalues are `ε_n = (n + 1/2)ℏω_c + ℏ²k_z²/2m`.
* **Josephson Equations of Motion:**
  * The time-dependent Schrödinger equation for a Josephson junction is given by `iℏ∂Ψ_1/∂t = TΨ_2 ; iℏ∂Ψ_2/∂t = TΨ_1` (Eq. 38).
  * With a dc voltage `V` applied, the equations become `iℏ∂Ψ_1/∂t = TΨ_2 − qVΨ_1 ; iℏ∂Ψ_2/∂t = TΨ_1 + qVΨ_2` (Eq. 48).
  * Population changes are given by `∂n_1/∂t = (2T/ℏ)(n_1n_2)^(1/2) sin δ ; ∂n_2/∂t = −(2T/ℏ)(n_1n_2)^(1/2) sin δ` (Eq. 43).
  * Phase changes are given by `∂θ_1/∂t = (T/ℏ)(n_2/n_1)^(1/2) cos δ ; ∂θ_2/∂t = −(T/ℏ)(n_1/n_2)^(1/2) cos δ` (Eq. 44).
  * If `n_1 = n_2`, the phase difference rate is `∂δ/∂t = −2qV/ℏ` (Eq. 55).
  * Integration yields the relative phase variation `δ(t) = δ(0) − (2qVt/ℏ)` (Eq. 56).
* **Harmonically Bound Electron Equation of Motion:** For an electron of mass `m` bound harmonically with force constant `β` (resonance frequency `ω₀ = (β/m)^(1/2)`) in a local electric field `E_local sin(ωt)`, its equation of motion is `m ẍ + βx = -eE_local sin(ωt)`.
* **Crystal Instability Condition:** If the transverse optical phonon frequency `ω_T` vanishes (`ω_T = 0`), the crystal is unstable.
* **Ferroelectric State Condition (Landau Theory):** To obtain a ferroelectric state, the coefficient `g₂` in the Landau free energy expansion must pass through zero at some temperature `T₀`, such that `g₂ = γ(T - T₀)` where `γ` is a positive constant.
  * A small positive `g₂` indicates a "soft" lattice, close to instability.
  * A negative `g₂` indicates an unstable unpolarized lattice.
* **Spontaneous Polarization (Second-Order Transition, E=0):** For a second-order transition where `g₄ > 0` and `g₂ = γ(T - T₀)`, the spontaneous polarization `P_s` for `T < T₀` is given by `P_s² = (γ/g₄)(T₀ - T)`. For `T ≥ T₀`, `P_s = 0`. `T₀` is the Curie temperature.
* **Equilibrium Polarization (First-Order Transition, E=0):** For a first-order transition where `g₄ < 0`, the coefficient `g₆` must be positive. The equilibrium polarization `P_s` for `E=0` is found from `γ(T - T₀)P_s - |g₄|P_s³ + g₆P_s⁵ = 0`.
* **Transverse Optical Phonon Condensation:** This occurs when the corresponding TO phonon frequency vanishes at some point in the Brillouin zone, representing a time-independent displacement of finite amplitude.

## Symmetry & Conservation Laws

* **Adhere to Bloch Theorem:**
  * Solutions of the Schrödinger equation for a periodic potential `U(r)` must be of the form `ψ_k(r) = e^(ik⋅r) u_k(r)` (Eq. 7).
  * The function `u_k(r)` must have the period of the crystal lattice, i.e., `u_k(r) = u_k(r + T)`, where `T` is a lattice translation vector.
  * This implies `ψ_k(r + T) = e^(ik⋅T) ψ_k(r)` (Eq. 30), meaning `e^(ik⋅T)` is the phase factor by which a Bloch function is multiplied under a lattice translation.
* **Ensure Potential Energy is Real:** The Fourier series expansion for the potential energy `U(x)` must ensure `U(x)` is a real function: `U(x) = Σ_G U_G e^(iGx) = 2 Σ_G>0 U_G cos(Gx)` (Eq. 23).
* **Conserve Crystal Momentum:** The quantity `ħk` is called the crystal momentum of an electron and must be used in collision processes. For an electron `k` absorbing a phonon `q` and scattering to `k'`, the selection rule is `k + q = k' + G`, where `G` is a reciprocal lattice vector.
* **Brillouin Zone Construction:** Construct all lines equivalent by symmetry to the perpendicular bisectors of `G_1`, `G_2`, `G_3` to define the regions in k-space forming the first three Brillouin zones.
* **Fermi Surface Enclosed Volume Invariance:** The total volume in k-space enclosed by the Fermi surface depends only on the electron concentration and is independent of the details of the lattice interaction.
* **Gauge Invariance:** The k-space orbit area `S_k` must be gauge invariant.
* **Electron-Hole Circulation Sense:** Particles of opposite charge must circulate in a magnetic field in opposite senses.
* **Lattice Symmetry of k=0 Wavefunction:** In a crystal, the k=0 wavefunction `u_0(r)` must have lattice symmetry and be symmetric about `r = 0`.
* **Number of Orbitals in a Band:** For `N` atoms, the number of orbitals in a band (nondegenerate atomic level) must be `2N`.
* **Total Orbitals per k-space Volume:** The number of orbitals (counting both spin orientations) per unit volume of k-space must be `V/(4π³)`.
* **Dipole Moment Origin Independence:** The total dipole moment `p = Σ q_i r_i` for a system of charges `q_i` is independent of the origin chosen for the position vectors `r_i` **provided that** the system is neutral (`Σ q_i = 0`).
* **Landau Free Energy Odd Powers:** The Landau free energy expansion `F(P)` does not contain terms in odd powers of `P` **if** the unpolarized crystal has a center of inversion symmetry.

## Locality, Causality & Constraints

* **Define Insulator Behavior:** A crystal behaves as an insulator if its allowed energy bands are entirely filled or entirely empty, preventing electron movement in an electric field (unless the field is strong enough to disrupt electronic structure).
* **Define Metal Behavior:** A crystal behaves as a metal if one or more energy bands are partly filled (e.g., between 10% and 90% filled).
* **Define Semiconductor/Semimetal Behavior:** A crystal is a semiconductor or semimetal if one or two bands are slightly filled or slightly empty.
* **Identify Energy Gap Origin:** Bragg reflection of electron waves in crystals is the cause of energy gaps.
* **Characterize Standing Waves at Zone Boundary:** At `k = ±π/a`, wavefunctions are standing waves (e.g., `ψ(+) = 2 cos(πx/a)` and `ψ(-) = 2 sin(πx/a)`) composed of equal parts of right- and left-directed traveling waves.
* **Associate Wavefunctions with Gap Edges:** Just below an energy gap, the wavefunction is `ψ(+)`; just above it, the wavefunction is `ψ(-)`.
* **Restrict k for Fourier Expansion:** If a particular wavevector `k` is part of a Bloch function `ψ`, then all other wavevectors in its Fourier expansion must be of the form `k + G`, where `G` is any reciprocal lattice vector.
* **Fermi Surface Properties:**
  * The Fermi surface will almost always intersect zone boundaries perpendicularly.
  * The crystal potential will round out sharp corners in Fermi surfaces.
* **Macroscopic Field Adequacy:** The macroscopic electric field `E` is adequate for electrodynamics of crystals **provided that**:
    1. The connection between `E`, `P`, and `j` is known.
    2. The wavelengths of interest are long in comparison with the lattice spacing.
* **Constant Polarization Condition:** If the polarization `P` is constant, then `div P = 0`.
* **First-Order Transition Properties:** For a first-order ferroelectric transition, the transverse optical phonon frequency `ω_T ≠ 0` and the static dielectric constant `ε(0) ≠ ∞` at the transition temperature `T_c`.
* **Maxwell-Wagner Mechanism Constraint:** High values of effective dielectric constant `ε_eff` caused by the Maxwell-Wagner mechanism (interfacial polarization) are **always** accompanied by large AC losses.
* **TO/LO Phonon Frequencies Relation:** LO phonons always have higher frequencies than TO phonons of the same wavevector.

## Thermodynamics & Entropy Production

* **Equilibrium Structure at Absolute Zero:** The stable crystal structure `A` at absolute zero generally has the lowest accessible internal energy.
* **Pressure Effect on Structure:** Low atomic volume favors closest-packed or metallic structures under extreme pressure.
* **Stable Structure at Temperature T:** The stable structure at a temperature `T` is determined by the minimum of the free energy `F = U - TS`.
* **Phase Transition Condition (Free Energy):** A transition from structure `A` to structure `B` occurs if a temperature `T_c` exists (below the melting point) such that `F_A(T_c) = F_B(T_c)`.
* **Equilibrium Polarization (Landau Theory):** The value of polarization `P` in thermal equilibrium is given by the minimum of the free energy `F` as a function of `P`, which implies `∂F/∂P = 0`.
  * In an applied electric field `E`, this condition is `-E + g₂P + g₄P³ + g₆P⁵ + ... = 0`.

## Constitutive Relations & Material Laws

* **Maxwell's Equations:**
  * **CGS Units:**
    * `∇ ⋅ D = 4πρ`
    * `∇ × H = (4π/c)j + (1/c)∂D/∂t`
    * `∇ × E = -(1/c)∂B/∂t`
    * `∇ ⋅ B = 0`
  * **SI Units:**
    * `∇ ⋅ D = ρ`
    * `∇ × H = j + ∂D/∂t`
    * `∇ × E = -∂B/∂t`
    * `∇ ⋅ B = 0`
* **London Equation and its Time Derivative:**
  * Combining Maxwell and London equations yields `∇²B = B/λ_L²` (Eq. 14) for a superconductor.
  * The time derivative of the London equation yields `∂j/∂t = (c²/4πλ_L²)E`.
* **Electric Field from Dipole:** The electric field `E(r)` at a point `r` from a dipole moment `p` is `E(r) = (1/r³) [3(p ⋅ r̂)r̂ - p]` (CGS) or `E(r) = (1/(4πε₀r³)) [3(p ⋅ r̂)r̂ - p]` (SI).
* **Macroscopic Field from Uniform Polarization:**
  * The macroscopic electric field `E` caused by a uniform polarization `P` is equal to the electric field in vacuum of a fictitious surface charge density `σ = n̂ ⋅ P` on the body's surface.
  * The electric field `E_p` between parallel plates with uniform polarization `P` is `E_p = -4πP` (CGS) or `E_p = -P/ε₀` (SI).
  * The total macroscopic electric field `E` inside a uniformly polarized slab is `E = E₀ + E_p`, specifically `E = E₀ - 4πP` (CGS) or `E = E₀ - P/ε₀` (SI).
  * If polarization `P` is uniform within the body, the macroscopic field `E` is composed of the applied field `E₀` and the depolarization field `E_d`.
* **Depolarization Field in an Ellipsoid:** For an ellipsoid with uniform polarization `P` (components `P_x, P_y, P_z` along principal axes), the components of the depolarization field `E_d` are `E_dx = -N_x P_x`, `E_dy = -N_y P_y`, `E_dz = -N_z P_z` (CGS) or `E_dx = -N_x P_x / ε₀`, etc. (SI). Depolarization factors `N_x, N_y, N_z` must be positive.
* **Uniform Polarization in Ellipsoid:** A uniform applied field `E₀` induces uniform polarization `P` in an ellipsoid.
* **Macroscopic Field in Ellipsoid:** For `E₀` uniform and parallel to a principal axis of an ellipsoid, the macroscopic field `E` is `E = E₀ - NP` (CGS) or `E = E₀ - NP/ε₀` (SI).
* **Polarization in Ellipsoid:** Polarization `P` is calculated as `P = χ(E₀ - NP)` (CGS) or `P = ε₀χ(E₀ - NP/ε₀)` (SI). The value of `P` depends on the depolarization factor `N`.
* **Lorentz Cavity Field:** The Lorentz cavity field `E_L` at the center of a spherical cavity in a uniformly polarized medium is `E_L = 4πP/3` (CGS) or `E_L = P/(3ε₀)` (SI). For a sphere, `E_L = -E_d`, so `E_L + E_d = 0`.
* **Crystal Structure Dependence of Local Field:** The field `E_i` (from atoms inside cavity) is the only term in the local field `E_local` that depends on the crystal structure.
* **Local Field at Cubic Site (Lorentz Relation):** For an atom at a site with cubic symmetry, the local field `E_local = E + (4π/3)P` (CGS) or `E_local = E + P/(3ε₀)` (SI).
* **Dielectric Constant Definition:** The dielectric constant `ε` of an isotropic or cubic medium is defined in terms of the macroscopic `E` and `P` as `D = E + 4πP = εE` (CGS) or `D = ε₀E + P = ε₀εE` (SI).
  * This implies `ε = 1 + 4πP/E` (CGS) and `ε = 1 + P/(ε₀E)` (SI).
* **Dielectric Susceptibility Relation:** Dielectric susceptibility `χ` is related to dielectric constant `ε` by `χ = (ε-1)/(4π)` (CGS) or `χ = ε-1` (SI).
* **Polarization (Noncubic Crystal):** For noncubic crystals, dielectric response is described by components of susceptibility tensor `χ_jk` or dielectric constant tensor `ε_jk`, such that `P_j = χ_jk E_k` (CGS) or `P_j = ε₀χ_jk E_k` (SI).
* **Crystal Polarization (Approximate):** The polarization `P` of a crystal may be expressed approximately as `P = Σ N_j p_j = Σ N_j α_j E_local(j)`.
* **Susceptibility (Lorentz Local Field):** If the local field follows the Lorentz relation, `χ = P/E = (Σ N_j α_j) / (1 - (4π/3)Σ N_j α_j)`.
* **Clausius-Mossotti Relation:** If the local field follows the Lorentz relation, `(ε-1)/(ε+2) = (4π/3)Σ N_j α_j` (CGS) or `(ε-1)/(ε+2) = (1/3ε₀)Σ N_j α_j` (SI).
* **Optical Frequency Dielectric Constant:** At optical frequencies, the dielectric constant arises almost entirely from electronic polarizability.
* **Refractive Index and Dielectric Constant (Optical Range):** In the optical range, `n² = ε`, where `n` is the refractive index.
* **Ionic Polarizability Property:** The electronic polarizability of an ion depends somewhat on the environment in which it is placed. Negative ions are highly polarizable due to their larger size.
* **Classical Polarizability:**
  * Classical Resonance Frequency: For an electron bound harmonically with force constant `β` to an atom, resonance absorption occurs at `ω₀ = (β/m)^(1/2)`.
  * Classical Static Electronic Polarizability: `α_electronic = e²/mω₀²`.
  * Classical Frequency-Dependent Electronic Polarizability: `α_electronic(ω) = e²/(m(ω₀² - ω²))` (CGS).
* **Quantum Electronic Polarizability:** `α_electronic = (e²/m) Σ_j (f_j / (ω_j₀² - ω²))` (CGS), where `f_j` is the oscillator strength.
* **Perovskite Deformation below T_c:** Below the Curie temperature, the perovskite structure of BaTiO₃ is slightly deformed, with specific ion displacements (e.g., Ba²⁺ and Ti⁴⁺ relative to O²⁻) developing a dipole moment.
* **Dielectric Constant (Paraelectric State, T > T_c):** For `T > T_c`, `ε(T) = 1 + 4π/(γ(T - T₀))` (CGS), assuming `P³` and `P⁵` terms in `∂F/∂P` are negligible. `T₀ = T_c` for second-order, `T₀ < T_c` for first-order.
* **Lyddane-Sachs-Teller (LST) Relation:** `ω_L² / ω_T² = ε(ω)/ε(0)`.
* **LST Consequence for Temperature Dependence:** If `1/ε(0) ∝ (T - T₀)`, then `ω_T² ∝ (T - T₀)`, assuming `ω_L` is temperature independent.
* **Dielectric Constant (Second-Order Transition, T < T_c):** For a second-order phase transition, `ε(T) = 1 + 4π/(2γ(T_c - T))` (CGS) for `T < T_c`.
* **Capacitor with Two Layers (Maxwell-Wagner):** A parallel-plate capacitor made of two parallel layers (one dielectric with `ε`, `σ=0`, `d₁`; the other with `ε=0`, `σ₀`, `d₂`) behaves as if filled with a homogeneous dielectric with complex dielectric constant `ε_eff = (ε₁d₁ + ε₂d₂) / (d₁ + d₂) * (1 - (iε₂ω)/(4πσ₀(d₁ + d₂)))^(-1)` (simplified form from source needs care for precise application).
* **Polarizability of Conducting Sphere:** The polarizability of a conducting metallic sphere of radius `a` is `α = a³` (CGS). `E=0` inside a conducting sphere.
* **Piezoelectric Effect Relations:** An applied stress `Z` changes electric polarization `P`. An applied electric field `E` causes crystal strain `ε`.
* **Piezoelectric Equations (1D, CGS):** `P = Zd + χE` and `ε = Zs + dE`.
* **Spontaneous Polarization Condition (Linear Array):** For a linear array of atoms of polarizability `α` and separation `a`, spontaneous polarization occurs if `α = e² / (4Z_n^α)`, where `Z_n^α = Σ (1/n³) ≈ 1.202`.

## Boundary & Initial Conditions

* **Periodic Boundary Conditions (1D):** For a free electron gas confined to a length `L` with periodic boundary conditions, the allowed wavevectors `k` are `0, ±2π/L, ±4π/L, ...`.
* **Periodic Boundary Conditions (3D):** For electrons confined to a cube of side `L` with periodic boundary conditions, the components of the wavevector `k` must satisfy `k_x = 0, ±2π/L, ±4π/L, ...` and similarly for `k_y` and `k_z`.
* **Fixed External Field (Problem 5):** For a sphere in a uniform external field `E₀` created by distant charges, `E₀` must remain unchanged when the sphere is inserted.

## Units, Conventions & Signatures

* **Bloch Function Labeling:** Usually, label Bloch functions with the wavevector `k` that lies within the first Brillouin zone.
* **Band Structure Exhibition:** Actual band structures are usually plotted as energy versus wavevector in the first Brillouin zone (reduced zone scheme).
* **Wavefunction Normalization at Zone Boundary:** The wavefunctions at the Brillouin zone boundary `k = π/a` are `sqrt(2) cos(πx/a)` and `sqrt(2) sin(πx/a)`, normalized over unit length.
* **Reduced Zone Scheme:** Any energy `ε` for `k'` outside the first zone is equivalent to an `ε` in the first zone, where `k = k' + G`. All bands are mapped into the first Brillouin zone.
* **Periodic Zone Scheme:** Energy `ε` as a function of wavevector `k` must be a periodic function in the reciprocal lattice: `ε_n(k) = ε_n(k + G)` (Eq. 2).
* **Counting Independent k Values:** In a linear crystal of `N` primitive cells of lattice constant `a`, the allowed `k` values in the first Brillouin zone are `0, ±2π/L, ..., ±(N-1)π/L, Nπ/L (=π/a)`, where `L = Na`. The point `-Nπ/L` is not counted as independent.
* **Total Orbitals in a Band:** Each primitive cell contributes exactly one independent value of `k` to each energy band (in 1D and 3D). Accounting for spin, there are `2N` independent orbitals in each energy band, where `N` is the number of primitive cells.
* **Depolarization Factor Sum Rule:** Depolarization factors `N_x, N_y, N_z` satisfy the sum rule `N_x + N_y + N_z = 4π` (CGS) or `N_x + N_y + N_z = 1` (SI).
* **Depolarization Factor Values (Limiting Cases):**
  * Sphere (any axis): `N = 4π/3` (CGS), `N = 1/3` (SI).
  * Thin slab (normal to P): `N = 4π` (CGS), `N = 1` (SI).
  * Thin slab (in plane of P): `N = 0` (CGS), `N = 0` (SI).
  * Long circular cylinder (longitudinal to P): `N = 0` (CGS), `N = 0` (SI).
  * Long circular cylinder (transverse to P): `N = 2π` (CGS), `N = 1/2` (SI).
* **Unit Conversions (CGS to SI):**
  * Electric Field (dipole moment `p`): Replace `p` with `p/(4πε₀)`.
  * Dielectric Susceptibility: `χ_SI = 4πχ_CGS`.
  * Dielectric Constant: `ε_CGS = ε_SI`.
  * Atomic Polarizability: `α_SI = 4πε₀α_CGS`. For Table 1 values (CGS), multiply by `9 × 10⁻³¹`.
  * Spontaneous Polarization (µC/cm² to esu cm⁻²): Multiply by `3 × 10⁻⁷`.
  * Piezoelectric Strain Constant (m/V to cm/stat-V): Multiply by `3 × 10⁴`.
  * Piezoelectric Equations (1D): Replace `χ` by `ε₀χ`.

## Numerical Methods & Discretization Assumptions

* **Cell Dipole Moment Calculation:** The dipole moment of a cell `p` can be calculated as the saturation polarization `P_s` multiplied by the cell volume `V_cell`: `p = P_s * V_cell`.
* **Local Field from Dipoles (Problem 18):** For a specific configuration, `E_dipole_x = E_dipole_y = E_dipole_z = 0`.

## Measurement, Operational Definitions & Protocols

* **Polarization Definition (`P`):** The polarization `P` is defined as the dipole moment per unit volume, averaged over the volume of a cell. (Macroscopic field `E` and `P` are averaged fields over the specimen volume).
* **Total Dipole Moment Definition (`p`):** The total dipole moment `p` for a system of charges `q_i` at positions `r_i` is `p = Σ q_i r_i`.
* **Applied Electric Field Definition (`E₀`):** `E₀` is defined as the field produced by fixed charges external to the body.
* **Average Electric Field Definition (`E(r₀)`):** The average electric field `E(r₀)` over the volume `V` of a crystal cell containing lattice point `r₀` is `E(r₀) = (1/V) ∫_V e(r) dV`, where `e(r)` is the microscopic electric field.
* **Depolarization Field Definition (`E_d`):** The depolarization field `E_d` is the field arising from a fictitious surface charge density `n̂ ⋅ P` on the outer surface of the specimen. It opposes the applied field `E₀` within the body.
* **Reducing Depolarization Field:** To reduce the depolarization field to zero, either:
    1. Work parallel to the axis of a long fine specimen.
    2. Make an electrical connection between electrodes deposited on the opposite surfaces of a thin slab.
* **Local Electric Field (Decomposition):** The local electric field `E_local` at a general lattice site is expressed as `E_local = E₀ + E_d + E_L + E_i`.
  * `E₀`: Field produced by fixed charges external to the body.
  * `E_d`: Depolarization field, from a surface charge density `n̂ ⋅ P` on the outer surface.
  * `E_L`: Lorentz cavity field, from polarization charges on the inside of a fictitious spherical cavity.
  * `E_i`: Field of atoms inside the cavity. `E_i(r_j)` varies rapidly within a cell.
* **Atomic Polarizability Definition (`α`):** The polarizability `α` of an atom is defined in terms of the local electric field `E_local` at the atom as `p = αE_local`, where `p` is the dipole moment.
  * For a nonspherical atom, `α` will be a tensor.
* **Polarizability Decomposition:** Total polarizability may usually be separated into electronic, ionic, and dipolar parts.
  * Electronic: displacement of electron shell relative to nucleus.
  * Ionic: displacement of charged ion relative to other ions.
  * Dipolar: orientation change of molecules with a permanent electric dipole moment.
* **Magnetic Moment Definition:** The magnetic moment `μ` of a system at absolute zero is given by `μ = −dU/dB`.
* **Ferroelectric Transition Definition:** Ferroelectric transitions are structural phase transitions marked by the appearance of a spontaneous dielectric polarization in the crystal.
* **Ferroelectric Crystal Properties:**
  * Exhibits an electric dipole moment even without an external electric field.
  * In the ferroelectric state, the center of positive charge does not coincide with the center of negative charge.
  * Polarization versus electric field shows a hysteresis loop.
* **Curie Point (`T_c`):** The transition temperature (`T_c`) (Curie point) above which ferroelectricity disappears and the crystal enters a paraelectric state.
* **Pyroelectric Crystal Definition:** Crystals whose spontaneous dipole moment changes with temperature and is not altered by an electric field of maximum intensity before electrical breakdown.
* **Ferroelectric Crystal Classification:** Ferroelectric crystals may be classified into order-disorder or displacive types.
* **Displacive Transition Definition:** A transition is displacive if a soft optical phonon mode can propagate in the crystal at the transition.
* **Order-Disorder Transition (Soft Mode):** If the soft mode is only diffusive (non-propagating), it's not a phonon, indicating an order-disorder system.
* **First-Order Transition Definition:** A transition with latent heat, where the order parameter (polarization) changes discontinuously at the transition temperature.
* **Second-Order Transition Definition:** A transition with no latent heat, where the order parameter (polarization) is continuous at the transition temperature.
* **Antiferroelectric Definition:** A deformation with neighboring lines of ions displaced in opposite senses, which does not produce a net spontaneous polarization.
* **Ferroelectric Domains Definition:** Regions within a ferroelectric crystal where polarization is in the same direction, but differs in adjacent domains.
* **Piezoelectric Effect Definition:** A stress `Z` applied to a crystal changes its electric polarization `P`. An electric field `E` applied to a crystal causes it to become strained `ε`. A crystal may be piezoelectric without being ferroelectric.
* **Piezoelectric Strain Constant Definition (`d_ik`):** `d_ik = (∂ε_i / ∂E_k)_Z`.

## Assumptions, Domains of Validity & Prohibitions

* **Assume One-Electron Approximation:** The orbital `ψ(x)` must describe the motion of one electron in the potential of ion cores and the average potential of other conduction electrons when using the wave equation (Eq. 24).
* **Assume Weak Perturbation:** For the nearly free electron model, assume band electrons are perturbed only weakly by the periodic potential of ion cores.
* **Assume Small Fourier Components:** When solving for orbitals near a zone boundary, assume the Fourier components `U_G` of the potential energy are small compared to the kinetic energy of a free electron at the zone boundary.
* **Assume Non-Degenerate Case (for restricted Bloch theorem proof):** The proof of the Bloch theorem for `ψ(x + a) = Cψ(x)` (Eq. 8) is valid only when `ψ` is non-degenerate (no other wavefunction has the same energy and wavevector).
* **Assume Periodic Delta-Function Potential (Kronig-Penney Simplification):** To simplify the Kronig-Penney model, assume the potential is a periodic delta function where `b = 0` and `U_0 = ∞` such that `Q^2ħ^2a / (2m) = P` is a finite quantity. In this limit, `Q >> K` and `Qb << 1`.
* **Insulator Condition (Valence Electrons):** A crystal can only be an insulator if the number of valence electrons in a primitive cell is an even integer. If bands overlap in energy, a crystal with an even number of valence electrons can be a metal.
* **Metal Condition (Valence Electrons):** Alkali and noble metals, having one valence electron per primitive cell (an odd number), must be metals.
* **Insulators at Absolute Zero:** Pure diamond, silicon, and germanium crystals are insulators at absolute zero, as their bands do not overlap and they have eight valence electrons per primitive cell.
* **Average Field Calculation for Neutral Body:** If the body is neutral, express the contribution to the average field in terms of the sum of the fields of atomic dipoles.
* **Smooth Contribution from Distant Dipoles:** Dipoles at distances greater than perhaps ten lattice constants from the reference site make a smoothly varying contribution and may be replaced by two surface integrals.
* **Fictitious Spherical Cavity:** The spherical cavity used in decomposing the local field is a mathematical fiction.
* **Smoothness of `E_p`:** The depolarization field `E_p` is smoothly varying in space (on an atomic scale) because discrete dipoles are replaced with smoothed polarization `P`.
* **Clausius-Mossotti Relation Applicability:** The Clausius-Mossotti relation applies only for crystal structures where the Lorentz local field obtains (e.g., cubic sites).
* **Optical Range Dispersion:** In the visible region, frequency dependence (dispersion) is not usually very important in most transparent materials.
* **Total Crystal Polarization Approximation:** The polarization `P` of a crystal may be expressed *approximately* as `P = Σ N_j p_j = Σ N_j α_j E_local(j)`.
* **Optical Frequency Contribution:** At optical frequencies, the dielectric constant arises *almost entirely* from electronic polarizability; dipolar and ionic contributions are small due to inertia.
* **Non-zero Curie Point:** Some ferroelectric crystals have no Curie point because they melt before leaving the ferroelectric phase.
* **Simplified Catastrophe Theory (Local Field):** For the simple form of catastrophe theory, assume the local field at all atoms is `E + 4πP/3` (CGS) or `E + P/(3ε₀)` (SI).
* **Landau Theory Power Series Validity:** Power series expansions of the free energy do not always exist, especially when very near a transition where nonanalytic terms are known to occur.
* **Long Rod Specimen (Landau Theory):** In the section on Landau theory, assume the specimen is a long rod with the external applied field `E` parallel to the long axis.
* **Linear Variation of `s` (Paraelectric State):** Near the critical temperature, assume `s` varies linearly with temperature, `s = (T - T₀)ξ`.
* **Negligible `P³` and `P⁵` Terms (Dielectric Constant above T_c):** When calculating the dielectric constant `ε(T)` for `T > T_c` from Landau theory, assume `P³` and `P⁵` terms can be neglected.
* **Semiclassical H Atom Polarizability (Problem 1):** For this model, assume `x << a₀` (electron displacement much smaller than Bohr radius).

## Key Highlights

* The solutions for an electron in a periodic crystal potential are Bloch functions, `ψ_k(r) = e^(ik⋅r) u_k(r)`, where `u_k(r)` has the crystal lattice period and satisfies the Bloch condition `Ψ_k(r + T) = exp(ik · T) Ψ_k(r)`.
* The Coulomb interaction between atom cores and electrons splits energy levels into bands when free atoms form a crystal, with Bragg reflection of electron waves being the fundamental cause of energy gaps.
* A crystal is classified as an insulator if its energy bands are entirely filled or empty, preventing electron movement, whereas it is a metal if one or more bands are partly filled.
* Electron orbit flux `Φ` in a static magnetic field must be quantized, leading to discrete Landau energy eigenvalues `ε_n = (n + 1/2)ℏω_c + ℏ²k_z²/2m`.
* For a Josephson junction, the phase difference rate is `∂δ/∂t = −2qV/ℏ` when a dc voltage `V` is applied, resulting in a linear variation of the relative phase over time.
* A ferroelectric state is achieved when the coefficient `g₂` in the Landau free energy expansion passes through zero at a critical temperature `T₀`, often linked to the vanishing frequency of a transverse optical phonon mode.
* For an atom at a site with cubic symmetry, the local electric field `E_local` relates to the macroscopic field `E` and polarization `P` by `E_local = E + (4π/3)P`, a key component in the Clausius-Mossotti relation.
* The Lyddane-Sachs-Teller (LST) relation, `ω_L² / ω_T² = ε(ω)/ε(0)`, fundamentally connects the longitudinal and transverse optical phonon frequencies to the high-frequency and static dielectric constants, respectively.