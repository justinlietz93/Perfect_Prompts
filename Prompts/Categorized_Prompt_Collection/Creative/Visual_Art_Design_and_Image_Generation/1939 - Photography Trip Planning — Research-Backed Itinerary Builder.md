# Photography Trip Planning Prompt
## Reusable Template for Travel Photographers
### v3.0

---

> **Two ways to use this template:**
>
> **Lightweight mode** — Skip all sections marked `[OPTIONAL]` and the entire Technical Notes section. Fill in your style profile and trip details, then ask Claude for a text-based research brief and day-by-day schedule. No scripting required.
>
> **Full production mode** — Use every section. Claude will produce a PowerPoint slide deck (via Node.js + pptxgenjs), an Excel workbook (via Python + openpyxl), and Google Maps CSVs — all color-coded and QA'd. Requires comfort running scripts from the command line.
>
> In both modes: fill in every section marked `[FILL IN]`. Sections marked `[EXAMPLE]` show what a completed entry looks like — replace them with your own details. Sections marked `[OPTIONAL]` can be removed if not relevant to your workflow.

---

## WHO I AM

I am a travel photographer planning a trip [with / without] a companion. My name is [FILL IN]. I shoot with [FILL IN — e.g., Canon EOS R5 and Sony A7IV]. My lens kit for travel: [FILL IN — e.g., 16-35mm wide, 24-70mm standard, 100mm macro]. I travel with [FILL IN — e.g., a carbon fiber travel tripod / no tripod / a compact gorilla-pod]. My carry system is [FILL IN — e.g., a chest rig with Peak Design clips to secure cameras to the straps / a camera backpack with a cube insert].

> [EXAMPLE]: I shoot with a Canon 5D Mark II and Canon EOS-R with EF adapter. Lens kit: 16-35mm (primary workhorse), 24-105mm (street/mid-range), 100mm macro (details/close work). Carry system: a Condor Stowaway chest rig with two Peak Design clips. No ND filters on this trip.

---

## MY PHOTOGRAPHIC STYLE

This is the most important section. Read it carefully before suggesting any locations.

**The core subject:** [FILL IN — Describe the through-line of your work. What do you photograph and why? What draws you to a subject?]

> [EXAMPLE]: I photograph things that endure — structures, landscapes, and moments that exist outside of time. The through-line across my work is things built or lived in that now outlive their original purpose, still standing.

**Technical signatures:** [FILL IN — List your consistent compositional and technical choices.]

> [EXAMPLE]:
> - Symmetrical or near-symmetrical composition with a strong central vanishing point
> - Low angle or looking straight up to exaggerate scale and eliminate horizon — I do this consistently
> - A single human figure used for scale, not as the primary subject
> - Long exposure or slow shutter to pull motion out of water, clouds, and crowds
> - B&W for structural, industrial, and decay subjects; color when the palette itself is the subject
> - Strong tonal contrast — I print dark
> - The underside, interior skeleton, and structural bones of things interest me more than facades

**Recurring subject categories:** [FILL IN — List the types of places and subjects you consistently seek out.]

> [EXAMPLE]:
> - Decay and abandonment — things that have outlived their purpose (plane wrecks, ruined churches, abandoned institutions)
> - Sacred spaces with weight and edge — not pretty churches, spaces where something happened
> - Old-meets-industrial juxtapositions (ancient marble in a power plant, Roman columns in a modern piazza)
> - Underground and subterranean spaces — crypts, tunnels, ancient layers beneath modern cities
> - Geometric structural form — bridges, piers, arches, repeating elements
> - Quiet and empty streets — I shoot before crowds arrive
> - Atlas Obscura-type locations — the unusual, the hidden, the forgotten

**What I consistently avoid:** [FILL IN — List what you do not want recommended.]

> [EXAMPLE]:
> - Postcard framing of famous places
> - Posed subjects
> - Soft or sentimental light
> - Crowded tourist spots as primary targets
> - Markets as planned stops (open to stumbling upon them)

---

## TRAVEL COMPANION [OPTIONAL]

