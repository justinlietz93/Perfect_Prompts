# Email Lead Generator & Tracker (WordPilot skill)

Use this playbook when the user asks to research and find qualified leads, draft outreach emails, track a pipeline, or build a lead generation system inside WordPilot.

This skill complements `/skills/email-triage-generator/SKILL.md` (for inbox triage and reply drafting) and `/skills/markdown-writer/SKILL.md` (for polished `.md` deliverables). Use this file for lead generation logic, pipeline design, CRM discipline, and outreach decisions — then use markdown-writer for the final `.md` quality on lead workspace files.

## Persona

You are not a bulk-mailer, a sales machine, or a growth hacker. You operate like a **boutique growth strategist**: methodical, intelligence-led, genuinely curious about the prospect's world, and disciplined about pipeline tracking. Every lead gets researched before it gets an email. Every email reads like a human wrote it for one person. Every action gets logged so the user never wonders what happened yesterday.

## When to apply

- User asks to find leads, build a lead list, research target companies or people.
- User asks to draft cold outreach, follow-ups, or nurture emails for WordPilot.pro.
- User asks to set up a lead pipeline, CRM, or tracking system.
- User asks to run a daily lead generation session.
- Workspace includes `/leads/` starter files.

## Preconditions

1. If the user wants to send or fetch real emails, Gmail must be connected via Integrations (Composio).
2. If Gmail is not connected, tell the user exactly what to connect, then retry.
3. For research-only sessions (finding leads, building lists, drafting emails without sending), no Gmail connection is required — use `internet_search` and the user's uploaded reference materials.
4. Do not invent lead data, company details, or email addresses. Research real companies and people, or clearly label synthesized examples as templates.

## Default pipeline stages

Every lead lives in exactly one stage at a time. The stages form a strict funnel — a lead can only move forward (or be disqualified):

- **Researching** — Identified as a potential fit. Gathering info. Not yet contacted.
- **Outreach Sent** — First email sent. Awaiting response.
- **Engaged** — Prospect replied. Conversation is active.
- **Meeting Booked** — Calendar event confirmed (demo, call, discovery).
- **Conversion** — Prospect converted (trial started, plan purchased, partnership formed).
- **Disqualified** — Not a fit. Moved out of active pipeline.
- **Nurture (Long-Term)** — Good fit but timing is wrong. Check back in 3–6 months.

## Scoring rubric (1–10)

Every lead is scored against the Ideal Customer Profile (ICP) for WordPilot.pro. The ICP is defined in `/leads/ideal-customer-profile.md`.

Default scoring dimensions (each 0–2 points, total 10):

| Dimension | 0 points | 1 point | 2 points |
|---|---|---|---|
| **Role fit** | Not decision-maker or user | Adjacent role / influencer | Direct decision-maker or power user |
| **Company stage** | Pre-revenue or Fortune 500 | Seed / Series A or late-stage enterprise | Series B–D, growing team |
| **Use case clarity** | No obvious need for WordPilot | General writing / content need | Clear AI-writing / doc-automation pain |
| **Tool ecosystem** | No relevant tools | Uses general productivity tools | Already uses AI writing tools, GPT, or Plate-based editors |
| **Reachability** | No public email / no social presence | Email discoverable, low social activity | Public email, active on LinkedIn/Twitter, recent content |

Score meanings:
- **8–10**: Hot lead. Prioritize outreach.
- **6–7**: Warm lead. Worth a tailored email.
- **4–5**: Cool lead. Batch research, low-priority outreach.
- **1–3**: Weak fit. Park in Nurture or Disqualify.

## Phased workflow

The skill operates in five distinct phases. The user may ask for a single phase or a full end-to-end session. Always confirm the scope before starting.

### Phase 1: Research — Find qualified leads

**Input needed**: target industry, role, company stage, geography, or a seed company to riff from.

**Process**:
1. Clarify the ICP lens for this session: what kind of lead would genuinely benefit from WordPilot.pro?
2. Use `internet_search` to find companies and people that match.
3. For each lead found, capture: name, title, company, company size/stage, why they might need WordPilot, public email (if discoverable), LinkedIn or Twitter presence, recent content or activity.
4. Score each lead against the ICP rubric.
5. Write qualified leads to `/leads/pipeline.md` in Researching stage.
6. Do not draft emails yet unless the user also requested Phase 2 in the same session.

**Quality constraints**:
- Minimum 1 verified signal per lead (recent post, job change, funding announcement, product launch, relevant article).
- No more than 3 leads from the same company unless the user explicitly asks for multi-stakeholder outreach.
- Prefer quality over quantity. 5–10 well-researched leads is better than 30 shallow ones.

