{
  "model": "nano-banana",
  "task": "image_to_image_product_transformation",

  "objective": "Transform the provided clothing product image into a luxury studio ghost-mannequin presentation where the garment appears naturally worn and volumetric, as if inflated with air on an invisible mannequin. Preserve the exact identity of the original product with zero alterations.",

  "input_description": {
    "source_image_type": "flat lay clothing product photo",
    "background": "white background",
    "product_category": "general clothing (t-shirts, jackets, hoodies, pants, denim, vests, etc)"
  },

  "transformation_rules": {
    "garment_structure": "inflate the garment as if worn by an invisible mannequin, creating natural body volume and shape while keeping the interior empty",
    "mannequin_style": "luxury ghost mannequin used in high-end fashion e-commerce photography",
    "fabric_condition": "perfectly ironed fabric with subtle natural folds that reflect realistic garment tension",
    "pose": "natural wearable garment shape as if placed on a torso or body form, but with no visible mannequin or human presence",
    "center_alignment": "the garment must remain perfectly centered in the frame",
    "framing": "clean product catalog composition with balanced margins on all sides",
    "background": "pure white professional studio background (#FFFFFF) with no gradients, textures, props, or shadows except a very soft natural grounding shadow"
  },

  "lighting": {
    "style": "high-end fashion e-commerce studio lighting",
    "direction": "soft frontal lighting with balanced fill light",
    "goal": "highlight fabric texture, stitching, seams, and garment structure",
    "shadow_control": "minimal soft shadow directly beneath garment for realism",
    "exposure": "clean bright exposure without overblown highlights or crushed shadows"
  },

  "identity_preservation": {
    "color": "preserve the exact original color values",
    "texture": "preserve the exact fabric texture and weave",
    "logos": "preserve existing logos exactly if present",
    "stitching": "preserve stitching patterns exactly",
    "details": "preserve pockets, buttons, zippers, seams, embroidery, tags, and all construction details exactly"
  },

  "strict_prohibitions": [
    "do not add new logos",
    "do not remove existing logos",
    "do not change garment color",
    "do not alter stitching",
    "do not modify pockets",
    "do not modify garment design",
    "do not invent new fabric textures",
    "do not change garment proportions",
    "do not add accessories",
    "do not add a human model",
    "do not add a mannequin",
    "do not add props or scenery",
    "do not crop the garment"
  ],

  "fabric_realism": {
    "structure": "realistic garment volume based on clothing physics",
    "folds": "subtle natural folds caused by gravity and body form",
    "tension": "light tension around chest, shoulders, waist, or hips depending on garment type",
    "fabric_behavior": "respect real textile behavior such as denim stiffness, cotton softness, or knit flexibility"
  },

  "composition_requirements": {
    "camera_angle": "straight-on front-facing catalog angle",
    "symmetry": "balanced and professional e-commerce alignment",
    "product_visibility": "entire garment fully visible without cropping",
    "catalog_standard": "consistent framing suitable for automated product galleries"
  },

  "quality_requirements": {
    "style": "luxury fashion e-commerce photography",
    "sharpness": "high-detail crisp garment texture",
    "resolution": "high resolution suitable for product zoom",
    "cleanliness": "no dust, wrinkles, artifacts, distortions, or AI hallucinations"
  },

  "pipeline_goal": {
    "use_case": "360-degree product rotation pipeline",
    "consistency_requirement": "garment structure, lighting, and proportions must remain stable and repeatable across multiple angles",
    "output_type": "professional e-commerce catalog image"
  }
}
