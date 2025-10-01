# Rules for Particle Physics Reviews

**COVERAGE:** Across various domains of particle physics, astrophysics, and statistical methods.
**NOTES:** Units conventions are SI first, then cgs or other common units in parentheses. Metric signature is assumed to be mostly (+,-,-,-) for (E,p) and (t,x,y,z) 4-vectors in kinematics, with specific equations showing E² - |p|² = m².

**Generated on:** September 30, 2025 at 7:21 PM CDT

---

## Variational Principles & Equations of Motion

1. **Lorentz Transformation:** Energy and momentum must transform between frames according to the Lorentz transformation equations (Eq. 49.1).
2. **Center-of-Mass Energy:** For a collision of two particles with masses *m1* and *m2*, the total center-of-mass energy *E_cm* must be expressed by the Lorentz-invariant form (Eq. 49.2).
3. **Lab Frame E_cm:** In the lab frame (where *m2* is at rest), *E_cm* is given by (Eq. 49.3).
4. **Center-of-Mass Velocity & Gamma:** The velocity of the center-of-mass in the lab frame *β_cm* is *P_lab / (E_1lab + m2)* (Eq. 49.4), and its gamma factor *γ_cm* is *(E_1lab + m2) / E_cm* (Eq. 49.5).
5. **Center-of-Mass Momenta:** The c.m. momenta of incoming particles 1 and 2 must have magnitude *p_cm = p_1lab (m2 / E_cm)* (Eq. 49.6) and are explicitly given by *p_1cm = √(E_1cm² - m1²)* and *p_2cm = √(E_2cm² - m2²)* (Eq. 49.37).
6. **E_cm Differential Relation:** The relation *E_cm dE_cm = m2 dE_1lab = m2 β_1lab p_1lab dE_1lab* must hold (Eq. 49.7).
7. **Invariant Amplitude:** Matrix elements for scattering or decay processes must be written in terms of an invariant amplitude *-iM*.
8. **S-matrix Relation:** For 2 → 2 scattering, the S-matrix must be related to *M* by *(p'1 p'2 |S - 1| p1 p2) = i(2π)⁴ δ⁴(p1 + p2 - p'1 - p'2) (-iM)* (Eq. 49.8).
9. **Partial Decay Rate (Rest Frame):** The partial decay rate *dΓ* of a particle of mass *M* into *n* bodies in its rest frame is *dΓ = (1/(2M)) |M|² dΦn(P; p1, ..., pn)* (Eq. 49.11).
10. **n-body Phase Space:** The element of *n*-body phase space *dΦn* must be *dΦn(P; p1, ..., pn) = (2π)³⁻³ⁿ δ⁴(P - Σpi) Π [d³pi / (2Ei)]* (Eq. 49.12).
11. **Phase Space Recursion:** Phase space *dΦn* can be generated recursively (Eq. 49.13).
12. **Two-Body Decay Rate:** The partial decay rate *dΓ* for two-body decays is *dΓ = (1/(32π²)) |M|² (|p1| / M²) dΩ1* (Eq. 49.18).
13. **Invariant Mass Squared Identity:** When defining *m_ij² = (p_i + p_j)²*, the relation *m_12² + m_13² + m_23² = M² + m_1² + m_2² + m_3²* must hold.
14. **Invariant Mass Relation:** The invariant mass *m_12²* is defined as *(P - p3)² = M² + m3² - 2M E3*, where *E3* is the energy of particle 3 in the rest frame of *M*.
15. **Three-Body Decay Rate (General):** The partial decay rate *dΓ* for three-body decays can be written as *dΓ = (1/(256π⁵)) (1/M) |M|² dE1 dE2 dα d(cos δ) dγ* (Eq. 49.19).
16. **Three-Body Decay Rate (Alternative):** Alternatively, *dΓ = (1/(256π⁵)) (1/M²) |M|² |p1| |p3| dm12² dΩ3 dΩ1* (Eq. 49.20).
17. **Three-Body Decay Rate (Scalar/Averaged Spin):** If the decaying particle is a scalar or averaged over spin states, integration over angles in Eq. (49.19) for three-body decays gives *dΓ = (1/(2π³)) (1/(8M)) |M|² dE1 dE2 = (1/(2π³)) (1/(8M)) |M|² (1/(2M)) dm_12² dm_23²* (Eq. 49.22).
18. **Three-Body Dalitz Plot Limits:** For a given *m_12²*, the maximum value for *m_23²* is *(m_23²)_max = (E2' + E3')² - (√[E2'² - m2²] - √[E3'² - m3²])²* (Eq. 49.23a). The minimum value for *m_23²* is *(m_23²)_min = (E2' + E3')² - (√[E2'² - m2²] + √[E3'² - m3²])²* (Eq. 49.23b). *E2'* and *E3'* are the energies of particles 2 and 3 in the *m_12* rest frame.
19. **Invariant Mass Generalization:** If *p_ijk... = pi + pj + pk + ...*, then *M_ijk... = √(p_ijk...²)* (Eq. 49.26), and *M_ijk...* may be used in place of *m_12* in relations from Sec. 49.4.3 or Sec. 49.4.4.
20. **Differential Cross Section:** The differential cross section *dσ* is given by *dσ = ( (2π)⁴ / (4√[(p1·p2)² - m1² m2²]) ) |M|² dΦn(p1 + p2; p3, ..., pn)* (Eq. 49.27).
21. **Flux Factor (Lab & CM):** In the rest frame of *m2* (lab), *√[(p1·p2)² - m1² m2²] = m2 p1lab* (Eq. 49.28a). In the center-of-mass frame, *√[(p1·p2)² - m1² m2²] = p1cm √s* (Eq. 49.28b).
22. **Mandelstam Variables:** For 2 → 2 scattering, the Lorentz-invariant Mandelstam variables are defined as:
    * *s = (p1 + p2)² = (E_cm)² = m1² + m2² + 2E1E2 - 2p1·p2* (Eq. 49.29).
    * *t = (p1 - p3)² = (p2 - p4)² = m1² + m3² - 2E1E3 + 2p1·p3* (Eq. 49.30).
    * *u = (p1 - p4)² = (p2 - p3)² = m1² + m4² - 2E1E4 + 2p1·p4* (Eq. 49.31).
23. **Two-Body Cross Section:** The two-body cross section *dσ/dt* may be written as *dσ/dt = (1/(16πs²)) |M|²* (Eq. 49.33).
24. **CM Scattering Angle:** In the center-of-mass frame, *t = t0 - 2p_1cm p_3cm sin²(θ_cm/2)* (Eq. 49.34), where *θ_cm* is the angle between particle 1 and 3.
25. **CM Energy of Incoming Particles:** The center-of-mass energies of incoming particles are *E_1cm = (s + m1² - m2²) / (2√s)* and *E_2cm = (s + m2² - m1²) / (2√s)* (Eq. 49.36).
26. **Cosmological Equations of Motion:** Cosmological equations of motion must be derived from Einstein's equations (Eq. 22.6).
27. **Friedmann Equations:** The Friedmann equations (Eqs. 22.8 and 22.9) must be used.
28. **Energy Conservation Equation:** Energy conservation (T^μ_ν;μ = 0) must lead to the equation *ρ̇ = -3H(ρ+P)* (Eq. 22.10).
29. **Friedmann Equation Derivation Consistency:** The first Friedmann equation (Eq. 22.8) must also be derivable from the first law of thermodynamics.
30. **Higgs Production Channels:** The Standard Model Higgs boson can be produced resonantly in collisions of quarks, leptons, W or Z bosons, gluons, or photons.
31. **Higgs Cross Section Control:** The production cross section for Higgs bosons is controlled by its partial width into the entrance channel and its total width.
32. **Higgs to Gluons Process:** Higgs decay to two gluons proceeds through quark loops, with the *t* quark dominating.
33. **Higgstrahlung:** The Standard Model Higgs boson can be produced in the decay of a virtual W or Z ("Higgstrahlung").
34. **ZZ Fusion Analogy:** Fusion of ZZ to make a Higgs boson can be treated similarly to WW fusion.
35. **Quark-Antiquark Higgs Production:** Identical formulae apply for Higgs production in collisions of quarks whose charges permit W+ and W- emission, except QCD corrections and CKM matrix elements are required.

### Symmetry & Conservation Laws

1. **Photon Stability:** The photon must be stable.
2. **Gluon Color State:** Gluons must be SU(3) color octet gauge vector bosons, and each quark must come in three colors.
3. **Gluon Role:** Gluons are responsible for the formation of bound states (mesons and baryons).
4. **W Boson Charge:** The W boson charge must be ±1e.
5. **Charge Conjugation of Decays:** All W boson and Y(nS) decay modes must be charge conjugates of the listed modes.
6. **Lepton Family Number (LF) & Lepton Number (L) Conservation:** For specific decay modes, adhere to stated upper limits for LF and L violating modes (e.g., μ → eγ LF < 4.2 x 10⁻¹³, τ → e-2e+ L < 5.3 x 10⁻⁷).
7. **Neutrino Mass Ordering:** Normal Ordering (NO) implies *m₃ > m₂ > m₁*, and Inverted Ordering (IO) implies *m₂ > m₁ > m₃*.
8. **Mixing Matrix Element Magnitudes:** Experimentally, *|U_e1| > |U_e2| > |U_e3|*.
9. **Neutrino Mixing Matrix Unitarity:** All mixing matrices (CKM, neutrino) must be unitary.
10. **Majorana/Dirac Neutrino Phases:** Phases η₁, η₂ in the mixing matrix are physical if neutrinos are Majorana particles, but can be absorbed in wave functions in the Dirac case.
11. **CPT Symmetry Implication:** CPT symmetry implies the equality of the masses and widths of a particle and its antiparticle.
12. **Electric Charge Conservation:** Conservation of electric charge is associated with QED gauge symmetry.
13. **Lepton-Flavor Violation (Charged Leptons):** Lepton-flavor violation (LFV) in neutrinoless transitions from one charged lepton flavor to another has never been observed.
14. **Neutrinoless Double-Beta Decay (SM):** Neutrinoless double-β decay is forbidden in the Standard Model as it violates lepton number conservation (by 2 units).
15. **Quark Flavor Conservation:** Strong and electromagnetic forces must preserve quark flavor.
16. **Quark Flavor Change (Weak CC):** Charged-current weak interactions generate transitions among different quark species.
17. **Tree-Level Weak Transitions (SM):** In the Standard Model, tree-level weak transitions must satisfy a ΔF = ΔQ rule, where ΔQ is the change in hadron charge.
18. **FCNC Violation:** The ΔF = ΔQ rule can be violated by quantum loop contributions (FCNCs).
19. **Higgs Boson Quantum Numbers:** Higgs boson quantum numbers must be consistent with the J^PC = 0^+ hypothesis.
20. **Standard Model CP Violation Source:** Standard Model CP violation must originate from complex phases in Yukawa couplings.
21. **Single CP-Violating Parameter:** After removing unphysical phases in the Standard Model, only a single CP-violating parameter remains.
22. **CP Violation Classification:** Classify CP violation in mixing (type II) as indirect, and CP violation in decay (type I) as direct.
23. **CP Violation (Baryogenesis):** CP violation is a necessary condition for baryogenesis.
24. **Meson Quantum Numbers:**
    * Meson charge conjugation C must be (-1)^(l+s).
    * Meson parity P must be (-1)^(l+1).
    * Mesons made of a quark and its antiquark must be G-parity eigenstates with G = (-1)^(l+I₁).
