from perfect_prompts.contracts.dto import SearchHit, SearchRequest
from perfect_prompts.contracts.ports import SearchIndexPort


class ExportQuery:
    def __init__(self, index: SearchIndexPort):
        self._index = index

    def execute(self, request: SearchRequest, hits: tuple[SearchHit, ...]) -> str:
        return self._index.export_query(request, hits)
