{
  "meta_data": {
    "task_type": "text_to_image_with_reference",
    "version": "v1.0",
    "priority": "high"
  },
  "technical_constraints": {
    "identity_preservation": {
      "enabled": true,
      "reference_mode": "strict",
      "parameters": {
        "use_reference_face_only": true,
        "identity_lock": true,
        "preserve_facial_features": true,
        "preserve_skin_texture": true,
        "avoid_face_morphing": true,
        "preservation_strength": 1.0
      }
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "resolution_target": "ultra_high_res",
      "render_engine_style": "photorealistic"
    }
  },
  "creative_prompt": {
    "scene": {
      "location": "dim billiards bar",
      "background": "dark ceiling, red-and-white wall stripe, a few tables/chairs in the back, low-light ambience with subtle film grain",
      "key_props": [
        "green-felt pool table (foreground)",
        "vintage red billiard lamps overhead (warm red glow)",
        "scattered billiard balls on the table",
        "pool cue (held by the subject)"
      ]
    },
    "subject": {
      "type": "young adult woman",
      "identity_instruction": "The subject must be 100% identical to the uploaded reference photo (same face, proportions, age, and identity). No identity drift.",
      "pose": "leaning against the pool table edge; one hand braced on the table; the other hand holding the cue stick vertically; hip slightly popped; head slightly tilted; gaze up and to the side",
      "expression": "cool, confident, subtly flirtatious",
      "wardrobe": {
        "top": "leopard-print corset/bustier top with straps",
        "bottom": "black mini skirt",
        "accessories": "minimal jewelry (small hoops or studs)"
      },
      "details": {
        "nails": "red nail polish",
        "hair": "long, voluminous, wavy hair",
        "makeup": "night-out glam: defined eyeliner/lashes, warm blush, nude-brown lips"
      }
    },
    "camera_and_lighting": {
      "shot_style": "realistic nightlife flash photo + ambient bar lighting",
      "camera": "full-frame DSLR",
      "lens": "35mm or 50mm",
      "aperture": "f/1.8",
      "shutter_speed": "1/80s",
      "iso": "800",
      "lighting": {
        "primary": "on-camera flash (crisp subject, natural falloff, realistic shadows)",
        "secondary": "overhead red lamps glow + dim ambient fill",
        "look": "high contrast, controlled specular highlights, no blown whites"
      },
      "color_grading": "warm reds with natural skin tones, subtle film grain",
      "focus": "tack-sharp eyes and face, shallow depth of field, soft background bokeh"
    }
  },
  "negative_prompt": [
    "different person",
    "identity change",
    "face morphing",
    "extra people",
    "extra limbs",
    "extra fingers",
    "bad hands",
    "deformed anatomy",
    "warped cue stick",
    "warped pool table",
    "text",
    "logo",
    "watermark",
    "cartoon",
    "anime",
    "illustration",
    "over-smoothed skin",
    "plastic skin",
    "low resolution",
    "blurred face",
    "overexposed flash highlights"
  ]
}
