from perfect_prompts.contracts.ports import SearchIndexPort


class GetIndexStatus:
    def __init__(self, index: SearchIndexPort):
        self._index = index

    def execute(self) -> dict[str, object]:
        return self._index.status()
