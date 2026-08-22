---
name: second-opinion
description: Second Opinion from Codex and Gemini CLI for Claude Code 
---

# Second Opinion

When invoked:

1. **Summarize the problem** from conversation context (~100 words)

2. **Spawn both subagents in parallel** using Task tool:
   - `gemini-consultant` with the problem summary
   - `codex-consultant` with the problem summary

3. **Present combined results** showing:
   - Gemini's perspective
   - Codex's perspective  
   - Where they agree/differ
   - Recommended approach

## CLI Commands Used by Subagents

```bash
gemini -p "I'm working on a coding problem... [problem]"
codex exec "I'm working on a coding problem... [problem]"
```