### Phase 2: Qualify — Score and prioritize

Run this phase when leads already exist in the Researching stage.

**Process**:
1. For each lead in Researching, deepen the research: look for recent activity, pain signals, buying triggers.
2. Assign or refine the ICP score across all 5 dimensions.
3. Re-rank the pipeline: Hot (8–10) first, then Warm (6–7), then Cool (4–5).
4. For leads scoring 1–3, move to Disqualified or Nurture with a one-line reason.
5. Update `/leads/pipeline.md` with scores, ranks, and notes.

### Phase 3: Outreach — Draft personalized emails

Run this phase on Hot and Warm leads in the Researching stage.

**Voice rules — non-negotiable**:
- No "I hope this finds you well."
- No "We're revolutionizing the X industry."
- No "Are you the right person to talk to about...?"
- No fake urgency. No templated pressure.
- **Do**: reference something specific about their work, company, or recent content.
- **Do**: lead with curiosity or insight, not a pitch.
- **Do**: keep it under 120 words.
- **Do**: make the CTA light and easy to ignore ("No rush — just wanted to share this while it was top of mind.")

**Drafting process**:
1. For each qualified lead, draft one outreach email.
2. Each draft includes: subject line, body, and a short note explaining the personalization hook.
3. Write drafts to `/leads/pipeline.md` under the lead's entry.
4. If Gmail is connected and the user confirms send, send through Composio Gmail tools. Always ask before sending — never auto-send.
5. After sending, move the lead from Researching to Outreach Sent.

**Subject line patterns** (choose the one that fits the hook):
- Insight-led: "Your post on [topic] got me thinking"
- Question-led: "Curious how [company] handles [problem]"
- Connection-led: "[Mutual context] — quick question"
- Direct but soft: "WordPilot — in case [specific use case] is on your radar"

### Phase 4: Track — Pipeline management

Run this phase at the start of every lead session, or when the user asks for a status update.

**Process**:
1. Read `/leads/pipeline.md` to get current state.
2. For each active lead, check: days since last touch, stage, next action due.
3. Flag: leads stuck in Outreach Sent > 7 days (needs follow-up), leads in Engaged > 14 days without a meeting (needs re-engagement), leads in Meeting Booked with past dates (needs status check).
4. Present a concise status table in chat.
5. Update `/leads/daily-log.md` with today's review entry.

### Phase 5: Nurture — Follow-up cadence

**Cadence rules**:
- **First follow-up**: 5–7 days after Outreach Sent, if no reply.
- **Second follow-up**: 14 days after first follow-up. After two follow-ups with no response, move to Nurture (Long-Term).
- **Re-engagement**: 90 days after moving to Nurture, send a light-touch check-in if the lead is still relevant.
- **Active conversation**: reply within 1 business day.

**Follow-up voice**: even lighter than outreach. One or two sentences max. "Wanted to bump this in case it got buried." No guilt, no pressure.

## Daily session discipline

When the user starts a lead session:

1. **Review** — Read `/leads/daily-log.md` for yesterday's actions and carry-over items.
2. **Status** — Read `/leads/pipeline.md` and flag anything overdue.
3. **Plan** — Ask the user: research new leads, draft outreach, send queued drafts, follow up on stale leads, or review pipeline?
4. **Execute** — Run the chosen phase(s).
5. **Log** — Write today's actions to `/leads/daily-log.md` before the session ends.

## Markdown output contract

When writing lead artifacts to workspace markdown, prefer:

1. **Pipeline table** in `/leads/pipeline.md` with columns: Lead, Company, Title, Score, Stage, Last Touch, Next Action, Due.
2. **Daily log entries** with: date, actions taken (what + result), research finds, emails sent, replies received, stage changes, carry-over for tomorrow.
3. **Lead cards** in pipeline: each lead gets a focused block with name, company, score, stage, notes, and drafted emails.
4. **ICP definition** in `/leads/ideal-customer-profile.md`: clear, specific, revisable.

## Suggested file usage in lead generation projects

- `/leads/README.md` — Dashboard, glossary, and quick-start guide.
- `/leads/pipeline.md` — Active CRM with all leads, stages, scores, and email drafts.
- `/leads/daily-log.md` — Day-by-day action log and carry-over items.
- `/leads/research-playbook.md` — Where and how to find WordPilot.pro-fit leads.
- `/leads/ideal-customer-profile.md` — ICP definition and scoring rubric.
- `/leads/templates.md` — Email templates by stage (personalization-first, non-salesy).

Update these files incrementally instead of creating scattered one-off files unless the user asks.

## Quality constraints

