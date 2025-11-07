# Rules for Human-Centered Design and Resilient Systems

**Generated on:** November 7, 2025 at 5:52 PM CST

These rules synthesize principles for designing robust, usable, and human-centric technical systems. They prioritize user needs, anticipate human limitations, and guide the entire product lifecycle from conception to operation.

---

## 1. Human-Centered Design Principles

* **You will prioritize human needs, capabilities, and behavior** in all design decisions (Human-Centered Design).
* **You will base designs on a deep understanding of people**, their psychology, and their interaction with technology.
* **You will assume people will make errors** and design systems to prevent them or minimize their impact; never blame users for misuse.
* **You will design systems to function well even when plans deviate or errors occur**, focusing on failure cases, not just planned operation.
* **You will treat all failures (human or mechanical) by finding fundamental causes** and redesigning the system to prevent recurrence or minimize impact.
* **You will design with consideration of the entire system**, ensuring requirements, intentions, and desires are understood and respected across all stages and disciplines.
* **You will produce successful products by satisfying all requirements** from multiple disciplines: usability, aesthetics, affordability, reliability, manufacturability, serviceability, distinctiveness, and core functions.
* **You will provide flexibility in design** (e.g., adjustable sizes, settings) to accommodate diverse user needs and design for a wide range of human anthropometry.
* **You will design for activities rather than individuals** to ensure broad usability, supporting both high-level activities and their constituent low-level tasks seamlessly.
* **You will leverage Inclusive/Universal Design principles**, designing aids for people with difficulties to be universally beneficial.
* **You will avoid confusion and tame complexity** by providing a clear, coherent, and appropriate conceptual model.

## 2. Usability & Interaction Design

### 2.1. Discoverability & Conceptual Models

* **You will ensure the discoverability of possible actions** and methods for their performance.
* **You will make relevant components visible** and ensure they communicate correct messages about possible actions.
* **You will provide sufficient cues and knowledge "in the world"** to enable good performance, even without prior knowledge, making memory unnecessary where possible.
* **You will provide aids for users to form correct conceptual models** of how the product works and avoid misleading information.

### 2.2. Affordances & Signifiers

* **You will ensure affordances and anti-affordances are discoverable and perceivable**, providing strong clues for operation.
* **You will use signifiers to communicate where actions should take place** and help users understand the product's purpose, structure, operation, current state, and alternative actions.
* **You will ensure signifiers are perceivable** and communicate appropriate behavior, integrating them into a cohesive experience.
* **You will ensure physical designs (e.g., doors, faucets) naturally indicate their operation** without requiring external signs or trial and error.

### 2.3. Mappings

* **You will employ clear and understandable mappings** between controls, actions, and results.
* **You will utilize natural mappings** (spatial analogies) for immediate understanding, grouping related controls together and placing them close to the item being controlled.
* **You will prioritize natural mappings** (e.g., direct mounting of controls on items) to reduce human memory load.

### 2.4. Feedback

* **You will provide immediate feedback** (delay of no more than a tenth of a second) to indicate system response to user requests.
* **You will ensure feedback is informative**, unobtrusive for routine confirmations, and attention-capturing for important signals, avoiding poor, distracting, or excessive feedback.
* **You will display progress indicators** (e.g., hourglass, progress bars) for delayed operations, and when predicting time, underpredict or display the slowest possible time.
* **You will ensure feedforward (possible actions) and feedback (results) are presented in a readily interpretable form** that matches user goals and expectations.
* **You will use sound to provide otherwise unavailable or invisible information** (e.g., system status, action confirmation), ensuring sounds are informative, non-annoying, and privacy-respecting.

## 3. Error Prevention & Resilience

