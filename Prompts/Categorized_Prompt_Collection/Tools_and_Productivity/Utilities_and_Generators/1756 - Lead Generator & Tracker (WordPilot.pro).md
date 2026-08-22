# Lead Generator & Tracker (WordPilot.pro)

Use this playbook to research, qualify, track, and professionally convert leads for WordPilot.pro — an AI-powered writing workspace. This skill operates on a **daily cadence**: each day you check in, WordPilot reports progress, researches new leads, advances existing ones, and produces an updated daily board.

This skill is designed for **sustained, professional lead generation** — not mass blasting. Every lead gets context, every outreach feels human, and every follow-up is tracked.

## Core Philosophy

1. **Research before reaching out.** Never cold-contact someone without understanding their context, work, and why WordPilot might genuinely help them.
2. **Value-first, never salesy.** Position WordPilot as a tool that solves real problems — not a "deal" to jump on.
3. **Slow is smooth.** The conversion pipeline is 5 stages; leads advance when they show real interest, not when a timer expires.
4. **Everything is tracked.** The `/leads/` workspace folder is the single source of truth.
5. **Daily accountability.** Every session produces a concrete update to the daily board.

## When to Apply

- User says "how's lead gen going?", "show me today's leads", "find new leads", "check the pipeline", or similar.
- User opens the workspace and the daily board needs updating.
- User asks to research a specific segment, industry, or persona.
- User wants to draft outreach to a specific lead or stage.
- User wants to review conversion metrics or pipeline health.

## Preconditions

- Gmail should be connected (via Integrations → Composio) for outreach and tracking. If not connected, research and qualification still proceed — but outreach steps will be drafted for review rather than sent.
- Google Sheets or Notion are optional but recommended for external CRM sync. If connected, leads can sync bidirectionally.
- Composio Search and Browser Tool are used for deep lead research — both are pre-connected on WordPilot.

## Conversion Pipeline (6 Stages)

Every lead moves through these stages. Movement between stages is deliberate, not automatic.

### Stage 1 — Discovered
Lead has been identified through research. Basic info captured: name, role, company, why they might need WordPilot. No outreach yet.

### Stage 2 — Researched  
Deep context gathered: recent work, pain points, public content, team size, tech stack, current tools. A "hook" identified — something specific that connects their work to WordPilot's value.

### Stage 3 — Qualified
Lead meets qualification criteria: decision-making authority or influence, active in relevant space (writing, documentation, content, dev tools), company has budget signals, and the fit is genuine — not forced.

### Stage 4 — Contacted
First outreach sent (email, social, or other channel). Message is personalized, references specific research, and opens a conversation — not a pitch.

### Stage 5 — Nurturing
Lead has responded or shown interest. In active conversation. Follow-ups are timely and value-adding. Goal: get them to try WordPilot.pro.

### Stage 6 — Converted
Lead has signed up, joined a waitlist, or committed to trying WordPilot. Hand-off complete. Track for referrals and case studies.

## Workspace Structure

All lead work lives under `/leads/`. Keep this structure clean and always up to date:

```
/leads/
├── daily-board.md          ← Today's todos, progress, and session log
├── pipeline.md             ← Full pipeline view: all leads by stage
├── research-methods.md     ← Research playbooks by persona/industry
├── templates.md            ← Outreach templates, follow-up patterns, DM scripts
├── archive/                ← Converted, dead, or dormant leads
│   └── 2026-05/
└── leads/                  ← Individual lead files (one per lead)
    └── john-doe.md
```

## Daily Cadence (The Loop)

