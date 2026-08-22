# Perfect Prompts v2.0.0 Validation Report

## Release lineage

`v2.0.0` is the first Perfect Prompts release after the published `v1.0.0` repository release.

The major-version increment is intentional. The desktop GUI is additive, but this release also reorganizes repository paths into the filesystem-first semantic taxonomy documented by `REPOSITORY_MAP.md`. Direct path consumers of the v1.0.0 layout can therefore require migration, so the release is treated as semantically breaking rather than as `v1.1.0`.

The earlier local `0.2.x` labels were development-package numbering and were never the correct Perfect Prompts release lineage. They have been removed from release metadata.

## Repository migration

The source-corpus migration represented by `REORGANIZATION_MANIFEST.json` remains:

- source files: **3,036**;
- mapped: **3,036 / 3,036**;
- missing: **0**;
- unmapped: **0**;
- unexpected changes: **0**;
- byte-identical relocations: **3,026**;
- documented intentional source edits: **10**.

`REORGANIZATION_MANIFEST.json` is the old→new source-path authority.

## Application tests

```text
18 passed
```

The suite includes search/index/sync/add/remove/batch/settings/launcher/package tests, native icon validation, and a real PySide6 window-construction smoke test using Qt's offscreen platform.

Python bytecode compilation of application source, tests, and scripts also passed.

## Native icon validation

The original user-supplied image is preserved unchanged at:

```text
Application/assets/source/perfect-prompts-logo-source.png
```

Source SHA-256:

```text
e655cb15971ed1e035183dba432db12e944342907d461d68eaa0f94c2d94bf18
```

Derived launcher assets:

```text
Application/assets/perfect-prompts-icon.png
Application/assets/perfect-prompts-icon-256.png
Application/assets/perfect-prompts.ico
```

Validation results:

- 1024×1024 PNG is RGBA with transparent exterior corners;
- visible artwork is inset from the canvas rather than hard-cropped to the square boundary;
- 256×256 Linux PNG is RGBA with transparent exterior corners;
- Windows file identifies as an MS Windows icon resource;
- `.ico` contains 10 native sizes: 16, 20, 24, 32, 40, 48, 64, 96, 128, and 256 px;
- 256 px ICO surface has transparent exterior corners;
- internal logo artwork is preserved;
- derivation is reproducible through `Application/scripts/build_icons.py`.

Derived SHA-256 values:

```text
76b2e2a5b52bed3b79543f6624754e1a5777c494fd6ee75c82ccebba8176c900  perfect-prompts-icon.png
681431f0b8b07f37cbe858de21bfd43ad62181cf3e0842e2afae6a5e6131e665  perfect-prompts-icon-256.png
526ad85914527f55c6121686e4568adb6f1e034a8eb681ea29c13143c3726b2b  perfect-prompts.ico
```

## Launcher behavior

Windows shortcuts use the multi-resolution `.ico`. The GUI sets the stable `PerfectPrompts.Desktop` AppUserModelID so Windows taskbar and pinned surfaces identify the process as Perfect Prompts rather than as a generic Python application.

Linux launcher installation copies the transparent 256 px icon to:

```text
~/.local/share/icons/hicolor/256x256/apps/perfect-prompts.png
```

The `.desktop` launcher uses the native icon name `perfect-prompts`.

## Distribution smoke test

A clean wheel was built from the v2.0.0 application source:

```text
perfect_prompts-2.0.0-py3-none-any.whl
```

Wheel SHA-256 during validation:

```text
d451fe3d43ffb56aaa5f88740503d0955da3dba32c2e4131710baf80c8fe746c
```

The wheel was installed into a fresh isolated virtual environment without dependencies. `perfect-prompts-cli --version` reported:

```text
Perfect Prompts 2.0.0
```

All three packaged runtime icon resources were present.

## Version surfaces

The release version is represented consistently at:

```text
VERSION
README.md
Application/pyproject.toml
Application/src/perfect_prompts/__init__.py
Application/docs/PRODUCT_DEFINITION.md
Application/CHANGELOG.md
Application/tests/test_package.py
```

The repository release and desktop application package both identify as **2.0.0**.
