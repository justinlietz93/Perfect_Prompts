# Rules for Quantum Field Theory

**COVERAGE:** Introductory to advanced Quantum Field Theory concepts.
**NOTES:** Natural units ($c=1, \hbar=1$) are employed unless otherwise specified. The Minkowski metric signature is $\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$. Summation convention is always implicitly used for repeated indices.

**Generated on:** September 30, 2025 at 10:31 PM CDT

---

## Variational Principles & Equations of Motion

1. **Formulate Field Dynamics:** The true path taken by a system must correspond to an extremal of the action ($S$), which means $\delta S = 0$.
2. **Derive Equations of Motion (Euler-Lagrange):** For fields $\phi_a$, the equations of motion are given by $\partial_\mu \left( \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi_a)} \right) = \frac{\partial \mathcal{L}}{\partial \phi_a}$.
3. **Define Hamiltonian Density:** The Hamiltonian density $\mathcal{H}$ must be given by $\mathcal{H} = \pi^a(\mathbf{x}) \dot{\phi}_a(\mathbf{x}) - \mathcal{L}(\mathbf{x})$, where $\dot{\phi}_a(\mathbf{x})$ is eliminated in favor of the conjugate momentum $\pi^a(\mathbf{x})$.
4. **Define Total Hamiltonian:** The total Hamiltonian $H$ must be $H = \int d^3x \mathcal{H}$.
5. **Formulate Quantum Dynamics:** The dynamics of a quantum system must be governed by the Hamiltonian operator $H$.
6. **Ensure First-Order Time Evolution (Dirac Fields):** For an equation of motion where the momentum conjugate $\pi$ does not involve the time derivative of the field, the equation of motion must be first order in time (e.g., Dirac field).
7. **Determine Full Evolution with Initial Conditions:** Specify the field $\psi$ and its conjugate momentum $\pi$ on an initial time slice to determine the full evolution of a first-order equation of motion.
8. **Define Dirac Lagrangian:** Use the form $\mathcal{L} = \bar{\psi}(x) (i\slash{\partial} - m) \psi(x)$ (Eq. 5.1).
9. **Fermionic Propagator Must Satisfy Dirac Equation:** Away from singularities, the fermionic propagator $S(x-y)$ must satisfy $(i\slash{\partial} - m)S(x-y) = 0$ (Eq. 5.32).
10. **Feynman Propagator as Green's Function:** The Feynman propagator $S_F(x-y)$ must satisfy $(i\slash{\partial} - m)S_F(x-y) = i\delta^4(x-y)$.
11. **Derive Maxwell's Equations:** Maxwell's equations in the absence of sources must follow from the Lagrangian $\mathcal{L} = -\frac{1}{4} F^{\mu\nu} F_{\mu\nu}$, yielding $\partial_\mu F^{\mu\nu} = 0$.
12. **Relate Electric and Magnetic Fields to Potentials:** The electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ must be defined from the 4-component field $A^\mu = (\phi, \mathbf{A})$ as $\mathbf{E} = -\mathbf{\nabla}\phi - \partial\mathbf{A}/\partial t$ and $\mathbf{B} = \mathbf{\nabla} \times \mathbf{A}$.

### Symmetry & Conservation Laws

1. **Adhere to Spin-Statistics Theorem:**
    * Quantize integer-spin fields as bosons.
    * Quantize half-integer-spin fields as fermions.
    * Failure to adhere will lead to inconsistencies (e.g., unbounded Hamiltonian, negative norm states).
