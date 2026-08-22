"""Composition root: concrete Perfect Prompts application wiring lives here."""

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
from perfect_prompts.infrastructure.execution.task_runner import ThreadPoolTaskRunner
from perfect_prompts.infrastructure.filesystem.artifact_store import LocalArtifactStore
from perfect_prompts.infrastructure.search.prompt_beacon import PromptBeaconIndex
from perfect_prompts.presentation.controllers.library_controller import LibraryController


def build_container(root: Path, dispatch: Callable[[Callable[[], None]], None]) -> LibraryController:
    index = PromptBeaconIndex(root)
    store = LocalArtifactStore(root)
    return LibraryController(
        root=root,
        search=SearchLibrary(index),
        rebuild=RebuildIndex(index),
        sync=SyncIndex(index),
        batch=BatchQuery(index, root),
        add=AddArtifact(store),
        remove=RemoveArtifact(store),
        preview=PreviewArtifact(index),
        status=GetIndexStatus(index),
        export=ExportQuery(index),
        runner=ThreadPoolTaskRunner(max_workers=2),
        dispatch=dispatch,
    )
