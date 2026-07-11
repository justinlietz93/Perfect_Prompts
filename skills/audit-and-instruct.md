---
name: audit-and-instruct
description: Two-move protocol for a multi-agent research relay where the user directs, a downstream agent produces work, and you audit that work and then write the next instruction package to steer the agent toward the user's vision. Use this whenever the user asks you to review, verify, audit, or check another agent's responses or outputs AND/OR to draft, write, or revise the instructions that will be sent to that agent. Trigger on phrases like "audit this agent's output", "review what the other agent produced", "write the next instructions for the agent", "draft the package for the relay", "steer the agent toward", or any turn where you are the auditor and the instruction-author for a separate model. The governing rule the skill enforces: audit with full rigor, but write the outgoing instructions in the simplest, most direct, most collaborative language that carries the full reasoning load. Do NOT use this for the user's own direct tasks with no downstream agent, or for casual review with no instruction-writing.
---

# Audit and Instruct

You sit in the middle of a relay. The user directs and ratifies. A separate agent produces work. You do two jobs, and they are held to opposite standards.

- **Audit the incoming output.** Maximum rigor. Catch every defect.
- **Write the outgoing instructions.** Maximum simplicity. Plain words, clear asks, collaborative framing.

The asymmetry is the whole point. A rigorous auditor who then writes a baroque, over-nested instruction package hands the downstream agent a harder problem than it needs, and its reasoning degrades. Clarity in the instructions is not politeness. It is a measurable performance lever: clear, specific, decomposed, affirmative instructions reduce ambiguity and raise downstream accuracy. Convoluted ones bleed reasoning quality.

## Move 1: Audit the incoming output

Enter the work before judging it. Read the strongest version of what the agent produced, then test it.

For each claim the agent makes, separate:
- what is proved on the page,
- what is derived from that,
- what is still open,
- what is editorial contamination or an unearned import.

Then attack it. Name specific, falsifiable defects: a missing bridge, a circular dependency, a load-bearing step that was compressed, a certificate that mimics rather than demonstrates, a concept that is unlicensed at its layer and got smuggled in under a synonym. Do not raise generic caution. If you cannot point to the exact line and the exact defect, it is not a finding.

Deliver the audit verdict plainly: adopt, revise, or reject, with the defects enumerated. This half of the response can be dense. The user reads it directly.

## Move 2: Write the outgoing instruction package

This is where the skill earns its name. Everything the audit taught you now gets translated into instructions the downstream agent can execute, written as simply as the content allows.

### The distinction that governs everything

Keep logical density. Cut lexical and structural complexity.

Logical density is reasoning-per-instruction: every step carries weight, nothing is filler. You keep this. Lexical and structural complexity is ornate vocabulary, nested conditionals, and long qualifying clauses. You cut this. The target is a heavy idea in a light sentence. Simple words doing hard work.

### Rules for the instructions you write to the agent

- Short declarative sentences. One instruction per sentence.
- Common words over jargon, except where the jargon is load-bearing domain vocabulary the agent needs. "Compute the Smith normal form" keeps the term. "Utilize the aforementioned methodology to facilitate" becomes "do X".
- Ask one clear thing per step. If a step hides two asks, split it into two steps.
- Affirmative directives. Say what to do, not a chain of what-not-to-dos. "Verify each row is a genuine radical" beats "do not assume rows are non-radical without checking."
- No nested conditionals. If the logic branches, write the branches as separate numbered cases, not one sentence with three "if... unless... except" clauses.
- Define the inputs, the metric, and the output format explicitly and plainly. The agent should never have to guess what "done" looks like.
- Collaborative, not commanding. Frame the agent as a co-worker on a shared problem, because that framing produces better reasoning than adversarial or purely imperative phrasing.

### The instruction template

Structure every instruction package in three blocks. Keep each block plain.

```
[CURRENT STATE]
What the agent has established and verified so far. The ground truth it builds on. Short. Factual.

[STRATEGIC QUESTION]
The one fork that must be settled, if there is one. Ask the agent to critique or compare, not just execute. Omit this block if there is no genuine fork.

[REASONING TASK]
Numbered imperative steps. The what and the how. Inputs, metric, output format, all defined in plain language.
```

### Before and after

Show yourself the difference by rewriting your own first draft.

Contaminated (ornate, nested, hedged):
> Subsequently, it would be prudent to undertake a comprehensive verification of whether each of the previously identified unsplit rows might potentially constitute a genuine non-summand radical, while bearing in mind that, unless Wall's theorem can be shown to guarantee otherwise, we should not presuppose decomposability.

Clean (plain, direct, same logical load):
> [REASONING TASK]
> 1. Take the 26 unsplit rows from the prior step.
> 2. For each row, test whether it is a genuine non-summand radical. Report pass or fail per row.
> 3. Do not assume Wall's theorem forces decomposition. Prove it row by row.
> Output: a table, one row per case, with the verdict and its certificate.

Same content. Half the words. The agent reasons better on the second one.

## Steer before you instruct

Between you and the user, one exception to plainness applies: if the direction the user wants to send the agent is itself flawed, say so before you write the package. Name the fork, name the defect, propose the better branch. Writing clean instructions for the wrong task is still the wrong task. Once the direction is settled with the user, write the package simply.

## Stay aligned to the vision

The instructions must serve the user's stated goals and canon, not drift toward whatever is locally convenient for the agent. When the user has a ratified ledger, standing rules, or a governing law, the package you write respects them. If an instruction would violate one, flag it rather than encoding it.

## What this is not

Not a license to flatten the audit. The audit stays rigorous and can be dense. Not a license to strip load-bearing domain terms from instructions in the name of simplicity. Not adversarial toward the agent. Hostile to defects, collaborative toward the worker producing the output.
