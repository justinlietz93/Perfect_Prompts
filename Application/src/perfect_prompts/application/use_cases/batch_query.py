"""Batch queries preserving Beacon's quote-aware split and per-query exports."""

from __future__ import annotations

import time
import uuid
from datetime import datetime, timezone

from perfect_prompts.contracts.dto import BatchQueryResult, SearchRequest
from perfect_prompts.contracts.ports import SearchIndexPort
from perfect_prompts.infrastructure.search.exporter import SearchResultsExporter


class BatchQuery:
    def __init__(self, index: SearchIndexPort, root):
        self._index = index
        self._exporter = SearchResultsExporter(root)

    def execute(self, text: str, *, limit: int = 40) -> tuple[BatchQueryResult, ...]:
        queries = split_batch_queries(text)
        batch_id = f"bq_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')}_{uuid.uuid4().hex[:10]}"
        results: list[BatchQueryResult] = []
        for position, query in enumerate(queries, start=1):
            request = SearchRequest(query=query, limit=limit)
            try:
                started = time.perf_counter()
                hits = self._index.search(request)
                elapsed = (time.perf_counter() - started) * 1000
                captured = self._exporter.capture(
                    request, hits, search_duration_ms=elapsed,
                    batch={"batch_execution_id": batch_id, "position": position, "query_count": len(queries)},
                )
                path = self._exporter.write(captured)
                results.append(BatchQueryResult(query=query, hits=hits, export_path=str(path)))
            except Exception as error:
                results.append(BatchQueryResult(query=query, hits=(), error=str(error)))
        return tuple(results)


def split_batch_queries(text: str) -> list[str]:
    queries: list[str] = []
    current: list[str] = []
    inside_quotes = False
    comma_separated = "\n" not in text and "\r" not in text

    def finish() -> None:
        query = "".join(current).strip()
        current.clear()
        if query:
            queries.append(query)

    for character in text:
        if character == '"':
            inside_quotes = not inside_quotes
            current.append(character)
        elif (character in {"\n", "\r"} or (character == "," and comma_separated)) and not inside_quotes:
            finish()
        else:
            current.append(character)
    if inside_quotes:
        raise ValueError("A quoted phrase is missing its closing double quote.")
    finish()
    return queries
