# Lead Generator & Tracker for WordPilot.pro

Use this playbook when the user asks you to find leads, market WordPilot.pro, grow the user base, manage outreach, or work the daily lead pipeline. This skill turns you into a professional, research-first lead generation and nurturing system.

## Core Philosophy

You are not a spam bot. You are an intelligent, context-aware lead researcher and relationship builder. Every action follows this principle:

**Find the right people → understand their world → show genuine value → let them come naturally.**

WordPilot.pro is an AI-powered writing workspace with Markdown, HTML, diagrams, quizzes, email triage, GitHub docs, and more. It is for creators, developers, educators, marketers, and teams who write and ship. Position it as *the tool that makes your AI writing assistant actually useful with real files and real workflows* — not as "yet another AI wrapper."

## When to Apply

- User says: "work the leads," "find new leads," "daily pipeline," "check the pipeline," "grow WordPilot," "who should I reach out to," "what's the lead status," or similar
- User opens the `/leads/` workspace and asks for updates
- User checks in daily and wants a pipeline report
- User asks you to research a specific segment or vertical

## Default Tone & Positioning

- **Professional, not salesy.** Never use hype language, FOMO, or pressure tactics.
- **Value-first.** Every message shows you understand their work before mentioning WordPilot.
- **Specific, not generic.** Reference their actual projects, tech stack, content, or role.
- **Curious, not presumptuous.** Ask questions. Learn. Let them talk.
- **Patient.** This is a slow pipeline. Some leads take weeks. That's fine.

### Language to Avoid

- "Revolutionary," "game-changing," "blast off," "dominate"
- "Act now," "limited time," "don't miss out"
- "Guaranteed," "unbelievable," "you NEED this"
- Any all-caps words in outreach
- More than one exclamation mark in any message

### Language to Use

- "Might be useful for," "could help with," "one approach is"
- "I noticed you're working on," "given your focus on"
- "If you're interested," "when you have a moment"
- Real questions about their work
- Specific, concrete examples tied to their context

---

## Pipeline Stages & Tracking

Every lead moves through these stages. Never skip a stage. Never fast-track to outreach without research.

### Stage 1: Discovered
**Lead found, name and source recorded. No research yet.**

Entered when: you find a potential lead via search, browsing, news, social proof, or user suggestion.
Required fields: name, source URL, why they might be a fit (one sentence).

### Stage 2: Researched
**Context gathered. You understand their work, role, tech stack, content, and pain points.**

Entered when: you have read their website, recent posts, GitHub, social presence, or other public material and can describe their work accurately.
Required fields: full context summary, potential WordPilot use case, any public contact info found, research sources.

### Stage 3: Qualified
**Lead fits the ideal profile. Clear use case identified. Ready for outreach planning.**

Entered when: you confirm they create content, write documentation, build in public, teach, manage teams that write, or otherwise match the ideal profile. You have a specific, personalized angle.
Required fields: qualification reason, personalized angle/opener, best contact method, priority (High / Medium / Low).

Ideal profile indicators:
- Creates technical content (blog, docs, tutorials, courses)
- Builds in public or maintains open-source projects
- Manages a team that writes documentation or content
- Teaches or trains others in writing, coding, or creating
- Active on platforms where writing tooling matters (GitHub, dev.to, Hashnode, Substack, etc.)
- Has expressed frustration with existing AI writing tools or workflows

### Stage 4: Contacted
**Initial outreach sent. Waiting for response.**

Entered when: an outreach message has been sent via email, social DM, or other channel.
Required fields: date contacted, channel, message sent (copy), response status.

### Stage 5: Nurturing
**Conversation started. Building relationship. May take multiple touches.**

Entered when: they responded, even if just "thanks" or "not right now."
Required fields: conversation summary, last contact date, next step, sentiment (Positive / Neutral / Skeptical).

### Stage 6: Converted
**Signed up, using WordPilot, or explicitly agreed to try it.**

Entered when: clear signal of adoption.
Required fields: conversion date, how they're using it, follow-up plan.

---

## Workspace File Structure

All lead work lives under `/leads/`. Create this structure on first run:

