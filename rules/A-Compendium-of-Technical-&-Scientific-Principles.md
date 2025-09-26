# A Compendium of Technical & Scientific Principles

**Generated on:** September 26, 2025 at 1:52 AM CDT

---

## Generated Summary

This document synthesizes critical technical rules, requirements, and constraints from various segments of a larger body of work, presented as a single, cohesive, and de-duplicated master list of principles.

---

### Foundational Principles & Critical Thinking

*   Critically evaluate all definitions, recognizing their strong influence on conclusions and inherent potential for distortion.
*   Believe nothing unless it aligns with personal reason and common sense; assume responsibility for your beliefs.
*   Regularly challenge accepted rules and avoid blind application of flawed methods; doubt fosters leadership, but too much leads to paralysis.
*   Recognize that an order of magnitude change (factor of 10) in technology can produce fundamentally new effects.
*   Identify fundamental concepts by their longevity and their ability to derive the rest of the field using standard methods.
*   Master jargon to gain its advantages, but be aware it can obscure meaning and hinder thinking outside its original scope.
*   Mathematical postulates are human constructs, subject to change.
*   The meaning of a symbol (or string of bits in a machine) arises solely from its usage and processing, not from any inherent definition.
*   Science describes *how* things happen, not *why*.
*   Recognize that multiple theories can account for a body of observations; data alone cannot yield a unique theory.
*   All linear theories with conjugate variables exhibit an uncertainty principle.

### System Design & Architecture

*   Understand the fundamental machine cycle: fetch instruction from Current Address Register (CAR), decode, execute (potentially altering CAR without incrementing for a jump).
*   Machines manipulate symbols without inherent meaning; they obey programmed instructions precisely. Debug by assuming strict instruction execution, not "free will."
*   Computers rely on physically close two-state (binary) devices (bits, gates) for high-speed operation within integrated circuits.
*   Design software systems to prevent unauthorized access and alteration of system-reserved resources (e.g., through address partitioning).
*   Avoid absolute addressing in software and libraries, as it complicates modification and reuse.
*   Do not optimize individual components; this likely ruins overall system performance.
*   Design modern systems with flexibility and graceful degradation to handle future changes and exceeding specifications without sharp failure.
*   Integrate reliability into component design by selecting materials and geometries that manage stress.
*   Standard computers handle only discrete symbols, limiting what they can process.
*   Digital machines offer high accuracy and "deep computation." Analog machines, though limited in accuracy (rarely better than 1 part in 10,000 per component), can be faster for some problems, provide immediate feedback, and incorporate physical components directly. Analog computers still have a place as tools.

### Software Development & Engineering

*   Design programming languages for human users with adequate redundancy (e.g., 40-60%) to mitigate human error, prioritizing human capabilities over pure logical design or ease for computer experts.
*   In rapidly changing software fields, projects with only distant payoffs are unlikely to succeed.
*   Before programming, rigorously define the entire task, including acceptance tests and future maintenance. Acknowledge that real-world problems often lack initial well-defined specifications.
*   Recognize significant programmer productivity variations (often by more than a factor of 10); years of experience or number of languages alone do not guarantee improvement.
*   Neural networks can learn functions from data without explicit programming rules, solving broad problems by adjusting parameters and data. If neural networks have finite usable bandwidth, the sampling theorem equivalence applies.
*   Be skeptical of claims that programs can be "proved correct" like mathematical theorems, as theorems themselves aren't absolutely certain and many real-world problems lack sharp definitions for formal proof.

### Data Management & Analysis

