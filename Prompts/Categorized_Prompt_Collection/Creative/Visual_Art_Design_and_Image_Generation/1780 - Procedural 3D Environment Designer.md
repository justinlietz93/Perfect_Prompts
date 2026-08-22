I want you to act as a 3D Level Design Expert specializing in procedural content generation (PCG).

Task:
Create a system that generates an infinite, dynamic 3D landscape using Perlin or Simplex noise algorithms for a high-speed racing or flight game.

Technical Details:

Develop a vertex shader or a CPU-side logic that modifies a plane geometry’s heightmap in real-time based on player displacement.

Implement an object-pooling mechanism for "terrain chunks" to ensure 60 FPS performance on mobile devices.

Define a logic to automatically spawn obstacle meshes at points where the terrain gradient exceeds a specific threshold.

Calculate real-time surface normals so player characters can align their orientation and adjust acceleration based on the slope.

Suggest an environmental lighting setup (Direct/Ambient) to enhance the depth perception of the procedural terrain.
