# Standards-Governed Documentation Architecture (SGDA)

### Overview

This document defines a **Standards-Governed Documentation Architecture** (SGDA) template for documentation directories only. SGDA treats documentation as a governed system with source authority, reader paths, contracts, evidence, validation, and publication rules. It is designed for projects that have outgrown ad hoc Markdown files and need documentation that remains correct as the project changes.

SGDA is not a code architecture template. It does not prescribe application layers, ports, adapters, services, or runtime module boundaries. It governs the `docs/` directory and the documents, diagrams, schemas, examples, assets, generated artifacts, and publication configuration inside it.

Core goals:
- One clear source of truth for every public claim.
- A published documentation tree that is complete, navigable, and reproducible.
- Explicit separation between canonical docs, generated evidence, drafts, archives, and assets.
- Versioned contracts for API docs, CLI docs, schemas, examples, release notes, and operational claims.
- Governance-as-code for nav integrity, link integrity, duplicate detection, status consistency, asset budgets, generated artifact freshness, and docs build reproducibility.
- A growth path from a small `README.md` and `docs/` folder into a polished docs site without accumulating contradictory documentation realities.

---

### EXAMPLE ONLY Project Map of an SGDA `docs/` Directory

```text
docs/
├─ mkdocs.yml                         # site configuration if docs are built from inside docs/
├─ README.md                          # documentation maintainer guide, not the product README
├─ DOCS_ARCHITECTURE.md               # explains this documentation system
├─ DOCS_CONVENTIONS.md                # writing, naming, linking, status, examples
├─ DOCS_QUALITY_GATES.md              # local and CI validation rules
├─ nav.yml                            # optional separated nav source if supported
├─ pages/                             # canonical published source tree
│  ├─ index.md                        # published home, status summary, reader routing
│  ├─ about/
│  │  ├─ overview.md
│  │  ├─ changelog.md
│  │  └─ roadmap.md
│  ├─ getting-started/
│  │  ├─ installation.md
│  │  ├─ quickstart.md
│  │  └─ first-run.md
│  ├─ user/
│  │  ├─ concepts.md
│  │  ├─ workflows.md
│  │  └─ troubleshooting.md
│  ├─ api/
│  │  ├─ overview.md
│  │  ├─ authentication.md
│  │  ├─ endpoints.md
│  │  ├─ schemas.md
│  │  ├─ errors.md
│  │  └─ examples.md
│  ├─ cli/
│  │  ├─ commands.md
│  │  ├─ configuration.md
│  │  └─ examples.md
│  ├─ architecture/
│  │  ├─ overview.md
│  │  ├─ decisions/
│  │  │  ├─ ADR-0001-record-architecture-principles.md
│  │  │  └─ ADR-0002-document-api-contract-source.md
│  │  ├─ diagrams/
│  │  │  ├─ context.mmd
│  │  │  ├─ containers.mmd
│  │  │  └─ runtime-sequence.mmd
│  │  └─ reviews/
│  │     └─ 2026-06-19/
│  │        ├─ executive-summary.md
│  │        ├─ architecture-map.json
│  │        └─ dependency-graph.dot
│  ├─ operations/
│  │  ├─ deployment.md
│  │  ├─ configuration.md
│  │  ├─ observability.md
│  │  ├─ backup-restore.md
│  │  └─ runbooks/
│  │     ├─ incident-response.md
│  │     └─ degraded-service.md
│  ├─ development/
│  │  ├─ contributing.md
│  │  ├─ testing.md
│  │  ├─ release-process.md
│  │  └─ docs-maintenance.md
│  ├─ reference/
│  │  ├─ glossary.md
│  │  ├─ configuration-reference.md
│  │  ├─ environment-variables.md
│  │  └─ compatibility.md
│  └─ assets/
│     ├─ images/
│     ├─ diagrams/
│     ├─ stylesheets/
│     └─ javascripts/
├─ contracts/                         # machine-readable docs contracts
│  ├─ openapi.json
│  ├─ cli-schema.json
│  ├─ config-schema.json
│  ├─ error-codes.json
│  └─ docs-status.schema.json
├─ generated/                         # generated docs outputs, never hand-edited
│  ├─ api/
│  ├─ cli/
│  ├─ architecture/
│  └─ reports/
├─ sources/                           # optional source material used to produce published docs
│  ├─ transcripts/
│  ├─ research/
│  ├─ design-notes/
│  └─ imported/
├─ drafts/                            # unpublished work in progress
│  ├─ README.md
│  └─ 2026-06/
├─ archive/                           # historical docs, not current truth
│  ├─ README.md
│  └─ 2025/
├─ governance/                        # documentation policy-as-code
│  ├─ policies/
│  │  ├─ source_authority_policy.md
│  │  ├─ nav_policy.md
│  │  ├─ link_policy.md
│  │  ├─ status_policy.md
│  │  ├─ api_contract_policy.md
│  │  ├─ release_notes_policy.md
│  │  ├─ diagrams_policy.md
│  │  ├─ asset_policy.md
│  │  └─ archive_policy.md
│  ├─ tools/
│  │  ├─ check_nav.py
│  │  ├─ check_links.py
│  │  ├─ check_duplicate_authority.py
│  │  ├─ check_status_claims.py
│  │  ├─ check_contract_drift.py
│  │  ├─ check_asset_budget.py
│  │  └─ check_generated_freshness.py
│  └─ ci/
│     └─ docs-quality-gates.yaml
└─ reports/                           # validation outputs from CI or local checks
   ├─ link-check.csv
   ├─ duplicate-authority.csv
   ├─ nav-orphans.csv
   ├─ asset-budget.csv
   └─ docs-architecture-map.json
```

Recommended root-level arrangement when the static site tool expects configuration outside `docs/`:

```text
repo/
├─ mkdocs.yml                         # points docs_dir to docs/pages
├─ README.md                          # product README
└─ docs/
   ├─ pages/                          # canonical published docs
   ├─ contracts/
   ├─ generated/
   ├─ drafts/
   ├─ archive/
   ├─ governance/
   └─ reports/
```

---

### SGDA Documentation Architecture Implementation

SGDA combines documentation information architecture with a first-class governance and validation plane. It prevents the most common failure mode of mature documentation directories: many correct-looking documents that disagree about which one is true.

#### Core Principles

