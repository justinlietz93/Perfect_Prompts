"""Thin GUI controller translating gestures into application operations."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from perfect_prompts.application.use_cases.add_artifact import AddArtifact
from perfect_prompts.application.use_cases.batch_query import BatchQuery
from perfect_prompts.application.use_cases.export_query import ExportQuery
from perfect_prompts.application.use_cases.get_index_status import GetIndexStatus
from perfect_prompts.application.use_cases.preview_artifact import PreviewArtifact
from perfect_prompts.application.use_cases.rebuild_index import RebuildIndex
from perfect_prompts.application.use_cases.remove_artifact import RemoveArtifact
from perfect_prompts.application.use_cases.search_library import SearchLibrary
from perfect_prompts.application.use_cases.sync_index import SyncIndex
from perfect_prompts.contracts.dto import (
    AddArtifactReceipt,
    AddArtifactRequest,
    BatchQueryResult,
    IndexReport,
    RemoveArtifactReceipt,
    RemoveArtifactRequest,
    SearchHit,
    SearchRequest,
)
from perfect_prompts.contracts.ports import TaskRunnerPort


class LibraryController:
    def __init__(
        self,
        root: Path,
        search: SearchLibrary,
        rebuild: RebuildIndex,
        sync: SyncIndex,
        batch: BatchQuery,
        add: AddArtifact,
        remove: RemoveArtifact,
        preview: PreviewArtifact,
        status: GetIndexStatus,
        export: ExportQuery,
        runner: TaskRunnerPort,
        dispatch: Callable[[Callable[[], None]], None],
    ) -> None:
        self.root = root
        self._search = search
        self._rebuild = rebuild
        self._sync = sync
        self._batch = batch
        self._add = add
        self._remove = remove
        self._preview = preview
        self._status = status
        self._export = export
        self._runner = runner
        self._dispatch = dispatch
        self._index_handle = None

    def search(self, request: SearchRequest) -> tuple[SearchHit, ...]:
        return self._search.execute(request)

    def preview(self, relative_path: str) -> str:
        return self._preview.execute(relative_path)

    def status(self) -> dict[str, object]:
        return self._status.execute()

    def add_artifact(self, request: AddArtifactRequest) -> AddArtifactReceipt:
        return self._add.execute(request)

    def remove_artifact(self, request: RemoveArtifactRequest) -> RemoveArtifactReceipt:
        return self._remove.execute(request)

    def export_query(self, request: SearchRequest, hits: tuple[SearchHit, ...]) -> str:
        return self._export.execute(request, hits)

    def rebuild_index(self, callback: Callable[[IndexReport | None, BaseException | None], None]) -> None:
        self._run_index_work(lambda token: self._rebuild.execute(cancelled=lambda: token.is_cancelled), callback)

    def sync_index(self, callback: Callable[[IndexReport | None, BaseException | None], None]) -> None:
        self._run_index_work(lambda token: self._sync.execute(cancelled=lambda: token.is_cancelled), callback)

    def _run_index_work(self, work, callback) -> None:
        if self._index_handle is not None and not self._index_handle.is_done:
            return
        self._index_handle = self._runner.submit(
            work,
            lambda result, error: self._dispatch(lambda: callback(result, error)),
        )

    def run_batch(
        self,
        text: str,
        callback: Callable[[tuple[BatchQueryResult, ...] | None, BaseException | None], None],
    ) -> None:
        self._runner.submit(
            lambda token: self._batch.execute(text),
            lambda result, error: self._dispatch(lambda: callback(result, error)),
        )

    def close(self) -> None:
        self._runner.shutdown(wait=True)
