# Prompt Engineering Spec: Guided Autonomy Prompting (GAP)

**Objective:** To enforce strict theoretical or mathematical constraints on an AI coding agent without micromanaging its software architecture.

**Core Philosophy:** AI coding agents (like LLMs) perform significantly better when their "Chain of Thought" reasoning is activated. If you dictate exact code changes, you bypass their reasoning engine, often resulting in brittle, hacked-together code. If you feed them the *theoretical constraints* and frame the implementation as an *architectural puzzle*, they will naturally write elegant, structurally sound code to solve it.

**The Rule of Thumb:** You dictate the *Physics* (the "Why"). The agent dictates the *Engineering* (the "How").

---

### The 4-Part Prompt Blueprint

When drafting a prompt using this strategy, always structure it in these four sequential steps:

#### 1. The Collaborative Observation

Start by framing the prompt as a joint brainstorming session rather than a direct order. This prevents the agent from blindly apologizing and immediately writing a patched script.

* **Example:** *"I was thinking about why we keep getting stuck on [X], and I want to get your thoughts on the theoretical architecture here."*

#### 2. The Theoretical Breadcrumbs (The Hard Rules)

Feed the agent the exact mathematical boundaries, formal documents, or core axioms it must respect. Do not mention code yet. Only talk about the theoretical rules of the system.

* **Example:** *"Since our framework is governed by [Formalism Y], shouldn't we be looking at this as a strict split between [Concept A] and [Concept B]?"*

#### 3. The Logical Bridge (The "Aha!" Moment)

Connect your theoretical breadcrumbs directly to the bug or feature you are working on, framing it as a logical deduction or a question.

* **Example:** *"If that's the case, wouldn't [Problematic Feature] simply belong to [Concept A], while [Baseline Feature] belongs strictly to [Concept B]?"*

#### 4. The Open Architectural Question (Handing over the keys)

Conclude by asking the agent to design the software architecture that satisfies the realization you just guided it toward.

* **Example:** *"If you agree with this theoretical split, how should we architect the code so that [Concept A] is processed exclusively by its own rules, keeping it safely out of [Concept B]'s operators?"*

---

### Reusable Template

> "I was thinking about why we keep running into issues with **[Current Bug/Friction Point]**, and I want to get your thoughts on the theoretical architecture here.
> Based on our formal rules for **[Insert Core Axiom/Document Name]**, we know that **[State the hard mathematical or logical constraint]**.
> If that is the case, wouldn't it make sense that **[The specific problematic variable/function]** is actually a representation of **[Theory A]**, while our standard baseline represents **[Theory B]**?
> If you agree with this theoretical split, how should we architect the Python codebase to ensure these two systems are processed independently, so we don't accidentally violate **[Core Axiom]**?"

---

### Why This Works (The "Under the Hood" Mechanics)

* **It bypasses the "Yes Man" reflex:** If you tell an AI, "Fix this bug by doing X," it will blindly do X, even if X breaks the rest of your system. Asking "How should we architect this?" forces the AI to analyze the entire codebase before writing a single line.
* **It builds context anchors:** By explicitly naming your formalisms (e.g., *S1 Metriplectic Split*), you force the AI's attention mechanism to retrieve those specific rules from its context window and hold them as absolute truth while it generates the code.

Would you like me to format this into a `.md` Markdown file format inside a code block so you can easily copy and paste it directly into your `Derivation` repository for future reference?
