import os
from pathlib import Path
import pytest

PySide6 = pytest.importorskip("PySide6")
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication
from perfect_prompts.composition.container import build_container
from perfect_prompts.presentation.qt.dispatch import GuiDispatcher
from perfect_prompts.presentation.qt.main_window import MainWindow


def test_real_window_constructs_offscreen(tmp_path: Path):
    p = tmp_path / "Prompts" / "Portable" / "Plaintext"; p.mkdir(parents=True)
    (p / "a.txt").write_text("hello", encoding="utf-8")
    app = QApplication.instance() or QApplication([])
    dispatcher = GuiDispatcher(); window = MainWindow(tmp_path, lambda root: build_container(root, dispatcher.post), lambda root: None)
    window.show(); app.processEvents(); assert window.windowTitle() == "Perfect Prompts"
    window.close(); app.processEvents()
