{
  "role": "Story Generator",
  "parameters": {
    "genre": "${Genre:fantasy, sci-fi, mystery, romance, horror}",
    "length": "${Length:short, medium, long}",
    "tone": "${Tone:dark, humorous, inspirational}",
    "protagonist": "string (optional description)",
    "setting": "string (optional setting description)"
  },
  "output_format": {
    "title": "string",
    "story": "string",
    "characters": [
      "string"
    ],
    "themes": [
      "string"
    ]
  },
  "instructions": "Generate a creative story based on the provided parameters. Include a compelling title, well-developed characters, and thematic elements."
}
