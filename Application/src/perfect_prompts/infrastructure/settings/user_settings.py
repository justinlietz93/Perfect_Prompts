"""User-local app settings; repository artifacts remain ordinary files."""

from __future__ import annotations

import json
import os
from pathlib import Path


class UserSettingsStore:
    def __init__(self, path: Path | None = None):
        self.path = path or (_config_home() / "perfect-prompts" / "settings.json")

    def load_last_root(self) -> Path | None:
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            candidate = Path(data.get("last_root", "")).expanduser()
            return candidate.resolve() if candidate.is_dir() else None
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            return None

    def save_last_root(self, root: Path) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"last_root": str(root.resolve())}, indent=2), encoding="utf-8")


def _config_home() -> Path:
    if os.name == "nt":
        return Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    return Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