25. **C Parity Conservation:** C parity forbids decays via a single-photon process (e.g., [f] on page 169).
26. **Angular Momentum Conservation:** Adhere to angular momentum conservation, which forbids certain decays (e.g., [e] on page 169).
27. **CP Violation in Leading Order:** Decays that violate CP in leading order serve as tests of direct CP violation, as indirect and CP-conserving contributions are suppressed.
28. **Time Reversal/Invariance (Neutron decay):** Time reversal invariance requires the α_ν parameter to be 0° or 180°. The D coefficient is zero if time invariance is not violated.
29. **4-Momentum Scalar Product:** The scalar product of two 4-momenta *p1 · p2 = E1 E2 - p1 · p2* must be invariant (frame independent).
30. **Rapidity Transformation:** Under a boost in the z-direction to a frame with velocity *β*, rapidity *y* transforms as *y → y - tanh⁻¹ β*.
31. **Rapidity Distribution Invariance:** The shape of the rapidity distribution *dN/dy* must be invariant under a z-boost.
32. **Rapidity Difference Invariance:** Differences in rapidity must be invariant under a z-boost.
33. **Electroweak Model Gauge Group:** The standard model of electroweak interactions must be based on the gauge group SU(2) x U(1).
34. **Meson Total Spin:** For mesons, total spin J must lie between *|l-s|* and *l+s*.

### Locality, Causality & Constraints

1. **Photon Mass Limit:** Photon mass must be less than 1 x 10⁻¹⁸ eV.
2. **Photon Charge Limit:** Photon charge must be less than 1 x 10⁻³⁵ e (mixed charge) and less than 1 x 10⁻³⁶ e (single charge).
3. **Electron Charge Anomaly:** *|q_e+ + q_e-|/e* must be less than 8 x 10⁻⁹.
4. **Neutrino Mass Squared Difference Constraint:** *|Δm²₂₁ - Δm²₃₁|* must be less than 1.1 x 10⁻⁴ eV² at 99.7% CL.
5. **Proton Charge Anomaly:** *|q_p + q_e|/e* must be less than 1 x 10⁻²¹, assuming *q_p = q_p̄ + q_e*.
6. **Proton Mean Life Limit:** Proton mean life must be greater than 9 x 10²⁹ years (for invisible mode) at 90% CL.
7. **Neutron n-n̄ Oscillation Time:** Mean n-n̄ oscillation time must be greater than 8.6 x 10⁷ s (free n) and greater than 4.7 x 10⁸ s (bound n) at 90% CL. Mean n-n̄' oscillation time must be greater than 448 s at 90% CL.
8. **Σ+ Decay Branching Ratio Limit:** The ratio *Γ(Σ+ → nℓ+ν)/Γ(Σ+ → nπ+)* must be less than 0.043.
9. **Magnetic Monopole Flux Limit:** Cosmic-ray supermassive monopole flux must be less than 1.4 x 10⁻¹⁶ cm⁻² s⁻¹ sr⁻¹ for 1 x 10⁻³ < β < 1.
10. **Proton Charge Radius:** Proton charge radius must be 0.8409 ± 0.0004 fm (and specifically 0.84087 ± 0.00039 fm from pp Lamb shift).
11. **Neutron Charge Anomaly:** Neutron charge *q* must be (-0.2 ± 0.8) x 10⁻²¹ e.
12. **Neutrinoless Double Beta Decay Half-life Limit:** The half-life for neutrinoless double beta decay with Majoron emission must be greater than 7.2 x 10²⁴ years at 90% CL.
13. **Radiation Dose Limits (ICRP):** Follow the ICRP recommendation [3]: average dose over 5 years must not exceed 20 mSv/year, and dose in any single year must be less than 50 mSv.
14. **Correlation Coefficient Bound:** The correlation coefficient *ρ_xy* must satisfy *|ρ_xy| ≤ 1*.
15. **Multivariate Gaussian Covariance Matrix:** For *n* Gaussian random variables, the covariance matrix *V* must be *n x n*, symmetric, and positive definite.
16. **Gaussian Probability Ranges:**
    * The probability *P(x in range μ ± σ)* for a Gaussian distribution is 0.6827.
    * The probability *P(x in range μ ± 0.6745σ)* for a Gaussian distribution is 0.5.
    * For a Gaussian distribution, *E[|x - μ|] = √(2/π)σ = 0.7979σ*.
    * For a Gaussian distribution, the half-width at half maximum must be *√2ln2 · σ ≈ 1.177σ*.
17. **Poisson Distribution Variance:** The variance of a Poisson distribution must equal its mean parameter *ν*.
18. **Three-Body Decay Planarity:** In the rest frame of *M*, the momenta of the three decay particles must lie in a plane. The relative orientation of the three momenta is fixed if their energies are known.
19. **Dalitz Plot Uniformity:** If *|M|²* is constant, the allowed region of the Dalitz plot must be uniformly populated with events (see Eq. 49.22).
20. **Random Variable Independence:**
    * Random variables *x* and *y* are independent if and only if *f(x,y) = f₁(x) · f₂(y)*.
    * If *x* and *y* are independent, then *ρ_xy = 0*.
    * If *x* and *y* are independent, then *E[u(x) v(y)] = E[u(x)] E[v(y)]*.
    * If *x* and *y* are independent, then *V[x+y] = V[x] + V[y]*.
    * If *f₁(x)* and *f₂(y)* are p.d.f.s for independent random variables *x* and *y* with characteristic functions *φ₁(u)* and *φ₂(u)*, then the characteristic function of the weighted sum *ax + by* is *φ₁(au)φ₂(bu)*.
21. **Three-Body Decay Max Momenta:** If, in a three-body decay, *m₃ > m₁, m₂*, then *|p1|_max > |p2|_max, |p3|_max*.

### Thermodynamics & Entropy Production

*(No specific rules were identified for this category beyond those integrated into Constitutive Relations or Equations of Motion.)*

### Scaling, Dimensional Analysis & RG

*(No specific rules were identified for this category beyond those integrated into Constitutive Relations.)*

### PDE Type, Regularity & Well-Posedness

*(Rules for cosmological equations of motion are covered under "Variational Principles & Equations of Motion".)*

### Boundary & Initial Conditions

1. **Curvature Constant:** Choose the curvature constant *k* to be +1 (closed), -1 (open), or 0 (spatially flat).

### Constitutive Relations & Material Laws

1. **Perfect Fluid Stress-Energy Tensor:** Use *T_μν = -P g_μν + (P + ρ) u_μ u_ν* (Eq. 22.7) for a perfect fluid.
2. **General Equation of State (Density):** For a single component with constant equation of state parameter *w = P/ρ*, the density *ρ ∝ R^(-3(1+w))* (Eq. 22.16).
3. **General Equation of State (Scale Factor):** For *w ≠ -1*, the scale factor *R(t) ∝ t^(2/(3(1+w)))* (Eq. 22.17).
4. **Radiation-Dominated Universe:** For a radiation-dominated universe, assume *w = 1/3*, which implies *ρ ∝ R⁻⁴* and *R(t) ∝ t¹/²*.
5. **Matter-Dominated Universe:** For a matter-dominated universe, assume *w = 0*, which implies *ρ ∝ R⁻³* (if *k=0*) and *R(t) ∝ t²/³*.
6. **Vacuum Energy Dominated Universe:** For a universe dominated by vacuum energy, assume *w = -1*, which implies *R(t) ∝ e^(√(Λ/3) t)*.
7. **Early Universe Energy Density:** For the early Universe at *T >> m_i*, approximate energy density by including only particles with *m_i < T* using *ρ = (π²/30) g(T) T⁴* (Eq. 22.42).
8. **Particle Decay Probability:**
    * The probability *P(t0)* that a particle lives for a time *t0* or greater before decaying is *P(t0) = e^(-t0/τ) = e^(-MΓt0/E)* (Eq. 49.14).
    * The probability *P(z0)* that a particle travels a distance *z0* or greater before decaying is *P(z0) = e^(-Mz0Γ/|p|)* (Eq. 49.15).
9. **Resonant Cross Sections:** Resonant cross sections are generally described by the Breit-Wigner formula (Sec. 18 of this Review): *σ(E) = [ (4π(2J+1)) / ((2s1+1)(2s2+1)) ] (Γ_in Γ_out / [(E - E0)² + Γ²/4]) (1/k²)* (Eq. 51.1).
10. **W Boson Partial Widths:**
    * *Γ(W → lν) = (G_F m_W³)/(6π√2)* (Eq. 51.22).
    * *Γ(W → q_i qbar_j) = 3 (G_F m_W³ |V_ij|²)/(6π√2)* (Eq. 51.23).
