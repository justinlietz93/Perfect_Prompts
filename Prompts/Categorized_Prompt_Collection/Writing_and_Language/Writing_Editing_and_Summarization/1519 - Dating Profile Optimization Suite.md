Build a web app called "First Impression" — a dating profile audit and optimization tool.

Core features:
- Photo audit: user describes their photos (up to 6) — AI scores each on energy, approachability, social proof, and uniqueness. Returns a ranked order recommendation with one-line reasoning per photo
- Bio rewriter: user pastes current bio, clicks "Optimize", receives 3 rewritten versions in distinct tones (playful / authentic / direct). Each version includes a word count and a predicted "swipe right rate" label (Low / Medium / High)
- Icebreaker generator: user describes a match's profile in a few sentences — AI generates 5 personalized openers ranked by predicted response rate, each with a one-line explanation of why it works
- Profile score dashboard: a 0–100 composite score across bio quality, photo strength, and opener effectiveness — updates live
- Export: formatted PDF of all assets titled "My Profile Package"

Stack: React, [LLM API] for all AI calls, jsPDF for export. Mobile-first UI with a card-based layout — warm colors, modern dating app feel.
