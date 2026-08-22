from collections.abc import Callable
from perfect_prompts.contracts.dto import IndexReport
from perfect_prompts.contracts.ports import SearchIndexPort


class SyncIndex:
    def __init__(self, index: SearchIndexPort):
        self._index = index

    def execute(self, cancelled: Callable[[], bool] | None = None) -> IndexReport:
        return self._index.sync(cancelled=cancelled)
