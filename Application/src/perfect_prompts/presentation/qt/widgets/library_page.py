"""Native-filesystem library browser and artifact management surface."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QDir, QModelIndex, Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QFileDialog,
    QFileSystemModel,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTreeView,
    QVBoxLayout,
    QWidget,
)

from perfect_prompts.contracts.dto import AddArtifactRequest, RemoveArtifactRequest
from perfect_prompts.presentation.controllers.library_controller import LibraryController


class LibraryPage(QWidget):
    def __init__(self, controller: LibraryController, on_sync, parent=None):
        super().__init__(parent)
        self._controller = controller
        self._on_sync = on_sync
        self._build()

    def _build(self) -> None:
        intro = QLabel(
            "This is the real repository filesystem. Changes made here or in your OS file manager operate on the same files."
        )
        intro.setWordWrap(True)

        self._model = QFileSystemModel(self)
        self._model.setFilter(QDir.Filter.AllEntries | QDir.Filter.NoDotAndDotDot)
        root_index = self._model.setRootPath(str(self._controller.root))
        self._tree = QTreeView()
        self._tree.setModel(self._model)
        self._tree.setRootIndex(root_index)
        self._tree.setAlternatingRowColors(True)
        self._tree.setSortingEnabled(True)
        self._tree.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self._tree.setColumnWidth(0, 430)

        self._add_files = QPushButton("Add File(s)…")
        self._add_folder = QPushButton("Add Folder…")
        self._remove = QPushButton("Remove")
        self._remove.setObjectName("dangerButton")
        self._open = QPushButton("Open")
        self._open.setObjectName("secondaryButton")
        self._reveal = QPushButton("Open Folder")
        self._reveal.setObjectName("secondaryButton")
        self._sync = QPushButton("Sync Search Index")
        self._sync.setObjectName("secondaryButton")
        row = QHBoxLayout()
        for button in (self._add_files, self._add_folder, self._remove, self._open, self._reveal, self._sync):
            row.addWidget(button)
        row.addStretch(1)

        self._status = QLabel("Select a folder to add into it, or select an artifact to open/remove.")
        self._status.setWordWrap(True)
        layout = QVBoxLayout(self)
        layout.addWidget(intro)
        layout.addLayout(row)
        layout.addWidget(self._tree, 1)
        layout.addWidget(self._status)

        self._add_files.clicked.connect(self._choose_files)
        self._add_folder.clicked.connect(self._choose_folder)
        self._remove.clicked.connect(self._remove_selected)
        self._open.clicked.connect(self._open_selected)
        self._reveal.clicked.connect(self._reveal_selected)
        self._sync.clicked.connect(lambda: self._on_sync(False))
        self._tree.doubleClicked.connect(self._double_clicked)

    def refresh(self) -> None:
        path = self._selected_path() or self._controller.root
        self._model.setRootPath(str(self._controller.root))
        index = self._model.index(str(path))
        if index.isValid():
            self._tree.setCurrentIndex(index)

    def _selected_path(self) -> Path | None:
        index = self._tree.currentIndex()
        if not index.isValid():
            return None
        return Path(self._model.filePath(index)).resolve()

    def _destination_directory(self) -> Path:
        selected = self._selected_path()
        if selected is None:
            prompts = self._controller.root / "Prompts"
            return prompts if prompts.is_dir() else self._controller.root
        return selected if selected.is_dir() else selected.parent

    def _destination_relative(self) -> str:
        destination = self._destination_directory()
        return "" if destination == self._controller.root else destination.relative_to(self._controller.root).as_posix()

    def _choose_files(self) -> None:
        paths, _ = QFileDialog.getOpenFileNames(self, "Add artifacts to Perfect Prompts")
        if not paths:
            return
        successes: list[Path] = []
        try:
            destination = self._destination_relative()
            for raw in paths:
                receipt = self._controller.add_artifact(AddArtifactRequest(Path(raw), destination))
                successes.append(receipt.destination)
        except Exception as error:
            QMessageBox.critical(self, "Could not add artifact", str(error))
        if successes:
            self._status.setText(f"Added {len(successes)} file(s) to {self._destination_directory()}")
            self._on_sync(True)

    def _choose_folder(self) -> None:
        raw = QFileDialog.getExistingDirectory(self, "Add artifact folder")
        if not raw:
            return
        try:
            receipt = self._controller.add_artifact(AddArtifactRequest(Path(raw), self._destination_relative()))
            self._status.setText(f"Added folder: {receipt.destination}")
            self._on_sync(True)
        except Exception as error:
            QMessageBox.critical(self, "Could not add folder", str(error))

    def _remove_selected(self) -> None:
        path = self._selected_path()
        if path is None or path == self._controller.root:
            return
        try:
            relative = path.relative_to(self._controller.root).as_posix()
        except ValueError:
            return
        kind = "folder and all of its contents" if path.is_dir() else "file"
        answer = QMessageBox.question(
            self,
            "Remove artifact",
            f"Remove this {kind} from the repository?\n\n{relative}",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if answer != QMessageBox.StandardButton.Yes:
            return
        try:
            receipt = self._controller.remove_artifact(RemoveArtifactRequest(relative, recursive=path.is_dir()))
            self._status.setText(f"Removed {receipt.relative_path} ({receipt.removed_count} filesystem node(s))")
            self._on_sync(True)
        except Exception as error:
            QMessageBox.critical(self, "Could not remove artifact", str(error))

    def _open_selected(self) -> None:
        path = self._selected_path()
        if path and path.exists():
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))

    def _reveal_selected(self) -> None:
        path = self._selected_path()
        if path:
            target = path if path.is_dir() else path.parent
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(target)))

    def _double_clicked(self, index: QModelIndex) -> None:
        path = Path(self._model.filePath(index))
        if path.is_file():
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))