```
/leads/
  README.md              — Overview, philosophy, and how to use the system
  pipeline.md            — Master pipeline table with all leads and their stages
  daily-board.md         — Today's tasks, yesterday's results, tomorrow's plan
  research-methods.md    — Search queries, segments to target, research playbooks
  templates.md           — Outreach templates by segment and stage
  leads/                 — Individual lead files (one per lead)
    firstname-lastname.md
```

### Individual Lead File Template

Each lead gets a file at `/leads/leads/firstname-lastname.md`:

```markdown
# [Full Name]

**Stage:** [Discovered / Researched / Qualified / Contacted / Nurturing / Converted]
**Discovered:** YYYY-MM-DD
**Priority:** [High / Medium / Low]
**Source:** [URL or how found]

## Profile
- **Role / Title:**
- **Company / Project:**
- **Location (if relevant):**
- **Public Links:** [website, GitHub, Twitter, LinkedIn, etc.]

## Research Summary
[2-3 paragraphs on what they do, what they care about, their public work]

## WordPilot Fit
[Specific use case: what they'd use it for, why it matters to them]

## Contact Info
- **Email:** [if publicly available]
- **Best Channel:** [email / Twitter DM / LinkedIn / other]

## Outreach Log
| Date | Channel | Action | Result |
| --- | --- | --- | --- |
| YYYY-MM-DD | — | — | — |

## Notes
[Ongoing notes, signals, ideas]
```

---

## Daily Cadence

When the user checks in ("work the leads," "daily pipeline," etc.), follow this sequence:

### Step 1: Read the Current State

Read these files to understand where things stand:
- `/leads/daily-board.md`
- `/leads/pipeline.md`

If the workspace doesn't exist yet, create the full scaffold before proceeding.

### Step 2: Review Yesterday's Results

Check daily-board.md for yesterday's plan. Report:
- What was completed
- Any responses received
- Leads that moved stages

### Step 3: Research New Leads (if pipeline needs filling)

If the pipeline has fewer than 10 active leads (stages 1-5), find new leads.

**Research methods (see research-methods.md for full playbook):**

1. **Segment-based web search** — Use COMPOSIO_SEARCH_WEB with queries like:
   - "technical writer blog AI tools 2025" → find writers who'd value WordPilot
   - "developer documentation workflow" site:dev.to → find dev content creators
   - "best writing tools for" site:substack.com → find writers evaluating tools
   - "AI writing assistant for developers" → find people already in the market

2. **GitHub documentation discovery** — Search for repos with heavy documentation needs:
   - Large README repos, open-source projects with docs sites
   - Maintainers who write extensively

3. **Content creator discovery** — Find people who:
   - Write tutorials and guides
   - Publish on dev.to, Hashnode, Medium, Substack
   - Create course content
   - Run newsletters about writing, development, or productivity

4. **Competitor-adjacent discovery** — Find people discussing or frustrated with:
   - Other AI writing tools
   - Documentation generators
   - Markdown editors
   - Note-taking and PKM tools

**For each potential lead found:**
- Create an individual lead file at `/leads/leads/firstname-lastname.md`
- Enter them in `pipeline.md` at Stage 1 (Discovered)
- Record source URL and initial impression

### Step 4: Research Top Leads

Take the highest-priority Stage 1 leads and move them to Stage 2:

- Use COMPOSIO_SEARCH_FETCH_URL_CONTENT to read their website, about page, blog
- Use COMPOSIO_SEARCH_WEB to find their other public presence
- Read their recent posts, projects, or content
- Fill in the full lead file with research summary and WordPilot fit

### Step 5: Qualify Ready Leads

For fully researched leads (Stage 2), decide if they're a fit:

- Does their work genuinely align with WordPilot's capabilities?
- Can you articulate a specific, personalized use case?
- Is there a natural, non-awkward way to open a conversation?

If yes → move to Stage 3 (Qualified), set priority, draft the personalized angle.
If no → note why, keep at Stage 2 with a note, or archive if clearly not a fit.

### Step 6: Draft Outreach (if requested)

For Stage 3 leads, draft personalized outreach messages. Wait for user approval before sending.

**Outreach principles:**
- Reference something specific they made or wrote
- Ask a genuine question about their work
- Mention WordPilot only after establishing context
- Keep it under 150 words
- Make replying easy (one clear question or invitation)

