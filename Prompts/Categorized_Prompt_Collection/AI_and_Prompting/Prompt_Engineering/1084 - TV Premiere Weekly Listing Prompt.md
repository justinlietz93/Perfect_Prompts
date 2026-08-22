### TV Premieres & Returning Seasons Weekly Listings Prompt (v3.1 – Balanced Emphasis)

**Author:** Scott M (tweaked with Grok assistance)  
**Goal:**  
Create a clean, user-friendly summary of TV shows premiering or returning — including new seasons starting, series resuming after a hiatus/break, and brand-new series premieres — plus new movies releasing to streaming services in the upcoming week. Highlight both exciting comebacks and fresh starts so users can plan for all the must-watch drops without clutter.

**Supported AIs (sorted by ability to handle this prompt well – from best to good):**  
1. Grok (xAI) – Excellent real-time updates, tool access for verification, handles structured tables/formats precisely.  
2. Claude 3.5/4 (Anthropic) – Strong reasoning, reliable table formatting, good at sourcing/summarizing schedules.  
3. GPT-4o / o1 (OpenAI) – Very capable with web-browsing plugins/tools, consistent structured outputs.  
4. Gemini 1.5/2.0 (Google) – Solid for calendars and lists, but may need prompting for separation of tables.  
5. Llama 3/4 variants (Meta) – Good if fine-tuned or with search; basic versions may require more guidance on format.

**Changelog:**  
- v1.0 (initial) – Basic table with Date, Name, New/Returning, Network/Service.  
- v1.1 – Added Genre column; switched to separate tables per day with date heading for cleaner layout (no Date column).  
- v1.2 – Added this structured header (title, author, goal, supported AIs, changelog); minor wording tweaks for clarity and reusability.  
- v1.3 – Fixed date range to look forward 7 days from current date automatically.  
- v2.0 – Expanded to include movies releasing to streaming services; added Type column to distinguish TV vs Movie content.  
- v3.0 – Shifted primary focus to returning TV shows (new seasons or restarts after breaks); de-emphasized brand-new series premieres while still including them.  
- v3.1 – Balanced emphasis: Treat new series premieres and returning seasons/restarts as equally important; removed any prioritization/de-emphasis language; updated goal/instructions for symmetry.

**Prompt Instructions:**

List TV shows premiering or returning (new seasons starting, series resuming from hiatus/break, and brand-new series premieres), plus new movies releasing to streaming services in the next 7 days from today's date forward.

Organize the information with a separate markdown table for each day that has at least one notable premiere/return/release. Place the date as a level-3 heading above each table (e.g., ### February 6, 2026). Skip days with no major activity—do not mention empty days.

Use these exact columns in each table:  
- Name  
- Type (either 'TV Show' or 'Movie')  
- New or Returning (for TV: use 'Returning - Season X' for new seasons/restarts after break, e.g., 'Returning - Season 4' or 'Returning after hiatus - Season 2'; use 'New' for brand-new series premieres; add notes like '(all episodes drop)' or '(Part 2 of season)' if applicable. For Movies: use 'New' or specify if it's a 'Theatrical → Streaming' release with original release date if notable)  
- Network/Service  
- Genre (keep concise, primary 1-3 genres separated by ' / ', e.g., 'Crime Drama / Thriller' or 'Action / Sci-Fi')

Focus primarily on major streaming services (Netflix, Disney+, Apple TV+, Paramount+, Hulu, Prime Video, Max, etc.), but include notable broadcast/cable premieres or returns if high-profile (e.g., major network dramas, reality competitions resuming). For movies, include theatrical films moving to streaming, original streaming films, and notable direct-to-streaming releases. Exclude limited theatrical releases not yet on streaming. Only include content that actually premieres/releases during that exact week—exclude trailers, announcements, or ongoing shows without a premiere/new season starting.

Base the list on the most up-to-date premiere schedules from reliable sources (e.g., Deadline, Hollywood Reporter, Rotten Tomatoes, TVLine, Netflix Tudum, Disney+ announcements, Metacritic, Wikipedia TV/film pages, JustWatch). If conflicting dates exist, prioritize official network/service announcements.

End the response with brief notes section covering:  
- Any important drop times (e.g., time zone specifics like 3AM ET / midnight PT),  
- Release style (full binge drop vs. weekly episodes vs. split parts for TV; theatrical window info for movies),  
- Availability caveats (e.g., regional restrictions, check platform for exact timing),  
- And a note that schedules can shift—always verify directly on the service.

If literally no major premieres, returns, or releases in the week, state so briefly and suggest checking a broader range or popular ongoing content.
