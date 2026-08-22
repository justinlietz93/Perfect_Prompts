{
  "category": "CAR_PASSENGER_SEAT_SELFIE",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Lock identity to reference image exactly. Preserve face proportions, features, and skin tone. Adult 21+ only."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking (match reference).",
    "hair": {
      "color": "Match reference.",
      "style": "Loose, slightly wind-touched",
      "texture": "Individual strands visible; a few flyaways",
      "movement": "Hair resting on shoulder with subtle motion"
    },
    "face": {
      "eyes": "Exact reference shape; bright catchlights from window",
      "skin_details": "Pores visible, warm glow; no smoothing",
      "micro_details": "Preserve marks exactly"
    },
    "clothing": {
      "top": "Casual black top or hoodie (no logos/text)",
      "texture": "Cotton weave visible"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Handheld selfie vibe (do not show phone)",
    "orientation": "Close-up to half-body",
    "head_position": "Slight tilt toward window light",
    "limbs": "One arm implied holding camera out of frame",
    "gaze": "Direct eye contact",
    "expression": "Confident relaxed pout (subtle, not exaggerated)"
  },
  "setting": {
    "environment": "Car passenger seat",
    "background_elements": [
      "Seat fabric texture visible",
      "Window light streaks",
      "Outside scenery blurred (no readable signs)"
    ],
    "depth": "Face sharp; background soft blur"
  },
  "camera": {
    "shot_type": "Selfie-style portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "24-28mm smartphone wide",
    "framing": "3:4 or 4:5, chest-up crop",
    "focus": "Eyes sharp; slight fall-off at shoulders"
  },
  "lighting": {
    "source": "Golden hour sunlight through car window",
    "direction": "Side/front warm",
    "highlights": "Warm highlight on cheek and hair",
    "shadows": "Soft under-chin shadow, realistic contrast"
  },
  "mood_and_expression": {
    "tone": "Casual, confident, candid",
    "atmosphere": "Warm travel moment"
  },
  "style_and_realism": {
    "style": "Photorealistic social selfie",
    "imperfections": "Mild noise, slight imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Mild grain in shadows",
    "mode_variants": {
      "amateur": "Slightly shaky framing, subtle motion blur away from face, phone-like HDR",
      "pro": "Cleaner exposure and sharper micro-contrast, still realistic"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_outside_signs": true
  },
  "negative_prompt": [
    "identity drift", "face morphing",
    "warped car interior", "duplicate subject",
    "extra fingers", "bad anatomy",
    "readable text", "logos", "watermark",
    "plastic skin", "over-smoothing"
  ]
}
