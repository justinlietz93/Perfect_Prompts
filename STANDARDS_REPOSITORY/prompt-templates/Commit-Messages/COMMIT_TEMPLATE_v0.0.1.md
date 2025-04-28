# Commit Message Guidelines

This document outlines the rules and conventions for writing commit messages for this project. Following these guidelines ensures consistency and clarity in the version history.

## General Principles

- **Clarity and Conciseness:** Commit messages should be clear, concise, and easy to understand. Avoid jargon or overly complex vocabulary where simpler terms suffice.
- **Focus:** Each commit should ideally represent a single logical change. The message should accurately describe that change.

## Commit Message Structure

A commit message consists of a subject line and an optional body.

```text
<Project/Component>: <type>: <Short Description>

- <Detailed change 1>
- <Detailed change 2>
- ...
```

### 1. Subject Line

The subject line provides a brief summary of the change.

- **Project/Component Prefix:** Start with the name of the project or component affected, followed by a colon and a space companyinitials.solutionname.layeracronym.module
  (e.g., `MPAI.Doom.API.Test: `).
- **Type:** Indicate the type of change made. Common types include:
  - `feat:` (new feature)
  - `fix:` (bug fix)
  - `refactor:` (code change that neither fixes a bug nor adds a feature)
  - `style:` (changes that do not affect the meaning of the code - formatting, etc.)
  - `docs:` (documentation only changes)
  - `test:` (adding missing tests or correcting existing tests)
  - `chore:` (changes to the build process or auxiliary tools)
- **Description:** Write a short description of the change in the present tense (e.g., "add user login endpoint", "fix calculation error").
  - Use simple language.
  - Keep it concise.

**Example Subject Line:**

```text
AJI.Poker.BL.Models: refactor: updated model format and used file scoped namespaces
```

### 2. Body

The body is optional but recommended for commits that require more explanation than the subject line allows.

- **Bullet Points:** Use bullet points (starting with `- `) to detail specific changes.
- **Capitalization:** Start each bullet point with a lowercase letter, _unless_ it begins with a proper noun or a code object identifier (like a class name, method name, or file name).
- **Code Objects:** Enclose file names, class names, method names, variable names, or other code identifiers in backticks (`` ` ``). Example: `` `HealthPack.cs` ``, `` `Heal()` ``.
- **Hyphenation:** Avoid hyphenating compound words that describe concepts. Use spaces instead (e.g., "file scoped" instead of "file-scoped") or combine them if more appropriate ("filescoped" - though prefer the spaced version generally). Standard English hyphenation for compound adjectives before a noun is acceptable if necessary (e.g., "well-defined interface").
- **Conciseness:** Keep descriptions brief and to the point.

**Example Body:**

```text
- switched models to use file scoped namespaces
- updated header comments in model files
- applied consistent code formatting in models
- removed unused `GlobalUsings.cs` and `ModelTemplate.cs` files
- cleaned up whitespace in the `.csproj` file
```

## Example Complete Commit Message

```text
MPAI.Doom.BL.Models: refactor: updated model format and used file scoped namespaces

- switched models to use file scoped namespaces
- updated header comments in model files
- applied consistent code formatting in models
- removed unused `GlobalUsings.cs` and `ModelTemplate.cs` files
- cleaned up whitespace in the `.csproj` file
```
