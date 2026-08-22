"""Graphical Perfect Prompts application entry point."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from perfect_prompts import __version__
from perfect_prompts.infrastructure.settings.user_settings import UserSettingsStore


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="perfect-prompts", add_help=True)
    parser.add_argument("--root", type=Path, default=None, help="Perfect Prompts repository root to open")
    parser.add_argument("--version", action="version", version=f"Perfect Prompts {__version__}")
    args, qt_args = parser.parse_known_args(argv)
    try:
        from PySide6.QtGui import QIcon
        from PySide6.QtWidgets import QApplication, QFileDialog
    except ImportError:
        print("PySide6 is required for the GUI. Run: python install.py", file=sys.stderr)
        return 2

    from perfect_prompts.composition.container import build_container
    from perfect_prompts.presentation.qt.dispatch import GuiDispatcher
    from perfect_prompts.presentation.qt.main_window import MainWindow
    from perfect_prompts.resources import icon_png_path

    if os.name == "nt":
        # Give Windows a stable application identity so pinned/taskbar surfaces
        # use the Perfect Prompts icon instead of a generic Python identity.
        try:
            import ctypes

            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("PerfectPrompts.Desktop")
        except Exception:
            pass

    app = QApplication([sys.argv[0], *qt_args])
    app.setApplicationName("Perfect Prompts")
    app.setOrganizationName("Neuroca")
    app.setWindowIcon(QIcon(str(icon_png_path())))
    settings = UserSettingsStore()
    root = args.root.expanduser().resolve() if args.root else settings.load_last_root() or discover_repository_root()
    if root is None or not root.is_dir():
        selected = QFileDialog.getExistingDirectory(None, "Select Perfect Prompts repository", str(Path.cwd()))
        if not selected:
            return 0
        root = Path(selected)
    dispatcher = GuiDispatcher()
    window = MainWindow(root, lambda selected_root: build_container(selected_root, dispatcher.post), settings.save_last_root)
    window.show()
    return app.exec()


def discover_repository_root() -> Path | None:
    candidates = [Path.cwd(), Path(__file__).resolve()]
    seen: set[Path] = set()
    for candidate in candidates:
        start = candidate if candidate.is_dir() else candidate.parent
        for directory in (start, *start.parents):
            directory = directory.resolve()
            if directory in seen:
                continue
            seen.add(directory)
            if (directory / "Prompts").is_dir() and (directory / "Standards").is_dir() and (directory / "Skills").is_dir():
                return directory
    return None


if __name__ == "__main__":
    raise SystemExit(main())