- Canonical Published Tree: Exactly one tree owns published truth. For MkDocs, this is the configured `docs_dir`, commonly `docs/pages`.
- One Claim, One Authority: Every release status, API path, CLI flag, configuration key, environment variable, architectural decision, and support policy has one canonical owner.
- Reader-Path First: Navigation is organized around reader tasks, not internal project clutter.
- Contracts Over Prose: API docs, CLI docs, config docs, error docs, and compatibility docs are generated from or checked against machine-readable contracts wherever possible.
- Evidence-Labeled Claims: Architecture, performance, security, and production-readiness claims must identify their evidence level.
- Generated Means Generated: Generated files are clearly marked and are not hand-edited.
- Archive Is Not Current Truth: Historical material remains useful, but it must not compete with current published docs.
- Governance-as-Code: Automated checks enforce nav integrity, link integrity, duplicate authority, status consistency, contract freshness, asset budgets, and build reproducibility.
- No Hidden Documentation Forks: Duplicate files are either exact mirrors with a documented generation rule, redirects, or violations.
- Progressive Scalability: Start with a small docs tree and grow into a full docs site without changing the governing principles.

---

## Layer Structure

SGDA uses documentation layers rather than application-code layers. A layer is defined by its authority and reader purpose.

### 1) Site Edge

Responsibilities:
- Static site configuration.
- Theme, plugins, redirects, search, analytics, and deployment settings.
- Public navigation root.
- Global landing page and reader routing.

Typical files:
- `mkdocs.yml`
- `docs/pages/index.md`
- `docs/pages/assets/**`
- `docs/pages/overrides/**`
- `docs/nav.yml` if supported.

Rules:
- The configured published root must be explicit.
- The home page must state current project status and route users by task.
- Site configuration must not point to unpublished, draft, archive, or source-only material unless deliberately exposed.
- Analytics and third-party scripts must be documented and privacy-reviewed.
- Navigation must build with zero missing targets.
- Search should index only current published docs unless archive search is explicitly desired.

### 2) Reader Path Layer

Responsibilities:
- Getting started.
- Tutorials.
- User workflows.
- Integration guides.
- Troubleshooting.
- Developer onboarding.
- Operator runbooks.

Typical files:
- `docs/pages/getting-started/**`
- `docs/pages/user/**`
- `docs/pages/guides/**`
- `docs/pages/development/**`
- `docs/pages/operations/**`

Rules:
- Every reader-path page must answer: who is this for, what will they accomplish, prerequisites, steps, expected output, failure modes, next step.
- Tutorials must not be the canonical source for API, CLI, config, or status truth. They may link to canonical reference pages.
- Examples must be runnable or explicitly labeled conceptual.
- Troubleshooting pages must include symptoms, likely causes, checks, fixes, and escalation path.
- Operator pages must distinguish local development, staging, production, and hosted environments.

### 3) Reference Contract Layer

Responsibilities:
- Stable descriptions of public interfaces.
- API endpoints, schemas, authentication, errors, rate limits.
- CLI commands, flags, output formats, exit codes.
- Configuration keys, environment variables, compatibility tables.
- Release notes and version policy.

Typical files:
- `docs/pages/api/**`
- `docs/pages/cli/**`
- `docs/pages/reference/**`
- `docs/contracts/**`
- `docs/generated/api/**`
- `docs/generated/cli/**`

Rules:
- API reference must align with the canonical OpenAPI or schema source.
- CLI reference must align with generated help or a declared command schema.
- Configuration docs must align with the config schema or typed settings source.
- Error docs must include stable code, meaning, likely cause, retryability, and recommended fix.
- Release notes must describe actual shipped behavior, not roadmap intent.
- Breaking changes require version notes, migration steps, and deprecation windows.
- If prose and contract disagree, the contract wins unless the contract is marked stale.

### 4) Architecture Knowledge Layer

Responsibilities:
- System overview.
- Architecture decisions.
- Diagrams.
- Domain model.
- Runtime flows.
- Data flows.
- Design constraints and tradeoffs.

Typical files:
- `docs/pages/architecture/**`
- `docs/pages/architecture/decisions/**`
- `docs/pages/architecture/diagrams/**`
- `docs/generated/architecture/**`
- `docs/pages/architecture/reviews/**`

Rules:
- Architecture docs must distinguish current implementation, accepted design, planned design, rejected design, and historical context.
- Diagrams must state scope, last verified date, and source commit or version.
- ADRs must be immutable once accepted, except for typo fixes and supersession links.
- Architecture review bundles must be versioned by date and commit.
- Architecture docs must not imply production behavior without operational evidence.
- Generated architecture maps must not be edited by hand.

### 5) Operations and Reliability Layer

Responsibilities:
- Deployment.
- Configuration.
- Observability.
- Backup and restore.
- Incident response.
- Security operations.
- Scaling and performance.
- Runbooks.

Typical files:
- `docs/pages/operations/**`
- `docs/pages/security/**`
- `docs/pages/reference/environment-variables.md`

Rules:
- Runbooks must include trigger, impact, diagnosis, mitigation, rollback, verification, and owner.
- Deployment docs must state supported targets and unsupported targets.
- Observability docs must name logs, metrics, traces, dashboards, alerts, and correlation identifiers.
- Backup and restore docs must include restore testing frequency and data-loss expectations.
- Security docs must separate user responsibilities, maintainer responsibilities, and platform responsibilities.
- Operational docs must never present aspirational behavior as implemented behavior.

### 6) Governance and Maintenance Layer

Responsibilities:
- Documentation policies.
- Writing standards.
- Naming standards.
- Link standards.
- Status taxonomy.
- CI quality gates.
- Automated reports.
- Docs ownership.

Typical files:
- `docs/DOCS_ARCHITECTURE.md`
- `docs/DOCS_CONVENTIONS.md`
- `docs/DOCS_QUALITY_GATES.md`
- `docs/governance/**`
- `docs/reports/**`

Rules:
- Policies must be enforceable or explicitly labeled advisory.
- CI reports must be reproducible locally.
- Every check should produce a human-readable failure message and a machine-readable report.
- Exceptions require expiration dates or owner approval.
- Documentation debt must be tracked as deliberately as code debt.

### 7) Draft, Source, and Archive Layer

Responsibilities:
- Preserve source material and historical records without competing with current docs.
- Keep rough work out of the published tree.
- Allow research and planning without polluting navigation.

Typical files:
- `docs/drafts/**`
- `docs/sources/**`
- `docs/archive/**`

