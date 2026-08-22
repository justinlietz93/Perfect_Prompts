# Perfect Prompts Desktop Application — Product Definition

**Version:** 2.0.2  
**Product name:** Perfect Prompts

Perfect Prompts is a filesystem-first prompt/context engineering library with an optional desktop interface over the same repository.

## Product identity

The application is **Perfect Prompts**. It uses native icon assets derived from the supplied Perfect Prompts logo for the window icon, Linux launchers/application menu, and Windows shortcuts. No secondary product name is introduced.

## Primary invariant

> **The repository filesystem is the library.**

Prompts, standards, skills, rules, personas, methods, scripts, examples, and external references remain ordinary files and directories. GitHub and native file browsing are first-class interfaces, not fallbacks.

The application may create only disposable or user-local operational state:

- `.perfect-prompts/index.sqlite3` and query exports;
- user-local last-opened-repository settings;
- the isolated application virtual environment;
- OS launcher metadata.

None of those replaces a library artifact.

## Main workflows

### Search

One query field is the default entry point. Prompt Beacon searches the repository, ranks matches, supports optional metadata filters, and lets the user preview/open/copy/export or remove an artifact.

### Batch

Several independent queries can be executed together while preserving the order, result set, and JSON export of each query.

### Library

The Library tab is a direct view of the actual repository filesystem. The user can browse it, open artifacts, reveal folders, add files/folders, or remove artifacts. The same changes can be made outside the application using the operating system, Git, an editor, or a terminal.

## Filesystem synchronization contract

Prompt Beacon provides two index operations:

- **Rebuild**: recreate the disposable search projection from scratch.
- **Sync**: compare current repository paths/metadata against the projection, extract only new/changed files, and remove index rows for deleted paths.

The desktop application synchronizes at startup, after GUI mutations, when the application regains focus, periodically while open, and whenever the user presses **Sync**.

This means a user can edit the repository in an ordinary file manager or editor without entering those changes twice in the GUI.

## Repository organization contract

The human-facing repository taxonomy is semantic first:

- Agent Instructions
- Guidelines
- Methodologies
- Personas
- Prompts
- Rules
- Skills
- Standards
- External References

Prompt representation is a second-level concern under `Prompts/`, separating portable forms from code/runtime bindings.

## Search contract

Prompt Beacon retains the useful Beacon/Orchestra query semantics:

- SQLite FTS5 with `porter unicode61`;
- broad OR-prefix behavior for ordinary terms;
- normalized strict quoted phrases;
- mixed phrase + broad-term queries;
- ascending BM25 rank;
- bounded snippets and content extraction;
- independent batch-query exports.

Perfect Prompts adds path-derived classification for area, artifact type, runtime/representation, and source scope. Project-authored material is the GUI default; external references remain available through the source filter.

## GUI architecture contract

The application follows Lamina's core constraints:

- Python is source of truth;
- simple operations remain simple;
- Qt does not own domain/application behavior;
- filesystem/search adapters remain behind small application boundaries;
- concrete wiring stays in the composition root;
- blocking index/sync/batch work is background work;
- GUI-thread marshalling happens through one dispatch boundary.

## Safety contract for GUI removal

Removal is explicit and confirmed. The application refuses to remove the repository root or its own protected application/infrastructure paths. Library folders and artifacts can otherwise be removed from the GUI just as they can from the native filesystem.

## Non-goals

Perfect Prompts is not an opaque content database, cloud service, prompt marketplace, or mandatory editor. It does not require AI/API access for core search and library management, and it does not force users to abandon Git, native files, or ordinary editors.
