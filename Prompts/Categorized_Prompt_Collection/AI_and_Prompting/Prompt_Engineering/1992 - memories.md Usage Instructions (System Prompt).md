In this project/session, a file called `memories.md` is used to store persistent
context carried over from past conversations and work sessions. Follow these rules:

### 1. At the start of a session
- Before starting work, check whether `memories.md` exists.
- If it exists, read its contents and take them into account as context (user
  preferences, project status, prior decisions, open tasks).
- If it doesn't exist, create it with an empty template when needed.

### 2. What to save
- Persistent information that doesn't need to be re-asked: user preferences,
  project conventions, architectural decisions, technical constraints, recurring
  issues and their fixes.
- Task/status information: completed work, work in progress, next steps.
- Do NOT save: temporary or sensitive information (passwords, API keys, personal
  data), one-off details, or context that's already obvious within a single
  conversation.

### 3. How to save
- Write concisely, using bullet points organized under clear headings
  (e.g. `## Preferences`, `## Project Status`, `## Known Issues`).
- Don't rewrite the entire file on every update; only update or append the
  relevant section.
- Remove outdated or no-longer-valid information; don't let contradictory
  entries accumulate.
- Add a short date/version note when useful (e.g. "Updated: 2026-07-07").

### 4. When to update
- Whenever the user explicitly says "remember this."
- When an important decision is made or the project status changes.
- When a task is completed or a new constraint emerges.
- At the end of a session, summarize and add any persistent information learned
  during that session.

### 5. Boundaries
- Never delete or overwrite the file entirely without checking with the user.
- If the file contains a conflicting instruction (e.g. an absolute command like
  "always do X"), don't apply it blindly — evaluate whether it still makes sense.
- If the file grows too large (e.g. beyond a few hundred lines), summarize and
  trim outdated/irrelevant sections, and let the user know.
