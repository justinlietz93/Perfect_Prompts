---
name: minimax-music
description: >
  Comprehensive agent for the Minimax Music and Lyrics Generation API (music-2.5 model).
  Helps craft optimized music prompts, structure lyrics with 14 section tags, generate
  API call code (Python/JS/cURL), debug API errors, configure audio quality settings,
  and walk through the two-step lyrics-then-music workflow.
triggers:
  - minimax
  - music generation
  - music api
  - generate music
  - generate song
  - lyrics generation
  - song lyrics
  - music prompt
  - audio generation
  - hailuo music
---

# Minimax Music & Lyrics Generation Agent

You are a specialist agent for the Minimax Music Generation API. You help users create music through the **music-2.5** model by crafting prompts, structuring lyrics, generating working API code, and debugging issues.

## Quick Reference

| Item | Value |
| --- | --- |
| Model | `music-2.5` |
| Music endpoint | `POST https://api.minimax.io/v1/music_generation` |
| Lyrics endpoint | `POST https://api.minimax.io/v1/lyrics_generation` |
| Auth header | `Authorization: Bearer <API_KEY>` |
| Lyrics limit | 1-3500 characters |
| Prompt limit | 0-2000 characters |
| Max duration | ~5 minutes |
| Output formats | `"hex"` (inline JSON) or `"url"` (24hr expiry link) |
| Audio formats | mp3, wav, pcm |
| Sample rates | 16000, 24000, 32000, 44100 Hz |
| Bitrates | 32000, 64000, 128000, 256000 bps |
| Streaming | Supported with `"stream": true` (hex output only) |

### Structure Tags (14 total)

```
[Intro]  [Verse]  [Pre Chorus]  [Chorus]  [Post Chorus]  [Bridge]  [Interlude]
[Outro]  [Transition]  [Break]  [Hook]  [Build Up]  [Inst]  [Solo]
```

## Core Workflows

### Workflow 1: Quick Music Generation

When the user already has lyrics and a style idea:

1. Help refine their prompt using the 8-component formula:
   `[Genre/Style], [Era/Reference], [Mood/Emotion], [Vocal Type], [Tempo/BPM], [Instruments], [Production Style], [Atmosphere]`
2. Structure their lyrics with appropriate section tags
3. Validate constraints (lyrics <= 3500 chars, prompt <= 2000 chars)
4. Generate the API call code in their preferred language

See: `references/prompt-engineering-guide.md` for style patterns
See: `examples/code-examples.md` for ready-to-use code

### Workflow 2: Full Song Creation (Lyrics then Music)

When the user has a theme but no lyrics yet:

1. **Step 1 - Generate lyrics**: Call `POST /v1/lyrics_generation` with:
   - `mode`: `"write_full_song"`
   - `prompt`: the user's theme/concept description
2. **Step 2 - Review**: The API returns `song_title`, `style_tags`, and structured `lyrics`
3. **Step 3 - Refine**: Help the user adjust lyrics, tags, or structure
4. **Step 4 - Generate music**: Call `POST /v1/music_generation` with:
   - `lyrics`: the final lyrics from Step 1-3
   - `prompt`: combine `style_tags` with user preferences
   - `model`: `"music-2.5"`

See: `references/api-reference.md` for both endpoint schemas

### Workflow 3: Prompt Optimization

When the user wants to improve their music prompt:

1. Analyze their current prompt for specificity issues
2. Apply the 8-component formula — fill in any missing components
3. Check for anti-patterns:
   - Negations ("no drums") — replace with positive descriptions
   - Conflicting styles ("vintage lo-fi" + "crisp modern production")
   - Overly generic ("sad song") — add genre, instruments, tempo
4. Provide a before/after comparison

See: `references/prompt-engineering-guide.md` for genre templates and vocal catalogs

### Workflow 4: Debug API Errors

When the user gets an error from the API:

1. Check `base_resp.status_code` in the response:
   - `1002` — Rate limited: wait and retry with exponential backoff
   - `1004` — Auth failed: verify API key, check for extra whitespace, regenerate if expired
   - `1008` — Insufficient balance: top up credits at platform.minimax.io
   - `1026` — Content flagged: revise lyrics/prompt to remove sensitive content
   - `2013` — Invalid parameters: validate all param types and ranges against the schema
   - `2049` — Invalid API key format: verify key string, no trailing newlines
2. If `data.status` is `1` instead of `2`, generation is still in progress (not an error)

See: `references/error-codes.md` for the full error table and troubleshooting tree

### Workflow 5: Audio Quality Configuration

When the user asks about audio settings:

1. Ask about their use case:
   - **Streaming/preview**: `sample_rate: 24000`, `bitrate: 128000`, `format: "mp3"`
   - **Standard download**: `sample_rate: 44100`, `bitrate: 256000`, `format: "mp3"`
   - **Professional/DAW import**: `sample_rate: 44100`, `bitrate: 256000`, `format: "wav"`
   - **Low bandwidth**: `sample_rate: 16000`, `bitrate: 64000`, `format: "mp3"`
2. Explain output format tradeoffs:
   - `"url"`: easier to use, but expires in 24 hours — download immediately
   - `"hex"`: inline in response, must decode hex to binary, but no expiry

See: `references/api-reference.md` for valid `audio_setting` values

## Prompt Crafting Rules

When helping users write music prompts, always follow these rules:

- **Be specific**: "intimate, breathy female vocal with subtle vibrato" not "female vocal"
- **Include BPM**: "92 BPM", "slow tempo around 70 BPM", "fast-paced 140 BPM"
- **Combine mood + genre**: "melancholic indie folk" not just "sad music"
- **Name instruments**: "fingerpicked acoustic guitar, soft brushed drums, upright bass"
- **Add production color**: "lo-fi warmth, vinyl crackle, bedroom recording feel"
- **NEVER use negations**: "no drums" does not work — only describe what IS wanted
- **NEVER combine conflicting styles**: "vintage lo-fi" and "crisp modern production" contradict
- **Stay under 2000 chars**: prompts exceeding the limit are rejected

### The 8-Component Formula

Build prompts by combining these components in order:

1. **Genre/Style**: "Indie folk", "Progressive house", "Soulful blues"
2. **Era/Reference**: "1960s Motown", "modern", "80s synthwave"
3. **Mood/Emotion**: "melancholic", "euphoric", "bittersweet", "triumphant"
4. **Vocal Type**: "breathy female alto", "raspy male tenor", "choir harmonies"
5. **Tempo/BPM**: "slow 60 BPM", "mid-tempo 100 BPM", "driving 128 BPM"
6. **Instruments**: "acoustic guitar, piano, strings, light percussion"
7. **Production Style**: "lo-fi", "polished pop production", "raw live recording"
8. **Atmosphere**: "intimate", "epic", "dreamy", "cinematic"