[FILL IN or delete this section] — If you are traveling with a companion, describe their interests here so Claude can build a plan that works for both of you, not a photographer's itinerary with someone along for the ride.

> [EXAMPLE]: My partner travels with me for the entire trip. They enjoy boutique shopping, aperitivo culture, neighborhood wandering, and unusual cultural experiences including ossuaries and catacombs. They are game for unusual locations. Nearly all photography targets are shared experiences — they are present for the vast majority of shoots, not waiting elsewhere. The only genuinely solo time is pre-dawn sessions. Build shared experiences into the plan, not a parallel track.

**On adventure and physical effort:** By default, a fully researched, ticketed, pre-scheduled itinerary can feel risk-free and passive — nothing left to chance, no physical exertion, no uncertainty. If a harder, more physically engaged way to reach a location exists (climbing down to a site instead of taking a boat, hiking a trail instead of driving), surface it explicitly as a choice rather than silently defaulting to the easier option. Don't just describe the harder option — check the return logistics too (e.g., if hiking down from a summit, where does the car end up, and how do you get back to it?).

**On fatigue:** Don't assume unlimited energy across a multi-city trip. Calculate the cumulative load of pre-dawn shoots, jet lag, and daily walking distance, and flag when a trip has no genuine rest morning built in. A trip with five excellent pre-dawn sessions beats one with six mediocre ones. Recommend at least one no-alarm, fully unplanned rest morning roughly mid-trip, not just on arrival day.

---

## THE TRIP

**Destination:** [FILL IN — e.g., "Italy: Rome, Venice, Milan"]
**Departure:** [FILL IN — e.g., "LAX, Sept 16, 3:05 PM"]
**Return:** [FILL IN — e.g., "LIN (Milan Linate), Sept 28, 9:50 AM"]
**Outbound arrival:** [FILL IN — e.g., "FCO (Rome), Sept 17, 2:05 PM"]
**Cities and nights:** [FILL IN — e.g., "Rome 3 nights, Venice 3 nights, Milan 3 nights"]
**City-to-city transport:** [FILL IN — e.g., "Frecciarossa train, targeting ~5 PM arrival at each new city to protect the outgoing city's final morning"]
**Base neighborhoods:** [FILL IN, or ask Claude to recommend based on shooting targets and companion interests]

---

## WHAT I WANT CLAUDE TO BUILD

### 1. PowerPoint Slide Deck [OPTIONAL — requires Node.js and pptxgenjs]

> This deliverable is for users comfortable running Node.js scripts. If you want a simpler output, replace this section with a request for a formatted document or text plan.

**Format:** LAYOUT_WIDE (13.3 x 7.5 inches), built with pptxgenjs in Node.js. Dark navy background with gold accent text on divider and reference slides. Off-white background on content/schedule slides. Version number on cover and filename.

**Badges/flags on slide header or inline:**
- Red badge: "★ ADVANCE BOOKING REQUIRED" — for locations requiring pre-purchase tickets
- Green badge: "★ ATLAS OBSCURA" — for unusual/hidden locations in that spirit
- Gold banner: "SHARED EXPERIENCE" — for meaningful shared visits
- Dark red badge: "⊘ PHOTOGRAPHY PROHIBITED" — only after direct verification (see Location Research Standards)
- Dark red badge on High Viewpoints cards: "⊘ CONFIRMED CLOSED" — for viewpoints that no longer exist or have shut down

**Slides to include:**
- Cover (trip title, cities, dates, version number)
- Trip overview (card layout, one card per city stop with dates/nights/base)
- Photography approach (style summary, gear)
- Schedule color legend
- For each city:
  - City section divider (full dark background)
  - Light timing table (blue hour start, sunrise, golden hour AM, golden hour PM, sunset, blue hour end — calculated with Python astral library, exact coordinates, actual trip dates)
  - Base camp slide (why this neighborhood, proximity to shooting targets, highlights nearby, transit)
  - Location slides for each confirmed shooting target: About / Shot List (4–5 shots) / Unconventional Perspectives (3–4 angles), plus a Key Notes bar (hours, access, cost)
  - High Viewpoints slide (card layout, 3 viewpoints; flag confirmed closures; distinguish true post-sundown viewpoints from golden-hour-only ones that close before dark)
  - Daily schedule — combine all days for a city onto a single slide; only split to a continuation slide if the content would actually overflow the slide height. Do not split preemptively at a fixed row count.
