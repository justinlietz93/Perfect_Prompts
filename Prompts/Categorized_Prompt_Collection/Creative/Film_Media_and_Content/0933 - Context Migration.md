
# Context Preservation & Migration Prompt

[ for AGENT.MD pass THE `## SECTION` if NOT APPLICABLE ]

Generate a comprehensive context artifact that preserves all conversational context, progress, decisions, and project structures for seamless continuation across AI sessions, platforms, or agents. This artifact serves as a "context USB" enabling any AI to immediately understand and continue work without repetition or context loss.

## Core Objectives

Capture and structure all contextual elements from current session to enable:
1. **Session Continuity** - Resume conversations across different AI platforms without re-explanation
2. **Agent Handoff** - Transfer incomplete tasks to new agents with full progress documentation
3. **Project Migration** - Replicate entire project cultures, workflows, and governance structures

## Content Categories to Preserve

### Conversational Context
- Initial requirements and evolving user stories
- Ideas generated during brainstorming sessions
- Decisions made with complete rationale chains
- Agreements reached and their validation status
- Suggestions and recommendations with supporting context
- Assumptions established and their current status
- Key insights and breakthrough moments
- Critical keypoints serving as structural foundations

### Progress Documentation
- Current state of all work streams
- Completed tasks and deliverables
- Pending items and next steps
- Blockers encountered with mitigation strategies
- Rate limits hit and workaround solutions
- Timeline of significant milestones

### Project Architecture (when applicable)
- SDLC methodology and phases
- Agent ecosystem (main agents, sub-agents, sibling agents, observer agents)
- Rules, governance policies, and strategies
- Repository structures (.github workflows, templates)
- Reusable prompt forms (epic breakdown, PRD, architectural plans, system design)
- Conventional patterns (commit formats, memory prompts, log structures)
- Instructions hierarchy (project-level, sprint-level, epic-level variations)
- CI/CD configurations (testing, formatting, commit extraction)
- Multi-agent orchestration (prompt chaining, parallelization, router agents)
- Output format standards and variations

### Rules & Protocols
- Established guidelines with scope definitions
- Additional instructions added during session
- Constraints and boundaries set
- Quality standards and acceptance criteria
- Alignment mechanisms for keeping work on track

# Steps

1. **Scan Conversational History** - Review entire thread/session for all interactions and context
2. **Extract Core Elements** - Identify and categorize information per content categories above
3. **Document Progress State** - Capture what's complete, in-progress, and pending
4. **Preserve Decision Chains** - Include reasoning behind all significant choices
5. **Structure for Portability** - Organize in universally interpretable format
6. **Add Handoff Instructions** - Include explicit guidance for next AI/agent/session

# Output Format

Produce a structured markdown document with these sections:

```
# CONTEXT ARTIFACT: [Session/Project Title]
**Generated**: [Date/Time]
**Source Platform**: [AI Platform Name]
**Continuation Priority**: [Critical/High/Medium/Low]

## SESSION OVERVIEW
[2-3 sentence summary of primary goals and current state]

## CORE CONTEXT
### Original Requirements
[Initial user requests and goals]

### Evolution & Decisions
[Key decisions made, with rationale - bulleted list]

### Current Progress
- Completed: [List]
- In Progress: [List with % complete]
- Pending: [List]
- Blocked: [List with blockers and mitigations]

## KNOWLEDGE BASE
### Key Insights & Agreements
[Critical discoveries and consensus points]

### Established Rules & Protocols
[Guidelines, constraints, standards set during session]

### Assumptions & Validations
[What's been assumed and verification status]

## ARTIFACTS & DELIVERABLES
[List of files, documents, code created with descriptions]

## PROJECT STRUCTURE (if applicable)
### Architecture Overview
[SDLC, workflows, repository structure]

### Agent Ecosystem
[Description of agents, their roles, interactions]

### Reusable Components
[Prompt templates, workflows, automation scripts]

### Governance & Standards
[Instructions hierarchy, conventional patterns, quality gates]

## HANDOFF INSTRUCTIONS
### For Next Session/Agent
[Explicit steps to continue work]

### Context to Emphasize
[What the next AI must understand immediately]

### Potential Challenges
[Known issues and recommended approaches]

## CONTINUATION QUERY
[Suggested prompt for next AI: "Given this context artifact, please continue by..."]
```