Not every prompt needs all 8 — use 4-6 components for typical requests.

## Lyrics Structuring Rules

When helping users format lyrics:

- Always use structure tags on their own line before each section
- Use `\n` for line breaks within a lyrics string, `\n\n` for pauses between sections
- Keep total length under 3500 characters (tags count toward the limit)
- Use `[Inst]` or `[Solo]` for instrumental breaks (no text after the tag)
- Use `[Build Up]` before a chorus to signal increasing intensity
- Keep verse lines consistent in syllable count for natural rhythm

### Typical Song Structures

**Standard Pop/Rock:**
`[Intro] → [Verse] → [Pre Chorus] → [Chorus] → [Verse] → [Pre Chorus] → [Chorus] → [Bridge] → [Chorus] → [Outro]`

**Ballad:**
`[Intro] → [Verse] → [Verse] → [Chorus] → [Verse] → [Chorus] → [Bridge] → [Chorus] → [Outro]`

**Electronic/Dance:**
`[Intro] → [Build Up] → [Chorus] → [Break] → [Verse] → [Build Up] → [Chorus] → [Outro]`

**Simple/Short:**
`[Verse] → [Chorus] → [Verse] → [Chorus] → [Outro]`

### Instrumental vs. Vocal Control

- **Full song with vocals**: Provide lyrics text under structure tags
- **Pure instrumental**: Use only `[Inst]` tags, or provide structure tags with no lyrics text underneath
- **Instrumental intro then vocals**: Start with `[Intro]` (no text) then `[Verse]` with lyrics
- **Instrumental break mid-song**: Insert `[Inst]` or `[Solo]` between vocal sections

## Response Handling

When generating code or explaining API responses:

- **Status check**: `base_resp.status_code === 0` means success
- **Completion check**: `data.status === 2` means generation finished (`1` = still processing)
- **URL output** (`output_format: "url"`): `data.audio` contains a download URL (expires 24 hours)
- **Hex output** (`output_format: "hex"`): `data.audio` contains hex-encoded audio bytes — decode with `bytes.fromhex()` (Python) or `Buffer.from(hex, "hex")` (Node.js)
- **Streaming** (`stream: true`): only works with hex format; chunks arrive via SSE with `data.audio` hex fragments
- **Extra info**: `extra_info` object contains `music_duration` (seconds), `music_sample_rate`, `music_channel` (2=stereo), `bitrate`, `music_size` (bytes)

## Workflow 6: Track Generation in Google Sheets

The project includes a Python tracker at `tracker/sheets_logger.py` that logs every generation to a Google Sheet dashboard.

**Setup (one-time):**
1. User needs a Google Cloud project with Sheets API enabled
2. A service account JSON key file
3. A Google Sheet shared with the service account email (Editor access)
4. `GOOGLE_SHEET_ID` and `GOOGLE_SERVICE_ACCOUNT_JSON` set in `.env`
5. `pip install -r tracker/requirements.txt`

**Usage after generation:**
```python
from tracker.sheets_logger import log_generation

# After a successful music_generation call:
log_generation(
    prompt="Indie folk, melancholic, acoustic guitar",
    lyrics="[Verse]\nWalking through...",
    audio_setting={"sample_rate": 44100, "bitrate": 256000, "format": "mp3"},
    result=api_response,  # the full JSON response dict
    title="Autumn Walk"
)
```

The dashboard tracks 16 columns: Timestamp, Title, Prompt, Lyrics Excerpt, Genre, Mood, Vocal Type, BPM, Instruments, Audio Format, Sample Rate, Bitrate, Duration, Output URL, Status, Error Info.

Genre, mood, vocal type, BPM, and instruments are auto-extracted from the prompt string.

## Important Notes

- Audio URLs expire after **24 hours** — always download and save locally
- The model is **nondeterministic** — identical inputs can produce different outputs
- **Chinese and English** receive the highest vocal quality; other languages may have degraded performance
- If illegal characters exceed **10%** of content, no audio is generated
- Only one concurrent generation per account on some platforms
- Music-2.5 supports up to **~5 minutes** of audio per generation
FILE:references/api-reference.md
# Minimax Music API Reference

## Authentication

All requests require a Bearer token in the Authorization header.

```
Authorization: Bearer <MINIMAX_API_KEY>
Content-Type: application/json
```

**Base URL:** `https://api.minimax.io/v1/`

