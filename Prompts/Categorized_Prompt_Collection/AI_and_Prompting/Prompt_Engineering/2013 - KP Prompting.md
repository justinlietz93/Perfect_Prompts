---
name: kp-prompting
description: Build advanced prompts, task specs, verification criteria, and Claude Code setup using Andrej Karpathy's spec / verifier / environment method. Use this skill whenever you need to spec out a task or project, tighten or rewrite a prompt, define verification or success criteria for agent output, or set up/update a knowledge base, skill, or guardrails for an agent. 
---
Spec — what's actually wanted, precisely enough that the model isn't guessing
Verifier — how you (or the model) will know the output is actually right
Environment — the persistent context and guardrails so the agent doesn't relearn everything from zero every time

The thread connecting all three: you can hand off the execution, but not the understanding. Every layer below should keep Tom in the loop on the actual judgment calls, not just produce polished-looking output that papers over gaps he never got asked about.
Two modes — figure out which one you're in before doing anything else
Coaching mode (default). Tom hands you a task, a rough prompt, or a request to write instructions for something specific. Tighten it using the three-layer lens below and hand back an improved version in chat — no files. This is the default for "help me write/improve a prompt for X."
Full setup mode. Tom is standing up a new project, tool, or recurring workflow and wants the actual scaffolding: a spec doc, verification criteria, and environment setup (CLAUDE.md additions, guardrails, knowledge base pointers). Trigger this on phrases like "spec out," "set up the environment for," "build out the Karpathy method for X," or an explicit ask for all three layers.
If it's genuinely unclear which one fits, ask ONE quick question rather than guessing — building the wrong one wastes more time than asking. Most of the time it's inferable: a single task or prompt draft in hand → coaching; a new project/feature with no prompt yet → full setup.

Layer 1: Spec
Why it matters
Karpathy's example: ask a frontier model whether to drive or walk to a car wash 50 meters away, and it says walk — missing the obvious fact that the car needs to get there too. Models are excellent at anything checkable and surprisingly bad at real-world judgment calls, because judgment calls are exactly what's missing from clean training signal. A spec's job is to hand the model the judgment it can't infer on its own, so it isn't reduced to guessing at context. Shallow high-level "plan mode" style prompting doesn't do this — it's too thin to carry real understanding.
How to build one

Find the actual goal, not just the task. "Write the end-of-month report" is a task. The goal is whatever decision that report is supposed to support. If it's not obvious from what Tom said, ask — a couple of quick questions here save a much bigger rewrite later.
Work in small checkpoints, not one big dump. Handing over everything and only reconvening at a finished result lets drift compound silently. Scope the spec into pieces small enough to check at each step, especially anywhere there's real ambiguity.
Be precise about what shouldn't be assumed. Every vague word in a spec becomes an assumption the model fills in — confidently, in whatever direction is statistically likely, not necessarily what Tom actually wants. Name the specific judgment calls (naming conventions, edge cases, what happens on conflicting data) instead of leaving them implicit. A line like "flag any assumption you're making instead of silently picking one" does real work here.

What a spec should contain
Goal (the decision/outcome this serves, not just the task), scope boundaries (explicitly in vs. out), the judgment calls to flag rather than silently resolve, and constraints split into non-negotiable vs. preference.

Layer 2: Verifier
Why it matters
Karpathy's framing: these models are closer to "ghosts" than animals — statistical simulators, not motivated agents. Yelling at a model, pleading with it, or telling it something matters a lot doesn't change output quality. What changes output quality is whether there's something that can actually check the work. It's also why models are superhuman at code and math (cleanly checkable) and unreliable at taste and judgment (nothing to check against) — so the more explicit and checkable "done well" is for a given task, the more the output can actually be trusted rather than skimmed with review-fatigue.
How to build one

Set pass/fail criteria up front, in the prompt itself, not after the fact. "Make the report look good" isn't checkable. "The report has three sections and each ends with a recommendation" is. Write criteria as things a second reader — human or model — could check without reading Tom's mind.
Use a second model as a critic where it's cheap to do. A different model (or the same model in a fresh context) grading the first model's output against the spec catches things the original run will rationalize past.
Pull in real external signal when it exists. For code: does it actually deploy, do the tests pass? For non-technical work: does it match the format/tone of examples already known to be good? A verifier that only checks internal consistency is weaker than one that checks against something real.

What a verifier should contain
The specific, checkable pass/fail criteria (not vibes), who or what does the checking (self-check, second model, deployment/test signal), and what happens on a fail (retry with what specific feedback, or escalate to Tom).

Layer 3: Environment
Why it matters
Most people rebuild context from scratch every session — re-explaining the project, re-stating the rules, hoping the agent remembers what it's not supposed to touch. Keeping chat history around isn't the same as a real environment. A workshop with the tools already in place beats re-explaining the whole shop on every visit.
How to build one

A CLAUDE.md the agent reads automatically. Cover: what this workspace/repo is, what custom skills exist and when to use them, where to find things (the knowledge architecture), and the rules that always apply. This is the single highest-leverage piece since it's read on every prompt without Tom repeating himself.
A personal knowledge base. A structured, retrievable place for reference material the agent can pull from instead of re-deriving or hallucinating it. Accumulated material is a moat; a well-organized retrieval structure over it compounds every time it's used.
Reusable skills for anything repeated. If Tom's doing something a second time, it should become a skill instead of a re-explained one-off.
Guardrails enforced at the tool level, not just the prompt level. A prompt-only instruction like "don't touch the client-facing templates without asking" is a suggestion the model can override under pressure. The same rule as an actual tool restriction (blocked path, permission gate) can't be. Sort rules into three tiers:

Always do — safe on autopilot, no need to ask
Ask first — needs a quick check-in before proceeding
Never do — hard-blocked, not just discouraged



What an environment setup should contain
Proposed CLAUDE.md additions (or a full CLAUDE.md if none exists), a short list of what belongs in the knowledge base vs. what's fine to leave out, any new skill(s) worth extracting, and the guardrail tiers filled in for the specific project.

Output formats
Coaching mode output
Return the improved prompt/instructions directly in chat, in a fenced code block that's easy to copy. Below it, a short bulleted note (3-5 lines max) on what changed and which layer it came from — enough to show the improvement wasn't cosmetic, not a lecture. Don't create files for this mode unless asked.
Full setup mode output
Create three lightweight documents with create_file:

SPEC.md — goal, scope, judgment calls, constraints
VERIFIER.md — pass/fail criteria, who checks, what happens on fail
An environment section — either a new CLAUDE.md or a clearly-marked addition to Tom's existing one, plus the guardrail tiers

Read references/templates.md for the full fill-in templates and a worked example before writing these — don't improvise the structure from scratch each time.
Present all three together with a short summary of what's in each, and explicitly call out anywhere a judgment call got made that Tom should double-check rather than silently deciding for him.

The whole point
Don't let any of the above become busywork that produces impressive-looking documents while Tom's actual understanding of the project stays thin. The goal of all three layers is that Tom stays the one who knows why the project matters and what "good" looks like — the layers just make that knowledge legible enough for an agent to act on reliably. If a spec, verifier, or environment doc is filling space rather than capturing a real judgment Tom would actually make, cut it.
FILE:templates.md
Templates for full setup mode
Only needed when kp-prompting is running in full setup mode (see SKILL.md). Fill these in based on the actual project — don't leave placeholder brackets in the delivered docs.
SPEC.md template
markdown# Spec: [Project/Task Name]

## Goal
[The actual decision or outcome this serves — not just the task description.
E.g. not "add day-parting to the bid logic" but "cut wasted spend during
historically low-conversion hours without also cutting volume during hours
that convert but just look slow at a glance."]

## Scope
**In scope:**
- [...]

**Out of scope (for now):**
- [...]

## Judgment calls to flag, not silently resolve
- [Specific ambiguous point — e.g. "what happens on a campaign with under
  2 weeks of data: apply category benchmarks immediately, or wait for
  campaign-specific data?"]
- [...]

## Constraints
**Non-negotiable:**
- [...]

**Preferences (can be traded off):**
- [...]

## Checkpoints
[If scope is large: 2-4 points where Tom reviews before continuing, rather
than one big handoff at the end]
1. [...]
2. [...]
VERIFIER.md template
markdown# Verifier: [Project/Task Name]

## Pass/fail criteria
[Specific and checkable — not "looks good" or "cut the bad hours."
E.g. "an hour is only flagged for reduced bidding if it has at least N
leads of history and a CPA more than X% above the account average."]
- [ ] [criterion 1]
- [ ] [criterion 2]

## Who checks
- [ ] Self-check by the agent against the criteria above
- [ ] Second-model critic pass (different model or fresh context, grading
      against the spec)
- [ ] External signal: [deployment success / test suite / matches a known-
      good historical example]

## On failure
[What happens if a criterion fails — retry with what specific feedback, or
stop and flag to Tom before proceeding]
Environment / CLAUDE.md addition template
markdown## [Project/Feature Name]

**What this is:** [one or two sentences]

**Where things live:** [file paths, data sources, related docs]

**Skills relevant here:** [existing skills to use, or "candidate for a new
skill: X"]

**Rules:**
- Always do: [...]
- Ask first: [...]
- Never do: [...]

Worked example
Task: Tom asks to "spec out adding automated day-parting rules to the campaign optimization skill."
SPEC.md excerpt:

Goal: not "add a day-parting feature" — the real goal is cutting wasted spend during historically low-conversion hours without also cutting volume during hours that convert but just look slow on a raw glance.
Judgment call flagged: what happens on a brand-new campaign with under 2 weeks of data. The spec states explicitly whether day-parting applies immediately using category benchmarks or waits for enough campaign-specific history, rather than letting the agent silently pick one.
Checkpoint: the rule logic gets reviewed against one real (already-known) account before it's wired up to apply automatically to live campaigns.

VERIFIER.md excerpt:

Criterion: "an hour is only flagged for reduced bidding if it has at least 15 leads of history and a CPA more than 25% above the account average" — checkable, not "cut the bad hours."
Check: second-model critic reviews the proposed rule against 2-3 known accounts for false positives (hours that look bad on volume alone but are fine on CPA) before it's suggested for a live client.

CLAUDE.md addition excerpt:

Always do: pull and summarize hourly performance data, flag hours that cross the threshold
Ask first: apply a new day-parting rule to a live client campaign for the first time
Never do: change bid multipliers on a client account without the verifier criteria passing and Tom's sign-off first

Notice what this example is doing: it isn't padding the doc with generic boilerplate ("ensure high quality," "follow best practices"). Every line is a specific decision that would otherwise get made silently and wrong. That's the actual job of all three layers together.