* **You will design systems to prevent users from making errors** and to quickly detect errors if they occur.
* **You will avoid designing systems that induce users to make errors** or require prolonged, unnatural attention, complex memory, or multitasking for critical operations.
* **You will implement poka-yoke (error-proofing) techniques** such as fixtures, asymmetrical designs, or physical constraints (e.g., unique filling points) to ensure correct operation.
* **You will provide "undo" functionality** (preferably multi-level) or make irreversible actions harder to perform.
* **You will treat user actions as approximations, not errors**, providing assistance for proper completion and never forcing users to start over.
* **You will design for easy error discovery and correction**, always preserving critical information needed to resume interrupted tasks.
* **You will implement sensibility checks** (common sense tests) on user actions and system operations to prevent egregious errors or detect anomalous values.
* **You will design systems to facilitate resuming operations easily after interruptions**, assuming users will be interrupted.
* **You will embrace errors as learning opportunities**, investigate their causes (e.g., using "Five Whys"), and redesign products or procedures to prevent recurrence.
* **You will foster a culture of non-punitive error reporting**, establishing systems that encourage admission and focus on cause analysis and prevention.
* **You will minimize slips by making actions and their controls as dissimilar or physically separated as possible**, avoiding rows of identical controls.
* **You will implement multiple layers of defense** (e.g., multi-person checklists, redundant systems) to reduce opportunities for slips, mistakes, or equipment failure.
* **You will continuously invest in anticipating changing failure potential** and develop foresight to prevent harm.

## 4. Information & Communication

* **You will ensure good communication from machine to person** regarding possible actions, current state, impending events, and especially when things go wrong.
* **You will ensure the system image is coherent, appropriate, complete, and non-contradictory**, providing information that supports good conceptual models.
* **You will eliminate unhelpful error messages** from electronic systems, providing help, guidance, and direct correction mechanisms instead.
* **You will design systems to accept any intelligible input format** (e.g., names, dates), accommodating human imprecision and inaccuracy in input.
* **You will mitigate short-term memory limits** by externalizing information ("knowledge in the world"), using multiple sensory modalities, and facilitating immediate entry of critical information.
* **You will ensure all relevant information** (goals, plans, current system evaluation) is continuously available and never presented in transient messages.
* **You will design warning signals to be noticed without being annoying or distracting**, attracting attention and conveying information, and coordinating them across instruments to avoid cacophony.

## 5. System & Software Architecture

* **You will avoid unnecessary modes**; if modes are necessary, the active mode must be obvious, and the system designed to compensate for mode confusion.
* **You will design automated systems as collaborative, cooperative partners** with human teams, assisting where humans need it most, not just handling easy tasks.
* **You will avoid creating rules or procedures that are inappropriate** or encourage violation, ensuring work can be done without requiring violations.
* **You will utilize checklists** as a collaborative team activity to increase accuracy and reduce slips, designing them iteratively and ensuring electronic versions track skipped items.
* **You will design security systems to be effective without being overly complex or restrictive**, as this can lead to users bypassing them.
* **You will require multiple identifiers for security** (e.g., combining "something you have" with "something you know").
* **You will prefer 24-hour time specification** over AM/PM to reduce confusion and error.

## 6. Design Process & Collaboration

* **You will understand the real, fundamental, root problem** before attempting solutions, treating the original problem statement as a suggestion and using methods like "Five Whys" to explore underlying issues.
* **You will employ an iterative and expansive design process** involving continuous observation, idea generation, prototyping, and testing.
* **You will conduct design research through direct observation** of potential customers in their natural environment to understand their activities, motives, and true needs.
* **You will integrate both qualitative design research and quantitative market research** through collaborative teams.
* **You will generate numerous ideas** without early fixation, encouraging creativity and questioning all assumptions.
* **You will test ideas by building quick, low-fidelity prototypes** or mock-ups, testing them with target users in realistic scenarios.
* **You will embrace frequent, fast failures during prototyping** as learning experiences for continual refinement.
* **You will form harmonious, multidisciplinary product development teams** with continuous representation from all relevant disciplines (e.g., design, engineering, marketing, manufacturing, service) to ensure clear communication and resolve conflicts collaboratively.
* **You will continuously refine requirements** through repeated study and testing, rather than relying on abstract definitions or direct questioning.

## 7. Standards & Consistency

* **You will strive for agreed-upon standards for controls and mappings** to minimize learning effort and facilitate knowledge transfer between systems.
* **You will maintain design consistency**, prioritizing it over minor improvements, and ensuring all related systems change together if a design change is implemented.
* **You will implement design changes only when new methods are vastly superior**, clearly outweighing the difficulties of adaptation.
* **You will account for cultural constraints and conventions** in design, anticipating and adapting to changes over time, and planning for confusion when breaking conventions or switching metaphors.
* **You will standardize only when no other design solution is possible**, avoiding standardization too early (locking into primitive tech) or too late (preventing agreement on new standards).

