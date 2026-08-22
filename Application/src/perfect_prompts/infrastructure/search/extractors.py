from __future__ import annotations

import html
import json
import logging
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree

TEXT_EXTENSIONS = {
    ".c", ".cc", ".cfg", ".conf", ".cpp", ".cs", ".css", ".csv", ".go",
    ".h", ".hpp", ".html", ".ini", ".java", ".js", ".json", ".jsonl",
    ".jsx", ".lean", ".log", ".md", ".mmd", ".py", ".r", ".rs", ".rst",
    ".sh", ".sql", ".tex", ".toml", ".ts", ".tsv", ".tsx", ".txt",
    ".xml", ".yaml", ".yml",
}
MAX_TEXT_BYTES = 10 * 1024 * 1024
MAX_ZIP_MEMBER_BYTES = 2 * 1024 * 1024
MAX_ZIP_TOTAL_BYTES = 8 * 1024 * 1024


def extract_searchable_text(path: Path) -> str:
    suffix = path.suffix.casefold()
    if suffix in TEXT_EXTENSIONS:
        return _read_bounded_text(path)
    if suffix == ".ipynb":
        return _read_notebook(path)
    if suffix == ".pdf":
        return _read_pdf(path)
    if suffix in {".docx", ".pptx", ".xlsx"}:
        return _read_openxml(path, suffix)
    if suffix in {".odt", ".ods", ".odp"}:
        return _read_odf(path)
    if suffix in {".zip", ".skill"}:
        return _read_zip(path)
    return ""


def _read_bounded_text(path: Path) -> str:
    size = path.stat().st_size
    with path.open("rb") as handle:
        if size <= MAX_TEXT_BYTES:
            data = handle.read()
        else:
            head_size = MAX_TEXT_BYTES * 4 // 5
            tail_size = MAX_TEXT_BYTES - head_size
            head = handle.read(head_size)
            handle.seek(max(0, size - tail_size))
            data = head + b"\n[... bounded index gap ...]\n" + handle.read(tail_size)
    if b"\x00" in data[:8192]:
        return ""
    return data.decode("utf-8", errors="replace")


def _read_notebook(path: Path) -> str:
    data = json.loads(_read_bounded_text(path))
    pieces: list[str] = []
    for cell in data.get("cells", []):
        source = cell.get("source", [])
        pieces.append("".join(source) if isinstance(source, list) else str(source))
        for output in cell.get("outputs", []):
            text = output.get("text")
            if text:
                pieces.append("".join(text) if isinstance(text, list) else str(text))
    return "\n".join(pieces)


def _read_pdf(path: Path) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    reader = PdfReader(str(path))
    pieces: list[str] = []
    length = 0
    for page in reader.pages:
        text = page.extract_text() or ""
        pieces.append(text)
        length += len(text.encode("utf-8", errors="ignore"))
        if length >= MAX_TEXT_BYTES:
            break
    return "\n".join(pieces)


def _read_openxml(path: Path, suffix: str) -> str:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if suffix == ".docx":
            targets = [n for n in names if n == "word/document.xml" or n.startswith("word/header") or n.startswith("word/footer")]
        elif suffix == ".pptx":
            targets = [n for n in names if n.startswith("ppt/slides/slide") and n.endswith(".xml")]
        else:
            targets = [n for n in names if n == "xl/sharedStrings.xml" or (n.startswith("xl/worksheets/sheet") and n.endswith(".xml"))]
        pieces = [_xml_text(archive.read(name)) for name in targets]
    return "\n".join(piece for piece in pieces if piece)


def _read_odf(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        pieces = [_xml_text(archive.read(name)) for name in ("content.xml", "styles.xml", "meta.xml") if name in archive.namelist()]
    return "\n".join(piece for piece in pieces if piece)


def _xml_text(raw: bytes) -> str:
    try:
        root = ElementTree.fromstring(raw)
        text = " ".join(part.strip() for part in root.itertext() if part and part.strip())
        return html.unescape(re.sub(r"\s+", " ", text))
    except ElementTree.ParseError:
        text = re.sub(r"<[^>]+>", " ", raw.decode("utf-8", errors="replace"))
        return html.unescape(re.sub(r"\s+", " ", text))


def _read_zip(path: Path) -> str:
    pieces: list[str] = []
    consumed = 0
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile:
        return ""
    with archive:
        for info in archive.infolist():
            pieces.append(info.filename)
            suffix = Path(info.filename).suffix.casefold()
            if info.is_dir() or suffix not in TEXT_EXTENSIONS | {".ipynb"}:
                continue
            if info.file_size > MAX_ZIP_MEMBER_BYTES or consumed >= MAX_ZIP_TOTAL_BYTES:
                continue
            raw = archive.read(info)
            consumed += len(raw)
            if b"\x00" not in raw[:8192]:
                pieces.append(raw.decode("utf-8", errors="replace"))
    return "\n".join(pieces)
