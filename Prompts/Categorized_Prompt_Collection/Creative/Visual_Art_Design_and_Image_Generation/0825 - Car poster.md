${primary_text:Megane}{
  "category": "STUDIO_RACE_CAR_SIDE_PROFILE",
  "subject": {
    "vehicle_type": "GT endurance race car",
    "base_form": "Modern GT-class silhouette, low-slung aerodynamic body",
    "branding": {
      "primary_text": "Megane",
      "replacement_rule": "All instances where 'Porsche' branding would normally appear are replaced with 'Megane'",
      "style": "Clean motorsport typography, realistic vinyl application",
      "placement": [
        "Door panel main branding area",
        "Side intake area where manufacturer name is typically placed"
      ]
    },
    "livery": {
      "primary_colors": ["White", "Red", "Black"],
      "pattern": "Sharp motorsport color blocking",
      "finish": "Gloss paint with subtle reflections",
      "decals": "Sponsor-style decals present but non-distracting"
    },
    "details": {
      "aerodynamics": [
        "Large rear wing",
        "Front splitter",
        "Side air intakes",
        "Rear diffuser"
      ],
      "wheels": {
        "type": "Center-lock racing wheels",
        "tires": "Slick racing tires with visible sidewall text",
        "brakes": "Large performance brake discs visible through rims"
      },
      "surface_realism": {
        "panel_lines": "Crisp and accurate",
        "bolts_and_fasteners": "Visible around aero elements",
        "minor_wear": "Subtle race-use marks, not damaged"
      }
    }
  },
  "pose_and_orientation": {
    "view": "Perfect side profile",
    "orientation": "Vehicle aligned horizontally, facing left",
    "stance": "Static studio pose, wheels straight"
  },
  "setting": {
    "environment": "Studio backdrop",
    "background": {
      "color": "Bold red and white graphic background",
      "design": "Large typographic shapes abstracted behind the car",
      "interaction": "No shadows cast onto background text"
    },
    "ground_plane": "Clean studio floor, minimal reflection"
  },
  "camera": {
    "shot_type": "Side profile product-style shot",
    "angle": "Eye-level, orthographic feel",
    "focal_length_equivalent": "70-100mm (compressed, distortion-free)",
    "framing": "Vehicle fully contained within frame",
    "focus": "Entire car sharp from front splitter to rear wing"
  },
  "lighting": {
    "setup": "Controlled studio lighting",
    "key_light": "Even lateral illumination along body panels",
    "fill_light": "Soft fill to maintain detail in shadow areas",
    "highlights": "Clean reflections on paint and carbon surfaces",
    "shadows": "Minimal, soft-edged, grounded under tires"
  },
  "mood_and_style": {
    "tone": "High-performance, premium motorsport",
    "atmosphere": "Editorial racing showcase",
    "emotion": "Precision, speed, engineering confidence"
  },
  "style_and_realism": {
    "style": "Photoreal automotive studio photography",
    "fidelity": "High material accuracy (paint, carbon fiber, rubber)",
    "imperfections": "Very subtle, realistic — not overly polished CGI"
  },
  "technical_details": {
    "aspect_ratio": "Portrait crop adapted from landscape source",
    "sharpness": "High across entire vehicle",
    "noise": "Very low, studio clean"
  },
  "constraints": {
    "no_original_brand_names": true,
    "brand_replacement_enforced": true,
    "no_watermarks": true,
    "no_unreadable_text": true,
    "single_vehicle_only": true
  },
  "negative_prompt": [
    "incorrect car proportions",
    "distorted wheels",
    "warped typography",
    "floating car",
    "motion blur",
    "cgi look",
    "low detail textures",
    "wrong brand logos",
    "extra vehicles"
  ],
  "extra_changes": {
    "explicit_request": "Replace all 'Porsche' text with 'Megane'",
    "implementation_note": "Typography scale, alignment, and realism preserved while changing brand name"
  }
}