11. **Z Boson Partial Width:** *Γ(Z → ffbar) = N_c (G_F m_Z³ / (24π√2)) [(T_3^f - Q_f sin² θ_W)² + (Q_f sin² θ_W)²]* (Eq. 51.24).
12. **Higgs Boson Partial Widths:**
    * *Γ(H → ffbar) = (G_F m_H M_f² N_c) / (4π√2) (1 - 4M_f² / m_H²)^(3/2)* (Eq. 51.30).
    * *Γ(H → WW) = (G_F m_H³ / (8π√2)) (1 - α_W)^1/2 (4α_W + 3α_W²)*, where *α_W = 1 - 4m_W² / m_H²* (Eq. 51.31).
    * *Γ(H → ZZ) = (G_F m_H³ / (16π√2)) (1 - α_Z)^1/2 (4α_Z² + 3α_Z + 1)*, where *α_Z = 1 - 4m_Z² / m_H²* (Eq. 51.32).
    * *Γ(H → gg) = (G_F m_H³ α_s² / (16π√2)) |I(m_H² / (4m_q²))|²* (Eq. 51.33).
13. **Higgs to Gluon Loop Function:** For *z > 1/4*, *I(z) = (3/2) [ 2z + 2z(1 - 4z)^(1/2) sin⁻¹ (1 / (4z)^(1/2)) ]* (Eq. 51.34). In the limit *z → ∞*, *I(z) → 1*.
14. **Higgs Production Cross Sections:**
    * *σ(q_i qbar_j → WH) = (π² α |V_ij|² / (12 sin² θ_W)) (k / (s - m_W²)^2) (k² + 3m_W²)* (Eq. 51.35).
    * *σ(ffbar → ZH) = (πα² (L²+R²) / (48 N_c sin⁴ θ_W cos² θ_W)) (k / (s(s-m_Z²)²)) (k² + 3m_Z²)* (Eq. 51.36).
15. **Longitudinal W Distribution:** The distribution of longitudinal Ws carrying a fraction *y* of the electron’s energy is *f(y) = (g² / (16π²)) [ (1+(1-y)²)/y ] log(s/m_W²)*, where *g = e/sinθ_W* (Eq. 51.37).
16. **Higgs Decay to Longitudinal Ws:** In the limit *s >> m_H² >> m_W²*, the rate *Γ(H → W_L W_L) = (g² / (64π)) (m_H² / m_W²)*.
17. **Equivalent W Approximation:** In the equivalent W approximation, *σ(e+e- → ν_e νbar_e H) = (1 / (16m_W²)) (g² / sin² θ_W)² (m_W² / s) [ (1 + m_H²/s) log(s/m_W²) - 2 + m_H²/s ]* (Eq. 51.38).
18. **Early Universe CMB Spectrum:** The Cosmic Microwave Background (CMB) spectrum must be that of blackbody radiation.

### Stochastic Processes & Noise Models

1. **Poisson Distribution:** The Poisson distribution *f(n;ν)* gives the probability of finding exactly *n* events in a given interval when events occur independently and at an average rate *ν* per interval. It is the limiting case *p → 0, N = ∞, Np = ν* of the binomial distribution.
2. **Poisson to Gaussian Approximation:** The Poisson distribution must approach the Gaussian distribution for large *ν*.
3. **Gaussian Cumulative Distribution:** For a Gaussian distribution with mean 0 and variance 1, the cumulative distribution *F(0,1)* is *F(0,1) = 1/2 [1 + erf(x/√2)]* (Eq. 39.26). To adapt it for mean *μ* and variance *σ²*, replace *x* with *(x - μ)/σ*.
4. **Multivariate Gaussian PDF:** The joint p.d.f. for *n* Gaussian random variables *x_i* is the multivariate Gaussian *f(x; μ, V)* as given by Eq. 39.27.
5. **Multivariate Gaussian Covariance Elements:** The elements of the covariance matrix *V_ij* in the multivariate Gaussian are *E[(x_i - μ_i)(x_j - μ_j)] = ρ_ij σ_i σ_j*.
6. **Multivariate Gaussian Marginal Distribution:** The marginal distribution of any *x_i* from a multivariate Gaussian must be a Gaussian with mean *μ_i* and variance *V_ii*.
7. **Chi-Squared Distribution (Quadratic Form):** For *n* Gaussian random variables represented by vector *X* with covariance matrix *V*, the quadratic form *X^T V⁻¹ X* must obey the χ² distribution with *n* degrees of freedom.
8. **Chi-Squared Distribution (Sum of Normals):** If *z1,...,zn* are independent Gaussian random variables, the sum *χ² = Σ(zi - μi)² / σi²* must follow the χ² p.d.f. with *n* degrees of freedom, denoted *χ²(n)*.
9. **Chi-Squared Distribution (Sum of Chi-Squareds):** The sum of *χ²_i*, where each *χ²_i* follows χ²(*n_i*), must follow χ²(*Σ n_i*).
10. **Chi-Squared Distribution (Gaussian Approximation):** For large *n*, the χ² p.d.f. must approach a Gaussian with mean *n* and variance *2n*.
11. **Chi-Squared Goodness-of-Fit Context:** The χ² p.d.f. is often used in evaluating the level of compatibility between observed data and a hypothesis for the p.d.f. that the data might follow.
12. **Gamma Distribution:** For a process generating events according to a Poisson distribution, the distance from an arbitrary starting point to the *k*-th event must follow a gamma distribution, *f(z; λ, k)*.
13. **Exponential Distribution:** The special case *k=1* of the gamma distribution (*f(z; λ, 1) = λe^(-λz)*) is called the exponential distribution.
14. **Sum of Exponential Variables:** A sum of *k* exponential random variables *z_i* must be distributed as *f(Σz_i; λ, k)*.
15. **Gamma to Chi-Squared Relation:** For *λ = 1/2* and *k = n/2*, the gamma distribution reduces to the χ²(*n*) distribution.
16. **Variance of Variance Estimator (Gaussian):** If *x_i* are Gaussian distributed, the variance of *σ̂²* must be *2σ⁴/(n-1)* for any *n > 2*. For large *n* and Gaussian distributed *x_i*, the standard deviation of *σ̂²* is *σ²/√2n*.

### Units, Conventions & Signatures

1. **Unit Convention:** List SI units first, followed by cgs (or other common) units in parentheses where they differ.
2. **Becquerel Definition:** Define 1 Becquerel (Bq) as 1 disintegration per second.
3. **Gray Definition:** Define 1 Gray (Gy) as 1 J/kg.
4. **CKM Matrix Size:** The CKM matrix must be a 3x3 matrix.
5. **CKM Mixing Angles Quadrant:** Choose CKM mixing angles θ_ij to lie in the first quadrant (*0 < θ_ij < π/2*).
6. **Wolfenstein Parameterization Unitarity:** The CKM matrix written in terms of λ, A, ρ̄, and η̄ must be unitary to all orders in λ.
7. **Jarlskog Invariant Definition:** Define the Jarlskog invariant J by *Im(V_ij V_kl V_jk V_li) = Jε_iklmε_jln*.
8. **Unitarity Triangle Normalization:** The most commonly used unitarity triangle is derived from *V_ud V*_ub + V_cd V*_cb + V_td V*_tb = 0*, divided by *V_cd V*_cb.
9. **Weak Neutrino Eigenstates:** Weak neutrino eigenstates *|ν_α⟩* are defined as linear combinations of mass eigenstates *|ν_i⟩* via the mixing matrix U.
10. **Oscillation Probability:** Calculate oscillation probability between flavors α and β using Eq. 14.39 for plane monoenergetic ultra-relativistic waves.
11. **χ_ij Parameter Definition:** Define *χ_ij = Δm_ij² L / (4E) = 1.267 Δm_ij²(eV²) L(km)/E(GeV)*.
12. **Neutrino Effective Potential Sign:** For neutrino effective potential V, use + for neutrinos and - for antineutrinos.
13. **Instantaneous Mixing Angle in Matter:** Define the instantaneous mixing angle in matter θ_m(x) by *tan(2θ_m(x)) = (Δm² sin(2θ)) / (Δm² cos(2θ) - 2EG_F n_e(x))*.
14. **Robertson-Walker Metric:** Use the Robertson-Walker metric (Eq. 22.1) for a homogeneous and isotropic universe.
15. **Anisotropy Power Definition:** Anisotropy power per unit lnℓ must be *ℓ(ℓ+1)C_ℓ / (2π)*.
16. **CMB Mean Temperature:** The CMB must have a mean temperature of *T₀ = 2.7255 ± 0.0006 K*.
17. **CMB Temperature Evolution:** CMB temperature must evolve with redshift as *T(z) = T₀(1+z)* in an expanding Universe.
18. **CMB Anisotropy Expression:** Express CMB anisotropies using a spherical harmonic expansion (Eq. 29.1).
19. **CMB Linear Polarization Expression:** Express linear polarization patterns using spin-2 spherical harmonics.
20. **Particle Energy Gain:** Particles with charge Ze must gain energy *ΔE_b = ZeGl* in an RF electric field.
21. **Particle Momentum in Rings:** In circular rings, the momentum *p* of ultra-relativistic particles must be determined by *p = ZeBρ*.
22. **Momentum-Energy Relation:** For relativistic particles, *E_b[GeV] = 0.3Z[Bρ](Tm)*.
23. **Luminosity Formula:** Use the basic luminosity expression for head-on bunched beams (Eq. 31.15).
24. **Beam Size Relation:** Relate rms transverse beam sizes to normalized emittances and beta-functions by *σ_x,y² = β*_x,y ε_N_x,y / γ*.
25. **Synchrotron Radiation Power Loss:** Calculate synchrotron radiation power loss *P_SR = I_b ΔE_SR*.
26. **Synchrotron Radiation Energy Loss Per Turn (e+e-):** For e+e- beams, the SR energy loss per turn must be *ΔE_SR = 88.5 [keV/turn] E_b⁴[GeV]/ρ[m]*.
27. **Beam-Beam Tuneshift Parameter:** Characterize beam disruptions using the dimensionless beam-beam tuneshift parameter ξ (Eq. 31.16).
28. **Mass Stopping Power Units:** Express mass stopping power in units of MeV g⁻¹cm⁻².
29. **Linear Stopping Power Calculation:** Calculate linear stopping power in MeV/cm as *(-dE/dx) * ρ*.
30. **Electromagnetic Cascade Scale Variables:** Introduce scale variables *t = z/X₀* and *y = E/E_c* for describing electromagnetic cascades.
31. **Neutron β-Decay Parameters:** Define n → peν̄_e decay parameters g_A, g_V, g_WM by *B_i = [g_V² + g_A² + i(g_WM/m_n)σ_μν q^ν]B_i*, and α is defined by *g_A/g_V = |g_A/g_V|e^(iα)*.
32. **Quark Mass Definitions:**
    * u, d, and s quark masses must be reported as MS masses at the scale μ = 2 GeV.
    * c and b quark masses must be reported as MS masses renormalized at the MS mass (*m = m(μ=m)*).
