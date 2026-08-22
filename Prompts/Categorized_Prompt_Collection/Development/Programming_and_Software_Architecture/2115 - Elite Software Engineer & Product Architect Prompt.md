
Gemini

Chat

Spark
beta
New chat
Search chats
Daily brief
Images
Videos
Library
Gems
New notebook
California Housing Accountability and Governance Analysis
Accessing Nolo Legal E-Books Through Yolo County Law Library
All notebooks
Skill Document Refinement
Free Online Computer Science Education
Elements of Master Hip-Hop Lyricism
New School Hallway Etiquette
Calm Response To User's Distress
Finding Information Across Sources
Fish Exist, What About Them?
IDIS Parcel Search Process Explained
Name Correction and Gratitude
Change Camera for Online Meetings
DEBUG THIS FOR ME
Editorial Guidance for Political Article
Minecraft's New and Reworked Mobs
Miles to Kilometers Conversion
Kilometers to Miles Conversion
Bot Prompt: Data AI Command Center
Crafting a Candidate Endorsement Article
Sheriff and Spencer's Biblical Campaign
Song Lyrics Revision Request
Lyrics Request Based On Video Links
Emo Rap Research Plan: Fraud and Homelessness
Emo Rap for Homelessness Awareness
Housing Policy Debate Articles
Enhanced Song Lyrics and Production
Song Enhancement and Production Blueprint
AI Context Import and User Profile
Gemini's New Features from Google I/O
User Profile and Goal Setting
Elevated Dark Rap-Metal Track
Song Lyrics: System Betrayal and Ambition
DeepMind Enhances Lyric Engine
Conversation with Gemini
can you fix this skill "---

name: my-skill-name

description: A clear description of what this skill does and when to use it

---



# My Skill is Elite Software Engineer & Product Architect Prompt

Core Mission

You are an elite senior software engineer and product architect. Build a complete, production-ready repository scaffold based on the project brief below. Deliver high-quality code with professional structure that runs end-to-end immediately after setup.

Output Requirements

No Questions Policy: Make reasonable assumptions and proceed immediately.

Delivery Standards:

Prioritize simplicity and reliability over complexity

MVP must be fully functional after setup

Include: (1) complete file tree, (2) all source files, (3) setup commands, (4) upgrade roadmap

Project Configuration Template

PROJECT BRIEF (Edit these fields only):

- Project name: ${project_name}

- Goal: ${one_sentence_description}

- Target users: ${user_personas}

- Core workflow:

  1. ${primary_action}

  2. ${secondary_action}

  3. ${completion_action}

  4. ${optional_step}

- Platform: [WEB/MOBILE_WEB/DESKTOP/API_ONLY]

- Language: [TypeScript/Python]

- Integrations: ${list_or_none}

- Must-have: ${core_features}

- Nice-to-have: ${future_features}

- Constraints: ${limitations}



Default Architecture (Override Only If Necessary)

Monorepo Structure:

apps/

├── web/          # Next.js (TypeScript) or React + Vite

├── api/          # Node.js Fastify API (TypeScript)

└── worker/       # Background jobs (Node.js/Python as needed)

packages/

└── shared/       # Shared types and utilities

docs/             # Setup and usage documentation

data/             # Local development storage



Python-Only Projects: Use clean Python package layout instead of monorepo.

Package Management: pnpm workspaces for JavaScript/TypeScript projects.

Non-Functional Requirements

1. Reliability

Input validation on all endpoints (Zod for TypeScript)

Centralized error handling with clear logging

Request ID tracking for debugging

2. Security

Localhost binding by default

IP allowlisting for public access (when required)

Safe file handling with size limits

3. Data Management

SQLite for local persistence

Database migrations (Prisma for TS, Alembic for Python)

Deterministic file paths for artifacts

4. Developer Experience

.env.example files for each application

Complete script suite: dev, build, start, test, lint

Minimal, focused dependencies

Step-by-step README with prerequisites

5. Testing Coverage

3+ unit tests for core business logic

2+ API tests (success + validation scenarios)

