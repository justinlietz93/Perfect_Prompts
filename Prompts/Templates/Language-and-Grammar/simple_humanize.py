# Convenient basic script pulled from AlgoInsights - https://algoinsights.medium.com/how-to-make-ai-writing-sound-human-and-beat-ai-detectors-47c30d90ebaf

import re
from statistics import stdev

nope_words = [
    "unleash", "empower", "harness", "unlock", "revolutionary",
    "supercharge", "ultimate", "elevate", "turbocharge", "skyrockets",
    "next-level", "ecosystem"
]
def check_for_robot_vibes(text):
    tips = []
    # Look for annoying AI words
    for word in nope_words:
        if word in text.lower():
            tips.append(f"Ditch '{word}' and say something like 'Here's the scoop' or 'This makes things easier.'")
    

    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    word_counts = [len(s.split()) for s in sentences]
    
    if word_counts:
        variation = stdev(word_counts) if len(word_counts) > 1 else 0
        if variation < 2.0:
            tips.append("Your sentences are kinda same-y. Mix it up with some short ones and a few rambly ones.")
    
    return tips
# Test it
text = """This revolutionary app supercharges your work. It's a total game-changer."""
results = check_for_robot_vibes(text)
for tip in results:
    print(tip)