33. **Light Meson Quark Composition:**
    * I=1 mesons (π, ρ, a) must be composed of ūd, (ūu−d̄d)/√2, or d̄u.
    * I=0 mesons (η, η', h, ω, φ, f, f') must be composed of *c₁(ūu+d̄d) + c₂(s̄s)*.
34. **CMB Anisotropy Interpretation:** Interpret variations in CMB temperature maps at higher multipoles (ℓ>2) as primarily the result of density perturbations in the early Universe.
35. **Cosmic Ray Energy Spectrum:** The differential spectrum of charged cosmic rays must follow a power-law dependence *E⁻γ*.
36. **Cosmic Ray Spectral Index (Knee):** At the "knee" (a few PeV), the cosmic ray spectral index γ must change from approximately 2.7 to approximately 3.
37. **Cosmic Ray Spectral Index (Second Knee):** At the "second knee" (approximately 100 PeV), the cosmic ray spectral index γ must change to approximately 3.3.
38. **Cosmic Ray Spectral Index (Ankle):** At the "ankle" (a few EeV), the cosmic ray spectral index γ must change to approximately 2.5.
39. **Cosmic Ray Flux Suppression:** The cosmic ray flux must be largely suppressed above a few tens of EeV.
40. **Radiation Worker Effective Dose Limits:** Recommended effective dose limit for radiation workers (whole-body) is 20 mSv yr⁻¹ in EU/Switzerland, and 50 mSv yr⁻¹ in the U.S.
41. **Equation, Section, Figure Numbering:** Equation, section, and figure numbers must follow those of the full Review.
42. **Kinematics Unit Convention:** In the Kinematics section, units must be used where *ħ = c = 1*.
43. **4-Vector Properties:** The energy *E* and 3-momentum *p* of a particle of mass *m* must form a 4-vector *p = (E,p)*. The square of the 4-vector *p* must be *p² = E² - |p|² = m²*. The velocity of the particle *β* must be *β = p/E*. Other 4-vectors, such as space-time coordinates of events, must transform in the same way as *E* and *p*.
44. **Two-Body Decay Momentum (In-flight):** The 4-momentum *p1²* for particle 1 in a two-body decay is *p1² = (M² - m2² + m1²) / (2M)* (Eq. 49.16).
45. **Two-Body Decay Momentum Magnitude:** The magnitude of momentum *|p1|* must equal *|p2|* and is given by *|p1| = |p2| = (1/(2M)) √[λ(M², m1², m2²)]* (Eq. 49.17), where *λ(a, b, c) = a² + b² + c² - 2ab - 2ac - 2bc* is the Källén function.
46. **Three-Body Decay Momenta (In-flight):**
    * The magnitude of momentum *|p1|* in the rest frame of the decaying particle must be *|p1| = (1/(2m_12)) √[λ(m_12², m_1², m_2²)]* (Eq. 49.21a).
    * The magnitude of momentum *|p3|* in the rest frame of the decaying particle must be *|p3| = (1/(2M)) √[λ(M², m_12², m_3²)]* (Eq. 49.21b).
47. **CM Energies of Incoming Particles:** The center-of-mass energies of incoming particles are *E_1cm = (s + m1² - m2²) / (2√s)* and *E_2cm = (s + m2² - m1²) / (2√s)* (Eq. 49.36). To get *E_3cm* and *E_4cm*, change *m1* to *m3* and *m2* to *m4* in Eq. 49.36.
48. **Energy and Momentum in Rapidity:** Choose the z-axis as the beam direction. The energy and momentum of a particle can be written as *E = m_T cosh y*, *p_x, p_y*, *p_z = m_T sinh y* (Eq. 49.38).
49. **Transverse Mass Definition:** *m_T*, conventionally called 'transverse mass', is given by *m_T² = m² + p_x² + p_y²* (Eq. 49.39).
50. **Rapidity Definition:** The rapidity *y* is defined by *y = (1/2) ln[(E + p_z) / (E - p_z)] = arctanh(p_z/E)* (Eq. 49.40).
51. **Rapidity Approximations/Identities:** For *p >> m*, rapidity *y* can be approximated by *y ≈ -ln tan(θ/2) = η* (Eq. 49.47), where *cos θ = p_z/p*. From the definition of *η*, the identities *sinh η = cot θ*, *cosh η = 1/sin θ*, *tanh η = cos θ* must hold (Eq. 49.48).
52. **Invariant Cross Section:** The invariant cross section *E d³σ / dp³* may also be rewritten as *(1/2π) (d²σ / (dp_T dy)) = (1/π) (d²σ / (dy d(p_T²)))* (Eq. 49.41).
53. **Feynman's x_F:** Feynman's *x_F* variable is given by *x_F = (E + p_z) / (E + p_z)_max* (for *p_T << p_L*) (Eq. 49.42). In the c.m. frame, *x_F_cm ≈ (2m_T sinh y_cm) / (√s)* (Eq. 49.43).
54. **CM Rapidity Maximum:** For the c.m. frame, *(y_cm)_max = ln(√s/m)* (Eq. 49.44).
55. **Invariant Mass for Two Particles:** The invariant mass *M* of a two-particle system (Sec. 49.4.2) can be written as *M² = m1² + m2² + 2[E_T(1)E_T(2) cosh Δy - p_T(1) · p_T(2)]* (Eq. 49.45).
56. **E_T(i) Definition:** *E_T(i)* is defined as *√[p_T(i)² + m_i²]* (Eq. 49.46).
57. **Cross Section for e+e- → γ → ffbar:** At c.m. energy squared *s*, *dσ/dΩ = (α² / (4s)) N_c β [ (1 + cos² θ) + (1 - β²) sin² θ ] Q²* (Eq. 51.2), where *β* is *v/c* for produced fermions, *θ* is the c.m. scattering angle, and *Q* is the fermion charge. *N_c* is 1 for charged leptons and 3 for quarks. In the ultrarelativistic limit (*β → 1*), *σ = (86.8 nb / s (GeV²)) N_c Q²* (Eq. 51.3).
58. **QCD Cross Sections:**
    * *qqbar → q'qbar'*: *dσ/dt = (4π α_s² / (9s²)) (s² + u²)/t²* (Eq. 51.4), with *t = -s sin²(θ/2)* and *u = -s cos²(θ/2)*.
    * *qg → qg*: *dσ/dt = (π α_s² / s²) (s²+u²)/t²* (Eq. 51.5).
    * *qq → qq* (identical quarks): *dσ/dt = (π α_s² / s²) [ (4/9) (s²+u²)/t² + (4/9) (t²+u²)/s² - (8/27) u²/(st) ]* (Eq. 51.6).
    * *qqbar → qqbar* (identical quarks): *dσ/dt = (π α_s² / s²) [ (4/9) (s²+t²)/u² + (4/9) (t²+u²)/s² - (8/27) t²/(su) ]* (Eq. 51.7).
    * *qbar q → gg*: *dσ/dt = (8π α_s² / (27s²)) (t² + u²)/tu* (Eq. 51.9).
    * *gg → qbar q*: *dσ/dt = (π α_s² / (6s²)) (t² + u²)/tu* (Eq. 51.10).
    * *gq → gq*: *dσ/dt = (π α_s² / (6s²)) (s² + u²)/t²* (Eq. 51.11).
    * *gg → gg*: *dσ/dt = (9π α_s² / s²) (3/8) (s²/t² + t²/u² + u²/s²)* (Eq. 51.12).
59. **Cross Section for e+e- → γγ:** *dσ/dΩ = (α² / (2s)) (u²/t² + t²/u²)* (Eq. 51.8).
60. **Lepton-Quark Scattering (Neglecting Z):** *dσ/dt (eq → eq) = (2π α² Q_q² / s²) (s² + u²)/t²* (Eq. 51.13).
61. **Neutrino Scattering (Four-Fermi):**
    * *νd → μu*: *dσ/dΩ = G_F² s / (π)* (Eq. 51.14).
    * *νbar u → μbar d*: *dσ/dΩ = G_F² s (1 + cosθ)² / (4π)* (Eq. 51.15).
62. **Deep Inelastic Scattering Variables:**
    * *x = Q² / (2Mν)*, where *ν = E - E'* is the energy lost by the lepton in the nucleon rest frame.
    * *y = ν/E*.
63. **Deep Inelastic Scattering Cross Sections (Parton Distributions):**
    * *eN → eX*: *d²σ / (dx dy) = (4πα² x / Q⁴) [1 + (1-y)²] [ (5/18) (u(x) + d(x) + ...) + (1/9) (ubar(x) + dbar(x) + ...) ]* (Eq. 51.17).
    * *νN → μ⁻ X*: *d²σ / (dx dy) = (G_F² s / π) [ (d(x) + ...) + (1-y)² (ubar(x) + ...) ]* (Eq. 51.18).
    * *νbar N → μ⁺ X*: *d²σ / (dx dy) = (G_F² s / π) [ (dbar(x) + ...) + (1-y)² (u(x) + ...) ]* (Eq. 51.19).
