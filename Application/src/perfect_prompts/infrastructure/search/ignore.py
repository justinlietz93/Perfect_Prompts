from __future__ import annotations

import fnmatch
from dataclasses import dataclass
from pathlib import Path

DEFAULT_IGNORED_DIRECTORIES = frozenset({
    ".git", ".perfect-prompts", ".venv", "venv", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", "node_modules", "build", "dist",
})
DEFAULT_IGNORED_ROOT_DIRECTORIES = frozenset({"Application"})


@dataclass(frozen=True, slots=True)
class IgnoreRule:
    pattern: str
    negate: bool


class IgnoreMatcher:
    def __init__(self, root: Path, ignore_file: Path | None = None):
        self.root = root.resolve()
        self.rules = self._load(ignore_file)

    def ignored(self, path: Path) -> bool:
        relative = path.relative_to(self.root).as_posix()
        if path.is_dir() and path.name in DEFAULT_IGNORED_DIRECTORIES:
            return True
        if path.is_dir() and path.parent == self.root and path.name in DEFAULT_IGNORED_ROOT_DIRECTORIES:
            return True
        ignored = False
        for rule in self.rules:
            if self._matches(relative, path.is_dir(), rule.pattern):
                ignored = not rule.negate
        return ignored

    @staticmethod
    def _load(path: Path | None) -> tuple[IgnoreRule, ...]:
        if path is None or not path.exists():
            return ()
        rules: list[IgnoreRule] = []
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            negate = line.startswith("!")
            if negate:
                line = line[1:].strip()
            if line:
                rules.append(IgnoreRule(line.replace("\\", "/"), negate))
        return tuple(rules)

    @staticmethod
    def _matches(relative: str, is_dir: bool, pattern: str) -> bool:
        directory_only = pattern.endswith("/")
        pattern = pattern.rstrip("/")
        anchored = pattern.startswith("/")
        pattern = pattern.lstrip("/")
        if directory_only and not is_dir:
            return False
        if anchored:
            return fnmatch.fnmatchcase(relative, pattern) or relative.startswith(pattern + "/")
        if "/" in pattern:
            return fnmatch.fnmatchcase(relative, pattern) or relative.startswith(pattern.rstrip("*") + "/")
        return any(fnmatch.fnmatchcase(part, pattern) for part in relative.split("/"))
