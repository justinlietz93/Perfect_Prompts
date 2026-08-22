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


def test_linux_desktop_entry_invokes_verified_python_module(tmp_path):
    python = tmp_path / "runtime" / "bin" / "python"
    root = tmp_path / "repo"
    icon = tmp_path / "icons" / "perfect-prompts.png"
    content = installer._desktop_entry(python=python, root=root, icon=icon)
    assert f"Icon={icon}" in content
    assert "Icon=perfect-prompts\n" not in content
    assert "StartupWMClass=perfect-prompts" in content
    assert f"TryExec={python}" in content
    assert f'Exec="{python}" -m perfect_prompts.main --root "{root}"' in content
    assert "perfect-prompts --root" not in content


def test_linux_installer_uses_runtime_python_and_trusts_desktop(tmp_path, monkeypatch):
    home = tmp_path / "home"
    repo = tmp_path / "repo"
    runtime_python = tmp_path / "runtime" / "venv" / "bin" / "python"
    runtime_python.parent.mkdir(parents=True)
    runtime_python.write_text("python", encoding="utf-8")

    for size in (16, 32, 48, 64, 128, 256, 512):
        source = repo / "Application" / "assets" / "icons" / "hicolor" / f"{size}x{size}" / "apps" / "perfect-prompts.png"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_bytes(f"png-{size}".encode())

    trusted = []
    monkeypatch.setattr(installer.Path, "home", classmethod(lambda cls: home))
    monkeypatch.setattr(installer.sys, "executable", str(runtime_python))
    monkeypatch.setattr(installer, "_desktop_directory", lambda: home / "Desktop")
    monkeypatch.setattr(installer, "_trust_desktop_file", lambda path: trusted.append(path))
    monkeypatch.setattr(installer, "_refresh_linux_desktop_caches", lambda: None)
    fallback_source = tmp_path / "fallback.png"
    fallback_source.write_bytes(b"fallback")
    monkeypatch.setattr(installer, "icon_png_256_path", lambda: fallback_source)

    receipt = installer._install_linux(repo, desktop=True, menu=True)
    menu_file = home / ".local" / "share" / "applications" / "perfect-prompts.desktop"
    desktop_file = home / "Desktop" / "Perfect Prompts.desktop"
    icon_256 = home / ".local" / "share" / "icons" / "hicolor" / "256x256" / "apps" / "perfect-prompts.png"

    assert menu_file in receipt.paths
    assert desktop_file in receipt.paths
    assert desktop_file in trusted
    assert icon_256 in receipt.paths
    assert icon_256.read_bytes() == b"png-256"
    content = menu_file.read_text(encoding="utf-8")
    assert f"Icon={icon_256}" in content
    assert f'TryExec={runtime_python.absolute()}' in content
    assert f'Exec="{runtime_python.absolute()}" -m perfect_prompts.main --root "{repo}"' in content
    for size in (16, 32, 48, 64, 128, 256, 512):
        assert (home / ".local" / "share" / "icons" / "hicolor" / f"{size}x{size}" / "apps" / "perfect-prompts.png").is_file()