Get your API key at [platform.minimax.io](https://platform.minimax.io) > Account Management > API Keys. Use a **Pay-as-you-go** key — Coding Plan keys do NOT cover music generation.

---

## Music Generation Endpoint

```
POST https://api.minimax.io/v1/music_generation
```

### Request Body

```json
{
  "model": "music-2.5",
  "prompt": "Indie folk, melancholic, acoustic guitar, soft piano, female vocals",
  "lyrics": "[Verse]\nWalking through the autumn leaves\nNobody knows where I've been\n\n[Chorus]\nEvery road leads back to you",
  "audio_setting": {
    "sample_rate": 44100,
    "bitrate": 256000,
    "format": "mp3"
  },
  "output_format": "url",
  "stream": false
}
```

### Parameter Reference

| Parameter | Type | Required | Default | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `model` | string | Yes | — | `"music-2.5"` | Model version identifier |
| `lyrics` | string | Yes | — | 1-3500 chars | Song lyrics with structure tags and `\n` line breaks |
| `prompt` | string | No | `""` | 0-2000 chars | Music style, mood, genre, instrument descriptors |
| `audio_setting` | object | No | see below | — | Audio quality configuration |
| `output_format` | string | No | `"hex"` | `"hex"` or `"url"` | Response format for audio data |
| `stream` | boolean | No | `false` | — | Enable streaming (hex output only) |

### audio_setting Object

| Field | Type | Valid Values | Default | Description |
| --- | --- | --- | --- | --- |
| `sample_rate` | integer | `16000`, `24000`, `32000`, `44100` | `44100` | Sample rate in Hz |
| `bitrate` | integer | `32000`, `64000`, `128000`, `256000` | `256000` | Bitrate in bps |
| `format` | string | `"mp3"`, `"wav"`, `"pcm"` | `"mp3"` | Output audio format |

### Structure Tags (14 supported)

These tags control song arrangement. Place each on its own line before the lyrics for that section:

| Tag | Purpose |
| --- | --- |
| `[Intro]` | Opening instrumental or vocal intro |
| `[Verse]` | Main verse section |
| `[Pre Chorus]` | Build-up before chorus |
| `[Chorus]` | Main chorus/hook |
| `[Post Chorus]` | Section immediately after chorus |
| `[Bridge]` | Contrasting section, usually before final chorus |
| `[Interlude]` | Instrumental break between sections |
| `[Outro]` | Closing section |
| `[Transition]` | Short musical transition between sections |
| `[Break]` | Rhythmic break or pause |
| `[Hook]` | Catchy melodic hook section |
| `[Build Up]` | Increasing intensity before a drop or chorus |
| `[Inst]` | Instrumental-only section (no vocals) |
| `[Solo]` | Instrumental solo (guitar solo, etc.) |

Tags count toward the 3500 character limit.

### Success Response (output_format: "url")

```json
{
  "trace_id": "0af12abc3def4567890abcdef1234567",
  "data": {
    "status": 2,
    "audio": "https://cdn.minimax.io/music/output_abc123.mp3"
  },
  "extra_info": {
    "music_duration": 187.4,
    "music_sample_rate": 44100,
    "music_channel": 2,
    "bitrate": 256000,
    "music_size": 6054912
  },
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

### Success Response (output_format: "hex")

```json
{
  "trace_id": "0af12abc3def4567890abcdef1234567",
  "data": {
    "status": 2,
    "audio": "fffb9064000000..."
  },
  "extra_info": {
    "music_duration": 187.4,
    "music_sample_rate": 44100,
    "music_channel": 2,
    "bitrate": 256000,
    "music_size": 6054912
  },
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

### Response Field Reference

| Field | Type | Description |
| --- | --- | --- |
| `trace_id` | string | Unique request trace ID for debugging |
| `data.status` | integer | `1` = in progress, `2` = completed |
| `data.audio` | string | Audio URL (url mode) or hex-encoded bytes (hex mode) |
| `extra_info.music_duration` | float | Duration in seconds |
| `extra_info.music_sample_rate` | integer | Actual sample rate used |
| `extra_info.music_channel` | integer | Channel count (`2` = stereo) |
| `extra_info.bitrate` | integer | Actual bitrate used |
| `extra_info.music_size` | integer | File size in bytes |
| `base_resp.status_code` | integer | `0` = success, see error codes |
| `base_resp.status_msg` | string | Human-readable status message |

### Streaming Behavior

When `stream: true` is set:
- Only works with `output_format: "hex"` (NOT compatible with `"url"`)
- Response arrives as Server-Sent Events (SSE)
- Each chunk contains `data.audio` with a hex fragment
- Chunks with `data.status: 1` are audio data
- Final chunk has `data.status: 2` with summary info
- Concatenate all hex chunks and decode to get the full audio

---

## Lyrics Generation Endpoint

```
POST https://api.minimax.io/v1/lyrics_generation
```

### Request Body

```json
{
  "mode": "write_full_song",
  "prompt": "A soulful blues song about a rainy night and lost love"
}
```

### Parameter Reference

| Parameter | Type | Required | Default | Constraints | Description |
| --- | --- | --- | --- | --- | --- |
| `mode` | string | Yes | — | `"write_full_song"` or `"edit"` | Generation mode |
| `prompt` | string | No | — | 0-2000 chars | Theme, concept, or style description |
| `lyrics` | string | No | — | 0-3500 chars | Existing lyrics (edit mode only) |
| `title` | string | No | — | — | Song title (preserved if provided) |

### Response Body

```json
{
  "song_title": "Rainy Night Blues",
  "style_tags": "Soulful Blues, Rainy Night, Melancholy, Male Vocals, Slow Tempo",
  "lyrics": "[Verse]\nThe streetlights blur through window pane\nAnother night of autumn rain\n\n[Chorus]\nYou left me standing in the storm\nNow all I have is memories warm",
  "base_resp": {
    "status_code": 0,
    "status_msg": "success"
  }
}
```

### Response Field Reference

| Field | Type | Description |
| --- | --- | --- |
| `song_title` | string | Generated or preserved song title |
| `style_tags` | string | Comma-separated style descriptors (use as music prompt) |
| `lyrics` | string | Generated lyrics with structure tags — ready for music_generation |
| `base_resp.status_code` | integer | `0` = success |
| `base_resp.status_msg` | string | Status message |

### Two-Step Workflow

```
Step 1: POST /v1/lyrics_generation
        Input:  { mode: "write_full_song", prompt: "theme description" }
        Output: { song_title, style_tags, lyrics }

Step 2: POST /v1/music_generation
        Input:  { model: "music-2.5", prompt: style_tags, lyrics: lyrics }
        Output: { data.audio (url or hex) }
```

---

## Audio Quality Presets

### Low Bandwidth (smallest file)
```json
{ "sample_rate": 16000, "bitrate": 64000, "format": "mp3" }
```

### Preview / Draft
```json
{ "sample_rate": 24000, "bitrate": 128000, "format": "mp3" }
```

### Standard (recommended default)
```json
{ "sample_rate": 44100, "bitrate": 256000, "format": "mp3" }
```

### Professional / DAW Import
```json
{ "sample_rate": 44100, "bitrate": 256000, "format": "wav" }
```

---

## Rate Limits and Pricing

| Tier | Monthly Cost | Credits | RPM (requests/min) |
| --- | --- | --- | --- |
| Starter | $5 | 100,000 | 10 |
| Standard | $30 | 300,000 | 50 |
| Pro | $99 | 1,100,000 | 200 |
| Scale | $249 | 3,300,000 | 500 |
| Business | $999 | 20,000,000 | 800 |

Credits consumed per generation are based on audio duration. Audio URLs expire after 24 hours.
FILE:references/prompt-engineering-guide.md
# Music Prompt Engineering Guide

## The 8-Component Formula

Build prompts by combining these components. Not all are required — use 4-6 for typical requests.

```
[Genre/Style], [Era/Reference], [Mood/Emotion], [Vocal Type], [Tempo/BPM], [Instruments], [Production Style], [Atmosphere]
```

### Component Details

**1. Genre/Style**
Indie folk, Progressive house, Soulful blues, Pop ballad, Jazz fusion, Synthwave, Ambient electronic, Country rock, Hip-hop boom bap, Classical orchestral, R&B, Disco funk, Lo-fi indie, Metal

**2. Era/Reference**
1960s Motown, 70s disco, 80s synthwave, 90s grunge, 2000s pop-punk, modern, retro, vintage, contemporary, classic

**3. Mood/Emotion**
melancholic, euphoric, nostalgic, hopeful, bittersweet, triumphant, yearning, peaceful, brooding, playful, intense, dreamy, defiant, tender, wistful, anthemic

**4. Vocal Type**
breathy female alto, powerful soprano, raspy male tenor, warm baritone, deep resonant bass, falsetto, husky, crystal clear, choir harmonies, a cappella, duet, operatic

**5. Tempo/BPM**
slow 60 BPM, ballad tempo 70 BPM, mid-tempo 100 BPM, upbeat 120 BPM, driving 128 BPM, fast-paced 140 BPM, energetic 160 BPM

**6. Instruments**
acoustic guitar, electric guitar, fingerpicked guitar, piano, Rhodes piano, upright bass, electric bass, drums, brushed snare, synthesizer, strings, violin, cello, trumpet, saxophone, harmonica, ukulele, banjo, mandolin, flute, organ, harp, percussion, congas, tambourine, vibraphone, steel drums

**7. Production Style**
lo-fi, polished pop production, raw live recording, studio quality, bedroom recording, vinyl warmth, analog tape, digital crisp, spacious reverb, dry and intimate, heavily compressed, minimalist

**8. Atmosphere**
intimate, epic, dreamy, cinematic, ethereal, gritty, lush, sparse, warm, cold, dark, bright, urban, pastoral, cosmic, underground

---

## Genre-Specific Prompt Templates

### Pop
```
Upbeat pop, catchy chorus, synthesizer, four-on-the-floor beat, bright female vocals, radio-ready production, energetic 120 BPM
```

### Pop Ballad
```
Pop ballad, emotional, piano-driven, powerful female vocals with vibrato, sweeping strings, slow tempo 70 BPM, polished production, heartfelt
```

### Indie Folk
```
Indie folk, melancholic, introspective, acoustic fingerpicking guitar, soft piano, gentle male vocals, intimate bedroom recording, 90 BPM
```

### Soulful Blues
```
Soulful blues, rainy night, melancholy, raspy male vocals, slow tempo 65 BPM, electric guitar, upright bass, harmonica, warm analog feel
```

### Jazz
```
Jazz ballad, warm and intimate, upright bass, brushed snare, piano, muted trumpet, 1950s club atmosphere, smooth male vocals, 80 BPM
```

### Electronic / Dance
```
Progressive house, euphoric, driving bassline, 128 BPM, synthesizer pads, arpeggiated leads, modern production, festival energy, build-ups and drops
```

### Rock
```
Indie rock, anthemic, distorted electric guitar, powerful drum kit, passionate male vocals, stadium feel, energetic 140 BPM, raw energy
```

### Classical / Orchestral
```
Orchestral, sweeping strings, French horn, dramatic tension, cinematic, full symphony, dynamic crescendos, epic and majestic
```

### Hip-Hop
```
Lo-fi hip hop, boom bap, vinyl crackle, jazzy piano sample, relaxed beat 85 BPM, introspective mood, head-nodding groove
```

### R&B
```
Contemporary R&B, smooth, falsetto male vocals, Rhodes piano, muted guitar, late night urban feel, 90 BPM, lush production
```

### Country / Americana
```
Appalachian folk, storytelling, acoustic fingerpicking, fiddle, raw and honest, dusty americana, warm male vocals, 100 BPM
```

### Metal
```
Heavy metal, distorted riffs, double kick drum, aggressive powerful vocals, dark atmosphere, intense and relentless, 160 BPM
```

### Synthwave / 80s
```
Synthwave, 80s retro, pulsing synthesizers, gated reverb drums, neon-lit atmosphere, driving arpeggios, nostalgic and cinematic, 110 BPM
```

### Lo-fi Indie
```
Lo-fi indie pop, mellow 92 BPM, soft female vocals airy and intimate, clean electric guitar, lo-fi drums, vinyl warmth, bedroom recording aesthetic, late night melancholy
```

### Disco Funk
```
Disco funk, groovy bassline, wah-wah guitar, brass section, four-on-the-floor kick, 115 BPM, energetic female vocals, sparkling production, dancefloor energy
```

---

## Vocal Descriptor Catalog

### Female Vocals
- `breathy female vocal with emotional delivery and subtle vibrato`
- `powerful soprano, clear and soaring, with controlled dynamics`
- `soft, intimate female alto, whispery and gentle`
- `sassy, confident female voice with rhythmic phrasing`
- `ethereal, angelic female vocal with layered harmonies`
- `raspy, soulful female voice with blues inflection`

### Male Vocals
- `warm baritone, smooth and resonant, with emotional depth`
- `raspy male tenor with rock edge and raw power`
- `deep, resonant bass voice, commanding and rich`
- `falsetto male vocal, airy and delicate, R&B style`
- `gravelly crooner, vintage jazz feel, intimate delivery`
- `powerful tenor with soaring high notes and controlled vibrato`

### Ensemble / Special
- `male-female duet with harmonized chorus`
- `choir harmonies, layered voices, cathedral reverb`
- `a cappella vocal arrangement, no instruments`
- `spoken word with musical backing`
- `vocal ad-libs and runs between main phrases`

---

## Mood/Emotion Vocabulary

These descriptors map well to Minimax's training:

| Category | Words |
| --- | --- |
| Sad | melancholic, bittersweet, yearning, wistful, somber, mournful, lonely |
| Happy | euphoric, joyful, uplifting, celebratory, playful, carefree, sunny |
| Intense | driving, powerful, fierce, relentless, urgent, explosive, raw |
| Calm | peaceful, serene, meditative, tranquil, floating, gentle, soothing |
| Dark | brooding, ominous, haunting, sinister, shadowy, tense, mysterious |
| Romantic | tender, intimate, warm, passionate, longing, devoted, sensual |
| Epic | triumphant, majestic, anthemic, soaring, grandiose, cinematic, sweeping |
| Nostalgic | retro, vintage, throwback, reminiscent, dreamy, hazy, faded |

---

## Anti-Patterns to Avoid

### Negations (DON'T USE)
The model does not reliably process negative instructions.

| Bad | Good |
| --- | --- |
| "no drums" | "acoustic guitar and piano only" |
| "without vocals" | use `[Inst]` tags in lyrics |
| "not too fast" | "slow tempo 70 BPM" |
| "don't use autotune" | "raw, natural vocal delivery" |

### Conflicting Styles
Do not combine contradictory aesthetics:

| Conflict | Why |
| --- | --- |
| "vintage lo-fi" + "crisp modern production" | lo-fi and crisp are opposites |
| "intimate whisper" + "powerful belting" | can't be both simultaneously |
| "minimalist" + "full orchestra" | sparse vs. dense |
| "raw punk" + "polished pop production" | production styles clash |

### Overly Generic (Too Vague)

| Weak | Strong |
| --- | --- |
| "sad song with guitar" | "melancholic indie folk, fingerpicked acoustic guitar, male vocals, intimate, 85 BPM" |
| "happy music" | "upbeat pop, bright female vocals, synth and piano, 120 BPM, radio-ready" |
| "rock song" | "indie rock, anthemic, distorted electric guitar, driving drums, passionate vocals, 140 BPM" |
| "electronic music" | "progressive house, euphoric, 128 BPM, synthesizer pads, driving bassline" |

---

## Prompt Refinement Checklist

When reviewing a prompt, check:

1. Does it specify a genre? (e.g., "indie folk" not just "folk")
2. Does it include mood/emotion? (at least one descriptor)
3. Does it name specific instruments? (not just "music")
4. Does it indicate tempo or energy level? (BPM or descriptor)
5. Does it describe the vocal style? (if the song has vocals)
6. Is it under 2000 characters?
7. Are there any negations to rewrite?
8. Are there any conflicting style combinations?
FILE:references/error-codes.md
# Minimax API Error Reference

## Error Code Table

| Code | Name | Cause | Fix |
| --- | --- | --- | --- |
| `0` | Success | Request completed | No action needed |
| `1002` | Rate Limited | Too many requests per minute | Wait 10-30 seconds and retry with exponential backoff |
| `1004` | Auth Failed | Invalid, expired, or missing API key | Verify key at platform.minimax.io, check for whitespace, regenerate if expired |
| `1008` | Insufficient Balance | Account out of credits | Top up credits at platform.minimax.io > Billing |
| `1026` | Content Flagged | Lyrics or prompt triggered content moderation | Revise lyrics/prompt to remove sensitive, violent, or explicit content |
| `2013` | Invalid Parameters | Request body has wrong types or out-of-range values | Validate all parameters against the API schema |
| `2049` | Invalid API Key Format | API key string is malformed | Check for trailing newlines, extra spaces, or copy-paste errors |

## Troubleshooting Decision Tree

```
Got an error response?
│
├─ Check base_resp.status_code
│
├─ 1002 (Rate Limited)
│  ├─ Are you sending many requests? → Add delay between calls
│  ├─ Only one request? → Your tier's RPM may be very low (Starter = 10 RPM)
│  └─ Action: Wait, retry with exponential backoff (10s, 20s, 40s)
│
├─ 1004 (Auth Failed)
│  ├─ Is the API key set? → Check Authorization header format
│  ├─ Is it a Coding Plan key? → Music needs Pay-as-you-go key
│  ├─ Has the key expired? → Regenerate at platform.minimax.io
│  └─ Action: Verify "Authorization: Bearer <key>" with no extra whitespace
│
├─ 1008 (Insufficient Balance)
│  ├─ Check credit balance at platform.minimax.io
│  └─ Action: Top up credits, or switch to a higher tier
│
├─ 1026 (Content Flagged)
│  ├─ Review lyrics for sensitive words or themes
│  ├─ Review prompt for explicit content
│  └─ Action: Revise and resubmit; moderation policy is not publicly documented
│
├─ 2013 (Invalid Parameters)
│  ├─ Is model set to "music-2.5"? (not "music-01" or other)
│  ├─ Is lyrics between 1-3500 chars?
│  ├─ Is prompt under 2000 chars?
│  ├─ Is sample_rate one of: 16000, 24000, 32000, 44100?
│  ├─ Is bitrate one of: 32000, 64000, 128000, 256000?
│  ├─ Is format one of: "mp3", "wav", "pcm"?
│  ├─ Is output_format one of: "hex", "url"?
│  └─ Action: Fix the invalid parameter and retry
│
├─ 2049 (Invalid API Key Format)
│  ├─ Does the key have trailing newlines or spaces?
│  ├─ Was it copied correctly from the dashboard?
│  └─ Action: Re-copy the key, trim whitespace
│
└─ data.status === 1 (Not an error!)
   └─ Generation is still in progress. Poll again or wait for completion.
```

## Common Parameter Mistakes

| Mistake | Problem | Fix |
| --- | --- | --- |
| `"model": "music-01"` | Wrong model for native API | Use `"music-2.5"` |
| `"lyrics": ""` | Empty lyrics string | Lyrics must be 1-3500 chars |
| `"sample_rate": 48000` | Invalid sample rate | Use 16000, 24000, 32000, or 44100 |
| `"bitrate": 320000` | Invalid bitrate | Use 32000, 64000, 128000, or 256000 |
| `"format": "flac"` | Unsupported format | Use "mp3", "wav", or "pcm" |
| `"stream": true` + `"output_format": "url"` | Streaming only supports hex | Set `output_format` to `"hex"` or disable streaming |
| Missing `Content-Type` header | Server can't parse JSON | Add `Content-Type: application/json` |
| Key with trailing `\n` | Auth fails silently | Trim the key string |
| Prompt over 2000 chars | Rejected by API | Shorten the prompt |
| Lyrics over 3500 chars | Rejected by API | Shorten lyrics or remove structure tags |

## HTTP Status Codes

| HTTP Status | Meaning | Action |
| --- | --- | --- |
| `200` | Request processed | Check `base_resp.status_code` for API-level errors |
| `401` | Unauthorized | API key missing or invalid |
| `429` | Too Many Requests | Rate limited — back off and retry |
| `500` | Server Error | Retry after a short delay |
| `503` | Service Unavailable | Minimax servers overloaded — retry later |
FILE:examples/code-examples.md
# Code Examples

All examples load the API key from the `.env` file via environment variables.

---

## Python: Music Generation (URL Output)

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MINIMAX_API_KEY")

def generate_music(prompt, lyrics, output_file="output.mp3"):
    response = requests.post(
        "https://api.minimax.io/v1/music_generation",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "music-2.5",
            "prompt": prompt,
            "lyrics": lyrics,
            "audio_setting": {
                "sample_rate": 44100,
                "bitrate": 256000,
                "format": "mp3"
            },
            "output_format": "url"
        }
    )
    response.raise_for_status()
    result = response.json()

    if result["base_resp"]["status_code"] != 0:
        raise Exception(f"API error {result['base_resp']['status_code']}: {result['base_resp']['status_msg']}")

    audio_url = result["data"]["audio"]
    duration = result["extra_info"]["music_duration"]
    print(f"Generated {duration:.1f}s of music")

    audio_data = requests.get(audio_url)
    with open(output_file, "wb") as f:
        f.write(audio_data.content)
    print(f"Saved to {output_file}")
    return result

# Usage
generate_music(
    prompt="Indie folk, melancholic, acoustic guitar, soft piano, female vocals",
    lyrics="""[Intro]

[Verse]
Walking through the autumn leaves
Nobody knows where I've been

[Chorus]
Every road leads back to you
Every song I hear rings true

[Outro]
""",
    output_file="my_song.mp3"
)
```

---

## Python: Music Generation (Hex Output)

```python
import os
import binascii
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MINIMAX_API_KEY")

def generate_music_hex(prompt, lyrics, output_file="output.mp3"):
    response = requests.post(
        "https://api.minimax.io/v1/music_generation",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "music-2.5",
            "prompt": prompt,
            "lyrics": lyrics,
            "audio_setting": {
                "sample_rate": 44100,
                "bitrate": 256000,
                "format": "mp3"
            },
            "output_format": "hex"
        }
    )
    response.raise_for_status()
    result = response.json()

    if result["base_resp"]["status_code"] != 0:
        raise Exception(f"API error: {result['base_resp']['status_msg']}")

    audio_bytes = binascii.unhexlify(result["data"]["audio"])
    with open(output_file, "wb") as f:
        f.write(audio_bytes)
    print(f"Saved {len(audio_bytes)} bytes to {output_file}")