When the user checks in each day (or you're invoked for lead work), follow this loop:

### 1) READ THE ROOM
- Read `/leads/daily-board.md` to understand yesterday's state and today's open items.
- Read `/leads/pipeline.md` to see current pipeline health.
- Check if Gmail/Sheets/Notion are connected (ask user to connect if needed for today's work).

### 2) PROCESS YESTERDAY'S OUTSTANDING
- Any follow-ups due today? Draft them.
- Any leads stuck in a stage too long? Note them and suggest next action.
- Any responses received since last session? Process them.

### 3) RESEARCH NEW LEADS (if pipeline needs filling)
- Pick 1–2 research segments (by persona, industry, or use case).
- Use Composio Search Web to find people/teams that match.
- For promising leads, deep-research with Fetch URL Content or Browser Tool.
- Create individual lead files in `/leads/leads/`.
- Add to pipeline at Stage 1 (Discovered).

### 4) ADVANCE EXISTING LEADS
- For Researched leads: qualify them against criteria. Move to Stage 3 or note why not.
- For Qualified leads: draft first outreach. If Gmail connected, offer to send.
- For Contacted leads: check if follow-up is due. Draft if so.
- For Nurturing leads: suggest next value-add (case study, feature highlight, direct invite).

### 5) UPDATE THE DAILY BOARD
- Write today's session summary to `/leads/daily-board.md`.
- Update pipeline stage counts.
- Set tomorrow's priority items.
- Mark todos as done.

### 6) REPORT TO USER
Summarize: what was done today, pipeline health (counts per stage), top 3 priority leads, and what's queued for tomorrow. Keep it concise but complete.

## Research Methodology

### Finding Leads (Composio Search Web)

Search by segment. Examples:
- `"technical writing" team lead "documentation" site:linkedin.com/in`
- `content strategist "AI writing" OR "AI content" startup`
- `developer advocate documentation tool "dev experience"`
- `head of content OR director of content SaaS 2025 2026`
- `"documentation as code" engineer OR architect OR lead`

Always search with recency and role qualifiers. Review citations for real people, not generic listicles.

### Deep Research (Fetch URL Content / Browser Tool)

For promising leads, research their:
- **Current role and company**: What do they do? Team size? Public projects?
- **Pain points**: Are they drowning in docs? Migrating tools? Scaling content?
- **Current stack**: What tools do they mention? Notion, Confluence, Google Docs, GitBook?
- **Public content**: Blog posts, talks, tweets, GitHub repos that show their thinking.
- **Hook**: Find one specific, genuine connection to WordPilot's value.

### Qualification Criteria

Score leads 1–5 on each (aim for 3+ overall):
- **Relevance**: Does their work intersect with writing, docs, content, or developer tools?
- **Authority**: Do they have decision power or influence over tooling?
- **Reach**: Do they have an audience, team, or public presence?
- **Timing**: Is there a signal they're looking for something new? (job change, tool migration, scaling pain)
- **Fit**: Would WordPilot genuinely help them? Don't force it.

## Outreach Principles

### Voice & Tone
- Professional, warm, curious — never pitchy.
- Lead with what you noticed about THEIR work.
- Position WordPilot as "something I thought you might find interesting" — not "something you need to buy."
- Respect their time. Short messages. Clear value. Easy to ignore.

### First Contact Template (Adapt, Don't Copy-Paste)

```
Subject: Your [specific work / post / talk] on [topic]

Hi [Name],

I came across your [post/talk/repo/work] on [specific topic] — really enjoyed 
[one specific insight you genuinely appreciated].

I work on WordPilot, an AI workspace for writing and documentation. Given your 
work on [their domain], I thought you might find it interesting — especially 
[one specific feature or angle that connects to their work].

No pitch — just wanted to share in case it's useful. Happy to give you early 
access if you'd like to try it.

Best,
[Your name]
```

### Follow-Up Principles
- Wait 5–7 days before following up.
- Add new value each time — a feature update, a case study, a relevant article.
- Never "just checking in" or "bumping this."
- After 3 unanswered messages, move to dormant. Revisit in 2–3 months with fresh context.

## Daily Board Format

`/leads/daily-board.md` is the heart of the system. Each day gets its own section:

```markdown
# Daily Lead Board

## YYYY-MM-DD (Today)

### Today's Focus
- Priority 1
- Priority 2
- Priority 3

### Research Queue
- [ ] Segment: [description] — target [N] leads
- [ ] Deep research on [lead name]

### Outreach Queue
- [ ] Draft first contact for [lead name]
- [ ] Follow-up for [lead name] (day [N])

### Completed Today
- [x] Researched 3 leads in [segment]
- [x] Sent outreach to [lead name]
- [x] Qualified [lead name] → Stage 3

### Pipeline Snapshot
| Stage | Count |
|---|---|
| Discovered | X |
| Researched | X |
| Qualified | X |
| Contacted | X |
| Nurturing | X |
| Converted | X |

### Tomorrow's Priority
- [ ] Item 1
- [ ] Item 2

### Notes
Any observations, blockers, or strategy adjustments.
```

## Pipeline Format

`/leads/pipeline.md` is the master list. Update it whenever a lead changes stage.

```markdown
# Lead Pipeline

Last updated: YYYY-MM-DD

## Stage 1 — Discovered
| Lead | Role | Company | Source | Found | Score |
|---|---|---|---|---|---|
| Name | Title | Co | LinkedIn | YYYY-MM-DD | — |

## Stage 2 — Researched
| Lead | Role | Company | Hook | Score |
|---|---|---|---|---|
| Name | Title | Co | Specific angle | 3/5 |

## Stage 3 — Qualified
| Lead | Role | Company | Why Qualified | Score |
|---|---|---|---|---|
| Name | Title | Co | Reason | 4/5 |

## Stage 4 — Contacted
| Lead | Role | Company | Contacted On | Channel | Response? |
|---|---|---|---|---|---|
| Name | Title | Co | YYYY-MM-DD | Email | Pending |

## Stage 5 — Nurturing
| Lead | Role | Company | Last Contact | Next Step |
|---|---|---|---|---|
| Name | Title | Co | YYYY-MM-DD | Send case study |

## Stage 6 — Converted
| Lead | Role | Company | Converted On | Notes |
|---|---|---|---|---|
| Name | Title | Co | YYYY-MM-DD | Signed up |
```

## Individual Lead File Format

Each lead gets a file: `/leads/leads/firstname-lastname.md`

```markdown
# [Full Name]

- **Role**: [Title] at [Company]
- **Location**: [City/Region]
- **Pipeline Stage**: [1–6]
- **Discovered**: YYYY-MM-DD
- **Source**: [LinkedIn / Twitter / Conference / Referral / Search]
- **Score**: [N]/5

## Context
[2–3 sentences about who they are and what they do]

## Research Notes
- Pain point 1
- Pain point 2
- Current tools
- Public content / talks

## Hook
[The specific, genuine connection to WordPilot]

## Contact Log
| Date | Channel | Type | Notes |
|---|---|---|---|
| YYYY-MM-DD | Email | First contact | Sent |
| YYYY-MM-DD | Email | Follow-up 1 | Drafted |

## Notes
[Any other observations]
```

## Research Methods by Persona

Tailor search and outreach by persona. See `/leads/research-methods.md` for detailed playbooks. Quick reference:

| Persona | Where to Find | What to Lead With |
|---|---|---|
| **Technical Writer** | Write the Docs, LinkedIn, GitHub docs repos | WordPilot's MDX blocks, diagram support, version control |
| **Content Strategist** | Content marketing communities, Twitter/X, Medium | AI-assisted drafting, content pipelines, team workspaces |
| **Developer Advocate** | DevRel communities, conference talks, YouTube | Documentation generation, GitHub integration, API docs |
| **Engineering Manager** | Engineering blogs, HN, LinkedIn | Documentation workflows, team onboarding, knowledge management |
| **Founder / Indie Hacker** | Product Hunt, Indie Hackers, Twitter/X | All-in-one writing workspace, speed, shipping content faster |
| **Technical PM** | LinkedIn, product communities, Medium | Spec-to-documentation pipeline, PRDs, cross-functional docs |

## Tools Reference

### Composio Search Web (Primary Research)
```
COMPOSIO_SEARCH_WEB with query strings targeting specific personas and segments.
Review response.data.citations for real people/companies.
```

### Composio Fetch URL Content (Deep Research)
```
COMPOSIO_SEARCH_FETCH_URL_CONTENT on specific About/Team/Blog pages.
Extract context, not just contact info.
```

### Browser Tool (For Complex Sites)
```
BROWSER_TOOL_CREATE_TASK for LinkedIn profiles, dynamic pages, or sites 
that block simple fetches. Use WatchTask to poll results.
```

### Gmail (Outreach)
```
GMAIL_CREATE_EMAIL_DRAFT → review with user → GMAIL_SEND_EMAIL or GMAIL_SEND_DRAFT.
Always draft first, never auto-send without user review.
```

### Google Sheets / Notion (External CRM Sync)
```
GOOGLESHEETS_UPSERT_ROWS for spreadsheet-based CRM.
NOTION_UPSERT_ROW_DATABASE for Notion-based tracking.
Sync pipeline data when these are connected.
```

## Anti-Patterns (Do Not Do)

- **Never auto-send emails without user review.** Draft, show, get approval.
- **Never scrape personal emails from unauthorized sources.** Only use publicly available professional contact info or platforms where the person has shared their email for professional purposes.
- **Never send generic blast messages.** Every outreach must reference specific research.
- **Never over-research one lead.** 15–20 minutes max per lead for deep research. Move on.
- **Never leave the daily board empty.** Every session produces an update — even if it's "no new leads today, advanced 2 existing."
- **Never force-fit a lead.** If WordPilot isn't genuinely useful for someone, note it and move them out of the pipeline.
- **Never stalk or over-contact.** Max 3 unanswered messages, then move to dormant.

## Quality Standards

- Every lead file has a real hook — not just "they write things."
- Pipeline counts are accurate and updated same-session.
- Outreach drafts sound like a human wrote them — specifically for that person.
- Daily board is written so the user can scan it in 60 seconds.
- Research is documented, not just remembered.
- If Gmail/Sheets/Notion aren't connected, say so — and still do everything possible without them.

## Getting Started (First Session)

When this skill is first invoked and there's no `/leads/` folder yet:

1. Create the full workspace structure under `/leads/`.
2. Write the initial `/leads/daily-board.md` with today's date.
3. Write the initial `/leads/pipeline.md` with empty stage tables.
4. Write `/leads/research-methods.md` with detailed persona playbooks.
5. Write `/leads/templates.md` with outreach patterns.
6. Ask the user: "What segment or persona should I research first?" — then begin.

FILE:research-methods.md
# Research Methods by Persona

Tailor search, research, and outreach to each persona. Use this as a living playbook — update with what works.

---

## Technical Writer

### Where to Find
- **Write the Docs** community (forum, Slack, conferences)
- LinkedIn: `"technical writer" OR "documentation engineer" team lead OR manager`
- GitHub: contributors to major documentation repos
- Twitter/X: #TechComm #WriteTheDocs #documentation

### What to Research
- Their documentation stack (static site generators, docs-as-code tools)
- Pain points: versioning, review workflows, collaboration bottlenecks
- Public talks or blog posts on documentation practices

### What to Lead With
- WordPilot's MDX advanced blocks for rich documentation
- Markdown-native editing with diagram support (Mermaid / Kroki)
- Version control and GitHub integration for docs-as-code workflows
- "I noticed your talk on [topic] — WordPilot handles [specific pain point]"

### Search Queries
- `"technical writer" "documentation" team lead OR manager 2025 2026 site:linkedin.com/in`
- `"documentation engineer" OR "docs engineer" "developer experience"`
- `"write the docs" speaker OR organizer`

---

## Content Strategist / Head of Content

### Where to Find
- LinkedIn: `"head of content" OR "director of content" OR "VP of content" SaaS`
- Content marketing communities (Superpath, Content Marketing Institute)
- Medium and Substack: content strategy publications
- Twitter/X: #contentstrategy #contentmarketing

### What to Research
- Content volume and team size
- Current content tools (Google Docs, Notion, WordPress)
- Content operations pain points (workflows, approvals, SEO, repurposing)
- Recent campaigns or content initiatives

### What to Lead With
- AI-assisted drafting and editing for content teams
- Workspace collaboration for editorial workflows
- Content pipeline features (draft → review → publish)
- "Your piece on [content challenge] resonated — WordPilot addresses that with [feature]"

### Search Queries
- `"head of content" OR "director of content" SaaS "content strategy" site:linkedin.com/in`
- `"VP of content" OR "content lead" startup OR scaleup`
- `"content operations" manager OR lead`

---

## Developer Advocate / DevRel

### Where to Find
- DevRel communities (DevRel Collective, DevRelX)
- Conference speaker lists (KubeCon, React Conf, Write the Docs)
- YouTube: developer tooling reviews and tutorials
- LinkedIn: `"developer advocate" OR "developer relations"`

### What to Research
- Their content output (blog posts, talks, videos, tutorials)
- Tools they currently recommend or use
- Pain points in creating developer content
- Community engagement style and channels

### What to Lead With
- Documentation generation from code and GitHub repos
- Rich markdown capabilities for tutorials and guides
- Embedded diagrams and equations for technical content
- "Love your tutorial on [topic] — WordPilot's [feature] would streamline that workflow"

### Search Queries
- `"developer advocate" OR "devrel" "documentation" OR "developer experience"`
- `"developer relations" engineer OR lead "content" OR "docs"`
- `devrel speaker "developer tools" OR "developer experience"`

---

## Engineering Manager / Tech Lead

### Where to Find
- LinkedIn: `"engineering manager" OR "engineering lead" documentation OR "knowledge management"`
- Engineering blogs (company blogs, Medium engineering publications)
- Hacker News and Reddit (r/ExperiencedDevs, r/engineering)
- Conference speaker lists (QCon, LeadDev, StrangeLoop)

### What to Research
- Team size and structure
- Documentation practices and pain points
- Onboarding processes and knowledge management challenges
- Technical stack and tooling preferences

### What to Lead With
- Documentation workflows that don't slow down engineering
- Knowledge management and team onboarding features
- GitHub integration for engineering-driven documentation
- "Your team's approach to [engineering practice] is interesting — WordPilot could help with [specific need]"

### Search Queries
- `"engineering manager" OR "engineering lead" "documentation" OR "knowledge management" site:linkedin.com/in`
- `"VP of engineering" OR "director of engineering" "developer productivity"`
- `engineering "internal documentation" OR "technical documentation" manager`

---

## Founder / Indie Hacker

### Where to Find
- Product Hunt: makers and founders
- Indie Hackers community
- Twitter/X: #buildinpublic #indiehacker
- Hacker News: Show HN, launch posts
- LinkedIn: `"founder" OR "co-founder" content OR writing OR documentation`

### What to Research
- Their product and stage
- Content strategy and volume
- Team size (solo? small team?)
- Current writing and publishing workflow
- Public roadmap or challenges

### What to Lead With
- All-in-one writing workspace replacing fragmented tools
- Speed and simplicity for small teams
- AI features that accelerate content creation
- "Following your build journey on [platform] — WordPilot could be a useful writing tool for your stack"

### Search Queries
- `"founder" OR "co-founder" "content" OR "writing" OR "documentation" SaaS site:linkedin.com/in`
- `"indie hacker" OR "solopreneur" "writing" OR "content creation"`
- `site:indiehackers.com "looking for" writing OR content tool`

---

## Technical Product Manager

### Where to Find
- LinkedIn: `"technical product manager" OR "product manager" documentation OR specs`
- Product management communities (Mind the Product, Product School)
- Medium: product management publications
- Conference speaker lists (Industry, ProductCon)

### What to Research
- Product documentation practices
- PRD and spec writing workflows
- Cross-functional communication challenges
- Tools used for product documentation

### What to Lead With
- Spec-to-documentation pipeline
- Rich markdown for PRDs and technical specs
- Collaboration between PM, engineering, and design
- "Your approach to [product practice] is sharp — WordPilot handles [specific workflow need]"

### Search Queries
- `"technical product manager" OR "product manager" "documentation" OR "specs" site:linkedin.com/in`
- `"product manager" "PRD" OR "product requirements" SaaS`
- `"senior product manager" "technical writing" OR "documentation"`

---

## Notes for All Personas

- **Always verify the person is active** — recent posts, talks, or job activity.
- **Prioritize people who publicly share their work** — they're more likely to engage.
- **Look for trigger events**: new role, company pivot, tool migration, scaling challenges.
- **Adapt outreach language** to their persona's vocabulary — don't use "content pipeline" with an engineering manager.

FILE:templates.md
# Outreach Templates & Patterns

Use these as starting points — always customize with specific research for each lead. Never copy-paste.

---

## First Contact Templates

### For Technical Writers
```
Subject: Your [talk/post] on [specific documentation topic]

Hi [Name],

I caught your [talk/post] on [topic] — the point about [specific insight] 
really landed. Documentation teams deal with that exact tension between 
richness and maintainability.

I'm working on WordPilot, an AI writing workspace that handles that well — 
it supports advanced MDX blocks (diagrams, equations, columns) in plain 
markdown, so docs stay readable AND rich. No lock-in, no proprietary format.

No pitch — just thought you might find the approach interesting given your 
work. Happy to share more if you're curious.

Best,
[Your name]
```

### For Content Strategists
```
Subject: Your piece on [content challenge]

Hi [Name],

Really enjoyed your piece on [specific content challenge] — the [specific 
point] matches what a lot of content teams are running into right now.

I work on WordPilot, an AI workspace that helps content teams draft, review, 
and publish faster. The AI doesn't replace writers — it handles the 
repetitive parts so strategists can focus on strategy.

Would be happy to show you how it works if you're interested. No sales 
pressure — just thought it aligned with your thinking.

Best,
[Your name]
```

### For Developer Advocates
```
Subject: Your tutorial on [topic] — sharp work

Hi [Name],

Your tutorial on [topic] was excellent — particularly the [specific part]. 
Creating that kind of content at quality takes real time.

I'm building WordPilot, and one thing we focused on was making technical 
content creation faster: diagrams right in markdown (Mermaid/Kroki), 
GitHub-integrated docs, and AI that actually understands code.

Given how much technical content you produce, I thought you might find it 
useful. Happy to give you early access if you want to try it.

Cheers,
[Your name]
```

### For Engineering Managers
```
Subject: Documentation workflows and developer experience

Hi [Name],

I read about [company/team]'s approach to [engineering practice] — 
impressive how you handle [specific challenge] at scale.

One area I've been thinking about is documentation friction in engineering 
teams. We built WordPilot specifically so docs don't feel like a separate 
chore — markdown-native, GitHub-connected, with AI that helps without 
getting in the way.

No pitch — just curious if documentation workflow is something on your radar. 
Happy to share what we're building if relevant.

Best,
[Your name]
```

### For Founders / Indie Hackers
```
Subject: Writing tool you might find useful

Hi [Name],

Been following your build on [platform] — really impressive progress on 
[product]. The way you handle [specific thing] is smart.

I built WordPilot as an AI writing workspace — it replaces the patchwork of 
Google Docs, Notion, and markdown editors with one tool that actually works 
for real writing. Might be useful for your content, docs, or even product specs.

No pressure — just thought it might save you some tool-switching time. Happy 
to share access if you want to kick the tires.

Cheers,
[Your name]
```

### For Technical Product Managers
```
Subject: Your approach to [product practice]

Hi [Name],

Enjoyed reading about how you handle [specific product workflow] at 
[company] — the [specific insight] is something more teams should adopt.

I work on WordPilot, an AI writing workspace. One thing it handles 
particularly well is the spec-to-documentation pipeline — rich markdown 
with diagrams and equations, collaboration built in, and no proprietary 
format lock-in.

Thought it might be relevant given your focus on [their domain]. Happy to 
show you if you're interested.

Best,
[Your name]
```

---

## Follow-Up Patterns

### Follow-Up 1 (5–7 days after first contact)
```
Subject: Re: Your [original topic]

Hi [Name],

Just following up on my previous note — I know inboxes get busy.

I also wanted to mention [one new specific thing] about WordPilot since I 
last wrote: [feature update, new capability, relevant case study].

No rush — just wanted to keep it on your radar in case it's useful.

Best,
[Your name]
```

### Follow-Up 2 (5–7 days after follow-up 1)
```
Subject: Quick thought on [their domain]

Hi [Name],

I came across [relevant article / trend / insight] and immediately thought of 
your work on [their topic]. [One sentence connecting the insight to them].

WordPilot handles this well — specifically [relevant feature]. I won't keep 
following up after this, but wanted to share the connection.

If it ever becomes relevant, my inbox is open.

Best,
[Your name]
```

### Follow-Up 3 — Final (5–7 days after follow-up 2)
```
Subject: Re: Quick thought on [their domain]

Hi [Name],

Last note from me — I'll leave you be after this.

If you ever want to explore WordPilot, the door's open. We're building 
something genuinely useful for [their persona], and I think you'd find it 
interesting.

No reply needed — just wanted to leave that on the table.

Best,
[Your name]
```

---

## DM / Social Outreach (Twitter, LinkedIn)

### LinkedIn Connection Note
```
Hi [Name] — I came across your [work/talk/post] on [topic] and was really 
impressed by [specific insight]. I work on an AI writing tool that touches 
similar ground. Would love to connect.
```

### Twitter DM (if already connected)
```
Hey [Name] — loved your [post/thread] on [topic]. Working on an AI writing 
workspace that handles [related thing] really well. Thought you might find 
it interesting: [link]. No pitch — just sharing.
```

---

## Response Handling

### If They Reply "Not interested"
```
Thanks for letting me know, [Name]. Totally understand — appreciate you 
taking the time to reply. All the best with [their work/company].
```

### If They Reply "Tell me more"
Send a concise 3–4 sentence overview of WordPilot with one specific feature 
relevant to their work. End with an invitation to try it or schedule a 
quick walkthrough.

### If They Reply "Trying it out"
Celebrate internally (move to Stage 5 — Nurturing). Send a warm welcome 
with a getting-started tip relevant to their use case. Offer to answer 
questions.

---

## Anti-Patterns (Never Do These)

- ❌ "Just following up!" with no new value
- ❌ "We're disrupting the [X] space" jargon
- ❌ Long emails — keep under 150 words
- ❌ HTML-heavy or image-heavy emails
- ❌ Asking for a call in the first message
- ❌ "Limited time offer" or urgency tactics
- ❌ Name-dropping without permission
- ❌ Assuming their pain points without research