2. **Noether's Theorem:** Every continuous symmetry of the Lagrangian must give rise to a conserved current $j^\mu(x)$ such that the equations of motion imply $\partial_\mu j^\mu = 0$.
3. **Conserved Charge from Current:** A conserved current $j^\mu$ implies a conserved charge $Q$, defined as $Q = \int d^3x j^0$.
4. **Lorentz Invariance Definition:** For a theory to be Lorentz invariant, if $\phi(x)$ solves the equations of motion, then $\phi(\Lambda^{-1}x)$ must also solve the equations of motion.
5. **Requirement for Lorentz Invariance:** Ensure the action is Lorentz invariant to guarantee Lorentz invariance of the theory.
6. **Infinitesimal Lorentz Transformation Constraint:** The infinitesimal form $\omega^{\mu\nu}$ of a Lorentz transformation must be an anti-symmetric matrix ($\omega^{\mu\nu} = -\omega^{\nu\mu}$).
7. **Definition of Internal Symmetry:** An internal symmetry is one that only involves a transformation of the fields and acts the same at every point in spacetime.
8. **Interpretation of Conserved Charges:** Conserved charges arising from internal symmetries must have the interpretation of electric charge or particle number (e.g., baryon or lepton number).
9. **Gauge Symmetry Definition:** The vector potential $A_\mu(x)$ must possess a gauge symmetry acting as $A_\mu(x) = A_\mu(x) + \partial_\mu \Lambda(x)$ for any function $\Lambda(x)$.
10. **Gauge Invariance of Field Strength:** The field strength $F_{\mu\nu}$ must be invariant under gauge transformations (e.g., $A_\mu \to A_\mu + \partial_\mu \Lambda$).
11. **Physical State Identification (Gauge Symmetry):** Two states related by a gauge symmetry must be identified as the same physical state.
12. **Axial Current Conservation:** The S-matrix formalism implies axial current conservation.
13. **Charge Conjugation for Dirac Spinor:** The charge conjugate spinor $\psi^c$ must satisfy the Dirac equation with charge $-e$ instead of $+e$.
14. **Conserve Fermion Number in Diagrams:** Ensure that the arrows on fermion lines flow consistently through Feynman diagrams.

### Locality, Causality & Constraints

1. **Locality Principle:** All interactions must be mediated in a local fashion by the field.
2. **Lagrangian Locality:** Only consider local Lagrangians, meaning no terms directly coupling $\phi(\mathbf{x}, t)$ to $\phi(\mathbf{y}, t)$ with $\mathbf{x} \neq \mathbf{y}$.
3. **Local Charge Conservation:** Charge must be conserved locally.
4. **Ensure Positive Definite Hilbert Space Norm:** The Hilbert space for a quantized theory must have a positive definite norm.
5. **Prohibit Negative Norm States:** Do not define the vacuum state for a Dirac field such that `c†` (a creation operator from a bosonic quantization attempt) annihilates it, as this leads to states with negative norm.
6. **Prohibit Unbounded-Below Hamiltonian:** The Hamiltonian of a physical theory must be bounded below (to prevent energy-tumble).
7. **Prohibit Single-Particle Dirac Interpretation:** Do not interpret the Dirac equation as consistently describing a single particle. It must be viewed as a classical field.
8. **Ensure Causality for Observables:** The theory remains causal if fermionic operators are not directly observable, but rather observables are bilinear in fermionic fields (e.g., Hamiltonian). This ensures observables commute for spacelike separations.
9. **Non-Dynamical $A_0$ (Absence of Charged Matter):** In the absence of charged matter, the field $A_0$ must not be dynamical (i.e., it has no kinetic term in the Lagrangian).
10. **$A_0$ Determination (Absence of Charged Matter):** In the absence of charged matter, $A_0$ is fully determined by the equation of motion $\mathbf{\nabla} \cdot \mathbf{E} = 0$.
11. **Particle Number Non-Conservation:** The combination of quantum mechanics and special relativity implies that particle number is not conserved.
12. **Compton Wavelength Phenomenon:** At distances shorter than the Compton wavelength ($\lambda = \hbar / (mc)$), there is a high probability of detecting particle-antiparticle pairs.
13. **Decay Condition:** The decay of a meson to a nucleon-anti-nucleon pair only happens if $m_{meson} > 2M_{nucleon}$.
14. **Propagator `+iε` Condition (Stable Meson):** For nucleon-anti-nucleon scattering, if $m_{meson} < 2M_{nucleon}$, the `$i\epsilon$` term in the propagator denominator may be dropped.
15. **Propagator `+iε` Condition (Unstable Meson):** When correctly treated, the instability of a meson ($m_{meson} > 2M_{nucleon}$) adds a finite imaginary piece to the denominator of the amplitude, which overwhelms the `$i\epsilon$` term.
16. **Compton Scattering Constraint:** The amplitude for Compton scattering must vanish for longitudinal photons.
17. **Real Scalar-Gauge Field Coupling Prohibition:** A real scalar field cannot be coupled to a gauge field, as it lacks a suitable conserved current.
18. **Momentum Conservation from Delta Function:** The $\delta$-function in S-matrix elements imposes constraints on possible decays and follows from spacetime translational invariance.

