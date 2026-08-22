"""Stable request/result shapes shared across application boundaries."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class SearchRequest:
    query: str
    area: str | None = None
    artifact_type: str | None = None
    runtime: str | None = None
    source_scope: str | None = None
    path_prefix: str | None = None
    limit: int = 100


@dataclass(frozen=True, slots=True)
class SearchHit:
    path: str
    name: str
    area: str
    artifact_type: str
    runtime: str
    source_scope: str
    kind: str
    extension: str
    content_indexed: bool
    snippet: str
    rank: float


@dataclass(frozen=True, slots=True)
class BatchQueryResult:
    query: str
    hits: tuple[SearchHit, ...]
    export_path: str = ""
    error: str = ""


@dataclass(frozen=True, slots=True)
class IndexReport:
    nodes: int
    indexed_files: int
    skipped_files: int
    errors: int
    cancelled: bool
    added: int = 0
    updated: int = 0
    removed: int = 0


@dataclass(frozen=True, slots=True)
class AddArtifactRequest:
    source: Path
    destination_directory: str
    target_name: str = ""
    replace: bool = False


@dataclass(frozen=True, slots=True)
class AddArtifactReceipt:
    source: Path
    destination: Path
    copied_directory: bool


@dataclass(frozen=True, slots=True)
class RemoveArtifactRequest:
    relative_path: str
    recursive: bool = False


@dataclass(frozen=True, slots=True)
class RemoveArtifactReceipt:
    relative_path: str
    removed_directory: bool
    removed_count: int