- Time Allocation pie chart (hours by category, pulled from actual schedule data)
- Tickets and booking slide (3 columns: book in advance / pay on day / free)
- Gear list slide (cameras, lenses, support, carry system, accessories, notes on where tripods/photography are restricted)
- Aperitivo/food bars slide — specific named bars by city, local picks only, with address and description. These are options spread across multiple evenings, not a single-night bar crawl.
- Train/transport connections summary slide [OPTIONAL]
- **Appendix — Shot Diagrams:** plan-view and cross-section schematics for every photography location. Camera position (red dot), shooting direction (dashed line), field-of-view cone (dotted lines), recommended lens, all numbered to match the location's shot list. Every plan-view diagram must include a north arrow/compass indicator. Cross-section diagrams (showing vertical relationships like a flooded crypt or a cliff-face) don't need one.

**Schedule color coding (7 categories):**
- Pre-Dawn Shoot / Photography: dark navy bg, light blue text
- Aperitivo: dark purple bg, light purple text
- Shared Activity: dark gold bg, light gold text
- Free / Optional: dark green bg, light green text
- Travel / Arrival: dark gray bg, light gray text
- Rest / Checkout: medium gray bg, light gray text
- Advance Booking Required: dark red bg, light red text
- (Sunset/golden-hour blocks can get a dark-orange variant if useful)

---

### 2. Excel Workbook [OPTIONAL — requires Python and openpyxl]

**Master tab — ask which format the person wants:**
- **List format:** chronological rows (Date, Day, City, Time, Activity, Category, Duration, Notes), one row per activity across the whole trip.
- **Calendar grid format:** horizontal week view — all trip days as columns left to right, a shared time axis down both sides (e.g. 5:00 AM–10:30 PM in 30-minute rows), each activity rendered as a color-coded block merged vertically across the rows it spans. Travel/transition-day columns get a visually distinct header and background tint. Sunrise, sunset, blue hour, and golden hour rows are highlighted on the time axis (label as trip-average approximations with a footnote — point to per-city Light Timing slides for precision). One sheet, all days, no tab splits.

One tab per city (vertical day-by-day format regardless of which Master style is chosen), plus a Legend tab.

Same color coding as schedule slides. Freeze panes, hide gridlines, auto-filter on header rows where the sheet is a flat list. Include a Duration column.

---

### 3. Google Maps CSVs — one per city [OPTIONAL]

Columns: Name, Description, Category, Best Time, Latitude, Longitude, Address.

**Critical:** Use Python csv.writer with utf-8 encoding. No special characters — plain ASCII only, with explicit character substitution (e.g. é→e, —→--, '→'). Verify coordinates before including.

Categories: Shooting Location, Shared Activity, Base, High Viewpoint, Transit, Optional Day Trip, CLOSED - DO NOT USE, Atlas Obscura Optional.

**File naming convention:** [destination]-trip-[year]-v[N].pptx / .xlsx / [city]-locations-v[N].csv. Increment the version number on every rebuild, and keep the deck, workbook, and all CSVs at the same version number even if only one file changed — rename/re-copy unchanged files so the full deliverable set stays in sync.

---

## LOCATION RESEARCH STANDARDS

### For each shooting location, provide:
1. **Description** — what it is, why it matters photographically, best conditions, connection to my style profile where relevant
2. **Shot list** — 4–5 standard shots worth getting
3. **Unconventional perspectives** — 3–4 angles or approaches most photographers miss, matched to my style profile above
4. **Key notes** — hours, access, cost, transit, proximity to other targets
5. **Best time** — pre-dawn / early morning / morning / afternoon / golden hour

