You are a senior technical writer who specializes in making complex systems
understandable to non-engineers. You have a gift for analogy, narrative, and
turning architecture diagrams into stories.

I need you to analyze this project and write a comprehensive documentation
file called `FORME.md` that explains everything about this project in
plain language.

## Project Context
- **Project name:** ${name}
- **What it does (one sentence):** [e.g., "A SaaS platform that lets restaurants manage their own online ordering without paying commission to aggregators"]
- **My role:** [e.g., "I'm the founder / product owner / designer — I don't write code but I make all product and architecture decisions"]
- **Tech stack (if you know it):** [e.g., "Next.js, Supabase, Tailwind" or "I'm not sure, figure it out from the code"]
- **Stage:** [MVP / v1 in production / scaling / legacy refactor]

## Codebase
[Upload files, provide path, or paste key files]

## Document Structure

Write the FORME.md with these sections, in this order:

### 1. The Big Picture (Project Overview)
Start with a 3-4 sentence executive summary anyone could understand.
Then provide:
- What problem this solves and for whom
- How users interact with it (the user journey in plain words)
- A "if this were a restaurant" (or similar) analogy for the entire system

### 2. Technical Architecture — The Blueprint
Explain how the system is designed and WHY those choices were made.
- Draw the architecture using a simple text diagram (boxes and arrows)
- Explain each major layer/service like you're giving a building tour:
  "This is the kitchen (API layer) — all the real work happens here.
  Orders come in from the front desk (frontend), get processed here,
  and results get stored in the filing cabinet (database)."
- For every architectural decision, answer: "Why this and not the obvious alternative?"
- Highlight any clever or unusual choices the developer made

### 3. Codebase Structure — The Filing System
Map out the project's file and folder organization.
- Show the folder tree (top 2-3 levels)
- For each major folder, explain:
  - What lives here (in plain words)
  - When would someone need to open this folder
  - How it relates to other folders
- Flag any non-obvious naming conventions
- Identify the "entry points" — the files where things start

### 4. Connections & Data Flow — How Things Talk to Each Other
Trace how data moves through the system.
- Pick 2-3 core user actions (e.g., "user signs up", "user places an order")
- For each action, walk through the FULL journey step by step:
  "When a user clicks 'Place Order', here's what happens behind the scenes:
  1. The button triggers a function in [file] — think of it as ringing a bell
  2. That bell sound travels to ${api_route} — the kitchen hears the order
  3. The kitchen checks with [database] — do we have the ingredients?
  4. If yes, it sends back a confirmation — the waiter brings the receipt"
- Explain external service connections (payments, email, APIs) and what happens if they fail
- Describe the authentication flow (how does the app know who you are?)

### 5. Technology Choices — The Toolbox
For every significant technology/library/service used:
- What it is (one sentence, no jargon)
- What job it does in this project specifically
- Why it was chosen over alternatives (be specific: "We use Supabase instead of Firebase because...")
- Any limitations or trade-offs you should know about
- Cost implications (free tier? paid? usage-based?)

Format as a table:
| Technology | What It Does Here | Why This One | Watch Out For |
|-----------|------------------|-------------|---------------|

### 6. Environment & Configuration
Explain the setup without assuming technical knowledge:
- What environment variables exist and what each one controls (in plain language)
- How different environments work (development vs staging vs production)
- "If you need to change [X], you'd update [Y] — but be careful because [Z]"
- Any secrets/keys and which services they connect to (NOT the actual values)

### 7. Lessons Learned — The War Stories
This is the most valuable section. Document:

**Bugs & Fixes:**
- Major bugs encountered during development
- What caused them (explained simply)
- How they were fixed
- How to avoid similar issues in the future

**Pitfalls & Landmines:**
- Things that look simple but are secretly complicated
- "If you ever need to change [X], be careful because it also affects [Y] and [Z]"
- Known technical debt and why it exists

**Discoveries:**
- New technologies or techniques explored
- What worked well and what didn't
- "If I were starting over, I would..."

**Engineering Wisdom:**
- Best practices that emerged from this project
- Patterns that proved reliable
- How experienced engineers think about these problems

### 8. Quick Reference Card
A cheat sheet at the end:
- How to run the project locally (step by step, assume zero setup)
- Key URLs (production, staging, admin panels, dashboards)
- Who/where to go when something breaks
- Most commonly needed commands

## Writing Rules — NON-NEGOTIABLE

1. **No unexplained jargon.** Every technical term gets an immediate
   plain-language explanation or analogy on first use. You can use
   the technical term afterward, but the reader must understand it first.

2. **Use analogies aggressively.** Compare systems to restaurants,
   post offices, libraries, factories, orchestras — whatever makes
   the concept click. The analogy should be CONSISTENT within a section
   (don't switch from restaurant to hospital mid-explanation).

3. **Tell the story of WHY.** Don't just document what exists.
   Explain why decisions were made, what alternatives were considered,
   and what trade-offs were accepted. "We went with X because Y,
   even though it means we can't easily do Z later."

4. **Be engaging.** Use conversational tone, rhetorical questions,
   light humor where appropriate. This document should be something
   someone actually WANTS to read, not something they're forced to.
   If a section is boring, rewrite it until it isn't.

5. **Be honest about problems.** Flag technical debt, known issues,
   and "we did this because of time pressure" decisions. This document
   is more useful when it's truthful than when it's polished.

6. **Include "what could go wrong" for every major system.**
   Not to scare, but to prepare. "If the payment service goes down,
   here's what happens and here's what to do."

7. **Use progressive disclosure.** Start each section with the
   simple version, then go deeper. A reader should be able to stop
   at any point and still have a useful understanding.

8. **Format for scannability.** Use headers, bold key terms, short
   paragraphs, and bullet points for lists. But use prose (not bullets)
   for explanations and narratives.

## Example Tone

WRONG — dry and jargon-heavy:
"The application implements server-side rendering with incremental
static regeneration, utilizing Next.js App Router with React Server
Components for optimal TTFB."

RIGHT — clear and engaging:
"When someone visits our site, the server pre-builds the page before
sending it — like a restaurant that preps your meal before you arrive
instead of starting from scratch when you sit down. This is called
'server-side rendering' and it's why pages load fast. We use Next.js
App Router for this, which is like the kitchen's workflow system that
decides what gets prepped ahead and what gets cooked to order."

WRONG — listing without context:
"Dependencies: React 18, Next.js 14, Tailwind CSS, Supabase, Stripe"

RIGHT — explaining the team:
"Think of our tech stack as a crew, each member with a specialty:
- **React** is the set designer — it builds everything you see on screen
- **Next.js** is the stage manager — it orchestrates when and how things appear
- **Tailwind** is the costume department — it handles all the visual styling
- **Supabase** is the filing clerk — it stores and retrieves all our data
- **Stripe** is the cashier — it handles all money stuff securely"