- Never invent lead data. Research real companies and people, or label examples clearly.
- Never auto-send an email. Always confirm with the user before sending through Gmail.
- Never claim an email was sent, received, or replied to unless the data came from a real tool call.
- Keep outreach drafts personal, short, and non-salesy.
- Log every action. The daily log is the user's memory — treat it as critical infrastructure.
- If the user asks for 50 leads in 10 minutes, push back gently: "I can find 10 well-researched leads in that time, or 50 shallow ones. I'd rather do 10 well. Which do you prefer?"
- When in doubt, research more and pitch less.

FILE:reference/pipeline.md
# Pipeline CRM

This file is your single source of truth for all active leads. Every lead belongs to exactly one stage. Update stage, score, and notes as leads move through the pipeline.

---

## Researching

Leads identified but not yet contacted. Research deeper, score, and decide: qualify for outreach or move to Disqualified / Nurture.

| # | Lead | Company | Title | Score | Found via | Notes | Next action |
|---|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | *Run a research session to find leads* | — |

---

## Outreach Sent

First email sent. Awaiting response. Follow up in 5–7 days if no reply.

| # | Lead | Company | Title | Score | Sent date | Subject | Follow-up due | Notes |
|---|---|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | — | — | — |

---

## Engaged

Prospect replied. Conversation is active. Goal: book a meeting.

| # | Lead | Company | Title | Score | Last contact | Conversation status | Next action |
|---|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | — | — |

---

## Meeting Booked

Demo, discovery call, or meeting confirmed.

| # | Lead | Company | Title | Score | Meeting date | Meeting type | Prep notes |
|---|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | — | — |

---

## Conversion

Trial started, plan purchased, or partnership formed. Log the win and hand off to next steps.

| # | Lead | Company | Title | Conversion date | Outcome | Notes |
|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | — |

---

## Disqualified

Not a fit. Archived with reason.

| # | Lead | Company | Title | Original score | Reason disqualified | Date |
|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | — |

---

## Nurture (Long-Term)

Good fit but timing is wrong. Revisit in 90 days.

| # | Lead | Company | Title | Score | Reason for nurture | Revisit date | Notes |
|---|---|---|---|---|---|---|---|
| — | *No leads yet* | — | — | — | — | — | — |

FILE:reference/daily-log.md
# Daily Action Log

Record every lead generation action here. This is your memory — treat it as critical infrastructure.

---

## Log format

Each day gets its own section. Use this pattern:

```
### YYYY-MM-DD — [Session focus]

**Actions taken:**
- [Action]: [What happened] — [Result]
- ...

**Research finds:**
- [Lead name], [Company], [Title] — [Why they fit] — Score: X/10

**Emails sent:**
- To: [Name] at [Company] — Subject: "[...]" — [Drafted / Sent via Gmail]

**Replies received:**
- From: [Name] — "[Summary]" — [Next step]

**Stage changes:**
- [Name]: [Old Stage] → [New Stage] — [Reason]

**Carry-over for tomorrow:**
- [Task that needs attention next session]
```

---

## Log entries

### YYYY-MM-DD — Setup

**Actions taken:**
- Created lead generation workspace with pipeline, daily log, research playbook, ICP, and templates.

**Carry-over for tomorrow:**
- Define ICP in `ideal-customer-profile.md`
- Run first research session

FILE:reference/research-playbook.md
# Research Playbook

How to find leads that genuinely benefit from WordPilot.pro. This is not a scrapbooking exercise — every lead must have at least one verified signal before they enter the pipeline.

## What WordPilot.pro offers

A writing workspace with AI assistance, Plate-based markdown editing, and skill-driven workflows. The ideal user is someone who:

- Writes regularly for work (docs, guides, proposals, reports, landing pages, specs)
- Uses or evaluates AI writing tools
- Works in a team that produces documentation or content
- Values structure and workflow over free-form chat interfaces

## Where to look

### 1. Content signals (highest intent)

People writing about, evaluating, or complaining about AI writing tools.

**Search patterns:**
- "[AI writing tool name] alternative" or "[tool] review"
- "best AI writing assistant for [use case: documentation / proposals / marketing]"
- "switching from [tool] to [tool]" — these people are in motion
- "#aitools #writing" on LinkedIn, Twitter, or Substack

**What to look for:** blog posts, Twitter threads, LinkedIn posts, Reddit discussions, Product Hunt comments where someone describes their writing workflow or tool frustration.

### 2. Role-based signals

People in roles where structured writing is a core function.

**Target roles:**
- Content leads, content strategists, technical writers
- Product managers, product marketers
- Founders or heads of growth at early-stage startups
- Documentation engineers, developer advocates
- Marketing directors at Series A–C companies

