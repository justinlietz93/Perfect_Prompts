"""Perfect Prompts specialization of Beacon's local SQLite FTS5 search engine."""

from __future__ import annotations

import os
import sqlite3
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterator

from perfect_prompts.contracts.dto import IndexReport, SearchHit, SearchRequest
from perfect_prompts.domain.classification import classify_relative_path
from perfect_prompts.infrastructure.search.exporter import SearchResultsExporter
from perfect_prompts.infrastructure.search.extractors import extract_searchable_text
from perfect_prompts.infrastructure.search.ignore import IgnoreMatcher
from perfect_prompts.infrastructure.search.query import fields_match_all_phrases, parse_search_query


class PromptBeaconIndex:
    """Filesystem-authoritative repository search optimized for Perfect Prompts.

    The database is disposable. `rebuild()` recreates the whole projection;
    `sync()` walks current repository metadata and only re-extracts new/changed
    artifacts while removing deleted paths. That makes changes performed either
    in the GUI or directly through the OS filesystem converge on the same index.
    """

    def __init__(self, root: Path | str):
        self.root = Path(root).expanduser().resolve()
        self.state_directory = self.root / ".perfect-prompts"
        self.db_path = self.state_directory / "index.sqlite3"
        self.ignore_file = self.root / ".perfect-promptsignore"
        self.exporter = SearchResultsExporter(self.root)

    def rebuild(self, cancelled: Callable[[], bool] | None = None) -> IndexReport:
        self.state_directory.mkdir(parents=True, exist_ok=True)
        fd, tmp_name = tempfile.mkstemp(prefix="index-", suffix=".sqlite3", dir=self.state_directory)
        os.close(fd)
        temp_path = Path(tmp_name)
        try:
            connection = sqlite3.connect(temp_path, timeout=30)
            try:
                self._create_schema(connection)
                report = self._populate_fresh(connection, cancelled)
                if report.cancelled:
                    return report
                connection.commit()
            finally:
                connection.close()
            os.replace(temp_path, self.db_path)
            return report
        finally:
            temp_path.unlink(missing_ok=True)

    def sync(self, cancelled: Callable[[], bool] | None = None) -> IndexReport:
        if not self.db_path.exists():
            return self.rebuild(cancelled=cancelled)
        matcher = IgnoreMatcher(self.root, self.ignore_file)
        connection = sqlite3.connect(self.db_path, timeout=30)
        connection.row_factory = sqlite3.Row
        try:
            existing = {
                row["path"]: row
                for row in connection.execute(
                    "SELECT id,path,kind,size,mtime_ns,content_indexed FROM nodes"
                ).fetchall()
            }
            seen: set[str] = set()
            added = updated = removed = errors = 0
            for path in self._walk(matcher):
                if cancelled and cancelled():
                    connection.rollback()
                    return self._report_from_db(connection, errors=errors, cancelled=True, added=added, updated=updated, removed=removed)
                relative = path.relative_to(self.root).as_posix()
                seen.add(relative)
                try:
                    stat = path.stat(follow_symlinks=False)
                except OSError:
                    errors += 1
                    continue
                kind = "symlink" if path.is_symlink() else ("file" if path.is_file() else "directory")
                size = stat.st_size if path.is_file() else 0
                prior = existing.get(relative)
                if prior is not None and prior["kind"] == kind and prior["size"] == size and prior["mtime_ns"] == stat.st_mtime_ns:
                    continue
                body, content_indexed, extraction_error = self._extract(path)
                errors += extraction_error
                classification = classify_relative_path(relative)
                if prior is None:
                    cursor = connection.execute(
                        """
                        INSERT INTO nodes(path,name,area,artifact_type,runtime,source_scope,kind,extension,size,mtime_ns,content_indexed)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)
                        """,
                        (
                            relative, path.name, classification.area, classification.artifact_type,
                            classification.runtime, classification.source_scope, kind,
                            path.suffix.casefold() if path.is_file() else "", size, stat.st_mtime_ns, content_indexed,
                        ),
                    )
                    node_id = int(cursor.lastrowid)
                    added += 1
                else:
                    node_id = int(prior["id"])
                    connection.execute(
                        """
                        UPDATE nodes SET name=?,area=?,artifact_type=?,runtime=?,source_scope=?,kind=?,extension=?,size=?,mtime_ns=?,content_indexed=?
                        WHERE id=?
                        """,
                        (
                            path.name, classification.area, classification.artifact_type, classification.runtime,
                            classification.source_scope, kind, path.suffix.casefold() if path.is_file() else "",
                            size, stat.st_mtime_ns, content_indexed, node_id,
                        ),
                    )
                    connection.execute("DELETE FROM search WHERE rowid=?", (node_id,))
                    updated += 1
                connection.execute(
                    "INSERT INTO search(rowid,path,name,area,artifact_type,runtime,body) VALUES (?,?,?,?,?,?,?)",
                    (node_id, relative, path.name, classification.area, classification.artifact_type, classification.runtime, body),
                )

            missing = set(existing) - seen
            for relative in missing:
                node_id = int(existing[relative]["id"])
                connection.execute("DELETE FROM search WHERE rowid=?", (node_id,))
                connection.execute("DELETE FROM nodes WHERE id=?", (node_id,))
                removed += 1

            self._update_metadata(connection, errors_delta=errors)
            connection.commit()
            return self._report_from_db(connection, errors=errors, cancelled=False, added=added, updated=updated, removed=removed)
        finally:
            connection.close()

    def search(self, request: SearchRequest) -> tuple[SearchHit, ...]:
        parsed = parse_search_query(request.query)
        if not parsed.fts_expression or not self.db_path.exists():
            return ()
        connection = sqlite3.connect(self.db_path, timeout=15)
        connection.row_factory = sqlite3.Row
        try:
            clauses = ["search MATCH ?"]
            params: list[object] = [parsed.fts_expression]
            if parsed.quoted_phrases:
                connection.create_function(
                    "prompt_beacon_phrases_match", 3,
                    lambda path, name, body: int(fields_match_all_phrases(parsed.quoted_phrases, path, name, body)),
                    deterministic=True,
                )
                clauses.append("prompt_beacon_phrases_match(search.path,search.name,search.body)=1")
            for column, value in (
                ("area", request.area), ("artifact_type", request.artifact_type),
                ("runtime", request.runtime), ("source_scope", request.source_scope),
            ):
                if value:
                    clauses.append(f"n.{column} = ?")
                    params.append(value)
            if request.path_prefix:
                clauses.append("n.path LIKE ?")
                prefix = request.path_prefix.strip().replace("\\", "/").strip("/")
                params.append(prefix + "%")
            params.append(max(1, min(int(request.limit), 500)))
            rows = connection.execute(
                f"""
                SELECT n.path,n.name,n.area,n.artifact_type,n.runtime,n.source_scope,n.kind,n.extension,n.content_indexed,
                       snippet(search,5,'<mark>','</mark>',' … ',36) AS snippet,
                       bm25(search,3.5,5.0,1.2,2.0,1.2,1.0) AS rank
                FROM search JOIN nodes n ON n.id=search.rowid
                WHERE {' AND '.join(clauses)}
                ORDER BY rank, n.path
                LIMIT ?
                """, params,
            ).fetchall()
        finally:
            connection.close()
        return tuple(SearchHit(
            path=row["path"], name=row["name"], area=row["area"], artifact_type=row["artifact_type"],
            runtime=row["runtime"], source_scope=row["source_scope"], kind=row["kind"], extension=row["extension"],
            content_indexed=bool(row["content_indexed"]), snippet=row["snippet"] or row["path"], rank=float(row["rank"]),
        ) for row in rows)

    def export_query(self, request: SearchRequest, hits: tuple[SearchHit, ...]) -> str:
        captured = self.exporter.capture(request, hits)
        return str(self.exporter.write(captured))

    def read_content(self, relative_path: str) -> str:
        absolute = (self.root / relative_path).resolve()
        if absolute != self.root and self.root not in absolute.parents:
            raise ValueError("Path escapes the selected repository root")
        if not absolute.is_file():
            return ""
        return extract_searchable_text(absolute)

    def status(self) -> dict[str, object]:
        if not self.db_path.exists():
            return {"exists": False, "database_path": str(self.db_path), "root": str(self.root)}
        connection = sqlite3.connect(self.db_path, timeout=15)
        try:
            metadata = dict(connection.execute("SELECT key,value FROM metadata").fetchall())
            area_counts = dict(connection.execute("SELECT area,COUNT(*) FROM nodes GROUP BY area ORDER BY area").fetchall())
            type_counts = dict(connection.execute("SELECT artifact_type,COUNT(*) FROM nodes GROUP BY artifact_type ORDER BY artifact_type").fetchall())
        finally:
            connection.close()
        return {
            "exists": True, "database_path": str(self.db_path), "database_size_bytes": self.db_path.stat().st_size,
            "area_counts": area_counts, "type_counts": type_counts, **metadata,
        }

    def _populate_fresh(self, connection: sqlite3.Connection, cancelled: Callable[[], bool] | None) -> IndexReport:
        matcher = IgnoreMatcher(self.root, self.ignore_file)
        indexed_files = skipped_files = errors = nodes = 0
        for path in self._walk(matcher):
            if cancelled and cancelled():
                connection.rollback()
                return IndexReport(nodes, indexed_files, skipped_files, errors, True, added=nodes)
            relative = path.relative_to(self.root).as_posix()
            try:
                stat = path.stat(follow_symlinks=False)
            except OSError:
                errors += 1
                continue
            body, content_indexed, extraction_error = self._extract(path)
            errors += extraction_error
            if path.is_file() and not path.is_symlink():
                if content_indexed:
                    indexed_files += 1
                else:
                    skipped_files += 1
            classification = classify_relative_path(relative)
            kind = "symlink" if path.is_symlink() else ("file" if path.is_file() else "directory")
            cursor = connection.execute(
                """
                INSERT INTO nodes(path,name,area,artifact_type,runtime,source_scope,kind,extension,size,mtime_ns,content_indexed)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    relative, path.name, classification.area, classification.artifact_type,
                    classification.runtime, classification.source_scope, kind,
                    path.suffix.casefold() if path.is_file() else "",
                    stat.st_size if path.is_file() else 0, stat.st_mtime_ns, content_indexed,
                ),
            )
            node_id = int(cursor.lastrowid)
            connection.execute(
                "INSERT INTO search(rowid,path,name,area,artifact_type,runtime,body) VALUES (?,?,?,?,?,?,?)",
                (node_id, relative, path.name, classification.area, classification.artifact_type, classification.runtime, body),
            )
            nodes += 1
        self._update_metadata(connection, absolute_errors=errors)
        return IndexReport(nodes, indexed_files, skipped_files, errors, False, added=nodes)

    @staticmethod
    def _extract(path: Path) -> tuple[str, int, int]:
        if not path.is_file() or path.is_symlink():
            return "", 0, 0
        try:
            body = extract_searchable_text(path)
            return body, int(bool(body)), 0
        except Exception:
            return "", 0, 1

    def _walk(self, matcher: IgnoreMatcher) -> Iterator[Path]:
        stack = [self.root]
        while stack:
            directory = stack.pop()
            try:
                entries = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.casefold()))
            except OSError:
                continue
            children: list[Path] = []
            for entry in entries:
                if matcher.ignored(entry):
                    continue
                yield entry
                if entry.is_dir() and not entry.is_symlink():
                    children.append(entry)
            stack.extend(reversed(children))

    def _update_metadata(self, connection: sqlite3.Connection, *, absolute_errors: int | None = None, errors_delta: int = 0) -> None:
        nodes = int(connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0])
        indexed = int(connection.execute("SELECT COUNT(*) FROM nodes WHERE kind='file' AND content_indexed=1").fetchone()[0])
        skipped = int(connection.execute("SELECT COUNT(*) FROM nodes WHERE kind='file' AND content_indexed=0").fetchone()[0])
        if absolute_errors is None:
            prior = connection.execute("SELECT value FROM metadata WHERE key='error_count'").fetchone()
            total_errors = int(prior[0]) + errors_delta if prior else errors_delta
        else:
            total_errors = absolute_errors
        prior_built = connection.execute("SELECT value FROM metadata WHERE key='built_at'").fetchone()
        now = _utc_now()
        metadata = {
            "root": str(self.root), "built_at": prior_built[0] if prior_built else now, "synced_at": now,
            "node_count": str(nodes), "indexed_file_count": str(indexed), "skipped_file_count": str(skipped),
            "error_count": str(total_errors),
        }
        connection.executemany("INSERT OR REPLACE INTO metadata(key,value) VALUES (?,?)", metadata.items())

    @staticmethod
    def _report_from_db(
        connection: sqlite3.Connection, *, errors: int, cancelled: bool,
        added: int, updated: int, removed: int,
    ) -> IndexReport:
        nodes = int(connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0])
        indexed = int(connection.execute("SELECT COUNT(*) FROM nodes WHERE kind='file' AND content_indexed=1").fetchone()[0])
        skipped = int(connection.execute("SELECT COUNT(*) FROM nodes WHERE kind='file' AND content_indexed=0").fetchone()[0])
        return IndexReport(nodes, indexed, skipped, errors, cancelled, added=added, updated=updated, removed=removed)

    @staticmethod
    def _create_schema(connection: sqlite3.Connection) -> None:
        try:
            connection.executescript("""
                PRAGMA journal_mode=WAL;
                DROP TABLE IF EXISTS metadata;
                DROP TABLE IF EXISTS nodes;
                DROP TABLE IF EXISTS search;
                CREATE TABLE metadata(key TEXT PRIMARY KEY,value TEXT NOT NULL);
                CREATE TABLE nodes(
                    id INTEGER PRIMARY KEY,
                    path TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    area TEXT NOT NULL,
                    artifact_type TEXT NOT NULL,
                    runtime TEXT NOT NULL,
                    source_scope TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    extension TEXT NOT NULL,
                    size INTEGER NOT NULL,
                    mtime_ns INTEGER NOT NULL,
                    content_indexed INTEGER NOT NULL
                );
                CREATE VIRTUAL TABLE search USING fts5(
                    path,name,area,artifact_type,runtime,body,tokenize='porter unicode61'
                );
            """)
        except sqlite3.OperationalError as error:
            if "fts5" in str(error).casefold():
                raise RuntimeError("Perfect Prompts requires Python SQLite with FTS5 enabled.") from error
            raise


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