### Thermodynamics & Entropy Production

*(No specific rules from the provided text segments within this category.)*

### Scaling, Dimensional Analysis & Renormalization Group

1. **Natural Units for Dimensions:** All quantities in QFT (mass, length, time, energy, momentum) are expressed in terms of mass dimensions `[X] = d` where `c=1` and `ħ=1`.
2. **Action Dimensionality:** The action $S$ must have mass dimensions of $0$.
3. **Lagrangian Density Dimensionality:** The Lagrangian density $\mathcal{L}$ must have mass dimensions of $4$.
4. **Field Dimensionality:**
    * A scalar field $\phi$ must have mass dimensions of $1$ (`[φ] = 1`).
    * A Dirac field $\psi$ must have mass dimensions of $3/2$ (`[ψ] = 3/2`).
5. **Mass Dimensionality:** A mass parameter $m$ must have mass dimensions of $1$.
6. **Coupling Constant Dimensionality:** For an interaction term $\lambda_n \phi^n/n!$ in the Lagrangian, the mass dimension of the coupling constant is $[\lambda_n] = 4-n$.
    * The Yukawa coupling constant `λ` for $\bar{\psi}\psi\phi$ has dimension $0$ (`[λ] = 0`).
7. **Relevant Coupling:** If $[\lambda_3] = 1$, the coupling $\lambda_3 \phi^3$ is "relevant," acting as a small perturbation at high energies $E \gg \lambda_3$ and a large perturbation at low energies $E \ll \lambda_3$.
8. **Marginal Coupling:** If $[\lambda_4] = 0$, the coupling $\lambda_4 \phi^4$ is "marginal," acting as a small perturbation if $\lambda_4 \ll 1$.
9. **Irrelevant Coupling:** If $[\lambda_n] < 0$ for $n > 5$, the coupling $\lambda_n \phi^n$ is "irrelevant," acting as a small perturbation at low energies and a large perturbation at high energies.
10. **Consequence of Irrelevant Operators:** Irrelevant operators typically lead to "non-renormalizable" field theories, which are incomplete at some energy scale.

### PDE Type, Regularity & Well-Posedness

1. **Lagrangian Derivative Order:** Only consider Lagrangians depending on $\mathbf{\nabla}\phi$ and not higher spatial derivatives.
2. **Lagrangian Explicit Time/Space Dependence:** Do not consider Lagrangians with explicit dependence on $x^\mu$; all such dependence must come only through fields $\phi$ and their derivatives.
3. **Maxwell's Equations and Uniqueness:** Maxwell's equations are not sufficient to uniquely specify the evolution of $A_\mu$ (leading to a uniqueness problem) if $A_\mu$ is considered a physical object.

### Boundary & Initial Conditions

1. **Variational Principle Boundary Conditions:** When deriving equations of motion, field variations $\delta\phi_a(\mathbf{x}, t)$ must decay at spatial infinity and obey $\delta\phi_a(\mathbf{x}, t_1) = \delta\phi_a(\mathbf{x}, t_2) = 0$.
2. **Coulomb Gauge Initial Data:** In Coulomb gauge, the initial field $A_0$ is not independent and cannot be specified on the initial time slice.

### Field Interactions & Gauge Theory Principles

