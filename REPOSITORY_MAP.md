# Repository Reorganization Map

This repository is organized for **native filesystem and GitHub use first**. The desktop application is an optional interface over the same files. No library artifact is stored only in an application database.

## Previous → current locations

| Previous path | Current path | Rationale |
|---|---|---|
| `AGENTS_library/` | `Agent_Instructions/` | Persistent agent behavior is a first-class artifact type. |
| `Methodologies/` | `Methodologies/` | Already semantic and clear. |
| `PERSONAS/` | `Personas/` | Human-readable casing; representation folders renamed by target format. |
| `STANDARDS_REPOSITORY/apex/` | `Standards/APEX/` | Standards grouped by authority/domain. |
| `STANDARDS_REPOSITORY/architecture_standards/` | `Standards/Architecture/` | Architecture is directly browseable. |
| `STANDARDS_REPOSITORY/nasa/` | `Standards/NASA/` | External authority retained as its own standards family. |
| `STANDARDS_REPOSITORY/research_standards/` | `Standards/Research/` | Research/publication standards grouped together. |
| `STANDARDS_REPOSITORY/prompt-templates/` | `Prompts/Templates/` | Prompt templates are prompt artifacts, not standards themselves. |
| `general_guidelines/` | `Guidelines/` | Cross-cutting guidance. |
| `rules/` | `Rules/` | Scoped reusable rulesets. |
| `skills/` | `Skills/` | Reusable procedural packages. |
| `python/`, `typescript/`, `rust/`, `go/` | `Prompts/Runtime_Bindings/<Runtime>/` | Code-embedded prompt implementations remain intact but no longer define the root taxonomy. |
| `plaintext/`, `structured_text/`, `json/` | `Prompts/Portable/<Format>/` | Human/pasteable and structured portable representations grouped together. |
| `submodules/` | `External_References/` | Clearly separates external/reference corpora from project-authored material. |

## Design rule

**Meaning first, representation second.** A person browsing the repository should start from the kind of artifact they need. Runtime and serialization variants remain available without dominating the top-level structure.

Historical names are preserved in Git history and this map. The application index is disposable and can always be rebuilt from these files.
