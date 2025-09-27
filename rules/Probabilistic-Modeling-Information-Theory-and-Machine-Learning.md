# Rules Distilled from Probabilistic Modeling, Information Theory, and Machine Learning Systems

**Generated on:** September 26, 2025 at 1:14 AM CDT

---

## Generated Summary

---

## I. General Principles & Document Process

*   Chapters on advanced or optional topics must be placed towards the end of Parts I, II, IV, and V.
*   All chapters of Part III are optional on a first reading, except possibly Chapter 16 (Message Passing).
*   The final sections within a chapter often deal with advanced topics that can be skipped on a first reading.
*   For Chapters 4 and 10, the first-time reader should detour at section 4.5 and section 10.4, respectively.
*   Inference (and data compression) requires making assumptions.
*   Once assumptions are made, Bayesian inferences are objective, unique, and reproducible by anyone with the same information and assumptions.
*   Predictions must account for uncertainty regarding assumptions by using the sum rule: P(t|D,I) = ΣH P(t|D,H,I)P(H|D,I).
*   When performing model comparison, assign values to the prior probabilities P(H).
*   The evidence for a model is typically the normalizing constant of an earlier Bayesian inference.
*   Always write down the probability of everything.
*   The overall goal of channel coding is to make the noisy channel behave like a noiseless channel.
*   The task of decision theory is to select the action `a` that maximizes `E[U|a] = ∫ dx U(x, a)P(x|a)`.
*   Priors should describe assumptions, not enforce prior equivalence to prevent causal inference.
*   Message length `L(x)` in bits must be defined as `-log_2 P(x)`.
*   Models that minimize message length in bits (MDL principle) are preferred.
*   When performing model comparison under the MDL principle, proper priors must be used; otherwise the evidences and Occam factors are meaningless.
*   In ordinary coding theory and information theory, transmitter time `t` and receiver time `u` are assumed to be perfectly synchronized.

## II. Mathematical & Notation Standards

### General Notation
*   "iff" must be interpreted as "if and only if".
*   Natural logarithms (logₑ) must be denoted by 'ln'.
*   Logarithms to base 2 (log₂) must be denoted by 'log'.
*   logb(x) must be calculated as logk(x) / logk(b).
*   When referring to the size of a set Ax, use |Ax|.
*   When referring to the absolute value of a number z, use |z|.
*   The word 'bit' is used both as a unit of information and to denote a binary variable (0 or 1); context must clarify the meaning.
*   The notation ⌈N/2⌉ denotes the smallest integer greater than or equal to N/2.
*   The notation Λ denotes the null string.
*   The notation 0̃ denotes the end of transmission/file in specific coding contexts.
*   x ∈ [1,2) means that x ≥ 1 and x < 2.
*   x ∈ (1,2] means that x > 1 and x ≤ 2.

### Probability Notation
*   P(x=aᵢ) may be abbreviated as P(aᵢ) or P(x).
*   Commas are optional when writing ordered pairs of variables (e.g., xy ≡ x,y).
*   The pronunciation of P(x=aᵢ | y=bⱼ) is "the probability that x equals aᵢ, given y equals bⱼ".
*   The degree of belief in a proposition x must be denoted by B(x).
*   The negation of x (NOT-x) must be written as x̄.
*   The degree of belief in a conditional proposition "x, assuming proposition y to be true" must be represented by B(x|y).

### Probability Density Notation
*   P() can denote probability densities over continuous variables, as well as probabilities over discrete variables and logical propositions.
*   P(v)dv must be dimensionless.
*   P(v) is a dimensional quantity, having dimensions inverse to the dimensions of v.
*   When calculating entropy for continuous variables, it is not permissible to take the logarithm of a dimensional quantity (e.g., a probability density `P(x)`).

### Likelihood Terminology
*   Do not say "the likelihood of the data".
*   Always say "the likelihood of the parameters".
*   If referring to data, say "the likelihood of the parameters given the data".

### Entropy Notation
*   When convenient, H(X) may be written as H(p), where p is the probability vector.
*   For P(x)=0, the convention 0 × log₂(1/0) = 0 must be used in entropy calculations.
*   Expressions like I(X;Y;Z) and I(X|Y;Z) are illegal in the defined entropy system.
*   Conjunctions of arbitrary numbers of variables are permitted in each of the three spots in the expression I(X;Y|Z) (e.g., I(A,B;C,D|E,F) is valid).

### Gaussian Distribution Syntax
*   A one-dimensional Gaussian distribution is represented as `y ~ Normal(μ, σ^2)` or `P(y) = Normal(y; μ, σ^2)`.
*   The inverse-variance `η` must be `1/σ^2`.
*   For a multivariate Gaussian distribution, `μ` must be the mean of the distribution.
*   For a multivariate Gaussian distribution, `Λ` must be the inverse of the variance-covariance matrix.
*   For a multivariate Gaussian distribution, the normalizing constant `Z(Λ)` must be `(det(Λ/2π))^(1/2)`.
*   `Λ^-1` must be the inverse of the matrix `Λ`.

## III. Probability Theory & Bayesian Inference

### Ensembles
*   An ensemble X must be a triple (x, Ax, Px), where x is an outcome, Ax is a set of possible values, and Px is a set of probabilities.
*   For an ensemble, P(x=aᵢ) = pᵢ, with pᵢ ≥ 0 and Σᵢpᵢ = 1.
*   A joint ensemble XY results in an ordered pair outcome (x,y).

### Basic Probability Rules
*   The probability of a subset T of Ax is P(T) = P(x∈T) = Σax∈T P(x=a).
*   Marginal probability P(x=a) must be obtained from joint probability P(x,y) by summation: P(x=a) = Σy∈Ay P(x=a,y).
*   Marginal probability P(y) must be obtained from joint probability P(x,y) by summation: P(y) = Σx∈Ax P(x,y).
*   Conditional probability P(x=aᵢ|y=bⱼ) = P(x=aᵢ,y=bⱼ) / P(y=bⱼ) if P(y=bⱼ) ≠ 0.
*   If P(y=bⱼ) = 0, then P(x=aᵢ|y=bⱼ) is undefined.
*   Product rule: P(x,y|H) = P(x|y, H)P(y|H) = P(y|x, H)P(x|H). (Also known as the chain rule for probability).
*   Sum rule: P(x|H) = Σy P(x,y|H) = Σy P(x|y,H)P(y|H).
*   Bayes’ theorem: P(y|x,H) = [P(x|y,H)P(y|H)] / P(x|H) = [P(x|y,H)P(y|H)] / [Σy P(x|y,H)P(y|H)].
*   Independence: Two random variables X and Y are independent if and only if P(x,y) = P(x)P(y).

### Cox Axioms for Beliefs
*   Axiom 1: Degrees of belief must be orderable.
*   Axiom 2: The degree of belief in a proposition x and its negation x̄ must be related by a function f (B(x̄) = f[B(x)]).
*   Axiom 3: The degree of belief in a conjunction of propositions x,y must be related to B(x|y) and B(y) by a function g (B(x,y) = g[B(x|y), B(y)]).
*   If a set of beliefs satisfies these axioms, they can be mapped onto probabilities where P(FALSE) = 0, P(TRUE) = 1, 0 ≤ P(x) ≤ 1, P(x̄) = 1 - P(x), and P(x,y) = P(x|y)P(y).

