# Changelog

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