64. **Heavy Quark Hadroproduction Cross Sections:**
    * *qqbar → QQbar*: *σ(qqbar → QQbar) = (8π α_s² / (27s)) β [ (β² - 1)² + 4(m_Q²/s) (m_Q²/s - 1) + 2(m_Q²/s) ]* (Eq. 51.20).
    * *gg → QQbar*: Cross section is given by Eq. 51.21.
65. **Weak Mixing Angle:** *θ_W* is the weak mixing angle.
66. **CKM Matrix Elements:** *V_ij* are CKM matrix elements.
67. **N_c in Z Decays:** *N_c* is 3 for quarks and 1 for leptonic final states in the context of *Z → ffbar* width (Eq. 51.24).
68. **Fermion Couplings (ffbar → WW):** For *ffbar → WW*, *L* and *R* fermion couplings are defined as *L = 2(T₃ - Q_f sin² θ_W)* and *R = 2Q_f sin² θ_W*. *T₃* is the third component of weak isospin for the left-handed fermion *f*, and *Q* is the electric charge (in units of proton charge).
69. **sin² θ_W Shorthand:** *t_W = sin² θ_W*.
70. **N_c in Boson Production:** *N_c* is 3 for quarks and 1 for leptons in Eq. 51.26 (ffbar → WW) and Eq. 51.30 (Higgs decay to fermions).
71. **Cross Section for ffbar → WW:** The cross section for *ffbar → WW* is given by Eq. 51.26.
72. **Cross Section for q_i qbar_j → W⁺ Z⁰:** The cross section for *q_i qbar_j → W⁺ Z⁰* is given by Eq. 51.28, where *L_i* and *L_j* are the couplings of left-handed *q_i* and *q_j*, and *V_ij* is the CKM matrix element between *q_i* and *q_j*.
73. **Cross Section for q_i qbar_i → Z⁰ Z⁰:** The cross section for *q_i qbar_i → Z⁰ Z⁰* is given by Eq. 51.29.
74. **Monte Carlo Particle Numbering Scheme:**
    * The general form of a Monte Carlo particle number must be a 7-digit number following the pattern *±n n_l n_q1 n_q2 n_q3 n_j n_k*.
    * Tetra- and pentaquark states must be signified by a 9-digit code.
    * Nuclear codes must be 10-digit numbers.
    * Use the specified Monte Carlo particle numbers for the listed particles (e.g., Down quark is 1, Proton is 2212, Electron is 11, Photon is 22).
    * Certain excited baryons must follow the pre-2012 numbering scheme.
75. **CMB Dipole Interpretation:** Interpret the largest CMB anisotropy (ℓ=1 dipole) as the result of Doppler boosting of the monopole caused by Solar System motion relative to the CMB.
76. **Proton Mass:** Proton mass must be 1.007276466621 ± 0.000000000053 u or 938.27208816 ± 0.00000029 MeV.
77. **Proton-Antiproton Mass Difference:** *|m_p - m_p̄|/m_p* must be less than 7 x 10⁻¹⁰ at 90% CL.
78. **Proton Charge Anomaly:** *|q_p + q_p̄|/e* must be less than 7 x 10⁻¹⁹ at 90% CL.
79. **Neutron Mass:** Neutron mass must be 1.0086649160 ± 0.0000000005 u or 939.5654205 ± 0.000005 MeV.
80. **Neutron-Proton Mass Difference:** *m_n - m_p* must be 1.2933324 ± 0.0000005 MeV.
81. **a_s(m_Z) World Average:** The final world average value of *a_s(m_Z)* must be 0.1180 ± 0.0009.
82. **Higgs Boson Mass:** Higgs boson mass must be 125.20 ± 0.11 GeV.
83. **Higgs Production Cross-section (13 TeV):** The total SM Higgs production cross-section at LHC operating at 13 TeV must be *σ_13TeV(H) = 55.1 ± 3.3 pb*.
84. **Higgs Cross-section Scaling:** Higgs production cross sections increase by about 10% at 13.6-14 TeV.

### Numerical Methods & Discretization Assumptions

*(No specific rules were identified for this category.)*

### Measurement, Operational Definitions & Protocols

1. **Event Rate Calculation:** Calculate event rate *dN_exp/dt = σ_exp L*.
2. **Charged Particle Fluence for 1 Gy:** Calculate charged particle fluence (per cm²) to deposit one Gy as approximately *6.24 x 10⁹ / (dE/dx)* (dE/dx in MeV g⁻¹ cm⁻²).
3. **Photon Fluence for 1 Gy:** Calculate photon fluence (per cm²) to deposit one Gy as approximately *6.24 x 10⁹ / (Eℓf)* (E in MeV, ℓ in g cm⁻²).
4. **Maximum Energy Transfer (Formula):** Calculate the maximum energy transfer to an electron in a single collision using Eq. 34.4.
5. **Mass Stopping Power (Bethe Equation):** Calculate the mean rate of energy loss for moderately relativistic charged heavy particles using the Bethe equation (Eq. 34.5).
6. **Most Probable Energy Loss (Formula):** Calculate the most probable energy loss using *Δ_p = ξ [ln(ξ/I) + j - β² - δ(βγ)]*, where *ξ = (K/2)(Z/A)z²(x/β²) MeV* and *j = 0.200*.
7. **Radiation Length X₀ (Formula):** Calculate the radiation length *X₀* using Eq. 34.25.
8. **Bremsstrahlung Cross Section (Complete Screening):** Approximate the bremsstrahlung cross section in the "complete screening case" using Eq. 34.28.
9. **Simplified Bremsstrahlung Cross Section:** Use the simplified bremsstrahlung cross section (Eq. 34.29) when appropriate.
10. **Critical Energy E_c (Rossi Definition):** Define electron critical energy *E_c* as the energy at which ionization loss per radiation length equals the electron energy.
11. **Electron Critical Energy (Approximation):** Approximate *E_c* for electrons by *(610 MeV)/(Z + 1.24)* for solids and *(710 MeV)/(Z + 0.92)* for gases.
12. **Mean Longitudinal Energy Profile (Formula):** Describe the mean longitudinal profile of energy deposition in an electromagnetic cascade using a gamma distribution (Eq. 34.35).
13. **Muon Energy Loss (Formula):** Calculate the average rate of muon energy loss using *dE/dx = a(E) + b(E)E* (Eq. 34.39).
14. **Muon Range (Formula):** For approximately constant *a(E)* and *b(E)*, calculate the mean range *z₀* of a muon using *z₀ = (1/b) ln(1 + E₀/E_µc)* (Eq. 34.40).
15. **Cherenkov Angle (Formula):** Calculate the angle *θ_c* of Cherenkov radiation using *cosθ_c = 1/(nβ)* (Eq. 34.41).
16. **Cherenkov Radiation Threshold Velocity:** Cherenkov radiation threshold velocity *β_t* must be *1/n*.
17. **Cherenkov Photon Production (Formula):** Calculate the number of photons produced per unit path length and energy interval using Eq. 34.43 or Eq. 34.44.
18. **Transition Radiation Energy (Formula):** Calculate the energy radiated when a particle crosses a boundary using *I = αz²ħω_pγ/3* (Eq. 34.45).
19. **Transition Radiation Photon Yield (Formula):** Calculate the number of transition radiation photons above a fixed energy *ħω₀* using Eq. 34.47.
20. **Radiation Effects from Stack of Foils:** For a stack of N foil radiators, the intensity of coherent transition radiation is proportional to N (not N²).
21. **Statistical Probability Definitions:**
    * For a continuous random variable *x*, the probability *x* is between *z* and *z + dz*, given parameter(s) *θ*, is defined as *f(z; θ)dz*.
    * For a discrete random variable *z*, the probability of *z*, given parameter(s) *θ*, is defined as *f(z; θ)*.
22. **Cumulative Distribution Function:** The cumulative distribution function *F(a)* is defined as *F(a) = ∫ f(z) dz* (Eq. 39.6). If *z* is discrete-valued, replace the integral with a sum, including the endpoint 'a'.
23. **Expectation Value:** The expectation value of a function *u(x)*, *E[u(x)]*, is defined as *E[u(x)] = ∫ u(x) f(x) dx* (Eq. 39.7). If *x* is discrete-valued, replace the integral with a sum.
24. **Moments:**
    * The n-th moment of a random variable, *a_n*, is defined as *a_n = E[x^n]* (Eq. 39.8a).
    * The n-th central moment, *μ_n*, is defined as *μ_n = E[(x - a1)^n]* (Eq. 39.8b).
25. **Mean, Variance, Skewness, Kurtosis:**
    * The mean, *μ*, is defined as *μ = a1* (Eq. 39.9a).
    * The variance, *σ²* or *V[x]*, is defined as *σ² = V[x] = μ2 = a2 - μ²* (Eq. 39.9b).
    * The coefficient of skewness, *γ1*, is defined as *γ1 = μ3 / σ³*.
    * The kurtosis, *γ2*, is defined as *γ2 = μ4 / σ⁴ - 3*.
26. **Median:** The median, *x_med*, satisfies *F(x_med) = 1/2*.
27. **Marginal Probability Density Functions:** For two random variables *x* and *y* with joint p.d.f. *f(x,y)*, the marginal p.d.f. for *x* is *f1(x) = ∫ f(x,y) dy* and for *y* is *f2(y) = ∫ f(x,y) dx* (Eq. 39.10). If *x* or *y* is discrete-valued, replace the integral with a sum.
28. **Conditional Probability Density Functions:**
    * The conditional p.d.f. *f1(x|y)* is defined as *f(x,y) / f2(y)*.
    * The conditional p.d.f. *f2(y|x)* is defined as *f(x,y) / f1(x)*.
