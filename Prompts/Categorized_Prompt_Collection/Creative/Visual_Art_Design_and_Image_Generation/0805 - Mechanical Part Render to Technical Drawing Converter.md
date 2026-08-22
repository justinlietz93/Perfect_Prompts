{
  "task": "image_to_image",
  "description": "Convert a 3D mechanical part render into a fully dimensioned manufacturing drawing",
  "input_image": "3d_render_of_pipe_or_mechanical_part.png",
  "prompt": "mechanical engineering drawing, multi-view orthographic projection, front view, top view, side view and section view, fully dimensioned technical drawing, precise numeric measurements in millimeters, diameter symbols, radius annotations, hole count notation, center lines, section hatching, consistent line weights, ISO mechanical drafting standard, black ink on white background, manufacturing-ready documentation",
  "negative_prompt": "artistic style, perspective view, soft shading, textures, realistic lighting, colors, decorative rendering, sketch, hand-drawn look, incomplete dimensions",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 40,
    "cfg_scale": 6,
    "denoising_strength": 0.5,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "ISO-style mechanical drawing with clear dimensions suitable for CNC, casting, or fabrication reference"
}
