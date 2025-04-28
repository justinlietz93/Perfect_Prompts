Code Comment Standards
This document outlines the standards for code comments across all projects. Following these guidelines ensures consistency, clarity, and maintainability.

1. File Header Comments
File headers must use the following format:

/***********************************************************************************
 * Path: [relative path from the repository root]
 * Description: [brief description of the file purpose]
 *
 * Change Date    Developer                    Reason
 * YYYY/MM/DD     [Developer Name]             Created
 * YYYY/MM/DD     [Developer Name]             [Change reason]
 *
 * Examples: [Optional: example usage or important considerations for use]
 ************************************************************************************/

One block at the top of each file with no repeats
Maintain all history entries with consistent spacing
Description should concisely explain the file's purpose

2. Class and Interface Summaries
Place a single XML summary comment immediately above each class/interface declaration:

/// <summary>
/// [Imperative verb phrase describing the class purpose]
/// </summary>
public class ClassName { }
Use imperative voice (e.g., "Processes," "Manages," "Represents")
Keep under 10 words when possible
Avoid implementation details; focus on purpose

3. Method and Function Summaries
Use XML documentation format for method summaries:

/// <summary>
/// [Imperative phrase describing what the method does]
/// </summary>
public void MethodName() { }
Use imperative voice (e.g., "Calculates," "Retrieves," "Updates")
Focus on what the method does, not how it does it
Keep to one line unless absolutely necessary
Omit redundant phrases like "This method..." or "Method that..."

4. Property Comments
Add comments only for non-obvious properties:

/// <summary>Gets or sets the authentication token</summary>
public string Token { get; set; }
Use XML format or inline comments as appropriate
Start with verb
Keep under 12 words

5. Inline Comments
Use sparingly and only for non-trivial logic:

// calculate hash after user object is populated
var hash = ComputeHash(user);
Start with verb in present tense
Brief note (under 12 words)
Place directly above the relevant code line
Avoid obvious comments that repeat what the code clearly does

6. TODO/FIXME Tags
Format consistently with uppercase tags:

// TODO: handle null password case
// FIXME: race condition in concurrent access
Always use uppercase for TODO and FIXME keywords
Include brief note on what needs to be done
Prefer specific details over vague statements

7. General Guidelines
Direct & Concise: Avoid fluffy language and redundancy
Present Tense: Use present tense verbs in all comments
Imperative Voice: Phrase comments as commands or statements
Consistency: Maintain consistent style throughout codebase
Format: Preserve proper indentation and alignment
Remove: Delete commented-out code, obsolete comments, and redundant explanations

Maintain consistent style throughout the codebase