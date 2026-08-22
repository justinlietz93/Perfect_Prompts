#!/usr/bin/env python3
"""
Scaffold a Standards-Governed Documentation Architecture (SGDA) docs tree.

Default behavior creates a docs/ directory that follows the SGDA example layout:
- canonical published docs under docs/pages/
- machine-readable contracts under docs/contracts/
- generated outputs under docs/generated/
- source material, drafts, archive, governance, and reports areas
- starter Markdown, JSON, Mermaid, DOT, CSV, and policy/tool templates

The script is intentionally dependency-free and safe by default:
- existing files are not overwritten unless --force is passed
- --dry-run previews planned writes
- --site-config controls where mkdocs.yml is written
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
from pathlib import Path
from textwrap import dedent
from typing import Dict, Iterable, List, Tuple


DIRECTORIES: Tuple[str, ...] = (
    "pages/about",
    "pages/getting-started",
    "pages/user",
    "pages/api",
    "pages/cli",
    "pages/architecture/decisions",
    "pages/architecture/diagrams",
    "pages/architecture/reviews/{review_date}",
    "pages/operations/runbooks",
    "pages/development",
    "pages/reference",
    "pages/assets/images",
    "pages/assets/diagrams",
    "pages/assets/stylesheets",
    "pages/assets/javascripts",
    "contracts",
    "generated/api",
    "generated/cli",
    "generated/architecture",
    "generated/reports",
    "sources/transcripts",
    "sources/research",
    "sources/design-notes",
    "sources/imported",
    "drafts/{year_month}",
    "archive/2025",
    "governance/policies",
    "governance/tools",
    "governance/ci",
    "reports",
)


PAGE_SPECS: Dict[str, Tuple[str, str, List[str]]] = {
    "pages/index.md": (
        "Home",
        "Published landing page, project status summary, and reader routing hub.",
        ["Project Status", "Reader Paths", "Supported Versions", "Next Steps"],
    ),
    "pages/about/overview.md": (
        "Overview",
        "High-level description of the project, audience, scope, and non-goals.",
        ["What This Is", "Who It Is For", "What It Does Not Claim", "Where To Go Next"],
    ),
    "pages/about/changelog.md": (
        "Changelog",
        "Chronological record of shipped documentation and product changes.",
        ["Unreleased", "Released Versions", "Migration Notes"],
    ),
    "pages/about/roadmap.md": (
        "Roadmap",
        "Planned, accepted, experimental, deprecated, and removed work.",
        ["Current", "Experimental", "Planned", "Deprecated", "Removed"],
    ),
    "pages/getting-started/installation.md": (
        "Installation",
        "Prerequisites, installation commands, supported targets, and verification steps.",
        ["Prerequisites", "Install", "Verify", "Common Failures", "Next Step"],
    ),
    "pages/getting-started/quickstart.md": (
        "Quickstart",
        "Smallest successful path from install to working output.",
        ["Goal", "Before You Start", "Run", "Expected Output", "Troubleshooting", "Next Step"],
    ),
    "pages/getting-started/first-run.md": (
        "First Run",
        "First meaningful run with expected output and failure modes.",
        ["Goal", "Inputs", "Command", "Expected Output", "Failure Modes", "Next Step"],
    ),
    "pages/user/concepts.md": (
        "Concepts",
        "User-facing concepts required to understand the system without implementation details.",
        ["Core Terms", "Mental Model", "Common Misunderstandings", "Related Reference"],
    ),
    "pages/user/workflows.md": (
        "Workflows",
        "Task-oriented user workflows with prerequisites, steps, outputs, and recovery paths.",
        ["Workflow Index", "Workflow Template", "Expected Outputs", "Recovery"],
    ),
    "pages/user/troubleshooting.md": (
        "Troubleshooting",
        "Symptom-driven problem diagnosis and fixes.",
        ["Symptoms", "Checks", "Fixes", "Escalation"],
    ),
    "pages/api/overview.md": (
        "API Overview",
        "API scope, base URLs, authentication model, versioning, and contract source.",
        ["Contract Source", "Base URLs", "Versioning", "Authentication", "Errors", "Examples"],
    ),
    "pages/api/authentication.md": (
        "Authentication",
        "Authentication mechanisms, token handling, scopes, and security notes.",
        ["Mechanisms", "Tokens", "Scopes", "Security Notes", "Failure Modes"],
    ),
    "pages/api/endpoints.md": (
        "Endpoints",
        "Canonical API endpoint reference or generated projection from OpenAPI.",
        ["Contract Source", "Endpoint Index", "Requests", "Responses", "Examples"],
    ),
    "pages/api/schemas.md": (
        "Schemas",
        "Canonical request, response, and shared object schemas.",
        ["Schema Source", "Objects", "Validation", "Compatibility"],
    ),
    "pages/api/errors.md": (
        "Errors",
        "Stable API error codes, retryability, causes, and remediations.",
        ["Error Envelope", "Error Codes", "Retryability", "Remediation"],
    ),
    "pages/api/examples.md": (
        "API Examples",
        "Runnable API examples tied to the canonical API contract.",
        ["Before You Start", "Examples", "Expected Responses", "Common Failures"],
    ),
    "pages/cli/commands.md": (
        "CLI Commands",
        "Canonical CLI command, argument, flag, output, and exit-code reference.",
        ["Contract Source", "Command Index", "Flags", "Output Formats", "Exit Codes"],
    ),
    "pages/cli/configuration.md": (
        "CLI Configuration",
        "CLI configuration files, environment variables, and precedence rules.",
        ["Config Sources", "Precedence", "Environment Variables", "Examples"],
    ),
    "pages/cli/examples.md": (
        "CLI Examples",
        "Runnable CLI examples with expected outputs and failure modes.",
        ["Before You Start", "Examples", "Expected Output", "Troubleshooting"],
    ),
    "pages/architecture/overview.md": (
        "Architecture Overview",
        "Current architecture, accepted design, planned work, and known constraints.",
        ["Status", "Context", "Containers", "Components", "Runtime Flows", "Known Gaps"],
    ),
    "pages/operations/deployment.md": (
        "Deployment",
        "Supported deployment targets, steps, verification, rollback, and ownership.",
        ["Supported Targets", "Deploy", "Verify", "Rollback", "Owners"],
    ),
    "pages/operations/configuration.md": (
        "Operations Configuration",
        "Runtime configuration required to operate the system safely.",
        ["Sources", "Required Values", "Optional Values", "Validation", "Rotation"],
    ),
    "pages/operations/observability.md": (
        "Observability",
        "Logs, metrics, traces, dashboards, alerts, and correlation identifiers.",
        ["Logs", "Metrics", "Traces", "Dashboards", "Alerts", "Correlation"],
    ),
    "pages/operations/backup-restore.md": (
        "Backup and Restore",
        "Backup strategy, restore procedure, test cadence, and data loss expectations.",
        ["Backup Scope", "Restore Procedure", "Verification", "RPO/RTO", "Test Cadence"],
    ),
    "pages/operations/runbooks/incident-response.md": (
        "Incident Response Runbook",
        "Trigger, impact, diagnosis, mitigation, rollback, verification, and owner.",
        ["Trigger", "Impact", "Diagnosis", "Mitigation", "Rollback", "Verification", "Owner"],
    ),
    "pages/operations/runbooks/degraded-service.md": (
        "Degraded Service Runbook",
        "Procedure for diagnosing and mitigating degraded service conditions.",
        ["Trigger", "Impact", "Checks", "Mitigation", "Verification", "Escalation"],
    ),
    "pages/development/contributing.md": (
        "Contributing",
        "Contributor workflow, branch policy, review expectations, and docs standards.",
        ["Setup", "Branching", "Review", "Documentation Expectations", "Submitting Changes"],
    ),
    "pages/development/testing.md": (
        "Testing",
        "Test strategy, commands, expected reports, and acceptance gates.",
        ["Test Types", "Commands", "Reports", "Acceptance Gates", "Troubleshooting"],
    ),
    "pages/development/release-process.md": (
        "Release Process",
        "Release preparation, versioning, changelog, docs verification, and publication.",
        ["Versioning", "Pre-release Checks", "Changelog", "Docs Verification", "Publish"],
    ),
    "pages/development/docs-maintenance.md": (
        "Documentation Maintenance",
        "How to maintain, validate, archive, and refactor documentation safely.",
        ["Ownership", "Routine Checks", "Refactor Procedure", "Archive Procedure", "Quality Gates"],
    ),
    "pages/reference/glossary.md": (
        "Glossary",
        "Canonical definitions for user, developer, operator, and architecture terms.",
        ["Terms", "Deprecated Terms", "Naming Notes"],
    ),
    "pages/reference/configuration-reference.md": (
        "Configuration Reference",
        "Canonical configuration key reference checked against config schema.",
        ["Contract Source", "Configuration Keys", "Defaults", "Validation", "Examples"],
    ),
    "pages/reference/environment-variables.md": (
        "Environment Variables",
        "Canonical environment variable reference and precedence behavior.",
        ["Required", "Optional", "Deprecated", "Security Notes"],
    ),
    "pages/reference/compatibility.md": (
        "Compatibility",
        "Supported versions, platforms, dependency ranges, and deprecation policy.",
        ["Supported Versions", "Supported Platforms", "Dependency Ranges", "Deprecations"],
    ),
}


POLICY_SPECS: Dict[str, Tuple[str, str]] = {
    "governance/policies/source_authority_policy.md": (
        "Source Authority Policy",
        "Rules for canonical, generated, mirror, draft, source, archive, redirect, and external authority classes.",
    ),
    "governance/policies/nav_policy.md": (
        "Navigation Policy",
        "Rules for site navigation completeness, reader-path order, orphans, and missing targets.",
    ),
    "governance/policies/link_policy.md": (
        "Link Policy",
        "Rules for relative links, anchors, external links, source links, images, and archive references.",
    ),
    "governance/policies/status_policy.md": (
        "Status Policy",
        "Rules for current, experimental, planned, draft, deprecated, archived, removed, and unknown statuses.",
    ),
    "governance/policies/api_contract_policy.md": (
        "API Contract Policy",
        "Rules for aligning API prose, examples, schemas, error docs, and OpenAPI contracts.",
    ),
    "governance/policies/release_notes_policy.md": (
        "Release Notes Policy",
        "Rules for changelog entries, version notes, migration guidance, and shipped-vs-planned claims.",
    ),
    "governance/policies/diagrams_policy.md": (
        "Diagrams Policy",
        "Rules for Mermaid, Graphviz, exported assets, legends, scope, and verification metadata.",
    ),
    "governance/policies/asset_policy.md": (
        "Asset Policy",
        "Rules for image size, file naming, alt text, provenance, and performance budgets.",
    ),
    "governance/policies/archive_policy.md": (
        "Archive Policy",
        "Rules for preserving historical docs without allowing them to compete with current truth.",
    ),
}


def slug_title(path: str) -> str:
    stem = Path(path).stem
    return stem.replace("_", " ").replace("-", " ").title()


def yaml_front_matter(
    title: str,
    status: str,
    authority: str,
    owner: str,
    today: str,
    project_name: str,
    audience: Iterable[str] = ("user", "developer"),
    extra: Dict[str, str] | None = None,
) -> str:
    data = {
        "title": title,
        "status": status,
        "authority": authority,
        "owner": owner,
        "last_verified": today,
        "verified_against": "scaffold",
        "audience": list(audience),
        "project": project_name,
    }
    if extra:
        data.update(extra)
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            items = ", ".join(f'"{item}"' for item in value)
            lines.append(f"{key}: [{items}]")
        else:
            lines.append(f'{key}: "{value}"')
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def markdown_page(
    title: str,
    purpose: str,
    sections: List[str],
    *,
    status: str,
    authority: str,
    owner: str,
    today: str,
    project_name: str,
    audience: Iterable[str] = ("user", "developer"),
) -> str:
    body = [
        yaml_front_matter(title, status, authority, owner, today, project_name, audience),
        f"# {title}\n",
        f"> Purpose: {purpose}\n",
        "> Status: scaffolded template. Replace placeholders with verified project-specific content.\n",
    ]
    for section in sections:
        body.append(f"\n## {section}\n\nTODO: Fill in verified content.\n")
    return "".join(body).rstrip() + "\n"


def policy_page(title: str, purpose: str, *, today: str, project_name: str) -> str:
    return dedent(
        f"""
        ---
        title: "{title}"
        status: "current"
        authority: "canonical"
        owner: "docs"
        last_verified: "{today}"
        verified_against: "SGDA scaffold"
        audience: ["maintainer", "developer", "operator"]
        project: "{project_name}"
        ---

        # {title}

        > Purpose: {purpose}

        ## Rule

        TODO: State the enforceable rule.

        ## Rationale

        TODO: Explain why this policy exists.

        ## Required Practice

        - TODO: Add required practice.
        - TODO: Add required practice.

        ## Violations

        - TODO: Describe violation.

        ## Enforcement

        - Local check: TODO
        - CI check: TODO
        - Report output: TODO

        ## Exceptions

        Exceptions require an owner, reason, and expiration date.
        """
    ).strip() + "\n"


def mkdocs_config(project_name: str, docs_dir: str, nav_file_note: str) -> str:
    return dedent(
        f"""
        site_name: {project_name} Documentation
        site_description: Standards-governed documentation site for {project_name}.
        docs_dir: {docs_dir}
        theme:
          name: material
          features:
            - navigation.sections
            - navigation.expand
            - navigation.top
            - search.suggest
            - search.highlight
            - content.code.copy
        markdown_extensions:
          - admonition
          - attr_list
          - md_in_html
          - pymdownx.details
          - pymdownx.superfences
          - toc:
              permalink: true
        plugins:
          - search
        nav:
          - Home: index.md
          - About:
              - Overview: about/overview.md
              - Changelog: about/changelog.md
              - Roadmap: about/roadmap.md
          - Getting Started:
              - Installation: getting-started/installation.md
              - Quickstart: getting-started/quickstart.md
              - First Run: getting-started/first-run.md
          - User Guide:
              - Concepts: user/concepts.md
              - Workflows: user/workflows.md
              - Troubleshooting: user/troubleshooting.md
          - API:
              - Overview: api/overview.md
              - Authentication: api/authentication.md
              - Endpoints: api/endpoints.md
              - Schemas: api/schemas.md
              - Errors: api/errors.md
              - Examples: api/examples.md
          - CLI:
              - Commands: cli/commands.md
              - Configuration: cli/configuration.md
              - Examples: cli/examples.md
          - Architecture:
              - Overview: architecture/overview.md
              - Decisions:
                  - Architecture Principles: architecture/decisions/ADR-0001-record-architecture-principles.md
                  - API Contract Source: architecture/decisions/ADR-0002-document-api-contract-source.md
          - Operations:
              - Deployment: operations/deployment.md
              - Configuration: operations/configuration.md
              - Observability: operations/observability.md
              - Backup and Restore: operations/backup-restore.md
              - Runbooks:
                  - Incident Response: operations/runbooks/incident-response.md
                  - Degraded Service: operations/runbooks/degraded-service.md
          - Development:
              - Contributing: development/contributing.md
              - Testing: development/testing.md
              - Release Process: development/release-process.md
              - Docs Maintenance: development/docs-maintenance.md
          - Reference:
              - Glossary: reference/glossary.md
              - Configuration Reference: reference/configuration-reference.md
              - Environment Variables: reference/environment-variables.md
              - Compatibility: reference/compatibility.md

        # {nav_file_note}
        """
    ).lstrip()


def nav_yml() -> str:
    return dedent(
        """
        # Optional separated navigation source.
        # MkDocs does not consume this file by default unless your build tooling merges it
        # into mkdocs.yml. Keep it here when you want navigation review separate from theme config.

        - Home: index.md
        - About:
            - Overview: about/overview.md
            - Changelog: about/changelog.md
            - Roadmap: about/roadmap.md
        - Getting Started:
            - Installation: getting-started/installation.md
            - Quickstart: getting-started/quickstart.md
            - First Run: getting-started/first-run.md
        - User Guide:
            - Concepts: user/concepts.md
            - Workflows: user/workflows.md
            - Troubleshooting: user/troubleshooting.md
        - API:
            - Overview: api/overview.md
            - Authentication: api/authentication.md
            - Endpoints: api/endpoints.md
            - Schemas: api/schemas.md
            - Errors: api/errors.md
            - Examples: api/examples.md
        - CLI:
            - Commands: cli/commands.md
            - Configuration: cli/configuration.md
            - Examples: cli/examples.md
        - Architecture:
            - Overview: architecture/overview.md
            - Decisions:
                - Architecture Principles: architecture/decisions/ADR-0001-record-architecture-principles.md
                - API Contract Source: architecture/decisions/ADR-0002-document-api-contract-source.md
        - Operations:
            - Deployment: operations/deployment.md
            - Configuration: operations/configuration.md
            - Observability: operations/observability.md
            - Backup and Restore: operations/backup-restore.md
            - Runbooks:
                - Incident Response: operations/runbooks/incident-response.md
                - Degraded Service: operations/runbooks/degraded-service.md
        - Development:
            - Contributing: development/contributing.md
            - Testing: development/testing.md
            - Release Process: development/release-process.md
            - Docs Maintenance: development/docs-maintenance.md
        - Reference:
            - Glossary: reference/glossary.md
            - Configuration Reference: reference/configuration-reference.md
            - Environment Variables: reference/environment-variables.md
            - Compatibility: reference/compatibility.md
        """
    ).lstrip()


def adr(number: int, title: str, today: str, project_name: str) -> str:
    slug = title.lower().replace(" ", "-")
    return dedent(
        f"""
        ---
        title: "ADR-{number:04d}: {title}"
        status: "current"
        authority: "canonical"
        owner: "architecture"
        last_verified: "{today}"
        verified_against: "scaffold"
        audience: ["architect", "developer", "maintainer"]
        project: "{project_name}"
        ---

        # ADR-{number:04d}: {title}

        ## Status

        Accepted.

        ## Context

        TODO: Describe the situation that forced this decision.

        ## Decision

        TODO: State the decision in one or two precise paragraphs.

        ## Consequences

        - Positive: TODO
        - Negative: TODO
        - Follow-up: TODO

        ## Supersession

        This ADR is active until superseded by a later ADR.

        <!-- slug: {slug} -->
        """
    ).strip() + "\n"


def mermaid_context(project_name: str, today: str) -> str:
    return dedent(
        f"""
        %% SGDA diagram
        %% title: Documentation Context
        %% project: {project_name}
        %% last_verified: {today}
        %% authority: canonical template
        flowchart LR
            Reader[Reader] --> Site[{project_name} Docs Site]
            Maintainer[Docs Maintainer] --> Site
            Site --> Published[Canonical Published Pages]
            Site --> Contracts[Machine-Readable Contracts]
            Site --> Governance[Docs Governance Checks]
            Contracts --> Published
            Governance --> Reports[Validation Reports]
        """
    ).lstrip()


def mermaid_containers(project_name: str, today: str) -> str:
    return dedent(
        f"""
        %% SGDA diagram
        %% title: Documentation Containers
        %% project: {project_name}
        %% last_verified: {today}
        flowchart TB
            Pages[pages/\nCanonical published docs]
            Contracts[contracts/\nOpenAPI, CLI, config, errors]
            Generated[generated/\nGenerated docs outputs]
            Sources[sources/\nRaw source material]
            Drafts[drafts/\nUnpublished work]
            Archive[archive/\nHistorical docs]
            Governance[governance/\nPolicies and tools]
            Reports[reports/\nValidation outputs]

            Contracts --> Pages
            Generated --> Pages
            Sources -.promotion only.-> Pages
            Drafts -.review only.-> Pages
            Archive -.historical links.-> Pages
            Governance --> Reports
            Governance --> Pages
            Governance --> Contracts
        """
    ).lstrip()


def mermaid_sequence(project_name: str, today: str) -> str:
    return dedent(
        f"""
        %% SGDA diagram
        %% title: Documentation Change Runtime Sequence
        %% project: {project_name}
        %% last_verified: {today}
        sequenceDiagram
            participant Author
            participant Pages as docs/pages
            participant Contracts as docs/contracts
            participant Governance as docs/governance/tools
            participant Reports as docs/reports
            participant Site as Built docs site

            Author->>Pages: Edit canonical page
            Author->>Contracts: Update machine-readable contract if public interface changed
            Governance->>Pages: Check nav, links, status, duplicate authority
            Governance->>Contracts: Check contract drift
            Governance->>Reports: Write validation outputs
            Governance-->>Author: Pass/fail with actionable report
            Pages->>Site: Publish only after checks pass
        """
    ).lstrip()


def openapi_contract(project_name: str) -> str:
    return json.dumps(
        {
            "openapi": "3.1.0",
            "info": {
                "title": f"{project_name} API",
                "version": "0.1.0",
                "description": "Scaffold placeholder. Replace with generated or canonical OpenAPI.",
            },
            "paths": {},
            "components": {"schemas": {}, "securitySchemes": {}},
        },
        indent=2,
    ) + "\n"


def json_contract(title: str, description: str) -> str:
    return json.dumps(
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": title,
            "description": description,
            "type": "object",
            "additionalProperties": True,
            "properties": {},
        },
        indent=2,
    ) + "\n"


def docs_status_schema() -> str:
    return json.dumps(
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "SGDA Docs Status Front Matter",
            "type": "object",
            "required": ["title", "status", "authority"],
            "properties": {
                "title": {"type": "string"},
                "status": {
                    "type": "string",
                    "enum": [
                        "current",
                        "experimental",
                        "planned",
                        "draft",
                        "deprecated",
                        "archived",
                        "removed",
                        "unknown",
                    ],
                },
                "authority": {
                    "type": "string",
                    "enum": [
                        "canonical",
                        "generated",
                        "mirror",
                        "draft",
                        "source",
                        "archive",
                        "redirect",
                        "external",
                    ],
                },
                "owner": {"type": "string"},
                "last_verified": {"type": "string"},
                "verified_against": {"type": "string"},
                "audience": {"type": "array", "items": {"type": "string"}},
            },
        },
        indent=2,
    ) + "\n"


def checker_script(name: str, purpose: str) -> str:
    return dedent(
        f'''\
        #!/usr/bin/env python3
        """{purpose}

        Scaffold placeholder for SGDA governance tooling.
        Replace TODO logic with project-specific validation. Keep output deterministic.
        """

        from __future__ import annotations

        import argparse
        from pathlib import Path


        def main() -> int:
            parser = argparse.ArgumentParser(description={purpose!r})
            parser.add_argument("docs_root", nargs="?", default="docs", help="Path to docs root")
            parser.add_argument("--report", default=None, help="Optional report output path")
            args = parser.parse_args()

            docs_root = Path(args.docs_root)
            if not docs_root.exists():
                print(f"FAIL: docs root not found: {{docs_root}}")
                return 2

            # TODO: implement {name} validation.
            print(f"PASS: {name} scaffold check found docs root: {{docs_root}}")
            if args.report:
                Path(args.report).parent.mkdir(parents=True, exist_ok=True)
                Path(args.report).write_text("status,result\\nPASS,scaffold check only\\n", encoding="utf-8")
            return 0


        if __name__ == "__main__":
            raise SystemExit(main())
        '''
    )


def docs_quality_ci() -> str:
    return dedent(
        """
        # Reference CI workflow fragment for documentation quality gates.
        # Adapt this to GitHub Actions, GitLab CI, Buildkite, or local Makefile targets.

        name: docs-quality-gates

        on:
          pull_request:
            paths:
              - "docs/**"
              - "mkdocs.yml"
          push:
            branches: [main]
            paths:
              - "docs/**"
              - "mkdocs.yml"

        jobs:
          docs:
            runs-on: ubuntu-latest
            steps:
              - uses: actions/checkout@v4
              - uses: actions/setup-python@v5
                with:
                  python-version: "3.12"
              - name: Install docs dependencies
                run: |
                  python -m pip install --upgrade pip
                  pip install mkdocs mkdocs-material
              - name: Governance checks
                run: |
                  python docs/governance/tools/check_nav.py docs --report docs/reports/nav-orphans.csv
                  python docs/governance/tools/check_links.py docs --report docs/reports/link-check.csv
                  python docs/governance/tools/check_duplicate_authority.py docs --report docs/reports/duplicate-authority.csv
                  python docs/governance/tools/check_status_claims.py docs
                  python docs/governance/tools/check_contract_drift.py docs
                  python docs/governance/tools/check_asset_budget.py docs --report docs/reports/asset-budget.csv
                  python docs/governance/tools/check_generated_freshness.py docs
              - name: Build docs strictly
                run: mkdocs build --strict
        """
    ).lstrip()


def build_templates(project_name: str, today: str, review_date: str, year_month: str) -> Dict[str, str]:
    templates: Dict[str, str] = {}

    templates["README.md"] = dedent(
        f"""
        # {project_name} Documentation Maintainer Guide

        This directory follows Standards-Governed Documentation Architecture.

        ## Canonical Published Tree

        `pages/` is the canonical published source tree unless your repository-level
        `mkdocs.yml` points somewhere else.

        ## Authority Rule

        Every public claim must have one owner. Do not duplicate current truth across
        `pages/`, `generated/`, `sources/`, `drafts/`, and `archive/`.

        ## Common Commands

        ```bash
        mkdocs serve
        mkdocs build --strict
        python governance/tools/check_nav.py . --report reports/nav-orphans.csv
        python governance/tools/check_links.py . --report reports/link-check.csv
        ```

        ## Maintenance Loop

        1. Edit canonical pages under `pages/`.
        2. Update contracts under `contracts/` when public interfaces change.
        3. Regenerate generated docs under `generated/` when applicable.
        4. Run governance checks.
        5. Publish only after nav, links, status, contract, and asset checks pass.
        """
    ).strip() + "\n"

    templates["DOCS_ARCHITECTURE.md"] = markdown_page(
        "Documentation Architecture",
        "Explains the documentation system, authority boundaries, reader paths, and governance plane.",
        ["Canonical Tree", "Authority Classes", "Reader Paths", "Contracts", "Generated Artifacts", "Governance Checks", "Refactor Procedure"],
        status="current",
        authority="canonical",
        owner="docs",
        today=today,
        project_name=project_name,
        audience=("maintainer", "developer", "architect"),
    )

    templates["DOCS_CONVENTIONS.md"] = markdown_page(
        "Documentation Conventions",
        "Writing, naming, linking, diagram, status, and example conventions for this docs directory.",
        ["Voice and Scope", "File Naming", "Front Matter", "Links", "Examples", "Diagrams", "Statuses", "Review Checklist"],
        status="current",
        authority="canonical",
        owner="docs",
        today=today,
        project_name=project_name,
        audience=("maintainer", "developer", "writer"),
    )

    templates["DOCS_QUALITY_GATES.md"] = markdown_page(
        "Documentation Quality Gates",
        "Local and CI validation rules for documentation integrity.",
        ["Required Gates", "Advisory Gates", "Reports", "Failure Handling", "Exceptions", "Strict Mode"],
        status="current",
        authority="canonical",
        owner="docs",
        today=today,
        project_name=project_name,
        audience=("maintainer", "developer", "operator"),
    )

    templates["nav.yml"] = nav_yml()

    for path, (title, purpose, sections) in PAGE_SPECS.items():
        templates[path] = markdown_page(
            title,
            purpose,
            sections,
            status="current",
            authority="canonical",
            owner="docs",
            today=today,
            project_name=project_name,
        )

    templates["pages/architecture/decisions/ADR-0001-record-architecture-principles.md"] = adr(
        1, "Record Architecture Principles", today, project_name
    )
    templates["pages/architecture/decisions/ADR-0002-document-api-contract-source.md"] = adr(
        2, "Document API Contract Source", today, project_name
    )

    templates["pages/architecture/diagrams/context.mmd"] = mermaid_context(project_name, today)
    templates["pages/architecture/diagrams/containers.mmd"] = mermaid_containers(project_name, today)
    templates["pages/architecture/diagrams/runtime-sequence.mmd"] = mermaid_sequence(project_name, today)

    templates[f"pages/architecture/reviews/{review_date}/executive-summary.md"] = markdown_page(
        f"Architecture Review {review_date}",
        "Versioned architecture review summary tied to a commit or release.",
        ["Scope", "Commit", "Findings", "Risks", "Recommendations"],
        status="current",
        authority="generated",
        owner="architecture",
        today=today,
        project_name=project_name,
        audience=("architect", "developer", "maintainer"),
    )
    templates[f"pages/architecture/reviews/{review_date}/architecture-map.json"] = json.dumps(
        {
            "system": project_name,
            "review_date": review_date,
            "commit": "TODO",
            "containers": [],
            "components": [],
            "risks": [],
        },
        indent=2,
    ) + "\n"
    templates[f"pages/architecture/reviews/{review_date}/dependency-graph.dot"] = dedent(
        f"""
        digraph docs_architecture_review_{review_date.replace('-', '_')} {{
          rankdir=LR;
          label="{project_name} architecture review dependency graph";
          pages [label="pages/"];
          contracts [label="contracts/"];
          generated [label="generated/"];
          contracts -> pages;
          generated -> pages;
        }}
        """
    ).lstrip()

    templates["contracts/openapi.json"] = openapi_contract(project_name)
    templates["contracts/cli-schema.json"] = json_contract(
        f"{project_name} CLI Schema",
        "Scaffold placeholder. Replace with generated CLI command schema.",
    )
    templates["contracts/config-schema.json"] = json_contract(
        f"{project_name} Config Schema",
        "Scaffold placeholder. Replace with canonical configuration schema.",
    )
    templates["contracts/error-codes.json"] = json.dumps(
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": f"{project_name} Error Codes",
            "type": "object",
            "properties": {
                "errors": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["code", "meaning", "retryable", "fix"],
                        "properties": {
                            "code": {"type": "string"},
                            "meaning": {"type": "string"},
                            "retryable": {"type": "boolean"},
                            "fix": {"type": "string"},
                        },
                    },
                }
            },
            "errors": [],
        },
        indent=2,
    ) + "\n"
    templates["contracts/docs-status.schema.json"] = docs_status_schema()

    for path, (title, purpose) in POLICY_SPECS.items():
        templates[path] = policy_page(title, purpose, today=today, project_name=project_name)

    tools = {
        "governance/tools/check_nav.py": ("check_nav", "Validate docs navigation targets and orphan policy."),
        "governance/tools/check_links.py": ("check_links", "Validate internal links, anchors, images, and external-link policy."),
        "governance/tools/check_duplicate_authority.py": ("check_duplicate_authority", "Detect duplicate current-truth pages and divergent mirrors."),
        "governance/tools/check_status_claims.py": ("check_status_claims", "Validate front matter statuses and forbidden status contradictions."),
        "governance/tools/check_contract_drift.py": ("check_contract_drift", "Compare API, CLI, config, and error prose against machine-readable contracts."),
        "governance/tools/check_asset_budget.py": ("check_asset_budget", "Validate image and asset size budgets."),
        "governance/tools/check_generated_freshness.py": ("check_generated_freshness", "Validate generated artifacts against declared sources and freshness metadata."),
    }
    for path, (name, purpose) in tools.items():
        templates[path] = checker_script(name, purpose)

    templates["governance/ci/docs-quality-gates.yaml"] = docs_quality_ci()

    templates["drafts/README.md"] = dedent(
        f"""
        # Drafts

        Drafts are unpublished work in progress for {project_name}.

        Rules:
        - Drafts are not canonical.
        - Drafts must not be linked from current published docs unless clearly labeled experimental.
        - Promote drafts into `pages/` only after review and source-authority assignment.
        """
    ).strip() + "\n"

    templates["archive/README.md"] = dedent(
        f"""
        # Archive

        Historical documentation for {project_name}.

        Archived documents are not current truth. When possible, archived pages should link to their current replacement.
        """
    ).strip() + "\n"

    reports = {
        "reports/link-check.csv": "path,target,status,message\n",
        "reports/duplicate-authority.csv": "path_a,path_b,status,message\n",
        "reports/nav-orphans.csv": "path,status,message\n",
        "reports/asset-budget.csv": "path,size_bytes,budget_bytes,status,message\n",
    }
    templates.update(reports)
    templates["reports/docs-architecture-map.json"] = json.dumps(
        {
            "system": project_name,
            "generated_at": today,
            "canonical_root": "pages",
            "contracts": ["contracts/openapi.json", "contracts/cli-schema.json", "contracts/config-schema.json"],
            "checks": [],
        },
        indent=2,
    ) + "\n"

    return templates


def format_path(path_template: str, *, review_date: str, year_month: str) -> str:
    return path_template.format(review_date=review_date, year_month=year_month)


def write_file(path: Path, content: str, *, force: bool, dry_run: bool) -> str:
    if path.exists() and not force:
        return "skip"
    if dry_run:
        return "write" if not path.exists() else "overwrite"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if path.suffix == ".py":
        try:
            path.chmod(path.stat().st_mode | 0o111)
        except OSError:
            pass
    return "write" if not path.exists() else "overwrite"


def scaffold(
    target: Path,
    *,
    project_name: str,
    site_config: str,
    force: bool,
    dry_run: bool,
    gitkeep: bool,
    today: str,
    review_date: str,
    year_month: str,
) -> Dict[str, int]:
    stats = {"dirs": 0, "written": 0, "skipped": 0, "overwritten": 0, "gitkeep": 0}

    all_dirs = [format_path(d, review_date=review_date, year_month=year_month) for d in DIRECTORIES]
    for rel in all_dirs:
        path = target / rel
        if not dry_run:
            path.mkdir(parents=True, exist_ok=True)
        stats["dirs"] += 1
        print(f"DIR   {path}")

    templates = build_templates(project_name, today, review_date, year_month)

    if site_config == "inside":
        templates["mkdocs.yml"] = mkdocs_config(
            project_name,
            "pages",
            "nav.yml is optional and is not consumed unless your build tooling merges it.",
        )
    elif site_config == "outside":
        outside_path = target.parent / "mkdocs.yml"
        outside_content = mkdocs_config(
            project_name,
            f"{target.name}/pages",
            "Generated by SGDA scaffold with --site-config outside.",
        )
        result = write_file(outside_path, outside_content, force=force, dry_run=dry_run)
        if result == "skip":
            stats["skipped"] += 1
        elif result == "overwrite":
            stats["overwritten"] += 1
        else:
            stats["written"] += 1
        print(f"{result.upper():5} {outside_path}")

    for rel, content in sorted(templates.items()):
        path = target / rel
        existed = path.exists()
        if existed and not force:
            result = "skip"
        else:
            if not dry_run:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
                if path.suffix == ".py":
                    try:
                        path.chmod(path.stat().st_mode | 0o111)
                    except OSError:
                        pass
            result = "overwrite" if existed else "write"

        if result == "skip":
            stats["skipped"] += 1
        elif result == "overwrite":
            stats["overwritten"] += 1
        else:
            stats["written"] += 1
        print(f"{result.upper():5} {path}")

    if gitkeep:
        templated_parents = {str((target / rel).parent) for rel in templates}
        for rel in all_dirs:
            folder = target / rel
            folder_key = str(folder)
            if folder_key in templated_parents:
                continue
            gitkeep_path = folder / ".gitkeep"
            if gitkeep_path.exists() and not force:
                stats["skipped"] += 1
                print(f"SKIP  {gitkeep_path}")
                continue
            if not dry_run:
                gitkeep_path.parent.mkdir(parents=True, exist_ok=True)
                gitkeep_path.write_text("", encoding="utf-8")
            stats["gitkeep"] += 1
            print(f"WRITE {gitkeep_path}")

    return stats


def parse_args() -> argparse.Namespace:
    today = _dt.date.today().isoformat()
    parser = argparse.ArgumentParser(
        description="Scaffold an SGDA documentation directory with template files and folders."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="docs",
        help="Target docs directory to create or update. Default: docs",
    )
    parser.add_argument(
        "--project-name",
        default=None,
        help="Project name used in generated templates. Default: target directory name title-cased",
    )
    parser.add_argument(
        "--site-config",
        choices=("inside", "outside", "none"),
        default="inside",
        help="Where to create mkdocs.yml. inside=target/mkdocs.yml, outside=target.parent/mkdocs.yml, none=no mkdocs.yml. Default: inside",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffolded files. Existing files are preserved by default.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without writing files.",
    )
    parser.add_argument(
        "--no-gitkeep",
        action="store_true",
        help="Do not add .gitkeep files to empty directories.",
    )
    parser.add_argument(
        "--today",
        default=today,
        help=f"Verification date stamped into templates. Default: {today}",
    )
    parser.add_argument(
        "--review-date",
        default=today,
        help=f"Initial architecture review directory date. Default: {today}",
    )
    parser.add_argument(
        "--year-month",
        default=today[:7],
        help=f"Initial draft folder year-month. Default: {today[:7]}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target).expanduser().resolve()
    project_name = args.project_name or target.name.replace("_", "-").replace("-", " ").title()

    print(f"SGDA scaffold target: {target}")
    print(f"Project name: {project_name}")
    print(f"Site config: {args.site_config}")
    print(f"Mode: {'dry-run' if args.dry_run else 'write'}")

    stats = scaffold(
        target,
        project_name=project_name,
        site_config=args.site_config,
        force=args.force,
        dry_run=args.dry_run,
        gitkeep=not args.no_gitkeep,
        today=args.today,
        review_date=args.review_date,
        year_month=args.year_month,
    )

    print("\nSummary")
    for key, value in stats.items():
        print(f"- {key}: {value}")

    if args.dry_run:
        print("\nDry run complete. Re-run without --dry-run to create files.")
    else:
        print("\nScaffold complete.")
        if args.site_config == "inside":
            print(f"Try: cd {target} && mkdocs serve")
        elif args.site_config == "outside":
            print(f"Try: cd {target.parent} && mkdocs serve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
