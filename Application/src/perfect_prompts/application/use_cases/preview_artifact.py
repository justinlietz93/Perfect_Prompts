from perfect_prompts.contracts.ports import SearchIndexPort


class PreviewArtifact:
    def __init__(self, index: SearchIndexPort):
        self._index = index

    def execute(self, relative_path: str) -> str:
        return self._index.read_content(relative_path)
