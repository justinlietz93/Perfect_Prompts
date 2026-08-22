from perfect_prompts.contracts.dto import AddArtifactReceipt, AddArtifactRequest
from perfect_prompts.contracts.ports import ArtifactStorePort


class AddArtifact:
    def __init__(self, store: ArtifactStorePort):
        self._store = store

    def execute(self, request: AddArtifactRequest) -> AddArtifactReceipt:
        return self._store.add(request)