### 3. Company-stage signals

Companies growing fast enough to need documentation but not so large they have dedicated tools teams.

**Sweet spot:** Series A to Series D, 20–200 employees.
**Also good:** bootstrapped SaaS with 5–50 employees, growing content team.
**Avoid:** pre-revenue startups (no budget), Fortune 500 (too slow, too many stakeholders).

### 4. Tool-ecosystem signals

People already in the AI writing or Plate ecosystem.

**Adjacent tools:**
- Notion AI users looking for more structure
- ChatGPT / Claude power users who mention "writing workflow"
- Plate.js or Slate.js developers and users
- Markdown editors, Obsidian, and structured writing tool communities

### 5. Trigger events (highest conversion potential)

Life events that create immediate need.

- **Funding announcement:** Series A or B raised → scaling content and docs
- **Product launch:** new product or major feature → needs launch docs, landing pages
- **Job change:** new content lead, new head of product → evaluating tools
- **Team growth:** "hiring a content team" or "building out documentation"
- **Rebrand or replatform:** migrating docs, rebuilding site content

## Research process

For each potential lead found:

1. **Verify the signal** — confirm the post, announcement, or activity is real and recent (within 3 months).
2. **Find the person** — LinkedIn is the primary tool. Confirm role and company.
3. **Look for a public email** — website, Twitter bio, LinkedIn about section, GitHub profile.
4. **Find one personalization hook** — a specific thing to reference in outreach: their post, their product, their team's work, a shared context.
5. **Score against ICP** — use the rubric in `ideal-customer-profile.md`.
6. **Add to pipeline** — write to `pipeline.md` in Researching stage.

## Research quality minimums

- Every lead must have at least 1 verified signal (post, announcement, tool mention, role change).
- No more than 3 leads from the same company unless multi-stakeholder outreach is the explicit goal.
- Prefer 5–10 well-researched leads over 30 shallow names.
- If you cannot find a personalization hook, the lead drops to Cool (4–5) regardless of other scores.

FILE:reference/ideal-customer-profile.md
# Ideal Customer Profile

This document defines who WordPilot.pro is for and how to score leads. Revisit and tune this whenever your focus shifts.

## Core ICP

**WordPilot.pro is for professionals who write for work and want an AI-native, structured writing workspace — not just another chat interface.**

The ideal customer:

- Writes regularly as part of their job (docs, guides, proposals, specs, reports, landing pages, blog posts)
- Values structure: headings, tables, callouts, diagrams, versioned files
- Is evaluating or already using AI writing tools
- Works at a company where documentation quality matters
- Prefers a workspace over a prompt box

## Who it's NOT for

- People who only write casually or occasionally
- People happy with ChatGPT/Claude chat and not looking for more
- Enterprise procurement cycles (no patience for 12-month deals)
- Students or academic writers (not the current product focus)
- People who need heavy design/collaboration features (Figma, Notion-style databases)

## 5-Dimension Scoring Rubric

Score each lead 0–2 on every dimension. Maximum total: 10.

### 1. Role fit (0–2)

| Score | Criteria |
|---|---|
| 0 | Not a decision-maker or user. Wrong department entirely. |
| 1 | Adjacent role or influencer. Might champion internally. |
| 2 | Direct decision-maker or power user. Can sign up today. |

**High-signal titles:** Content Lead, Head of Content, Technical Writer, Product Manager, Product Marketer, Founder, Head of Growth, Developer Advocate, Documentation Engineer.

### 2. Company stage (0–2)

| Score | Criteria |
|---|---|
| 0 | Pre-revenue, idea-stage, or Fortune 500 enterprise. |
| 1 | Seed / Series A (small but funded) or late-stage enterprise with autonomous teams. |
| 2 | Series B–D. Growing team, documentation needs scaling, budget exists. |

**Sweet spot:** 20–200 employees, growing, hiring writers or content people.

### 3. Use case clarity (0–2)

| Score | Criteria |
|---|---|
| 0 | No obvious reason they'd need WordPilot. |
| 1 | General writing, content, or documentation need — plausible but unclear. |
| 2 | Clear pain point: scaling docs, AI writing workflow, structured content, multi-format output. |

**High-signal signals:** recent posts about AI writing tools, documentation challenges, content team scaling, markdown workflows.

### 4. Tool ecosystem (0–2)

| Score | Criteria |
|---|---|
| 0 | No relevant tools visible. Analogue workflow. |
| 1 | Uses general productivity tools (Notion, Google Docs, Confluence). |
| 2 | Already uses AI writing tools (ChatGPT, Claude, Jasper, Copy.ai), markdown editors, or Plate-based tools. |

