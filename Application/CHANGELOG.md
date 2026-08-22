# Changelog

## 0.2.1 — 2026-08-22

- Rebuilt the supplied Perfect Prompts artwork into proper native application icon assets instead of treating the original square PNG as the launcher icon directly.
- Preserved the original user-supplied logo unchanged under `assets/source/`.
- Added a transparent 1024 px master icon with native breathing room and transparent exterior corners.
- Rebuilt the Windows `.ico` as a true multi-resolution icon container (16–256 px).
- Added a native Linux 256 px icon-theme asset and launcher installation under the user hicolor theme.
- Added a stable Windows AppUserModelID so taskbar/pinned surfaces resolve Perfect Prompts as its own application identity.
- Added reproducible programmatic icon generation and icon-asset validation tests.

## 0.2.0 — 2026-08-22

- Reoriented Perfect Prompts around a filesystem-first, human-browseable repository taxonomy.
- Added the `Search`, `Batch`, and `Library` desktop workflow.
- Added GUI file/folder import and confirmed artifact removal against the real repository filesystem.
- Added Prompt Beacon incremental synchronization so external filesystem edits, moves, additions, and removals converge into the disposable search index.
- Added programmatic `sync`, `add`, and `remove` CLI commands.
- Made project-authored material the default GUI search scope while preserving filterable external-reference search.
- Isolated application source under `Application/`; application code is excluded from the library search corpus by default.
- Preserved all 3,036 source-corpus files through the reorganization, with only documented path/metadata edits.
- Retained the supplied Perfect Prompts logo as native application identity and generated Windows icon variants from it.
