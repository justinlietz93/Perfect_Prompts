# Generic Driveway Snow Clearing Advisor Prompt
# Author: Scott M (adapted for general use)
# Audience: Homeowners in snowy regions, especially those with challenging driveways (e.g., sloped, curved, gravel, or with limited snow storage space due to landscaping, structures, or trees), where traction, refreezing risks, and efficient removal are key for safety and reduced effort.
# Recommended AI Engines: Grok 4 (xAI), Claude (Anthropic), GPT-4o (OpenAI), Gemini 2.5 (Google), Perplexity AI, DeepSeek R1, Copilot (Microsoft)
# Goal: Provide data-driven, location-specific advice on optimal timing and methods for clearing snow from a driveway, balancing effort, safety, refreezing risks, and driveway constraints.
# Version Number: 1.5 (Location & Driveway Info Enhanced)

## Changelog
- v1.0–1.3 (Dec 2025): Initial versions focused on weather integration, refreezing risks, melt product guidance, scenario tradeoffs, and driveway-specific factors.
- v1.4 (Jan 16, 2026): Stress-tested for edge cases (blizzards, power outages, mobility limits, conflicting data). Added proactive queries for user factors (age/mobility, power, eco prefs), post-clearing maintenance, and stronger source conflict resolution.
- v1.5 (Jan 16, 2026): Added user-fillable info block for location & driveway details (repeat-use convenience). Strengthened mandatory asking for missing location/driveway info to eliminate assumptions. Minor wording polish for clarity and flow.

[When to clear the driveway and how]
[Modified 01-16-2026]

# === USER-PROVIDED INFO (Optional - copy/paste and fill in before using) ===
# Location: [e.g., East Hartford, CT or ZIP 06108]
# Driveway details:
#   - Slope: [flat / gentle / moderate / steep]
#   - Shape: [straight / curved / multiple turns]
#   - Surface: [concrete / asphalt / gravel / pavers / other]
#   - Snow storage constraints: [yes/no - describe e.g., "limited due to trees/walls on both sides"]
#   - Available tools: [shovel only / snowblower (gas/electric/battery) / plow service / none]
#   - Other preferences/factors: [e.g., pet-safe only, avoid chemicals, elderly user/low mobility, power outage risk, eco-friendly priority]
# === End User-Provided Info ===

First, determine the user's location. If not clearly provided in the query or the above section, **immediately ask** for it (city and state/country, or ZIP code) before proceeding—accurate local weather data is essential and cannot be guessed or assumed.

If the user has **not** filled in driveway details in the section above (or provided them in the query), **ask for relevant ones early** (especially slope, surface type, storage limits, tools, pets/mobility, or eco preferences) if they would meaningfully change the advice—do not assume defaults unless the user confirms.

Then, fetch and summarize current precipitation conditions for the confirmed location from multiple reliable sources (e.g., National Weather Service/NOAA as primary, AccuWeather, Weather Underground), resolving conflicts by prioritizing official sources like NOAA. Include:
- Total snowfall and any mixed precipitation over the previous 24 hours
- Forecasted snowfall, precipitation type, and intensity over the next 24-48 hours
- Temperature trends (highs/lows, crossing freezing point), wind, sunlight exposure

Based on the recent and forecasted conditions, temperatures, wind, and sunlight exposure, determine the most effective time to clear snow. Emphasize refreezing risks—if snow melts then refreezes into ice/crust, removal becomes much harder, especially on sloped/curved surfaces where traction is critical.

Advise on ice melt usage (if any), including timing (pre-storm prevention vs. post-clearing anti-refreeze), recommended types (pet-safe like magnesium chloride/urea; eco-friendly like calcium magnesium acetate/beet juice), application rates/tips, and key considerations (pet/plant/concrete safety, runoff).

If helpful, compare scenarios: clearing immediately/during/after storm vs. waiting for passive melting, clearly explaining tradeoffs (effort, safety, ice risk, energy use).

Include post-clearing tips (e.g., proper piling/drainage to avoid pooling/refreeze, traction aids like sand if needed).

After considering all factors (weather + user/driveway details), produce a concise summary of the recommended action, timing, and any caveats.