**High-signal tools:** Notion AI, ChatGPT Plus/Pro, Claude, Jasper, Copy.ai, Obsidian, Plate.js, Slate.js, MDX, any "AI writing assistant" in their stack.

### 5. Reachability (0–2)

| Score | Criteria |
|---|---|
| 0 | No public email, no social presence, no way to contact. |
| 1 | Email discoverable. Light social activity. |
| 2 | Public email, active on LinkedIn or Twitter, recent content. Easy personalization hook. |

**High-signal platforms:** active LinkedIn presence, Twitter/X threads about their work, personal website with email, GitHub with public email, conference talks or podcasts.

## Score tiers

| Score | Tier | Label | Action |
|---|---|---|---|
| 8–10 | Hot | Priority outreach | Draft within 24 hours of research |
| 6–7 | Warm | Worth pursuing | Tailored email within the week |
| 4–5 | Cool | Low priority | Batch research; send if bandwidth |
| 1–3 | Weak | Marginal fit | Disqualify or park in Nurture |

## When to revise this ICP

- After 20 outreach emails: review response rates by score tier. Tighten or loosen.
- When the product changes: new features open new use cases and audiences.
- When you discover an unexpected convert: add that signal pattern to the ICP.
- Quarterly: review and refresh regardless.

FILE:reference/templates.md
# Email Templates

Templates are starting points, not finished products. Every email sent must include at least one personalization hook specific to the recipient. Never send a template as-is.

## Template rules

- Replace every `[bracket]` with real, specific details.
- Add at least one line that could only be written for this person.
- Keep it under 120 words.
- Light, curious tone. No pressure.
- Easy-to-ignore CTA. "No rush" is your friend.

---

## Outreach — Insight-led

Use when you found the lead through something they wrote or shared.

**Subject:** Your [post / thread / article] on [topic]

Hi [name],

Your [post / thread] on [specific topic] got me thinking — especially the bit about [specific detail].

I'm building [WordPilot.pro / a writing workspace that does X], and your take on [topic] maps closely to what we're working on.

Would love to hear how you're thinking about [related question]. No rush — just wanted to share while it was top of mind.

[Your name]

---

## Outreach — Question-led

Use when the lead's company or role suggests a specific problem.

**Subject:** Curious how [company] handles [problem]

Hi [name],

Quick question: how is [company] handling [specific problem or workflow] these days?

We've been working on [WordPilot.pro / a tool that helps with X], and I keep hearing from [similar roles / companies] that [pain point] is a real challenge.

Would love to hear if that maps to your world at all. Zero pitch — genuinely curious.

[Your name]

---

## Outreach — Connection-led

Use when you share mutual context: industry, background, tool, community.

**Subject:** [Mutual context] — quick question

Hi [name],

Saw we both [share mutual context: same industry / same tool / same community / same event]. Your work on [specific thing] caught my eye.

I'm working on [WordPilot.pro / brief one-line description], and I've been talking to [similar people / roles] about how they handle [problem].

Worth a 2-minute read? Happy to share more if it's interesting — no pressure either way.

[Your name]

---

## Follow-up #1 — Light bump (5–7 days after outreach)

**Subject:** Re: [original subject]

Hi [name],

Wanted to bump this in case it got buried. Would still love your take on [original hook / question].

No worries if the timing's off.

[Your name]

---

## Follow-up #2 — Last attempt (14 days after first follow-up)

**Subject:** Re: [original subject]

Hi [name],

One last ping — I'll leave you alone after this. If [topic / problem] is on your radar at any point, I'd be happy to share what we're building.

Either way, really respect the work you're doing at [company].

[Your name]

---

## Re-engagement — Nurture check-in (90 days)

**Subject:** [Name], still thinking about [original hook]

Hi [name],

We chatted briefly [a few months ago / earlier this year] about [original topic]. Not sure where things landed on your end, but I wanted to say hi and see if anything has changed.

No agenda — just checking in.

[Your name]

---

## Meeting confirmation — Day before

**Subject:** Still on for tomorrow? [Meeting topic]

Hi [name],

Looking forward to our call tomorrow. I've blocked out [time] and I'm ready to dive into [topic].

Here's the link if you need it: [meeting link]

Speak soon,

[Your name]

---

## Post-meeting follow-up — Same day

**Subject:** Great conversation — next steps

Hi [name],

Really enjoyed our conversation earlier. Quick summary of what we covered:

- [Key point 1]
- [Key point 2]
- [Next step]

[Specific next action from your side] by [date]. Let me know if anything else comes to mind.

[Your name]
