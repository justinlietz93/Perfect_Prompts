# Installation

## End-user install

From the Perfect Prompts repository root:

```bash
python install.py
```

The installer:

1. creates `Application/.venv/`;
2. installs the Perfect Prompts application and GUI dependencies;
3. builds the initial Prompt Beacon index against the repository root;
4. saves that repository as the default library;
5. creates native application-menu/Start Menu and desktop launchers unless disabled.

The supplied Perfect Prompts logo is preserved as source artwork and converted into native launcher assets: a transparent PNG for Qt/Linux surfaces and a multi-resolution `.ico` for Windows shortcuts.

### Options

```bash
python install.py --no-desktop
python install.py --no-menu
python install.py --skip-index
python install.py --without-pdf
```

`--without-pdf` disables the optional PDF text-extraction dependency; PDFs remain searchable by path/name.

## Development

```bash
cd Application
python -m venv .venv
source .venv/bin/activate
pip install -e ".[gui,pdf,dev]"
pytest
perfect-prompts --root ..
```

On Windows activate with `Application\.venv\Scripts\activate`.

## Uninstall behavior

The library itself does not need uninstalling because it is ordinary repository content. Removing `Application/.venv/`, OS shortcuts, user-local Perfect Prompts settings, and `.perfect-prompts/` removes application state while leaving every library artifact intact.

## Native icon installation

Windows shortcuts use the packaged multi-resolution `perfect-prompts.ico`. Linux installation copies the transparent 256 px icon into `~/.local/share/icons/hicolor/256x256/apps/perfect-prompts.png` and registers launchers with `Icon=perfect-prompts`. The original supplied artwork is retained separately under `Application/assets/source/`.
