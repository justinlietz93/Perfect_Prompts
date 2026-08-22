from perfect_prompts.contracts.dto import RemoveArtifactReceipt, RemoveArtifactRequest
from perfect_prompts.contracts.ports import ArtifactStorePort


class RemoveArtifact:
    def __init__(self, store: ArtifactStorePort):
        self._store = store

    def execute(self, request: RemoveArtifactRequest) -> RemoveArtifactReceipt:
        return self._store.remove(request)
