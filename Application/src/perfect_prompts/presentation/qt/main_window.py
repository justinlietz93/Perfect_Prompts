"""Perfect Prompts application shell using Lamina's presentation boundaries."""

from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtGui import QAction, QIcon, QKeySequence, QPixmap
from PySide6.QtWidgets import (
    QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMessageBox, QPushButton,
    QTabWidget, QVBoxLayout, QWidget,
)

from perfect_prompts.presentation.controllers.library_controller import LibraryController
from perfect_prompts.presentation.qt.theme import STYLE
from perfect_prompts.presentation.qt.widgets.batch_page import BatchPage
from perfect_prompts.presentation.qt.widgets.library_page import LibraryPage
from perfect_prompts.presentation.qt.widgets.search_page import SearchPage
from perfect_prompts.resources import icon_png_path


class MainWindow(QMainWindow):
    AUTO_SYNC_MS = 10_000

    def __init__(self, initial_root: Path, controller_factory, remember_root):
        super().__init__()
        self._controller_factory = controller_factory
        self._remember_root = remember_root
        self._controller: LibraryController | None = None
        self._index_busy = False
        self._build_shell()
        self._load_root(initial_root)
        self._auto_sync = QTimer(self)
        self._auto_sync.setInterval(self.AUTO_SYNC_MS)
        self._auto_sync.timeout.connect(lambda: self._start_sync(True))
        self._auto_sync.start()

    def _build_shell(self) -> None:
        self.setWindowTitle("Perfect Prompts")
        self.setWindowIcon(QIcon(str(icon_png_path())))
        self.resize(1280, 880)
        self.setMinimumSize(980, 660)
        self.setStyleSheet(STYLE)
        icon = QLabel(); pix = QPixmap(str(icon_png_path())); icon.setPixmap(pix.scaled(54, 54)); icon.setFixedSize(58, 58)
        title = QLabel("Perfect Prompts"); title.setObjectName("brandTitle")
        subtitle = QLabel("Prompt & Context Engineering Library"); subtitle.setObjectName("brandSubtitle")
        titles = QVBoxLayout(); titles.setSpacing(1); titles.addWidget(title); titles.addWidget(subtitle)
        brand = QHBoxLayout(); brand.addWidget(icon); brand.addLayout(titles); brand.addStretch(1)

        self._root_field = QLineEdit(); self._root_field.setReadOnly(True)
        self._choose_root = QPushButton("Open Repository…"); self._choose_root.setObjectName("secondaryButton")
        self._sync = QPushButton("Sync")
        self._rebuild = QPushButton("Rebuild Index"); self._rebuild.setObjectName("secondaryButton")
        self._status = QLabel("No repository loaded"); self._status.setObjectName("statusLabel")
        root_row = QHBoxLayout()
        root_row.addWidget(QLabel("Repository")); root_row.addWidget(self._root_field, 1)
        root_row.addWidget(self._choose_root); root_row.addWidget(self._sync); root_row.addWidget(self._rebuild)
        self._tabs = QTabWidget()
        wrapper = QWidget(); layout = QVBoxLayout(wrapper)
        layout.addLayout(brand); layout.addLayout(root_row); layout.addWidget(self._status); layout.addWidget(self._tabs, 1)
        self.setCentralWidget(wrapper)
        self._choose_root.clicked.connect(self._choose_repository)
        self._sync.clicked.connect(lambda: self._start_sync(False))
        self._rebuild.clicked.connect(self._start_rebuild)
        focus = QAction(self); focus.setShortcut(QKeySequence("Ctrl+K")); focus.triggered.connect(self._focus_search); self.addAction(focus)

    def _load_root(self, root: Path) -> None:
        root = root.expanduser().resolve()
        if not root.is_dir():
            return
        if self._controller is not None:
            self._controller.close()
        self._controller = self._controller_factory(root)
        self._root_field.setText(str(root))
        self._remember_root(root)
        self._tabs.clear()
        self._search_page = SearchPage(self._controller, self._start_sync)
        self._batch_page = BatchPage(self._controller)
        self._library_page = LibraryPage(self._controller, self._start_sync)
        self._tabs.addTab(self._search_page, "Search")
        self._tabs.addTab(self._batch_page, "Batch")
        self._tabs.addTab(self._library_page, "Library")
        status = self._controller.status()
        self._render_status(status)
        if not status.get("exists"):
            QTimer.singleShot(0, self._start_rebuild)
        else:
            QTimer.singleShot(0, lambda: self._start_sync(True))

    def _choose_repository(self) -> None:
        path = QFileDialog.getExistingDirectory(self, "Open Perfect Prompts repository", self._root_field.text())
        if path:
            self._load_root(Path(path))

    def _start_rebuild(self) -> None:
        if self._controller is None or self._index_busy:
            return
        self._index_busy = True
        self._set_index_buttons(False)
        self._status.setText("Rebuilding the Prompt Beacon index in the background…")
        self._controller.rebuild_index(lambda report, error: self._index_done(report, error, "Rebuild"))

    def _start_sync(self, silent: bool = False) -> None:
        if self._controller is None or self._index_busy:
            return
        self._index_busy = True
        self._set_index_buttons(False)
        if not silent:
            self._status.setText("Synchronizing filesystem changes with the Prompt Beacon index…")
        self._controller.sync_index(lambda report, error: self._index_done(report, error, "Sync", silent=silent))

    def _index_done(self, report, error, operation: str, *, silent: bool = False) -> None:
        self._index_busy = False
        self._set_index_buttons(True)
        if error:
            self._status.setText(f"{operation} failed: {error}")
            if not silent:
                QMessageBox.critical(self, f"{operation} failed", str(error))
            return
        if report is None:
            return
        changed = report.added + report.updated + report.removed
        if operation == "Rebuild" or changed or not silent:
            self._status.setText(
                f"Index ready · {report.nodes:,} nodes · {report.indexed_files:,} searchable files · "
                f"{report.added} added · {report.updated} updated · {report.removed} removed · {report.errors} extraction errors"
            )
        if hasattr(self, "_library_page"):
            self._library_page.refresh()

    def _set_index_buttons(self, enabled: bool) -> None:
        self._sync.setEnabled(enabled)
        self._rebuild.setEnabled(enabled)

    def _render_status(self, status: dict[str, object]) -> None:
        if not status.get("exists"):
            self._status.setText("Search index not built yet. It will be created automatically.")
            return
        self._status.setText(
            f"Index ready · {status.get('node_count','?')} nodes · {status.get('indexed_file_count','?')} searchable files · "
            f"synced {status.get('synced_at') or status.get('built_at','unknown')}"
        )

    def _focus_search(self) -> None:
        if hasattr(self, "_search_page"):
            self._tabs.setCurrentWidget(self._search_page)
            self._search_page.focus_query()

    def changeEvent(self, event) -> None:
        super().changeEvent(event)
        if event.type() == QEvent.Type.ActivationChange and self.isActiveWindow():
            QTimer.singleShot(0, lambda: self._start_sync(True))

    def closeEvent(self, event) -> None:
        if self._controller is not None:
            self._controller.close()
        super().closeEvent(event)