### Likelihood Principle
*   Given a generative model P(d|θ) and an observed outcome d₀, all inferences and predictions must depend only on the function P(d₀|θ).

### Sampling Theory & Hypothesis Testing
*   A p-value is the probability of an outcome as extreme as or more extreme than observed, given a null hypothesis.
*   A p-value must not be interpreted as a Bayesian posterior probability.
*   P-values must not be used as their value depends on the stopping rule, which is extraneous to the data.
*   A confidence interval's confidence level `f` is the proportion of times it contains the true parameter value `θ` over many hypothetical repetitions of the experiment, for all true `θ`.
*   Confidence levels must not be interpreted as the probability that the true parameter lies within the interval for a specific dataset.
*   Standard tabulated χ² distributions are only accurate if expected counts `F_ij` are ≥ 5.

### Chebyshev's Inequalities
*   If t is a non-negative real random variable and a > 0, then P(t ≥ a) ≤ E[t]/a.
*   If x is a random variable and a > 0, then P((x − x̄)² ≥ a) ≤ σ²/a.
*   Weak law of large numbers: If x is the average of N i.i.d. random variables h_n with mean h and variance σh², then P((x − h)² ≥ a) ≤ σh²/(aN).

## IV. Information Theory Fundamentals

### Shannon Information Content
*   The Shannon information content of an outcome x must be defined as h(x) = log₂(1/P(x)).
*   Information content must be measured in bits.
*   For independent random variables x and y, h(x,y) = h(x) + h(y).
*   Chain rule for information content: h(x,y) = h(x) + h(y|x).

### Entropy Definition and Properties
*   The entropy of an ensemble X must be defined as H(X) = Σx P(x) log₂(1/P(x)).
*   Entropy must be measured in bits.
*   H(X) ≥ 0, with equality if and only if pᵢ = 1 for one i.
*   H(X) ≤ log₂(|Ax|), with equality if and only if pᵢ = 1/|Ax| for all i (entropy is maximized for a uniform distribution).
*   Joint entropy H(X,Y) = Σx,y P(x,y) log₂(1/P(x,y)).
*   Entropy is additive for independent random variables: H(X,Y) = H(X) + H(Y) if and only if P(x,y) = P(x)P(y).
*   Conditional entropy of X given y=bⱼ is H(X|y=bⱼ) = Σx P(x|y=bⱼ) log₂(1/P(x|y=bⱼ)).
*   Conditional entropy of X given Y is H(X|Y) = Σy P(y) Σx P(x|y) log₂(1/P(x|y)).
*   Chain rule for entropy: H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y).
*   The marginal entropy of X is H(X).
*   Entropy is decomposable for any m: H(p) = H(p₁ + ... + pm), P(m+1) + ... + P(|Ax|)] + (p₁ + ... + pm)H(p₁/(p₁ + ... + pm), ..., pm/(p₁ + ... + pm)) + (pm+1 + ... + p|Ax|)H(pm+1/(pm+1 + ... + p|Ax|), ..., p|Ax|/(pm+1 + ... + p|Ax|)).

### Relative Entropy (Kullback-Leibler Divergence)
*   Relative entropy (Kullback-Leibler divergence) between P(x) and Q(x) is DKL(P||Q) = Σx P(x) log₂(P(x)/Q(x)).
*   DKL(P||Q) ≥ 0 (Gibbs’ inequality), with equality only if P = Q.
*   DKL(P||Q) is generally not symmetric (DKL(P||Q) ≠ DKL(Q||P)).
*   Relative entropy `D_KL(Q||P)` is non-negative, and zero if and only if `Q=P`.

### Mutual Information
*   Mutual information between X and Y is I(X;Y) = H(X) − H(X|Y).
*   I(X;Y) = I(Y;X).
*   I(X;Y) ≥ 0.
*   Conditional mutual information between X and Y given z=cⱼ is I(X;Y|z=cⱼ) = H(X|z=cⱼ) − H(X|Y,z=cⱼ).
*   Conditional mutual information between X and Y given Z is I(X;Y|Z) = H(X|Z) − H(X|Y,Z).
*   Data processing inequality: I(s; ŝ) ≤ I(x; y).

### Convexity & Jensen's Inequality
*   A function f(x) is convex over (a,b) if for all x₁,x₂ ∈ (a,b) and 0 < λ < 1, f(λx₁ + (1−λ)x₂) ≤ λf(x₁) + (1−λ)f(x₂).
*   A function f is strictly convex if for all x₁≠x₂ ∈ (a,b), equality holds only for λ=0 and λ=1.
*   Similar definitions apply to concave and strictly concave functions.
*   Jensen’s inequality: If f is a convex function and x is a random variable, then E[f(x)] ≥ f(E[x]).
*   If f is strictly convex and E[f(x)] = f(E[x]), then x is a constant.
*   For a concave function, the direction of Jensen's inequality is reversed.

### Maximization with Concave Functions
*   If f(x) is concave and ∂f/∂xᵢ = 0 for all i at some point, then f(x) has its maximum value at that point.
*   If a concave f(x) is maximized at some x, it is not necessarily true that ∇f(x) = 0 there.

## V. Source Coding (Compression)

### Compressor Types
*   A lossy compressor maps some files to the same encoding.
*   For perfect recovery, a lossy compressor has a probability δ of failure (source string is one of the confusable files).
*   A lossless compressor maps all files to different encodings; if some files are shortened, others must be lengthened.

### Information Measures for Compression
*   The raw bit content of X is H₀(X) = log₂(|Ax|).
*   H₀(X) is a lower bound for binary questions guaranteed to identify an outcome.
*   H₀(X) is additive: H₀(X,Y) = H₀(X) + H₀(Y).
*   The smallest δ-sufficient subset Sδ is the smallest subset of Ax such that P(x∈Sδ) > 1−δ.
*   Sδ can be constructed by ranking elements by decreasing probability and adding them until total probability ≥ (1−δ).
*   The essential bit content of X is Hδ(X) = log₂(|Sδ|).
*   H₀(X) is the special case of Hδ(X) with δ=0 (if P(x)>0 for all x∈Ax).

### Shannon's Source Coding Theorem
*   Let X be an ensemble with entropy H. Given ϵ > 0 and 0 < δ < 1, there exists N₀ such that for N > N₀, (1/N)Hδ(Xᴺ) − H < ϵ.
*   N i.i.d. random variables with entropy H(X) can be compressed into more than NH(X) bits with negligible information loss as N → ∞.
*   Conversely, if N i.i.d. random variables are compressed into fewer than NH(X) bits, information is virtually certain to be lost.

### Typicality
*   The typical set TδN consists of x ∈ Axᴺ where |(1/N)log₂(1/P(x)) − H(X)| < δ.
*   For i.i.d. random variables Xᴺ, the probability that an outcome x falls in TδN approaches 1 as N → ∞ for any δ.
*   The number of elements in the typical set |TδN| is close to 2^(NH(X)).

