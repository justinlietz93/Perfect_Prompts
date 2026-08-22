# Changelog

## v2.0.4 - 2026-08-22

- Fixed Linux desktop launchers to invoke the verified runtime interpreter directly with `python -m perfect_prompts.main`, removing dependence on pip-generated GUI entry-point wrappers.
- Desktop shortcuts are now marked trusted with `gio` when available so GNOME-compatible desktops can launch newly rewritten `.desktop` files without manual "Allow Launching" intervention.
- Runtime repair now performs an actual Qt platform smoke test rather than stopping at import validation.

## 2.0.3 — 2026-08-22

- Fixed launcher repair when the stable per-user runtime already exists but its editable Perfect Prompts installation points at an older or removed checkout.
- `python install.py --repair-launcher` now always refreshes the editable installation against the current repository before rewriting launchers.
- Added runtime validation that imports Perfect Prompts and the Qt GUI stack from the repaired environment and verifies that `perfect_prompts.__file__` resolves to the current `Application/src/` tree.
- Added a regression test for an existing-but-stale runtime, which was the case missed by v2.0.2.

## 2.0.2 — 2026-08-22

- Fixed a launcher regression caused by keeping the installed Python virtual environment inside the tracked `Application/` directory. Replacing `Application/` during an update could therefore remove the launch target while leaving a desktop shortcut behind.
- Moved the default desktop runtime to stable per-user application data (`~/.local/share/perfect-prompts/runtime/venv` on Linux; `%LOCALAPPDATA%\PerfectPrompts\runtime\venv` on Windows).
- `python install.py --repair-launcher` now recreates the runtime automatically when it is missing instead of failing or writing a shortcut to a vanished executable.
- Preserved `--venv` as an explicit override for development/custom installations.

## 2.0.1 — 2026-08-22

### Fixed

- Fixed Linux launcher/icon resolution by writing an absolute icon path into generated `.desktop` files instead of relying solely on icon-theme name lookup.
- Installed the complete hicolor icon-size set when available, while retaining the 256 px fallback.
- Added Linux desktop identity metadata (`StartupWMClass=perfect-prompts`) and Qt desktop-file identity so running windows associate with the Perfect Prompts launcher instead of a generic application/gear icon.
- Refreshes desktop-entry and icon caches after launcher installation when the platform tools are available.
- Desktop-folder resolution now uses `xdg-user-dir DESKTOP` when available instead of assuming `~/Desktop`.
- Added `python install.py --repair-launcher` for a fast launcher/icon repair without dependency reinstall or index rebuild.


## 2.0.0 — 2026-08-22

First Perfect Prompts release after the published `v1.0.0` repository release. This is a major release because it both adds the optional desktop application and reorganizes repository paths, which can break consumers that referenced the previous filesystem layout directly.

### Repository

- Reorganized the repository around semantic artifact classes while preserving ordinary GitHub and native-filesystem use.
- Added `REPOSITORY_MAP.md` and the reorganization manifest so previous paths remain traceable.
- Preserved the existing prompt, skill, persona, rule, methodology, script, runtime-binding, architecture-standard, research-standard, APEX, NASA, and external-reference corpus.
- Kept the repository filesystem as the authoritative library rather than moving artifacts into an application database.

### Desktop application

- Added the optional Perfect Prompts desktop GUI using the Lamina-oriented Python/Qt architecture.
- Added Search, Batch, and Library workflows.
- Added Prompt Beacon, a Perfect Prompts-specialized Beacon index/query layer with FTS5/BM25 search, quoted phrases, broad prefix matching, filters, exports, and incremental filesystem synchronization.
- Added GUI and CLI add/remove operations against the real repository filesystem.
- Added external filesystem change synchronization so edits made through Git, editors, terminals, or file managers converge into the disposable search index.
- Added native Linux and Windows launcher installation.

### Application identity

- Uses Perfect Prompts as the sole product/application name.
- Preserves the user-supplied Perfect Prompts logo as source artwork.
- Generates proper transparent PNG launcher assets and a true multi-resolution Windows `.ico` rather than using the original square source image directly as an icon.
- Adds a stable Windows AppUserModelID for taskbar and pinned-launcher identity.

### Compatibility

- The desktop application is optional; the repository remains directly browsable and editable without installation.
- `.perfect-prompts/` contains only disposable/local application state and can be rebuilt from the repository files.
- The repository reorganization is the reason this release advances from `v1.0.0` to `v2.0.0` rather than `v1.1.0`.