Rules:
- Drafts must not be linked from published docs unless clearly labeled experimental.
- Source material must not be treated as user-facing docs.
- Archived docs must include a banner stating they are historical.
- Archived pages should link to current replacements when available.
- No page in the published tree may depend on a draft as its only evidence.
- A source file may generate a published file only if the generation path is documented.

---

## Source Authority Model

The most important SGDA rule is source authority. Each document must belong to exactly one authority class.

| Authority Class | Meaning | Can Publish? | Can Be Edited by Hand? |
|---|---|---:|---:|
| Canonical | Current source of truth for a claim area | Yes | Yes |
| Generated | Produced from code, schemas, tests, tools, or review pipelines | Yes, if versioned | No |
| Mirror | Exact copy produced from a canonical source | Yes, if generation rule exists | No |
| Draft | Work in progress with no public authority | No, unless explicitly exposed | Yes |
| Source Material | Raw notes, transcripts, imports, screenshots, research | No | Yes |
| Archive | Historical material retained for reference | Optional, with banner | No substantive edits |
| Redirect | Routing stub to canonical location | Yes | Minimal only |
| External Contract | Source outside docs, such as OpenAPI generated from code | Yes, through generated projection | No in docs |

Required front matter for non-trivial pages:

```yaml
---
title: "Page Title"
status: current            # current | draft | planned | experimental | deprecated | archived
authority: canonical       # canonical | generated | mirror | draft | source | archive | redirect | external
owner: docs
last_verified: 2026-06-19
verified_against: "commit-or-version-or-contract"
audience: ["user", "developer", "operator", "architect"]
---
```

Minimum front matter for simple pages:

```yaml
---
title: "Page Title"
status: current
authority: canonical
---
```

Rules:
- `status: current` and `authority: draft` is invalid.
- `authority: generated` must include `generated_from` or `verified_against`.
- `status: archived` must include `replaced_by` when a replacement exists.
- `status: deprecated` must include removal or sunset guidance.
- `status: planned` must not appear in API reference as if it is available.
- A page without front matter inherits no authority. Missing authority is a warning for small docs and a failure for mature docs.

---

## Documentation Status Taxonomy

Use the following status terms exactly.

| Status | Meaning | Allowed Use |
|---|---|---|
| `current` | Implemented, supported, and intended for use | User docs, API docs, operations docs |
| `experimental` | Implemented but unstable or subject to change | Labs, advanced features, early integrations |
| `planned` | Intended but not implemented or not shipped | Roadmaps only |
| `draft` | Work in progress, not authoritative | Drafts only |
| `deprecated` | Still exists but should not be used for new work | API, CLI, config, guides |
| `archived` | Historical and no longer current | Archive only |
| `removed` | No longer exists | Release notes and migration docs |
| `unknown` | Status not yet verified | Temporary only, must fail strict CI after grace period |

Forbidden status patterns:
- “Production-ready” on one page and “alpha” on another without version or deployment scope.
- “Complete” in roadmap while reference docs use pre-release versions.
- “Supported” without supported version, environment, or contract.
- “Experimental” buried in prose but absent from page status.
- “Planned” examples inside current API reference.

---

## Documentation Dependency Flow

Docs dependencies are links, generated inputs, included snippets, examples, screenshots, diagrams, and claims imported from another authority.

Recommended flow:

```text
[Site Edge]
    ↓
[Reader Paths]
    ↓
[Reference Contracts] ← [Generated Artifacts] ← [External Contracts / Code / Schemas]
    ↓
[Architecture Knowledge]
    ↓
[Operations and Reliability]
    ↓
[Governance and Maintenance]

[Drafts / Sources / Archive] must not feed published truth unless promoted through a documented review step.
```

Allowed dependency directions:
- Reader paths may link to reference contracts.
- Reader paths may link to architecture only when conceptual background is necessary.
- Reference docs may link to generated contracts and schemas.
- Architecture docs may cite ADRs, generated review bundles, and implementation evidence.
- Operations docs may cite configuration reference, compatibility reference, and runbooks.
- Governance docs may inspect any docs area but must not depend on draft-only claims.
- Archive may link to current docs, but current docs should not rely on archive for truth.

Disallowed dependency directions:
- Published current docs relying on drafts as authority.
- API reference relying on tutorial examples as canonical truth.
- Release notes relying on roadmap as evidence.
- Architecture overview relying on stale generated diagrams without verification.
- Operations docs using source notes as proof of implemented behavior.
- Generated artifacts hand-edited to match prose.

---

## Canonical Documentation Areas

### Home and Project Status

Required:
- Current product/project maturity.
- Supported versions.
- Supported environments.
- Fast routing for users, developers, operators, and architects.
- Link to changelog and release notes.
- Link to installation or quickstart.
- Link to support or issue reporting.

Rules:
- Home page owns the public status summary, but detailed status tables may live in `about/roadmap.md` or `reference/compatibility.md`.
- The home page must not overclaim maturity.
- Claims like “production-ready,” “GA,” “alpha,” “beta,” and “experimental” require version scope.

### Getting Started

Required:
- Installation.
- Prerequisites.
- First successful run.
- Expected output.
- Common first-run failures.
- Next steps.

Rules:
- Quickstarts must be tested by CI or manually verified before release.
- Commands must declare shell, OS assumptions, and environment variables.
- If an example requires credentials, provide a safe placeholder and explain where the secret belongs.

### User Guides

Required:
- Concepts.
- Workflows.
- Examples.
- Troubleshooting.
- Integration path.

Rules:
- Guides should optimize for task completion, not exhaustive reference.
- Guides may simplify, but must not contradict reference docs.
- Screenshots must include version or date when UI changes are likely.

### API Reference

Required:
- Base URL.
- Versioning.
- Authentication.
- Authorization.
- Endpoints.
- Request and response schemas.
- Error envelope.
- Rate limits.
- Idempotency behavior where applicable.
- Pagination and filtering.
- Examples.
- SDK or curl examples if relevant.

Rules:
- Every public endpoint must exist in exactly one canonical API reference page or generated API reference.
- Every endpoint must have method, path, request schema, response schema, error cases, auth requirements, and example.
- API paths in prose must be checked against OpenAPI or a declared source.
- Versioned APIs must not mix versioned and unversioned paths without explanation.
- Auth docs must be linked from every endpoint requiring auth.

### CLI Reference