1. **Define Conjugate Momentum:** The momentum $\pi^a(\mathbf{x})$ conjugate to $\phi_a(\mathbf{x})$ must be defined as $\pi^a(\mathbf{x}) = \frac{\partial \mathcal{L}}{\partial \dot{\phi}_a}$.
2. **Covariant Derivative Transformation:** The covariant derivative $D_\mu \psi = \partial_\mu \psi + ieA_\mu \psi$ must transform as $D_\mu \psi \to e^{-ie\Lambda} D_\mu \psi$ under gauge transformation $A_\mu \to A_\mu + \partial_\mu \Lambda$ and $\psi \to e^{-ie\Lambda} \psi$.
3. **Minimal Coupling Rule:** To couple a U(1) symmetry to a gauge field, replace all derivatives by suitable covariant derivatives. This procedure is called minimal coupling.
4. **Electric Charge Definition:** The coupling constant $e$ in the interaction term (e.g., $e \bar{\psi} \gamma^\mu A_\mu \psi$) must be interpreted as the electric charge of the $\psi$ particle.
5. **Fine Structure Constant Relation:** In QED, the electric charge $e$ is related to the dimensionless fine structure constant $\alpha = e^2 / (4\pi \hbar c)$.
6. **Charged Scalar Interaction Rules:** For charged scalars, the cubic vertex Feynman rule is $-ie(p+q)^\mu$, and the quartic "seagull" vertex rule is $+2ie\eta^{\mu\nu}$.
7. **Seagull Diagram Combinatoric Factor:** The factor of two in the seagull diagram arises because of the two identical particles appearing in the vertex.

### Stochastic Processes & Noise Models

*(No specific rules from the provided text segments within this category.)*

### Units, Conventions & Signatures

1. **Natural Units Convention:** Use "natural" units, where $c=1$ and $\hbar=1$.
2. **Mass Dimension Notation:** If a quantity $X$ has dimensions of (mass)$^d$, denote it as $[X]=d$.
3. **Minkowski Metric Convention:** Use the Minkowski space metric $\eta_{\mu\nu} = \text{diag}(+1, -1, -1, -1)$.
4. **Summation Convention:** Employ the summation convention in which repeated indices (spacetime or spin) are summed over. Implicitly sum over spin indices $s=1,2$ unless explicitly stated otherwise.
5. **Spacetime Index Placement:** For spacetime indices, it is crucial to keep track of whether they are up or down; expressions like $a^\mu b^\mu$ must not be encountered.
6. **Dummy Index Usage:** Do not use the same pairs of dummy indices twice.
7. **Fourier Transform Convention:** The Fourier transform convention is $f(x) = \int \frac{d^4k}{(2\pi)^4} \tilde{f}(k)e^{-ik \cdot x}$.
8. **Dirac Delta Function Definition:** The Dirac delta function $\delta(x)$ is defined by $\delta(x) = 0$ for $x \neq 0$ and $\int_{-\infty}^{+\infty} \delta(x) dx = 1$.
9. **Residue Theorem:** For a positively oriented (anticlockwise) simple closed contour $\Gamma$ within which $f(z)$ is analytic except for isolated singular points $z_j$, $\oint_\Gamma f(z) dz = 2\pi i \sum_{j=1}^n b_j$, where $b_j$ is the residue at $z_j$.
10. **Operator Notation:** Do not denote operators with a hat; context must clarify whether an object is classical or quantum.
11. **Fermionic Propagator as Matrix:** Remember that the fermionic propagator $S(x-y)$ is a $4x4$ matrix.
12. **Fermion Operator Ordering (States):** The ordering of creation and annihilation operators in initial and final states is crucial and affects the overall sign of the amplitude.
13. **Photon Polarization Normalization (Lorentz Gauge):** Photon polarization vectors $e^{(\lambda)}_\mu(p)$ must be normalized such that $e^{(\lambda)*}_\mu(p) e^{(\sigma)}_\nu(p) \eta^{\mu\nu} = \eta^{\lambda\sigma}$.
14. **Photon Polarization Conditions (Coulomb Gauge):** In Coulomb gauge, photon polarization vectors $\mathbf{e}^{(r)}(p)$ must be perpendicular to the momentum ($\mathbf{e}^{(r)}(p) \cdot \mathbf{p} = 0$) and orthonormal ($\mathbf{e}^{(r)}(p) \cdot \mathbf{e}^{(s)}(p) = \delta_{rs}$).

### Quantum Field Theory Formalism & Feynman Rules

1. **Quantize Dirac Fields as Operators:** Promote the Dirac field $\psi$ and its momentum $\pi$ to operators.
2. **Fermionic Anti-Commutation Relations (Fields):** For fermionic quantization of spinor fields, they must satisfy the anti-commutation relations:
    * $\{\psi_\alpha(x), \psi_\beta(y)\} = 0$
    * $\{\psi^\dagger_\alpha(x), \psi^\dagger_\beta(y)\} = 0$
    * $\{\psi_\alpha(x), \psi^\dagger_\beta(y)\} = \delta_{\alpha\beta} \delta^3(x - y)$ (Eq. 5.14).
