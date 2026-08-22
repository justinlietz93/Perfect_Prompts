{
  "prompt": "instagirl, candid phone snapshot, realistic amateur vibe, natural skin texture, light makeup at most, handheld micro-blur, iPhone 11 wide 26mm EXIF look, f/1.8, 1/60s, ISO 200, slight lens distortion, casual posture, everyday outfit, mild flyaway hair, imperfect framing, background clutter present, no retouching, realistic shadows, faithful anatomy, same person identity, same body proportions",
  "negative_prompt": "beauty filter, skin smoothing, studio glam, hdr glow, cinematic grading, fashion editorial, airbrush, liquify, body morph, face changed, de-aged, uncanny valley, extra fingers, warped limbs, NSFW, lingerie, bikini, watermark, text, logo, border",
  "image": "<REFERENCE_IMAGE_URL>",
  "strength": 0.35,
  "guidance": 5.0,
  "control_nets": [
    {
      "type": "openpose",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.7,
      "guess_mode": false
    },
    {
      "type": "depth",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.45
    }
  ],
  "face_lock": {
    "type": "ip_adapter_faceid",
    "ref_image": "<REFERENCE_FACE_CROP_OR_SAME_URL>",
    "weight": 0.75
  }
}