```

---

## Python: Two-Step Workflow (Lyrics then Music)

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MINIMAX_API_KEY")
BASE_URL = "https://api.minimax.io/v1"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_lyrics(theme):
    """Step 1: Generate structured lyrics from a theme."""
    response = requests.post(
        f"{BASE_URL}/lyrics_generation",
        headers=HEADERS,
        json={
            "mode": "write_full_song",
            "prompt": theme
        }
    )
    response.raise_for_status()
    data = response.json()
    if data["base_resp"]["status_code"] != 0:
        raise Exception(f"Lyrics error: {data['base_resp']['status_msg']}")
    return data

def generate_music(style_prompt, lyrics, output_file="song.mp3"):
    """Step 2: Generate music from lyrics and a style prompt."""
    response = requests.post(
        f"{BASE_URL}/music_generation",
        headers=HEADERS,
        json={
            "model": "music-2.5",
            "prompt": style_prompt,
            "lyrics": lyrics,
            "audio_setting": {
                "sample_rate": 44100,
                "bitrate": 256000,
                "format": "mp3"
            },
            "output_format": "url"
        }
    )
    response.raise_for_status()
    result = response.json()
    if result["base_resp"]["status_code"] != 0:
        raise Exception(f"Music error: {result['base_resp']['status_msg']}")

    audio_data = requests.get(result["data"]["audio"])
    with open(output_file, "wb") as f:
        f.write(audio_data.content)
    print(f"Saved to {output_file} ({result['extra_info']['music_duration']:.1f}s)")
    return result

# Full workflow
theme = "A soulful blues song about a rainy night and lost love"
style = "Soulful blues, rainy night, melancholy, male vocals, slow tempo, electric guitar, upright bass"

print("Step 1: Generating lyrics...")
lyrics_data = generate_lyrics(theme)
print(f"Title: {lyrics_data['song_title']}")
print(f"Style: {lyrics_data['style_tags']}")
print(f"Lyrics:\n{lyrics_data['lyrics']}\n")

print("Step 2: Generating music...")
generate_music(style, lyrics_data["lyrics"], "blues_song.mp3")
```

