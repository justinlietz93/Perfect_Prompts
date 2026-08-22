"""Native Linux/Windows launcher installation using the packaged Perfect Prompts icon."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from perfect_prompts.infrastructure.settings.user_settings import UserSettingsStore
from perfect_prompts.resources import icon_ico_path, icon_png_256_path

APP_ID = "perfect-prompts"


@dataclass(frozen=True, slots=True)
class LauncherReceipt:
    paths: tuple[Path, ...]


def install_launchers(root: Path, *, desktop: bool = True, menu: bool = True) -> LauncherReceipt:
    root = root.expanduser().resolve()
    UserSettingsStore().save_last_root(root)
    if os.name == "nt":
        return _install_windows(root, desktop=desktop, menu=menu)
    return _install_linux(root, desktop=desktop, menu=menu)


def _gui_executable() -> Path:
    # Console-script entry points live beside the command that invoked this
    # installer, which is more reliable than resolving sys.executable through
    # virtual-environment symlinks.
    invoked = Path(sys.argv[0]).expanduser()
    invoked_directory = invoked.parent if invoked.parent != Path("") else Path.cwd()
    candidates = [
        invoked_directory / "perfect-prompts.exe",
        invoked_directory / "perfect-prompts",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate.absolute()
    located = shutil.which("perfect-prompts")
    if located:
        return Path(located).absolute()
    executable_directory = Path(sys.executable).parent
    for name in ("perfect-prompts.exe", "perfect-prompts"):
        candidate = executable_directory / name
        if candidate.is_file():
            return candidate.absolute()
    raise FileNotFoundError("Could not locate the installed perfect-prompts launcher")


def _desktop_directory() -> Path:
    """Resolve the user's real desktop directory without assuming ~/Desktop."""
    command = shutil.which("xdg-user-dir")
    if command:
        try:
            value = subprocess.check_output(
                [command, "DESKTOP"], text=True, stderr=subprocess.DEVNULL
            ).strip()
            if value:
                return Path(value).expanduser()
        except (OSError, subprocess.SubprocessError):
            pass
    return Path.home() / "Desktop"


def _install_hicolor_icons(root: Path) -> tuple[Path, ...]:
    """Install every packaged Linux raster size, with a 256 px fallback."""
    user_hicolor = Path.home() / ".local" / "share" / "icons" / "hicolor"
    source_hicolor = root / "Application" / "assets" / "icons" / "hicolor"
    installed: list[Path] = []

    if source_hicolor.is_dir():
        for source in sorted(source_hicolor.glob("*x*/apps/perfect-prompts.png")):
            relative = source.relative_to(source_hicolor)
            target = user_hicolor / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            installed.append(target)

    # Keep installation functional for pip/package-only scenarios where the
    # repository's generated hicolor tree is unavailable.
    fallback = user_hicolor / "256x256" / "apps" / "perfect-prompts.png"
    if fallback not in installed:
        fallback.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(icon_png_256_path(), fallback)
        installed.append(fallback)

    return tuple(installed)


def _desktop_entry(*, target: Path, root: Path, icon: Path) -> str:
    # Absolute Icon= is deliberate. Several Linux desktops continue to show a
    # generic gear until their icon-theme cache catches up; the absolute path
    # makes the launcher correct immediately while the hicolor copies preserve
    # normal theme integration.
    return "\n".join(
        [
            "[Desktop Entry]",
            "Version=1.0",
            "Type=Application",
            "Name=Perfect Prompts",
            "Comment=Prompt and Context Engineering Library",
            f'TryExec={target}',
            f'Exec="{target}" --root "{root}"',
            f"Path={root}",
            f"Icon={icon}",
            "Terminal=false",
            "Categories=Development;Utility;",
            "StartupNotify=true",
            f"StartupWMClass={APP_ID}",
            "",
        ]
    )


def _refresh_linux_desktop_caches() -> None:
    applications = Path.home() / ".local" / "share" / "applications"
    hicolor = Path.home() / ".local" / "share" / "icons" / "hicolor"

    update_desktop = shutil.which("update-desktop-database")
    if update_desktop and applications.is_dir():
        subprocess.run(
            [update_desktop, str(applications)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    update_icons = shutil.which("gtk-update-icon-cache")
    if update_icons and hicolor.is_dir():
        subprocess.run(
            [update_icons, "-f", "-t", str(hicolor)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def _install_linux(root: Path, *, desktop: bool, menu: bool) -> LauncherReceipt:
    target = _gui_executable()
    created: list[Path] = list(_install_hicolor_icons(root))
    icon_target = Path.home() / ".local" / "share" / "icons" / "hicolor" / "256x256" / "apps" / "perfect-prompts.png"
    content = _desktop_entry(target=target, root=root, icon=icon_target)

    if menu:
        path = Path.home() / ".local" / "share" / "applications" / "perfect-prompts.desktop"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        path.chmod(0o755)
        created.append(path)

    if desktop:
        desktop_dir = _desktop_directory()
        desktop_dir.mkdir(parents=True, exist_ok=True)
        path = desktop_dir / "Perfect Prompts.desktop"
        path.write_text(content, encoding="utf-8")
        path.chmod(0o755)
        created.append(path)

    _refresh_linux_desktop_caches()
    return LauncherReceipt(tuple(created))


def _install_windows(root: Path, *, desktop: bool, menu: bool) -> LauncherReceipt:
    target = _gui_executable()
    icon = icon_ico_path()
    created: list[Path] = []
    destinations: list[Path] = []
    if menu:
        appdata = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
        destinations.append(appdata / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Perfect Prompts.lnk")
    if desktop:
        destinations.append(Path.home() / "Desktop" / "Perfect Prompts.lnk")
    for destination in destinations:
        destination.parent.mkdir(parents=True, exist_ok=True)
        script = (
            "$w=New-Object -ComObject WScript.Shell;"
            f"$s=$w.CreateShortcut('{_ps(destination)}');"
            f"$s.TargetPath='{_ps(target)}';$s.Arguments='--root \"{_ps(root)}\"';$s.WorkingDirectory='{_ps(root)}';"
            f"$s.IconLocation='{_ps(icon)}';$s.Description='Prompt and Context Engineering Library';$s.Save()"
        )
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script], check=True)
        created.append(destination)
    return LauncherReceipt(tuple(created))


def _ps(path: Path) -> str:
    return str(path).replace("'", "''")
