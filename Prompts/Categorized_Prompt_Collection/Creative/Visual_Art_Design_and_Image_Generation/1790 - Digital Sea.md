I want you to act as a VFX Artist focused on bioluminescent fluid simulations and particle-based environmental effects.

Objective: Design an interactive "Digital Sea" where particles behave like bioluminescent plankton reacting to mouse movement or touch events.

Key Mechanics:

Develop a smoothed-particle hydrodynamics (SPH) or a simplified grid-based fluid solver to govern particle flow.

Implement a "Luminescence Decay" logic where particles brighten upon collision or high-velocity movement and slowly fade back to a baseline glow.

Use an additive blending mode and a custom Bloom pass to create a high-end cinematic glow effect.

Integrate a "Vortex Field" where users can create swirls in the particle field that persist for a set duration.

Optimize the system using GPU Instanced Meshes to ensure a stable 60 FPS even with 100,000+ active particles.

Please describe the physics parameters and provide the GLSL code for the fragment shader responsible for the glowing trail effect.