### Symbol Codes
*   A (binary) symbol code C for ensemble X maps Ax to {0,1}*.
*   c(x) denotes the codeword for x, and l(x) denotes its length lᵢ = l(aᵢ).
*   The extended code C* maps A* to {0,1}* by concatenation (without punctuation): c*(x₁x₂...xN) = c(x₁)c(x₂)...c(xN).
*   Any encoded string must have a unique decoding.
*   The symbol code must be easy to decode.
*   The code must achieve as much compression as possible.
*   A code C(X) is uniquely decodeable if for all x≠y ∈ A*, c*(x) ≠ c*(y).
*   A symbol code is a prefix code if no codeword is a prefix of any other codeword.
*   Prefix codes are also known as instantaneous or self-punctuating codes.
*   A prefix code is uniquely decodeable.
*   The expected length L(C, X) = Σx∈Ax P(x)l(x) = Σᵢpᵢlᵢ.

### Kraft Inequality
*   For any uniquely decodeable code C over {0,1}, the codeword lengths {lᵢ} must satisfy Σᵢ 2⁻lᵢ ≤ 1.
*   If a uniquely decodeable code satisfies the Kraft inequality with equality, it is a complete code.
*   Given a set of codeword lengths satisfying the Kraft inequality, there exists a uniquely decodeable prefix code with those lengths.
*   Unique decodeability implies the Kraft inequality holds (McMillan).

### Optimality in Symbol Codes
*   L(C,X) is bounded below by H(X).
*   L(C,X) = H(X) only if the Kraft equality is satisfied (Σᵢ 2⁻lᵢ = 1) and lᵢ = log₂(1/pᵢ).
*   Optimal source codelengths must be lᵢ = log₂(1/pᵢ) for minimal expected length.
*   Any choice of codelengths {lᵢ} implicitly defines a probability distribution {qᵢ} where qᵢ = 2⁻lᵢ/Z (if complete, Z=1 and qᵢ = 2⁻lᵢ), for which those lᵢ would be optimal.
*   The average length exceeds entropy by DKL(p||q) if implicit probabilities q are used for true distribution p.

### Source Coding Theorem for Symbol Codes
*   For an ensemble X, there exists a prefix code C with expected length H(X) ≤ L(C,X) < H(X) + 1.
*   Codelengths lᵢ = ⌈log₂(1/pᵢ)⌉ satisfy this theorem.

### Huffman Coding Algorithm
*   To construct an optimal prefix code: Take the two least probable symbols; they will have equal longest codewords, differing only in the last digit. Combine these two symbols into a single symbol, and repeat.
*   If multiple choices exist for the two least probable symbols, any choice yields the same expected code length.
*   Huffman codes are optimal symbol codes but have an overhead of 0 to 1 bit per symbol compared to entropy.
*   Huffman codes do not handle changing ensemble probabilities elegantly.
*   Communicating the code itself (header) for adaptive Huffman coding is suboptimal due to redundancy.

### Metacodes
*   It is not possible to switch between multiple codes "for free" (i.e., without a cost to indicate the switch).
*   Indicating code choice with a leading bit makes the combined code incomplete and suboptimal (fails Kraft equality).

### Stream Codes (General)
*   Stream codes are not constrained to emit at least one bit per source symbol.
*   Arithmetic codes achieve near-optimal compression, where compressed length matches Shannon information content given the model.
*   Arithmetic codes are almost optimal (message length within 2 bits of total Shannon information content/entropy).
*   Both arithmetic and Lempel-Ziv codes fail to decode correctly if compressed file bits are altered.

### Arithmetic Coding
*   Probabilistic modeling must be clearly separated from encoding.
*   Can handle complex adaptive models and context-dependent predictive distributions.
*   The encoder uses model predictions to create a binary string; the decoder uses an identical model to interpret it.
*   The Ith symbol in the alphabet (aᵢ) can be assigned the special meaning "end of transmission".
*   A computer program must provide the encoder (and decoder) with identical predictive probability distributions P(x_n=aᵢ | x₁,...,x_n-₁).
*   A binary transmission defines an interval within the real line [0,1).
*   Intervals are defined by lower (Q_n) and upper (R_n) cumulative probabilities.
*   As the nth symbol arrives, the (n-1)th interval is subdivided at points defined by Q_n and R_n.
*   To encode a string, locate its interval and send a binary string whose interval lies within it.
*   The overhead required to terminate a message is never more than 2 bits relative to the ideal message length.
*   When transmitting multiple files, if no statistical transfer is desired, the decoder must be reset after the end-of-file character.
*   For statistical transfer between files, a new end-of-file character can instruct the models to continue.
*   Can be used with any (and time-varying) source and encoded alphabets and any probability distribution.
*   If encoding alphabet symbols (e.g., 0 and 1) require unequal frequency, subdivide the right-hand interval proportionally.
*   Generating random samples: feed ordinary random bits into an arithmetic decoder for a model; this method uses very nearly the smallest possible number of random bits.
*   Predictive distributions can be based on models like Laplace's rule: P(a|s,F) = (Fₐ+1)/(Fₐ+F_b+2) for symbols a,b.

### Lempel-Ziv Coding
*   Compression replaces a substring with a pointer to an earlier occurrence.
*   Input must be parsed into an an ordered dictionary of previously unseen substrings.
*   The empty substring Λ must be included as the first entry in the dictionary.
*   Substrings in the dictionary must be ordered by their emergence from the source.
*   Each new substring in the dictionary must be one bit longer than an earlier prefix.
*   Each substring is encoded by a pointer to its prefix and the extra bit.
*   A pointer's value is conveyed in ⌈log₂s(n)⌉ bits, where s(n) is the number of enumerated substrings.
*   The decoder must use an identical twin (dictionary construction) to decode.
*   The Lempel-Ziv algorithm is asymptotically proven to compress down to the entropy for any ergodic source.

### Codes for Integers
*   Standard binary representation e_b(n) (e.g., e_b(5)=101) is not uniquely decodeable for integers on its own.
*   e_b(n) is uniquely decodeable if the length l_b(n) is known beforehand.
*   Headless binary representation e_h(n) (e.g., e_h(5)=01, e_h(1)=Λ) is uniquely decodeable if l_b(n) is known beforehand.
*   **Self-delimiting codes**: Communicate the length l_b(n) first, then e_h(n).
*   **Codes with 'end of file' characters**: Code the integer in blocks of length b, reserving one of 2^b symbols as 'end of file'. This reserved symbol must not be used for other purposes.
*   **Unary code**: Integer n is encoded as n-1 zeros followed by a 1. Its length l_u(n) = n. It is optimal for p_n = 2⁻n distribution.
*   **Code C_λ**: c_λ(n) = c_u[l_b(n)]e_h(n). Its length l_λ(n) = 2l_b(n) − 1.
*   **Code C_λk**: c_λk(n) = c_λ[l_b(n)]e_h(n). (Iterated self-delimiting).
*   **Byte-based codes**: Encode integer in base q (e.g., 15) and use a reserved symbol (e.g., 1111) as punctuation. This works for bases of the form 2^b − 1.
*   **Elias’s universal code**: Algorithm 7.4 (right-to-left: write '0', loop: if ⌈log₂n⌉ = 0 halt, prepend e_h(n), n=⌈log₂n⌉).
*   One cannot switch between codes for integers freely; indication of the chosen code is required.
*   A code is 'universal' if it achieves an average length within some factor of the ideal for any distribution in a given class.

