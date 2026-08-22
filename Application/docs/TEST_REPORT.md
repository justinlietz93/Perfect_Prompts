# Perfect Prompts v2.0.1 Validation Report

## Scope

`v2.0.1` is a patch release over `v2.0.0` focused on Linux desktop identity and native icon resolution. The filesystem-first repository reorganization and desktop GUI introduced in `v2.0.0` are otherwise unchanged.

## Repository continuity

The `v2.0.0` source-corpus migration authority remains `REORGANIZATION_MANIFEST.json`:

- source files: **3,036**;
- mapped: **3,036 / 3,036**;
- missing: **0**;
- unmapped: **0**;
- byte-identical relocations: **3,026**;
- documented intentional source edits: **10**.

## Linux icon/launcher repair

The reported failure mode was reproduced from the installed launcher state: the icon file existed at the standard user hicolor location, while the `.desktop` entry referenced only `Icon=perfect-prompts`. That leaves rendering dependent on desktop/icon-theme lookup and cache behavior, and it does not by itself guarantee that the running Qt window will associate with the launcher.

`v2.0.1` changes that contract:

- generated `.desktop` files use an **absolute `Icon=` path** to the installed 256 px PNG;
- all packaged hicolor raster sizes are installed when available (16, 24, 32, 48, 64, 128, 256, 512 px);
- `StartupWMClass=perfect-prompts` is included in the launcher;
- Qt publishes the matching `perfect-prompts` application/desktop-file identity while retaining the visible display name **Perfect Prompts**;
- `update-desktop-database` and `gtk-update-icon-cache` are invoked opportunistically after installation when present;
- desktop shortcut placement uses `xdg-user-dir DESKTOP` when available rather than assuming `~/Desktop`.

The original user-supplied image remains preserved unchanged under `Application/assets/source/`. Native PNG and ICO assets remain derived from that source.

## Automated tests

```text
20 passed
```

The suite now includes launcher tests that verify:

- absolute icon paths in Linux `.desktop` files;
- matching `StartupWMClass`;
- installation of the complete packaged hicolor size set;
- preservation of the real 256 px source asset rather than replacing it with fallback data.

The existing search/index/sync/add/remove/batch/settings/package/icon tests also remain passing.

## Direct launcher smoke test

A temporary HOME and fake installed `perfect-prompts` executable were used to execute the real Linux launcher installer against the repository. The generated entry contained:

```text
Icon=<absolute HOME path>/.local/share/icons/hicolor/256x256/apps/perfect-prompts.png
StartupWMClass=perfect-prompts
```

and all eight packaged Linux icon sizes were copied into the temporary user hicolor tree.

## Version surfaces

The active release version is represented consistently at:

```text
VERSION
README.md
Application/pyproject.toml
Application/src/perfect_prompts/__init__.py
Application/docs/PRODUCT_DEFINITION.md
Application/CHANGELOG.md
Application/tests/test_package.py
```

The repository and desktop application identify as **2.0.1**.