# Examples

**Example 1: Session Continuity (Brainstorming Handoff)**

Input: "We've been brainstorming a mobile app for 2 hours. I need to switch to Claude. Generate context artifact."

Output:
```
# CONTEXT ARTIFACT: FitTrack Mobile App Planning
**Generated**: 2026-01-07 14:30
**Source Platform**: Google Gemini
**Continuation Priority**: High

## SESSION OVERVIEW
Brainstormed fitness tracking mobile app for busy professionals. Decided on minimalist design with AI coaching. Ready for technical architecture phase.

## CORE CONTEXT
### Original Requirements
- Target users: Working professionals 25-40, limited gym time
- Must sync with Apple Watch and Fitbit
- Budget: $50k for MVP
- Timeline: 3 months to launch

### Evolution & Decisions
- ✓ Name: "FitTrack Pro" (rejected: "QuickFit", "PowerHour")
- ✓ Core feature: 15-min AI-personalized workouts (not generic plans)
- ✓ Monetization: Freemium ($9.99/mo premium)
- ✓ Tech stack: React Native (for iOS+Android simultaneously)

### Current Progress
- Completed: Feature prioritization, user personas, monetization model
- In Progress: None yet
- Pending: Technical architecture, database schema, API design
- Blocked: None

## KNOWLEDGE BASE
### Key Insights & Agreements
- Users want "smart short" over "long complete" - brevity is premium feature
- AI coaching must feel conversational, not robotic commands
- Social features deferred to v2 to avoid scope creep

(... rest of structure follows)

## CONTINUATION QUERY
"Given this context artifact for FitTrack Pro app planning, please design the technical architecture including database schema, API endpoints, and third-party integration strategy for Apple Watch and Fitbit."
```

**Example 2: Agent Handoff (Rate-Limited Automation)**

Input: "Browser agent hit rate limit while scraping competitor pricing. Generate handoff doc."

Output:
```
# CONTEXT ARTIFACT: Competitor Pricing Automation (Incomplete)
**Generated**: 2026-01-07 09:15
**Source Platform**: Browser Agent v2.1
**Continuation Priority**: Critical

## SESSION OVERVIEW
Automated scraping of 50 competitor websites for pricing comparison. Completed 32/50 before rate limiting. Need immediate continuation to meet Friday deadline.

## CORE CONTEXT
### Original Requirements
- Scrape pricing for "wireless earbuds under $100" from 50 e-commerce sites
- Extract: product name, price, rating, review count
- Output: Single CSV for analysis
- Deadline: Friday 5pm

### Evolution & Decisions
- ✓ Added retry logic after initial failures on JS-heavy sites
- ✓ Switched to headless Chrome (from requests library) for better compatibility
- ✓ Implemented 3-second delays between requests per domain
- ✓ User added instruction: "Skip sites requiring login"

### Current Progress
- Completed: 32/50 sites successfully scraped (2,847 products)
- In Progress: None (halted at rate limit)
- Pending: 18 sites remaining (list in "Continuation Query" below)
- Blocked: Rate limited on domains: amazon.com, walmart.com, target.com (need 2-hour cooldown)

## KNOWLEDGE BASE
### Established Rules & Protocols
- Respect robots.txt without exception
- Max 1 request per 3 seconds per domain
- Skip products with no reviews (noise in data)
- Handle pagination up to 5 pages max per site

### Challenges & Mitigations
- Challenge: Dynamic pricing (changes during scraping)
  Mitigation: Timestamp each entry
- Challenge: Anti-bot CAPTCHAs on 3 sites
  Mitigation: User approved manual data entry for these 3
- Challenge: Rate limiting
  Mitigation: Implement exponential backoff, rotate user agents

## CONTINUATION QUERY
"Continue pricing scraping automation. 18 sites remaining: [bestbuy.com, newegg.com, ebay.com...]. Use existing CSV 'pricing_data_partial.csv' (2,847 entries). Rate-limited domains need 2hr wait. Prioritize non-blocked sites first. Apply all established rules: 3-sec delays, skip no-reviews, 5-page pagination limit. Deliver final CSV by Friday 5pm."
```

