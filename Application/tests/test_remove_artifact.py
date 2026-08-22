from pathlib import Path
import pytest
from perfect_prompts.contracts.dto import RemoveArtifactRequest
from perfect_prompts.infrastructure.filesystem.artifact_store import LocalArtifactStore


def test_remove_file_and_directory(tmp_path: Path):
    repo = tmp_path / "repo"; target = repo / "Prompts" / "Portable" / "Plaintext"; target.mkdir(parents=True)
    file = target / "a.md"; file.write_text("alpha", encoding="utf-8")
    store = LocalArtifactStore(repo)
    receipt = store.remove(RemoveArtifactRequest("Prompts/Portable/Plaintext/a.md"))
    assert receipt.removed_count == 1 and not file.exists()
    folder = target / "bundle"; folder.mkdir(); (folder / "b.md").write_text("beta", encoding="utf-8")
    receipt = store.remove(RemoveArtifactRequest("Prompts/Portable/Plaintext/bundle", recursive=True))
    assert receipt.removed_directory and receipt.removed_count == 2 and not folder.exists()


def test_remove_refuses_repository_root_and_application(tmp_path: Path):
    repo = tmp_path / "repo"; (repo / "Application").mkdir(parents=True)
    store = LocalArtifactStore(repo)
    with pytest.raises(ValueError): store.remove(RemoveArtifactRequest(""))
    with pytest.raises(PermissionError): store.remove(RemoveArtifactRequest("Application", recursive=True))