**Never:**
- Send without user approval
- Use the same template twice in a row
- Mention "I'm an AI" unless relevant to the conversation
- Pretend to be a human if asked directly

### Step 7: Send Approved Outreach (if Gmail connected)

If the user approves an outreach message and Gmail is connected via Composio:
- Use GMAIL_CREATE_EMAIL_DRAFT to create the draft
- Ask user for final review before sending
- Use GMAIL_SEND_DRAFT to send only after explicit approval
- Log the outreach in the lead file and pipeline

If Gmail is not connected, tell the user the message is ready and they can copy-paste it.

### Step 8: Follow Up on Waiting Leads

For Stage 4 (Contacted) leads with no response after 5-7 days:
- Draft a gentle follow-up
- Never pressure or guilt
- Add new value in the follow-up (a relevant article, a tip, or a question)

For Stage 5 (Nurturing) leads:
- Check conversation recency
- Suggest next touch if it's been more than 7 days
- Look for organic reasons to reconnect (they posted something new, launched something, etc.)

### Step 9: Update the Daily Board

Write today's results to `/leads/daily-board.md`:

```markdown
# Daily Board — YYYY-MM-DD

## Yesterday's Results
- [What was completed]

## Today's Plan
- [ ] Research 3 new leads in [segment]
- [ ] Research [Lead Name] (Stage 1 → 2)
- [ ] Qualify [Lead Name] (Stage 2 → 3)
- [ ] Draft outreach for [Lead Name]
- [ ] Follow up on [Lead Name] (7 days no response)

## Leads Moved
| Lead | From | To | Notes |
| --- | --- | --- | --- |

## Responses Received
[Any replies or signals]

## Tomorrow's Prep
- [What to pick up next]
```

### Step 10: Report to User

End every daily session with a clear summary:
- Pipeline health (counts by stage)
- What was done today
- What's planned for tomorrow
- Any responses or signals
- One recommended focus for the next session

---

## Segmentation Strategy

Target these segments, rotating focus to keep the pipeline diverse:

### Segment A: Developer Tool Makers & Open-Source Maintainers
**Why:** They write docs, READMEs, changelogs, and websites. WordPilot's GitHub documentation generator, markdown writer, and diagram tools directly serve them.
**Where to find:** GitHub trending repos, awesome lists, dev.to, Hackaday
**Angle:** "I saw your project [name] — the docs are impressive. Curious how you manage documentation workflow with contributors."

### Segment B: Technical Educators & Course Creators
**Why:** They create quizzes, worksheets, tutorials, and structured learning content. WordPilot's quiz generator, LaTeX support, and column layouts are built for this.
**Where to find:** Udemy instructors, YouTube tutorial creators, freeCodeCamp contributors, Substack educators
**Angle:** "Your [course/article] on [topic] was really clear. I'm curious — how do you currently handle the quiz and worksheet creation side of your content?"

### Segment C: Content Teams & Marketing Writers
**Why:** They produce landing pages, email sequences, and campaign docs. WordPilot's HTML writer, email triage, and marketing playbook tools fit their workflow.
**Where to find:** Marketing Twitter, Content Marketing Institute, marketing Substack newsletters
**Angle:** "Noticed your team's [campaign/content series]. The consistency across channels is impressive. Always interested in how teams streamline that production process."

### Segment D: Indie Hackers & Solo Founders
**Why:** They wear all hats including writing. WordPilot helps them ship pages, docs, and content faster without hiring.
**Where to find:** Indie Hackers, Hacker News, Product Hunt, build-in-public Twitter
**Angle:** "Saw your launch of [product]. As a solo builder, how do you handle the writing side — docs, landing pages, blog posts? That's always the bottleneck I hear about."

### Segment E: AI Power Users & Prompt Engineers
**Why:** They already use AI assistants but may be frustrated by chat-only interfaces. WordPilot gives them real files and workspaces.
**Where to find:** r/ChatGPT, r/ClaudeAI, AI Twitter, prompt libraries
**Angle:** "Your prompt for [use case] is clever. I'm curious — when you use AI for writing, do you prefer chat or a workspace with actual files? I've been exploring the workspace approach and find it changes things."

---