3. **Fermionic Anti-Commutation Relations (Operators):** When quantizing Dirac fields as fermions, the annihilation and creation operators must satisfy:
    * $\{b_r(p), b^\dagger_s(q)\} = (2\pi)^3 \delta_{rs} \delta^3(p - q)$
    * $\{c_r(p), c^\dagger_s(q)\} = (2\pi)^3 \delta_{rs} \delta^3(p - q)$
    * All other anti-commutators must vanish (Eqs. 5.15, 5.16).
4. **Define Fermionic Vacuum:** The vacuum state $|0\rangle$ must be defined such that annihilation operators $b_s$ and $c_s$ annihilate it: $b_s|0\rangle = 0$ and $c_s|0\rangle = 0$ (Eq. 5.18).
5. **Obey Pauli Exclusion Principle:** Fermionic states must obey the Pauli Exclusion Principle (e.g., $|s,r; s,r\rangle = 0$).
6. **Normal Order Hamiltonian:** The Hamiltonian (for both bosonic and fermionic cases) is typically dealt with by normal ordering for delta function terms. Note that fermionic normal ordering implies a negative contribution $-(2\pi)^3 \delta^3(0)$.
7. **Time Ordering Definition:** In Dyson’s Formula, $\mathcal{T}$ stands for time ordering, where operators evaluated at later times are placed to the left.
8. **Wick's Theorem:** For any collection of fields $\phi_i = \phi(x_i)$, the time-ordered product is $T(\phi_1...\phi_n) = : \phi_1...\phi_n : + : \text{all possible contractions} :$. This theorem applies to fermions with the understanding that:
    * Fermionic operators must anti-commute inside a time-ordered product $T(...)$.
    * Fermionic operators must anti-commute inside a normal-ordered product $:...:$.
9. **Contraction Definition:** The contraction of a pair of fields $\phi(x)\phi(y)$ in a string of operators means replacing those operators with the Feynman propagator $\Delta_F(x-y)$.
10. **Define Feynman Propagator (Fermionic):** The fermionic Feynman propagator $S_F(x-y)$ is defined as the time-ordered product $i\langle0|T(\psi(x)\bar{\psi}(y))|0\rangle$ (Eq. 5.34), and a minus sign must be included for Lorentz invariance.
11. **Define Fermionic Contraction:** The fermionic contraction $\psi(x)\bar{\psi}(y)$ is defined as $T(\psi(x)\bar{\psi}(y)) - :\psi(x)\bar{\psi}(y): = S_F(x-y)$ (Eq. 5.36).
12. **Gauge Fixing (Lorentz Gauge Parameter):** When quantizing in Lorentz gauge, one must choose a gauge parameter (e.g., $\alpha=1$ for "Feynman gauge" or $\alpha=0$ for "Landau gauge").
13. **General Feynman Rules for Amplitudes:**
    * Draw all possible diagrams with appropriate external legs.
    * Impose 4-momentum conservation at each vertex.
    * Assign appropriate factors to vertices, internal lines, and external lines.
    * Integrate over momentum $k$ flowing through each loop ($\int \frac{d^4k}{(2\pi)^4}$).
    * Add extra minus signs for statistics (e.g., anti-commuting field operators, fermionic loops).
14. **Feynman Rules for External Lines (QED/Yukawa):**
    * **Incoming Fermion:** Associate a spinor $u^r(p)$ with momentum $p$ and spin $r$.
    * **Outgoing Fermion:** Associate a spinor $\bar{u}^r(p)$ with momentum $p$ and spin $r$.
    * **Incoming Anti-Fermion:** Associate a spinor $\bar{v}^r(p)$ with momentum $p$ and spin $r$.
    * **Outgoing Anti-Fermion:** Associate a spinor $v^r(p)$ with momentum $p$ and spin $r$.
    * **Incoming Photon:** Attach a polarization vector $\epsilon^\mu$.
    * **Outgoing Photon:** Attach a polarization vector $\epsilon^{*\mu}$.
