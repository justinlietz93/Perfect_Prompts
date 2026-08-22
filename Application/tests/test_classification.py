from perfect_prompts.domain.classification import classify_relative_path


def test_project_specific_classification():
    assert classify_relative_path("Standards/Architecture/CLEAN_ARCHITECTURE_STANDARDS.md").artifact_type == "standard"
    assert classify_relative_path("Prompts/Templates/Research-Prompts/example.md").artifact_type == "prompt_template"
    assert classify_relative_path("Prompts/Runtime_Bindings/Python/agent_prompts/reasoner.py").runtime == "python"
    assert classify_relative_path("Prompts/Portable/Plaintext/context_builder_prompts/session.md").area == "Context Builders"
    assert classify_relative_path("External_References/library/prompt.md").source_scope == "external_reference"
    assert classify_relative_path("Skills/session_handoff_skill/validate_snapshot.py").artifact_type == "skill"
