Build a personal knowledge and narrative tool called "Thread" — a second brain that connects notes into a living story.

Core features:
- Note capture: fast input with title, body, tags, date, and an optional "life chapter" label (user-defined periods like "Building the company" or "Year in Berlin") — chapter labels create narrative structure
- Connection engine: [LLM API] periodically analyzes all notes and suggests thematic connections between entries. User sees a "Suggested connections" panel — accepts or rejects each. Accepted connections create bidirectional links
- Narrative timeline: a D3.js timeline showing notes grouped by chapter. Zoom out to decade view, zoom in to week view. Click any note to read it in context of its surrounding entries
- Weekly synthesis: every Sunday, AI generates a "week in review" paragraph from that week's notes — stored as a special entry in the timeline. Accumulates into a readable life chronicle
- Pattern report: monthly — AI identifies recurring themes (concepts mentioned 5+ times), most-linked ideas (high connection density), and "dormant" ideas (not referenced in 60+ days, surfaced as "worth revisiting")
- Chapter export: select any chapter by date range and export as a formatted PDF narrative document

Stack: React, [LLM API] for connection suggestions, synthesis, and pattern reports, D3.js for timeline visualization, localStorage with JSON export/import for backup. Literary design — serif fonts, generous whitespace.
