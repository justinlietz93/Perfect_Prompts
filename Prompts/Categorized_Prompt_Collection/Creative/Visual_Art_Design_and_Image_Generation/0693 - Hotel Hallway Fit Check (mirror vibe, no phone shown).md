{
  "category": "HOTEL_HALLWAY_FIT_CHECK",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Preserve exact reference identity. Adult 21+ only. No face/ethnicity changes."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Sleek ponytail or loose waves",
      "texture": "Natural strands, mild flyaways"
    },
    "face": {
      "eyes": "Exact reference eyes; confident gaze",
      "skin_details": "Natural texture, pores visible"
    },
    "clothing": {
      "outfit": "Minimal black travel outfit (no logos/text)",
      "fabric": "Fabric weave visible, subtle wrinkles"
    },
    "accessories": {
      "jewelry": [
        "Small silver hoops"
      ],
      "bag": "Small shoulder bag (no logos)"
    }
  },
  "pose": {
    "type": "Fit-check candid",
    "orientation": "Full-body or three-quarter",
    "hands": "One hand adjusting jacket hem; other holding bag strap",
    "gaze": "Looking at mirror reflection (no phone visible)",
    "expression": "Neutral confident"
  },
  "setting": {
    "environment": "Hotel hallway",
    "background_elements": [
      "Warm wall sconces",
      "Carpet texture visible",
      "Door frames blurred (no room numbers readable)"
    ],
    "depth": "Subject sharp; background softly blurred"
  },
  "camera": {
    "shot_type": "Full-body hallway portrait",
    "angle": "Slightly low for height OR eye level",
    "focal_length_equivalent": "26mm phone or 35mm editorial",
    "framing": "4:5",
    "focus": "Face and outfit sharp"
  },
  "lighting": {
    "source": "Warm hallway sconces",
    "direction": "Top/side warm",
    "highlights": "Warm rim on hair",
    "shadows": "Soft"
  },
  "mood_and_expression": {
    "tone": "Travel chic, quiet luxury",
    "atmosphere": "Candid but composed"
  },
  "style_and_realism": {
    "style": "Photoreal lifestyle",
    "imperfections": "Slight noise, mild tilt allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Mild indoor grain",
    "mode_variants": {
      "amateur": "Slightly crooked handheld framing, mild grain, imperfect crop",
      "pro": "Clean editorial exposure, crisp detail, controlled highlights"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_numbers": true
  },
  "negative_prompt": [
    "readable door numbers",
    "readable text",
    "logos",
    "watermark",
    "identity drift",
    "face morphing",
    "extra fingers",
    "warped hands",
    "plastic skin",
    "over-smoothing"
  ]
}
