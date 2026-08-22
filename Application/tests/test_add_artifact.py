from pathlib import Path
import pytest
from perfect_prompts.contracts.dto import AddArtifactRequest
from perfect_prompts.infrastructure.filesystem.artifact_store import LocalArtifactStore


def test_add_artifact_copies_to_repository_relative_destination(tmp_path: Path):
    source = tmp_path / "source.md"; source.write_text("hello", encoding="utf-8")
    repo = tmp_path / "repo"
    receipt = LocalArtifactStore(repo).add(AddArtifactRequest(source, "Skills/custom"))
    assert receipt.destination == repo / "Skills" / "custom" / "source.md"
    assert receipt.destination.read_text(encoding="utf-8") == "hello"


def test_add_artifact_refuses_escape(tmp_path: Path):
    source = tmp_path / "source.md"; source.write_text("hello", encoding="utf-8")
    with pytest.raises(ValueError):
        LocalArtifactStore(tmp_path / "repo").add(AddArtifactRequest(source, "../escape"))


def test_add_artifact_refuses_protected_application_path(tmp_path: Path):
    source = tmp_path / "source.md"; source.write_text("hello", encoding="utf-8")
    with pytest.raises(PermissionError):
        LocalArtifactStore(tmp_path / "repo").add(AddArtifactRequest(source, "Application"))