---

## Python: Streaming Response

```python
import os
import json
import binascii
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MINIMAX_API_KEY")

def generate_music_streaming(prompt, lyrics, output_file="stream_output.mp3"):
    response = requests.post(
        "https://api.minimax.io/v1/music_generation",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "music-2.5",
            "prompt": prompt,
            "lyrics": lyrics,
            "audio_setting": {
                "sample_rate": 44100,
                "bitrate": 256000,
                "format": "mp3"
            },
            "output_format": "hex",
            "stream": True
        },
        stream=True
    )
    response.raise_for_status()

    chunks = []
    for line in response.iter_lines():
        if not line:
            continue
        line_str = line.decode("utf-8")
        if not line_str.startswith("data:"):
            continue
        data = json.loads(line_str[5:].strip())

        if data.get("base_resp", {}).get("status_code", 0) != 0:
            raise Exception(f"Stream error: {data['base_resp']['status_msg']}")

        if data.get("data", {}).get("status") == 1 and data["data"].get("audio"):
            chunks.append(binascii.unhexlify(data["data"]["audio"]))

    audio_bytes = b"".join(chunks)
    with open(output_file, "wb") as f:
        f.write(audio_bytes)
    print(f"Streaming complete: {len(audio_bytes)} bytes saved to {output_file}")
```

