### Olympic Games Events Weekly Listings Prompt (v1.0 – Multi-Edition Adaptable)

**Author:** Scott M 
**Goal:**  
Create a clean, user-friendly summary of upcoming Olympic events (competitions, medal events, ceremonies) during the next 7 days from today's date forward, for the current or specified Olympic Games (e.g., Winter Olympics Milano Cortina 2026, or future editions like LA 2028, French Alps 2030, etc.). Focus on major events across all sports, sorted by estimated popularity/viewership (e.g., prioritize high-profile sports like figure skating, alpine skiing, ice hockey over niche ones). Indicate broadcast/streaming details (primary channels/services like NBC/Peacock for US viewers) and translate event times to the user's local time zone (use provided user location/timezone). Organize by day with markdown tables for easy viewing planning, emphasizing key medal events, finals, and ceremonies while avoiding minor heats unless notable.

**Supported AIs (sorted by ability to handle this prompt well – from best to good):**  
1. Grok (xAI) – Excellent real-time updates, tool access for verification, handles structured tables/formats precisely.  
2. Claude 3.5/4 (Anthropic) – Strong reasoning, reliable table formatting, good at sourcing/summarizing schedules.  
3. GPT-4o / o1 (OpenAI) – Very capable with web-browsing plugins/tools, consistent structured outputs.  
4. Gemini 1.5/2.0 (Google) – Solid for calendars and lists, but may need prompting for separation of tables.  
5. Llama 3/4 variants (Meta) – Good if fine-tuned or with search; basic versions may require more guidance on format.

**Changelog:**  
- v1.0 (initial) – Adapted from sports events prompt; tailored for multi-day Olympic periods; includes broadcast/streaming, local time translation; sorted by popularity; flexible for future Games (e.g., specify edition if not current).

**Prompt Instructions:**

List major Olympic events (competitions, medal finals, key matches, ceremonies) occurring in the next 7 days from today's date forward for the ongoing or specified Olympic Games (default to current edition, e.g., Milano Cortina 2026 Winter Olympics; adaptable for future like LA 2028 Summer, French Alps 2030 Winter, etc.). Include Opening/Closing Ceremonies if within range.

Organize the information with a separate markdown table for each day that has at least one notable event. Place the date as a level-3 heading above each table (e.g., ### February 6, 2026). Skip days with no major activity—do not mention empty days.

Sort events within each day's table by estimated popularity (descending: use general viewership, global interest, and cultural impact—e.g., ice hockey finals > figure skating > curling; alpine skiing > biathlon). Use these exact columns in each table:  
- Name (e.g., 'Men's Figure Skating Short Program' or 'USA vs. Canada Ice Hockey Preliminary')  
- Sport/Discipline (e.g., 'Figure Skating' or 'Ice Hockey')  
- Broadcast/Streaming (primary platforms, e.g., 'NBC / Peacock' or 'Eurosport / Discovery+'; note US/international if relevant)  
- Local Time (translated to user's timezone, e.g., '8:00 PM EST'; include approximate duration or session if known, like '8:00-10:30 PM EST')  
- Notes (brief details like 'Medal Event' or 'Team USA Featured' or 'Live from Milan Arena'; keep concise)

Focus on events broadcast/streamed on major official Olympic broadcasters (e.g., NBC/Peacock in US, Eurosport/Discovery in Europe, official Olympics.com streams, host broadcaster RAI in Italy, etc.). Prioritize medal events, finals, high-profile matchups, and ceremonies. Only include events actually occurring during that exact week—exclude previews, recaps, or non-competitive activities unless exceptionally notable (e.g., torch relay if highlighted).

Base the list on the most up-to-date schedules from reliable sources (e.g., Olympics.com official schedule, NBCOlympics.com, TeamUSA.com, ESPN, BBC Sport, Wikipedia Olympic pages, official broadcaster sites). If conflicting times/dates exist, prioritize official IOC or host broadcaster announcements.

End the response with a brief notes section covering:  
- Time zone translation details (e.g., 'All times converted to EST based on user location in East Hartford, CT; Italy is typically 6 hours ahead during Winter Games'),  
- Broadcast caveats (e.g., regional availability, blackouts, subscription required for Peacock/Eurosport; check Olympics.com or local broadcaster for full streams),  
- Popularity sorting rationale (e.g., based on historical viewership data from previous Olympics),  
- General availability (e.g., many events stream live on Olympics.com or Peacock; replays often available),  
- And a note that Olympic schedules can shift due to weather, delays, or other factors—always verify directly on official sites/apps like Olympics.com or NBCOlympics.com.

If literally no major Olympic events in the week (e.g., outside Games period), state so briefly and suggest checking the full Olympic calendar or upcoming editions (e.g., LA 2028 Summer Olympics July 14–30, 2028).

To use for future Games: Replace or specify the edition in the prompt (e.g., "for the LA 2028 Summer Olympics") when running in future years.
