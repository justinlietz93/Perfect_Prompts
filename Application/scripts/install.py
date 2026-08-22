"""One-command local installation for the Perfect Prompts desktop application."""

from __future__ import annotations

import argparse
import os
import subprocess
import venv
from pathlib import Path


def _user_data_home() -> Path:
    """Return a stable per-user data directory for application runtime state."""
    if os.name == "nt":
        return Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))


def _default_venv_dir() -> Path:
    # The runtime deliberately lives outside Application/. Replacing or updating
    # the tracked Application directory must never delete the installed launcher
    # target again.
    if os.name == "nt":
        return _user_data_home() / "PerfectPrompts" / "runtime" / "venv"
    return _user_data_home() / "perfect-prompts" / "runtime" / "venv"


def _entry_points(env_dir: Path) -> tuple[Path, Path, Path]:
    if os.name == "nt":
        scripts = env_dir / "Scripts"
        return (
            scripts / "python.exe",
            scripts / "perfect-prompts-cli.exe",
            scripts / "perfect-prompts.exe",
        )
    scripts = env_dir / "bin"
    return scripts / "python", scripts / "perfect-prompts-cli", scripts / "perfect-prompts"


def _resolve_env_dir(application_dir: Path, requested: Path | None) -> Path:
    if requested is None:
        return _default_venv_dir().expanduser().resolve()
    requested = requested.expanduser()
    return requested.resolve() if requested.is_absolute() else (application_dir / requested).resolve()


def _install_runtime(*, env_dir: Path, application_dir: Path, without_pdf: bool) -> tuple[Path, Path, Path]:
    if not env_dir.exists():
        print(f"Creating Perfect Prompts runtime: {env_dir}")
        env_dir.parent.mkdir(parents=True, exist_ok=True)
        venv.EnvBuilder(with_pip=True).create(env_dir)
    python, cli, gui = _entry_points(env_dir)
    extras = "gui" if without_pdf else "gui,pdf"
    print("Installing/updating Perfect Prompts desktop runtime…")
    subprocess.run(
        [str(python), "-m", "pip", "install", "-e", f"{application_dir}[{extras}]"],
        check=True,
    )
    if not cli.is_file() or not gui.is_file():
        raise SystemExit(
            "Perfect Prompts installation completed but launcher entry points were not created. "
            f"Expected {cli} and {gui}."
        )
    _validate_runtime(python=python, application_dir=application_dir)
    return python, cli, gui


def _validate_runtime(*, python: Path, application_dir: Path) -> None:
    """Verify that the runtime imports this checkout and can load the GUI stack."""
    check = (
        "from pathlib import Path; "
        "import perfect_prompts, PySide6; "
        "from perfect_prompts.presentation.qt.main_window import MainWindow; "
        "print(Path(perfect_prompts.__file__).resolve())"
    )
    result = subprocess.run(
        [str(python), "-c", check],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    imported = Path(result.stdout.strip()).resolve()
    expected = (application_dir / "src" / "perfect_prompts" / "__init__.py").resolve()
    if imported != expected:
        raise SystemExit(
            "Perfect Prompts runtime is still bound to a different checkout after installation. "
            f"Expected {expected}, imported {imported}."
        )

    # Import success is not enough for a desktop application. Verify that Qt can
    # initialize its real platform plugin in the environment running the repair.
    # This catches xcb/Wayland/plugin failures before we declare the launcher fixed.
    smoke_env = os.environ.copy()
    if os.name != "nt" and not (smoke_env.get("DISPLAY") or smoke_env.get("WAYLAND_DISPLAY")):
        smoke_env["QT_QPA_PLATFORM"] = "offscreen"
    smoke = subprocess.run(
        [str(python), "-m", "perfect_prompts.main", "--smoke-test"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=smoke_env,
    )
    if smoke.returncode != 0:
        detail = (smoke.stderr or smoke.stdout).strip()
        raise SystemExit(
            "Perfect Prompts runtime imports correctly, but Qt cannot initialize the desktop runtime.\n"
            + (detail or f"Qt smoke test exited with code {smoke.returncode}.")
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--venv",
        type=Path,
        default=None,
        help=(
            "Override the runtime virtual environment. By default Perfect Prompts uses a stable "
            "per-user runtime outside the repository so Application/ updates cannot remove it."
        ),
    )
    parser.add_argument("--no-desktop", action="store_true")
    parser.add_argument("--no-menu", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    parser.add_argument("--without-pdf", action="store_true")
    parser.add_argument(
        "--repair-launcher",
        action="store_true",
        help=(
            "Repair the installed runtime and native launcher. If an older Application/.venv was "
            "removed during an update, repair mode recreates a stable user-local runtime automatically."
        ),
    )
    args = parser.parse_args()

    application_dir = Path(__file__).resolve().parents[1]
    repository_root = application_dir.parent
    env_dir = _resolve_env_dir(application_dir, args.venv)
    python, cli, gui = _entry_points(env_dir)

    # Always refresh the editable installation, including repair mode. A stable
    # runtime can legitimately exist while still pointing at an older checkout.
    # Skipping this step produced a launcher that targeted a valid executable
    # whose package import path was stale or missing.
    python, cli, gui = _install_runtime(
        env_dir=env_dir,
        application_dir=application_dir,
        without_pdf=args.without_pdf,
    )

    if not args.repair_launcher and not args.skip_index:
        print("Building initial Prompt Beacon index…")
        subprocess.run([str(cli), "index", "--root", str(repository_root)], check=True)

    launcher = [str(cli), "install-launcher", "--root", str(repository_root)]
    if args.no_desktop:
        launcher.append("--no-desktop")
    if args.no_menu:
        launcher.append("--no-menu")
    print("Installing native launcher(s)…")
    subprocess.run(launcher, check=True)

    print(f"Runtime: {env_dir}")
    print("Perfect Prompts launcher repaired." if args.repair_launcher else "Perfect Prompts is installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