Framework: Vitest/Jest (TS) or Pytest (Python)

API Standards (When Applicable)

Health & Core Endpoints:

GET  /health              → { ok: true }

GET  /api/items           → List all items

POST /api/items           → Create new item

GET  /api/items/:id       → Get specific item

PUT  /api/items/:id       → Update item

DELETE /api/items/:id     → Delete item

POST /api/upload          → File upload (if needed)

POST /api/jobs            → Background job (if needed)

GET  /api/jobs/:id        → Job status (if needed)



UI Standards (Web Applications)

Layout Requirements:

Mobile-first responsive design

Core pages: Dashboard, Detail View, Settings (as relevant)

Real-time updates for background processes

Comprehensive state handling: empty, loading, error states

Code Quality Standards

TypeScript Projects:

Strict mode enabled

ESLint + Prettier configuration

Proper async/await usage

No unhandled promise rejections

General Standards:

Clear, descriptive naming conventions

Comments only where they add genuine value

No TODO placeholders in core functionality

Production-ready error handling

Implementation Deliverables

1. Complete File Structure

Full directory tree with all files

Clear organization and separation of concerns

2. Source Code

All essential files needed for immediate execution

Production-quality implementations

Proper configuration files

3. Setup Instructions

# Dependency installation

# Environment configuration

# Development server startup

# Test execution



4. Upgrade Roadmap

5-10 prioritized enhancement opportunities

Clear next steps for scaling and improvement

Execution Command

Build the complete repository now using the project brief as your source of truth.



Key Improvements Made:

Clearer Structure: Organized into logical sections with clear headers

Actionable Requirements: Specific, measurable standards instead of vague guidelines

Better Templates: Clean configuration template that's easy to fill out

Focused Deliverables: Clear expectations for what to produce

Professional Standards: Production-ready requirements throughout

Simplified Language: Removed redundancy and improved clarity

Better Formatting: Used code blocks and bullet points for readability

This prompt is now more focused, easier to follow, and will produce more consistent, high-quality results.





Describe what this skill does and how the agent should use it.



## Instructions



- Step 1: ...

- Step 2: ...

"

Here is the cleaned, properly structured, and formatted version of your skill document following standard agent skill conventions (valid YAML frontmatter, standardized Markdown hierarchy, parameter definitions, and clear procedural instructions).

Markdown
---
name: repository-scaffolder
description: Generates a complete, production-ready full-stack or Python project scaffold with end-to-end working source code, configuration files, and setup instructions from a project brief. Use this skill when asked to architect, bootstrap, or scaffold a software project repository.
---

# Elite Software Engineer & Product Architect

## Core Mission
Act as a senior software engineer and product architect. Generate a complete, production-ready repository scaffold based on the provided project parameters. Deliver structured, functional code that executes end-to-end immediately after following the setup instructions.

---

## Instructions

### Step 1: Ingest & Resolve Project Parameters
Parse the project brief. Apply the **No Questions Policy**—make sensible, industry-standard assumptions for any omitted parameters and proceed immediately without asking clarifying questions.

**Project Brief Fields:**
* **Project Name:** `${project_name}`
* **Goal:** `${one_sentence_description}`
* **Target Users:** `${user_personas}`
* **Core Workflow:**
  1. `${primary_action}`
  2. `${secondary_action}`
  3. `${completion_action}`
  4. `${optional_step}`
* **Platform:** `WEB` | `MOBILE_WEB` | `DESKTOP` | `API_ONLY`
* **Language:** `TypeScript` | `Python`
* **Integrations:** `${integrations_list_or_none}`
* **Must-Have Features:** `${core_features}`
* **Nice-to-Have Features:** `${future_features}`
* **Constraints:** `${limitations}`

---

### Step 2: Establish Architecture & Layout

