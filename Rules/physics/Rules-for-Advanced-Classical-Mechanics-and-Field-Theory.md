# Rules for Advanced Classical Mechanics and Field Theory

**Coverage:** Chapters 1, 4, 5, 6, 8, 9, 10, 13 (typical for an advanced classical mechanics textbook like Goldstein).
**Notes:** Einstein summation convention assumed unless otherwise specified. Greek indices (e.g., $\mu, \nu$) typically range from 0 to 3 for 4-coordinates (spacetime); Roman indices (e.g., $i, j, k$) typically range from 1 to 3 for spatial coordinates. Metric signature for spacetime is generally (+,-,-,-).

**Generated on:** September 30, 2025 at 6:30 PM CDT

---

## Variational Principles & Equations of Motion

* **Derive Euler-Lagrange Field Equations:** For a continuous system, equations of motion must be derived from Hamilton's principle by varying the action integral $I = \int_{t_1}^{t_2} \int_{x_1}^{x_2} \mathcal{L} dx dt$, leading to the Euler-Lagrange equation: $\frac{\partial \mathcal{L}}{\partial \eta} - \frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{\eta}} \right) - \frac{d}{dx} \left( \frac{\partial \mathcal{L}}{\partial \eta'} \right) = 0$ (for 1D, single field) or the general form $\frac{\partial \mathcal{L}}{\partial \eta_\rho} - \frac{\partial}{\partial x^\nu} \left( \frac{\partial \mathcal{L}}{\partial \eta_{\rho,\nu}} \right) = 0$ (for field $\eta_\rho$ depending on 4-coordinates $x^\nu$).
* **Generalized Equation of Motion (Hamiltonian Mechanics):** The total time derivative of an arbitrary function $u(q, p, t)$ in Hamiltonian mechanics must be $\frac{du}{dt} = [u, H] + \frac{\partial u}{\partial t}$ (Eq. 9.94).
* **Hamilton's Equations via Poisson Brackets:** Hamilton's equations are expressed as $\dot{\eta} = [\eta, H]$ (Eq. 9.95b), equivalent to $\dot{\eta} = J \frac{\partial H}{\partial \eta}$ (Eq. 9.96, 8.31).
* **Hamiltonian as Trajectory Generator:** When the generator of an infinitesimal canonical transformation (ICT) is the Hamiltonian, the curve on which the system point moves is the trajectory of the system in phase space.
* **Equations of Motion for Angle Variables:** For action-angle variables, equations of motion for angle variables $w_i$ are $\dot{w_i} = \nu_i(J_1, ..., J_n) = \frac{\partial H}{\partial J_i}$ (Eq. 10.105), with solutions $w_i = \nu_i t + \beta_i$.
* **Mean Frequency (Vinti's Theorem):** For a multiply periodic system where a separable coordinate $q_k$ undergoes $m_k$ cycles in a time $T$, the mean frequency $\nu_k$ must be $\lim_{T \to \infty} \frac{m_k}{T} = \nu_k$ (Eq. 10.119).
* **Convert Second-Order to First-Order Equations:** A set of second-order nonlinear differential equations can be reduced to a larger system of first-order nonlinear differential equations (e.g., Hamilton's equations from Lagrange's equations).
* **Euler's Equations of Motion (General Form):** The Newtonian equation of motion relative to body axes must be $(dL/dt)_b + \omega \times L = N$ (Euler's Equation, Eq. 5.37), where $(dL/dt)_s = (dL/dt)_b + \omega \times L$ (Transformation Rule, Eq. 4.82, 5.36).
* **Euler's Equations for Principal Axes:** For principal axes, Euler's equations (no summation on $i$) must be $I_i \frac{d\omega_i}{dt} + \epsilon_{ijk} \omega_j \omega_k I_k = N_i$ (Eq. 5.39). For a rigid body with one fixed point and principal axes, these are:
  * $I_1 \frac{d\omega_1}{dt} - \omega_2 \omega_3 (I_2 - I_3) = N_1$
  * $I_2 \frac{d\omega_2}{dt} - \omega_3 \omega_1 (I_3 - I_1) = N_2$
  * $I_3 \frac{d\omega_3}{dt} - \omega_1 \omega_2 (I_1 - I_2) = N_3$ (Eq. 5.39')
* **Euler's Equations for Non-rigid Motion:** For nonrigid motion where rotating axes coincide with instantaneous principal axes, Euler's equations (5.39) must be replaced by $I_i \frac{d\omega_i}{dt} + \epsilon_{ijk} \omega_j \omega_k I_k - \sum_m \frac{dI_{im}}{dt} \omega_m = N_i$.
* **Small Oscillations Equations:** The equations of motion for small oscillations are $T_{ij} \ddot{\eta}_j + V_{ij} \eta_j = 0$ (Eq. 6.1).
* **Eigenvalue Equation for Oscillation Frequencies:** For small oscillations, the amplitude factors $a_j$ must satisfy $\sum_j (V_{ij} - \omega^2 T_{ij}) a_j = 0$ (Eq. 6.11), and the determinantal condition $det(V_{ij} - \omega^2 T_{ij}) = 0$ must be satisfied to find oscillation frequencies (Eq. 6.12). This is equivalent to $V a = \lambda T a$ (Eq. 6.12').
* **Eigenvector Normalization (Oscillations):** Eigenvectors $a_{ij}$ must satisfy $\sum_j a_{ij} (V_{ij} - \lambda_i \delta_{ij}) = 0$ and $\sum_j a_{ij}^2 = 1$ (sum on $j$, not $i$).
* **Normal Coordinate Solutions:** Normal coordinates $\xi_k$ must satisfy $\ddot{\xi}_k + \omega_k^2 \xi_k = 0$ (Eq. 6.27), with solutions $\xi_k = C_k e^{i \omega_k t}$.
* **Field Equations for Specific Lagrangians:**
  * **Klein-Gordon Equation:** For a complex scalar field with Lagrangian density $L = c^2 \phi^{,\mu} \phi^*_\mu - \mu_0^2 c^2 \phi \phi^*$, the field equations are $(\Box + \mu_0^2) \phi = 0$ and $(\Box + \mu_0^2) \phi^* = 0$ (Eqs. 13.99, 13.100).
  * **Sine-Gordon Equation:** For a real scalar field in one spatial dimension with $L = \frac{1}{2} [ (\frac{1}{c})^2 (\frac{\partial \phi}{\partial t})^2 - (\frac{\partial \phi}{\partial x})^2 - \mu_0^2 c^2 (1 - \cos \phi) ]$, the field equation must be $\frac{1}{c^2} \frac{\partial^2 \phi}{\partial t^2} - \frac{\partial^2 \phi}{\partial x^2} = \mu_0^2 c^2 \sin \phi$ (Eq. 13.110).
  * **Electromagnetic Field Equations:** For the electromagnetic field with $L = -\frac{1}{4} F^{\mu \nu} F_{\mu \nu} + \frac{1}{c} j^\mu A_\mu$, the Euler-Lagrange equations must be $\frac{\partial F^{\mu \nu}}{\partial x^\nu} = \frac{1}{c} j^\mu$ (Eq. 13.120).
* **Hamiltonian Density (Complex Scalar Field):** For the complex scalar field, the Hamiltonian density must be $\mathcal{H} = \pi \dot{\phi} + \pi^* \dot{\phi}^* - \mathcal{L}$, where conjugate momenta are $\pi = \dot{\phi}^*$ and $\pi^* = \dot{\phi}$ (Eqs. 13.102, 13.103).
* **Hamiltonian Density (Sine-Gordon Field):** For the sine-Gordon field, the Hamiltonian density must be $\mathcal{H} = \frac{1}{2} [ \pi^2 + c^2 (\frac{\partial \phi}{\partial x})^2 + \mu_0^2 c^2 (1 - \cos \phi) ]$, where $\pi = \frac{1}{c^2} \frac{\partial \phi}{\partial t}$ (Eqs. 13.112, 13.113).

### Symmetry & Conservation Laws

* **Orthogonality Condition:** For direction cosines $a_{ij}$ (or $\cos \theta_{ij}$), the orthogonality condition must hold: $\sum_l a_{il} a_{jl} = \delta_{ij}$ (Eq. 4.9, 4.15), which is equivalent to $A \tilde{A} = 1$ (Eq. 4.36) or $\tilde{A} A = 1$ (Eq. 4.37) for an orthogonal matrix $A$.
* **Determinant Invariance:** The determinant's value must be preserved under a similarity transformation: $|A'| = |A|$.
* **Eigenvalues of Orthogonal Matrices:**
  * The secular equation for real orthogonal matrices representing rigid body motion must have a root $\lambda = +1$.
  * For any non-trivial real orthogonal matrix, there must be exactly one eigenvalue of +1.
  * All eigenvalues of a real orthogonal matrix must have unit magnitude: $\lambda \lambda^* = 1$.
* **Antisymmetry of Infinitesimal Rotation Matrix:** Infinitesimal rotation matrices $\epsilon$ must be antisymmetric: $\epsilon = -\tilde{\epsilon}$.
* **Commutation Relations for Infinitesimal Rotation Generators:** Infinitesimal rotation generators $M_i$ must satisfy the commutation relations $[M_i, M_j] = \epsilon_{ijk} M_k$ (Eq. 4.80).
* **Inertia Tensor Symmetry:** The inertia tensor $I_{ij}$ must be symmetric: $I_{ij} = I_{ji}$ (Eq. 5.24), having only six independent components.
* **Decomposition of Angular Momentum and Kinetic Energy:** When the origin of the body system is the center of mass, total angular momentum (Eq. 1.28) and total kinetic energy (Eq. 1.31) must be decomposed into translational and rotational contributions.
* **Parallel Axis Theorem:** The moment of inertia $I_O$ about an arbitrary axis must be related to $I_{CM}$ about a parallel axis through the center of mass by $I_O = I_{CM} + M(R \times n)^2$ (Eq. 5.21).
* **Principal Moments of Inertia and Axes:** Principal moments of inertia are time-independent. For each principal moment of inertia, the eigenvalue equation $I_{ij} R_j = I R_i$ must be solved to find the direction of the corresponding principal axis.
* **Conservation Laws for Torque-Free Motion:** For torque-free motion of a rigid body (no net forces or torques), kinetic energy and the total angular momentum vector must be constant in time (Eq. 5.47). The direction of $L$ is fixed in space, and for a symmetrical rigid body, $\omega_3$ is a constant.
* **Constants of Motion (Lagrangian):** Generalized momenta corresponding to cyclic coordinates must be constant in time. If there is no component of torque along an axis, the components of angular momentum along that axis must be constant in time.
* **Constants of Motion (Symmetrical Top):** For a symmetrical top, $\omega_3$ must be constant in time and equal to $a$ (Eq. 5.61'). Also, $p_\psi = I_3 (\dot{\psi} + \dot{\phi} \cos \theta) = I_3 \omega_3 = I_3 a$ and $p_\phi = I_1 (\dot{\phi} \sin^2 \theta + I_3 \dot{\psi} \cos \theta) = I_1 b$ (Eqs. 5.60, 5.61) are conserved.
* **Energy Conservation:** For a conservative system, total energy $E$ must be constant in time.
* **Conservation for Normal Modes:** In the second mode of a linear molecule, outer atoms must vibrate exactly out of phase to conserve linear momentum. For symmetrical molecules, amplitudes of end atoms must be identical in magnitude, end atoms must travel in the same direction, and the center atom must revolve in the opposite direction to keep the center of mass at rest.
* **Degeneracy for Symmetrical Molecules:** For a linear molecule, the two modes of perpendicular vibration must be degenerate, and their frequencies must be equal.
* **Canonical Transformation Group Properties:** Canonical transformations must satisfy group properties: identity, inverse, closure under composition, and associativity.
* **Poisson Bracket Properties:** Poisson brackets must satisfy: antisymmetry ($[u, u] = 0$, $[u, v] = -[v, u]$), linearity ($[au + bv, w] = a[u, w] + b[v, w]$), product rule ($[uv, w] = [u, w]v + u[v, w]$), and Jacobi's Identity ($[u, [v, w]] + [v, [w, u]] + [w, [u, v]] = 0$) (Eqs. 9.75a-e).
* **Fundamental Poisson Bracket Values:** The fundamental Poisson brackets for canonical variables $(q_j, p_j)$ must satisfy: $[q_j, q_k] = 0 = [p_j, p_k]$ and $[q_j, p_k] = \delta_{jk} = -[p_j, q_k]$ (Eqs. 9.69a,b). In matrix form: $[\eta, \eta]_P = J$ (Eq. 9.70).
* **Canonical Invariance of Poisson Brackets:** All Poisson brackets are invariant under canonical transformations.
* **Criterion for Constant of Motion:** A function $u(q, p, t)$ is a constant of motion if and only if $\frac{du}{dt} = [u, H] + \frac{\partial u}{\partial t} = 0$. If $u$ does not depend explicitly on time, the condition simplifies to $[u, H] = 0$ (Eq. 9.97).
* **Poisson's Theorem:** The Poisson bracket of any two constants of the motion is also a constant of the motion.
* **Symmetry and Hamiltonian Invariance:** If a system is symmetrical under an operation, the Hamiltonian remains unaffected under the corresponding transformation.
* **System Vector Poisson Bracket Identity:** For any system vector $F$ (function only of $q,p$), $[F, L \cdot n] = n \times F$ (Eq. 9.123), or in components: $[F_i, L_j] = \epsilon_{ijk} F_k$ (Eq. 9.125).
* **Angular Momentum Poisson Bracket Relations:** The components of total canonical angular momentum $L$ satisfy: $[L, L \cdot n] = n \times L$, $[L_i, L_j] = \epsilon_{ijk} L_k$, and $[L^2, L \cdot n] = 0$ (Eqs. 9.127-129).
* **Lie Algebra Definition:** A non-commutative algebra is a Lie algebra if its elements $u_i$ satisfy the Poisson bracket properties and the condition $[u_i, u_j] = \sum_k c_{ij}^k u_k$ (Eq. 9.77).
* **Symmetry Group Definition:** Lie groups of infinitesimal canonical transformations whose generators are constants of motion are symmetry groups of the system and leave the Hamiltonian invariant.
* **Adiabatic Invariance of Action Variables:** Under sufficiently slow variation of a parameter (adiabatic change), the action variable $J$ remains constant (adiabatically invariant) to first order in the rate of change of the parameter.
* **Magnetic Moment Adiabatic Invariance:** For a charged particle in a slowly varying magnetic field, its magnetic moment $M = \frac{T_\perp}{B}$ is adiabatically invariant.
* **Stress-Energy Tensor Properties (Relativistic Field Theory):**
  * The stress-energy tensor $T^{\mu\nu}$ must be a linear, symmetric 4-tensor (Eq. 13.72).
  * $T^{\mu\nu} u_\nu$ represents the 4-momentum density in the observer's frame (Eq. 13.72).
  * $T^{\mu\nu} u_\mu u_\nu$ represents the mass-energy density in the rest frame (Eq. 13.76).
* **Stress-Energy Tensor for Perfect Fluid:** The stress-energy tensor for a perfect fluid must be $T_{ab} = (\rho + p)u_a u_b + p g_{ab}$ (Eq. 13.79). In the rest frame, $T^{00} = \rho c^2$ (Eq. 13.81) and momentum density $T^{0j} u_j = 0$ (Eq. 13.82).
* **Angular Momentum Density (Relativistic Field Theory):** The covariant angular momentum density tensor must be $M^{\mu \nu \lambda} = \frac{1}{c} (x^\mu T^{\nu \lambda} - x^\nu T^{\mu \lambda})$ (Eq. 13.91), which must be antisymmetric in $\mu$ and $\nu$. Conservation of the global quantity $M^{\mu\nu} = \int M^{\mu\nu\lambda} dS_\lambda$ requires a symmetric stress-energy tensor.
* **Noether's Theorem Conditions:** For flat 4-space, Noether's theorem applies to continuous, infinitesimal transformations if:
    1. The Lagrangian density is form-invariant: $\mathcal{L}(\phi', \phi'_{,\mu}, x') = \mathcal{L}(\phi, \phi_{,\mu}, x)$ (Eq. 13.130).
    2. The action integral is invariant: $\int_{\Omega'} \mathcal{L}(\phi', \phi'_{,\mu}, x') dx'^4 = \int_\Omega \mathcal{L}(\phi, \phi_{,\mu}, x) dx^4$ (Eq. 13.131).
* **Noether's Theorem Conclusions:** If Noether's theorem conditions hold for infinitesimal transformations $\delta x^\mu = \epsilon_r X^\mu_r$ and $\delta \phi_p = \epsilon_r Y_{pr}$, then there exist $r$ conserved quantities, each satisfying a differential conservation theorem: $\frac{\partial}{\partial x^\nu} [ (\frac{\partial \mathcal{L}}{\partial \phi_{,\nu}}) (Y_{pr} - \phi_{,\lambda} X^\lambda_r) + \mathcal{L} X^\nu_r ] = 0$ (Eq. 13.148).
  * **Stress-Energy Tensor Conservation:** If $\mathcal{L}$ does not depend explicitly on $x^\mu$, the conservation theorem $\frac{\partial T^\nu_\mu}{\partial x^\nu} = 0$ (Eq. 13.29) for the stress-energy tensor $T^\nu_\mu = (\frac{\partial \mathcal{L}}{\partial \phi_{,\nu}}) \phi_{,\mu} - \mathcal{L} \delta^\nu_\mu$ (Eq. 13.30) must hold.
  * **Conserved Current (Gauge Symmetry):** If $\mathcal{L}$ and the action integral are invariant under a gauge transformation of the first kind ($\delta x = 0$, $\delta \phi_p = c_p \phi_p$), then a conserved current $J^\nu = c_p (\frac{\partial \mathcal{L}}{\partial \phi_{,\nu}}) \phi_p$ (Eq. 13.152) exists, satisfying $\frac{\partial J^\nu}{\partial x^\nu} = 0$.
  * **Discrete System Conservation Theorems:** For a discrete system, the conservation theorem is $\frac{d}{dt} [ (\frac{\partial L}{\partial \dot{q}_k}) (Y_{kr} - \dot{q}_k X_r) + L X_r ] = 0$. This implies:
    * **Energy Conservation:** If $L$ is not an explicit function of time, the Jacobi integral (Hamiltonian) is conserved.
    * **Canonical Momentum Conservation:** If a coordinate $q_j$ is cyclic, its canonical momentum $p_j$ is conserved.

### Locality, Causality & Constraints

* **Rigid Body Definition:** A rigid body is defined as a system of mass points where the distances between all pairs of points remain constant throughout the motion.
* **Generalized Coordinates for Rigid Body:** A rigid body's configuration in space must be specified using exactly six independent generalized coordinates.
* **Degrees of Freedom (Rigid Body Construction):**
  * Three coordinates must be supplied to establish the position of one reference point.
  * If the first reference point is fixed, the second point must be specified by exactly two coordinates (constrained to a sphere).
  * If the first two reference points are determined, the third point must be specified by exactly one degree of freedom (constrained to rotate about the axis joining the other two).
* **Angular Velocity Uniformity:** The angular velocity vector $\omega$ must be assumed constant throughout a rigid body.
* **Coriolis Force:** The Coriolis force on a moving particle must be perpendicular to both the angular velocity $\omega$ and the particle's velocity $v$. It deflects projectiles to the right in the northern hemisphere and reverses in the southern, being zero at the equator. A body falling freely in the northern hemisphere must be deflected to the East.
* **Restricted Canonical Transformation:** A restricted canonical transformation is one in which time does not appear explicitly in the equations of transformation: $Q_i = Q_i(q, p)$, $P_i = P_i(q, p)$ (Eq. 9.44).
* **First-Order Term Retention for ICT:** For infinitesimal canonical transformations (ICTs), only first-order terms in the infinitesimals must be retained in all calculations.
* **Hamiltonian Appropriateness:** The Hamiltonian used in the generalized equation of motion must be appropriate to the particular set of canonical variables being used.
* **Hamiltonian Change for Time-Dependent CT:** Upon transforming to another set of variables by a time-dependent canonical transformation, one must also change to the transformed Hamiltonian $K$.
* **Jacobian Determinant for Real Canonical Transformation:** For a real canonical transformation, the Jacobian determinant $|M|$ must be $+1$ (Eq. 9.85).
* **Invertibility Condition for Generating Function:** For a generating function $F_1(q, Q)$ to exist, the partial derivative $\partial Q / \partial p$ must not vanish.
* **Integrable Hamiltonian Definition:** A Hamiltonian $H(q,p,t)$ is integrable if there exists a canonical transformation to new variables $P_i, Q_i$ in which all $Q_i$ are cyclic ($H = H(P_1, ..., P_n; t)$), such that Hamilton's equations can be readily integrated.
* **System Dimensionality for Chaos:** The minimal requirements for a system of first-order equations to exhibit chaos are that they must be nonlinear and have at least three variables.
* **Interaction Locality (Field Theory):**
  * Interactions between fields must be at a point to be consistent with special relativity.
  * Interaction between a field and a particle must be possible at a given point in spacetime.
* **Lagrangian Density Construction Constraints:**
  * Terms in the Lagrangian density $\mathcal{L}$ must be combinations of field and other quantities in such a manner as to produce a 4-scalar.
  * The Lagrangian density $\mathcal{L}$ is customarily restricted to field quantities or their first derivatives.

### PDE Type, Regularity & Well-Posedness

* **Characteristic Equation for Eigenvalues:** Require $det(A - \lambda I) = 0$ (Eq. 4.52) for non-trivial solutions to the eigenvalue problem. For principal moments of inertia, solve $det(I_{ij} - I \delta_{ij}) = 0$ (Eq. 5.31), the secular equation.
* **Hamilton-Jacobi Equation (General):** The Hamilton-Jacobi equation for Hamilton's principal function $S(q, P, t)$ is $H(q, \frac{\partial S}{\partial q}, t) + \frac{\partial S}{\partial t} = 0$ (Eq. 10.3), which is a first-order partial differential equation in $(n+1)$ variables $(q_1, ..., q_n, t)$.
* **Hamilton-Jacobi Equation (Time-Independent H):** When the Hamiltonian $H(q,p)$ does not depend explicitly on time, the Hamilton-Jacobi equation for Hamilton's characteristic function $W(q, P)$ is $H(q, \frac{\partial W}{\partial q}) = \alpha_1$ (Eq. 10.43).
* **Complete Solution for Hamilton's Principal Function:** A complete solution to the Hamilton-Jacobi equation (Eq. 10.3) for $S$ must be written as $S(q_1, ..., q_n; \alpha_1, ..., \alpha_n, t)$ (Eq. 10.5), where none of the $n$ independent constants $\alpha_i$ is solely additive.
* **Complete Solution for Hamilton's Characteristic Function:** A complete solution to the Hamilton-Jacobi equation (Eq. 10.43) for $W$ must contain $n-1$ non-trivial constants of integration $\alpha_2, ..., \alpha_n$, which, together with $\alpha_1$, form a set of $n$ independent constants.
* **Separability Condition (Hamilton-Jacobi):** A coordinate $q_j$ is separable in the Hamilton-Jacobi equation if $q_j$ and its conjugate momentum $p_j$ can be segregated in the Hamiltonian into a function $f(q_j, p_j)$ that does not contain any other variables. The equation is completely separable if all coordinates are separable.
* **Staeckel Conditions for Separability (Orthogonal Coordinates):** For orthogonal coordinate systems, the Hamilton-Jacobi equation is separable if:
    1. The Hamiltonian is conserved.
    2. The Lagrangian is no more than a quadratic function of generalized velocities, so $H = \frac{1}{2} p \cdot T^{-1} \cdot p + V(q)$.
    3. The elements $a_i$ of vector $\mathbf{a}$ in $T^{-1}$ are functions only of the corresponding coordinate $q_i$.
    4. The potential function $V(q)$ can be written as $V(q) = \sum_j \frac{V_j(q_j)}{\phi_{ji}}$.
    5. If $\phi^{-1}$ is a matrix with elements $\delta_{ij}\phi_{ij}^{-1} = \frac{1}{T_{ii}}$, and diagonal elements of both $\phi$ and $\phi^{-1}$ depend only on $q_i$.
    If these conditions are satisfied, Hamilton's characteristic function is completely separable, $W(q) = \sum_i W_i(q_i)$, with $W_i$ satisfying equations of the form $(\frac{\partial W_i}{\partial q_i})^2 = -2V_i(q_i) + 2\sum_j \gamma_j$ (Eq. 10.64).

### Boundary & Initial Conditions

* **Boundary Conditions for Hamilton's Principle (Continuous Systems):** In Hamilton's principle for continuous systems, the variation $\delta\eta$ must vanish at the temporal endpoints $t_1, t_2$ and the spatial limits $x_1, x_2$ of integration.
* **Boundary Conditions for Hamilton's Principle (Relativistic):** The variation $\delta\eta_\rho$ must vanish at the bounding surface $S$ of the 4-space region of integration.
* **Hamilton's Principle Covariant Integration:** The integration in Hamilton's principle in all Lorentz frames must be over a region in 4-space contained between two spacelike hypersurfaces and bounded by intersecting timelike surfaces.

### Constitutive Relations & Material Laws

* **Rigid Body Definition:** A rigid body is defined as a system of mass points where the distances between all pairs of points remain constant throughout the motion.
* **Continuous Elastic Rod Parameters:** For an elastic rod, the ratio $m/a$ (mass/separation) becomes the mass per unit length $\mu$, and $ka$ (spring constant * separation) becomes Young's modulus $Y$, in the continuous limit ($a \to 0$).
* **Charge and Current Density for Point Particle:** The spatial charge density $\rho$ corresponding to a particle of charge $q$ at point $s$ must be $\rho = q \delta(\mathbf{r}-\mathbf{s})$ (Eq. 13.122). The spatial current density $\mathbf{j}$ must be $\mathbf{j} = q \delta(\mathbf{r}-\mathbf{s}) \mathbf{v}(\mathbf{r})$ (Eq. 13.123).

### Units, Conventions & Signatures

* **Index Convention (Direction Cosines):** When using $\theta_{ij}$ or $a_{ij}$ for direction cosines, ensure the first index refers to the primed system and the second to the unprimed system.
* **Coordinate/Vector Transformation (Direction Cosines):** Express unit vectors in the primed system in terms of unit vectors in the unprimed system using direction cosines as coefficients (Eq. 4.3). Relate components of any vector $G$ in the primed system to its components in the unprimed system using direction cosines (Eq. 4.6).
* **Orthonormal Basis:** Ensure basis vectors in both coordinate systems are orthogonal and have unit magnitude (i.e., form an orthonormal basis).
* **Einstein Summation Convention:** Employ the Einstein summation convention: sum over all possible values of any index that appears two or more times in a term.
* **Matrix Multiplication Rules:** Apply matrix multiplication associatively: $(AB)C = A(BC)$. Ensure the number of columns of the first matrix equals the number of rows of the second matrix for matrix multiplication to be defined.
* **Orthogonal Matrix Inverse/Transpose:** Relate the elements of an orthogonal matrix's inverse to its transpose: $a^{-1}_{ij} = a_{ji}$ (Eq. 4.34). For orthogonal matrices, the reciprocal matrix is the transposed matrix: $A^{-1} = \tilde{A}$ (Eq. 4.35).
* **Vector Interpretation:** Interpret vector symbol $\mathbf{x}$ as a column or row matrix as context warrants.
* **Antisymmetric Matrix Properties:** Ensure diagonal elements of an antisymmetric matrix are zero.
* **Euler Angles Definition:** Define Euler angles as a specific sequence of three rotations: $\phi$ (counterclockwise about z), $\theta$ (counterclockwise about new x-axis, line of nodes), $\psi$ (counterclockwise about new z-axis). Calculate the complete transformation matrix $A$ for Euler angles as the product $BCD$ (Eq. 4.46). Obtain the inverse transformation matrix for Euler angles by transposing the forward transformation matrix (Eq. 4.47).
* **Cayley-Klein/Euler Parameters:** Define Cayley-Klein parameters as complex numbers with constraints $\beta = -\gamma^*$ and $\delta = \alpha^*$. Define Euler parameters as real quantities satisfying $e_0^2 + e_1^2 + e_2^2 + e_3^2 = 1$. Express the rotation matrix $A$ in terms of Euler parameters using Eq. (4.47').
* **Similarity Transformation for Diagonalization:** Construct the similarity transformation matrix for diagonalization using eigenvectors as its columns. Interpret the diagonal elements of the similarity-transformed matrix as the eigenvalues.
* **Rotation Angle from Trace:** Calculate the rotation angle $\Phi$ from $Tr(A) = 1 + 2\cos\Phi$ (Eq. 4.61).
* **Right-Hand Screw Rule:** Apply the right-hand screw rule to define the sense of rotation axes.
* **Infinitesimal Transformation Matrix:** Represent an infinitesimal transformation matrix as $1 + \epsilon$ (Eq. 4.66), and its inverse as $1 - \epsilon$ (Eq. 4.68). For counterclockwise rotations, represent $\epsilon$ using $\epsilon_{ij} = -\epsilon_{ijk} n_k d\Phi$ (Eq. 4.69').
* **Levi-Civita Symbol:** Define the Levi-Civita symbol $\epsilon_{ijk}$ as 0 if any two indices are equal, +1 for even permutations of (1,2,3), and -1 for odd permutations.
* **Cross Product Components:** Express the $i$-th component of a cross product $\mathbf{V}^* = \mathbf{D} \times \mathbf{F}$ as $V^*_i = \epsilon_{ijk} D_j F_k$ (Eq. 4.77).
* **Angular Velocity Alignment:** Align the angular velocity vector $\omega$ with the instantaneous axis of rotation.
* **Poisson Bracket Matrix Notation:** In matrix form, $[u,v]$ is written as $\frac{\partial u^T}{\partial \eta} J \frac{\partial v}{\partial \eta}$ (Eq. 9.68).
* **Lagrangian Density (Discrete/Continuous):** The Lagrangian density $\mathcal{L}$ in the continuous limit corresponds to $\mathcal{L}_i$ in the discrete system.
* **4-Coordinate Notation:** For compact notation in field theory, use $x^0 = ct, x^1=x, x^2=y, x^3=z$.
* **Derivative Notation (Field Theory):** A derivative of a field quantity $\eta_\rho$ with respect to $x^\nu$ is denoted by $\eta_{\rho,\nu}$.
* **Summation Convention (Relativistic Field Theory):** The summation convention is resumed for repeated indices (Greek for 4-coordinates, Roman for 3-spatial coordinates) in relativistic field theory.
* **Lagrangian Density as Scalar:** In relativistic field theory, the Lagrangian density $\mathcal{L}$ must be a scalar under Lorentz transformations.
* **Stress-Energy Tensor Normalization:** The multiplicative constant factor for the Lagrangian density is chosen such that $T^{00}$ (or its symmetrized form) directly represents the energy density in the field.
* **Action Variable Dimensions:** The action variable $J$ always has the dimensions of an angular momentum.
* **Angle Variable Convention:** The convention must be adhered to where $J$ has dimensions of angular momentum and $w$ is an angle, so $\dot{w} = \nu$ (frequency).
* **Complex Scalar Field Variables:** A complex field must be described by two independent parts, expressible either as real and imaginary parts, or as the complex field itself and its complex conjugate. The latter alternative uses the complex field $\phi$ and its complex conjugate $\phi^*$ as independent field variables.
* **Covariant Description of Integral Quantities:** The appropriate covariant description of integral quantities such as 4-momentum $P^\mu$ must be $P^\mu = \frac{1}{c} \int_S T^{\mu \nu} dS_\nu$ (Eq. 13.86), where $S$ is a region on a spacelike hypersurface. This reduces to a volume integral only if $T^{\mu\nu}$ is divergenceless.
* **Spacelike Surface Definition:** A spacelike surface is one in which all 4-vectors lying in it are spacelike. Vectors normal to a spacelike surface must be timelike. A surface at constant time is a specific example. The spacelike or timelike quality of a vector is unaffected by the Lorentz transformation.
* **Covariant Time Integration:** An integration over time $t$ at a fixed point must be described covariantly as an integration over a timelike surface.
* **Non-Covariant Fixed Volume Integration:** Spatial integration over a fixed volume $V$ for fixed time $t$ is not a covariant concept. Spatial integration must be conducted over a spacelike hypersurface of three dimensions.

### Numerical Methods & Discretization Assumptions

* **Eigenvector Component Ratios:** When solving homogeneous equations for eigenvector components, only ratios of components, not definite values, are obtained.
* **Continuous Body Approximation:** For continuous bodies, replace mass summations in inertia tensor definitions with volume integrations of mass density (Eq. 5.8).

### Measurement, Operational Definitions & Protocols

* **Rigid Body Coordinates:** Supply three coordinates to establish the position of one reference point.
* **Direction Cosines Indexing:** Define $\theta_{ij}$ or $a_{ij}$ for direction cosines such that the first index refers to the primed system and the second index refers to the unprimed system.
* **Orthogonal Transformation:** Define an orthogonal transformation as a linear transformation satisfying $a_{ij} a_{ik} = \delta_{jk}$ (Eq. 4.15).
* **Symmetric Matrix:** Define a symmetric matrix as one where $A_{ij} = A_{ji}$ (Eq. 4.38).
* **Antisymmetric Matrix:** Define an antisymmetric (or skew symmetric) matrix as one where $A_{ij} = -A_{ji}$ (Eq. 4.39).
* **Similarity Transformation:** Define a similarity transformation as $A' = BAB^{-1}$ (Eq. 4.41).
* **Eigenvalue Problem:** Define the eigenvalue problem as finding vectors $R$ that satisfy $AR = \lambda R$ (Eq. 4.49), where $\lambda$ are the eigenvalues of the matrix $A$.
* **Infinitesimal Rotation Parameters:** Identify $d\Omega_1, d\Omega_2, d\Omega_3$ as the three independent parameters specifying an infinitesimal rotation.
* **Instantaneous Angular Velocity:** Define instantaneous angular velocity $\omega$ such that $\omega dt = d\Omega$ (Eq. 4.83).
* **Effective Force in Rotating Frame:** Define the effective force $F_{eff}$ in a rotating frame as $F - 2m(\omega \times v_r) - m\omega \times (\omega \times r)$ (Eq. 4.91).
* **Moment of Inertia Coefficients:** Define moment of inertia coefficients $I_{xx}$ as $\sum_i m_i (r_i^2 - x_i^2)$ (Eq. 5.6).
* **Products of Inertia:** Define products of inertia $I_{xy}$ as $-\sum_i m_i x_i y_i$ (Eq. 5.7).
* **Rotational Kinetic Energy:** Define the rotational kinetic energy $T_{rotation}$ as $\frac{1}{2} \omega_\alpha I_{\alpha\beta} \omega_\beta$ (Eq. 5.22).
* **Moment of Inertia (about an axis):** Define the moment of inertia $I$ about an axis of rotation $n$ as $n \cdot I \cdot n$ or $\sum_i m_i (\mathbf{r}_i \times \mathbf{n}) \cdot (\mathbf{r}_i \times \mathbf{n})$ (Eqs. 5.18, 5.19).
* **Moment of Inertia Tensor:** Define the moment of inertia tensor $I_{\alpha\beta}$ as $\sum_i m_i (\delta_{\alpha\beta} r_i^2 - r_{i\alpha} r_{i\beta})$ (Eq. 5.22).
* **Nth-Rank Cartesian Tensor:** Define an Nth-rank Cartesian tensor $T$ by its $3^N$ components $T_{ijk...}$ transforming as $T'_{i'j'k'...} = a_{i'i} a_{j'j} a_{k'k} ... T_{ijk...}$ under orthogonal transformations (Eq. 5.10).
* **Unit Tensor:** Define the components of a unit tensor 1 as $1_{ij} = \delta_{ij}$ (Eq. 5.15).
* **Tensor Dot Products:** Define the right dot product of a tensor $T$ with a vector $C$ as a vector $D$ with components $D_i = T_{ij} C_j$. Define the left dot product of a vector $F$ with a tensor $T$ as a vector $E$ with components $E_j = F_i T_{ij}$.
* **Scalar from Double Dot Product:** Construct a scalar $S$ from a double dot product $F \cdot T \cdot C$ as $S = F_i T_{ij} C_j$.

### Assumptions, Domains of Validity & Prohibitions

* **Orthogonal Matrix Determinant:** Orthogonal matrices with a determinant of -1 must not represent a physical displacement of a rigid body. Transformations representing rigid body motion must be restricted to matrices having a determinant of +1.
* **Euler Angle Restriction:** When defining Euler angles, no two successive rotations must be about the same axis.
* **Sign of Square Root (Euler Angles):** The sign of the square root when calculating $\cos(\Phi/2)$ must be fixed by the physical requirement that $\Phi \to 0$ as $\phi, \psi, \theta \to 0$.
* **Finite Rotation Representation:** Finite rotations must not be represented by a single vector.
* **Infinitesimal Transformations Commutativity:** Infinitesimal transformations must be assumed to commute.
* **Axial/Polar Vector Distinction:** Axial and polar vectors must be distinguished when dealing with improper transformations (i.e., those involving inversion).
* **Principal Moments of Inertia (Non-negativity):** Principal moments of inertia must be non-negative.
* **Vanishing Principal Moment of Inertia:** If one principal moment of inertia vanishes, then all points of the body must lie along a single line.
* **Rigid Body Moment of Inertia:** The moment of inertia must be considered a function of time if the direction of angular velocity $\omega$ changes with respect to the body. When a body is constrained to rotate only about a fixed axis, its moment of inertia is a constant.
* **Restricted Hamilton-Jacobi for Conservative Systems:** The discussion on separability in Hamilton-Jacobi is restricted to conservative systems where the Hamiltonian $H$ is a constant of motion, and Hamilton's characteristic function $W$ is used exclusively.
* **Hamilton's Principal Function Limitation:** The relation $S = \int L dt + \text{constant}$ is not helpful for solving problems, as it requires knowledge of $q_i(t)$ and $p_i(t)$ beforehand.
* **Three-Body Problem Separability:** The three-body problem is an example where the Hamilton-Jacobi equation is generally not completely separable.
* **Commensurate Periods for Closed Orbits:** An orbit is closed (motion confined to a single curve) only when the various components of the motion have commensurate periods. Two frequencies $\nu_i, \nu_j$ are commensurate if $j_i \nu_i = j_j \nu_j$ for non-zero positive integers $j_i, j_j$.
* **Noncommensurate System Separability:** For a noncommensurate system, the separation of variables in the Hamilton-Jacobi equation must be unique.
* **Kepler Problem Symmetry Group Interpretation:** The symmetry groups of the Kepler problem (a non-relativistic Newtonian mechanics problem) should not be interpreted as implying physical kinship with special relativity.
* **Uncertainty in Lagrangian Density:** The Lagrangian density $\mathcal{L}$ is uncertain up to a 4-divergence term $\frac{\partial F^\nu}{\partial x^\nu}$.
* **Stress-Energy Tensor Indeterminacy:** The stress-energy tensor $T^\mu_\nu$ is indeterminate by any function whose 4-divergence vanishes.
* **Hamiltonian Formalism and Relativistic Covariance:** The Hamiltonian approach, by singling out time, is less easily incorporated into a manifestly Lorentz-covariant description of fields compared to the Lagrangian method. However, provided field quantities and derived functions have suitable transformation properties, it is consistent with special relativity.
* **Scalar Field in Klein-Gordon Equation:** The Klein-Gordon equation (Eq. 13.99) as presented (for $\phi$ and $\phi^*$) represents the relativistic analog of the Schrödinger equation for a charged zero-spin particle of rest mass energy $\mu_0 c^2$.
* **Perturbation Theory Limitation:** Even if the change in the Hamiltonian is small, the eventual effect of the perturbation on the motion can be large, requiring careful analysis of perturbation solutions.
* **First-Order Perturbation Approximation:** In time-dependent perturbation theory, a first-order approximation to the time variation of canonical variables $(\alpha, \beta)$ is obtained by replacing them with their constant unperturbed values on the right-hand side of their equations of motion.
* **Relativistic Precession Parameter:** In the application of perturbation theory to relativistic effects, the constant $h$ in the perturbation potential is not functionally dependent on the canonical momentum $L$.
* **Time-Independent Perturbation Theory Degeneracy Issue:** In time-independent perturbation theory, if the unperturbed system is degenerate (or if frequencies are near resonance, causing "small divisors"), the Fourier series for the generating function $Y_i$ (and thus the motion) may be only semi-convergent.
* **Adiabatic Change Condition:** For adiabatic invariance, a parameter must be varied slowly, such that there is little change during one period of oscillation.
* **D'Alembert Characteristic:** For perturbation Hamiltonians with the D'Alembert characteristic, the Fourier coefficients $C_j$ fall rapidly with increasing indices $j$ (generally exponentially), allowing perturbation expansions to converge even near resonance if frequencies are incommensurate.
* **Shallow vs. Deep Resonance:** Resonance is "shallow" if $C_j / (j \cdot \nu_0)$ is less than $O(\epsilon^{1/2})$ and "deep" otherwise, requiring different perturbation methods.
* **Free Field Lagrangian:** If a Lagrangian density describes a free field, it must not contain $x^\mu$ explicitly.
* **Klein-Gordon Dispersion Relation:** The dispersion relation for the Klein-Gordon equation, $\omega^2 = c^2 k^2 + \mu_0^2 c^4$, is nonlinear, becoming linear only when $\mu_0 \to 0$.
* **Sine-Gordon Equation Properties:** The sine-Gordon equation is nonlinear, with a nonlinear amplitude-dependent dispersion relation.
* **Soliton Description:** The presence of an infinite set of conserved quantities is a necessary condition for a field to describe solitons.
* **Noether's Converse:** The converse of Noether's theorem is not true; there can be conservation conditions that do not correspond to any symmetry property identifiable by the theorem.
* **Lagrangian for Complete Particle-Field System:** A single Lagrangian can be formed for a complete system of particle and field such that it implies the field equations (when considered as a function of field variables) and the particle equations of motion (when considered as a function of particle coordinates).

## Key Highlights

* Equations of motion for continuous systems and fields are derived from Hamilton's principle by varying the action integral, which leads to the generalized Euler-Lagrange field equations.
* In Hamiltonian mechanics, the total time derivative of any function is given by its Poisson bracket with the Hamiltonian plus its explicit time derivative, and the Hamiltonian itself generates infinitesimal canonical transformations.
* Noether's theorem fundamentally connects continuous symmetries of the action integral to conserved quantities, such as the stress-energy tensor or conserved currents.
* A function is a constant of motion if and only if its total time derivative vanishes, meaning its Poisson bracket with the Hamiltonian plus its explicit time derivative equals zero.
* For rigid bodies, Euler's equations describe rotational motion under torques, and in torque-free motion, kinetic energy and total angular momentum are conserved.
* The natural frequencies of small oscillations are determined by solving an eigenvalue problem represented by the determinantal condition $det(V_{ij} - \omega^2 T_{ij}) = 0$.
* The Hamilton-Jacobi equation is a first-order partial differential equation that, when solved, provides a complete description of system dynamics, particularly useful when the Hamiltonian is separable.
* In relativistic field theory, the Lagrangian density must be a Lorentz scalar, and interactions between fields must be local (at a point) to be consistent with special relativity.
* Action variables are adiabatically invariant, remaining constant to first order when system parameters change sufficiently slowly over a period of oscillation.
* The minimal requirements for a system of first-order equations to exhibit chaos are that they must be nonlinear and involve at least three variables.

## Next Steps & Suggestions

* Develop a computational framework for the symbolic derivation and numerical solution of equations of motion (e.g., Euler-Lagrange, Hamilton's, rigid body dynamics, Klein-Gordon) given a system's Lagrangian or Hamiltonian.
* Investigate the onset and characteristics of chaotic behavior in nonlinear Hamiltonian systems with three or more degrees of freedom, specifically probing the limitations of perturbation theory near resonances.
* Apply Noether's theorem to identify conserved currents for novel relativistic field theories, ensuring constructed Lagrangian densities and resulting field equations respect locality, causality, and Lorentz covariance.
* Conduct numerical simulations to quantify the 'slowness' criterion for adiabatic invariance of action variables in systems with slowly varying parameters, evaluating the accuracy of the invariance under different rates of change.
* Design a software module for automated identification of symmetries and corresponding constants of motion (e.g., cyclic momenta, Poisson bracket invariants) for arbitrary classical or field theory Lagrangians/Hamiltonians.
