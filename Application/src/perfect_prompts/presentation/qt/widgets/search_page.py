"""Primary single-query workspace."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QComboBox, QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMessageBox, QPlainTextEdit, QPushButton, QSplitter, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget,
)

from perfect_prompts.contracts.dto import RemoveArtifactRequest, SearchHit, SearchRequest
from perfect_prompts.domain.classification import AREAS, ARTIFACT_TYPES, RUNTIMES, SOURCE_SCOPES
from perfect_prompts.presentation.controllers.library_controller import LibraryController


class SearchPage(QWidget):
    def __init__(self, controller: LibraryController, on_sync, parent=None):
        super().__init__(parent)
        self._controller = controller
        self._on_sync = on_sync
        self._hits: tuple[SearchHit, ...] = ()
        self._last_request = SearchRequest("")
        self._build()

    def _build(self) -> None:
        self._query = QLineEdit()
        self._query.setPlaceholderText('Search prompts, skills, standards, personas, scripts…  e.g. "session handoff" or architecture')
        self._search = QPushButton("Search")
        self._area = _filter_combo("All areas", AREAS)
        self._type = _filter_combo("All types", ARTIFACT_TYPES)
        self._runtime = _filter_combo("All runtimes", tuple(value for value in RUNTIMES if value))
        self._scope = _filter_combo("All sources", SOURCE_SCOPES, default="project")
        self._path = QLineEdit(); self._path.setPlaceholderText("Optional path prefix")

        query_row = QHBoxLayout(); query_row.addWidget(self._query, 1); query_row.addWidget(self._search)
        filters = QHBoxLayout()
        for widget in (self._area, self._type, self._runtime, self._scope): filters.addWidget(widget)
        filters.addWidget(self._path, 1)

        self._summary = QLabel("Ready. Project-authored material is searched by default; external references are available from the source filter.")
        self._table = QTableWidget(0, 6)
        self._table.setHorizontalHeaderLabels(["Type", "Area", "Runtime", "Artifact", "Path", "Score"])
        self._table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self._table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self._table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        header = self._table.horizontalHeader()
        for column in (0,1,2,3,5): header.setSectionResizeMode(column, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self._preview_title = QLabel("Select a result"); self._preview_title.setObjectName("previewTitle")
        self._meta = QLabel(""); self._meta.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self._content = QPlainTextEdit(); self._content.setReadOnly(True)
        self._open = QPushButton("Open File"); self._open.setObjectName("secondaryButton")
        self._open_folder = QPushButton("Open Folder"); self._open_folder.setObjectName("secondaryButton")
        self._copy_path = QPushButton("Copy Path"); self._copy_path.setObjectName("secondaryButton")
        self._copy_content = QPushButton("Copy Content")
        self._remove = QPushButton("Remove"); self._remove.setObjectName("dangerButton")
        self._export = QPushButton("Export Query JSON"); self._export.setObjectName("secondaryButton")
        actions = QHBoxLayout()
        for widget in (self._open, self._open_folder, self._copy_path, self._copy_content, self._remove, self._export): actions.addWidget(widget)
        actions.addStretch(1)
        preview = QWidget(); preview_layout = QVBoxLayout(preview)
        preview_layout.addWidget(self._preview_title); preview_layout.addWidget(self._meta)
        preview_layout.addLayout(actions); preview_layout.addWidget(self._content, 1)

        splitter = QSplitter(Qt.Orientation.Vertical); splitter.addWidget(self._table); splitter.addWidget(preview); splitter.setSizes([370, 390])
        layout = QVBoxLayout(self); layout.addLayout(query_row); layout.addLayout(filters); layout.addWidget(self._summary); layout.addWidget(splitter, 1)

        self._search.clicked.connect(self._run_search); self._query.returnPressed.connect(self._run_search)
        self._table.itemSelectionChanged.connect(self._show_selected)
        self._open.clicked.connect(self._open_selected); self._open_folder.clicked.connect(self._open_selected_folder)
        self._copy_path.clicked.connect(self._copy_selected_path); self._copy_content.clicked.connect(self._copy_selected_content)
        self._remove.clicked.connect(self._remove_selected); self._export.clicked.connect(self._export_results)

    def focus_query(self) -> None:
        self._query.setFocus(); self._query.selectAll()

    def _run_search(self) -> None:
        self._last_request = SearchRequest(
            query=self._query.text(), area=self._area.currentData(), artifact_type=self._type.currentData(),
            runtime=self._runtime.currentData(), source_scope=self._scope.currentData(),
            path_prefix=self._path.text().strip() or None, limit=150,
        )
        try:
            self._hits = self._controller.search(self._last_request)
            self._render_hits()
        except Exception as error:
            self._summary.setText(f"Search error: {error}")

    def _render_hits(self) -> None:
        self._table.setRowCount(len(self._hits))
        for row, hit in enumerate(self._hits):
            values = [hit.artifact_type.replace("_", " "), hit.area, hit.runtime or "—", hit.name, hit.path, f"{hit.rank:.5f}"]
            for column, value in enumerate(values): self._table.setItem(row, column, QTableWidgetItem(value))
        self._summary.setText(f"{len(self._hits)} result(s)")
        if self._hits: self._table.selectRow(0)
        else:
            self._preview_title.setText("No result selected"); self._meta.clear(); self._content.clear()

    def _selected(self) -> SearchHit | None:
        row = self._table.currentRow()
        return self._hits[row] if 0 <= row < len(self._hits) else None

    def _show_selected(self) -> None:
        hit = self._selected()
        if hit is None: return
        self._preview_title.setText(hit.name)
        self._meta.setText(f"{hit.area} · {hit.artifact_type.replace('_',' ')} · {hit.runtime or 'generic'} · {hit.source_scope}")
        try: content = self._controller.preview(hit.path)
        except Exception as error: content = f"Preview unavailable: {error}"
        if len(content) > 160_000: content = content[:160_000] + "\n\n[… preview truncated …]"
        self._content.setPlainText(content)

    def _absolute_path(self) -> Path | None:
        hit = self._selected()
        return self._controller.root / hit.path if hit else None

    def _open_selected(self) -> None:
        path = self._absolute_path()
        if path and path.exists(): QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))

    def _open_selected_folder(self) -> None:
        path = self._absolute_path()
        if path:
            target = path if path.is_dir() else path.parent
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(target)))

    def _copy_selected_path(self) -> None:
        path = self._absolute_path()
        if path: QApplication.clipboard().setText(str(path))

    def _copy_selected_content(self) -> None:
        QApplication.clipboard().setText(self._content.toPlainText())

    def _remove_selected(self) -> None:
        hit = self._selected()
        path = self._absolute_path()
        if hit is None or path is None:
            return
        answer = QMessageBox.question(
            self, "Remove artifact", f"Remove this artifact from the repository?\n\n{hit.path}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer != QMessageBox.StandardButton.Yes:
            return
        try:
            self._controller.remove_artifact(RemoveArtifactRequest(hit.path, recursive=path.is_dir()))
            self._hits = tuple(item for item in self._hits if item.path != hit.path and not item.path.startswith(hit.path.rstrip('/') + '/'))
            self._render_hits()
            self._summary.setText(f"Removed {hit.path}; synchronizing search index…")
            self._on_sync(True)
        except Exception as error:
            QMessageBox.critical(self, "Could not remove artifact", str(error))

    def _export_results(self) -> None:
        if not self._last_request.query.strip(): return
        try:
            path = self._controller.export_query(self._last_request, self._hits)
            self._summary.setText(f"Exported query: {path}")
        except Exception as error:
            QMessageBox.critical(self, "Export failed", str(error))


def _filter_combo(label: str, values: tuple[str, ...], default: str | None = None) -> QComboBox:
    combo = QComboBox(); combo.addItem(label, None)
    default_index = 0
    for value in values:
        combo.addItem(value.replace("_", " ").title() if value.islower() else value, value)
        if value == default:
            default_index = combo.count() - 1
    combo.setCurrentIndex(default_index)
    return combo