## 8. Physical & Product Design Specifics

* **You will design controls and displays to be significantly different for distinct purposes** (e.g., shape coding) to prevent description-similarity slips.
* **You will prefer activity-centered controls over device-centered controls**, carefully selecting activities that match actual requirements.
* **You will design emergency exits to allow unimpeded egress** (e.g., panic bars) while deterring unauthorized use.
* **You will adhere to established conventions** for physical interactions (e.g., faucet operation, screw-thread mechanisms) and reflect psychological conceptual models in standards.
* **You will use sound as a signifier for vehicle presence and orientation**, ensuring it is not annoying and is standardized for easy interpretation while allowing for individualization.
* **You will not allow aesthetic focus to compromise usability.**
* **You will consider skeuomorphic design** to ease user transition to new technologies and simplify learning.

## 9. Security & Deliberate Constraints

* **You will deliberately make certain operations difficult or undiscoverable when safety or security is paramount.** This includes:
  * Restricting access for unauthorized individuals (e.g., doors, security systems).
  * Making dangerous equipment or operations difficult to perform accidentally (e.g., requiring two simultaneous, separated actions).
  * Child-proofing containers for dangerous substances.
  * Disrupting normal routine actions for critical, irreversible operations (e.g., permanent deletion).
* **For deliberately difficult designs, normal good design principles must be applied to all but the intentionally difficult parts.** Specifically, for the difficult parts:
  * Components may be hidden or invisible.
  * Unnatural or haphazard mappings may be used.
  * Actions may be physically difficult or require precise timing/manipulation.
  * Feedback may be omitted or evaluation made difficult to interpret.

## 10. Specialized Contexts & Regulatory Compliance

* **You will establish "sterile periods"** for safety-critical operations (e.g., aviation, medicine) to minimize interruptions and distractions.
* **You will ensure human operators for automation failures with short response times receive extensive training** and that systems provide clear, immediate indications of failure.
* **You will not allow untrained or incompetent people to perform activities** requiring specific skills or knowledge, and ensure continuous practice for critical skills.
* **You will adhere to industry-specific error reporting policies and standards** (e.g., NASA ASRS for aviation, potentially unique reporting structures in manufacturing), while generally aiming for non-punitive systems.
* **You will consult and comply with relevant regulatory and international standards** for system design, especially concerning warning signals and safety.

## Key Highlights

* Prioritize human needs, capabilities, and behavior in all design decisions, assuming users will make errors and designing systems to prevent or minimize their impact.
* Treat all failures, whether human or mechanical, by finding their fundamental causes and redesigning the system to prevent recurrence or minimize future impact.
* Ensure the discoverability of possible actions, provide clear affordances and signifiers, and offer immediate, informative feedback for all user interactions, making memory unnecessary where possible.
* Design systems to actively prevent users from making errors through techniques like poka-yoke, provide multi-level "undo" functionality, and treat user actions as approximations rather than mistakes.
* Understand the real, fundamental root problem before attempting solutions, employing an iterative design process that involves continuous observation, idea generation, prototyping, and testing with target users.
* Form harmonious, multidisciplinary product development teams with continuous representation from all relevant disciplines to ensure clear communication and collaborative conflict resolution.
* Deliberately make certain operations difficult or undiscoverable when safety or security is paramount, such as restricting access or making dangerous equipment hard to operate accidentally, while maintaining good design principles for all other parts.
* Maintain design consistency across systems and implement design changes only when new methods are vastly superior, clearly outweighing the difficulties of adaptation for users.

## Example ideas

* Perform a comprehensive audit of a flagship product or an ongoing project against these Human-Centered Design and Resilient Systems commandments to identify current adherence, gaps, and areas for immediate improvement.
* Integrate these HCD and Resilience principles into mandatory design, engineering, and product management training programs, establishing clear checkpoints within the product development lifecycle for their consistent application.
* Implement a structured 'Five Whys' root cause analysis process for all significant user errors and system failures, focusing on systemic redesign (poka-yoke) and fostering a non-punitive error reporting culture.
* Review and enhance current user research methodologies to prioritize direct observation of users in their natural environments and mandate rapid, low-fidelity prototyping with frequent user testing to embrace iterative learning and 'fast failures'.