15. **Feynman Rules for Internal Lines & Vertices (QED/Yukawa):**
    * **Scalar Propagator:** Assign $i / (p^2 - m_\phi^2 + i\epsilon)$.
    * **Fermion Propagator:** Assign $i(\slash{p} + m) / (p^2 - m^2 + i\epsilon)$ (Eq. 5.44). The $4x4$ matrix indices of the fermionic propagator must be contracted at each vertex.
    * **Photon Propagator (Lorentz Gauge):** Assign $\frac{-i\eta^{\mu\nu}}{p^2+i\epsilon}$.
    * **Scalar Yukawa Vertex:** Assign a factor of $(-ig)$ (for standard scalar Yukawa coupling $\mathcal{L}_{int} = g\phi\bar{\psi}\psi$).
    * **Pseudoscalar Yukawa Vertex:** If using $\mathcal{L}_{Yukawa} = -i\lambda \phi \bar{\psi}\gamma^5\psi$, the vertex factor is $-i\lambda\gamma^5$.
    * **QED Vertex:** Assign $-ie\gamma^\mu$.
    * **Fermionic Loops:** Each fermionic loop in a diagram must contribute an extra minus sign.
16. **Tree Diagram Property:** In tree diagrams, momentum conservation at each vertex is sufficient to determine the momentum flowing through each internal line.
17. **Symmetry Factors:** Feynman diagrams (especially in $\phi^4$ theory) sometimes require extra combinatoric factors (symmetry factors, typically 2 or 4).
18. **Green's Function Calculation:** Green's functions $G^{(n)}(x_1,...,x_n)$ must be calculated by summing over all connected Feynman graphs.
19. **Feynman Rules for Green's Functions ($\phi^4$ theory):**
    * Draw $n$ external points $x_1,...,x_n$, connected by propagators and vertices.
    * For each line $x \leftrightarrow y$, write down a factor of the Feynman propagator $\Delta_F(x-y)$.
    * For each vertex at position $y$, write down a factor of $-i\lambda \int dy$.
20. **Green's Function to S-Matrix Conversion:** To convert Green's functions $G^{(n)}(p_1,...,p_n)$ to S-matrix elements, cancel off the propagators on the external legs and place their momentum back on-shell.
21. **Green's Function Non-Zero Condition:** Only diagrams contributing to $G^{(n)}(x_1,...,x_n)$ which have propagators for each external leg yield a non-zero answer.

### Measurement, Operational Definitions & Protocols

1. **Definition of Field:** A field is a quantity defined at every point of space and time.
2. **Degrees of Freedom in QFT:** The basic degrees of freedom in quantum field theory must be operator-valued functions of space and time.
3. **Gauge Fixing Procedure:** To make progress in gauge theories, pick a representative from each gauge orbit, ensuring it is a "good" gauge that cuts the orbits.
4. **Physical States Definition (Lorentz Gauge):** Physical states $|\Psi\rangle$ in Lorentz gauge are defined by the Gupta-Bleuler condition $\partial_\mu A^{\mu(+)} |\Psi\rangle = 0$.
5. **Expectation Values for Gauge-Invariant Operators:** Expectation values of all gauge-invariant operators evaluated on physical states must be independent of the coefficients $C_n$ for timelike and longitudinal photon content.
6. **Definition of S-Matrix:** The amplitude to go from initial state $|i\rangle$ to final state $|f\rangle$ is $\lim_{t_f \to +\infty, t_i \to -\infty} \langle f| U(t_f, t_i) |i\rangle = \langle f| S |i\rangle$.
7. **Amplitude Definition:** The amplitude $A_{fi}$ is defined by stripping off the momentum-conserving delta-function from the S-matrix element: $(f|S-1|i) = i A_{fi} (2\pi)^4 \delta^{(4)}(p_f - p_i)$.
8. **Relativistic State Normalization:** Relativistically normalized states must obey $\langle i|i \rangle = (2\pi)^3 2E_i \delta^{(3)}(0) = 2E_i V$.
9. **Decay Probability per Unit Time (Width):** The decay probability per unit time $\Gamma$ (width) is given by $\Gamma = \frac{1}{2m_{initial}} \sum_{\text{final states}} \int |A_{fi}|^2 d\Pi$.
10. **Lorentz Invariant Phase Space Measure:** The density of final states $d\Pi$ is given by the Lorentz invariant measure $d\Pi = (2\pi)^4 \delta^{(4)}(P_{final} - P_{initial}) \prod_{\text{final states}} \frac{d^3p_j}{(2\pi)^3} \frac{1}{2E_j}$.
11. **Relation of Width to Half-Life:** The width $\Gamma$ of a particle is equal to the reciprocal of its half-life $\tau = 1/\Gamma$.
12. **Differential Cross Section Definition:** The differential cross section $d\sigma$ must be defined as $d\sigma = \frac{\text{Differential Probability per Unit Time}}{\text{Unit Flux}}$.
13. **Flux Definition:** The incoming flux $F$ for two particles per spatial volume $V$ is defined as $F = |\mathbf{v}_1 - \mathbf{v}_2|/V$.
14. **True Vacuum Definition:** The true vacuum of the interacting theory, $|\Omega\rangle$, must be normalized such that $\langle\Omega|\Omega\rangle = 1$.
15. **True Vacuum Dynamics:** The true vacuum of the interacting theory, $|\Omega\rangle$, must satisfy $H|\Omega\rangle = 0$.
16. **Green's Function Definition:** Correlation functions (Green's functions) are defined as $G^{(n)}(x_1, ..., x_n) = \langle\Omega|\mathcal{T} \phi_H(x_1) ... \phi_H(x_n)|\Omega\rangle$.
17. **Non-Relativistic Limit of Spinor:** The non-relativistic limit of the spinor $u(p)$ is $\sqrt{m} \begin{pmatrix} \xi \\ \xi \end{pmatrix}$.