*   Never process data without careful examination for errors; at minimum, pretest all data for consistency and outliers.
*   Do not trust machines to gather data about themselves accurately; calibrate and verify all new instruments.
*   Be skeptical of claimed measurement accuracies; expect the next independent measurement to often fall outside previous confidence limits.
*   Be wary of combining careful estimates with wild guesses, as overall system reliability is often erroneously assumed from only the reliable parts.
*   Be aware that definitions of what is being measured (e.g., economic indices, poverty) constantly change, confounding time series interpretations.
*   Recognize human unreliability in repetitive and accurate tasks. Prioritize small, carefully selected samples over large, poorly collected ones, as resources and time limit truly accurate large datasets.
*   Seek expert advice for questionnaire design, administration, and evaluation. Be aware that phrasing, ordering of questions, and the identity of the interviewer seriously affect answers.
*   Use averages only for homogeneous groups. For skewed distributions (e.g., income, house prices), prefer the median over the mean as an indicator.
*   Be aware that the presence of an observer (e.g., a high-ranking officer) can alter behavior and data collection outcomes.
*   Design rating schemes to utilize the full dynamic range for maximum information (maximum entropy).
*   Design exams around the pass-fail dividing point to provide clear evidence for making decisions and addressing complaints.
*   When designing or commenting on measurement systems, consider all hidden organizational consequences, as individuals will change their behavior in response. Avoid implementing systems that create counter-incentives detrimental to the overall system (e.g., measuring software productivity by lines of code).
*   Prioritize a poorer but more relevant measurement over an accurate, reproducible, but less relevant one.
*   Recognize that different measurement scales may be appropriate for different types of conclusions from the same data; this distinction is seldom recognized or used.
*   Be aware that individuals in an organization may "bend" reports to look good, and evaluations can be reinterpreted (e.g., as probabilities) at higher levels.
*   When dealing with count data, work with square roots of counts to stabilize variances and improve processing.

### Signal Processing & Numerical Methods

*   Sample band-limited signals at equal intervals at a rate of at least twice its highest frequency (Nyquist rate) for perfect reconstruction. In practice, use 7-10 samples per cycle for the highest frequency due to finite data and one-sided access. Sampling non-bandlimited functions causes higher frequencies to alias irrevocably into the Nyquist band.
*   The order of sampling a function and then limiting the range of observation, or vice versa, yields the same result.
*   A nonrecursive filter output is a weighted sum of current and past inputs; any nonrecursive filter can be decomposed into smoothing (cosine transfer function) and differentiating (sine transfer function) components.
*   Ideal filters have sharp cutoffs (transfer function values of 1 in passband, 0 in stopband). Representing discontinuous transfer functions with Fourier series requires infinite terms; truncating causes Gibbs' phenomenon (a fixed percentage overshoot near discontinuities). Windowing (e.g., Lanczos) reduces Gibbs' by modifying spectral leakage, and Fourier series convergence rate reflects function continuity.
*   Digital filter operations (time/spatial domain) are equivalent to convolution of coefficient arrays, which in the frequency domain is equivalent to multiplication of transfer functions. Cascaded filters have an overall transfer function that is the product of individual transfer functions. Multiplication in one domain corresponds to convolution in the other.
*   Kaiser window design guides filter length and parameter selection based on ripple tolerance and transition width, but may require iteration if ripples from multiple edges combine.
*   The Fast Fourier Transform (FFT) efficiently computes Fourier coefficients (reducing operations from N² to N log N), but implicitly assumes the input function is periodic over the sampling interval, forcing non-harmonic frequencies into harmonic ones.
*   The power spectrum (sum of squares of Fourier coefficients or square of absolute value of complex coefficients) is independent of the time origin.
*   While real noise spectra typically fall off at high frequencies, sampling aliases higher frequencies into a flat (white noise) spectrum. Signals are usually concentrated in lower frequencies. No linear filter can separate signal from noise at the same frequencies; oversampling allows low-pass filters to remove more noise by pushing it out of the signal band.
*   Recursive (Infinite Impulse Response) filters use past inputs/outputs, often for real-time, two-sided processing. They involve feedback, requiring careful attention to stability (not exponential growth from bounded inputs). Their transfer function is a rational function, and design methods are largely heuristic.
*   Differentiation magnifies high frequencies, which typically contain noise, necessitating a cutoff frequency in differentiating filters.
*   Do not adjust cutoff edges or other parameters for different parts of the same data run without strong justification (e.g., considering "degrees of freedom").
*   Fourier analysis assumes a linear underlying model; its application to highly nonlinear phenomena can lead to failure. Nonlinear filters (e.g., running median) exist and can offer advantages like local noise removal without smoothing discontinuities.
*   In numerical integration (e.g., predictor-corrector methods), dynamically adjust step size based on differences between predicted and corrected values for optimal accuracy and economy. For systems of differential equations, apply this process to each component vector.
*   In Quantum Mechanics, probability is assigned to individual particles (e.g., photons/electrons) and obtained by taking the square of the absolute value of complex numbers.