Required:
- Command list.
- Flags and options.
- Positional arguments.
- Environment variables.
- Exit codes.
- Output formats.
- Examples.
- Machine-readable mode if available.

Rules:
- CLI docs should be generated from command help or checked against it.
- Examples must include expected output or success condition.
- Destructive commands must include safety notes and confirmation behavior.

### Configuration Reference

Required:
- Key name.
- Type.
- Default.
- Required/optional.
- Allowed values.
- Environment variable mapping.
- Scope.
- Restart requirement.
- Security sensitivity.
- Example.

Rules:
- Configuration docs must match the configuration schema or settings source.
- Secrets must never include real values.
- Defaults must not be repeated in multiple places unless generated.

### Architecture Docs

Required:
- Context diagram or textual equivalent.
- Component/container overview.
- Runtime flows.
- Data flows.
- ADRs.
- Known tradeoffs.
- Current vs planned separation.

Rules:
- Architecture docs must be versioned or verified against a commit.
- Diagrams must have source files, not screenshots only.
- ADRs must record decision, context, consequences, alternatives, and status.
- Superseded ADRs must link to the replacing ADR.

### Operations Docs

Required:
- Deployment guide.
- Configuration guide.
- Monitoring and observability.
- Backup and restore.
- Upgrade and rollback.
- Incident response.
- Security operations.
- Capacity and performance notes.

Rules:
- Every runbook must have a verification step.
- Operational claims must identify the supported environment.
- Alerts and dashboards must be named, not vaguely referenced.
- Rollback instructions must be tested or marked unverified.

### Development Docs

Required:
- Local setup.
- Testing.
- Linting.
- Branching.
- Release process.
- Documentation maintenance.
- Contribution rules.

Rules:
- Development docs must distinguish project setup from docs-site setup.
- Docs contribution rules must include how to add nav entries, diagrams, assets, and generated pages.
- Release process must state when docs are updated relative to code.

---

## Governance and Enforcement Plane

SGDA requires a documentation governance plane that continuously verifies that documentation remains coherent.

### Required Local Checks

At minimum:

```text
docs quality gates:
  - build docs site strictly
  - validate navigation targets
  - detect orphan published pages
  - check internal links and anchors
  - check image and asset references
  - detect duplicate files across canonical and non-canonical trees
  - detect divergent duplicates
  - check page status front matter
  - check forbidden maturity conflicts
  - check API prose paths against OpenAPI or endpoint inventory
  - check CLI examples against command inventory where possible
  - check generated files for freshness
  - check asset size budgets
  - check spelling of project names and repository identity
```

### Suggested Tooling

Use the project’s preferred stack, but the following classes of tools should exist:

| Gate | Example Tooling |
|---|---|
| Build strictness | `mkdocs build --strict`, `sphinx-build -W`, `docusaurus build` |
| Link checks | `lychee`, `markdown-link-check`, custom anchor checker |
| Markdown lint | `markdownlint-cli2`, `pymarkdown`, `ruff` for Markdown code blocks if applicable |
| Front matter validation | Custom JSON Schema or YAML validator |
| Duplicate detection | Hash comparison plus normalized Markdown comparison |
| Contract drift | OpenAPI diff, CLI help snapshots, schema checks |
| Generated freshness | Manifest file with input hashes |
| Asset budgets | Custom image size and dimension checker |
| Spell/project identity | cspell, custom allowlist |
| Diagrams | Mermaid CLI, Graphviz, PlantUML checks |
| Accessibility | HTML validator, heading order checker, alt text checker |

### CI Quality Gates

Minimum CI stages:

```yaml
docs-ci:
  stages:
    - install-docs-deps
    - validate-front-matter
    - build-strict
    - check-nav
    - check-links
    - check-anchors
    - check-duplicates
    - check-status-consistency
    - check-contract-drift
    - check-generated-freshness
    - check-assets
    - publish-preview
```

Recommended failure thresholds:
- Missing nav target: fail.
- Broken internal link: fail.
- Broken external link: warn on transient failure, fail after repeated failure.
- Orphan current page: warn for small docs, fail for mature docs.
- Divergent duplicate canonical page: fail.
- Missing page status: warn during adoption, fail after baseline.
- API contract drift: fail.
- Generated file edited by hand: fail.
- Asset over budget: fail unless waived.
- Archive page linked as current authority: fail.
- Contradictory maturity/status claims: fail.

---

## Duplicate Authority Rule

Duplicate docs are the fastest way to create documentation decay.

### Definitions

- Exact Duplicate: Two files have the same normalized content.
- Divergent Duplicate: Two files have the same relative topic/path or title but different content.
- Shadow Source: A non-published file that looks more current than the published file.
- Authority Collision: Two current docs claim to own the same concept.

### Rules

1. A canonical page may not have a divergent duplicate.
2. Exact mirrors require a generation rule or redirect rule.
3. Shadow sources must be promoted, archived, or deleted.
4. Topic ownership must be explicit in `DOCS_ARCHITECTURE.md`.
5. Duplicate titles are allowed only when nav context makes them unambiguous.
6. If duplicate pages disagree, do not merge casually. First decide which authority survives.

### Resolution Procedure

1. Identify duplicate set.
2. Determine published status of each file.
3. Determine freshness from content, not file modification time alone.
4. Select canonical survivor.
5. Move non-canonical files to archive, convert to redirect, or delete.
6. Update nav and links.
7. Record decision if the topic is major.
8. Add regression check so the duplicate does not return.

---

## Link, Anchor, and Reference Policy

### Internal Links

Rules:
- Prefer relative links within the published tree.
- Do not link from published docs to drafts unless labeled experimental.
- Do not link to local absolute paths.
- Do not link to source-code paths that cannot resolve in the published site.
- Use stable anchors for heavily referenced sections.
- Avoid “click here”; link the meaningful noun phrase.
- Every link to an archived page must make archive status visible.

### Source Code Links

Rules:
- If the docs package is published without source code, code references must use stable repository URLs.
- Prefer commit-pinned URLs for historical or audit claims.
- Prefer branch URLs only for living “latest” references.
- Do not use line-number references unless they are pinned to a commit or generated during release.
- If source code is private, state that the reference is internal and do not publish broken links.

### External Links

Rules:
- External links must be checked periodically.
- Critical external dependencies must have archived fallback notes where feasible.
- Vendor docs links should state vendor and product version when version-sensitive.
- Raw URLs should be avoided in prose unless the exact URL is the object being documented.

