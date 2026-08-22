"""Programmatic companion CLI for library search and filesystem operations."""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

from perfect_prompts import __version__
from perfect_prompts.application.use_cases.batch_query import BatchQuery
from perfect_prompts.contracts.dto import AddArtifactRequest, RemoveArtifactRequest, SearchRequest
from perfect_prompts.infrastructure.filesystem.artifact_store import LocalArtifactStore
from perfect_prompts.infrastructure.launcher.installer import install_launchers
from perfect_prompts.infrastructure.search.exporter import SearchResultsExporter
from perfect_prompts.infrastructure.search.prompt_beacon import PromptBeaconIndex


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="perfect-prompts-cli", description="Perfect Prompts local library tools")
    parser.add_argument("--version", action="version", version=f"Perfect Prompts {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    for name in ("index", "sync", "status"):
        command = sub.add_parser(name)
        command.add_argument("--root", type=Path, default=Path.cwd())
        if name == "status":
            command.add_argument("--json", action="store_true")

    query = sub.add_parser("query")
    query.add_argument("query", nargs="+")
    query.add_argument("--root", type=Path, default=Path.cwd())
    query.add_argument("--limit", type=int, default=40)
    query.add_argument("--area")
    query.add_argument("--type", dest="artifact_type")
    query.add_argument("--runtime")
    query.add_argument("--source-scope")
    query.add_argument("--path-prefix")
    query.add_argument("--json", action="store_true")
    query.add_argument("--export", action="store_true")

    batch = sub.add_parser("batch")
    batch.add_argument("--root", type=Path, default=Path.cwd())
    source = batch.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", type=Path)
    source.add_argument("--queries")
    batch.add_argument("--limit", type=int, default=40)
    batch.add_argument("--json", action="store_true")

    add = sub.add_parser("add")
    add.add_argument("source", type=Path)
    add.add_argument("--to", dest="destination", required=True, help="Repository-relative destination directory")
    add.add_argument("--name", default="")
    add.add_argument("--replace", action="store_true")
    add.add_argument("--root", type=Path, default=Path.cwd())

    remove = sub.add_parser("remove")
    remove.add_argument("path", help="Repository-relative artifact path")
    remove.add_argument("--recursive", action="store_true")
    remove.add_argument("--root", type=Path, default=Path.cwd())

    launcher = sub.add_parser("install-launcher")
    launcher.add_argument("--root", type=Path, required=True)
    launcher.add_argument("--no-desktop", action="store_true")
    launcher.add_argument("--no-menu", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "install-launcher":
        receipt = install_launchers(args.root, desktop=not args.no_desktop, menu=not args.no_menu)
        for path in receipt.paths:
            print(path)
        return 0

    root = args.root.expanduser().resolve()
    index = PromptBeaconIndex(root)
    try:
        if args.command == "index":
            print(json.dumps(asdict(index.rebuild()), indent=2))
            return 0
        if args.command == "sync":
            print(json.dumps(asdict(index.sync()), indent=2))
            return 0
        if args.command == "add":
            receipt = LocalArtifactStore(root).add(AddArtifactRequest(args.source, args.destination, args.name, args.replace))
            report = index.sync()
            print(json.dumps({"artifact": str(receipt.destination), "sync": asdict(report)}, indent=2))
            return 0
        if args.command == "remove":
            receipt = LocalArtifactStore(root).remove(RemoveArtifactRequest(args.path, args.recursive))
            report = index.sync()
            print(json.dumps({"removed": asdict(receipt), "sync": asdict(report)}, indent=2))
            return 0
        if args.command == "query":
            request = SearchRequest(
                " ".join(args.query), area=args.area, artifact_type=args.artifact_type,
                runtime=args.runtime, source_scope=args.source_scope, path_prefix=args.path_prefix, limit=args.limit,
            )
            started = time.perf_counter(); hits = index.search(request); elapsed = (time.perf_counter() - started) * 1000
            captured = SearchResultsExporter(index.root).capture(request, hits, search_duration_ms=elapsed)
            if args.json:
                print(json.dumps(captured, indent=2, ensure_ascii=False))
            else:
                print(f"{len(hits)} result(s) in {elapsed:.2f} ms")
                for pos, hit in enumerate(hits, 1):
                    print(f"{pos:>3}. {hit.rank:.6f}  [{hit.area}/{hit.artifact_type}] {hit.path}")
            if args.export:
                print(f"exported: {SearchResultsExporter(index.root).write(captured)}")
            return 0
        if args.command == "batch":
            text = (args.file if args.file.is_absolute() else index.root / args.file).read_text(encoding="utf-8") if args.file else args.queries
            results = BatchQuery(index, index.root).execute(text, limit=args.limit)
            if args.json:
                print(json.dumps([asdict(item) for item in results], indent=2, ensure_ascii=False, default=str))
            else:
                for item in results:
                    print(f"{item.query}: {len(item.hits)} hit(s)" + (f" ERROR {item.error}" if item.error else f" -> {item.export_path}"))
            return 1 if any(item.error for item in results) else 0
        if args.command == "status":
            status = index.status()
            print(json.dumps(status, indent=2) if args.json else "\n".join(f"{k}: {v}" for k, v in status.items()))
            return 0
    except (OSError, ValueError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
