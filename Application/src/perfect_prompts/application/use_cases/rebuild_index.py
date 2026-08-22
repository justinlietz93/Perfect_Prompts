from collections.abc import Callable
from perfect_prompts.contracts.dto import IndexReport
from perfect_prompts.contracts.ports import SearchIndexPort


class RebuildIndex:
    def __init__(self, index: SearchIndexPort):
        self._index = index

    def execute(self, cancelled: Callable[[], bool] | None = None) -> IndexReport:
        return self._index.rebuild(cancelled=cancelled)
