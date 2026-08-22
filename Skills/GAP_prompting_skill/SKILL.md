---
name: gap-prompting
description: >
  Guided Autonomy Prompting (GAP) — a meta-methodology for AI-assisted software
  architecture. This skill operates in TWO modes. MODE A (Respond): When the user
  sends a GAP-structured prompt (collaborative framing + theoretical/system constraints
  + logical bridge + open architectural question), Claude activates deep architectural
  reasoning — analyzing the full codebase context before writing any code, treating
  named constraints as inviolable axioms, and designing the architecture before
  implementing it. MODE B (Craft): When the user asks for help writing a prompt for
  an AI coding agent, or is struggling to communicate constraints to an AI, or says
  things like "help me prompt this", "how should I frame this for Claude Code",
  "write a GAP prompt", "I need to get the agent to respect my architecture",
  "the AI keeps breaking my design pattern", or "how do I tell the AI about my
  constraints without micromanaging" — Claude helps them construct a 4-part GAP
  prompt using the appropriate domain template (physics/theoretical or general
  software). Also trigger when the user mentions "GAP", "guided autonomy", or
  references the 4-part prompt blueprint, or when the user is clearly frustrated
  that an AI agent isn't respecting their system architecture.
---

# Guided Autonomy Prompting (GAP)

## Philosophy

AI coding agents perform best when their chain-of-thought reasoning is activated by
*constraints*, not *instructions*. Dictating exact code changes bypasses the reasoning
engine and produces brittle patches. Feeding the agent the theoretical/system constraints
and framing implementation as an architectural puzzle produces elegant, structurally
sound code.

**The core rule:** You dictate the *Why* (physics, axioms, business logic, design
patterns). The agent dictates the *How* (code architecture, implementation).

This skill has two operational modes.

---

## Mode A: Responding to a GAP Prompt

### Recognition Signals