### Error Control & System Reliability

*   Transmission through space (signaling) is equivalent to transmission through time (storage).
*   An encoder should consist of two parts: source encoding (adapted to the information source) and channel encoding (adapted to the transmission channel).
*   Assume the communication channel has "random noise added" (incorporating all system noise), and that the encoder/decoder function without error for mathematical modeling.
*   Design codes to be instantaneously uniquely decodable (no symbol must be a prefix of any other) for practical efficiency; follow a decoding tree logic. Include an escape symbol for message termination unless continuous decoding is always intended.
*   Optimize code efficiency by minimizing average length (L), bounded by Kraft's inequality (∑(1/2^l_i) ≤ 1 for base 2). If the sum < 1, there is excess signaling capacity. Huffman coding, by repeatedly combining the two least frequent symbols, achieves minimal average length when symbol probabilities differ, and can minimize variance by careful placement of composite probabilities during its construction.
*   Implement single error detection by adding a parity bit (e.g., even number of 1s). A failed parity check indicates an odd number of errors; a successful one indicates either no errors or an even number of errors.
*   For mathematical tractability, assume white noise: errors are independent and have the same probability at each bit position.
*   Engineering judgment is required to balance block length (n) against error probability (p) to control redundancy and the probability of undetected errors.
*   Error detection schemes (e.g., 2-out-of-5 codes) aid maintenance by localizing errors early.
*   For human input errors (e.g., digit transpositions, single digit changes), single error detection is insufficient; use weighted codes with a prime modulus for calculation (e.g., ISBN modulo 11).
*   If an error can be detected, it can (with proper design) also be located and corrected by changing the erroneous bit.
*   Two-dimensional parity checks allow single error correction, but cannot unambiguously correct two errors (e.g., if they are not in the same row/column, or in the same row/column in a way that confounds location).
*   Design Hamming codes by ensuring the error syndrome (binary number from parity checks) directly identifies the erroneous bit position (all zeros indicate no error). Equivalent codes are formed by interchanging or complementing columns.
*   To add double error detection to a single error correcting code, add an overall parity check bit for the entire message; specific syndrome/parity combinations indicate correct, single, or double errors.
*   Error correction/detection capabilities are determined by the minimum Hamming distance between valid code points: distance 1 for unique decoding, 2 for single error detection, 3 for single error correction, 4 for single error correct and double error detect, 2k+1 for k error correction, and 2k+2 for k error correction and k+1 error detection.
*   Finding an error correcting code is equivalent to finding a set of code points in n-dimensional space with the required minimum distance between legal messages.
*   Error correction capabilities can be traded for detection capabilities (e.g., giving up one error correction can gain two error detections).
*   Error correcting codes are vital for reliable operation and successful field installation/maintenance of elaborate equipment, and are the only known solution when noise cannot be overcome (e.g., low power, jamming). For efficiency, if a system has error correction capacity, it should be utilized frequently, implying a high number of errors corrected per message.
*   Information (Shannon) is defined as "surprise" and measured as the negative logarithm (base 2) of the probability of an event: `I(p) = -log₂(p) = log₂(1/p)`. A certain event (probability 1) contains no information. For independent events, information is additive.
*   The average amount of information (expected value) in a system with `g` symbols and probabilities `p_i` is the entropy `H(P) = ∑ p_i * log₂(1/p_i)`. Maximum entropy (`log₂(g)`) occurs when all symbols have equal probability.
*   The entropy `H(P)` is a lower bound for the average code length `L` of any symbol-to-symbol encoding.
*   For a binary symmetric channel with probability `P` of no error and `Q=1-P` of error, the channel capacity `C` per bit is `C = 1 - H(P) = 1 - H(Q)`. More information cannot be sent reliably than the channel capacity permits. For sufficiently large block length `n`, an arbitrarily small error probability can be achieved while sending information arbitrarily close to the channel capacity.
*   Shannon's theorem implies very long message lengths (`n`) and very large, randomly generated codebooks are required to achieve near-capacity, low-error rates, making practical application challenging. Information theory guides towards efficient designs but does not provide explicit design methods.
*   Information theory, based on "surprise," is relevant for machine communication but not typically for human communication of "information" as humans understand it.
*   For binary error correcting codes, define `1+1=0` (modulo 2 arithmetic) as the basic operation.

