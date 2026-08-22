### Sports Events Weekly Listings Prompt (v1.0 – Initial Version)

**Author:** Scott M 
**Goal:**  
Create a clean, user-friendly summary of upcoming major sports events in the next 7 days from today's date forward. Include games, matches, tournaments, or key events across popular sports leagues (e.g., NFL, NBA, MLB, NHL, Premier League, etc.). Sort events by estimated popularity (based on general viewership metrics, fan base size, and cultural impact—e.g., prioritize football over curling). Indicate broadcast details (TV channels or streaming services) and translate event times to the user's local time zone (based on provided user info). Organize by day with markdown tables for quick planning, focusing on high-profile events without clutter from minor leagues or niche sports.

**Supported AIs (sorted by ability to handle this prompt well – from best to good):**  
1. Grok (xAI) – Excellent real-time updates, tool access for verification, handles structured tables/formats precisely.  
2. Claude 3.5/4 (Anthropic) – Strong reasoning, reliable table formatting, good at sourcing/summarizing schedules.  
3. GPT-4o / o1 (OpenAI) – Very capable with web-browsing plugins/tools, consistent structured outputs.  
4. Gemini 1.5/2.0 (Google) – Solid for calendars and lists, but may need prompting for separation of tables.  
5. Llama 3/4 variants (Meta) – Good if fine-tuned or with search; basic versions may require more guidance on format.

**Changelog:**  
- v1.0 (initial) – Adapted from TV Premieres prompt; basic table with Name, Sport, Broadcast, Local Time; sorted by popularity; includes broadcast and local time translation.

**Prompt Instructions:**

List upcoming major sports events (games, matches, tournaments) in the next 7 days from today's date forward. Focus on high-profile leagues and events (e.g., NFL, NBA, MLB, NHL, soccer leagues like Premier League or MLS, tennis Grand Slams, golf majors, UFC fights, etc.). Exclude minor league or amateur events unless exceptionally notable.

Organize the information with a separate markdown table for each day that has at least one notable event. Place the date as a level-3 heading above each table (e.g., ### February 6, 2026). Skip days with no major activity—do not mention empty days.

Sort events within each day's table by estimated popularity (descending order: use metrics like average viewership, global fan base, or cultural relevance—e.g., NFL games > NBA > curling events). Use these exact columns in each table:  
- Name (e.g., 'Super Bowl LV' or 'Manchester United vs. Liverpool')  
- Sport (e.g., 'Football / NFL' or 'Basketball / NBA')  
- Broadcast (TV channel or streaming service, e.g., 'ESPN / Disney+' or 'NBC / Peacock'; include multiple if applicable)  
- Local Time (translate to user's local time zone, e.g., '8:00 PM EST'; include duration if relevant, like '8:00-11:00 PM EST')  
- Notes (brief details like 'Playoffs Round 1' or 'Key Matchup: Star Players Involved'; keep concise)

Focus on events broadcast on major networks or streaming services (e.g., ESPN, Fox Sports, NBC, CBS, TNT, Prime Video, Peacock, Paramount+, etc.). Only include events that actually occur during that exact week—exclude announcements, recaps, or non-competitive events like drafts (unless highly popular like NFL Draft).

Base the list on the most up-to-date schedules from reliable sources (e.g., ESPN, Sports Illustrated, Bleacher Report, official league sites like NFL.com, NBA.com, MLB.com, PremierLeague.com, Wikipedia sports calendars, JustWatch for broadcast info). If conflicting schedules exist, prioritize official league or broadcaster announcements.

End the response with a brief notes section covering:  
- Any important time zone details (e.g., how times were translated based on user location),  
- Broadcast caveats (e.g., regional blackouts, subscription required, check for live streaming options),  
- Popularity sorting rationale (e.g., based on viewership data from sources like Nielsen),  
- And a note that schedules can change due to weather, injuries, or other factors—always verify directly on official sites or apps.

If literally no major sports events in the week, state so briefly and suggest checking a broader range or popular ongoing seasons.
