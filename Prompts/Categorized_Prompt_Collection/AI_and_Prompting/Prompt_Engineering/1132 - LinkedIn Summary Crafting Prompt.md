# LinkedIn Summary Crafting Prompt

## Author
Scott M.

## Goal
The goal of this prompt is to guide an AI in creating a personalized, authentic LinkedIn "About" section (summary) that effectively highlights a user's unique value proposition, aligns with targeted job roles and industries, and attracts potential employers or recruiters. It aims to produce output that feels human-written, avoids AI-generated clichés, and incorporates best practices for LinkedIn in 2025–2026, such as concise hooks, quantifiable achievements, and subtle calls-to-action. Enhanced to intelligently use attached files (resumes, skills lists) and public LinkedIn profile URLs for auto-filling details where relevant. All drafts must respect the current About section limit of 2,600 characters (including spaces); aim for 1,500–2,000 for best engagement.

## Audience
This prompt is designed for job seekers, professionals transitioning careers, or anyone updating their LinkedIn profile to improve visibility and job prospects. It's particularly useful for mid-to-senior level roles where personalization and storytelling can differentiate candidates in competitive markets like tech, finance, or manufacturing.

## Changelog
- Version 1.0: Initial prompt with basic placeholders for job title, industry, and reference summaries.
- Version 1.1: Converted to interview-style format for better customization; added instructions to avoid AI-sounding language and incorporate modern LinkedIn best practices.
- Version 1.2: Added documentation elements (goal, audience); included changelog and author; added supported AI engines list.
- Version 1.3: Minor hardening — added subtle blending instruction for references, explicit keyword nudge, tightened anti-cliché list based on 2025–2026 red flags.
- Version 1.4: Added support for attached files (PDF resumes, Markdown skills, etc.); instruct AI to search attachments first and propose answers to relevant questions (#3–5 especially) before asking user to confirm.
- Version 1.5: Added Versioning & Adaptation Note; included sample before/after example; added explicit rule: "Do not generate drafts until all key questions are answered/confirmed."
- Version 1.6: Added support for user's public LinkedIn profile URL (Question 9); instruct AI to browse/summarize visible public sections if provided, propose alignments/improvements, but only use public data.
- Version 1.7: Added awareness of 2,600-character limit for About section; require character counts in drafts; added post-generation instructions for applying the update on LinkedIn.

## Versioning & Adaptation Note
This prompt is iterated specifically for high-context models with strong reasoning, file-search, and web-browsing capabilities (Grok 4, Claude 3.5/4, GPT-4o/4.1 with browsing).  
For smaller/older models: shorten anti-cliché list, remove attachment/URL instructions if no tools support them, reduce questions to 5–6 max.  
Always test output with an AI detector or human read-through. Update Changelog for changes. Fork for industry tweaks.

## Supported AI Engines (Best to Worst)
- Best: Grok 4 (strong file/document search + browse_page tool for URLs), GPT-4o (creative writing + browsing if enabled).
- Good: Claude 3.5 Sonnet / Claude 4 (structured prose + browsing), GPT-4 (detailed outputs).
- Fair: Llama 3 70B (nuance but limited tools), Gemini 1.5 Pro (multimodal but inconsistent tone).
- Worst: GPT-3.5 Turbo (generic responses), smaller LLMs (poor context/tools).

## Prompt Text

I want you to help me write a strong LinkedIn "About" section (summary) that's aimed at landing a [specific job title you're targeting, e.g., Senior Full-Stack Engineer / Marketing Director / etc.] role in the [specific industry, e.g., SaaS tech, manufacturing, healthcare, etc.].

Make it feel like something I actually wrote myself—conversational, direct, with some personality. Absolutely no over-the-top corporate buzzwords (avoid "synergy", "leverage", "passionate thought leader", "proven track record", "detail-oriented", "game-changer", etc.), no unnecessary em-dashes, no "It's not X, it's Y" structures, no "In today's world…" openers, and keep sentences varied in length like real people write. Blend any reference styles subtly—don't copy phrasing directly. Include relevant keywords naturally (pull from typical job descriptions in your target role if helpful). Aim for 4–7 short paragraphs that hook fast in the first 2–3 lines (since that's what shows before "See more").

**Important rules:**
- If the user has attached any files (resume PDF, skills Markdown, text doc, etc.), first search them intelligently for relevant details (experience, roles, achievements, years, wins, skills) and use that to propose or auto-fill answers to questions below where possible. Then ask for confirmation or missing info—don't assume everything is 100% accurate without user input.
- If the user provides their LinkedIn profile URL, use available browsing/fetch tools to access the public version only. Summarize visible sections (headline, public About, experience highlights, skills, etc.) and propose how it aligns with target role/answers or suggest improvements. Only use what's publicly visible without login — confirm with user if data seems incomplete/private.
- Do not generate any draft summaries until the user has answered or confirmed all relevant questions (especially #1–7) and provided clarifications where needed. If input is incomplete, politely ask for the missing pieces first.
- Respect the LinkedIn About section limit: maximum 2,600 characters (including spaces, line breaks, emojis). Provide an approximate character count for each draft. If a draft exceeds or nears 2,600, suggest trims or prioritize key content.

To make this spot-on, answer these questions first so you can tailor it perfectly (reference attachments/URL where they apply):

1. What's the exact job title (or 1–2 close variations) you're going after right now?

2. Which industry or type of company are you targeting (e.g., fintech startups, established manufacturing, enterprise software)?

3. What's your current/most recent role, and roughly how many years of experience do you have in this space? (If attachments/LinkedIn URL cover this, propose what you found first.)

4. What are 2–3 things that make you different or really valuable? (e.g., "I cut deployment time 60% by automating pipelines", "I turned around underperforming teams twice", "I speak fluent Spanish and have led LATAM expansions", or even a quirk like "I geek out on optimizing messy legacy code") — Pull strong examples from attachments/URL if present.

5. Any big, specific wins or results you're proud of? Numbers help a ton (revenue impact, % improvements, team size led, projects shipped). — Extract quantifiable achievements from resume/attachments/URL first if available.

6. What's your tone/personality vibe? (e.g., straightforward and no-BS, dry humor, warm/approachable, technical nerd, builder/entrepreneur energy)

7. Are you actively job hunting and want to include a subtle/open call-to-action (like "Open to new opportunities in X" or "DM me if you're building cool stuff in Y")?

8. Paste 2–4 LinkedIn About sections here (from people in similar roles/industries) that you like the style of—or even ones you don't like, so I can avoid those pitfalls.

9. (Optional) What's your current LinkedIn profile URL? If provided, I'll review the public version for headline, About, experience, skills, etc., and suggest how to build on/improve it for your target role.

Once I have your answers (and any clarifications from attachments/URL), I'll draft 2 versions: one shorter (~150–250 words / ~900–1,500 chars) and one fuller (~400–500 words / ~2,000–2,500 chars max to stay safely under 2,600). Include approximate character counts for each. You can mix and match from them.

**After providing the drafts:**
Always end with clear instructions on how to apply/update the About section on LinkedIn, e.g.:
"To update your About section:
1. Go to your LinkedIn profile (click your photo > View Profile).
2. Click the pencil icon in the About section (or 'Add profile section' > About if empty).
3. Paste your chosen draft (or blended version) into the text box.
4. Check the character count (LinkedIn shows it live; max 2,600).
5. Click 'Save' — preview how the first lines look before "See more".
6. Optional: Add line breaks/emojis for formatting, then save again.
Refresh the page to confirm it displays correctly."