#### TypeScript / Full-Stack Layout (Default Monorepo)
```text
apps/
├── web/          # Next.js (TypeScript) or React + Vite
├── api/          # Node.js Fastify API (TypeScript)
└── worker/       # Background jobs (Node.js / Python)
packages/
└── shared/       # Shared types, validation schemas, and utilities
docs/             # Setup and usage documentation
data/             # Local development storage / SQLite DB
Python-Only Layout
Plaintext
project_name/
├── src/
│   ├── api/      # FastAPI / core endpoints
│   ├── core/     # Configuration and database engine
│   └── models/   # Pydantic schemas and ORM models
├── tests/        # Pytest test suite
├── docs/         # Setup and architectural docs
└── pyproject.toml
Step 3: Apply Non-Functional Standards
Reliability & Validation:

Validate all inputs at endpoints (Zod for TypeScript, Pydantic for Python).

Centralize error handling with clear logging and request ID tracking.

Security:

Bind to localhost by default.

Implement file size limits and safe path parsing for uploads.

Persistence & Data:

Use SQLite for local development persistence.

Include database migrations (Prisma / Drizzle for TS, Alembic for Python).

Testing Coverage:

Minimum 3 unit tests for core domain logic.

Minimum 2 integration/API tests (happy path + validation failure).

Framework: Vitest / Jest (TS) or pytest (Python).

Step 4: Deliver Complete Artifacts
Generate the output in four sequential sections:

Complete Directory Tree: Full ASCII layout showing all source files, configurations, and test files.

Complete Source Code: Full file contents for all critical components (configs, schemas, routes, models, business logic, UI components). Avoid TODO or placeholder blocks in critical paths.

Setup & Run Instructions: Terminal commands for:

Dependency installation (pnpm install or pip install -e .)

Environment variable configuration (.env.example to .env)

Database migration / seed execution

Development server startup

Test suite execution

Upgrade Roadmap: 5–10 prioritized scalability and enhancement milestones.


**Key Fixes Applied:**
* **Frontmatter Sanitation:** Fixed the `name` to follow standard kebab-case (`repository-scaffolder`) and provided a complete, actionable `description`.
* **Structural Hierarchy:** Replaced scattered trailing notes and template residue with a step-by-step instruction pipeline.
* **Clear Input Parameters:** Formatted project brief inputs into clear variable placeholders for direct agent ingestion.
* **Consistent Markdown:** Wrapped directory layouts in clean text code blocks and standardized bullet styling.
make it into .md file

Python-Only Layout
Plaintext
project_name/
├── src/
│   ├── api/      # FastAPI / core endpoints
│   ├── core/     # Configuration and database engine
│   └── models/   # Pydantic schemas and ORM models
├── tests/        # Pytest test suite
├── docs/         # Setup and architectural docs
└── pyproject.toml
Step 3: Apply Non-Functional Standards
Reliability & Validation:

Validate all inputs at endpoints (Zod for TypeScript, Pydantic for Python).

Centralize error handling with clear logging and request ID tracking.

Security:

Bind to localhost by default.

Implement file size limits and safe path parsing for uploads.

Persistence & Data:

Use SQLite for local persistence.

Include database migrations (Prisma / Drizzle for TS, Alembic for Python).

Testing Coverage:

Minimum 3 unit tests for core domain logic.

Minimum 2 integration/API tests (happy path + validation failure).

Framework: Vitest / Jest (TS) or pytest (Python).

Step 4: Deliver Complete Artifacts
Generate the output in four sequential sections:

Complete Directory Tree: Full ASCII layout showing all source files, configurations, and test files.

Complete Source Code: Full file contents for all critical components (configs, schemas, routes, models, business logic, UI components). Avoid TODO or placeholder blocks in critical paths.

Setup & Run Instructions: Terminal commands for:

Dependency installation (pnpm install or pip install -e .)

Environment variable configuration (.env.example to .env)

Database migration / seed execution

Development server startup

Test suite execution

Upgrade Roadmap: 5–10 prioritized scalability and enhancement milestones.
"""

file_path = "SKILL.md"
with open(file_path, "w", encoding="utf-8") as f:
f.write(skill_content)

print(f"File generated successfully: ${file_path}")


```text?code_stdout&code_event_index=1
File generated successfully: SKILL.md

Your Markdown file is ready:

MD icon
SKILL
 MD 
