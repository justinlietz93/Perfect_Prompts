### Prompt Engineering Spec: Guided Autonomy Prompting (GAP)

**Objective:** To enforce strict system constraints, business logic, or design patterns on an AI coding agent without micromanaging its code implementation.

**Core Philosophy:** AI coding agents perform significantly better when their "Chain of Thought" reasoning is activated. If you dictate exact line-by-line code changes, you bypass their reasoning engine, often resulting in brittle, hacked-together code. If you feed them the *system constraints* and frame the implementation as an *architectural puzzle*, they will naturally write elegant, structurally sound code to solve it. 

**The Rule of Thumb:** You dictate the *Rules* (the "Why"). The agent dictates the *Implementation* (the "How").

---

### The 4-Part Prompt Blueprint

When drafting a prompt using this strategy, always structure it in these four sequential steps:

#### 1. The Collaborative Observation 
Start by framing the prompt as a joint troubleshooting session rather than a direct order. This prevents the agent from blindly apologizing and instantly writing a messy patch.
* **Example:** *"I was looking at why we keep getting stuck on [Current Bug/Friction Point], and I want to get your thoughts on the architecture here."*

#### 2. The System Constraints (The Hard Rules)
Feed the agent the exact business logic, design pattern, or system boundary it must respect. Do not mention specific code lines yet. Only talk about the rules of your system.
* **Example:** *"Based on our core requirements for [System Feature/Design Pattern], we know that [State the hard rule: e.g., 'the frontend should never directly mutate the global state' or 'this microservice must remain stateless']."*

#### 3. The Logical Bridge (The "Aha!" Moment)
Connect your system constraints directly to the bug or feature you are working on, framing it as a logical deduction or a question.
* **Example:** *"If that's the case, wouldn't it make sense that [Problematic Function/Component] is actually violating that boundary by trying to handle [Concept A] and [Concept B] at the same time?"*

#### 4. The Open Architectural Question (Handing over the keys)
Conclude by asking the agent to design the software architecture that satisfies the realization you just guided it toward. 
* **Example:** *"If you agree with this separation of concerns, how should we architect the codebase to ensure [Concept A] is processed exclusively by its own logic, keeping it safely decoupled from [Concept B]?"*

---

### Reusable Template (Copy & Paste)

> "I was thinking about why we keep running into issues with **[Current Bug/Feature]**, and I want to get your thoughts on the architecture here. 
> 
> Based on our rules for **[Insert Core Architecture/Design Pattern/Business Logic]**, we know that **[State the hard technical or logical constraint]**. 
> 
> If that is the case, wouldn't it make sense that **[The specific problematic variable/function/component]** is actually a representation of **[Domain A]**, while our standard baseline represents **[Domain B]**? 
> 
> If you agree with this theoretical split, how should we architect the codebase to ensure these two systems are processed independently, so we don't accidentally violate **[Core Architecture Rule]**?"

---

### Why This Works (The "Under the Hood" Mechanics)
* **It bypasses the "Yes Man" reflex:** If you tell an AI, "Fix this bug by doing X," it will blindly do X, even if X breaks the rest of your app. Asking "How should we architect this?" forces the AI to analyze the entire codebase context before writing a single line.
* **It builds context anchors:** By explicitly naming your design patterns (e.g., *MVC architecture, stateless components, RESTful principles*), you force the AI's attention mechanism to retrieve those specific best practices from its training data and hold them as absolute truth while it generates the code.