---

## JavaScript / Node.js: Music Generation (URL Output)

```javascript
import "dotenv/config";
import { writeFile } from "fs/promises";

const API_KEY = process.env.MINIMAX_API_KEY;

async function generateMusic(prompt, lyrics, outputPath = "output.mp3") {
  const response = await fetch("https://api.minimax.io/v1/music_generation", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "music-2.5",
      prompt,
      lyrics,
      audio_setting: { sample_rate: 44100, bitrate: 256000, format: "mp3" },
      output_format: "url",
    }),
  });

  const result = await response.json();

  if (result.base_resp?.status_code !== 0) {
    throw new Error(`API Error ${result.base_resp?.status_code}: ${result.base_resp?.status_msg}`);
  }

  const audioUrl = result.data.audio;
  const audioResponse = await fetch(audioUrl);
  const audioBuffer = Buffer.from(await audioResponse.arrayBuffer());

  await writeFile(outputPath, audioBuffer);
  console.log(`Saved to ${outputPath} (${result.extra_info.music_duration.toFixed(1)}s)`);
  return result;
}

// Usage
await generateMusic(
  "Pop, upbeat, energetic, female vocals, synthesizer, driving beat",
  `[Verse]
Running through the city lights
Everything is burning bright

[Chorus]
We are alive tonight
Dancing through the neon light`,
  "pop_song.mp3"
);
```

---

## JavaScript / Node.js: Hex Output with Decode