29. **Bayes' Theorem:** Bayes' theorem is *f1(y|x) = [f2(x|y) f1(y)] / f2(x) = [f2(x|y) f1(y)] / [∫ f2(x|y) f1(y) dy]* (Eq. 39.11).
30. **Correlation Coefficient Definition:** The correlation coefficient *ρxy* is defined as *ρxy = E[(x - μx)(y - μy)] / (σx σy) = cov[x,y] / (σx σy)* (Eq. 39.12).
31. **Covariance Definition:** The covariance *cov[x,y]* is defined as *∫∫ (x - μx)(y - μy) f(x,y) dx dy*. The variance *σx²* is defined as *∫∫ (x - μx)² f(x,y) dx dy*.
32. **Change of Variables (PDFs):** When changing variables from *x = (x1,...,xn)* to *y = (y1,...,yn)*, the new p.d.f. *g(y)* is given by *g(y) = f(x(y)) · |J|*, where *|J|* is the absolute value of the determinant of the Jacobian *Jij = ∂xi/∂yj*. For discrete variables, use *|J| = 1*.
33. **Characteristic Function:** For a continuous random variable *z* with p.d.f. *f(z)*, the characteristic function *φ(u)* is given by *φ(u) = E[e^(iuz)] = ∫ e^(iuz) f(z) dz* (Eq. 39.19).
34. **Moments from Characteristic Function:** The n-th derivative of *φ(u)* with respect to *u*, evaluated at *u=0*, is related to the n-th moment *a_n* by *[d^n φ(u)/du^n] |_(u=0) = i^n E[z^n] = i^n a_n* (Eq. 39.20).
35. **Estimator Notation:** An estimator for a parameter *θ* must be denoted as *θ̂* (with a hat). An estimator must be a function of the data used to estimate the parameter value.
36. **Unbiased Estimators:**
    * Use *μ̂ = (1/n) Σ xi* (Eq. 40.5) as an unbiased estimator for the mean *μ*.
    * Use *σ̂² = [1/(n-1)] Σ (xi - μ̂)²* (Eq. 40.6) as an unbiased estimator for the variance *σ²*.