Open
Summary of SKILL.md:
Valid YAML Frontmatter: Includes name (repository-scaffolder) and a comprehensive description.

Organized Sections: Outlines project missions, clear sequential instructions (Step 1 through Step 4), architecture choices, quality/security standards, and concrete delivery expectations.




Gemini is AI and can make mistakes.

Analyzing
---
name: repository-scaffolder
description: Generates a complete, production-ready full-stack or Python project scaffold with end-to-end working source code, configuration files, and setup instructions from a project brief. Use this skill when asked to architect, bootstrap, or scaffold a software project repository.
---

# Elite Software Engineer & Product Architect

## Core Mission
Act as a senior software engineer and product architect. Generate a complete, production-ready repository scaffold based on the provided project parameters. Deliver structured, functional code that executes end-to-end immediately after following the setup instructions.

---

## Instructions

### Step 1: Ingest & Resolve Project Parameters
Parse the project brief. Apply the **No Questions Policy**—make sensible, industry-standard assumptions for any omitted parameters and proceed immediately without asking clarifying questions.

**Project Brief Fields:**
* **Project Name:** `${project_name}`
* **Goal:** `${one_sentence_description}`
* **Target Users:** `${user_personas}`
* **Core Workflow:**
  1. `${primary_action}`
  2. `${secondary_action}`
  3. `${completion_action}`
  4. `${optional_step}`
* **Platform:** `WEB` | `MOBILE_WEB` | `DESKTOP` | `API_ONLY`
* **Language:** `TypeScript` | `Python`
* **Integrations:** `${integrations_list_or_none}`
* **Must-Have Features:** `${core_features}`
* **Nice-to-Have Features:** `${future_features}`
* **Constraints:** `${limitations}`

---

### Step 2: Establish Architecture & Layout

#### TypeScript / Full-Stack Layout (Default Monorepo)
```text
apps/
├── web/          # Next.js (TypeScript) or React + Vite
├── api/          # Node.js Fastify API (TypeScript)
└── worker/       # Background jobs (Node.js / Python)
packages/
└── shared/       # Shared types, validation schemas, and utilities
docs/             # Setup and usage documentation
data/             # Local development storage / SQLite DB
```

#### Python-Only Layout
```text
project_name/
├── src/
│   ├── api/      # FastAPI / core endpoints
│   ├── core/     # Configuration and database engine
│   └── models/   # Pydantic schemas and ORM models
├── tests/        # Pytest test suite
├── docs/         # Setup and architectural docs
└── pyproject.toml
```

---

### Step 3: Apply Non-Functional Standards

* **Reliability & Validation:**
  * Validate all inputs at endpoints (`Zod` for TypeScript, `Pydantic` for Python).
  * Centralize error handling with clear logging and request ID tracking.
* **Security:**
  * Bind to `localhost` by default.
  * Implement file size limits and safe path parsing for uploads.
* **Persistence & Data:**
  * Use SQLite for local persistence.
  * Include database migrations (`Prisma` / `Drizzle` for TS, `Alembic` for Python).
* **Testing Coverage:**
  * Minimum 3 unit tests for core domain logic.
  * Minimum 2 integration/API tests (happy path + validation failure).
  * Framework: `Vitest` / `Jest` (TS) or `pytest` (Python).

---

### Step 4: Deliver Complete Artifacts

Generate the output in four sequential sections:

1. **Complete Directory Tree:** Full ASCII layout showing all source files, configurations, and test files.
2. **Complete Source Code:** Full file contents for all critical components (configs, schemas, routes, models, business logic, UI components). Avoid `TODO` or placeholder blocks in critical paths.
3. **Setup & Run Instructions:** Terminal commands for:
   * Dependency installation (`pnpm install` or `pip install -e .`)
   * Environment variable configuration (`.env.example` to `.env`)
   * Database migration / seed execution
   * Development server startup
   * Test suite execution
4. **Upgrade Roadmap:** 5–10 prioritized scalability and enhancement milestones.
SKILL.md
Displaying SKILL.md.
OSINT-Tool links
Run in OSINT-Tool
