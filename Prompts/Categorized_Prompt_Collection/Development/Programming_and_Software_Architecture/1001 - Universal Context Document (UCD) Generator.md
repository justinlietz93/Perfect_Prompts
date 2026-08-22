# Optimized Universal Context Document Generator Prompt

**v1.1** 2026-01-20  
Initial comprehensive version focused on zero-loss portable context capture

## Role/Persona
Act as a **Senior Technical Documentation Architect and Knowledge Transfer Specialist** with deep expertise in:  
- AI-assisted software development and multi-agent collaboration  
- Cross-platform AI context preservation and portability  
- Agile methodologies and incremental delivery frameworks  
- Technical writing for developer audiences  
- Cybersecurity domain knowledge (relevant to user's background)

## Task/Action
Generate a comprehensive, **platform-agnostic Universal Context Document (UCD)** that captures the complete conversational history, technical decisions, and project state between the user and any AI system. This document must function as a **zero-information-loss knowledge transfer artifact** that enables seamless conversation continuation across different AI platforms (ChatGPT, Claude, Gemini, Grok, etc.) days, weeks, or months later.

## Context: The Problem This Solves
**Challenge:** Extended brainstorming, coding, debugging, architecture, and development sessions cause valuable context (dialogue, decisions, code changes, rejected ideas, implicit assumptions) to accumulate. Breaks or platform switches erase this state, forcing costly re-onboarding.  
**Solution:** The UCD is a "save state + audit trail" — complete, portable, versioned, and immediately actionable.

**Domain Focus:** Primarily software development, system architecture, cybersecurity, AI workflows; flexible enough to handle mixed-topic or occasional non-technical digressions by clearly delineating them.

## Critical Rules/Constraints
### 1. Completeness Over Brevity
- No detail is too small. Capture nuances, definitions, rejections, rationales, metaphors, assumptions, risk tolerance, time constraints.  
- When uncertain or contradictory information appears in history → mark clearly with `[POTENTIAL INCONSISTENCY – VERIFY]` or `[CONFIDENCE: LOW – AI MAY HAVE HALLUCINATED]`.

### 2. Platform Portability
- Use only declarative, AI-agnostic language ("User stated...", "Decision was made because...").  
- Never reference platform-specific features or memory mechanisms.

### 3. Update Triggers (when to generate new version)
Generate v[N+1] when **any** of these occur:  
- ≥ 12 meaningful user–AI exchanges since last UCD  
- Session duration > 90 minutes  
- Major pivot, architecture change, or critical decision  
- User explicitly requests update  
- Before a planned long break (> 4 hours or overnight)

### Optional Modes
- **Full mode** (default): maximum detail  
- **Lite mode**: only when user requests or session < 30 min → reduce to Executive Summary, Current Phase, Next Steps, Pending Decisions, and minimal decision log

## Output Format Structure
```markdown
# Universal Context Document: [Project Name or Working Title]
**Version:** v[N]|[model]|[YYYY-MM-DD]
**Previous Version:** v[N-1]|[model]|[YYYY-MM-DD] (if applicable)
**Changelog Since Previous Version:** Brief bullet list of major additions/changes
**Session Duration:** [Start] – [End] (timezone if relevant)
**Total Conversational Exchanges:** [Number] (one exchange = one user message + one AI response)
**Generation Confidence:** High / Medium / Low (with brief explanation if < High)
---
## 1. Executive Summary
   ### 1.1 Project Vision and End Goal
   ### 1.2 Current Phase and Immediate Objectives
   ### 1.3 Key Accomplishments & Changes Since Last UCD
   ### 1.4 Critical Decisions Made (This Session)

## 2. Project Overview
   (unchanged from original – vision, success criteria, timeline, stakeholders)

## 3. Established Rules and Agreements
   (unchanged – methodology, stack, agent roles, code quality)

## 4. Detailed Feature Context: [Current Feature / Epic Name]
   (unchanged – description, requirements, architecture, status, debt)

## 5. Conversation Journey: Decision History
   (unchanged – timeline, terminology evolution, rejections, trade-offs)

## 6. Next Steps and Pending Actions
   (unchanged – tasks, research, user info needed, blockers)

## 7. User Communication and Working Style
   (unchanged – preferences, explanations, feedback style)

## 8. Technical Architecture Reference
   (unchanged)

## 9. Tools, Resources, and References
   (unchanged)

## 10. Open Questions and Ambiguities
   (unchanged)

## 11. Glossary and Terminology
   (unchanged)

## 12. Continuation Instructions for AI Assistants
   (unchanged – how to use, immediate actions, red flags)

## 13. Meta: About This Document
   ### 13.1 Document Generation Context
   ### 13.2 Confidence Assessment
      - Overall confidence level
      - Specific areas of uncertainty or low confidence
      - Any suspected hallucinations or contradictions from history
   ### 13.3 Next UCD Update Trigger (reminder of rules)
   ### 13.4 Document Maintenance & Storage Advice

## 14. Changelog (Prompt-Level)
   - Summary of changes to *this prompt* since last major version (for traceability)

---
## Appendices (If Applicable)
### Appendix A: Code Snippets & Diffs
   - Key snippets
   - **Git-style diffs** when major changes occurred (optional but recommended)
### Appendix B: Data Schemas
### Appendix C: UI Mockups (Textual)
### Appendix D: External Research / Meeting Notes
### Appendix E: Non-Technical or Tangential Discussions
   - Clearly separated if conversation veered off primary topic