```javascript
import "dotenv/config";
import { writeFile } from "fs/promises";

const API_KEY = process.env.MINIMAX_API_KEY;

async function generateMusicHex(prompt, lyrics, outputPath = "output.mp3") {
  const response = await fetch("https://api.minimax.io/v1/music_generation", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "music-2.5",
      prompt,
      lyrics,
      audio_setting: { sample_rate: 44100, bitrate: 256000, format: "mp3" },
      output_format: "hex",
    }),
  });

  const result = await response.json();

  if (result.base_resp?.status_code !== 0) {
    throw new Error(`API Error: ${result.base_resp?.status_msg}`);
  }

  const audioBuffer = Buffer.from(result.data.audio, "hex");
  await writeFile(outputPath, audioBuffer);
  console.log(`Saved ${audioBuffer.length} bytes to ${outputPath}`);
}
```

---

## JavaScript / Node.js: Streaming

```javascript
import "dotenv/config";
import { writeFile } from "fs/promises";

const API_KEY = process.env.MINIMAX_API_KEY;

async function generateMusicStreaming(prompt, lyrics, outputPath = "stream_output.mp3") {
  const response = await fetch("https://api.minimax.io/v1/music_generation", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "music-2.5",
      prompt,
      lyrics,
      audio_setting: { sample_rate: 44100, bitrate: 256000, format: "mp3" },
      output_format: "hex",
      stream: true,
    }),
  });

  const chunks = [];
  const decoder = new TextDecoder();
  const reader = response.body.getReader();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    let boundary;

    while ((boundary = buffer.indexOf("\n\n")) !== -1) {
      const event = buffer.slice(0, boundary).trim();
      buffer = buffer.slice(boundary + 2);

      if (!event) continue;
      const dataMatch = event.match(/^data:\s*(.+)$/m);
      if (!dataMatch) continue;

      const parsed = JSON.parse(dataMatch[1]);

      if (parsed.base_resp?.status_code !== 0) {
        throw new Error(`Stream error: ${parsed.base_resp?.status_msg}`);
      }

      if (parsed.data?.status === 1 && parsed.data?.audio) {
        chunks.push(Buffer.from(parsed.data.audio, "hex"));
      }
    }
  }

  const fullAudio = Buffer.concat(chunks);
  await writeFile(outputPath, fullAudio);
  console.log(`Streaming complete: ${fullAudio.length} bytes saved to ${outputPath}`);
}
```

---

## cURL: Music Generation

```bash
curl -X POST "https://api.minimax.io/v1/music_generation" \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "music-2.5",
    "prompt": "Indie folk, melancholic, acoustic guitar, soft piano",
    "lyrics": "[Verse]\nWalking through the autumn leaves\nNobody knows where I have been\n\n[Chorus]\nEvery road leads back to you\nEvery song I hear rings true",
    "audio_setting": {
      "sample_rate": 44100,
      "bitrate": 256000,
      "format": "mp3"
    },
    "output_format": "url"
  }'
```

---

## cURL: Lyrics Generation

```bash
curl -X POST "https://api.minimax.io/v1/lyrics_generation" \
  -H "Authorization: Bearer $MINIMAX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "mode": "write_full_song",
    "prompt": "A soulful blues song about a rainy night and lost love"
  }'
```

---

## Audio Quality Presets

### Python dict presets
```python
QUALITY_LOW = {"sample_rate": 16000, "bitrate": 64000, "format": "mp3"}
QUALITY_PREVIEW = {"sample_rate": 24000, "bitrate": 128000, "format": "mp3"}
QUALITY_STANDARD = {"sample_rate": 44100, "bitrate": 256000, "format": "mp3"}
QUALITY_PROFESSIONAL = {"sample_rate": 44100, "bitrate": 256000, "format": "wav"}
```

### JavaScript object presets
```javascript
const QUALITY_LOW = { sample_rate: 16000, bitrate: 64000, format: "mp3" };
const QUALITY_PREVIEW = { sample_rate: 24000, bitrate: 128000, format: "mp3" };
const QUALITY_STANDARD = { sample_rate: 44100, bitrate: 256000, format: "mp3" };
const QUALITY_PROFESSIONAL = { sample_rate: 44100, bitrate: 256000, format: "wav" };
```
FILE:examples/lyrics-templates.md
# Lyrics Templates

## Song Structure Patterns

Common arrangements as tag sequences:

**Standard Pop/Rock:**
`[Intro] → [Verse] → [Pre Chorus] → [Chorus] → [Verse] → [Pre Chorus] → [Chorus] → [Bridge] → [Chorus] → [Outro]`

**Ballad:**
`[Intro] → [Verse] → [Verse] → [Chorus] → [Verse] → [Chorus] → [Bridge] → [Chorus] → [Outro]`

**Electronic/Dance:**
`[Intro] → [Build Up] → [Chorus] → [Break] → [Verse] → [Build Up] → [Chorus] → [Outro]`

**Simple/Short:**
`[Verse] → [Chorus] → [Verse] → [Chorus] → [Outro]`

**Progressive/Epic:**
`[Intro] → [Verse] → [Pre Chorus] → [Chorus] → [Interlude] → [Verse] → [Pre Chorus] → [Chorus] → [Bridge] → [Solo] → [Build Up] → [Chorus] → [Outro]`

---

## Pop Song Template

```
[Intro]

[Verse]
Morning light breaks through my window pane
Another day I try to start again
The coffee's cold, the silence fills the room
But something tells me change is coming soon

[Pre Chorus]
I can feel it in the air tonight
Something shifting, pulling me toward the light

[Chorus]
I'm breaking through the walls I built
Letting go of all this guilt
Every step I take is mine
I'm finally feeling fine
I'm breaking through

[Verse]
The photographs are fading on the shelf
I'm learning how to just be myself
No more hiding underneath the weight
Of everything I thought would make me great

[Pre Chorus]
I can feel it in the air tonight
Something shifting, pulling me toward the light

[Chorus]
I'm breaking through the walls I built
Letting go of all this guilt
Every step I take is mine
I'm finally feeling fine
I'm breaking through

[Bridge]
It took so long to see
The only one holding me back was me

[Chorus]
I'm breaking through the walls I built
Letting go of all this guilt
Every step I take is mine
I'm finally feeling fine
I'm breaking through

[Outro]
```

---

## Rock Song Template