## VI. Channel Coding (Error Correction)

### Discrete Memoryless Channel (DMC)
*   A DMC Q is characterized by an input alphabet Ax, an output alphabet Ay, and conditional probability distributions P(y|x).
*   Transition probabilities Qᵢⱼ = P(y=bⱼ|x=aᵢ) can be written as a matrix.
*   The output probability p_y = Qp_x (right-multiplication if columns are probability vectors).
*   **Binary Symmetric Channel (BSC) with noise f**: Q = [(1-f, f), (f, 1-f)]^T.
*   **Binary Erasure Channel (BEC) with erasure f**: Q = [(1-f, f, 0), (0, f, 1-f)]^T.
*   **Z channel with noise f**: Q = [(1, 0), (f, 1-f)]^T.

### Channel Capacity
*   The capacity of a channel Q is C(Q) = max_Px I(X;Y).
*   The input distribution Px that maximizes I(X;Y) is the optimal input distribution (Px*).
*   For a BSC with noise f, C = 1 − H₂(f).
*   For a BEC with erasure f, C = 1 − f.
*   The capacity C measures the maximum amount of error-free information transmittable per unit time.
*   I(X;Y) is a concave function of the input probability vector p.
*   The input probabilities (`p_i`) must sum to `1` (`∑ p_i = 1`).
*   Individual input probabilities (`p_i`) must be greater than or equal to `0` (`p_i >= 0`).
*   Optimization routines for `I(X;Y)` must account for the inequality constraints `p_i >= 0`.
*   When maximizing `I(X;Y)`: if `p_i > 0`, then `∂I(X;Y)/∂p_i = λ`; if `p_i = 0`, then `∂I(X;Y)/∂p_i <= λ`.
*   The Lagrange multiplier `λ` is associated with the constraint `∑ p_i = 1`.
*   Any output `y` not used by an optimal input distribution must be unreachable (i.e., `Q(y|x) = 0` for all `x`).
*   All optimal input distributions for a channel have the same output probability distribution P(y).
*   I(X;Y) is a convex function of the channel parameters Q(y|x).

### Symmetric Channels
*   For a symmetric channel, the uniform distribution over inputs is an optimal input distribution.
*   For a channel to be symmetric, its outputs must be partitionable into subsets.
*   For each subset of a symmetric channel's outputs, the matrix of transition probabilities must have each row (if more than 1) as a permutation of every other row within that subset.
*   For each subset of a symmetric channel's outputs, the matrix of transition probabilities must have each column as a permutation of every other column within that subset.

### Block Codes & Decoding
*   An (N,K) block code is a list of S = 2^K codewords x^(s) ∈ Axᴺ, each of length N.
*   An (N,K) block code for channel `Q` is a list of `S = 2^K` codewords `{x^(s)}`, each of length `N`, where `x^(s) ∈ A^N`.
*   A signal `s ∈ {1,...,2^K}` must be encoded as `x^(s)`.
*   K = log₂S bits (not necessarily integer).
*   Rate R = K/N bits per channel use.
*   A decoder maps Ayᴺ to a codeword label ŝ ∈ {0,...,2^K}.
*   ŝ=0 can indicate a 'failure'.
*   Probability of block error P_B = Σs_in P(s_in) P(ŝ ≠ s_in | s_in).
*   Maximal probability of block error P_B^(max) = max_s_in P(ŝ ≠ s_in | s_in).
*   The optimal decoder minimizes P_B, decoding y as ŝ = argmax P(s|y).
*   For a uniform prior on s, the optimal decoder is the maximum likelihood decoder (argmax P(y|s)).
*   Probability of bit error p_b: average probability that a bit of ŝ differs from s (over K bits).
*   The Hamming distance between two binary vectors must be the number of coordinates in which they differ.
*   For a binary symmetric channel, the optimal decoder for a code must find the codeword closest to the received vector in Hamming distance.
*   The distance of a code (minimum distance) must be the smallest separation between any two of its codewords.
*   A code with distance `d` must be `⌊(d-1)/2⌋`-error-correcting.
*   For a linear code, all codewords must have identical distance properties.