### Assumptions, Domains of Validity & Prohibitions

1. **Fundamental Field Theory Viewpoint:** The field must be considered primary, and particles must be derived concepts appearing only after quantization.
2. **Completeness of Fields:** All fundamental laws of Nature must be described by introducing fields for each type of fundamental particle (e.g., electron fields, quark fields, neutrino fields, gluon fields, W and Z-boson fields, Higgs fields).
3. **Prohibition of Fixed Particle Number Theories:** Any attempt to write down a relativistic version of the one-particle Schrödinger equation (or for any fixed number of particles) is doomed to failure.
4. **Planck Scale Limit:** The Planck scale ($M_{pl} \sim 10^{19}$ GeV or $l_{pl} \sim 10^{-33}$ cm) is the smallest length scale that makes sense; beyond this, quantum gravity effects become important.
5. **Lagrangian Function Constraints (for Euler-Lagrange):** The Euler-Lagrange derivation assumes that the current $\mathbf{j} \to 0$ sufficiently quickly as $|\mathbf{x}| \to \infty$.
6. **Lorentz Invariance in Hamiltonian Formalism:** Although the Hamiltonian formalism is not manifestly Lorentz invariant, the derived physics must remain Lorentz invariant.
7. **Negative Norm States in QED (Lorentz Gauge):** The state $|p,0\rangle$ (timelike polarization) in Lorentz gauge has negative norm, leading to problematic negative probabilities.
8. **Gauge Equivalence of Zero-Norm States:** States in the physical Hilbert space that have zero norm (e.g., those involving timelike and longitudinal photons) must be treated as gauge equivalent to the vacuum.
9. **Validity of Current Conservation Assumption:** For the interaction $A_\mu j^\mu$, the current $j^\mu$ must be conserved ($\partial_\mu j^\mu = 0$) for consistency.
10. **Initial/Final State Assumption (S-Matrix):** Initial and final states in S-matrix calculations are assumed to be eigenstates of the free theory.
11. **S-Matrix Limitation:** The S-matrix formalism cannot cope with bound states.
12. **Fermi's Golden Rule Assumption:** Fermi's Golden Rule derivation assumes a transition to a cluster of states with a continuous density of states $\rho(E)$.
13. **Infinity in Probability:** The square of a delta-function, arising from squaring amplitudes, implies the probability for transition over infinite time. This must be handled by considering transition rates.
14. **Riemann-Lebesgue Lemma Condition:** The derivation of the true vacuum requires that the vacuum $|\Omega\rangle$ is special and separate from a continuum of states, implying the theory must have a mass gap (no massless particles).
15. **Nature of Yukawa Force:** The Yukawa potential, arising from scalar exchange, must be universally attractive.
16. **Scalar Yukawa Theory Limitation:** The scalar Yukawa theory has an unbounded potential for large enough $-\lambda \phi$, implying limitations on its range of validity.
17. **Scope of the Course (Implicit):** Only weakly coupled field theories, where perturbative techniques are applicable, are typically studied.
18. **Feynman Diagram Restriction (Connectedness):** When computing Green's functions, only connected Feynman diagrams (where every part is connected to at least one external line) must be considered.
19. **Feynman Diagram Restriction (External Loops):** Diagrams with loops on external lines must not be considered.
20. **Parity Preservation with Pseudoscalar Coupling:** If a pseudoscalar Yukawa coupling $\bar{\psi}\phi\gamma^5\psi$ is used, the scalar field $\phi$ must be a pseudoscalar to preserve parity (i.e., $P:\phi(\mathbf{x},t) = -\phi(-\mathbf{x},t)$).
21. **Spin Conservation in Non-Relativistic Limit:** When computing potentials from scattering amplitudes in the non-relativistic limit, spin must be conserved.