A GAP prompt has a distinctive shape. Recognize it when the user's message contains
most of these elements (they don't need to use the exact labels):

1. **Collaborative framing** — "I was thinking about...", "I want to get your thoughts
   on...", "Let's look at this together..." — NOT a direct order like "fix this bug"
2. **Named constraints** — Explicit references to formalisms, axioms, design patterns,
   or system rules that must be respected
3. **Logical bridge** — A deduction connecting the constraints to the current problem,
   often phrased as a question: "Wouldn't it make sense that..."
4. **Open architectural question** — "How should we architect..." rather than
   "Change line 42 to..."

When you detect this shape, even partially, activate the GAP response protocol.

### Response Protocol

When responding to a GAP prompt, follow this sequence rigorously:

#### Step 1: Confirm the Constraint Frame

Before touching any code, explicitly restate the constraints the user named. This
serves two purposes: it forces you to load those constraints into active attention,
and it lets the user verify you understood them correctly.

Say what the constraints *are*, what they *forbid*, and what they *require*. Be
precise. If the user named a formalism (e.g., "metriplectic split", "MVC",
"stateless microservice"), treat it as an axiom — do not question it, do not
weaken it, do not work around it.

#### Step 2: Validate the Logical Bridge

Evaluate the user's deduction connecting constraints to the current problem. Three
possible outcomes:

- **Confirmed** — The deduction holds. Say so explicitly and proceed.
- **Refined** — The deduction is directionally correct but needs tightening. State
  exactly what's imprecise and offer the corrected version.
- **Challenged** — The deduction doesn't follow from the stated constraints. This
  is rare if the user knows their domain — approach with curiosity, not skepticism.
  Explain the specific logical gap, and ask whether there's an unstated constraint
  that would close it.

#### Step 3: Architectural Analysis Before Implementation

This is the critical step that GAP exists to enforce. Before writing ANY code:

1. **Map the affected territory** — Which modules, functions, data flows, or
   derivation steps are touched by this change?
2. **Identify constraint boundaries** — Where exactly do the named constraints
   create separation lines in the codebase?
3. **Design the architecture** — Propose the structural change as a design, not
   as code. Use plain language: "Module A should own X, Module B should own Y,
   and the interface between them should enforce Z."
4. **Check for constraint violations** — Walk through the proposed design and
   verify it doesn't violate any of the named axioms, even at edge cases.

Only after this analysis is complete and the user has a chance to respond should
you write implementation code.

#### Step 4: Implement with Constraint Annotations

When you do write code, annotate the constraint-critical sections. The user should
be able to see *which* constraint each architectural decision serves. This doesn't
mean verbose comments everywhere — it means that at the key structural boundaries,
the connection between code and constraint is explicit.

### Anti-Patterns (What NOT to Do)

- **Don't skip to code.** The whole point of GAP is that architectural reasoning
  precedes implementation. If you find yourself writing code before completing
  Step 3, stop and back up.
- **Don't weaken constraints.** If the user says "this must be stateless," don't
  propose a solution that sneaks in state through a back door. Constraints are
  axioms, not suggestions.
- **Don't apologize and patch.** GAP exists specifically to prevent the "sorry,
  let me fix that" → immediate code dump cycle. Analyze first.
- **Don't flatten the user's framework.** If they're working in a specialized
  domain (physics, formal methods, etc.), their constraint vocabulary carries
  precise meaning. Don't rephrase it into generic terms.

---

## Mode B: Helping Craft a GAP Prompt

### Recognition Signals

Activate this mode when the user:
- Explicitly asks for help writing a prompt for an AI agent
- Is frustrated that an AI agent isn't respecting their constraints
- Says things like "how do I get it to understand my architecture"
- Mentions "GAP" or "guided autonomy" and wants to construct one
- Asks for a prompt template or strategy for communicating with AI agents

### Crafting Protocol

#### Step 1: Identify the Domain

Determine which template variant to use. Read the appropriate reference file:

- **Physics / Theoretical / Formal Methods** — `references/template_physics.md`
  Use when: the constraints are mathematical axioms, formal derivation rules,
  physical laws, or theoretical frameworks
- **General Software** — `references/template_general.md`
  Use when: the constraints are design patterns, business logic, API contracts,
  architectural boundaries, or system requirements

If the domain is ambiguous, ask. The templates are structurally identical but
use different vocabulary that matters for activating the right reasoning mode
in the target agent.

#### Step 2: Extract the Four Components

Help the user identify and articulate:

1. **The friction point** — What's going wrong? What does the agent keep
   breaking or misunderstanding?
2. **The hard constraints** — What rules must the system obey? These should be
   expressible as formal statements, not vague preferences. Help the user
   sharpen vague constraints into precise ones.
3. **The logical bridge** — How do the constraints connect to the current
   problem? This is often the hardest part for the user to articulate.
   Help them find the deductive link.
4. **The architectural question** — What should the agent design? Frame this
   as an open question that gives the agent room to reason, not a disguised
   instruction.

#### Step 3: Assemble and Refine

Combine the four components into a complete GAP prompt using the appropriate
template. Then review it for:

- **Constraint precision** — Are the hard rules actually hard? Or are they
  stated loosely enough that the agent could wriggle around them?
- **Bridge validity** — Does the logical connection actually follow from the
  constraints? If it's a leap, the agent will struggle.
- **Architectural openness** — Is the final question genuinely open? Or does
  it smuggle in a specific implementation? The whole point is to let the
  agent's reasoning engine work.

#### Step 4: Deliver the Prompt

Output the assembled GAP prompt as a clean, copy-paste-ready markdown block.
If the user wants it saved as a file, create a `.md` file in outputs.

---

## Why GAP Works (Mechanism)

Understanding the mechanism helps both modes work better:

**Attention anchoring** — When you explicitly name a formalism or design pattern
in a prompt, you force the LLM's attention mechanism to retrieve and hold those
specific rules in working memory while generating code. Generic descriptions
("make it clean") don't create this anchoring effect. Specific names do.

**Chain-of-thought activation** — An open architectural question ("how should we
architect...") triggers multi-step reasoning. A direct instruction ("change X to Y")
triggers pattern-matching and immediate execution. The reasoning path produces
better code because it considers the full system context.

**Yes-man bypass** — Direct instructions activate the compliance pathway. The
agent tries to satisfy the literal request, even if it violates system invariants.
Framing the request as a collaborative architectural question activates the
analytical pathway instead, where the agent evaluates feasibility and consistency
before proposing a solution.

---

## Quick Reference: The 4-Part Structure

| Part | Purpose | Key Phrase |
|------|---------|-----------|
| 1. Collaborative Observation | Frame as joint analysis, not an order | "I was thinking about..." |
| 2. System Constraints | State the hard rules (axioms, patterns, boundaries) | "Based on our rules for..." |
| 3. Logical Bridge | Connect constraints to the current problem | "If that's the case, wouldn't..." |
| 4. Open Architectural Question | Hand the design problem to the agent | "How should we architect..." |
