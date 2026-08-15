<img width="1774" height="887" alt="perfect-prompts-banner" src="https://github.com/user-attachments/assets/2ef86d9f-a64f-40e8-a9ad-fc4593ccb3b7" />

# Perfect Prompts

A working corpus of prompt engineering, context engineering, agent control, AI-assisted software development, research methodology, and reusable LLM tooling.

Despite the name, this repository has grown far beyond a collection of prompts. It contains prompt harnesses, agent instruction files, architecture and engineering standards, research protocols, reusable skills, context builders, personas, rulesets, structured templates, and multiple generations of experiments developed through active use.

This is a working repository, not a polished prompt pack.

## Repository Status

This repository has grown organically over time, and its current structure reflects that history.

I do intend to clean up, consolidate, and reorganize it eventually, but that is not a priority at the moment. Expect parallel implementations across languages and formats, historical generations, inconsistent naming, experimental material, and files at different levels of maturity. Many apparently duplicated artifacts are intentional: prompts are often embedded directly in language-specific source files so they can be reused without translation into another representation.

That is intentional for now. I would rather preserve useful work and the evolution of ideas than spend time prematurely normalizing the entire repository.

Do not assume every file is canonical or represents my current preferred approach. Some files are current tools, some are reusable references, and some are retained because they document earlier approaches or useful experiments.

## What Is In This Repository?

The repository currently includes several overlapping kinds of material.

### Prompt and Agent Harnesses

Reusable prompts for tasks such as:

* agent and multi-agent design
* project scaffolding
* task, phase, and step generation
* reasoning and analysis
* critique and review
* rewriting and style extraction
* citation handling
* mathematical formatting
* Mermaid diagram generation
* request decomposition
* next-step generation
* deep research
* session recovery and handoff
* context synthesis and persistence

Many prompt families exist in multiple representations so they can be copied directly, imported into applications, or adapted to different agent runtimes.

### Multi-Language Prompt Implementations

Several prompt collections are implemented in parallel across:

* Python
* TypeScript
* Rust
* Go
* plaintext
* JSON
* structured Markdown and related formats

The language implementations are useful when prompts need to live directly inside application code rather than being maintained as detached text files.

### Agent Instruction Files

The repository contains instruction sets intended to govern how autonomous or semi-autonomous coding and reasoning agents operate.

Examples include:

* `AGENTS_library/No-Assumptions_AGENTS.md`
* `Methodologies/Germinal_Theory/Emergence_Based_Design_AGENTS.md`
* tool-specific agent/persona formats for systems such as GitHub Copilot and Roo Code

These files focus less on one-shot prompting and more on persistent behavioral constraints, architecture discipline, evidence requirements, and reliable execution.

### Methodologies

The `Methodologies/` directory contains higher-level approaches for designing interactions with AI systems.

#### Guided Autonomy Prompting

`Methodologies/Guided_Autonomy_Prompting/`

Guided Autonomy Prompting is built around providing the model with clear constraints, goals, invariants, and reasons while avoiding unnecessary implementation micromanagement. The intent is to preserve useful model autonomy without sacrificing correctness or control.

The repository currently includes domain-agnostic and physics-oriented variants.

#### Germinal Theory / Emergence-Based Design

`Methodologies/Germinal_Theory/`

This material explores architecture and agent guidance based on discovering structure from the actual problem rather than imposing a preferred design pattern in advance.

The associated AGENTS file is designed to make an agent inspect evidence, constraints, existing structure, and failure modes before introducing architecture.

### Architecture and Engineering Standards

`STANDARDS_REPOSITORY/`

This area contains software architecture, implementation, documentation, testing, research, and engineering standards.

Architecture material currently includes:

* Clean Architecture
* Hexagonal Architecture
* Microservices
* Event-Driven Architecture
* Lite Event-Driven Architecture
* Serverless Architecture
* MVC
* Three-Tier Architecture
* Layered Monolith
* Dual-Plane Architecture
* Emergence-Based Architecture
* SGDA documentation architecture
* SGHM architecture

The standards repository also contains:

* Apex software compliance standards
* NASA-derived software standards and source documents
* prompt templates
* research and publication standards
* figure and presentation standards
* critique templates
* arXiv-oriented paper templates
* Lean-oriented review material

### Research and Reasoning Rules

`rules/`

This is a broad collection of reusable instruction sets for technical and scientific reasoning.

Topics include:

* formal logic and discrete mathematics
* rigorous mathematical inquiry
* technical and logical discourse
* objective decision making and truth seeking
* systems thinking
* Bayesian reasoning
* probability and information theory
* machine learning
* classical mechanics
* quantum field theory
* solid-state physics
* experimental physics and statistical analysis
* Linux system management
* software development
* technical writing
* cross-domain scientific reasoning

These are typically intended to be inserted into a system prompt, agent context, research workflow, or review process when a task needs stronger domain-specific constraints.

