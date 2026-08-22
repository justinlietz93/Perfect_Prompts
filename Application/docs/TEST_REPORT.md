# Perfect Prompts v0.2.1 Validation Report

## Scope

v0.2.1 is an application-identity/icon patch over the validated v0.2.0 filesystem-first repository/application release. The repository taxonomy, Prompt Beacon behavior, GUI library workflow, and source-corpus migration are unchanged.

The original v0.2.0 migration remains:

- source files: **3,036**;
- mapped: **3,036 / 3,036**;
- missing: **0**;
- unmapped: **0**;
- byte-identical relocations: **3,026**;
- documented intentional source edits: **10**.

`REORGANIZATION_MANIFEST.json` remains the old→new source-path authority.

## Application tests

```text
18 passed, 1 skipped
```

The skipped test is the real PySide6 window-construction smoke test because PySide6 is not installed in this execution environment. The passing suite includes the existing search/index/sync/add/remove/batch/settings/launcher/package tests plus native icon validation.

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
- Windows file identifies as an **MS Windows icon resource**;
- `.ico` contains **10 native sizes**: 16, 20, 24, 32, 40, 48, 64, 96, 128, and 256 px;
- 256 px ICO surface has transparent exterior corners;
- internal logo artwork is preserved; derivation removes the border-connected outer black canvas and adds transparent icon padding;
- derivation is reproducible through `Application/scripts/build_icons.py`.

Derived SHA-256 values:

```text
76b2e2a5b52bed3b79543f6624754e1a5777c494fd6ee75c82ccebba8176c900  perfect-prompts-icon.png
681431f0b8b07f37cbe858de21bfd43ad62181cf3e0842e2afae6a5e6131e665  perfect-prompts-icon-256.png
526ad85914527f55c6121686e4568adb6f1e034a8eb681ea29c13143c3726b2b  perfect-prompts.ico
```

## Launcher behavior

Windows shortcuts use the multi-resolution `.ico`. The GUI also sets a stable `PerfectPrompts.Desktop` AppUserModelID so Windows taskbar/pinned surfaces identify the process as Perfect Prompts rather than a generic Python application.

Linux launcher installation copies the transparent 256 px icon to the user's standard hicolor icon-theme location:

```text
~/.local/share/icons/hicolor/256x256/apps/perfect-prompts.png
```

The `.desktop` launcher then uses the native icon name `perfect-prompts` rather than pointing at an arbitrary source PNG.

## Distribution smoke test

A clean wheel was built without build isolation:

```text
perfect_prompts-0.2.1-py3-none-any.whl
```

Wheel SHA-256 during validation:

```text
c975a885614b6005840835e371c7b8f0adc1dd281fdb5bc06fa037a7a89f05ea
```

The wheel was installed into a fresh isolated virtual environment without dependencies. `perfect-prompts-cli --version` reported `Perfect Prompts 0.2.1`, and all three packaged runtime icon resources were present.

## GUI runtime boundary

The Qt source compiles and the GUI smoke test remains present. A live Qt window cannot be constructed in this execution environment because PySide6 is unavailable here; the normal installer installs the `gui` extra before creating launchers.
