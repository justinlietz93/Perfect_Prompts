Build a web app called "Alter" — a personalized digital avatar creation tool.

Core features:
- Style selector: 8 avatar styles presented as visual cards (professional headshot, anime, pixel art, oil painting, cyberpunk, minimalist line art, illustrated character, watercolor)
- Input panel: text description of desired look and vibe (mood, colors, personality) — no photo upload required in MVP
- Generation: calls fal.ai FLUX API with a structured prompt built from the style selection and description — generates 4 variants per request
- Customization: background color picker overlay, optional username/tagline text added via Canvas API
- Download: PNG at 400px, 800px, and 1500px square
- History: last 12 generated packs saved in localStorage — click any to view and re-download

UI: bright, expressive, fun. Large visual cards for style selection. Results shown in a 2x2 grid. Mobile-responsive.

Stack: React, fal.ai API for image generation, HTML Canvas for text overlays, localStorage for history.