### Photography policy verification — non-negotiable:
Before listing any location as a photography target, **verify the actual photography policy directly** — official site, or by contacting the venue if the policy is ambiguous or high-stakes. Do not assume "no photography" or "photography allowed" based on general reputation or partial information. Two real examples: a location assumed fully off-limits turned out to allow personal use with equipment-timing restrictions once the venue was emailed directly; a separate underground site turned out to prohibit photography completely despite initially being treated as a shooting target. When a venue's written policy restricts *equipment* (tripods, DSLRs) to specific hours rather than restricting photography outright, treat it as a scheduling constraint, not a footnote.

### For each city, also research:
- The best base neighborhood (balancing proximity to shooting targets and companion interests)
- **High viewpoints — split into two categories:** (a) true post-sundown/night viewpoints that stay open into darkness, and (b) golden-hour-only viewpoints that close before true dark (many rooftop terraces do — check exact closing time against that city's actual sunset time before assuming a rooftop works for night photography). Confirm current open/closed status; flag confirmed permanent closures clearly rather than omitting them silently.
- Optional day trips (3–4 options matched to both your aesthetic and companion interests)
- Atlas Obscura locations that genuinely fit your style — filter carefully, not everything qualifies
- Specific aperitivo/food bars: local picks only, not tourist-facing, with name, address, and what makes them worth going to
- Self-drive or no-license rental options (boats, small vehicles) where they'd give more compositional control than a scheduled ferry/tour — verify pricing and access logistics directly, don't extrapolate from aggregated blog content [OPTIONAL]

### Research and verification requirements:
- **Verify all locations exist** before including — web search any location you are not certain about
- **Confirm current access status** — search for closures before recommending any viewpoint or attraction
- **Days of week:** always calculate with Python datetime for the actual trip year. Never guess.
- **Light timing:** always calculate with Python astral library using exact city coordinates and trip dates. Never estimate.
- **Ticket prices and booking windows:** search for current prices — do not rely on training data
- **Do not hallucinate** — if uncertain about a fact, search or say so. If asked directly "why did you hallucinate X," own it plainly rather than explaining it away.
- **When new information contradicts prior research** (e.g., an official email reply from a venue), propagate the correction across every affected deliverable in the same pass — schedule, location slide, booking slide, Excel notes, CSV — not just in conversation.

---

## ATLAS OBSCURA APPROACH

Filter Atlas Obscura picks strictly against your style profile. Use these as a guide for what typically works and what doesn't:

**Strong fits:**
- Underground or subterranean spaces (crypts, tunnels, ancient layers)
- Abandoned or decaying spaces (former institutions, industrial ruins) — verify current safety and legal access status before including; drop anything requiring trespass regardless of photographic appeal
- Bone chapels and ossuaries
- Hidden architectural anomalies (a spiral staircase down an alley, an alchemist's gate in a park)
- Sacred spaces that have crossed into the uncanny

**Weak fits — do not suggest:**
- Quirky museums without strong visual potential
- Locations that are historically interesting but not photographically compelling
- Anything requiring illegal or unsafe access — note if access is uncertain and flag for research rather than recommending

---

## APERITIVO/FOOD RESEARCH STANDARD

For each city, research 3–4 specific local bars or restaurants. Requirements:
- Local crowd, not tourist-facing
- Named venue with street address
- One-sentence description of what makes it worth going to
- Flag any important closures (day of week, time of day)
- Prioritize venues near shooting locations so the same place can be visited at dawn (shooting) and evening (aperitivo) — this is a strong pairing when possible
- Present these as a menu of options across the trip's evenings, not a single night's itinerary — don't imply nightly bar-hopping unless the person says that's what they want

---

## PLANNING PROCESS

Follow this order:

1. Ask for trip dates, cities, and transport if not provided
2. Verify days of week with Python before doing anything else
3. Calculate light timing with Python astral for all shooting days
4. Research and propose shooting locations — filter against my style profile — ask to confirm before building
5. Research and propose base neighborhoods per city — ask to confirm
6. Research Atlas Obscura picks per city — propose with honest assessment of fit
7. Research specific local food/drink venues per city
8. Research high viewpoints per city, split by post-sundown vs. golden-hour-only access
9. Identify advance booking requirements and booking windows
10. Build the schedule — pre-dawn shoots, shared experiences, food/aperitivo, free time, and at least one genuine unplanned rest morning
11. **Audit the built schedule before presenting it:** (a) does it contain any real physical effort or unplanned time, or is everything ticketed and passive? (b) does the cumulative pre-dawn + walking load leave room to actually enjoy the trip, or will fatigue compound by mid-trip?
12. Build all deliverables in one go: PowerPoint, Excel, CSVs
13. QA slides before delivering: convert to PDF via soffice, then pdftoppm -jpeg -r 120, review per-slide images

**Batch changes, then rebuild only when explicitly told to.** Confirm all changes before touching any files. Hold requested changes in a running list and rebuild everything together, rather than rebuilding after each individual change.

---

## TECHNICAL NOTES [OPTIONAL — relevant only if using the PowerPoint, Excel, or CSV deliverables]

### pptxgenjs:
- Never pass a lambda as a positional y argument to helper functions — use inline `s.addText()` with explicit coordinates
- Always add `valign: "top"` to bulleted list text boxes
- Every bullet array's last item must include `options: { bullet: true }` explicitly
- Never use `#` in hex color values — pass without the hash
- When building card grids where content length varies, don't assume uniform row heights — either measure/estimate per-card height from item count, or use independently-tracked running y-offsets per column so taller cards don't overlap the next row
- QA every rebuild: `soffice --headless --convert-to pdf`, then `pdftoppm -jpeg -r 120`, review before delivering

### openpyxl:
- Use `PatternFill("solid")` for all cell fills
- Freeze panes at the top-left of the scrollable data region (this shifts if using a calendar-grid Master with header rows and a day-column axis)
- Set `showGridLines = False` on all sheets
- Auto-filter on header rows where the sheet is a flat list; a calendar-grid Master doesn't need auto-filter
- For calendar-grid layouts: resolve overlapping time blocks within a day before merging cells (sort by start time, clip a block's end to the next block's start); named/approximate time-of-day labels need an explicit anchor-hour mapping since they have no literal clock time

### CSVs:
- Always use Python `csv.writer` with utf-8 encoding
- No special characters — plain ASCII only, with explicit character substitution (é→e, —→--, '→')
- Verify coordinates are accurate before including

### Schedule splits (PowerPoint):
- Do not split a city's daily schedule across slides by default. Combine all days for one city onto a single slide.
- Only split to a continuation slide if the actual rendered content would overflow the available slide height — check total row count against available vertical space, not a fixed threshold.

---

## STYLE PREFERENCES

[FILL IN — describe your general planning philosophy. Examples below.]

> [EXAMPLE]:
> - Quality over quantity — fewer, richer locations beat comprehensive lists
> - Minimal logistics friction — don't route across a city when targets can be clustered
> - Authentic over tourist-facing — if a less-visited equivalent exists, recommend it
> - Pre-dawn access is a priority — but nearly all photography targets are shared experiences with my companion
> - The unusual over the famous — Atlas Obscura sensibility throughout
> - Adventure and unplanned time deserve deliberate room, not just ticketed efficiency
> - When in doubt about a fact, search before answering — and say so if you can't verify something rather than presenting an inference as confirmed

---

## COMPANION PRIORITIES [OPTIONAL]

[FILL IN or delete this section] — If traveling with a companion, list what matters to them so their priorities are built into the shared activities and food/aperitivo slides, not treated as an afterthought.

> [EXAMPLE]:
> - Boutique shopping (not chain stores, not department stores)
> - Aperitivo culture — spread across the trip's evenings, not a nightly ritual by default
> - Neighborhood wandering in places that feel local
> - Unusual cultural experiences — game for ossuaries, catacombs, and the uncanny
> - Good food and local restaurants

Remember: the large majority of photography locations should already be shared experiences. Treat the schedule as a joint itinerary with a few solo pre-dawn windows, not a photographer's itinerary with a companion along for the ride.

---

*Template built from a real multi-city Italy trip planning workflow, refined across multiple full deliverable rebuild cycles. Works with Claude, ChatGPT, Gemini, or any modern LLM.*
