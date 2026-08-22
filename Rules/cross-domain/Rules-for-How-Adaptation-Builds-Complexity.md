# Rules for How Adaptation Builds Complexity

**Generated on:** October 1, 2025 at 3:18 PM CDT

---

## **Agent Structure and Capabilities (General)**

* An agent's behavior must be determined by a collection of rules.
* Describe an agent's input using a set of detectors.
* Describe an agent's output using a set of effectors.
* Effectors must decode standardized messages to cause actions in the environment.
* Do not claim that all CAS agents use binary detectors; rather, use clusters of binary detectors to describe how agents filter information.

## **Syntax and Semantics (Rule-Based Systems)**

* **Messages:**
  * All messages must be binary strings.
  * All messages must be of a standard length (L).
  * The set of all possible messages (M) is formally defined as {1,0}L.
  * Detector-originated messages must have a built-in meaning assigned by detected environmental properties.
  * Rule-originated messages must not have assigned meaning, except when used to activate effectors; they acquire meaning by activating other rules.
  * Differentiate detector-originated messages from rule-originated messages, typically by assigning identifying tags.
* **Conditions:**
  * Use the symbol '#' to denote "anything is acceptable at this position" (a "don't care" symbol).
  * The set of all possible conditions (C) is formally defined as {1,0,#}L.
* **Rules (Basic Format):**
  * All rules must have the form: `IF (condition from C satisfied) THEN (send message from M)`.
* **Rules (Full Computational Power):**
  * For full computational power, rules must support two independent conditions: `IF ( ) AND IF ( ) THEN ( )`.
  * For full computational power, rules must support negation: `IF NOT ( ) THEN ( )`.
* **Schemata:**
  * Use the symbol '\*' as a new "don't care" symbol to define schemata, distinct from '#'.
  * A schema must be a string of the form {1,0,#,\*}L.
  * Each schema specifies the set of all conditions that use that building block.
  * A schema must have one of the three letters {1,0,#} at each of its defining positions (positions without a '\*').

## **Adaptation and Evolution (General)**

* Treat each rule as a producer (buying and selling messages).
* A rule's strength must be reduced when it buys a message.
* A rule's strength must be increased when it sells a message.
* Only rules with satisfied conditions are eligible to bid.
* Only winning rules gain the right to post their messages.
* The size of a rule’s bid must be determined by its strength.
* Stronger rules must bid more.
* A winning rule must thrive (get stronger) only if its consumers pay more than the amount bid.
* Modify bidding to make it proportional to the product of strength and specificity (fewer '#'s).

**Genetic Algorithm Mechanics**

* **Reproduction:**
  * Select parent strings (rules) from the current population based on fitness (strength): more fit strings are more likely to be chosen.
  * If a schema's average strength is less than the overall population average, its instances must be reduced in the next generation.
  * If a schema's average strength is greater than the overall population average, its instances must be increased in the next generation.
* **Recombination:**
  * Parent strings must be paired, crossed, and mutated to produce offspring strings.
  * The crossover point must be chosen at random along the string (in a simplified model).
* **Mutation:**
  * Individual alleles must be randomly modified (e.g., flipping a '1' to '0' or '#').
  * Mutation rates should be low compared to crossover rates.
* **Replacement:**
  * Offspring strings must replace randomly chosen strings in the current population.
  * Repeat the reproduction, recombination, and replacement cycle to produce successive generations.

**Echo Model Rules (General)**

* **Resources:**
  * Specify a set of "renewable" resources, represented by letters (e.g., a, b, c, d).
  * All structures in Echo must be constructed by combining these resources into strings.
  * All strings composed of resource letters are admissible.
* **Geography:**
  * Echo's geography must be specified by a set of interconnected sites.
  * Each site must be characterized by a resource fountain, specifying the amount of each resource appearing at that site on each time-step.
  * A site can hold many agents.
* **Core Reproduction Constraint:** An agent can reproduce only when it has acquired enough resources to make a copy of its chromosome string.
* **Interaction Mechanism:** All interactions must be mediated by tags.

**Echo Model 1 (Offense, Defense, Reservoir)**

* An agent must have two components: a reservoir and a single chromosome string.
* The chromosome must determine the agent's capabilities, specifically its ability to interact via tags specified by segments of the chromosome string.
* Each agent's chromosome must specify two tags: an offense tag and a defense tag.
* When two agents encounter each other, the offense tag of one agent must be matched against the defense tag of the other, and vice versa.
* **Tag Matching:**
  * Align tag strings so their left ends are coincident.
  * Determine a match score by going position by position, assigning a value from a table for each pair of letters.
  * The overall match score is the sum of these assigned points.
  * If one tag is longer than the other, each position without a paired letter must count for a fixed number of points.
* A single tag for each agent must not be used, as it would force transitivity of interactions.

**Echo Model 2 (Conditional Exchange)**

* An agent's chromosome must be divided into two parts: a control segment and a tag segment.
* The control segment must provide an exchange condition.
* The exchange condition must check the offense tag of the other interactant's chromosome.
* Designate one of the symbols already in the resource alphabet as the "don't care" symbol to avoid adding a new symbol.
* Treat the last specified letter in a condition string as if it were followed by an indefinite number of "don't care" symbols to accommodate arbitrary tag lengths.
* **Exchange Interaction Process:**
  * When two agents encounter each other, the exchange condition of each agent must first be checked against the other agent's offense tag.
  * If both conditions are satisfied, the exchange takes place.
  * If neither condition is satisfied, the interaction must be aborted.
  * If one condition is satisfied but not the other, the agent with the unsatisfied condition must have a chance of fleeing the interaction (in the simplest case, by aborting with a fixed probability).

**Echo Model 3 (Resource Transformation)**

* For each transformation desired, an enzyme subsegment must be added to the control segment of the chromosome.
* The cost of a transformation is the effort required to collect additional letters to specify its enzyme subsegment.
* A transformation subsegment must, at a minimum, specify the letter to be transformed and the resulting letter.
* A transformation can only take place if copies of the letter to be transformed are present in the agent's reservoir.
* Set the transformation rate at two letters per time-step (example rate).
* Multiple copies of a transformation segment must multiply the transformation rate.

**Echo Model 4 (Adhesion)**

* Add a new adhesion tag to the tag segment of the chromosome.
* The adhesion tag of each agent must be matched to the *offense* tag on the chromosome of the other agent (not its adhesion tag).
* **Boundary Formation:**
  * Each agent, at the time of its formation, must be assigned to exactly one boundary.
  * Even an isolated agent must be assigned to a unique boundary.
  * A boundary is adjacent to a given boundary if it is directly exterior, directly interior, or alongside (at the same level and connected to the same node).
  * An agent can only interact with agents belonging to the same boundary or to adjacent boundaries.
  * The site itself must be considered a boundary exterior to all agents it contains.
  * Only agents on the outermost boundary of an aggregate can have a domain of interaction that includes other aggregates at the site.
* **Adhesion Outcome Rules (for newly formed offspring with parent/selected agent):**
    1. If both match scores are low, agents do not adhere. If the parent belongs to an aggregate, the offspring is ejected and becomes a new one-boundary, one-agent aggregate.
    2. If both match scores are close to each other in value and not close to zero, the offspring is placed in the boundary of the selected agent.
    3. If the match score of the selected agent is substantially higher than that of the offspring, the offspring is placed in the boundary immediately interior to the selected agent’s boundary (and a new interior boundary is formed if none exists).
    4. If the net score is highly negative, the parent is forced to the interior of the boundary it occupies.

**Echo Model 5 (Selective Mating)**

* Add a mating condition to the control segment of the chromosome.
* The mating condition must be specified in the same way as the exchange condition.
* The mating condition must be matched against the offense tag of the potential mate.
* Mating must be initiated once an agent has collected enough resources to make a copy of itself.
* If the tag-mediated selective mating conditions of both agents are mutually satisfied, mating proceeds.
* During mating, copies of parents' chromosomes must be made using resources from their reservoirs.
* The copied chromosomes must be crossed over, and mutations must take place.
* The two resulting offspring must be added to the population at the site.
* If one or both mating conditions are not satisfied, mating must be aborted.
* All agents must have an average life span.
* Agents must be removed from their boundaries whenever chance, determined by a random death rate, dictates.
* Each offspring formed must be immediately tested for adhesion and placed in the determined boundary without replacing any existing agents.

**Echo Model 6 (Conditional Replication & Multiagents)**

* The multiagent's chromosome must not depend directly on the agent-compartments present within it; it must remain invariant across generations for hard-won adaptations to be retained.
* Agent-compartment replication must be dependent on the activity of other agent-compartments in the multiagent.
* The replication of an agent-compartment must be determined by a replication condition in the control segment of the multiagent’s chromosome part specifying that compartment.
* An agent-compartment can replicate only if its replication condition is satisfied by the activity of some other agent-compartment in the multiagent.
* The replication condition must look to the offense tags of other active agent-compartments in the multiagent.
* The replication condition is satisfied only if at least one active agent-compartment in the multiagent has an offense tag that meets the condition’s requirements.
* At multiagent replication, satisfied agent-compartment replication conditions must be marked (marker bit set to 1); otherwise, they are unmarked (marker bit set to 0).
* Agent-compartments with markers set to 1 are considered "present" in the offspring; those with markers set to 0 are considered "absent".
* Only agent-compartments with marked replication conditions ("present") are eligible to enter into interactions.
* All interactions between multiagents must be mediated by their marked agent-compartments.
* When multiagents interact, one agent-compartment must be randomly selected from the multiagent's outermost boundary to serve as the "point of contact".
* Only agent-compartments with markers set to 1 are eligible for selection as point of contact.
* A new point-of-contact selection must be made each time multiagents come into contact.
* Once point-of-contact agent-compartments are selected, interaction must be carried out as described for individual agents in previous models.
* The contents of the reservoirs of all agent-compartments in a multiagent must be shared (pooled) as the multiagent's resources.
* A multiagent reproduces only if its pooled resources are sufficient to construct a complete copy of its concatenated chromosome.

**Simulation Execution Rules**

* **Contact Definition:** A contact does not necessarily mean an interaction will take place; it only sets the stage.
* **General Contact Principle:** Select one agent at random from all agents at the site, then select the second agent at random from within the domain of interaction of the first agent.
* **Exchange Contacts:**
  * Involve exchange interactions and adhesion interactions not between parent and offspring.
  * Pairs for exchange contacts are drawn at random from the general population, subject to agent boundary conditions.
  * For exchange contacts, exchange conditions are checked first.
  * If both agents' exchange conditions are satisfied, offense tags are matched against defense tags, match scores are calculated, and resources are exchanged per Model 1.
  * If only one exchange condition is satisfied, the agent with the unsatisfied condition has a chance of fleeing the interaction (e.g., aborting with a fixed probability).
* **Mating Contacts:**
  * Involve mating and the adhesion of offspring.
  * Mating candidates are restricted to multiagents with enough resources to reproduce the whole of the multiagent's chromosome.
  * Once a mating pair is selected, the mating condition of each agent is checked against the offense tag of the other.
  * If both mating conditions are satisfied, a copy of each agent's chromosome is made using reservoir resources.
  * The copied chromosomes are then crossed over (crossover point chosen at random), and point mutations are made at a system-specified rate.
  * The two resulting offspring are then introduced into the population.
  * If either mating condition is not satisfied, mating is aborted.
* **Death Mechanism:**
  * At regular intervals, scan all agents.
  * Any agent with less than a prespecified amount of resources in its reservoir must be killed (deleted from the population).

## Key Highlights

* An agent's behavior must be determined by a collection of rules, utilizing detectors for input and effectors for output that decode standardized messages to cause environmental actions.
* All messages must be standardized binary strings of a fixed length; rules are formatted as `IF (condition) THEN (send message)` and support logical `AND` and `NOT` for full computational power.
* Rules adapt by adjusting their strength based on message "buying" and "selling," with stronger, more specific rules bidding more and thriving if their consumers pay sufficiently.
* The system employs a genetic algorithm for evolution, selecting parent rules based on fitness (strength), recombining them via random crossover, and mutating individual alleles at low rates to produce successive generations.
* All interactions within the Echo models are mediated by specialized "tags" on agent chromosomes, with outcomes determined by position-by-position match scores between these tags.
* Many Echo models incorporate conditional interactions, where specific conditions (e.g., exchange, mating, compartment replication) on an agent's chromosome must be met for an interaction or replication to proceed.
* In multiagents, the main chromosome is invariant, but agent-compartment replication is conditionally dependent on other compartments' activity, influencing which compartments are "present" and eligible for interaction.
* Echo Model 4 introduces boundaries, assigning agents to specific interaction domains where interactions are restricted to agents within the same or adjacent boundaries.
* Simulation execution involves randomly selecting agents for either exchange or mating contacts, where agent-defined conditions and genetic operations (crossover, mutation) determine the outcome.
* Agent survival and reproduction are resource-dependent; agents reproduce only with sufficient resources to copy their chromosomes and are killed if their reservoir resources fall below a specified threshold.

## Example ideas

* Conduct a detailed implementation feasibility assessment for the genetic algorithm mechanics, rule-based systems, and multi-agent interactions (Echo Model 6), identifying potential data structure requirements and performance bottlenecks.
* Develop a comprehensive strategy for parameter tuning and sensitivity analysis, specifically for mutation/crossover rates, bid functions, resource thresholds, death rates, and tag matching scores, to understand their impact on system dynamics and emergent properties.
* Design a modular and extensible software architecture that can incrementally incorporate the features of Echo Models 1 through 6, ensuring efficient management of agents, boundaries, and interactions for scalability and future development.
* Define clear metrics and develop visualization tools to analyze and interpret the emergent behaviors of the system, such as population stability, resource distribution, rule set evolution, and the formation/dynamics of multi-agent aggregates.
