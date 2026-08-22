"""Filesystem adapter for adding and removing library artifacts."""

from __future__ import annotations

import shutil
from pathlib import Path

from perfect_prompts.contracts.dto import (
    AddArtifactReceipt,
    AddArtifactRequest,
    RemoveArtifactReceipt,
    RemoveArtifactRequest,
)


PROTECTED_ROOT_NAMES = frozenset({
    ".git", ".perfect-prompts", ".venv", "Application",
    "README.md", "LICENSE", ".gitmodules", ".gitignore", "install.py", "REPOSITORY_MAP.md",
})


class LocalArtifactStore:
    def __init__(self, root: Path | str):
        self.root = Path(root).expanduser().resolve()

    def add(self, request: AddArtifactRequest) -> AddArtifactReceipt:
        source = request.source.expanduser().resolve()
        if not source.exists():
            raise FileNotFoundError(source)
        relative = _safe_relative(request.destination_directory)
        destination_directory = (self.root / relative).resolve()
        self._require_inside(destination_directory)
        self._require_not_protected(relative)
        destination_directory.mkdir(parents=True, exist_ok=True)
        name = request.target_name.strip() or source.name
        if Path(name).name != name or name in {".", ".."}:
            raise ValueError("Target name must be one filename or directory name")
        destination = destination_directory / name
        self._require_inside(destination.resolve(strict=False))
        if source == destination.resolve(strict=False):
            raise ValueError("Source and destination are the same artifact")
        if destination.exists():
            if not request.replace:
                raise FileExistsError(destination)
            self._remove_path(destination)
        if source.is_dir():
            shutil.copytree(source, destination)
            copied_directory = True
        else:
            shutil.copy2(source, destination)
            copied_directory = False
        return AddArtifactReceipt(source, destination, copied_directory)

    def remove(self, request: RemoveArtifactRequest) -> RemoveArtifactReceipt:
        relative = _safe_relative(request.relative_path)
        if not relative.parts:
            raise ValueError("The repository root cannot be removed")
        self._require_not_protected(relative)
        target = (self.root / relative).resolve(strict=False)
        self._require_inside(target)
        if not target.exists() and not target.is_symlink():
            raise FileNotFoundError(target)
        is_dir = target.is_dir() and not target.is_symlink()
        if is_dir and not request.recursive:
            raise IsADirectoryError("Directory removal requires recursive=True")
        removed_count = _count_nodes(target) if is_dir else 1
        self._remove_path(target)
        return RemoveArtifactReceipt(relative.as_posix(), is_dir, removed_count)

    def _remove_path(self, target: Path) -> None:
        if target.is_dir() and not target.is_symlink():
            shutil.rmtree(target)
        else:
            target.unlink()

    def _require_inside(self, path: Path) -> None:
        if path != self.root and self.root not in path.parents:
            raise ValueError("Path must stay inside the repository")

    @staticmethod
    def _require_not_protected(relative: Path) -> None:
        if relative.parts and relative.parts[0] in PROTECTED_ROOT_NAMES:
            raise PermissionError(f"Protected repository path: {relative.parts[0]}")


def _safe_relative(value: str) -> Path:
    raw = value.strip().replace("\\", "/").strip("/")
    if not raw:
        return Path()
    path = Path(raw)
    if path.is_absolute() or any(part in {"..", "."} for part in path.parts):
        raise ValueError("Path must be repository-relative")
    return path


def _count_nodes(path: Path) -> int:
    if not path.is_dir() or path.is_symlink():
        return 1
    total = 1
    for _ in path.rglob("*"):
        total += 1
    return total