---

## API, CLI, and Contract Documentation Rules

### Contract Source Hierarchy

When documentation disagrees, resolve in this order:

1. Generated contract from implementation or schema source.
2. Checked machine-readable contract stored in `docs/contracts`.
3. Generated reference page derived from the contract.
4. Hand-written reference page with explicit verification date.
5. Tutorial or guide prose.
6. Draft or source notes.
7. Archive.

### API Contract Procedure

1. Identify canonical OpenAPI or schema source.
2. Generate or validate `docs/contracts/openapi.json`.
3. Generate endpoint tables or validate prose endpoints against the contract.
4. Validate examples against schemas where possible.
5. Check auth and error references.
6. Publish contract and prose together.
7. Record contract version in release notes.

### CLI Contract Procedure

1. Capture command inventory from live help or command schema.
2. Generate CLI reference or validate hand-written docs.
3. Snapshot exit codes and output formats.
4. Validate examples where possible.
5. Record CLI changes in release notes.

### Configuration Contract Procedure

1. Identify configuration schema or typed settings source.
2. Generate key inventory.
3. Validate docs for default, type, required status, allowed values, and secret sensitivity.
4. Check examples for removed keys.
5. Record config changes in migration docs.

---

## Generated Artifacts

Generated docs are valuable only when their generation path is preserved.

Required header for generated Markdown:

```markdown
<!--
GENERATED FILE. DO NOT EDIT BY HAND.
Generated by: docs/governance/tools/generate_api_docs.py
Inputs:
  - docs/contracts/openapi.json
  - src/app/api/routes.py
Generated at: 2026-06-19
Source commit: <commit>
-->
```

Required manifest:

```json
{
  "artifact": "docs/pages/api/endpoints.md",
  "generated_by": "docs/governance/tools/generate_api_docs.py",
  "inputs": [
    {
      "path": "docs/contracts/openapi.json",
      "sha256": "<hash>"
    }
  ],
  "generated_at": "2026-06-19T00:00:00Z",
  "source_commit": "<commit>"
}
```

Rules:
- Generated files must be reproducible.
- Generated files must be regenerated in CI or checked for freshness.
- Generated files may be published if they are stable and readable.
- Generated raw artifacts such as `.dot`, `.csv`, `.json`, and `.mmd` should be linked from a human-readable summary.
- Generated review bundles must be versioned by commit or date.
- Generated artifacts from old versions must move to archive or versioned review paths.

---

## Diagrams and Visual Documentation

### Diagram Source Rules

- Every diagram must have an editable source file.
- Screenshots of diagrams are not sufficient as source.
- Mermaid diagrams should live near the page that uses them or under `architecture/diagrams`.
- Rendered SVG/PNG may be stored in assets only if the source is also present.
- Diagrams must include title, scope, and last verified marker in nearby prose.

### Diagram Types

| Diagram Type | Purpose | Required For |
|---|---|---|
| Context | Users and external systems | Mature architecture docs |
| Container | Major docs or app containers | System overview |
| Component | Major internal components | Detailed architecture |
| Runtime Sequence | Hot paths and workflows | API, operations, architecture |
| Dataflow | Data movement and storage | Privacy, security, operations |
| State / Lifecycle | Status changes and release flows | Complex docs or product lifecycles |
| Decision Map | ADR relationships | Large architecture decision sets |

### Diagram Quality Rules

- Diagrams must be legible at 125 percent zoom.
- Avoid overly dense diagrams. Split rather than compress.
- Use consistent names across diagrams and prose.
- Use a legend when shapes or colors encode meaning.
- Render diagrams in CI if the docs site depends on rendered assets.

---

## Asset Policy

### Asset Budget

Recommended limits:
- Logo source: may be large in `sources/`, but published logo should usually be under 250 KB.
- Hero image: under 500 KB unless waived.
- Inline diagram SVG: under 300 KB where practical.
- Screenshot: under 800 KB unless detail requires more.
- Total page payload target: under 2 MB for normal docs pages.

Rules:
- Store original large assets under `docs/sources/assets` if needed.
- Store optimized published assets under `docs/pages/assets`.
- Every image needs meaningful alt text unless decorative.
- Do not commit large binary artifacts without a reason.
- Prefer SVG for diagrams and PNG/WebP for screenshots depending on tooling.
- Avoid base64-embedded images in Markdown.

---

## Release Notes, Changelog, and Roadmap

### Changelog Rules

- Changelog entries must describe shipped changes.
- Changelog must include version, date, and category.
- Breaking changes must include migration notes.
- Security fixes must avoid exploit details until appropriate.
- Documentation-only changes should be marked as docs changes.

### Roadmap Rules

- Roadmap describes intent, not current behavior.
- Roadmap items must not be linked as current implementation evidence.
- Roadmap completion must be tied to version or release evidence.
- Planned APIs must not appear in current API reference unless clearly labeled planned.

### Release Status Rules

Release status claims must be consistent across:
- Home page.
- Changelog.
- Roadmap.
- API reference.
- Installation docs.
- Compatibility docs.
- Package metadata.
- OpenAPI or schema version.
- Deployment docs.

Forbidden:
- Claiming 1.0 GA while contracts identify pre-release versions without explanation.
- Marking a roadmap complete while installation docs still warn alpha behavior.
- Calling a feature production-ready in marketing prose but experimental in reference docs.

---

## Versioning and Compatibility

### Required Compatibility Table

```markdown
| Project Version | Docs Version | API Version | CLI Version | Supported Python/Node/etc. | Supported Storage | Status |
|---|---|---|---|---|---|---|
| 1.0.x | latest | v1 | v1 | Python 3.11-3.12 | Postgres 15+ | current |
```

Rules:
- Docs version must be visible on versioned sites.
- Version-sensitive pages must identify the version they describe.
- Older versions should be accessible under versioned docs or archive.
- Compatibility claims require verification or owner signoff.
- If docs track `main`, the site must clearly say so.

---

## Documentation Naming and Placement

### File Naming

Rules:
- Use lowercase kebab-case for Markdown files: `getting-started.md`, not `GettingStarted.md`.
- Use `index.md` only for section landing pages.
- Use `ADR-0001-short-title.md` for ADRs.
- Use descriptive names for runbooks: `database-restore.md`, not `runbook-1.md`.
- Avoid overloaded filenames like `overview.md` in the same nav level unless context is clear.
- Use stable names. Changing filenames breaks external links.

