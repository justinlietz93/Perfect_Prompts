SYSTEM:
You are an LLM prompt executor.

USER TASK:
Create a vertical 9:16 infographic for TikTok.

TITLE (ONLY ONE TITLE — display this at the top):
[Fraud Playbook: Voice Cloning Attacks (2026)]

LAYOUT (choose ONE):
[1-10 box]
Pick exactly one. Number boxes with circled numbers. Flow top-to-bottom.

CONTENT RULES:
Each box must include:
- 1 short subheading
- 2–4 bullet points (plain English, phone-readable)

Must include:
- At least 1 real-world example
- A final checklist/action box whenever possible

QUALITY GATES:
- Tone: professional, neutral, report-like.
- Specificity: include at least 1 concrete detail per box.
- No filler: avoid vague warnings.
- Evidence discipline: label uncertain claims as “unclear/contested.”
- No repetition. Clear and fast to read.

TEXT QUALITY REQUIREMENTS:
- Bullets max 10–12 words.
- Prefer 1-6 box for best readability.

FOOTER CREDIT (small/subtle at the bottom):
By SirCrypto

OUTPUT REQUIREMENT:
Return:
TITLE: [Fraud Playbook: Voice Cloning Attacks (2026)]
BOX 1: ...
...
FOOTER (small): By SirCrypto

Then follow the STYLE SPEC below exactly (DO NOT CHANGE it):

--- STYLE SPEC (DO NOT CHANGE) ---
{
  "layout_options": {
    "box_variants": ["1-2 box", "1-4 box", "1-6 box", "1-8 box", "1-10 box"],
    "remark": "Choose ONE box variant. Keep flow top-to-bottom. Number each box with circled numbers."
  },
  "footer_credit": {
    "text": "By SirCrypto",
    "placement": "Bottom center or bottom right",
    "size": "Small/subtle"
  },
  "style": {
    "name": "War Room Strategy Infographic",
    "description": "Mature command-briefing infographic: tactical labels, decisive callouts, clear hierarchy. Serious, professional."
  },
  "visual_foundation": {
    "surface": {
      "base": "Matte dark slate to charcoal background",
      "texture": "Subtle paper grain + faint chalk/marker smudge texture",
      "edges": "Content extends fully to edges, no border or frame",
      "feel": "Command briefing page on dark paper"
    },
    "overall_impression": "Command-center clarity—direct, credible, high-signal"
  },
  "illustration_style": {
    "line_quality": {
      "type": "Hand-drawn ink/chalk hybrid sketch aesthetic",
      "weight": "Medium strokes for main elements, thinner for details",
      "character": "Confident but imperfect—slight wobble that proves human touch",
      "edges": "Soft, not vector-crisp",
      "fills": "Loose hatching, gentle cross-hatching for shadows, never solid machine fills"
    },
    "icon_treatment": {
      "style": "Minimal tactical icons",
      "complexity": "Essential forms—readable at small sizes",
      "personality": "Professional and decisive, never cute",
      "consistency": "Same hand appears to have drawn everything"
    }
  },
  "color_philosophy": {
    "palette_character": {
      "mood": "Serious, tactical, focused",
      "saturation": "Low-to-medium",
      "harmony": "Muted complementary accents"
    },
    "primary_palette": {
      "ambers": "Muted amber for warnings and priority tags",
      "teals": "Soft teal for steps and logic",
      "off_whites": "Warm off-white ink for main text"
    },
    "color_application": {
      "fills": "Translucent washes behind boxes",
      "accents": "Marker highlight behind keywords (restrained)"
    }
  },
  "typography_integration": {
    "headline_style": {
      "appearance": "Bold hand-lettered feel, slightly uneven baseline",
      "weight": "Heavy, confident",
      "case": "Often uppercase",
      "color": "Warm off-white or muted amber"
    },
    "body_text": {
      "appearance": "Clean readable warm sans-serif",
      "spacing": "Generous"
    }
  },
  "layout_architecture": {
    "canvas": {
      "framing": "NO BORDER, NO FRAME",
      "boundary": "Full-bleed 9:16"
    },
    "structure": {
      "type": "Modular briefing grid",
      "sections": "Numbered boxes per chosen variant",
      "flow": "Top-to-bottom"
    },
    "visual_flow_devices": {
      "arrows": "Hand-drawn curved arrows",
      "connectors": "Dotted lines and braces"
    }
  },
  "technical_quality": {
    "resolution": "High-resolution for phone",
    "clarity": "All text readable",
    "balance": "Not crowded"
  },
  "avoid": [
    "ANY frame, border, or edge decoration",
    "Cute/cartoon characters",
    "Neon overload",
    "Text-dense paragraphs",
    "Sterile vector perfection"
  ]
}

make picture based on these
