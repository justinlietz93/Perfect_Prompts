# Source Lineage

## Perfect Prompts corpus

The v0.2 repository was reorganized from the user-supplied `Perfect_Prompts.zip` corpus. The source contained **3,036 files**.

The migration validator maps every source file to its new location:

- 3,036 / 3,036 source files mapped;
- 0 missing;
- 0 unmapped;
- 3,026 byte-identical after relocation;
- 10 intentionally edited.

The ten edits are limited to the root README, `.gitmodules`, and path-only repairs required because APEX/Go documentation references moved with the reorganization. `REORGANIZATION_MANIFEST.json` records the complete old→new mapping and byte-identity result.

## Beacon

Prompt Beacon is derived from the user-supplied standalone Beacon repository, itself extracted from Orchestra's local search architecture. The retained behavior includes SQLite FTS5, `porter unicode61`, broad prefix terms, normalized quoted phrases, BM25 ranking, bounded extraction, single-query exports, and independent batch-query exports.

Perfect Prompts adds repository-aware classification and incremental synchronization for filesystem mutations.

## Lamina

The desktop application uses the supplied Lamina repository as the GUI/application architecture template. The implementation follows Lamina's Python-source-of-truth, progressive-complexity, thin-presentation, composition-root, background-work, and GUI-thread-dispatch principles rather than copying an opaque project format.

## Application identity

The original user-supplied Perfect Prompts artwork is preserved byte-for-byte at `Application/assets/source/perfect-prompts-logo-source.png`. The launcher assets are derived rather than pretending that source square is already a native icon: exterior border-connected black canvas is removed, transparent breathing room is added, and platform-specific outputs are generated.

- `Application/assets/perfect-prompts-icon.png` — transparent 1024×1024 master for Qt/window surfaces.
- `Application/assets/perfect-prompts-icon-256.png` — native Linux raster launcher asset.
- `Application/assets/perfect-prompts.ico` — multi-resolution Windows icon container covering 16–256 px.
- `Application/scripts/build_icons.py` — reproducible derivation script.

No logo geometry, color treatment, or internal artwork is redesigned; the transformation is limited to icon-surface preparation and native packaging.
