#version 1.0
root{details,prompt:str}:
  details{atmosphere,camera_angle:str,color_palette,emotion,environmental_elements:str,genre:str,lighting,location:str,subject1,subject2,year:str}:
    atmosphere[4]: Playful,Dreamlike,Digital frontier,Calm isolation
    camera_angle: "High-angle isometric view, emphasizing the island's isolation and the blocky aesthetics, 1:1 cinematic aspect ratio."
    color_palette[4]: Saturated primary colors,vibrant greens and blues for the island,deep purples and blacks for the void,pixelated orange accents
    emotion[4]: Wonder,Curiosity,Discovery,Serenity
    environmental_elements: "Blocky, geometric trees with glowing leaves, pixelated waterfalls cascading into the void, floating abstract digital dust motes, subtle grid lines on the void's floor."
    genre: Voxel Art
    lighting[3]: Emissive light from the voxels themselves,"soft, diffuse ambient light from the digital void",subtle rim lighting on the blocky figures
    location: "A solitary, blocky floating island made of glowing voxels, suspended in an infinite digital void, with sparse, geometric trees and structures."
    subject1{costume:str,subject_action:str,subject_expression:str}:
      costume: "Low-polygon adventurer tunic and trousers in muted greens and browns, a blocky utility belt with voxel tools, simple, chunky voxel boots."
      subject_action: "Standing with one hand lightly resting on a large, blocky, glowing data crystal embedded in the island."
      subject_expression: "A subtle, curious expression, eyes wide with wonder at the digital landscape."
    subject2{costume:str,subject_action:str,subject_expression:str}:
      costume: "A vibrant, pixelated explorer jumpsuit in electric blue, with contrasting orange accents, chunky voxel goggles pushed up on her head, a small blocky digital compass attached to her wrist."
      subject_action: "Leaning forward slightly, arm outstretched, pointing excitedly towards a cluster of particularly vibrant voxel flora at the island's edge."
      subject_expression: "An excited, joyful expression, mouth slightly open in awe."
    year: "Retro-Futuristic, 8-bit aesthetic"
  prompt: "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Imagine Subject 1 (male) and Subject 2 (female) as blocky, low-polygon explorers discovering a vibrant, floating voxel island in a vast digital void. Subject 1 is contemplative, while Subject 2 is eagerly pointing out a new discovery amidst the pixelated flora."