37. **Variance of Mean Estimator:** The variance of the mean estimator *μ̂* must be *σ²/n*.
38. **Variance of Variance Estimator (General):** The variance of the variance estimator *σ̂²* is given by *V[σ̂²] = [1/n] (μ4 - [(n-3)/(n-1)] μ2²)* (Eq. 40.7), where *μ4* is the 4th central moment.
39. **Weighted Average:** If measurements *xi* have different, known variances *σi²*, use the weighted average *μ̂ = (Σ wi xi) / w* (Eq. 40.8) as an unbiased estimator for *μ* with *wi = 1/σi²* and *w = Σ wi*. The standard deviation of the weighted average *μ̂* is *1/√w*.
40. **Maximum Likelihood Estimators (MLEs):** Find MLEs for *θ* by solving the likelihood equations *∂lnL/∂θi = 0* for each parameter *θi* (Eq. 40.9).
41. **MLE Covariance Matrix Estimation:** Estimate the inverse *V⁻¹* of the covariance matrix for MLEs using *V_ij⁻¹ = -[∂²lnL/∂θi∂θj]* (Eq. 40.12).
42. **MLE Standard Deviations from Likelihood:** Obtain *s* times the standard deviations *σi* of MLEs from the distances in *θi* to the planes tangent to the surface defined by *ln L(θ) = ln L_max - s²/2* (Eq. 40.13).
43. **Least Squares Method:** Determine estimators by minimizing *χ²(θ) = -2lnL(θ) + constant = Σ [ (yi - μ(xi;θ))² / σi² ]* (Eq. 40.19). If measurements *y_i* have a covariance matrix *V_ij = cov[y_i, y_j]*, determine estimators by finding the minimum of *χ²(θ) = (y - μ(θ))^T V⁻¹ (y - μ(θ))* (Eq. 40.20).
44. **Frequentist Hypothesis Test:** Specify a critical region *w* in the data space. The probability of finding data *x* in *w* (under *H0*) must not exceed the specified size of the test *α*. Reject *H0* if the observed data falls within *w*. If data is discrete, *P(x ∈ w|H0) ≤ α*.
45. **Neyman-Pearson Lemma:** To maximize test power, choose the critical region *w* such that the likelihood ratio *Λ(x) = L(x|H1) / L(x|H0)* (Eq. 40.44) is *≥ cα* for all *x ∈ w*, and *< cα* outside *w*. Determine *cα* by the size of the test *α*.
46. **p-value Calculation:** A p-value quantifies agreement between *H0* and observed data *x*. Specify a subset of the data space that includes *x_obs* and represents data equally or less compatible with *H0*. Use constant values of a scalar statistic *t(x)* to define surfaces of equal compatibility. If large *t* implies poor agreement, calculate the p-value as *P(t > t_obs | H0)*.
47. **Goodness-of-Fit Statistic:** For a least squares fit, use the minimized *χ²* value (*t = χ²_min*) as a goodness-of-fit statistic.
48. **Chi-Squared Goodness-of-Fit:** If the fit function is correct, the minimized *χ²* statistic must follow a χ² p.d.f. for *n_d = N - M* degrees of freedom (N data points, M fitted parameters).
49. **Histogram Fitting (Chi-Squared):** The χ² p.d.f. approximation for goodness-of-fit remains approximately true for fitting a histogram with Poisson distributed data, provided there are sufficient entries in each bin.
50. **p-value from Chi-Squared:** Calculate the p-value for the χ² goodness-of-fit test using *p = ∫_(t_min)^∞ f(t; n_d) dt* (Eq. 40.55), where *f(t; n_d)* is the χ² p.d.f. for *n_d* degrees of freedom.
51. **Bayesian Hypothesis Testing:** A hypothesis *H* can be rejected in Bayesian statistics if its posterior probability *P(H|x)* is sufficiently small.
52. **Bayesian Prior Probability:** Write the full prior probability for models *Hi* and *Hj* as *π(Hi, θi) = P(Hi)π(θi|Hi)* (Eq. 40.61).
53. **Bayes Factor:** Define the Bayes factor *B_ij* using the ratio of integrals (Eq. 40.61). The Bayes factor *B_ij* gives the ratio of posterior probabilities for models *i* and *j* if the overall prior probabilities for the two models were equal.
54. **Bayesian Credible Interval:** A Bayesian (or credible) interval *[θ_lo, θ_up]* must contain a given fraction *1 - α* of the posterior probability, i.e., *1 - α = ∫_(θ_lo)^(θ_up) p(θ|x) dθ* (Eq. 40.66).
55. **Confidence Interval Construction (Frequentist):** Given a p.d.f. *f(x;θ)*, use a pre-defined rule and probability *1-α* to find for every value of *θ*, a set of values *x1(θ, α)* and *x2(θ, α)* such that *P(x1 ≤ x ≤ x2; θ) = ∫_(x1)^(x2) f(x;θ) dx ≥ 1-α* (Eq. 40.73).
56. **Gaussian Confidence Interval:** For data consisting of a single random variable *x* following a Gaussian distribution with known *σ*, the probability that the measured value *x* falls within *±δ* of the true value *μ* is *1-α = (1/√(2π)σ) ∫_(x-δ)^(x+δ) e^[- (x'-μ)² / (2σ²)] dx'* (Eq. 40.76).
57. **One-Sided Limits:** A one-sided (upper or lower) limit can be set by excluding above *x+δ* (or below *x-δ*). The *α* values for one-sided limits are half the values given for two-sided limits (e.g., Table 40.1).
58. **Coverage Probability and Parameters:** The *Δχ²* or *2ΔlnL* values corresponding to a coverage probability *1-α* in the large data sample limit for *m* parameters are given in Table 40.2.
59. **Poisson Limits (Neyman Procedure):** For Poisson distributed *n* events, the lower limit *μ_lo* on the mean *μ* from the Neyman procedure is *μ_lo = (1/2) F_χ²_inv(α_up; 2n)* (Eq. 40.82a). The upper limit *μ_up* is *μ_up = (1/2) F_χ²_inv(1 - α_up; 2(n+1))* (Eq. 40.82b).
60. **Binomial Limits (Neyman Procedure):** For binomially distributed *n* successes out of *N* trials with probability of success *p*:
    * The lower limit *p_lo* is *p_lo = nF_F_inv[1-α_up; 2n, 2(N-n+1)] / [ (N-n+1) + nF_F_inv[1-α_up; 2n, 2(N-n+1)] ]* (Eq. 40.83a).
    * The upper limit *p_up* is *p_up = (n+1)F_F_inv[1-α_lo; 2(n+1), 2(N-n)] / [ (N-n) + (n+1)F_F_inv[1-α_lo; 2(n+1), 2(N-n)] ]* (Eq. 40.83b).
61. **Three-Body Decay Kinematics (Endpoint):** For a three-body decay, the distribution of *m_12* values must possess an end-point or maximum value at *m_12 = M - m3*. This end-point can be used to constrain the mass difference of a parent particle and one invisible decay product.
62. **Invisible Particle Momentum Constraint:** If invisible particles are created in the final state at hadron colliders, their net momentum can only be constrained in the plane transverse to the beam direction.
63. **Missing Transverse Energy Vector:** The net transverse momentum of invisible particles is equal to the missing transverse energy vector *E_T_miss = - Σ_i p_T(i)* (Eq. 49.49), where the sum runs over transverse momenta of all visible final state particles.
64. **Transverse Mass (M_T):** The mass of the parent particle can be constrained with the quantity *M_T* (transverse mass), defined as *M_T² = [E_T(1) + E_T(2)]² - [p_T(1) + p_T(2)]² = m1² + m2² + 2[E_T(1)E_T(2) - p_T(1) · p_T(2)]* (Eq. 49.50). In this context, *E_T(1)* is defined as *p_T(1)* (Eq. 49.51). The distribution of event *M_T* values must possess an end-point at *M_T^max = M*.
65. **Pair Production with Semi-Invisible Final States:** For pair production with semi-invisible final states, *M* and *m* can be constrained with variables *M_T2* and *M_TR* defined in Refs. [4] and [5].
66. **Mandelstam Variables Identity:** The Mandelstam variables must satisfy *s + t + u = m1² + m2² + m3² + m4²* (Eq. 49.32).
67. **Deep Inelastic Scattering Correspondences:** The correspondences *[ (1 + cosθ) / 2 ] → (1-y)²* and *[ (1 - cosθ) / 2 ] → 1* must be used for deep inelastic scattering.
68. **Error Scaling:** Define and apply the scale factor *S = √χ²/(N − 1)* to enlarge errors when indicated, where N is the number of measurements used.
69. **Decay Momentum Definition (General):** Define decay momentum *p* for 2-body decays as the momentum of each product in the decaying particle's rest frame. For 3-or-more-body decays, define *p* as the largest momentum any product can have in the decaying particle's rest frame.
70. **W Boson Undetectable Decay Width:** Define W boson decay width into undetectable charged particles as those with momentum *p < 200 MeV*.
71. **Z-boson Mass Definition:** Define Z-boson mass as a Breit-Wigner resonance parameter, which is approximately 34 MeV above the real part of the pole position in the Z-boson propagator.
72. **Muon Decay Mode Separation:** When separating *e⁻γγ* and *e⁻e⁺e⁻* modes, regard *e⁻e⁺e⁻* as a subset of *e⁻γγ*, and include only events with electron energy > 45 MeV and gamma energy > 40 MeV.
73. **t Quark Mass Extraction:** Extract t-quark mass from event kinematics.
74. **B Meson Branching Fractions (Subchannel/Inclusive):** Correct resonant subchannels for resonance branching fractions to the final state. The sum of subchannel branching fractions *can* exceed that of the final state. Define inclusive branching fractions as average multiplicities (total number of observed particles divided by total number of B's). These can exceed 100% and inclusive partial widths can exceed total widths.
75. **Y(1S) (bb) ete- Branching Fraction:** The Y(1S) (ete-) branching fraction is not a pure measurement; it is derived from *Γ(hadron) + Γ(e+e-)*.
76. **Partial Mean Life (Nucleon Decay):** Partial mean life limits are on *τ/B_i*, where *τ* is total mean life and *B_i* is the branching fraction.
77. **AB = 2 Dinucleon Decay Limits:** Adhere to specified lifetime limits per iron nucleus for AB = 2 dinucleon modes.
78. **Accelerator Dark Matter Searches:** Assume dark matter particles escape the detector without interacting, leading to significant missing energy and momentum.
79. **Direct Dark Matter Detection Rate Assumptions:** Predicted WIMP event rates for direct detection must assume a certain dark matter mass, scattering cross section, local density (ρ₀), velocity distribution (f(v)), and escape velocity (v_esc).
80. **Indirect Dark Matter Detection Rate Dependency:** The production rate of detectable particles from indirect dark matter detection must depend on the annihilation/decay rate, the density of pairs/individual particles, and the number of final-state particles per event.
81. **CMB Monopole Measurement:** Measure the CMB monopole component only with absolute temperature devices.
82. **Detector Spatial Resolution:** Define spatial resolution as the intrinsic detector resolution, excluding multiple scattering effects. Analog detector readout can provide better spatial resolution than digital readout.
83. **Detector Time Resolution:** Define time resolution as the accuracy with which the time a particle crossed the detector can be determined.
84. **Detector Deadtime:** Define deadtime as the minimum separation in time between two resolved hits on the same channel.
85. **Kerma Definition:** Define Kerma as the sum of initial kinetic energies of all charged particles liberated by indirectly ionizing particles in a volume element of specified material, divided by the mass of that volume element.
86. **Exposure Definition:** Define Exposure with the implicit assumption that the small test volume is embedded in a sufficiently large, uniformly irradiated volume such that the number of secondary electrons entering equals the number leaving (charged particle equilibrium).
87. **Equivalent Dose Calculation:** Calculate equivalent dose *H_T* in an organ or tissue T as the sum of absorbed doses *D_T,R* for different radiation types R, weighted by radiation weighting factors *w_R* (Table 37.1).
88. **Effective Dose Calculation:** Calculate effective dose *E* as the sum of equivalent doses, weighted by tissue weighting factors *w_T* (with *Σ_T w_T = 1*) for sensitive organs and tissues.
89. **Cancer Induction Probability (Low LET):** The cancer induction probability for low LET radiation is about 5% per Sv on average for the entire population.
90. **Higgs Invisible Decay Limits:** Set limits on invisible Higgs decays at 95% confidence level.
91. **Neutrino Global Fits:** Perform global fits to neutrino data separately for Normal Ordering (NO) and Inverted Ordering (IO).
92. **³H β-decay Interpretation:** Interpret direct information from ³H β-decay as relating to *(m_β)² = Σ_i |U_ei|² m_i²*.
93. **Neutrinoless Double-Beta Decay (Majorana Neutrino):** If the neutrino is a Majorana particle, measurements of neutrinoless double-β decay half-lives provide information on *m_ββ = |Σ_i U_ei² m_i|*.
94. **LHC Data Fit (α_s constraint):** For fits to LHC data, the α_s constraint must be from an NNLO analysis of the transverse momentum distribution of Z bosons.
95. **Tevatron Data Fit (α_s and M_W):** For the Tevatron fit, use the α_s result from the inclusive jet cross-section at D0 and add the M_W result from CDF as adjusted in Ref. [208].
96. **Global Fit Confidence Level:** Global fits to all data must be reported at 90% CL.
97. **a_s(m_Z) World Average Calculation:** Calculate the *a_s(m_Z)* world average as an unweighted average of six subfields and the FLAG2021 lattice estimate.

### Assumptions, Domains of Validity & Prohibitions

1. **Data License:** Content is licensed under CC BY 4.0.
2. **Data Currency:** Data reflects an approximate closing date of January 15, 2024.
3. **Gluon Mass:** Gluon mass must be 0 (theoretical value).
4. **Higgs Full Width Assumption:** Higgs full width calculation assumes equal on-shell and off-shell effective couplings.
5. **Hypothetical Particle Mass Limits:** Adhere to specified confidence level (CL) mass limits for hypothetical particles, recognizing that mass limits for particles like L* depend on decay assumptions.
6. **Neutrino Mixing Scheme:** Neutrino mixing parameters are obtained from data analyses based on the 3-neutrino mixing scheme.
7. **Free Quark Searches:** All free quark searches conducted since 1977 have yielded negative results.
8. **Unestablished Particle Decay Limits:** For decay limits to particles not established, refer to designated search sections.
9. **B Meson Production at Υ(4S):** Assume 50% B⁰B⁰ and 50% B⁺B⁻ production at the Υ(4S) for branching fraction measurements. Rescale older B meson measurements to current Υ(4S) production ratios (50:50) and current D, D_s, D*, and τ branching ratios if it significantly affects averages and limits.
10. **B Meson Decay Vertex:** B⁰ and B± reactions must indicate the weak decay vertex and *not* include mixing.
11. **High-Energy b-hadron Production Fractions:** When reporting production fractions for weakly decaying b-hadrons at high energy, assume they are the same at LHC, LEP, and Tevatron. Normalize b-hadron production fractions such that B(B+)+B(B0)+B(Bs)+B(b-baryon) = 100%. Interpret reported production fractions as b-hadronization fractions, recognizing they may depend on kinematics and production environment.
12. **Y(nS) Decay Modes:** All Y(1S), Y(2S), and Y(3S) decay modes must be charge conjugates of the listed modes.
13. **Y(nS) Hadronic Decay Gluon Count:** Report Y(1S), Y(2S), and Y(3S) hadronic decay as 3g or 4g.
14. **P_c+ Classification:** P_c+ is classified as a pentaquark-charmonium state.
15. **Λ_c+ Decay Isospin Test:** The value [u] is a test that the isospin is indeed 0, so that the particle is indeed a Λ_c+.
16. **Ξ_c+ Doubly Cabibbo-Suppressed Decay:** The pK+π- decay of Ξ_c+ is a doubly Cabibbo-suppressed mode.
17. **Supersymmetric Particle Mass Bounds:** All supersymmetric mass bounds are model dependent. Assume the LSP is the lightest supersymmetric particle and R-parity is conserved (unless otherwise stated).
18. **Technicolor/Top-Color Limits:** Technicolor and top-color particle limits are varied and depend on assumptions.
19. **Excited Lepton Limits:** Limits from ℓ*ℓ* do not depend on Λ. Λ-dependent limits for excited leptons assume chiral coupling.
20. **Extra Dimensions:** Extra dimension bounds are model dependent.
21. **WIMP Event Rate Assumptions:** Predicted WIMP event rates must assume a certain dark matter mass, scattering cross section, local density (ρ₀), velocity distribution (f(v)), and escape velocity (v_esc).
22. **WIMP Search Results:** No confirmed evidence has been found for galactic WIMPs within specified mass and cross-section ranges.
23. **Accelerator Collider Center-of-Mass Energy:** For equal energy beams, the center-of-mass energy *E_cm* must be approximately *2E_b*.
24. **Beam-Beam Limits:** In circular hadron colliders, beam-beam limits must be *ξ < 0.01*. In circular e+e- colliders, beam-beam limits must be *ξ < 0.1*.
25. **Beamstrahlung Effect:** Recognize that beamstrahlung spreads the c.m.c. spectra of linear e+e- colliders.
26. **Hadron Collider Luminosity Limits:** Hadron collider luminosity is fundamentally limited by beam lifetime (inelastic pp interaction burn-off), SR heat in SC magnets, and radiation from collision debris.
27. **Mean Energy Loss (dE/dx) Caution:** Do not use the mean dE/dx as a dependable value for small samples; the most probable energy loss is more reliable.
28. **Electron/Positron Stopping Power Difference:** Acknowledge that stopping power for electrons/positrons differs from heavy particles due to kinematics, spin, charge, and identity effects.
29. **Photon Energy Loss Mechanisms:** At low energies, the photoelectric effect dominates for photons; pair production dominates at high energies but is suppressed by the LPM effect at ultrahigh energies.
30. **Photonuclear/Electonuclear Interactions:** At sufficiently high photon and electron energies (where LPM suppresses EM interactions), photonuclear and electronuclear interactions must predominate.
31. **Muon Critical Energy Definition:** Define the muon critical energy *E_µc* as the energy at which radiative and ionization losses are equal (*E_µc = a(E_µc)/b(E_µc)*).
32. **Cosmic Ray Origin:** Cosmic rays between hundreds of MeV and at least a few PeV are believed to be of galactic origin. Cosmic rays above a few EeV are most likely extra-galactic in origin.
33. **Proton Charge Radius Averaging Caution:** The proton electric charge radius values (*r_E^p* and *r_E^n*) are too different to average; the disagreement is not understood.
34. **Proton Magnetic Charge Radius Disagreement:** Acknowledge disagreement regarding the proton magnetic charge radius.
35. **Bound Neutron Oscillation Controversy:** Recognize controversy regarding nuclear physics and model dependence in the analysis of bound neutron oscillation limits.
36. **Mirror World Oscillation Condition:** For searches for n-n̄ oscillations in a mirror world, oscillations are maximal when magnetic fields B and B̄ are equal. The limit applies for any B in the range 0 to 12.5 µT.
37. **Λ_c(2595)+ Isospin Conservation:** Assuming isospin conservation, one-third of Λ_c(2595)+ decays to Λ_c(2455)+η.
38. **Lepton Symbol Interpretation:** The symbol ℓ indicates either an electron (e) or a muon (µ) mode, not their sum, unless explicitly stated (e.g., for W/Z decay modes or asymmetry parameters).
39. **Λ_c+ and Ξ_c+ Decay Branching Fraction Corrections:** Branching fractions for Λ_c+ and Ξ_c+ are corrected for decay modes not observed (e.g., K*(892)0 → K0π0 decays are multiplied up).
40. **Muon/Electron-Neutrino-Gamma Decay Consistency:** Measurements of *Γ(e±ν)* and *Γ(µ±ν)* *always* include decays with γ's. Measurements of *Γ(e±νγ)* and *Γ(µ±νγ)* *never* include low-energy γ's. To ensure consistency when separation is not possible, treat modes with γ's as subreactions of modes without them, and set *[Γ(e±ν) + Γ(µ±ν)]/Γ_total = 100%*.
41. **K⁰ Meson Modes (D decays):** When reporting D meson decay modes involving a neutral K meson, list them as K⁰ modes, not K⁰_S/L modes. Assume K⁰ is K⁰_S when interference effects between Cabibbo-allowed and doubly Cabibbo-suppressed modes invalidate the assumption *2Γ(K⁰_S) = Γ(K⁰)*.
42. **Λ_b Decay Branching Fractions:** *B(b-baryon → Λ_cℓ⁻ν̄_ℓ anything)* and *B(Λ_b → Λ_cℓ⁻ν̄_ℓ anything)* are not pure measurements; they are derived from products with *B(b → b-baryon)*. Λ_b inclusive branching fractions are defined as multiplicities and can be greater than one. b-baryon admixture branching fractions are averages over weakly decaying b-baryons, weighted by production rates, branching ratios, and detection efficiencies, and scale with *B(b → b-baryon)*.
43. **New Physics Contributions (S and T):** In constraints on S and T, these parameters represent the contributions of new physics *only*.
44. **α_s Fixing (S & T constraints):** When fitting S and T, fix *α_s = 0.1187* for datasets not involving *M_W* or *Γ_W*.
45. **Matter Content Assumption:** Assume the matter content of the Universe is a perfect fluid.
46. **Effective Degrees of Freedom (N(T)):** *N(T)* depends on the particle physics model. In the standard SU(3) x SU(2) x U(1) model, *N(T)* is specified up to O(100) GeV.
47. **Electroweak Model SM Errors:** Standard Model errors in *Γ_Z*, *Rℓ*, and *σ_had* are largely dominated by the uncertainty in *α_s*.
48. **Contact Interaction Scale Limit Definition:** For Lagrangian form given, define *Λ = Λ_L*. For other forms, refer to the Note in Listings.
49. **Contact Interaction Coupling:** For contact interactions, set *g²/4π* equal to 1.
50. **Estimators for Mean/Variance:** When using estimators for mean and variance, assume a set of *n* independent measurements, and assume each measurement follows a p.d.f. with unknown mean *μ* and unknown variance *σ²*. The measurements do not necessarily have to follow a Gaussian distribution for these estimators.
51. **MLE Standard Deviations Method:** Apply the method for standard deviations (Eq. 40.13) in the large sample limit.
52. **Least Squares Applicability:** The method of least squares is applicable for Gaussian distributed measurements *y_i* with mean *μ(x_i;θ)* and known variance *σ_i²*, or if measurements *y_i* have a covariance matrix *V_ij = cov[y_i, y_j]*.
53. **Neyman-Pearson Lemma Applicability:** For the Neyman-Pearson lemma, *H0* and *H1* must not contain undetermined parameters.
54. **Chi-Squared Goodness-of-Fit Conditions:** The rule that *χ²_min* follows a χ² p.d.f. for *n_d = N - M* degrees of freedom is conditional on the fit function being correct. This rule remains approximately true if data are approximately Gaussian, e.g., for fitting a histogram with Poisson data, provided sufficient entries in each bin. Assume the goodness-of-fit statistic follows a χ² p.d.f. under the hypothesis.
55. **Neyman Procedure Validity:** The limits from the Neyman procedure (Eqs. 40.82a, 40.82b for Poisson; Eqs. 40.83a, 40.83b for Binomial) apply under their respective distributional assumptions.
56. **Unified Approach for Intervals:** Use the unified approach of Feldman and Cousins [42] to overcome problems with these intervals.
57. **Resonant Cross Sections (Narrow Resonance):** Resonant cross sections, for a narrow resonance, may have the Breit-Wigner factor replaced by *πΓ δ(E - E0) / 2*.
58. **QCD Cross Section Assumptions (Massless Quarks):** The cross section for *qqbar → q'qbar'* (Eq. 51.4) requires treating all quarks as massless and averaging over initial quark colors. For hadroproduction of heavy quarks *Q = c, b, t*, include mass effects in the formulae.
59. **Higgs to Gluon Loop Function (Limits):** For *I(z)* in Higgs decay to gluons, *I(z)* is complex for *z < 1/4*. For *z < 2 x 10⁻³*, *|I(z)|* is small, so light quarks contribute negligibly to *Γ(H → gg)*.
60. **Higgs Production (W/Z Fusion):** For Higgs production via W and Z fusion, the longitudinal components of Ws and Zs are important.
61. **Fine-Structure Constant Evaluation:** Even without QCD corrections, the fine-structure constant *α* ought to be evaluated at the scale of the collision, e.g., *m_W*.
62. **ZZ Fusion Process:** All quarks must contribute to the ZZ fusion process.
63. **Ellipsoids as Error Indicators:** The validity of using ellipsoids as indicators of probable error (Sec. 40.4.2.2) assumes that *μ* and *V* are correct.
64. **Single Production with Semi-Invisible Final States:** When considering a single heavy particle decaying to two particles (one invisible, particle 1), use the definitions for *M_T* (Eq. 49.50) and *E_T(1)* (Eq. 49.51). If *m1 = m2 = 0*, *M_T² = 2|p_T(1)||p_T(2)|(1 - cos φ_12)* (Eq. 49.52).
65. **Pair Production with Semi-Invisible Final States:** For pair production with semi-invisible final states, assume two identical heavy particles of mass *M* are produced such that their combined center-of-mass is at rest in the transverse plane.
66. **K± Decay Form Factors:** K± decay form factors can be assumed with μ-e universality or not.

## Key Highlights

* Energy and momentum must transform via Lorentz transformation, with the square of a particle's 4-momentum, E² - |p|², being invariant and equal to its mass squared, m².
* Matrix elements for scattering or decay processes are expressed using an invariant amplitude *-iM*, which is central to calculating partial decay rates and differential cross sections, such as *dσ/dt = (1/(16πs²)) |M|²* for two-body scattering.
* The Friedmann equations and the energy conservation equation *ρ̇ = -3H(ρ+P)* are essential for deriving and describing the evolution of a homogeneous and isotropic universe based on its matter and energy content.
* Fundamental symmetries like CPT imply the equality of particle and antiparticle masses and widths. Electric charge conservation is tied to QED gauge symmetry, and lepton-flavor violation in charged lepton transitions has not been observed.
* The Standard Model Higgs boson has a mass of 125.20 ± 0.11 GeV. Its production cross section and decay partial widths are crucial parameters described by specific formulae depending on the decay channel.
* The probability of a particle living for a time *t0* before decaying follows *P(t0) = e^(-t0/τ)*. Resonant cross sections are generally described by the Breit-Wigner formula, which is critical for understanding particle resonances.
* The mean rate of energy loss for moderately relativistic charged heavy particles is accurately described by the Bethe equation, while phenomena like synchrotron radiation contribute significantly to energy loss in accelerators.
* Maximum Likelihood Estimators (MLEs) and the Least Squares method are primary techniques for parameter estimation, while the Chi-Squared distribution provides a framework for goodness-of-fit tests and for constructing confidence intervals.
* For processes involving invisible final state particles at hadron colliders, their net transverse momentum is measured as the missing transverse energy vector *E_T_miss*. The transverse mass *M_T* is then used to constrain the mass of the parent particle, exhibiting an endpoint at *M_T^max = M*.
* The differential spectrum of charged cosmic rays exhibits a power-law dependence *E⁻γ*, with distinct changes in the spectral index occurring at characteristic energies known as the 'knee,' 'second knee,' and 'ankle'.

## Next Steps & Suggestions

* Develop or integrate automated tools for verifying adherence to the fundamental kinematic, dynamic, and statistical rules outlined in the summary across event generators, detector simulations, and analysis pipelines, ensuring consistency and correctness.
* Conduct a focused review of current experimental constraints on unobserved phenomena (e.g., lepton-flavor violation, neutrinoless double-beta decay, proton decay, dark matter candidates) to identify and prioritize next-generation search strategies that push these limits further or explore parameter spaces where the Standard Model predicts zero.
* Establish a working group to standardize and cross-validate critical statistical methodology implementations (e.g., Maximum Likelihood Estimation, confidence interval construction, hypothesis testing procedures) against benchmark datasets to enhance the robustness and comparability of physics results across experiments.
* Perform a systematic sensitivity analysis for key Standard Model measurements (e.g., Higgs boson properties, W/Z boson widths) to variations in underlying Beyond-Standard-Model assumptions or model dependencies, and develop strategies for reporting results with reduced reliance on specific new physics models.