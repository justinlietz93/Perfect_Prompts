"""Path-derived classification for the reorganized Perfect Prompts library."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath


AREAS = (
    "Agent Instructions",
    "Methodologies",
    "Personas",
    "Standards",
    "Prompt Templates",
    "Prompt Implementations",
    "Context Builders",
    "Rules",
    "Skills",
    "Guidelines",
    "External References",
    "Repository",
    "Other",
)

ARTIFACT_TYPES = (
    "agent_instruction",
    "methodology",
    "persona",
    "standard",
    "prompt_template",
    "ruleset",
    "skill",
    "agent_prompt",
    "summary_prompt",
    "context_builder",
    "education_prompt",
    "prompt",
    "example",
    "reference",
    "repository_metadata",
    "other",
)

RUNTIMES = ("plaintext", "python", "typescript", "rust", "go", "json", "structured_text", "mixed", "")
SOURCE_SCOPES = ("project", "external_reference")

# Top-level directories that constitute the Perfect Prompts library corpus.
# Repository/application infrastructure at the root is deliberately outside this boundary.
LIBRARY_ROOT_DIRECTORIES = frozenset({
    "Agent_Instructions",
    "Guidelines",
    "Methodologies",
    "Personas",
    "Prompts",
    "Rules",
    "Skills",
    "Standards",
    "External_References",
})


def is_library_relative_path(relative_path: str) -> bool:
    """Return whether a repository-relative path belongs to the library corpus."""
    normalized = relative_path.replace("\\", "/").strip("/")
    if not normalized or normalized == ".":
        return False
    return PurePosixPath(normalized).parts[0] in LIBRARY_ROOT_DIRECTORIES


@dataclass(frozen=True, slots=True)
class ArtifactClassification:
    area: str
    artifact_type: str
    runtime: str
    source_scope: str


def classify_relative_path(relative_path: str) -> ArtifactClassification:
    normalized = relative_path.replace("\\", "/").strip("/")
    if not normalized or normalized == ".":
        return ArtifactClassification("Repository", "repository_metadata", "", "project")

    path = PurePosixPath(normalized)
    parts = path.parts
    lowered = tuple(part.casefold() for part in parts)
    top = parts[0]

    if top == "External_References":
        return ArtifactClassification("External References", "reference", _runtime(parts), "external_reference")
    if top == "Agent_Instructions":
        return ArtifactClassification("Agent Instructions", "agent_instruction", _runtime(parts), "project")
    if top == "Methodologies":
        kind = "agent_instruction" if path.name.casefold().endswith("agents.md") else "methodology"
        return ArtifactClassification("Methodologies", kind, _runtime(parts), "project")
    if top == "Personas":
        return ArtifactClassification("Personas", "persona", _runtime(parts), "project")
    if top == "Standards":
        return ArtifactClassification("Standards", "standard", _runtime(parts), "project")
    if top == "Rules":
        return ArtifactClassification("Rules", "ruleset", _runtime(parts), "project")
    if top == "Skills":
        return ArtifactClassification("Skills", "skill", _runtime(parts), "project")
    if top == "Guidelines":
        return ArtifactClassification("Guidelines", "reference", _runtime(parts), "project")
    if top == "Prompts":
        if len(parts) > 1 and parts[1] == "Templates":
            return ArtifactClassification("Prompt Templates", "prompt_template", _runtime(parts), "project")
        artifact_type, area = _prompt_family(lowered)
        return ArtifactClassification(area, artifact_type, _runtime(parts), "project")
    if len(parts) == 1:
        return ArtifactClassification("Repository", "repository_metadata", _runtime(parts), "project")
    return ArtifactClassification("Other", "other", _runtime(parts), "project")


def _prompt_family(lowered_parts: tuple[str, ...]) -> tuple[str, str]:
    if "context_builder_prompts" in lowered_parts:
        return "context_builder", "Context Builders"
    if "agent_prompts" in lowered_parts:
        return "agent_prompt", "Prompt Implementations"
    if "summary_prompts" in lowered_parts:
        return "summary_prompt", "Prompt Implementations"
    if "education_prompts" in lowered_parts:
        return "education_prompt", "Prompt Implementations"
    if "examples" in lowered_parts:
        return "example", "Prompt Implementations"
    return "prompt", "Prompt Implementations"


def _runtime(parts: tuple[str, ...]) -> str:
    normalized = {part.casefold(): part for part in parts}
    mapping = {
        "python": "python",
        "typescript": "typescript",
        "rust": "rust",
        "go": "go",
        "plaintext": "plaintext",
        "json": "json",
        "structured_text": "structured_text",
    }
    for key, value in mapping.items():
        if key in normalized:
            return value
    suffix = PurePosixPath(parts[-1]).suffix.casefold() if parts else ""
    return {
        ".py": "python", ".ts": "typescript", ".tsx": "typescript", ".rs": "rust", ".go": "go",
        ".txt": "plaintext", ".json": "json", ".jsonl": "json",
        ".yaml": "structured_text", ".yml": "structured_text", ".xml": "structured_text", ".md": "plaintext",
    }.get(suffix, "")
