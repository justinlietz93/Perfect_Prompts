{
  "image_analysis": {
    "environment": {
      "type": "Indoor",
      "location_type": "Bathroom or bedroom (indicated by mirror and sink edge)",
      "spatial_depth": "Shallow depth of field due to mirror reflection",
      "background_elements": "Grey painted wall, white door frame or window frame edge on the left, electrical outlet on the right, partial view of a white sink"
    },
    "camera_specs": {
      "lens_type": "Smartphone wide-angle lens (reflected)",
      "angle": "Eye-level, straight on relative to the mirror",
      "perspective": "Selfie reflection",
      "focus": "Sharp focus on the subject, slight softness on the background reflection"
    },
    "lighting": {
      "condition": "Natural daylight mixed with ambient indoor light",
      "sources": [
        {
          "source_id": 1,
          "type": "Natural Window Light",
          "direction": "From the left (subject's right)",
          "color_temperature": "Cool/Neutral daylight",
          "intensity": "Moderate to High",
          "effect_on_subject": "Highlights the texture of the ribbed top, illuminates the face profile and torso, creates soft gradients across the midriff"
        }
      ],
      "shadows": "Soft shadows cast on the right side of the subject's body (away from window) and under the bust line"
    },
    "subject_analysis": {
      "identity": "Young woman (face partially obscured by hair and angle)",
      "orientation": "Body angled 45 degrees to the left, Head turned to profile view facing left",
      "emotional_state": "Calm, focused, casual confidence",
      "visual_appeal": "Aesthetic, fit, natural",
      "posture": {
        "general_definition": "Standing upright, slight hip sway",
        "feet_placement": "Not visible in frame",
        "hand_placement": "Left hand holding the phone (visible), Right arm down by side (partially visible)",
        "visible_extent": "From top of head to upper hips/thighs"
      },
      "head_details": {
        "hair": {
          "color": "Dark Brown / Espresso",
          "style": "Shoulder-length, layered cuts",
          "texture": "Curly / Wavy, voluminous, messy-chic",
          "interaction_with_face": "Strands falling over the forehead and framing the cheekbones, partially obscuring the eye"
        },
        "ears": "Covered by hair",
        "face": {
          "definition": "Side profile view",
          "forehead": "Partially covered by curls",
          "eyebrows": "Dark, arched, natural thickness (partially visible)",
          "nose": "Straight bridge, slightly upturned tip",
          "mouth": "Lips relaxed, closed, full lower lip",
          "chin": "Defined, soft curve",
          "expression": "Neutral, concentrating on the reflection",
          "makeup": "Minimal or natural look"
        }
      },
      "body_details": {
        "body_type": "Ectomorph-Mesomorph blend (Slim with defined curves)",
        "skin_tone": "Light olive / Fair",
        "neck": "Slender, clavicles slightly visible",
        "shoulders": "Narrow, relaxed",
        "chest_area": {
          "ratio_to_body": "Proportionate to slim frame",
          "visual_estimate": "Moderate bust size",
          "undergarment_indications": "No distinct strap lines visible; likely seamless or no bra",
          "nipple_visibility": "Not explicitly defined due to fabric thickness",
          "shape_in_clothing": "Natural teardrop shape supported by tight fabric"
        },
        "midsection": {
          "belly_button": "Visible, vertical orientation",
          "ratio": "Slim waist, defined abdominals (linea alba visible)",
          "relation_to_chest": "Significantly narrower (hourglass suggestion)",
          "relation_to_hips": "Tapers inward before flaring to hips"
        },
        "hips_area": {
          "ratio_to_waist": "Wider than waist",
          "visibility": "Top curve visible",
          "width": "Moderate flare"
        }
      },
      "attire": {
        "upper_body": {
          "item": "Long-sleeve crop top",
          "style": "Henley neck with buttons (3 visible, unbuttoned at top), Ribbed knit texture",
          "color": "Light Brown / Taupe / Mocha",
          "fit": "Form-fitting / Tight",
          "fabric_drape": "Stretches over bust, hugs waist, cuffs at wrist"
        },
        "lower_body": {
          "item": "Pants / Leggings (Waistband only)",
          "color": "Heather Grey",
          "style": "Low-rise",
          "material": "Jersey or cotton blend",
          "visibility": "Only the waistband and upper hip area visible"
        },
        "accessories": {
          "hands": "Ring on left ring finger (thin band)",
          "wrist": "None visible"
        }
      }
    },
    "objects_in_scene": [
      {
        "object": "Smartphone",
        "description": "Black case, multiple camera lenses (iPhone Pro model style)",
        "function": "Capture device",
        "position": "Held in left hand, right side of image",
        "color": "Black"
      },
      {
        "object": "Mirror",
        "description": "Reflective surface containing the entire subject",
        "function": "Medium for the selfie",
        "position": "Foreground plane"
      },
      {
        "object": "Electrical Outlet",
        "description": "Standard white wall outlet",
        "position": "Background, right side behind subject",
        "color": "White"
      },
      {
        "object": "Sink",
        "description": "White ceramic basin edge",
        "position": "Bottom right corner",
        "color": "White"
      }
    ],
    "negative_prompts": [
      "blur",
      "noise",
      "distortion",
      "deformed hands",
      "missing fingers",
      "extra limbs",
      "bad anatomy",
      "overexposed",
      "underexposed",
      "cartoon",
      "illustration",
      "watermark",
      "text"
    ]
  }
}
