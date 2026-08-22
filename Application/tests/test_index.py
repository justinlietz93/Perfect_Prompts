from pathlib import Path
from perfect_prompts.contracts.dto import SearchRequest
from perfect_prompts.infrastructure.search.prompt_beacon import PromptBeaconIndex


def test_index_search_filters_and_application_exclusion(tmp_path: Path):
    standards = tmp_path / "Standards" / "Architecture"; standards.mkdir(parents=True)
    (standards / "a.md").write_text("emergence based architecture constraints", encoding="utf-8")
    prompts = tmp_path / "Prompts" / "Runtime_Bindings" / "Python" / "agent_prompts"; prompts.mkdir(parents=True)
    (prompts / "reasoner.py").write_text('PROMPT = "architecture reasoning"', encoding="utf-8")
    app = tmp_path / "Application"; app.mkdir(); (app / "noise.py").write_text("architecture", encoding="utf-8")
    index = PromptBeaconIndex(tmp_path); report = index.rebuild()
    assert report.indexed_files == 2
    hits = index.search(SearchRequest("architecture")); assert len([h for h in hits if h.kind == "file"]) == 2
    python_hits = index.search(SearchRequest("architecture", runtime="python"))
    assert [h.path for h in python_hits] == ["Prompts/Runtime_Bindings/Python/agent_prompts/reasoner.py"]
    standard_hits = index.search(SearchRequest("architecture", artifact_type="standard"))
    assert len([h for h in standard_hits if h.kind == "file"]) == 1