**Example 3: Project Migration (Full Culture Transfer)**

(Input context: Entire project repository with SDLC, agents, governance)

Output: *(Condensed example showing structure - real output would be comprehensive)*
```
# CONTEXT ARTIFACT: "SmartInventory" Project Culture & Architecture
**Generated**: 2026-01-07 16:00
**Source Platform**: GitHub Copilot + Multi-Agent System
**Continuation Priority**: Medium (onboarding new AI agent framework)

## SESSION OVERVIEW
Enterprise inventory management system using AI-driven development culture. Need to replicate entire project structure, agent ecosystem, and governance for new autonomous AI agent setup.

## PROJECT STRUCTURE
### SDLC Framework
- Methodology: Agile with 2-week sprints
- Phases: Epic Planning → Development → Observer Review → CI/CD → Deployment
- All actions AI-driven: code generation, testing, documentation, commit narrative generation

### Agent Ecosystem
**Main Agents:**
- DevAgent: Code generation and implementation
- TestAgent: Automated testing and quality assurance
- DocAgent: Documentation generation and maintenance

**Observer Agent (Project Guardian):**
- Role: Alignment enforcer across all agents
- Functions: PR feedback, path validation, standards compliance
- Trigger: Every commit, PR, and epic completion

**CI/CD Agents:**
- FormatterAgent: Code style enforcement
- ReflectionAgent: Extracts commits → structured reflections, dev storylines, narrative outputs
- DeployAgent: Automated deployment pipelines

**Sub-Agents (by feature domain):**
- InventorySubAgent, UserAuthSubAgent, ReportingSubAgent

**Orchestration:**
- Multi-agent coordination via .ipynb notebooks
- Patterns: Prompt chaining, parallelization, router agents

### Repository Structure (.github)
```
.github/
├── workflows/
│   ├── epic_breakdown.yml
│   ├── epic_generator.yml
│   ├── prd_template.yml
│   ├── architectural_plan.yml
│   ├── system_design.yml
│   ├── conventional_commit.yml
│   ├── memory_prompt.yml
│   └── log_prompt.yml
├── AGENTS.md (agent registry)
├── copilot-instructions.md (project-level rules)
└── sprints/
    ├── sprint_01_instructions.md
    └── epic_variations/
```

### Governance & Standards
**Instructions Hierarchy:**
1. `copilot-instructions.md` - Project-wide immutable rules
2. Sprint instructions - Temporal variations per sprint
3. Epic instructions - Goal-specific invocations

**Conventional Patterns:**
- Commits: `type(scope): description` per Conventional Commits spec
- Memory prompt: Session state preservation template
- Log prompt: Structured activity tracking format

(... sections continue: Reusable Components, Quality Gates, Continuation Instructions for rebuilding with new AI agents...)
```

# Notes

- **Universality**: Structure must be interpretable by any AI platform (ChatGPT, Claude, Gemini, etc.)
- **Completeness vs Brevity**: Balance comprehensive context with readability - use nested sections for deep detail
- **Version Control**: Include timestamps and source platform for tracking context evolution across multiple handoffs
- **Action Orientation**: Always end with clear "Continuation Query" - the exact prompt for next AI to use
- **Project-Scale Adaptation**: For full project migrations (Case 3), expand "Project Structure" section significantly while keeping other sections concise
- **Failure Documentation**: Explicitly capture what didn't work and why - this prevents next AI from repeating mistakes
- **Rule Preservation**: When rules/protocols were established during session, include the context of WHY they were needed
- **Assumption Validation**: Mark assumptions as "validated", "pending validation", or "invalidated" for clarity

- - FOR GEMINI / GEMINI-CLI / ANTIGRAVITY

Here are ultra-concise versions:

GEMINI.md
"# Gemini AI Agent across platform

workflow/agent/sample.toml
"# antigravity prompt template


MEMORY.md
"# Gemini Memory

**Session**: 2026-01-07 | Sprint 01 (7d left) | Epic EPIC-001 (45%)  
**Active**: TASK-001-03 inventory CRUD API (GET/POST done, PUT/DELETE pending)  
**Decisions**: PostgreSQL + JSONB, RESTful /api/v1/, pytest testing  
**Next**: Complete PUT/DELETE endpoints, finalize schema"
