"""Portable JSON exports for single and batched Prompt Beacon queries."""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from perfect_prompts.contracts.dto import SearchHit, SearchRequest


class SearchResultsExporter:
    def __init__(self, root: Path):
        self.root = root
        self.export_directory = root / ".perfect-prompts" / "search-exports"

    def capture(
        self,
        request: SearchRequest,
        hits: tuple[SearchHit, ...],
        *,
        search_duration_ms: float | None = None,
        batch: dict[str, object] | None = None,
    ) -> dict[str, object]:
        return {
            "schema": "perfect-prompts.prompt-beacon.query.v1",
            "captured_at": _utc_now(),
            "root": str(self.root),
            "query": {
                "text": request.query,
                "area": request.area,
                "artifact_type": request.artifact_type,
                "runtime": request.runtime,
                "source_scope": request.source_scope,
                "path_prefix": request.path_prefix,
                "limit": request.limit,
                "returned_count": len(hits),
                "search_duration_ms": round(search_duration_ms, 3) if search_duration_ms is not None else None,
            },
            "batch": batch,
            "ranked_matches": [asdict(hit) | {"position": index} for index, hit in enumerate(hits, start=1)],
        }

    def write(self, captured: dict[str, object], destination: Path | None = None) -> Path:
        self.export_directory.mkdir(parents=True, exist_ok=True)
        target = destination or self.export_directory / f"query_{_identifier()}.json"
        if not target.is_absolute():
            target = self.root / target
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(captured, indent=2, ensure_ascii=False), encoding="utf-8")
        return target

    def timed_capture(self, index, request: SearchRequest) -> tuple[tuple[SearchHit, ...], dict[str, object]]:
        started = time.perf_counter()
        hits = index.search(request)
        elapsed = (time.perf_counter() - started) * 1000
        return hits, self.capture(request, hits, search_duration_ms=elapsed)


def _identifier() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    return f"{stamp}_{uuid.uuid4().hex[:10]}"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
