"""Batch-query workspace using Prompt Beacon's independent-query semantics."""

from PySide6.QtWidgets import QLabel, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget

from perfect_prompts.presentation.controllers.library_controller import LibraryController


class BatchPage(QWidget):
    def __init__(self, controller: LibraryController, parent=None):
        super().__init__(parent)
        self._controller = controller
        self._queries = QPlainTextEdit()
        self._queries.setPlaceholderText('One query per line, or comma-separated on one line. Quoted phrases are preserved.\n\n"session handoff"\narchitecture standards\nprompt enhancer')
        self._run = QPushButton("Run Batch")
        self._status = QLabel("Each query is executed and exported independently.")
        self._results = QPlainTextEdit(); self._results.setReadOnly(True)
        layout = QVBoxLayout(self); layout.addWidget(QLabel("Batch queries")); layout.addWidget(self._queries, 1); layout.addWidget(self._run); layout.addWidget(self._status); layout.addWidget(self._results, 2)
        self._run.clicked.connect(self._on_run)

    def _on_run(self) -> None:
        self._run.setEnabled(False); self._status.setText("Running batch…")
        self._controller.run_batch(self._queries.toPlainText(), self._done)

    def _done(self, results, error) -> None:
        self._run.setEnabled(True)
        if error:
            self._status.setText(f"Batch failed: {error}"); return
        lines: list[str] = []; total_hits = 0
        for item in results or ():
            lines.append(f"## {item.query}")
            if item.error:
                lines.append(f"ERROR: {item.error}"); lines.append(""); continue
            total_hits += len(item.hits)
            for hit in item.hits: lines.append(f"- [{hit.area} / {hit.artifact_type}] {hit.path}")
            if not item.hits: lines.append("- no matches")
            if item.export_path: lines.append(f"  export: {item.export_path}")
            lines.append("")
        self._results.setPlainText("\n".join(lines))
        self._status.setText(f"Completed {len(results or ())} queries · {total_hits} total matches")
