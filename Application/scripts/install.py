"""One-command local installation for the Perfect Prompts desktop application."""

from __future__ import annotations

import argparse
import os
import subprocess
import venv
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--venv", type=Path, default=Path(".venv"))
    parser.add_argument("--no-desktop", action="store_true")
    parser.add_argument("--no-menu", action="store_true")
    parser.add_argument("--skip-index", action="store_true")
    parser.add_argument("--without-pdf", action="store_true")
    args = parser.parse_args()

    application_dir = Path(__file__).resolve().parents[1]
    repository_root = application_dir.parent
    env_dir = (application_dir / args.venv).resolve() if not args.venv.is_absolute() else args.venv.resolve()
    if not env_dir.exists():
        print(f"Creating virtual environment: {env_dir}")
        venv.EnvBuilder(with_pip=True).create(env_dir)
    if os.name == "nt":
        python = env_dir / "Scripts" / "python.exe"
        cli = env_dir / "Scripts" / "perfect-prompts-cli.exe"
    else:
        python = env_dir / "bin" / "python"
        cli = env_dir / "bin" / "perfect-prompts-cli"
    extras = "gui" if args.without_pdf else "gui,pdf"
    print("Installing Perfect Prompts and GUI dependencies…")
    subprocess.run([str(python), "-m", "pip", "install", "-e", f"{application_dir}[{extras}]"], check=True)
    if not args.skip_index:
        print("Building initial Prompt Beacon index…")
        subprocess.run([str(cli), "index", "--root", str(repository_root)], check=True)
    launcher = [str(cli), "install-launcher", "--root", str(repository_root)]
    if args.no_desktop:
        launcher.append("--no-desktop")
    if args.no_menu:
        launcher.append("--no-menu")
    print("Installing native launcher(s)…")
    subprocess.run(launcher, check=True)
    print("Perfect Prompts is installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
