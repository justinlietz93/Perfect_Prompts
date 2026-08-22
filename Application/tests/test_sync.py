from pathlib import Path
from perfect_prompts.contracts.dto import SearchRequest
from perfect_prompts.infrastructure.search.prompt_beacon import PromptBeaconIndex


def test_sync_reflects_native_filesystem_add_change_and_remove(tmp_path: Path):
    folder = tmp_path / "Prompts" / "Portable" / "Plaintext"; folder.mkdir(parents=True)
    first = folder / "a.md"; first.write_text("alpha", encoding="utf-8")
    index = PromptBeaconIndex(tmp_path); index.rebuild()
    assert index.search(SearchRequest("alpha"))

    second = folder / "b.md"; second.write_text("beta", encoding="utf-8")
    report = index.sync(); assert report.added >= 1
    assert any(hit.path.endswith("b.md") for hit in index.search(SearchRequest("beta")))

    second.write_text("gamma changed body", encoding="utf-8")
    report = index.sync(); assert report.updated >= 1
    assert any(hit.path.endswith("b.md") for hit in index.search(SearchRequest("gamma")))

    first.unlink()
    report = index.sync(); assert report.removed >= 1
    assert not any(hit.path.endswith("a.md") for hit in index.search(SearchRequest("alpha")))
