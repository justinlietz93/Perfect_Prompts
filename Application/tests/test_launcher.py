from pathlib import Path

from perfect_prompts.infrastructure.launcher import installer


def test_gui_executable_prefers_sibling_console_script(tmp_path, monkeypatch):
    cli = tmp_path / "perfect-prompts-cli"
    gui = tmp_path / "perfect-prompts"
    cli.write_text("cli", encoding="utf-8")
    gui.write_text("gui", encoding="utf-8")
    monkeypatch.setattr(installer.sys, "argv", [str(cli), "install-launcher"])
    monkeypatch.setattr(installer.shutil, "which", lambda _name: None)
    assert installer._gui_executable() == gui.absolute()
