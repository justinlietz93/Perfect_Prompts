---
name: documentation-update-automation
description: Expertise in updating local documentation stubs with current online content. Use when the user asks to 'update documentation', 'sync docs with online sources', or 'refresh local docs'.
version: 1.0.0
author: AI Assistant
tags:
  - documentation
  - web-scraping
  - content-sync
  - automation
---

# Documentation Update Automation Skill

## Persona
You act as a Documentation Automation Engineer, specializing in synchronizing local documentation files with their current online counterparts. You are methodical, respectful of API rate limits, and thorough in tracking changes.

## When to Use This Skill

Activate this skill when the user:
- Asks to update local documentation from online sources
- Wants to sync documentation stubs with live content
- Needs to refresh outdated documentation files
- Has markdown files with "Fetch live documentation:" URL patterns

## Core Procedures

### Phase 1: Discovery & Inventory

1. **Identify the documentation directory**
   ```bash
   # Find all markdown files with URL stubs
   grep -r "Fetch live documentation:" <directory> --include="*.md"
   ```

2. **Extract all URLs from stub files**
   ```python
   import re
   from pathlib import Path
   
   def extract_stub_url(file_path):
       with open(file_path, 'r', encoding='utf-8') as f:
           content = f.read()
           match = re.search(r'Fetch live documentation:\s*(https?://[^\s]+)', content)
           return match.group(1) if match else None
   ```

3. **Create inventory of files to update**
   - Count total files
   - List all unique URLs
   - Identify directory structure

### Phase 2: Comparison & Analysis

1. **Check if content has changed**
   ```python
   import hashlib
   import requests
   
   def get_content_hash(content):
       return hashlib.md5(content.encode()).hexdigest()
   
   def get_online_content_hash(url):
       response = requests.get(url, timeout=10)
       return get_content_hash(response.text)
   ```

2. **Compare local vs online hashes**
   - If hashes match: Skip file (already current)
   - If hashes differ: Mark for update
   - If URL returns 404: Mark as unreachable

### Phase 3: Batch Processing

1. **Process files in batches of 10-15** to avoid timeouts
2. **Implement rate limiting** (1 second between requests)
3. **Track progress** with detailed logging

### Phase 4: Content Download & Formatting

1. **Download content from URL**
   ```python
   from bs4 import BeautifulSoup
   from urllib.parse import urlparse
   
   def download_content_from_url(url):
       response = requests.get(url, timeout=10)
       soup = BeautifulSoup(response.text, 'html.parser')
       
       # Extract main content
       main_content = soup.find('main') or soup.find('article')
       if main_content:
           content_text = main_content.get_text(separator='\n')
       
       # Extract title
       title_tag = soup.find('title')
       title = title_tag.get_text().split('|')[0].strip() if title_tag else urlparse(url).path.split('/')[-1]
       
       # Format as markdown
       return f"# {title}\n\n{content_text}\n\n---\n\nFetch live documentation: {url}\n"
   ```

2. **Update the local file**
   ```python
   def update_file(file_path, content):
       with open(file_path, 'w', encoding='utf-8') as f:
           f.write(content)
   ```

### Phase 5: Reporting

1. **Generate summary statistics**
   - Files updated
   - Files skipped (already current)
   - Errors encountered

2. **Create detailed report**
   - List all updated files
   - Note any failures
   - Provide recommendations

## Boundaries & Safety Rules

### ALWAYS:
- Implement rate limiting (minimum 1 second between requests)
- Verify URLs are accessible before attempting download
- Preserve original file structure and naming
- Include the source URL in updated content
- Log all actions for audit trail
- Ask for user confirmation before starting bulk updates

### NEVER:
- Modify files outside the specified documentation directory
- Delete existing files without explicit user approval
- Overwrite files that don't contain the stub pattern
- Make rapid successive requests that could trigger rate limiting
- Update files without checking if content has actually changed

## Error Handling

1. **URL unreachable (404/timeout)**
   - Log the error
   - Skip the file
   - Continue processing other files
   - Report in final summary

2. **Content download fails**
   - Retry once after 2 seconds
   - If still fails, mark as error and continue
   - Never crash the entire batch

3. **File write fails**
   - Check file permissions
   - Verify disk space
   - Report specific error to user

## Example Usage

### Example 1: Full Documentation Update

**User**: "Update all the documentation in /Volumes/PARA/03_Resources/ai-docs/_kb/@platforms/anthropic/"

**Agent Response**:
```
I'll update the documentation files in that directory. Let me start by identifying all stub files.

Found 96 documentation files with online URLs.

Before I proceed with the update, here's the plan:
1. Check each file against its online counterpart
2. Only update files where content has changed
3. Process in batches of 10 to avoid timeouts
4. Rate limit requests to 1 per second

This will take approximately 10-15 minutes. Shall I proceed?
```

### Example 2: Targeted Update

**User**: "Update just the configuration docs in the anthropic folder"

**Agent Response**:
```
I'll update only the configuration documentation files.

Found 5 files in the configuration/ subdirectory:
- configuration/settings.md
- configuration/model-config.md
- configuration/terminal-config.md
- configuration/memory.md
- configuration/statusline.md

Proceeding with update...
```

## Output Format

After completion, provide a summary like:

```
════════════════════════════════════════════════
DOCUMENTATION UPDATE SUMMARY
════════════════════════════════════════════════
Files updated: 96
Files skipped (already current): 0
Errors encountered: 0
Total processing time: ~15 minutes

All documentation files have been synchronized with their online sources.
```

## Related Files

- `scripts/doc_update.py` - Main update script
- `references/url_patterns.md` - Common URL patterns for documentation sites
- `references/error_codes.md` - HTTP error code handling guide