## Key Highlights

* The true path taken by a system corresponds to an extremal of the action, yielding the Euler-Lagrange equations of motion for fields: $\partial_\mu \left( \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi_a)} \right) = \frac{\partial \mathcal{L}}{\partial \phi_a}$.
* Adherence to the Spin-Statistics Theorem is crucial, requiring integer-spin fields to be quantized as bosons and half-integer-spin fields as fermions, to avoid fundamental inconsistencies like negative norm states or unbounded Hamiltonians.
* Noether's Theorem establishes a foundational link between symmetry and conservation laws: every continuous symmetry of the Lagrangian gives rise to a conserved current and a corresponding conserved charge.
* Gauge theories identify states related by a gauge symmetry as the same physical state, and the minimal coupling rule is the standard procedure to introduce interactions by replacing derivatives with covariant ones.
* The Locality Principle mandates that all interactions are mediated locally by fields, prohibiting Lagrangian terms that directly couple fields at distinct spatial points.
* For a physical theory, the Hamiltonian must be bounded below to prevent energy-tumble, and the Hilbert space must possess a positive definite norm, thereby prohibiting unphysical negative norm states.
* Particle number is not conserved in the combination of quantum mechanics and special relativity, which implies that a field-theoretic approach is necessary, with particles viewed as emergent excitations.
* Coupling constants with negative mass dimensions, termed 'irrelevant operators,' typically lead to non-renormalizable field theories, signifying that such theories are incomplete at higher energy scales.
* The operational core of QFT calculations involves Feynman rules, which prescribe drawing all possible diagrams, imposing momentum conservation, assigning specific factors to lines and vertices, integrating over loops, and applying statistical sign conventions.
* In Quantum Field Theory, the field is considered the primary entity, with particles being derived concepts that emerge upon quantization; theories with a fixed number of particles are inherently problematic in a relativistic context.

## Example ideas

* Develop a test suite or computational exercise to rigorously apply the enumerated Feynman rules to a non-trivial QED process (e.g., electron-positron annihilation or Compton scattering), confirming agreement with known results and explicitly verifying momentum conservation, fermionic sign rules, and Lorentz invariance at each step.
* Investigate specific examples of 'irrelevant operators' in the context of an Effective Field Theory (EFT) framework, detailing how they modify low-energy physics and how their coefficients might be constrained by experiment or higher-energy theories, addressing the 'non-renormalizable' concern.
* Perform a comparative study of different gauge-fixing approaches (e.g., Lorentz, Coulomb, and perhaps an introduction to BRST quantization) for Maxwell's equations, explicitly demonstrating how each ensures physical consistency, positive definite Hilbert spaces, and correct identification of physical states despite issues like non-dynamical A0 or negative norm states.
* Deepen the analysis of 'particle number non-conservation' and 'Compton wavelength phenomenon' by examining specific loop diagrams (e.g., vacuum polarization) where virtual particle-antiparticle pairs fundamentally alter observable quantities, thereby justifying the QFT framework over fixed-particle QM.