### Shannon's Noisy-Channel Coding Theorem
*   1. Achievability: For any DMC, capacity C = max_Px I(X;Y). For any ϵ > 0 and R < C, for large enough N, there exists a code (length N, rate ≥R) and decoder such that P_B^(max) < ϵ.
*   2. Rate-Distortion Achievability: If bit error p_b is acceptable, rates R(p_b) = C / (1 − H₂(p_b)) are achievable.
*   3. Non-Achievability: For any p_b, rates R > C / (1 − H₂(p_b)) are not achievable.
*   **Proof Concepts**:
    *   Joint typicality: x,y of length N are jointly typical (to tolerance β) if x is typical of P(x), y is typical of P(y), and (x,y) is typical of P(x,y).
    *   The probability that (x,y) are jointly typical tends to 1 as N → ∞.
    *   The number of jointly typical sequences |JβN| is bounded by 2^(N(H(X,Y)+β)).
    *   If x'~XN and y'~YN are independent, P((x',y') ∈ JβN) < 2^(-N(I(X;Y)-3β)).
    *   Random coding: Generate S = 2^(NR') codewords randomly from P(x) = ΠP(x_n).
    *   Typical set decoding: Decode y as ŝ if (x^(ŝ),y) are jointly typical and no other s' yields joint typicality; otherwise, declare failure.
    *   The average probability of error (p_B) < δ + 2^(N(I(X;Y)-R'-3β)).
    *   Expurgation: A code can be modified by discarding codewords with high error probability to reduce P_B^(max).
    *   If a system achieves rate R and bit error p_b, then I(s; ŝ) ≥ NR(1−H₂(p_b)).
*   **Explicit N-Dependence**:
    *   Average error probability P_B < exp[−NE_r(R)], where E_r(R) is the random-coding exponent (convex, decreasing, positive for 0 < R < C).
    *   Maximal error probability P_B^(max) can also be exponentially small in N via expurgation.
    *   Error probability lower bound: P_B ≥ exp[−NE_sp(R)], where E_sp(R) is the sphere-packing exponent (convex, decreasing, positive for 0 < R < C).
*   **Coding Practice Limitations**:
    *   Implementing encoders/decoders for random codes with large N has exponentially high cost.
    *   Customers often don't know exact channel properties; performance charts across idealized channels are used instead.

### Practical Error-Correcting Codes
*   A practical error-correcting code must be encodable and decodable in time that scales as a polynomial function of the block length `N` (preferably linearly).
*   Practical codes must employ very large block sizes.
*   Practical codes must be based on semi-random code constructions.
*   Practical codes must make use of probability-based decoding algorithms.
*   Practical decoding algorithms for linear codes must be fast (not NP-complete).

### Linear Block Codes
*   A linear (N,K) block code's codewords `{x^(s)}` must form a K-dimensional subspace of `A^N`.
*   For a linear (N,K) block code, the encoding operation must be `t = G^T s mod 2`, where `G^T` is an `N x K` binary matrix and `s` is a vector of `K` bits.
*   Codewords `{t}` must satisfy `H t = 0 mod 2`, where `H` is the parity-check matrix.
*   If a code has a systematic generator matrix `G = [I_K | P^T]`, its parity-check matrix `H` must be `[P | I_M]`.

### Convolutional Codes
*   Convolutional codes must not divide the source stream into blocks.
*   For convolutional codes, transmitted bits must be a linear function of past source bits.
*   Generation of transmitted bits for convolutional codes typically involves feeding the present source bit into a linear feedback shift register of length `k` and transmitting one or more linear functions of the shift register's state at each iteration.

### Concatenated Codes
*   A concatenated code must consist of an outer code `C'` followed by an inner code `C`.
*   When decoding concatenated codes with individual subcode decoders, it is most sensible to first decode the code with the lowest rate (and greatest error-correcting ability).

### Interleaving & Product Codes
*   When using interleaving, after encoding a data block with the outer code, bits must be reordered within the block to separate nearby bits before feeding to the inner code.
*   A rectangular code must arrange data in a `K_s x K_l` block, encode horizontally using an `(N_l, K_l)` linear code, then vertically using an `(N_s, K_s)` linear code.

### Turbo Codes
*   A turbo code encoder must be based on the encoders of two convolutional codes.
*   For a turbo code, source bits must be fed into each convolutional encoder, with the order of source bits permuted randomly for one of the encoders.
*   For a turbo code, the resulting parity bits from each constituent code must be transmitted.
*   For a turbo code, the random permutation must be chosen when the code is designed and fixed thereafter.
*   A turbo code decoding algorithm must involve iteratively decoding each constituent code using its standard decoding algorithm.
*   A turbo code decoding algorithm must use the output of one constituent decoder as input to the other decoder.

### Low-Density Parity-Check (LDPC) Codes
*   An LDPC code must have a parity-check matrix, `H`, where every row and column is sparse.
*   For a regular Gallager code, every column of `H` must have the same weight `j`, and every row must have the same weight `k`.
*   The decoding algorithm must halt when all checks `Ĥx = z mod 2` are satisfied.
*   If the maximum number of iterations is reached without successful decoding, the block must be flagged as a failure.
*   The computational cost for decoding in GF(`q`) must scale as `q log q` if the appropriate Fourier transform is used in the check nodes.
*   If a low-density parity-check matrix has a staircase structure with `M` columns of weight 2 or less, it can be encoded in linear time.
*   The cost of staircase encoding is linear if the sparsity of `H` is exploited.
*   For fast encoding of general LDPC codes, the parity-check matrix must first be rearranged into approximate lower-triangular form by row- and column-interchanges.
*   For fast encoding, compute the upper syndrome of the source vector: `z_U = As`.
*   For fast encoding, define matrix `F = −E T⁻¹ B + D`.
*   For fast encoding, compute the inverse `F⁻¹`.

## VII. Gaussian Channels & Systems

### Gaussian Channel Properties
*   For a Gaussian channel, the conditional distribution of output `y` given input `x` must be a Gaussian distribution.
*   The average power of a continuous-time transmission `∫[z(t)]^2 dt / T` must be less than or equal to `P`.
*   Orthonormal basis functions `φ_n(t)` must satisfy `∫ φ_n(t)φ_m(t) dt = δ_nm`.
*   The scalar noise `n_n` must be Gaussian: `n_n ~ Normal(0, N_0/2)`.
*   The signal amplitudes `z_n` must satisfy `∑ z_n^2 <= P * T`.
*   Bandwidth `W` is defined as `N_max / T` where `N_max` is the maximum number of orthonormal functions in `T`.
*   If the highest frequency in a signal is `W`, the signal must be fully determined by samples separated by `Δt = 1/(2W)` seconds (Nyquist sampling theorem).
*   For equivalence with a continuous channel, a Gaussian channel's noise level `σ` must be `N_0/2`.
*   For equivalence with a continuous channel, a Gaussian channel must be subject to the signal power constraint `x^2 < P / (2W)`.
*   Rate-compensated signal-to-noise ratio `E_b/N_0` is `x^2 / (R * N_0)`.
*   `E_b/N_0` values must be reported in decibels (`10log_10 E_b/N_0`).

### Gaussian Channel Optimal Detection
*   Noise `n` in optimal pulse detection must be Gaussian.
*   `Λ` in optimal pulse detection must be the inverse of the variance-covariance matrix of the noise.
*   `Λ` must be a symmetric and positive-definite matrix.
*   To minimize the probability of error, the optimal detector must guess the most probable hypothesis.
*   If `a(y) > 0`, then the decision must be `s=1`.
*   If `a(y) < 0`, then the decision must be `s=0`.
*   If `a(y) = 0`, then the decision can be either `s=0` or `s=1`.

### Gaussian Channel Coding Constraints
*   Codes for Gaussian channels must be constrained such that their average cost `v(x)` is less than or equal to some maximum value.
*   For a Gaussian channel, the input `x`'s average power `x^2` must be constrained.
*   Capacity `C` of a continuous channel is `W log_2 (1 + P / (N_0 * W))` bits per second.

### Thresholded Channel Output
*   If a channel output `y` is thresholded: if `y > 0`, the output must be `1`; if `y < 0`, the output must be `0`.

## VIII. Algorithmic & Numerical Methods

### Sum-Product & Related Algorithms
*   The sum-product algorithm is only valid for tree-like graphs.
*   Sum-product algorithm messages are of two types: `g_n_m` (variable node `n` to factor node `m`) and `r_m_n` (factor node `m` to variable node `n`).
*   A message sent along an edge connecting factor `f_m` to variable `x_n` must be a function of `x_n`.
*   A message must only be created if all messages it depends on are present.
*   **Variable-to-Factor Message (`g_n_m`)**: `g_n_m(x_n) = Π_{m'∈M(n)\m} r_m'_n(x_n)`.
*   **Factor-to-Variable Message (`r_m_n`)**: `r_m_n(x_n) = Σ_{x_N(m)\n} [f_m(x_N(m)) Π_{n'∈N(m)\n} g_n'_m(x_n')]`.
*   **Initialization Method 1**: For all leaf variable nodes `n`, initialize `g_n_m(x_n) = 1`. For all leaf factor nodes `m`, initialize `r_m_n(x_n) = f_m(x_n)`.
*   **Initialization Method 2**: Initialize all variable-to-factor messages `g_n_m(x_n)` to `1`. Proceed by alternating factor message update rule (26.12) and variable message update rule (26.11).
*   **Leaf Node Specifics**: A node with only one edge is a leaf node. A leaf factor node `m` must always broadcast `r_m_n(x_n) = f_m(x_n)` to its single neighbor `x_n`. A leaf variable node `n` must perpetually broadcast `g_n_m(x_n) = 1` to its single neighbor `m`.
*   **Results Extraction**: Obtain the marginal function `Z_n(x_n)` by multiplying all incoming factor-to-variable messages `r_m_n(x_n)` at node `n`. Obtain the normalizing constant `Z` by summing any marginal function `Z_n(x_n)` over `x_n`. Obtain normalized marginals `P_n(x_n)` by dividing `Z_n(x_n)` by `Z`.
*   **On-the-fly Normalization**: Compute `r_m_n` using rule (26.12). Compute `g_n_m(x_n)` as `α_n_m Π_{m'∈M(n)\m} r_m'_n(x_n)`. The scalar `α_n_m` must be chosen such that `Σ_{x_n} g_n_m(x_n) = 1`.
*   **Factorization View**: The factored function `P(x)` is expressed as the product of `M` factor node functions `φ_m(x_N(m))` and `N` variable node functions `ψ_n(x_n)`. Initialize `φ_m(x_N(m))` to `f_m(x_N(m))` and `ψ_n(x_n)` to `1`. When `r_m_n(x_n)` is sent, update `ψ_n(x_n)` to `Π_{m∈M(n)} r_m_n(x_n)`. When `r_m_n(x_n)` is sent, update `φ_m(x_N(m))` to `f_m(x_N(m)) / Π_{n∈N(m)} r_m_n(x_n)`. Messages `r_m_n(x_n)` can be computed as `Σ_{x_N(m)\n} [φ_m(x_N(m)) Π_{n'∈N(m)} ψ_n'(x_n')]`. The factorization viewpoint is applicable regardless of graph tree-likeness.
*   **Min-Sum / Max-Product**: To solve the maximization problem using sum-product, replace 'add' with 'max' and 'multiply' with 'multiply'. If summation is replaced by maximization, the normalizing constant `Z` becomes `max_x P*(x)`. The max product algorithm is typically implemented in the negative log likelihood domain, replacing 'max' with 'min' and 'product' with 'sum'.
*   **Junction Tree**: The junction tree algorithm must agglomerate variables until the graph is acyclic.

### Monte Carlo Methods
*   A Metropolis method with random walk step size `ε` must run for at least `T ≈ (L/ε)²` iterations to obtain an independent sample, where `L` is the largest length scale of probable states.
*   The `T ≈ (L/ε)²` lower bound on Metropolis iterations is a minimum; actual convergence time may be longer due to distribution topology.
*   For a Markov chain to converge to `P(x)`, `P(x)` must be an invariant distribution of the chain.
*   An invariant distribution `π(x)` satisfies `π(x') = ∫ dVx T(x'; x)π(x)`.
*   For a Markov chain to converge to `π(x)`, it must be ergodic (i.e., `p(t)(x) → π(x)` for any initial `p(0)(x)`).
*   An ergodic Markov chain must have a non-reducible transition matrix.
*   An ergodic Markov chain must not have a periodic set.
*   Detailed balance property states `T(xa; xb) P(xb) = T(xb; xa) P(xa)`.
*   Invariance of `P(x)` under `T` is a necessary condition for MCMC chain convergence to `P(x)`.
*   Detailed balance is not an essential condition for MCMC chain convergence.
*   Metropolis proposal density width parameters must not be dynamically updated based on simulation history. Violation invalidates detailed balance.
*   Averaging over dependent points does not introduce bias into estimates.
*   Hamiltonian dynamics simulation must be perfectly reversible (`(x,p)→(x',p')` implies `(x',-p')→(x,-p)`) and conserve state-space volume.
*   **Importance Sampling**: Importance sampler `Q(x)` must not be small in regions where `|φ(x)P(x)|` is large, to ensure reliable estimation. An importance sampler must have heavy tails.
*   **Rejection Sampling**: For rejection sampling, a constant `c` must be known such that `cQ*(x) > P*(x)` for all `x`. In rejection sampling, if `u > P*(x)`, reject the sample; otherwise, accept it.
*   **Metropolis-Hastings**: In Metropolis-Hastings, if `α > 1`, accept the new state; otherwise, accept with probability `α`. If a Metropolis-Hastings step is accepted, `x(t+1)` must be set to `x'`. If a Metropolis-Hastings step is rejected, `x(t+1)` must be set to `x(t)`. Metropolis method parameters should be adjusted to achieve an acceptance rate of approximately 1/2 to maximize information acquired about `P`.
*   **Slice Sampling**: Slice sampling can be applied to any system where target density `P*(x)` can be evaluated at any point. Slice sampling's overall method must satisfy detailed balance. In integer slice sampling, a translation `U` must be introduced to avoid permanent sharp edges between binary integers. A single integer `X` can represent multiple real parameters in slice sampling via space-filling curves.
*   **Hamiltonian Monte Carlo**: Hamiltonian Monte Carlo involves two proposal types: (1) randomizing momentum `p` (leaving `x` unchanged), and (2) changing `x` and `p` via Hamiltonian dynamics `H(x,p) = E(x) + K(p)`. The momentum randomization proposal in HMC is always accepted. HMC rejection rule uses the change in `H(x,p)`.
*   **Overrelaxation**: An overrelaxation transition matrix with fixed update order does not satisfy detailed balance.
*   **Simulated Annealing**: Simple simulated annealing does not sample exactly from the target distribution. Skilling's multi-state leapfrog method should not be used alone; it must be combined with other Monte Carlo operators.
*   **Genetic Methods**: For a genetic algorithm to succeed, parameters `x` must be encoded to allow crossover to produce reasonably fit progeny from fit parents. To make a genetic algorithm crossover valid, accept/reject proposals using the Metropolis rule with `α = [P*(x')P*(y')] / [P*(x)P*(y)]`.

### Exact Sampling
*   In coupling from the past, when restarting from an earlier `T_0`, the same random numbers must be reused for overlapping time segments.
*   When coalescence occurs *before* time 0, `x(0)` can be recorded as an exact sample.
*   The state at the moment of coalescence is *not* a valid sample from the equilibrium distribution.
*   Propp and Wilson's Ising model method is only for 'attractive' probability distributions.
*   In the summary state exact sampling method, initialize all spins in the summary state to "?" at time `T_0`.
*   In summary state exact sampling, if all new local spin values agree, set the summary spin to that value; otherwise, set it to "?".
*   The summary state method is applicable to general spin systems with any couplings.

### Variational & Mean Field Methods
*   To approximate `P(x)` with `Q(x;θ)`, minimize the variational free energy `F(θ)` with respect to `θ`.
*   The variational free energy `F(θ)` provides an upper bound for the true free energy `F`.
*   Asynchronous updating of `α` parameters in mean field theory is guaranteed to decrease `F(α)`.
*   The approximations given by variational free energy minimization always tend to be more compact than the true distribution.
*   Variational free energy minimization is parameterization-independent.
*   For spin systems with a separable approximating distribution, mean field equations (33.26, 33.27) must be used to minimize variational free energy.
*   To obtain soft K-means exactly from the variational method, `Qθ` must be a delta function `δ(θ − θ̂)`.

## IX. Machine Learning (General)

### General Terminology
*   **Network Architecture**: Specifies variables and their topological relationships (e.g., weights, neuron activities).
*   **Activity Rule**: Defines how neuron activities change over short time scales based on weights.
*   **Learning Rule**: Specifies how network weights change over time, typically depending on neuron activities, target values, and current weights.
*   **Supervised Neural Networks**: Receive input data with corresponding target outputs.
*   **Unsupervised Neural Networks**: Receive unlabelled data examples.

### Regularization
*   A regularized objective function `M(w)` must be `G(w) + α E_W(w)`.
*   The simplest weight decay regularizer is `E_W(w) = (1/2) Σ w_i^2`.

### Learning as Inference
*   Neuron output `y(x;w)` defines `P(t=1|x,w)`.
*   Error function `G` is `-log likelihood`, i.e., `P(D|w) = exp[-G(w)]`.
*   Regularizer `E_W` is `-log prior`, i.e., `P(w|α) = (1/Z_W(α)) exp(-αE_W(w))`.
*   If `E_W` is quadratic, the prior is Gaussian with `σ_W^2 = 1/α`.
*   Objective function `M(w)` is `-log P(w|D,α)`, i.e., `P(w|D,α) ∝ exp(-M(w))`.
*   Bayesian prediction of a new datum `t*` must involve marginalizing over uncertain parameters.
*   Predictive probability `P(t*|x*,D,α)` must be calculated by integrating `P(t*|x*,w,α)P(w|D,α)` over `w`.

## X. Neural Networks (Specific Architectures)

### Single Neuron & Perceptron
*   A single neuron has `I` inputs `x_i` and one output `y`.
*   Each input `x_i` is associated with a weight `w_i`.
*   A neuron may include a bias `w_0`, equivalent to a weight for a constant input `x_0 = 1`.
*   A single neuron is a feedforward device; connections are directed from inputs to output.
*   **Activity Rules**:
    *   Neuron activation `a` must be computed as `Σ w_i x_i`.
    *   Neuron output `y` must be `f(a)`.
    *   **Linear activation**: `y(a) = a`.
    *   **Sigmoid (logistic) activation**: `y(a) = 1 / (1 + e^-a)`.
    *   **Sigmoid (tanh) activation**: `y(a) = tanh(a)`.
    *   **Threshold activation**: `y(a) = 1` if `a > 0`, else `0`.
    *   **Heat bath stochastic activation**: sets `y(a)=+1` with `1/(1+e^-2a)` probability, else `-1`.
    *   **Metropolis stochastic activation**: computes `A=ay`, flips `y` if `A<0`, else flips with probability `e^-A`.
*   **Training**:
    *   Binary classification error function `G(w)` must be calculated as `G(w) = -Σ [(t(n) ln y(x(n); w) + (1 - t(n)) ln(1 - y(x(n); w))]`.
    *   The gradient of `G(w)` with respect to `w_j` must be `g_j = -Σ (t(n) - y(x(n); w)) x_j(n)`.
    *   Neuron weights `w_i` must be adjusted by `Δw_i = η(t - y)x_i`.
    *   The activity and learning rules must be repeated for each input/target pair.
*   **Capacity**:
    *   Points are in general position if any subset of size `≤ K` is linearly independent.
    *   A linear threshold function output `y` is 1 if `a > 0`, else 0, where `a = Σ w_k x_k`.
    *   The VC dimension of a K-dimensional binary threshold function is `K`.
    *   A single neuron can memorize up to `N=2K` random binary labels but will likely fail for more.

### Hopfield Networks
*   **Architecture**: A Hopfield network must consist of `I` neurons. Hopfield network neurons must be fully connected.
*   **Connections**: Hopfield network connections must be symmetric (`wᵢⱼ = wⱼᵢ`). Hopfield networks must have no self-connections (`wᵢᵢ = 0`). The convention for weights is that `wᵢⱼ` denotes the connection from neuron `j` to neuron `i`.
*   **Activity Output**: The activity (output) of neuron `i` must be denoted by `zᵢ`.
*   **Learning Rule**: The learning rule for a Hopfield network must aim to make a set of desired memories `{x^(n)}` stable states of the network's activity rule. Hebbian learning increases weights between positively correlated neuron activities.
*   **Convergence General**: Systems with a Lyapunov function must converge to a fixed point or limit cycle; chaotic behavior is impossible. Asynchronous continuous Hopfield networks have a Lyapunov function. Hopfield network convergence to a fixed point requires symmetric connections and asynchronous updates. If a feedback network does not have symmetric connections, its dynamics may fail to converge to a fixed point.
*   **Binary Hopfield Network**:
    *   **Memory Pattern Type**: Each memory in a binary Hopfield network must be a binary pattern.
    *   **Memory Value Range**: For binary memory patterns, `zᵢ` must be an element of {-1, 1}.
    *   **Activity Rule**: Each neuron must update its state using the threshold activation function: `z(a) = 1` if `a > 0`, else `-1` (or `0`).
    *   **Biases**: Biases `b₀` may be included; they can be viewed as weights from a neuron 0 whose activity `z₀` is permanently 1.
    *   **Weight Setting (Hebbian Rule)**: Weights `wᵢⱼ` must be set using the sum of outer products (Hebbian rule): `wᵢⱼ = Σₙ (xᵢ^(n) xⱼ^(n))`.
    *   **Weight Scaling (Optional)**: To prevent the largest possible weight from growing with `N`, the constant `η` in the Hebbian rule may be set to `1/N`.
    *   **Update Order**: The order for updates to occur must be specified (synchronous or asynchronous).
    *   **Synchronous Update Process**: All neurons must compute their activations `aᵢ = Σⱼ wᵢⱼ zⱼ`. All neurons must then update their states simultaneously to `zᵢ = Θ(aᵢ)`.
    *   **Asynchronous Update Process**: One neuron at a time computes its activation and updates its state. The sequence of selected neurons may be fixed or random.
    *   **Convergence**: If a binary Hopfield network is updated synchronously, it may fail to converge to a fixed point.
*   **Continuous Hopfield Network**:
    *   **Activity Value Range**: The activities of a continuous Hopfield network must be real numbers between -1 and 1.
    *   **Activity Rule**: Each neuron must update its state using a sigmoid activation function. The activity rule must involve the equations: `aᵢ = Σⱼ wᵢⱼ zⱼ` and `zᵢ = tanh(aᵢ)`.
    *   **Gain (Optional)**: A gain `β ∈ (0, ∞)` may be introduced into the activation function: `zᵢ = tanh(βaᵢ)`.
    *   **Learning Rule**: The learning rule is the same as in the binary Hopfield network.
    *   **Convergence**: The continuous Hopfield network's dynamics will always converge to a stable fixed point if implemented asynchronously and its connections are symmetric.
    *   **Convergence Prerequisite (Symmetry)**: The Hopfield network's connections must be symmetric for the convergence proof to hold.
    *   **Convergence Prerequisite (Asynchronous Updates)**: Updates must be made asynchronously for the convergence proof to hold.
*   **Hopfield Networks for Optimization Problems**:
    *   **Energy Function Definition**: When solving constraint satisfaction problems, the weights of a Hopfield network must define an energy function that is minimized only when the network's state represents a valid solution.
    *   **Valid Tour State (TSP Example)**: For the Travelling Salesman Problem (TSP), a valid state must resemble a permutation matrix (exactly one '1' in every row and one '1' in every column).
    *   **Enforcing Validity (TSP Example)**: Large negative weights must be used between any pair of neurons in the same row or same column to enforce tour validity. A positive bias for all neurons must be set to ensure `K` neurons turn on (for `K` cities in TSP).
    *   **Encoding Objective Function (TSP Example)**: Weights must encode the objective function (e.g., total distance) to be minimized. Negative weights proportional to appropriate distances between nodes in adjacent columns must be used (e.g., `−dᵦᵧ` between B and D nodes in adjacent columns).
    *   **Continuous Hopfield Network in TSP**: The dynamics of a continuous Hopfield network for TSP must be confined to a 'valid subspace' (as shown by Aiyer, 1991) to prevent interference with solution validity.
    *   **Deterministic Annealing for TSP**: The deterministic annealing approach for TSP requires gradually increasing the gain `β` of the neurons from 0 to ∞.
*   **Optimizing Hopfield Network Weights**: Ensure self-weights `wᵢᵢ` are zero. Ensure the weight matrix is symmetrical (`wᵢⱼ = wⱼᵢ`).

### Boltzmann Machines
*   **Weight Symmetry**: `W` is defined to be symmetric with `wᵢⱼ = wⱼᵢ`.
*   **Activity Rule**: After computing the activation `aᵢ`, set `xᵢ = +1` with probability `P(xᵢ=+1|aᵢ)` (equation 43.3) else set `xᵢ = -1`.
*   **Probability for +1**: `P(xᵢ=+1|aᵢ)` must be `1 / (1 + exp(-2aᵢ))`.

### Multilayer Perceptrons (Supervised Learning)
*   **Error Function (Regression)**: For regression, the error function `E_D(w)` must be `1/2 Σₙ (t^(n) - y(x^(n); w))²`.
*   **Regularization (Regression)**: When regularization is included, the objective function `M(w)` must be `βE_D + αE_w`. `E_w` may be `1/2 Σᵢ wᵢ²`.
*   **Output (Binary Classification)**: For binary classification with targets (0,1), the network output `y(x; w, A)` must be bounded between 0 and 1. The output `y` must be interpreted as `P(t=1|x, w, A)`.
*   **Negative Log Likelihood (Binary Classification)**: The negative log likelihood `G(w)` must be `−Σₙ [t^(n) lny(x^(n); w) + (1 - t^(n))ln(1 - y(x^(n); w))]`.
*   **Total Objective (Binary Classification)**: The total objective function must be `M = G + αE_w`.
*   **Output (Multi-class Classification)**: For multi-class classification, outputs `yᵢ` must be coupled and sum to one. Coupled outputs `yᵢ` must be interpreted as class probabilities `P(tᵢ=1|x, w, A)`.
*   **Softmax (Multi-class Classification)**: The last part of equation (44.2) must be replaced by the softmax function: `exp(aᵢ) / Σⱼ exp(aⱼ)`.
*   **Negative Log Likelihood (Multi-class Classification)**: The negative log likelihood `G(w)` must be `−Σₙ Σᵢ tᵢ^(n) lnyᵢ(x^(n); w)`.
*   **Total Objective (Multi-class Classification)**: The total objective function must be `M(w) = G + αE_w`.

### Gaussian Processes
*   **Covariance Function Validity**: A chosen covariance function `C(x,x')` must generate a non-negative-definite covariance matrix for any set of points `{x^(n)}`.
*   **Prior Properness**: For the prior in equation (45.12) to be proper, `A` must be a positive definite operator.

### Langevin Monte Carlo (Neural Networks)
*   The Langevin method is gradient descent with added noise.
*   In Langevin method, a noise vector `p` must be generated from a unit variance Gaussian.
*   In Langevin method, `Δw` must be `-η g + ε p`.

### Ising Models
*   **Gibbs Sampling**: In Gibbs sampling for Ising models, the probability `P(+1|b_n)` must be computed as `1 / (1 + exp(-2βb_n))`. `β = 1/k_B T` and local field `b_n = Σ J_mn x_m + H`. The factor of 2 in (31.17) is due to spin states being `{+1, -1}`.
*   **Metropolis Algorithm**: In Metropolis algorithm for Ising models, the energy change `ΔE` from flipping spin `x_n` is `2x_n b_n`. In Metropolis algorithm for Ising models, accept `ΔE < 0` with probability 1, otherwise accept with probability `exp(-βΔE)`.
*   **Properties & Constraints**: For finite rectangular Ising models with periodic boundary conditions, if the grid size is odd, the checkerboard symmetry relating `J=+1` and `J=-1` is broken. For an infinite-length thin strip Ising model, only the largest eigenvalue is needed to find thermodynamic properties. If the transfer matrix is all positive, its principal eigenvector is also all positive (Frobenius Perron theorem). For iterative eigenvalue computation with a positive matrix, a reasonable initial vector is `(1,1,...,1)`.

## XI. Specialized Systems & Algorithms

### Independent Component Analysis (ICA)
*   ICA derivation assumes the observable vector `x` is generated without noise.
*   The simplest ICA algorithm assumes `I = J` (number of sources equals number of observations).
*   For ICA, source variables must be non-Gaussian to recover the mixing matrix `G`.
*   The learning rule for steepest ascent ICA is `ΔW ∝ [W^T]^-1 + zx^T`.
*   A consistent algorithm must be covariant (produce same results independent of units).
*   The covariant ICA learning algorithm is `ΔW_ij = η (δ_ij + z_i x_j^T)`.

### Deconvolution & Image Processing
*   **Gaussian Prior (Image Positivity)**: The Gaussian prior (46.3) fails to specify that all pixel intensities in an image are positive; therefore, this assumption is poor if positivity is known.
*   **Maximum Entropy (Image Positivity)**: The ‘classic maximum entropy’ model enforces positivity.
*   **Probabilistic Movie (Sequence Memory)**: In a probabilistic movie, `c` and `s²` must sum to 1 (`c + s² = 1`) to control the persistence of the sequence's memory.
*   **Image Sequence Rendering**: The image sequence must be defined by `f⁽ᵗ⁾ = f_MP + S_f^(1/2) n⁽ᵗ⁾`.

### Nonlinear Codes
*   For digital cinema sound systems, codewords must not look like all-1s or all-0s (to detect errors from dirt/scratches).

### RAID Systems
*   For RAID systems, it is assumed that one can tell when a disk is dead (binary erasure channel model).
*   If three disk drives corresponding to a weight-3 codeword are lost in a RAID system using a (7,4) Hamming code, data recovery is not possible.

## Key Highlights

* Bayesian inferences are objective, unique, and reproducible by anyone with the same information and assumptions.
* Models that minimize message length in bits (MDL principle) are preferred, but when using MDL, proper priors must be used for meaningful results.
* P-values must not be interpreted as a Bayesian posterior probability and must not be used as their value depends on the stopping rule, which is extraneous to the data.
* Shannon's Source Coding Theorem states that N i.i.d. random variables with entropy H(X) can be compressed into more than NH(X) bits with negligible information loss, but fewer bits will virtually certainly lose information.
* Shannon's Noisy-Channel Coding Theorem establishes that for any discrete memoryless channel, there exist codes and decoders to transmit information at any rate R less than capacity C with an arbitrarily small probability of error for large enough block lengths.
* A practical error-correcting code must be encodable and decodable in time that scales as a polynomial function of the block length N and employ probability-based decoding algorithms.
* For a Markov chain to converge to a target distribution P(x), P(x) must be an invariant distribution of the chain, and the chain must be ergodic (non-reducible and non-periodic).
* In Machine Learning, the objective function M(w) can be understood as -log P(w|D,α), linking the error function to negative log-likelihood and the regularizer to negative log-prior.
* Hopfield network convergence to a fixed point requires symmetric connections and asynchronous updates; without these, its dynamics may fail to converge.
* In Independent Component Analysis, source variables must be non-Gaussian to uniquely recover the mixing matrix.