### Directory Hygiene

Rules:
- Prefer no more than 12 Markdown files per directory before introducing subdirectories.
- Do not mix published docs, generated docs, drafts, and archives in one directory.
- Keep assets under `assets/`, not scattered beside prose, unless local colocation is the declared convention.
- Keep diagrams near architecture docs or in a diagrams subdirectory.
- Keep raw research/source material outside the published tree.

### Page Size

Guidelines:
- Under 300 lines: normal page.
- 300 to 600 lines: acceptable for reference docs.
- Over 600 lines: split unless strong reason exists.
- Over 1,000 lines: usually a generated reference, not hand-written prose.

Refactor procedure for oversized docs:
1. Identify sections that serve different reader tasks.
2. Extract reference material into reference pages.
3. Extract workflow material into guides.
4. Extract troubleshooting into troubleshooting pages.
5. Replace original page with a section landing page.

---

## Writing Standards

### Required Page Shape

Most pages should follow this shape:

```markdown
# Page Title

Brief purpose statement.

## Who this is for

## Prerequisites

## What this page covers

## Procedure / Reference / Explanation

## Validation

## Common failures

## Related pages
```

Reference pages may use:

```markdown
# Reference Title

Brief authority statement.

## Status

## Contract source

## Reference table

## Examples

## Errors or edge cases

## Version notes
```

Runbooks may use:

```markdown
# Runbook Title

## Trigger

## Impact

## Preconditions

## Diagnosis

## Mitigation

## Rollback

## Verification

## Escalation

## Related incidents
```

### Language Rules

- Prefer precise, direct language.
- Define specialized terms the first time they appear.
- Do not use marketing claims as technical claims.
- Avoid vague words like “easy,” “robust,” “production-grade,” and “secure” unless backed by specifics.
- Use “current,” “planned,” “experimental,” and “deprecated” according to the status taxonomy.
- Do not bury warnings in paragraphs. Use callouts.
- Do not repeat the same canonical fact in many places. Link to the owner.

### Examples

Rules:
- Examples must state whether they are minimal, realistic, conceptual, or production.
- Examples must avoid real secrets, tokens, private URLs, or personal data.
- Examples must show expected output when practical.
- Examples must be versioned if the API or CLI is versioned.
- Examples that are not tested must be labeled unverified.

---

## Documentation Security and Privacy

Rules:
- Never publish real secrets, tokens, keys, credentials, private URLs, personal data, customer data, or internal-only incident details.
- Redact logs before adding them to docs.
- Mark internal-only docs clearly and keep them out of public builds.
- Document data egress behavior for APIs, integrations, telemetry, analytics, and model providers.
- State whether examples send data to external services.
- Use placeholder values that cannot be confused with live credentials.
- Check docs with secret scanners.
- Treat screenshots as data-bearing artifacts.

Security checklist:
- [ ] No secrets or credentials.
- [ ] No real user/customer data.
- [ ] No private infrastructure names unless intended.
- [ ] No accidental screenshots of dashboards, tokens, email addresses, or file paths.
- [ ] External analytics or scripts documented.
- [ ] Security-sensitive procedures reviewed by owner.
- [ ] Public docs do not reveal exploit details prematurely.

---

## Observability and Operability Documentation

Documentation should make runtime behavior observable to readers.

Required for operational features:
- Logs emitted.
- Metrics emitted.
- Trace or correlation IDs.
- Health checks.
- Dashboards.
- Alerts.
- Common failure modes.
- Recovery procedures.
- Verification commands.

Rules:
- Do not say “check the logs” without naming the log source or command.
- Do not say “monitor the service” without naming metrics or signals.
- Every runbook must end with verification.
- Every deployment guide must include rollback or recovery path.
- Every backup guide must include restore testing.

---

## AI Agent Documentation Rules

AI agents editing docs must obey these rules.

1. Determine the canonical published tree before editing.
2. Never create a second source of truth for the same claim.
3. Do not edit generated files by hand.
4. Do not add a page without deciding its authority class.
5. Do not add a page to the published tree without updating nav or intentionally marking it orphan-exempt.
6. Do not add API, CLI, config, or error claims without checking the canonical contract or marking them unverified.
7. Do not promote draft or roadmap behavior into current docs.
8. Do not leave broken links to local source paths in published docs.
9. Do not duplicate status claims across many pages. Link to the canonical status page.
10. Do not use screenshots or diagrams without source, alt text, and version context.
11. Do not add large image assets without optimization.
12. Do not rewrite ADR history. Supersede ADRs instead.
13. Do not remove historical context silently. Archive it or record the decision.
14. Do not infer production readiness from aspirational prose.
15. Before finishing, run or describe the docs checks that should be run.

Required pre-edit questions for an AI agent:
- Which tree is published?
- Which page owns this claim?
- Is this page canonical, generated, draft, source, or archive?
- Does this change affect nav?
- Does this change affect API, CLI, config, status, or release truth?
- Are there duplicates that must be updated, redirected, or removed?
- Can the claim be validated?

Required post-edit checklist:
- [ ] Published tree confirmed.
- [ ] Authority class clear.
- [ ] Nav updated or orphan intentionally justified.
- [ ] Links and anchors checked.
- [ ] Status terms consistent.
- [ ] API/CLI/config claims checked against contract.
- [ ] Generated files not hand-edited.
- [ ] Assets optimized.
- [ ] Related docs updated or linked.
- [ ] Changelog/release notes updated if needed.

---

## Documentation Review Checklist

### Source Authority

- [ ] Every current claim has one owner.
- [ ] No divergent duplicates exist.
- [ ] Drafts are outside the published tree.
- [ ] Archive pages are clearly marked.
- [ ] Generated files are labeled and reproducible.
- [ ] Mirrors have generation rules.

### Navigation

- [ ] All nav targets resolve.
- [ ] Important published pages are in nav.
- [ ] Orphans are intentional.
- [ ] Navigation follows reader tasks.
- [ ] Section landing pages route readers clearly.
- [ ] Archived docs are not mixed into current nav without labels.

### Links

- [ ] Internal links resolve.
- [ ] Anchors resolve.
- [ ] Asset references resolve.
- [ ] External links checked.
- [ ] Code links use stable URLs or are intentionally internal.
- [ ] No published links point to drafts as authority.

### Contracts

