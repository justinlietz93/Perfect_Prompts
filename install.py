"""Install the optional Perfect Prompts desktop application."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).resolve().parent / "Application" / "scripts" / "install.py"), run_name="__main__")
