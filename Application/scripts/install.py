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
    return python, cli, gui


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

    runtime_missing = not (python.is_file() and cli.is_file() and gui.is_file())
    if not args.repair_launcher or runtime_missing:
        python, cli, gui = _install_runtime(
            env_dir=env_dir,
            application_dir=application_dir,
            without_pdf=args.without_pdf,
        )
    else:
        # Editable installs already point at the current Application/src. Repair
        # mode intentionally avoids a dependency reinstall when the stable
        # runtime is intact.
        print(f"Using existing Perfect Prompts runtime: {env_dir}")

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
