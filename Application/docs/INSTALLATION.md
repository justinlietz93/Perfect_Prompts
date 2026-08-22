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
python install.py --repair-launcher
```

`--repair-launcher` rewrites the native launcher/icon integration using the existing `Application/.venv` without reinstalling dependencies or rebuilding Prompt Beacon. It is the fastest way to repair an already-installed Linux launcher after upgrading.

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

Windows shortcuts use the packaged multi-resolution `perfect-prompts.ico`. Linux installation copies the available hicolor PNG sizes into `~/.local/share/icons/hicolor/<size>/apps/perfect-prompts.png`; generated `.desktop` files use the absolute 256 px icon path so the icon does not depend on a stale desktop/icon-theme cache. The launcher also declares `StartupWMClass=perfect-prompts`, and the Qt application publishes the matching desktop-file identity so running windows bind to the Perfect Prompts launcher instead of a generic gear icon. The installer refreshes desktop/icon caches when the relevant platform utilities are available. The original supplied artwork is retained separately under `Application/assets/source/`.
