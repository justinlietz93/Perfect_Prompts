# Perfect Prompts Application Architecture

## System shape

```text
                ┌───────────────────────────────┐
                │ Repository filesystem         │
                │ human/GitHub source of truth  │
                └──────────────┬────────────────┘
                               │
             native edits ─────┼───── GUI add/remove
                               │
                               ▼
                ┌───────────────────────────────┐
                │ Prompt Beacon                 │
                │ rebuild + incremental sync    │
                │ SQLite FTS5 read projection   │
                └──────────────┬────────────────┘
                               │
                    search / batch / preview
                               │
                               ▼
                ┌───────────────────────────────┐
                │ Application use cases         │
                └──────────────┬────────────────┘
                               │
                     Lamina-style boundary
                               │
                               ▼
                ┌───────────────────────────────┐
                │ PySide6 presentation          │
                │ Search | Batch | Library      │
                └───────────────────────────────┘
```

## Ownership

- `domain/`: path-derived artifact classification.
- `contracts/`: stable request/result shapes and small capability interfaces.
- `application/`: search, batch, preview, export, add/remove, rebuild, and sync operations.
- `infrastructure/search/`: Prompt Beacon and content extraction.
- `infrastructure/filesystem/`: guarded filesystem mutations.
- `infrastructure/execution/`: Lamina-derived background-task boundary.
- `infrastructure/launcher/`: OS-native launcher installation.
- `presentation/`: thin controllers and Qt views.
- `composition/`: the concrete object graph.

## Why the filesystem owns truth

A prompt/context library is naturally inspectable material. Hiding it behind application storage would damage Git history, direct reuse, editor workflows, GitHub navigation, and portability. SQLite is therefore a read model only.

## Incremental synchronization

Each indexed path records path, type/classification, size, modification timestamp, and whether body extraction succeeded. `sync()` walks the visible library tree and compares those fields to the current read model. New/changed files are re-extracted; missing paths are removed from both the node table and FTS table. Unchanged files require no content extraction.

The GUI invokes sync automatically while leaving an explicit Sync control available.

## Application-source exclusion

The repository's `Application/` directory is intentionally excluded from Prompt Beacon's default corpus. It is implementation machinery, not prompt/context library content. The rest of the repository, including external references, remains indexable; source-scope metadata lets the UI distinguish project-authored from external material.
