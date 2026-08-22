"""Small capability interfaces between the application and adapters."""

from __future__ import annotations

from collections.abc import Callable
from typing import Protocol

from perfect_prompts.contracts.dto import (
    AddArtifactReceipt,
    AddArtifactRequest,
    IndexReport,
    RemoveArtifactReceipt,
    RemoveArtifactRequest,
    SearchHit,
    SearchRequest,
)


class SearchIndexPort(Protocol):
    def search(self, request: SearchRequest) -> tuple[SearchHit, ...]: ...
    def rebuild(self, cancelled: Callable[[], bool] | None = None) -> IndexReport: ...
    def sync(self, cancelled: Callable[[], bool] | None = None) -> IndexReport: ...
    def read_content(self, relative_path: str) -> str: ...
    def status(self) -> dict[str, object]: ...
    def export_query(self, request: SearchRequest, hits: tuple[SearchHit, ...]) -> str: ...


class ArtifactStorePort(Protocol):
    def add(self, request: AddArtifactRequest) -> AddArtifactReceipt: ...
    def remove(self, request: RemoveArtifactRequest) -> RemoveArtifactReceipt: ...


class SearchLibraryInputPort(Protocol):
    def execute(self, request: SearchRequest) -> tuple[SearchHit, ...]: ...


class CancellationTokenPort(Protocol):
    @property
    def is_cancelled(self) -> bool: ...


class TaskHandlePort(Protocol):
    @property
    def is_done(self) -> bool: ...
    def cancel(self) -> None: ...


class TaskRunnerPort(Protocol):
    def submit(
        self,
        work: Callable[[CancellationTokenPort], object],
        done: Callable[[object | None, BaseException | None], None],
    ) -> TaskHandlePort: ...
    def shutdown(self, wait: bool = True) -> None: ...