- [ ] API docs match OpenAPI or declared source.
- [ ] CLI docs match command inventory.
- [ ] Configuration docs match settings source.
- [ ] Error docs match error taxonomy.
- [ ] Examples match current versions.
- [ ] Contract version is visible.

### Status and Releases

- [ ] Home, changelog, roadmap, API docs, and install docs agree.
- [ ] Experimental features are labeled.
- [ ] Deprecated features have migration guidance.
- [ ] Planned features are not presented as current.
- [ ] Release notes describe shipped behavior.
- [ ] Compatibility matrix is current.

### Writing Quality

- [ ] Page has a clear audience.
- [ ] Page has a clear task or reference purpose.
- [ ] Terms are defined.
- [ ] Warnings are visible.
- [ ] Examples are safe and verifiable.
- [ ] Related pages are linked.

### Operations

- [ ] Deployment docs name supported targets.
- [ ] Configuration docs include required values and defaults.
- [ ] Runbooks include diagnosis, mitigation, rollback, verification.
- [ ] Observability docs name logs, metrics, traces, alerts.
- [ ] Security docs separate public, internal, and operator responsibilities.

### Assets and Diagrams

- [ ] Images are optimized.
- [ ] Alt text exists.
- [ ] Diagram source exists.
- [ ] Diagrams are legible.
- [ ] Visuals are versioned or verified.
- [ ] No private data appears in screenshots.

---

## Documentation Quality Scorecard

Score each domain from 0 to 5.

| Domain | 0 | 3 | 5 |
|---|---|---|---|
| Source Authority | No clear owner; duplicates conflict | Mostly clear but some forks | One owner per claim, enforced |
| Navigation | Broken or cluttered | Mostly usable | Complete, task-oriented, validated |
| Link Integrity | Many broken links | Some warnings | All critical links pass |
| Contract Accuracy | Prose drifts from API/CLI/config | Manual sync | Generated or validated |
| Status Consistency | Conflicting maturity claims | Mostly consistent | Version-scoped and enforced |
| Reader Usability | Pages are dumps | Mixed guides/reference | Clear paths by audience/task |
| Operations Usefulness | Aspirational | Basic procedures | Actionable runbooks with verification |
| Architecture Clarity | Stale diagrams | Some current maps | Versioned diagrams and ADRs |
| Reproducibility | Build unclear | Build works locally | Strict CI with pinned deps |
| Security and Privacy | Unsafe examples | Basic caution | Scanned, reviewed, threat-aware |
| Asset Hygiene | Heavy assets | Some optimized | Budgets enforced |
| Maintenance Discipline | No ownership | Informal ownership | Owners, policies, reports |

Interpretation:
- 0.0 to 1.9: Documentation is unreliable.
- 2.0 to 2.9: Documentation is useful but not governed.
- 3.0 to 3.9: Documentation is usable with known debt.
- 4.0 to 4.5: Documentation is strong and maintainable.
- 4.6 to 5.0: Documentation is publication-grade and continuously governed.

---

## Refactor Procedure for Existing Docs Packages

Use this process when applying SGDA to an existing documentation directory.

### Phase 1: Inventory

Produce:
- File inventory.
- Published tree detection.
- Nav target list.
- Orphan pages.
- Broken links.
- Duplicate files.
- Divergent duplicates.
- Large assets.
- Generated artifacts.
- Status claims.
- API/CLI/config claim inventory.

### Phase 2: Authority Decision

For each content area:
- Pick canonical owner.
- Mark duplicates as mirror, archive, redirect, or delete.
- Identify generated sources.
- Identify external contracts.
- Identify source-only material.
- Identify drafts.

### Phase 3: Canonicalization

Actions:
- Move current docs into the published tree.
- Move historical docs into archive.
- Move raw notes into sources.
- Move WIP into drafts.
- Move generated outputs into generated or versioned review paths.
- Add banners to archive and generated pages.
- Update nav.
- Update links.

### Phase 4: Contract Alignment

Actions:
- Align API docs to OpenAPI.
- Align CLI docs to command help.
- Align config docs to settings schema.
- Align status docs to release metadata.
- Align examples to current behavior.
- Align architecture docs to current implementation or label planned.

### Phase 5: Governance

Actions:
- Add local docs checks.
- Add CI docs checks.
- Add status/front matter schema.
- Add duplicate authority checker.
- Add generated freshness checker.
- Add asset budget checker.
- Add docs ownership.

### Phase 6: Publication

Actions:
- Build docs strictly.
- Publish preview.
- Review by reader type.
- Fix navigation and search.
- Merge.
- Tag docs version if applicable.

---

## Example Implementation for MkDocs Material

Recommended layout:

```text
repo/
├─ mkdocs.yml
└─ docs/
   ├─ pages/
   │  ├─ index.md
   │  ├─ getting-started/
   │  ├─ user/
   │  ├─ api/
   │  ├─ architecture/
   │  ├─ operations/
   │  ├─ development/
   │  ├─ reference/
   │  └─ assets/
   ├─ contracts/
   ├─ generated/
   ├─ drafts/
   ├─ archive/
   ├─ governance/
   └─ reports/
```

Required `mkdocs.yml` properties:

```yaml
site_name: Project Docs
docs_dir: docs/pages
nav:
  - Home: index.md
  - Getting Started:
      - Installation: getting-started/installation.md
      - Quickstart: getting-started/quickstart.md
  - API:
      - Overview: api/overview.md
      - Authentication: api/authentication.md
      - Endpoints: api/endpoints.md
      - Schemas: api/schemas.md
  - Operations:
      - Deployment: operations/deployment.md
      - Runbooks: operations/runbooks/incident-response.md
```

Minimum CI command set:

```bash
python docs/governance/tools/check_front_matter.py
python docs/governance/tools/check_nav.py
python docs/governance/tools/check_duplicate_authority.py
python docs/governance/tools/check_status_claims.py
python docs/governance/tools/check_contract_drift.py
python docs/governance/tools/check_asset_budget.py
mkdocs build --strict
```

Optional link checker:

```bash
lychee --no-progress --accept 200,204,206,429 docs/pages/**/*.md
```

---

## Documentation Procedures

### Procedure: Add a New Page

1. Identify audience and task.
2. Identify authority class.
3. Choose location according to layer.
4. Add required front matter.
5. Write page using required page shape.
6. Link to canonical reference pages instead of copying facts.
7. Add nav entry if published.
8. Add related pages.
9. Run link and nav checks.
10. Add tests or validation if page includes commands, API paths, config keys, or examples.