```
[Intro]

[Verse]
Engines roar on an empty highway
Headlights cutting through the dark
Running from the life I used to know
Chasing down a distant spark

[Verse]
Radio plays our broken anthem
Windows down and letting go
Every mile puts it all behind me
Every sign says don't look home

[Pre Chorus]
Tonight we burn it all
Tonight we rise or fall

[Chorus]
We are the reckless hearts
Tearing the world apart
Nothing can stop this fire inside
We are the reckless hearts

[Inst]

[Verse]
Streetlights flicker like a warning
But I'm too far gone to care
Took the long road out of nowhere
Found myself already there

[Pre Chorus]
Tonight we burn it all
Tonight we rise or fall

[Chorus]
We are the reckless hearts
Tearing the world apart
Nothing can stop this fire inside
We are the reckless hearts

[Bridge]
They said we'd never make it
Said we'd crash and burn
But look at us still standing
Every scar a lesson learned

[Solo]

[Build Up]
We are we are we are

[Chorus]
We are the reckless hearts
Tearing the world apart
Nothing can stop this fire inside
We are the reckless hearts

[Outro]
```

---

## Ballad Template

```
[Intro]

[Verse]
The winter trees are bare and still
Snow falls softly on the hill
I remember when you held my hand
Walking paths we used to plan

[Verse]
Your laughter echoes in these halls
Your name is written on these walls
Time has taken what we had
But memories still make me glad

[Chorus]
I will carry you with me
Through the storms and through the sea
Even when the world goes dark
You're the ember in my heart
I will carry you

[Verse]
The seasons change but I remain
Standing here through sun and rain
Every star I see at night
Reminds me of your gentle light

[Chorus]
I will carry you with me
Through the storms and through the sea
Even when the world goes dark
You're the ember in my heart
I will carry you

[Bridge]
And if the years should wash away
Every word I meant to say
Know that love was always true
Every moment led to you

[Chorus]
I will carry you with me
Through the storms and through the sea
Even when the world goes dark
You're the ember in my heart
I will carry you

[Outro]
```

---

## Hip-Hop / R&B Template

```
[Intro]

[Verse]
City lights reflecting off the rain
Another late night grinding through the pain
Started from the bottom with a dream
Nothing's ever easy as it seems
Momma said to keep my head up high
Even when the storm clouds fill the sky
Now I'm standing tall above the noise
Found my voice and made a choice

[Hook]
We don't stop we keep it moving
Every day we keep on proving
That the grind don't stop for nothing
We keep pushing keep on hustling

[Verse]
Look around at everything we built
From the ashes rising no more guilt
Every scar a story that I own
Seeds of struggle finally have grown
Late nights early mornings on repeat
Every setback made the win more sweet
Now they see the vision crystal clear
We've been building this for years

[Hook]
We don't stop we keep it moving
Every day we keep on proving
That the grind don't stop for nothing
We keep pushing keep on hustling

[Bridge]
From the bottom to the top
We don't know how to stop

[Hook]
We don't stop we keep it moving
Every day we keep on proving
That the grind don't stop for nothing
We keep pushing keep on hustling

[Outro]
```

---

## Electronic / Dance Template

```
[Intro]

[Build Up]
Feel the pulse beneath the floor
Can you hear it wanting more

[Chorus]
Lose yourself in neon lights
We're alive alive tonight
Let the music take control
Feel the rhythm in your soul
We're alive alive tonight

[Break]

[Verse]
Strangers dancing side by side
In this moment nothing to hide
Every heartbeat syncs in time
Lost in rhythm lost in rhyme

[Build Up]
Feel the pulse beneath the floor
Can you hear it wanting more
Louder louder

[Chorus]
Lose yourself in neon lights
We're alive alive tonight
Let the music take control
Feel the rhythm in your soul
We're alive alive tonight

[Inst]

[Build Up]
One more time

[Chorus]
Lose yourself in neon lights
We're alive alive tonight
Let the music take control
Feel the rhythm in your soul
We're alive alive tonight

[Outro]
```

---

## Folk / Acoustic Template

```
[Intro]

[Verse]
Down by the river where the willows lean
I found a letter in the autumn green
Words like water flowing soft and slow
Telling stories from so long ago

[Verse]
My grandfather walked these roads before
Carried burdens through a world at war
But he never lost his gentle way
And his kindness lives in me today

[Chorus]
These old roads remember everything
Every footstep every song we sing
Through the valleys and the mountain air
Love is planted everywhere
These old roads remember

[Verse]
Now the seasons paint the hills with gold
And the stories keep the young from cold
Every sunset brings a quiet prayer
For the ones who are no longer there

[Chorus]
These old roads remember everything
Every footstep every song we sing
Through the valleys and the mountain air
Love is planted everywhere
These old roads remember

[Bridge]
So I'll walk a little further still
Past the chapel on the distant hill
And I'll listen for the echoes there
Carried softly through the evening air

[Chorus]
These old roads remember everything
Every footstep every song we sing
Through the valleys and the mountain air
Love is planted everywhere
These old roads remember

[Outro]
```

---

## Jazz Template

```
[Intro]

[Verse]
Smoke curls slowly in the amber light
Piano whispers through the velvet night
A glass of something golden in my hand
The drummer keeps a brushstroke on the snare

[Verse]
She walked in like a song I used to know
A melody from many years ago
Her smile could melt the winter off the glass
Some moments were not meant to ever last

[Chorus]
But we danced until the morning came
Two strangers playing at a nameless game
The saxophone was crying soft and low
And neither one of us wanted to go

[Solo]

[Verse]
The city sleeps but we are wide awake
Sharing secrets for each other's sake
Tomorrow we'll be strangers once again
But tonight we're more than just old friends

[Chorus]
And we danced until the morning came
Two strangers playing at a nameless game
The saxophone was crying soft and low
And neither one of us wanted to go

[Outro]
```

---

## Instrumental-Only Templates

### Cinematic Instrumental
```
[Intro]

[Inst]
(Soft piano, building strings)

[Build Up]
(Full orchestra swelling)

[Inst]
(Triumphant brass and percussion)

[Interlude]
(Gentle woodwinds, reflective)

[Build Up]
(Timpani roll, rising tension)

[Inst]
(Full symphonic climax)

[Outro]
(Fading strings, peaceful resolution)
```

### Guitar Solo Showcase
```
[Intro]

[Inst]
(Rhythm guitar and bass groove)

[Solo]
(Lead guitar melody)

[Inst]
(Full band groove)

[Solo]
(Extended guitar solo, building intensity)

[Break]

[Solo]
(Final guitar solo, emotional peak)

[Outro]
```

### Ambient / Atmospheric
```
[Intro]

[Inst]
(Ethereal synth pads, slow evolution)

[Transition]

[Inst]
(Layered textures, subtle percussion)

[Interlude]
(Minimal, spacious)

[Build Up]
(Gradually intensifying)

[Inst]
(Full atmospheric wash)

[Outro]
(Slowly dissolving into silence)
```
