from perfect_prompts.contracts.dto import SearchHit, SearchRequest
from perfect_prompts.contracts.ports import SearchIndexPort


class SearchLibrary:
    def __init__(self, index: SearchIndexPort):
        self._index = index

    def execute(self, request: SearchRequest) -> tuple[SearchHit, ...]:
        if not request.query.strip():
            return ()
        return self._index.search(request)
