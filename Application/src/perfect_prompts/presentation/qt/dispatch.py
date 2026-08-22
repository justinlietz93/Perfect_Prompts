from __future__ import annotations

from collections.abc import Callable
from PySide6.QtCore import QObject, Qt, Signal


class GuiDispatcher(QObject):
    _posted = Signal(object)

    def __init__(self, parent: QObject | None = None):
        super().__init__(parent)
        self._posted.connect(self._run, Qt.ConnectionType.QueuedConnection)

    def post(self, action: Callable[[], None]) -> None:
        self._posted.emit(action)

    @staticmethod
    def _run(action: Callable[[], None]) -> None:
        action()
