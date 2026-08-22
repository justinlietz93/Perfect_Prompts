I want you to act as a Master Game Designer specializing in immersive educational mechanics. Please construct a 3D semantic classification game prototype for an English vocabulary lesson.

Game Name: 《Semantic Pull: Word Family Grid》.

Game Function: The viewport displays three distinct glowing 3D conceptual zones (e.g., a cube, a cylinder, a torus representing Categories like Animals, Fruits, Colors). Multiple floating crystal nodes drift around the screen under a low-frequency noise algorithm. The user can drag any crystal using the mouse pointer; upon release, the system calculates the distance and a magnetic attraction vector to the nearest zone. If the crystal aligns with the correct category zone, it is absorbed via a smooth LERP scaling animation, triggering a burst of light trails. If incorrect, a elastic repulsion vector snaps it back to its origin.

Design Style: Retro-futuristic cyberpunk tailored for kids. Dark background contrasting with highly emissive, translucent neon materials for the category zones and holographic視差 effects inside the crystals.

Technologies Used: Three.js for asset management and shaders, GSAP for the non-linear magnetic spring and attraction interpolation, and Raycaster for high-precision 3D bounding box interaction.
