# Perfect_Prompts Repository Map

This repository is organized for **native filesystem and GitHub use first**. The desktop application is an optional interface over the same files. No library artifact is stored only in an application database.

544 directories, 4032 files. Click a folder below to browse its contents.

---

<details>
<summary><b>📁 Agent_Instructions/</b></summary>

```text
Agent_Instructions/
├── No-Assumptions_AGENTS.md
└── README.md
```

</details>

<details>
<summary><b>📁 Application/</b> <i>(Qt GUI, Python source, tests)</i></summary>

```text
Application/
├── assets/
├── docs/
├── pyproject.toml
├── scripts/
├── src/
│   └── perfect_prompts/
│       ├── application/
│       ├── cli.py
│       ├── main.py
│       └── presentation/
└── tests/
```

</details>

<details>
<summary><b>📁 Guidelines/</b></summary>

```text
Guidelines/
├── README.md
├── Rigorous-Truth-Seeking.md
└── SOURCE_README.md
```

</details>

<details>
<summary><b>📁 Methodologies/</b> <i>(GAP, Emergence, Cognitive)</i></summary>

```text
Methodologies/
├── Cognitive/
├── Germinal_Theory/
├── Guided_Autonomy_Prompting/
└── README.md
```

</details>

<details>
<summary><b>📁 Personas/</b> <i>(Apex multi-format personas)</i></summary>

```text
Personas/
├── Generic/
├── GitHub_Copilot/
├── README.md
├── Roo_Code/  (Analysts, Engineers, Researchers, etc.)
└── Structured/  (JSON, MD, XML, YAML variants)
```

</details>

<details>
<summary><b>📁 Prompts/</b> <i>(1,000+ categorized task templates)</i></summary>

```text
Prompts/
├── Categorized_Prompt_Collection/
│   ├── AI_and_Prompting/
│   ├── Business_and_Career/
│   ├── Creative/
│   ├── Data_Research_and_Analysis/
│   ├── Development/
│   ├── Education_and_Knowledge/
│   ├── Games_Roleplay_and_Simulation/
│   ├── Health_and_Wellness/
│   ├── Personal_and_Lifestyle/
│   ├── Tools_and_Productivity/
│   └── Writing_and_Language/
└── _manifest.csv
```

</details>

<details>
<summary><b>📁 Portable/</b> <i>(Canonical plaintext/JSON sources)</i></summary>

```text
Portable/
├── JSON/
├── Plaintext/
│   ├── agent_prompts/
│   ├── codex/
│   └── summary_prompts/
├── README.md
└── Structured_Text/
```

</details>

<details>
<summary><b>📁 Runtime_Bindings/</b> <i>(Go, Python, Rust, TypeScript exports)</i></summary>

```text
Runtime_Bindings/
├── Go/
├── Python/
├── README.md
├── Rust/
└── TypeScript/
```

</details>

<details>
<summary><b>📁 Rules/</b> <i>(Cross-domain, Linux, Physics, Software, UI/UX)</i></summary>

```text
Rules/
├── cross-domain/
├── health-and-fitness/
├── linux/
├── physics/
├── README.md
├── software-development/
└── writing/
```

</details>

<details>
<summary><b>📁 Skills/</b> <i>(Anthropic official, session handoff, research, etc.)</i></summary>

```text
Skills/
├── audit-and-instruct.md
├── comprehensive-data-analysis/
├── GAP_prompting_skill/
├── official-anthropic-skills/
├── pdf/
├── rigorous_research/
├── session_handoff_skill/
└── SKILL_TEMPLATE_v1.0_20260822/
```

</details>

<details>
<summary><b>📁 Standards/</b> <i>(Agentic, APEX, Architecture, NASA, Research, Templates)</i></summary>

```text
Standards/
├── Agentic/
│   ├── AI_AGENT_INTERACTION_...
│   ├── DOCUMENTATION_STANDARD_...
│   ├── ENGINEERING_SOFTWARE_...
│   ├── PROMPT_TEMPLATE_STANDARD_...
│   ├── RESEARCH_AND_EVIDENCE_...
│   ├── SKILL_STANDARD_...
│   └── WRITING_STYLE_STANDARD_...
├── APEX/
├── Architecture/
├── NASA/
├── README.md
├── Research/
└── Templates/
```

</details>

<details>
<summary><b>📁 Templates/</b> <i>(Orchestra, Curriculum, Novel Workflow, VDM Analysis)</i></summary>

```text
Templates/
├── 00_Critique_Report_Template/
├── EXPERT_CURRICULUM_TEMPLATE_v1.0_20260821/
├── NOVEL_WORKFLOW_TEMPLATE_v1.0_20260821/
├── ORCHESTRA_PUBLICATION_PACKAGE_TEMPLATE_v2.0_20260804/
├── ORCHESTRA_RESEARCH_PACKAGE_TEMPLATE_v2.0_20260804/
├── review-ready-lean-template/
├── SKILL_TEMPLATE_v1.0_20260822/
└── vdm_analysis_template_.../
```

</details>

---

<details>
<summary><b>📄 Root Files</b> <i>(README, LICENSE, VERSION, etc.)</i></summary>

```text
├── install.py
├── LICENSE
├── README.md
├── REPOSITORY_MAP.md
└── VERSION
```

</details>

## Design rule

**Meaning first, representation second.** A person browsing the repository should start from the kind of artifact they need. Runtime and serialization variants remain available without dominating the top-level structure.

Historical names are preserved in Git history and this map. The application index is disposable and can always be rebuilt from these files.
