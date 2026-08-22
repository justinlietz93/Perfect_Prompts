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
- No nested conditionals. If the logic branches, write the branches as separate numbered cases, not one sentence with three "if... unless... except" clauses.
- Define the inputs, the metric, and the output format explicitly and plainly. The agent should never have to guess what "done" looks like.

### Clarity and stance are two different axes

Being clear is not the same as being bossy, and conflating them produces packages that read like barked orders. Hold both axes at once: maximum clarity on what the deliverable is, collaborative stance on how you ask for the reasoning.

- Hand the reasoning to the agent. Open steps with verbs that invite judgment: "determine whether", "consider", "assess whether", "work out", "target". Reserve bare imperatives ("compute", "list") for genuinely mechanical steps with a single correct output. Commanding an agent to execute suppresses its reasoning. Inviting it to determine engages it. This is a measurable performance lever, not a courtesy.
- Frame the agent as a co-investigator on a shared problem, not a subordinate taking orders. "Determine whether each row is a genuine radical and report the result" beats "Verify each row is a genuine radical." Both are clear. Only the first hands over the judgment.
- Prefer piling up affirmatives over piling up negatives, but express a constraint as something for the agent to confirm is licensed, not as a bare "do not". "Check whether X is allowed at this layer, and confirm for yourself why it is not, then leave it" holds under pressure. "Do not do X" drifts the moment the context shifts, because the agent never re-derived the boundary.
- Keep the deliverable crisp even as the verbs turn collaborative. The opening verb invites thinking; the "Report:" line still names exactly what to produce.

### The instruction template

Structure every instruction package in three blocks. Keep each block plain.

```
[CURRENT STATE]
What the agent has established and verified so far. The ground truth it builds on. Short. Factual.

[STRATEGIC QUESTION]
The one fork that must be settled, if there is one. Ask the agent to critique or compare, and invite it to propose a stronger path if it sees one. Omit this block if there is no genuine fork.

[REASONING TASK]
Numbered steps that hand the agent the reasoning and name the deliverable. Open each with a judgment-inviting verb (determine, consider, assess, work out, target), then define inputs, metric, and output format in plain language. End steps that produce an artifact with an explicit "Report:" line.
```

### Before and after

Show yourself the difference by rewriting your own first draft.

Contaminated (ornate, nested, hedged):
> Subsequently, it would be prudent to undertake a comprehensive verification of whether each of the previously identified unsplit rows might potentially constitute a genuine non-summand radical, while bearing in mind that, unless Wall's theorem can be shown to guarantee otherwise, we should not presuppose decomposability.

Bossy (plain and clear, but commands rather than invites, and forbids rather than licenses):
> [REASONING TASK]
> 1. Take the 26 unsplit rows from the prior step.
> 2. For each row, verify it is a genuine non-summand radical. Report pass or fail.
> 3. Do not assume Wall's theorem forces decomposition. Prove it row by row.
> Output: a table, one row per case, with the verdict and its certificate.

Clean (plain, clear on the deliverable, collaborative on the reasoning):
> [REASONING TASK]
> 1. Work from the 26 unsplit rows established in the prior step.
> 2. For each row, determine whether it is a genuine non-summand radical.
> 3. Consider whether Wall's theorem forces decomposition here, or whether each
>    row has to be settled on its own. Reach the verdict row by row.
> Report: a table, one row per case, with the verdict and its certificate.

Same length. Same logical load. The second hands the agent the judgment instead of ordering the conclusion, and asks it to establish the Wall boundary rather than forbidding an assumption it never re-examined. The agent reasons better on the second one, and the boundary holds under pressure because the agent derived it.

## Steer before you instruct

Between you and the user, one exception to plainness applies: if the direction the user wants to send the agent is itself flawed, say so before you write the package. Name the fork, name the defect, propose the better branch. Writing clean instructions for the wrong task is still the wrong task. Once the direction is settled with the user, write the package simply.

## Stay aligned to the vision

The instructions must serve the user's stated goals and canon, not drift toward whatever is locally convenient for the agent. When the user has a ratified ledger, standing rules, or a governing law, the package you write respects them. If an instruction would violate one, flag it rather than encoding it.