### Procedure: Update an API Claim

1. Check canonical OpenAPI or schema source.
2. Update contract first if behavior changed.
3. Regenerate API docs if generated.
4. Update prose only where necessary.
5. Update examples.
6. Update changelog if user-visible.
7. Run contract drift check.
8. Run link check.

### Procedure: Update Project Status

1. Identify status owner page.
2. Update status owner.
3. Update home page summary if needed.
4. Update roadmap and changelog if needed.
5. Update compatibility table.
6. Search for old maturity terms.
7. Run status consistency check.

### Procedure: Add a Diagram

1. Add editable source file.
2. Add rendered asset only if required.
3. Reference diagram from a canonical page.
4. Add title, scope, and last verified date.
5. Check rendering.
6. Check image size.
7. Add alt text or textual equivalent.

### Procedure: Archive a Page

1. Confirm replacement or reason for archive.
2. Move page to `docs/archive`.
3. Add archive banner.
4. Add `replaced_by` front matter if applicable.
5. Update links to point to replacement.
6. Add redirect if external links are likely.
7. Remove from current nav unless archive nav is intentional.

### Procedure: Resolve a Divergent Duplicate

1. Compare both versions.
2. Determine published version.
3. Determine fresher/correcter version from content evidence.
4. Create canonical merged page.
5. Preserve useful history in archive if needed.
6. Delete, redirect, or mirror the losing copy.
7. Add duplicate regression check.

---

## Documentation Anti-Patterns

Avoid these patterns.

- Split Reality: Root docs and published docs both look canonical but disagree.
- Roadmap as Reference: Planned behavior is documented as if available.
- Tutorial as Contract: API behavior is defined by examples instead of schemas.
- Generated But Edited: Generated files silently hand-edited.
- Broken Code Links: Published docs link to local source paths that do not exist in the docs site.
- Status Fog: Alpha, beta, GA, experimental, stable, and production-ready mixed without version scope.
- Diagram Fossils: Beautiful diagrams with no source, date, or verification.
- Screenshot Truth: Screenshots used as the only source for operational procedures.
- Archive Leakage: Old docs remain linked as current guidance.
- Asset Bloat: Huge images slow docs pages.
- Hidden Private Data: Screenshots or logs expose credentials, emails, hostnames, or customer details.
- Overstuffed Pages: One giant page mixes tutorial, reference, architecture, and troubleshooting.
- Placeholder Drift: `your-org`, `example.com`, and old repo names survive into published docs.
- Nav Graveyard: Navigation mirrors folder structure instead of reader tasks.
- Orphan Authority: A current page exists but is unreachable from nav.

---

## Validation Domains and Best Combination

| Domain | Strategy | Practice |
|---|---|---|
| Source Authority | Duplicate and authority checks | Fail on divergent duplicates in current docs |
| Navigation | Strict nav validation | Fail on missing nav targets; warn/fail on current orphans |
| Link Integrity | Internal and external link checking | Fail on internal breaks; manage external flake policy |
| Contract Accuracy | Schema and generated doc checks | Fail on API/CLI/config drift |
| Status Consistency | Status taxonomy and claim scanner | Fail on contradictory maturity claims |
| Generated Freshness | Input hash manifests | Fail when generated docs are stale |
| Asset Hygiene | Size and dimension budgets | Fail on over-budget published assets |
| Security and Privacy | Secret scanning and screenshot review | Fail on credentials or private data |
| Accessibility | Heading order, alt text, readable diagrams | Warn or fail depending on maturity |
| Reproducibility | Pinned docs build | Build in CI with strict mode |
| Maintainability | Ownership and page size rules | Warn on oversized pages and unowned pages |

---

## Adoption Checklist

Use this checklist to install SGDA into an existing repo.

- [ ] Declare the canonical published tree.
- [ ] Create `docs/DOCS_ARCHITECTURE.md`.
- [ ] Create `docs/DOCS_CONVENTIONS.md`.
- [ ] Create `docs/DOCS_QUALITY_GATES.md`.
- [ ] Add page authority front matter to current pages.
- [ ] Add archive banners to historical pages.
- [ ] Separate drafts, source material, generated artifacts, and published pages.
- [ ] Resolve divergent duplicates.
- [ ] Add nav validation.
- [ ] Add link validation.
- [ ] Add contract drift validation.
- [ ] Add status consistency validation.
- [ ] Add generated freshness validation.
- [ ] Add asset budget validation.
- [ ] Add strict docs build in CI.
- [ ] Add docs owner review to PRs that alter canonical docs.
- [ ] Publish a preview build for documentation PRs.
- [ ] Review the docs through user, developer, operator, and architect paths.

---

## Minimum Viable SGDA

For a small project, the minimum useful version is:

```text
docs/
├─ pages/
│  ├─ index.md
│  ├─ getting-started.md
│  ├─ usage.md
│  ├─ api.md
│  ├─ configuration.md
│  └─ troubleshooting.md
├─ archive/
├─ drafts/
├─ DOCS_ARCHITECTURE.md
├─ DOCS_CONVENTIONS.md
└─ DOCS_QUALITY_GATES.md
```

Minimum rules:
1. `pages/` is the only published source.
2. No divergent duplicates.
3. Every page has status and authority.
4. Nav and links must pass.
5. API/config/CLI claims must have one owner.
6. Drafts and archives are not current truth.
7. The docs build is reproducible.

---

## Full SGDA Target State

A mature SGDA implementation has:

- One canonical published tree.
- Version-aware docs.
- Generated API/CLI/config reference.
- Architecture diagrams with sources.
- ADRs with supersession tracking.
- Operations runbooks with verification.
- Docs CI quality gates.
- Link, anchor, nav, duplicate, status, contract, generated freshness, asset, and security checks.
- Documentation ownership.
- Published previews for docs PRs.
- Machine-readable docs architecture report.
- Clear archive and draft boundaries.

---

## Closing Principle

Documentation is not a folder of explanations. It is the operating interface between the project and every person trying to use, trust, repair, extend, deploy, or evaluate it.

SGDA exists to keep that interface coherent. It makes documentation navigable, testable, versioned, and honest. A reader should never have to guess which page is true, which version is current, which API exists, which guide applies, or whether a diagram is still alive.
