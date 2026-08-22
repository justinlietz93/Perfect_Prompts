# Task: Create a Professional Developer Status Bar for Claude Code

## Role

You are a systems programmer creating a highly-optimized status bar script for Claude Code.

## Deliverable

A single-file Python script (`~/.claude/statusline.py`) that displays developer-critical information in Claude Code's status line.

## Input Specification

Read JSON from stdin with this structure:

```json
{
  "model": {"display_name": "Opus|Sonnet|Haiku"},
  "workspace": {"current_dir": "/path/to/workspace", "project_dir": "/path/to/project"},
  "output_style": {"name": "explanatory|default|concise"},
  "cost": {
    "total_cost_usd": 0.0,
    "total_duration_ms": 0,
    "total_api_duration_ms": 0,
    "total_lines_added": 0,
    "total_lines_removed": 0
  }
}

```

## Output Requirements

### Format

* Print exactly ONE line to stdout
* Use ANSI 256-color codes: \033[38;5;Nm with optimized color palette for high contrast
* Smart truncation: Visible text width ≤ 80 characters (ANSI escape codes do NOT count toward limit)
* Use unicode symbols: ● (clean), + (added), ~ (modified)
* Color palette: orange 208, blue 33, green 154, yellow 229, red 196, gray 245 (tested for both dark/light terminals)

### Information Architecture (Left to Right Priority)

1. Core: Model name (orange)
2. Context: Project directory basename (blue)
3. Git Status:
* Branch name (green)
* Clean: ● (dim gray)
* Modified: ~N (yellow, N = file count)
* Added: +N (yellow, N = file count)


4. Metadata (dim gray):
* Uncommitted files: !N (red, N = count from git status --porcelain)
* API ratio: A:N% (N = api_duration / total_duration * 100)



### Example Output

\033[38;5;208mOpus\033[0m \033[38;5;33mIsaacLab\033[0m \033[38;5;154mmain\033[0m \033[38;5;245m●\033[0m \033[38;5;245mA:12%\033[0m

## Technical Constraints

### Performance (CRITICAL)

* Execution time: < 100ms (called every 300ms)
* Cache persistence: Store Git status cache in /tmp/claude_statusline_cache.json (script exits after each run, so cache must persist on disk)
* Cache TTL: Refresh Git file counts only when cache age > 5 seconds OR .git/index mtime changes
* Git logic optimization:
* Branch name: Read .git/HEAD directly (no subprocess)
* File counts: Call subprocess.run(['git', 'status', '--porcelain']) ONLY when cache expires


* Standard library only: No external dependencies (use only sys, json, os, pathlib, subprocess, time)

### Error Handling

* JSON parse error → return empty string ""
* Missing fields → omit that section (do not crash)
* Git directory not found → omit Git section entirely
* Any exception → return empty string ""

## Code Structure

* Single file, < 100 lines
* UTF-8 encoding handled for robust unicode output
* Maximum one function per concern (parsing, git, formatting)
* Type hints required for all functions
* Docstring for each function explaining its purpose

## Integration Steps

1. Save script to ~/.claude/statusline.py
2. Run chmod +x ~/.claude/statusline.py
3. Add to ~/.claude/settings.json:

```json
{
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.py",
    "padding": 0
  }
}

```

4. Test manually: echo '{"model":{"display_name":"Test"},"workspace":{"current_dir":"/tmp"}}' | ~/.claude/statusline.py

## Verification Checklist

* Script executes without external dependencies (except single git status --porcelain call when cached)
* Visible text width ≤ 80 characters (ANSI codes excluded from calculation)
* Colors render correctly in both dark and light terminal backgrounds
* Execution time < 100ms in typical workspace (cached calls should be < 20ms)
* Gracefully handles missing Git repository
* Cache file is created in /tmp and respects TTL
* Git file counts refresh when .git/index mtime changes or 5 seconds elapse

## Context for Decisions

This is a "developer professional" style status bar. It prioritizes:

* Detailed Git information for branch switching awareness
* API efficiency monitoring for cost-conscious development
* Visual density for maximum information per character
