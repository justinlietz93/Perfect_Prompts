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


def test_linux_desktop_entry_uses_absolute_icon_and_matching_wm_class(tmp_path):
    target = tmp_path / "bin" / "perfect-prompts"
    root = tmp_path / "repo"
    icon = tmp_path / "icons" / "perfect-prompts.png"
    content = installer._desktop_entry(target=target, root=root, icon=icon)
    assert f"Icon={icon}" in content
    assert "Icon=perfect-prompts\n" not in content
    assert "StartupWMClass=perfect-prompts" in content
    assert f'TryExec={target}' in content
    assert f'Exec="{target}" --root "{root}"' in content


def test_linux_installer_copies_all_hicolor_sizes_and_writes_absolute_icon(tmp_path, monkeypatch):
    home = tmp_path / "home"
    repo = tmp_path / "repo"
    gui = tmp_path / "venv" / "bin" / "perfect-prompts"
    gui.parent.mkdir(parents=True)
    gui.write_text("launcher", encoding="utf-8")

    for size in (16, 32, 48, 64, 128, 256, 512):
        source = repo / "Application" / "assets" / "icons" / "hicolor" / f"{size}x{size}" / "apps" / "perfect-prompts.png"
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_bytes(f"png-{size}".encode())

    monkeypatch.setattr(installer.Path, "home", classmethod(lambda cls: home))
    monkeypatch.setattr(installer, "_gui_executable", lambda: gui)
    monkeypatch.setattr(installer, "_refresh_linux_desktop_caches", lambda: None)
    fallback_source = tmp_path / "fallback.png"
    fallback_source.write_bytes(b"fallback")
    monkeypatch.setattr(installer, "icon_png_256_path", lambda: fallback_source)

    receipt = installer._install_linux(repo, desktop=False, menu=True)
    desktop_file = home / ".local" / "share" / "applications" / "perfect-prompts.desktop"
    icon_256 = home / ".local" / "share" / "icons" / "hicolor" / "256x256" / "apps" / "perfect-prompts.png"

    assert desktop_file in receipt.paths
    assert icon_256 in receipt.paths
    assert icon_256.read_bytes() == b"png-256"
    assert f"Icon={icon_256}" in desktop_file.read_text(encoding="utf-8")
    for size in (16, 32, 48, 64, 128, 256, 512):
        assert (home / ".local" / "share" / "icons" / "hicolor" / f"{size}x{size}" / "apps" / "perfect-prompts.png").is_file()