### Simulation & Modeling

*   Simulations answer "What if...?" questions, offering cheaper, faster, often more accurate, and sometimes unique experimental capabilities than physical tests.
*   Simulations demand significant expert knowledge in the field of application (to avoid omitting crucial details) and highly repetitive programming components for affordability.
*   Simulations are feasible for systems with high stability; analyze system stability carefully before undertaking a simulation. Exercise extreme caution when simulating unstable situations.
*   Do not substitute careful thought and system intuition with a large volume of simulation output.
*   Adopt a phased simulation methodology: start with simple simulations to gain initial insights, gradually evolve to more complete ones, and include all small effects for final design.
*   Almost any mathematically describable situation can be simulated in principle.
*   Always question, "Why should anyone believe this simulation is relevant?" before beginning any simulation. Simulation reliability encompasses both the accuracy of modeling and the accuracy of computations.
*   Align simulation rigor with its purpose (e.g., amusement vs. critical design). Ensure all essential details are included, especially for critical systems (e.g., life-or-death situations).
*   Economic simulations inherently lack the reliability found in hard sciences due to the absence of single, reliable fundamental economic laws.
*   Exercise extreme caution when combining data, as it can obscure or create spurious effects (e.g., Simpson's paradox) not present in the detailed individual data. Combine data only when the underlying laws and the appropriateness of combination are well understood.
*   Maintain integrity; do not allow simulations to be used for propaganda. Be wary when agreeing to perform simulations.
*   Beware of simulations where human participants can use the output to alter their behavior patterns for their own benefit, thereby vitiating the simulation.
*   For highly uncertain situations, use scenarios rather than attempting to predict exact outcomes.
*   Evaluate simulation reliability by assessing: support for assumed laws in the background field; confidence that no vital effects are missing; reliability of input data; system stability (stable vs. unstable); availability of cross-checks against past experience; and presence of internal checks (e.g., conservation laws). Redundancy is essential for reliability checks.
*   Ensure accurate translation of problem descriptions (marks on paper) into machine input; programming errors are common. For complex systems with many similar equations/parameters, automate the generation of equations from input specifications to ensure accuracy and consistency.
*   Structure interdisciplinary simulation projects to keep experts focused on their core expertise (e.g., chemistry) rather than machine mechanics, while still requiring them to engage in the "thinking part."
*   In simulations involving physical systems, account for real-world constraints; e.g., do not allow people to move around in a vehicle during midcourse corrections in space flight simulations.
*   For new simulation areas lacking known experiences or theory, demand mathematically expressed rules for every possible interaction and real-live data for comparing test runs.
*   Do not assume simulation reliability based merely on a large machine producing nicely printed sheets or colorful pictures; critical scrutiny is always required.
*   Assume responsibility for decisions made based on simulations; do not attribute blame to those who performed the simulations.
*   Ensure precise agreement between proposer and programmer on the interpretation of mathematical symbols and model assumptions to avoid significant errors. Intimate understanding of the problem by the programmer is critical.

### Professional Conduct & Learning

*   Continuously learn new fields to adapt to evolving technology and avoid being left behind by new developments.
*   Foster collaboration and interdisciplinary engagement. Be helpful to others and allow them to take credit, as this fosters teamwork and recognition.
*   A systems engineering job is never truly done because solutions change the environment, creating new problems, and engineers gain deeper insight over time. Part of a systems engineer's job is to define the problem in a deeper sense, moving from client-reported symptoms to underlying causes. A solution that does not provide greater insight than was available at the beginning is a poor solution. The goal of a system will constantly change as the understanding of both the engineer and the customer deepens. Strive to solve the *right* problem (even imperfectly) with the realization that the solution is temporary and will evolve with deeper insight.
*   Specialists brought together for a systems engineering team must return to their specialties between jobs to maintain their expertise.
*   Education should focus on fundamentals to prepare students for their future, not just the past or present.
*   Use analogies as a powerful creative tool; a valuable analogy need not be close but merely suggestive. Be prepared to abandon an analogy when it is pressed too far, as they are rarely perfect.
*   Actively acquire new knowledge by looking at it from many different angles and pondering its various sides before filing it away. Avoid mere memorization; prepare your mind for future application.
*   Embrace false starts and faulty solutions as valuable; they sharpen your approach by showing what does not work and why. When stuck, consider inverting or reframing the problem, as this often leads to significant breakthroughs.
*   Set high goals for your career; it is worth striving to accomplish significant things rather than merely surviving.
*   Prepare yourself for success through consistent effort; do not depend solely on luck.
*   Prioritize working on important problems that have a possible attack, rather than just on random things or problems with only inherent (but unapproachable) importance.
*   Cultivate self-confidence and courage to pursue great work, especially during periods of discouragement.
*   Have a vision of excellence to guide your efforts consistently in a world of constant change.
*   Regularly dedicate time to ask larger strategic questions about your field's future, avoiding constant immersion in details. This is necessary for leadership.
*   Cultivate the ability to tolerate ambiguity, holding both belief in your field's excellence and recognition of its room for improvement simultaneously.
*   Keep a mental list of 10 to 20 basic, important unsolved problems in your field, ready to act when clues appear.
*   Master formal presentations, written reports, and informal presentations to effectively sell your ideas through clear presentation, not propaganda. Do not assume good ideas will win automatically without careful presentation.
*   Adopt the habit of privately critiquing all presentations you attend and asking for others' opinions to improve your presentation style.
*   Recognize that freedom to practice your expertise is generally earned by developing your abilities and establishing a reputation.
*   Expect to have superiors who are less capable than you as you rise in an organization.
*   Continuously examine your life and career choices; an unexamined life is not worth living.
*   Create a plan for the future to guide your efforts and avoid drifting aimlessly.
*   When you rise to leadership, remember that the methods that made you successful may be counterproductive when applied at a later date; be prepared to adapt.
*   When dealing with experts (including yourself), regularly ask, "What would you accept as evidence you are wrong?" to challenge underlying assumptions.
*   Do not automatically reject crazy ideas, especially from outside your official circle, but also do not pursue every crackpot idea.
*   Do your job in a way that allows others to build on your work, and share your ideas freely.
*   Strive to do your best in given circumstances, and focus on fundamental changes rather than trivial reforms.

## Key Highlights

* Critically evaluate all definitions, recognizing their strong influence on conclusions and inherent potential for distortion; believe nothing unless it aligns with personal reason and common sense.
* Avoid optimizing individual system components in isolation, as this often degrades overall system performance; instead, design for flexibility and graceful degradation.
* Never process data without careful examination for errors and pretest all data for consistency; prioritize poorer but more relevant measurements over accurate yet less pertinent ones.
* Always question the relevance and reliability of a simulation before beginning, ensuring all essential details are included and resisting its use for propaganda.
* Continuously learn new fields, embrace false starts and faulty solutions as valuable learning experiences, and dedicate time to ask larger strategic questions about your field's future.
* When dealing with experts, including yourself, regularly ask, 'What would you accept as evidence you are wrong?' to challenge underlying assumptions and foster critical review.
* Recognize that a systems engineering job is never truly done as solutions change the environment; continually strive to solve the *right* problem, understanding solutions are temporary and evolve with deeper insight.
* Master formal and informal presentations to effectively sell your ideas through clear communication, as good ideas do not automatically win without careful presentation.

## Insightful Ideas

* Establish a cross-functional working group to develop an audit framework and self-assessment tools, drawing directly from these principles, to evaluate current project methodologies, system designs, and data handling practices for adherence and potential improvements.
* Identify 3-5 critical principles from each technical section (System Design, Software, Data, Error Control) that are most relevant or frequently overlooked in our current operations, and develop targeted training modules or workshops to embed this knowledge across relevant teams.
* Conduct a comprehensive review of current simulation and modeling practices, focusing on adherence to principles related to validation, stability analysis, data combination caveats, and the responsible use of simulation output (avoiding propaganda).
* Initiate a focused investigation into the practical application of advanced error detection and correction codes (e.g., Hamming codes, weighted codes) for critical data storage and transmission pathways, particularly where noise or human error is a significant factor, and assess current practices against Shannon's theorem implications for channel capacity.
* Re-evaluate current strategic technology adoption and development processes to ensure they actively challenge accepted rules, avoid blind application of flawed methods, and prioritize flexibility and graceful degradation in system design, rather than merely optimizing individual components.