### Personas

`PERSONAS/`

The persona library contains specialized AI roles for software engineering, data analysis, mathematics, physics, formal logic, research, project orchestration, creative work, systems reasoning, and other domains.

Several personas are represented in multiple formats, including:

* Markdown
* YAML
* JSON
* XML
* Roo Code persona formatting
* GitHub Copilot agent formatting

The goal is portability across different model and agent environments rather than dependence on a single provider.

### Skills

`skills/`

The repository also contains reusable skill packages and skill definitions for more complete workflows.

Current examples include:

* Guided Autonomy Prompting
* rigorous research
* comprehensive data analysis
* session handoff and state preservation
* PDF work
* audit-and-instruct workflows
* README generation
* visual game asset creation

Unlike a simple prompt, these may define procedures, supporting files, schemas, validation steps, or expected outputs.

### Context Builders and Session State

Several files focus on preserving and reconstructing context across long-running work.

Examples include:

* Universal Context Synthesis Engine material
* session state persistence protocols
* session handoff prompts
* session handoff skills
* active-state snapshots and context packaging

These are intended for workflows where the important problem is not merely generating an answer, but preserving decisions, constraints, rejected paths, unresolved questions, and working state across agents or sessions.

## Repository Map

```text
Perfect_Prompts/
├── AGENTS_library/          # Reusable agent instruction files
├── Methodologies/           # Higher-level prompting and architecture methods
├── PERSONAS/                # Domain-specific personas in multiple formats
├── STANDARDS_REPOSITORY/    # Architecture, engineering, prompt, and research standards
├── general_guidelines/      # Cross-cutting reasoning and truth-seeking guidance
├── go/                      # Go prompt harnesses and examples
├── json/                    # Structured prompt/context data
├── plaintext/               # Plaintext prompts and templates
├── python/                  # Python prompt harnesses and examples
├── rules/                   # Scientific, technical, mathematical, and domain rulesets
├── rust/                    # Rust prompt harnesses and examples
├── skills/                  # Reusable agent/LLM skill packages
├── structured_text/         # Structured context-builder prompts
├── submodules/              # Additional prompt-library references
└── typescript/              # TypeScript prompt harnesses and examples
```

## How I Use This Repository

This repository is primarily a source library.

Typical use looks like:

1. Find a prompt, ruleset, persona, methodology, or standard relevant to the task.
2. Copy or import the useful parts into the target agent or application.
3. Combine it with project-specific context and constraints.
4. Modify it based on observed model behavior.
5. Preserve useful revisions or new variants here.

For agentic work, I generally treat prompts as part of the system architecture rather than as isolated strings. Instructions, context, tools, state, validation, handoff behavior, and implementation constraints all interact.

That is why this repository contains much more than conventional prompt templates.

## Choosing What To Use

There is no single "best prompt" in this repository.

Different materials solve different problems:

* Use `plaintext/` when you want something easy to inspect or paste directly.
* Use `python/`, `typescript/`, `rust/`, or `go/` when the prompt should live inside application code.
* Use `AGENTS_library/` or methodology-specific AGENTS files for persistent agent behavior.
* Use `rules/` when a task needs strong reasoning or domain constraints.
* Use `PERSONAS/` when role specialization is useful.
* Use `STANDARDS_REPOSITORY/` when the work needs architecture, engineering, publication, or review standards.
* Use `skills/` when the task requires a reusable multi-step procedure rather than a single prompt.
* Use context-builder and session-handoff material for long-running work where preserving state matters.

When multiple versions exist, inspect them rather than assuming the newest-looking filename is automatically the best fit.

## Cloning

Some additional prompt libraries are referenced as Git submodules.

```bash
git clone --recurse-submodules https://github.com/justinlietz93/Perfect_Prompts.git
```

If you already cloned the repository without submodules:

```bash
git submodule update --init --recursive
```

## Related Repositories

* [AI Content Suite](https://github.com/justinlietz93/AI-Content-Suite) - Browser-based AI context engineering platform.
* [Cogito Research](https://github.com/justinlietz93/Cogito.git) - Deep research tooling and agent workflows.
* [_Neuroca](https://github.com/Neuroca-Inc/_Neuroca) - Dynamic memory architecture for LLM systems.
* [Modular Utilities](https://github.com/justinlietz93/Modular_Utilities) - Modular tools and CLIs for extracting, transforming, and loading file-based data.

## Contributions

Issues and pull requests are welcome when they add something useful, fix a concrete problem, improve technical accuracy, or contribute a materially better formulation.

Because this repository is also a working archive, cleanup for its own sake is not necessarily an improvement. Changes should preserve useful history unless there is a clear reason to remove it.

## License

This repository is available under the MIT License. See [LICENSE](LICENSE) for details.

---

The repository started as a place to keep good prompts. It has gradually become a broader archive of practical methods for controlling, constraining, specializing, auditing, and transferring state between AI systems.
