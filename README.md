![Perfect Prompts Banner](https://github.com/user-attachments/assets/2ef86d9f-a64f-40e8-a9ad-fc4593ccb3b7)

# Perfect Prompts

**Current release: v2.0.0**

A filesystem-first library for **prompt engineering, context engineering, agent control, reusable AI workflows, research methodology, and LLM tooling**, with an optional desktop application for fast search and library management.

Perfect Prompts is intentionally useful in two completely independent ways:

1. **Open the repository normally** in your file manager, editor, terminal, or GitHub and browse/copy the artifacts directly.
2. **Launch the Perfect Prompts desktop application** when you want indexed search, batch queries, previews, or GUI-based add/remove operations.

The GUI does not own the library. The files do.

## Repository organization

The repository is now organized by **what an artifact is**, with format/runtime differences below that level instead of dominating the root structure.

```text
Perfect_Prompts/
├── Agent_Instructions/      persistent agent operating instructions
├── Guidelines/              cross-cutting guidance
├── Methodologies/           reusable interaction/design methods
├── Personas/                role/persona definitions and target formats
├── Prompts/
│   ├── Templates/           standalone and specialized prompt templates
│   ├── Portable/            plaintext, structured-text, and JSON forms
│   └── Runtime_Bindings/    Python, TypeScript, Rust, and Go implementations
├── Rules/                   scoped technical/scientific/domain rulesets
├── Skills/                  reusable procedural skill packages
├── Standards/
│   ├── APEX/
│   ├── Architecture/
│   ├── NASA/
│   └── Research/
├── External_References/     separately maintained/reference prompt libraries
├── Application/             optional Perfect Prompts desktop application
├── REPOSITORY_MAP.md        old → new path map and organization rationale
├── install.py               optional desktop-app installer
├── LICENSE
└── README.md
```

See [`REPOSITORY_MAP.md`](REPOSITORY_MAP.md) for the migration map from the older organically grown layout.

## Browse it directly

No application is required.

If you want an ordinary prompt you can start in `Prompts/`. If you need a persistent agent instruction, start in `Agent_Instructions/`. For procedural capability packages use `Skills/`; for scoped reasoning constraints use `Rules/`; for architecture/research/engineering authority use `Standards/`; and for role specialization use `Personas/`.

The representation split inside `Prompts/` is deliberate:

- `Portable/` is for directly inspectable/copyable prompt and context forms.
- `Runtime_Bindings/` keeps prompt implementations embedded in Python, TypeScript, Rust, and Go so application code can use them without translating them into a detached format.
- `Templates/` contains standalone/specialized prompt-template families.

Parallel implementations are not automatically assumed to be identical. They remain inspectable as their own artifacts.

## Desktop application

The desktop application is also called **Perfect Prompts** and uses the existing Perfect Prompts logo as its native application icon.

Its intentionally small workflow is:

```text
Search → inspect/open/copy → use the artifact
                   ↘ remove when needed

Batch → run several independent searches

Library → browse the real filesystem → add/remove/open artifacts
```

The primary feature is **Prompt Beacon**, a Perfect Prompts-specific version of the Beacon indexing/query system. It provides:

- local SQLite FTS5 indexing;
- broad prefix search for ordinary terms;
- strict quoted-phrase search;
- BM25 ranking;
- path, type, area, runtime, and source filters;
- single-query JSON export;
- independent batch-query execution and exports;
- extraction from ordinary text/source files, notebooks, Office/OpenDocument files, ZIP/skill packages, and PDFs when PDF support is installed;
- incremental synchronization after files are added, changed, moved, or removed.

The search database lives under `.perfect-prompts/` and is disposable. Delete it at any time; the application rebuilds it from the repository.

### Filesystem and GUI stay in sync

You can manage the library either way:

- add, move, edit, or remove files using your OS file manager, Git, terminal, or editor;
- add or remove artifacts from the **Library** tab in the GUI;
- remove a search result directly from the **Search** workspace;
- press **Sync** at any time, or let the application synchronize automatically while it is running.

The GUI uses the same repository paths. There is no private application-only artifact store.

## Install the desktop application

From the repository root:

```bash
python install.py
```

The installer creates an isolated environment under `Application/.venv/`, installs the GUI dependencies, builds the initial search index, and creates native launchers where supported:

- Linux application menu entry;
- Linux desktop launcher;
- Windows Start Menu shortcut;
- Windows desktop shortcut.

The launcher uses the supplied Perfect Prompts icon.

After installation you can also run the programmatic CLI:

```bash
perfect-prompts-cli sync
perfect-prompts-cli query "session handoff" --source-scope project
perfect-prompts-cli batch --queries 'architecture, "prompt template", context synthesis'
perfect-prompts-cli add ./new-skill --to Skills
perfect-prompts-cli remove Prompts/Portable/Plaintext/old-prompt.md
```

## What is in the library

The corpus includes multiple generations of material developed through active use, including:

- agent and multi-agent prompts;
- project scaffolding and task-generation prompts;
- context builders and session-state systems;
- rewriting, citation, mathematical-formatting, Mermaid, reasoning, critique, and analysis prompts;
- persistent AGENTS-style instructions;
- Guided Autonomy and emergence-oriented methodologies;
- software, research, architecture, documentation, NASA-derived, and APEX standards;
- scientific and technical rulesets;
- personas in several target formats;
- reusable skill packages;
- Python, TypeScript, Rust, Go, plaintext, JSON, and structured representations;
- scripts and examples that accompany those artifacts;
- external/reference prompt and skill libraries.

This remains a working corpus. The reorganization improves navigation without pretending every historical artifact is current or every parallel implementation is equivalent.

## Design rule

> **Meaning first, representation second; filesystem first, application second.**

A person should be able to understand and use the repository by browsing it normally. The desktop application exists to make a large library faster to search and manage, not to make the files dependent on the application.