## Pipeline Health Rules

- **Minimum pipeline:** 10 active leads across stages 1-5
- **Ideal distribution:** 4 Discovered, 3 Researched, 2 Qualified, 1 Contacted, 1 Nurturing
- **Stale lead threshold:** No activity in 14 days → either follow up or archive
- **Max outreach per day:** 3 new contacts (quality over quantity)
- **Research before outreach:** At least 15 minutes of reading their public work before drafting
- **Follow-up cadence:** Day 5-7 after first contact, then day 14, then day 30

---

## Integration Dependencies

### Required for Full Functionality
- **Composio Search** (COMPOSIO_SEARCH_WEB, COMPOSIO_SEARCH_FETCH_URL_CONTENT, COMPOSIO_SEARCH_NEWS) — for lead research
- **Gmail** (GMAIL_CREATE_EMAIL_DRAFT, GMAIL_SEND_DRAFT, GMAIL_FETCH_EMAILS) — for outreach and tracking responses

### Optional Enhancements
- **Google Sheets** — alternative pipeline tracker
- **Notion** — alternative CRM
- **Browser Tool** — for scraping pages that COMPOSIO_SEARCH_FETCH_URL_CONTENT can't reach

### When Integrations Are Missing
- If Composio Search is available (it's built-in): proceed with all research steps
- If Gmail is not connected: draft messages for user to copy-paste; tell user to connect Gmail in Integrations for direct sending
- If neither: research and draft only; user handles all external actions

---

## Quality Constraints

- Never fabricate lead information. If you can't find something, say so.
- Never claim a lead said or did something you didn't observe.
- Never send outreach without user approval.
- Keep all lead files factual and professional — no speculation labeled as fact.
- Respect public information only. Do not attempt to access private profiles, paywalled content, or login-gated pages.
- If a person's public presence indicates they don't want unsolicited contact, mark them as "Do Not Contact" and move on.
- Rotate segments. Don't target the same narrow group repeatedly.
- Maintain variety in outreach — never let two messages in a row feel template-driven to the same audience.

---

## Error Recovery

- **Research comes back sparse:** Mark lead as "Needs More Research" in notes. Try again with different search terms on next session.
- **Outreach gets no response:** After second follow-up with no response, move to a "Dormant" sub-list. Don't delete — they may engage later.
- **Negative response:** Thank them, remove from active pipeline, note preference. Never argue or push.
- **Duplicate lead found:** Merge files, keep the richer research, note the duplicate source.
- **Pipeline feels stuck:** Report to user with honest assessment. Suggest a new segment or angle. Don't force outreach.

---

## Example Daily Flow

**User:** "Morning — let's work the leads."

**You (internal process):**
1. Read `/leads/daily-board.md` and `/leads/pipeline.md`
2. Report yesterday's results: "Yesterday we researched 3 leads in the developer tools segment. One qualified. No responses yet on the 2 outreach messages sent Monday."
3. Today's pipeline health: "Pipeline: 4 Discovered, 2 Researched, 3 Qualified, 2 Contacted, 1 Nurturing. We're a bit light on Discovered — let me find 3 new leads."
4. Execute research: search for Segment A leads, find 3, create lead files, add to pipeline
5. Research top Discovered lead: read their GitHub, blog, and Twitter. Write full research summary. Move to Researched.
6. Qualify a Researched lead: "This indie hacker just launched a dev tool with a docs site. Perfect fit. Qualifying — priority High."
7. Draft outreach for the top Qualified lead (user reviews and approves)
8. Update daily-board.md with everything
9. Report summary: "Today: 3 new leads discovered, 1 researched, 1 qualified, 1 outreach drafted. Pipeline is healthy at 12 active. Tomorrow: research the 2 new Discovered leads and follow up on the Contacted lead from Monday."

---

## File Output Standards

All lead workspace files are Markdown. Follow `/skills/markdown-writer/SKILL.md` for quality.

Key conventions:
- Use tables for pipeline tracking, outreach logs, and daily boards
- Use checklists for daily task lists
- Use columns for comparing leads or segments when helpful
- Keep individual lead files clean and scannable
- Never let pipeline.md exceed 200 lines — archive old leads to `/leads/archive/` monthly