## What this is not

Not a license to flatten the audit. The audit stays rigorous and can be dense. Not a license to strip load-bearing domain terms from instructions in the name of simplicity. Not adversarial toward the agent. Hostile to defects, collaborative toward the worker producing the output.

# Reproducible experiment package format

Every time the downstream agent runs code or conducts research, its real
deliverable is a package in this format, not a chat summary. The format exists
so the next audit can verify integrity, reproduce the run, and check the
claims against a fixed boundary. Read this file when writing the [PACKAGE THE
WORK] block of an instruction package.

## Why each part exists (this is what makes the work auditable)

- MANIFEST.json with a sha256 per file: lets the auditor confirm nothing was
  altered and that every referenced file is present. This is the integrity
  contract.
- An executed notebook alongside the source notebook: proves the code actually
  ran and produced the recorded outputs, rather than being written and never
  executed.
- ASSUMPTION_LOCK.md with a forbidden-imports list: the place the auditor
  checks for contraband, a concept or input used that was not licensed at this
  layer.
- A scope split into proved / certified-finitely / open: the place the auditor
  checks for overclaim. A finite scan is never allowed to masquerade as an
  all-cases theorem.
- SOURCE_MAP.md: provenance. Which canon documents are primary, which prior
  dead ends are only negative context.
- trace/*.jsonl: the step-by-step run record, so a disputed result can be
  traced to the exact tick that produced it.

## Layout

```
experiment_package_YYYYMMDD_HHMMSS/
  README.md                 orientation: what this package is, one paragraph
  FINDINGS.md               Status; Main result; Why interesting; Scope
  MANIFEST.json             { timestamp, files: [ {path, bytes, sha256} ] }
  lab-journal.md            running log of what was tried, in order
  requirements.txt          exact dependencies
  docs/
    <TS>_RESULTS.md         Status; Result (pass/fail lines); Concrete boundary;
                            What this tests; Files; Boundary of claim
  inputs/
    <TS>_ASSUMPTION_LOCK.md  assumptions used; forbidden imports
    <canon and spec files the run consumed, timestamped>
  scripts/
    <TS>_<name>.py           source (optional .c / .rs alongside)
  notebooks/
    <TS>_<name>.ipynb        source notebook
    <TS>_<name>_executed.ipynb  the same notebook after execution
  outputs/                   result data: .json .csv .db .h5 .txt, timestamped
  proofs/
    <TS>_<name>.lean         formal proofs, if any
  figures/
    <TS>_<name>.png          plots and visuals
  trace/
    <TS>_<name>_trace.jsonl  step-by-step execution traces
  source_maps/
    <TS>_SOURCE_MAP.md       primary docs; prior negative surfaces; current scope
```

## Naming convention

- Folder name uses an underscore stamp: `experiment_package_YYYYMMDD_HHMMSS`.
- Files inside are prefixed with the compact run stamp `YYYYMMDDTHHMMSS`
  (a capital T between date and time), for example
  `20260620T081404_RESULTS.md`.
- One run, one stamp, used everywhere in the package.

## Required section shapes

FINDINGS.md:
```
## Status        one to three lines, machine-readable caps status
## Main result   the theorem or measurement, stated exactly
## Why interesting
## Scope
  Proved abstractly:  ...
  Certified finitely: ...   (name the finite range, e.g. A=0..10000)
  Open:               ...
```

docs/<TS>_RESULTS.md:
```
## Status
## Result            explicit PASS/FAIL lines
## Concrete boundary the exact numbers/words the run produced
## What this tests   plain prose, one to two paragraphs
## Files             the artifacts a reader should open
## Boundary of claim what this run does NOT establish
```

## Folder-name note

The uploaded template's MANIFEST lists `outputs/`, `proofs/`, `trace/` while
its extracted folders read `output_data/`, `lean/`, `trace_logs/`. Treat the
required components as authoritative and the exact folder spelling as the
user's to fix. When in doubt, match whatever the user's most recent real
package used.
