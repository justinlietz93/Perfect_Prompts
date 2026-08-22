I want you to act as an expert front-end game engineer specializing in single-file HTML5 games. Your task is to produce a SINGLE FILE (index.html) implementation of a 3D Kinetic Bounce Arena.

GAME SPEC:

Title: Kinetic Bounce Arena

Core mechanic: Launch a glowing sphere into a rotating 3D cylinder container filled with 25 smaller physics-driven particles.

Goal: Keep the main sphere bouncing by adjusting the container's tilt via mouse movement.

TECH REQUIREMENTS:

Single file: <!doctype html> with inline <style> and <script> using p5.js (loaded via CDN).

Rendering: WebGL mode in p5.js, 600x600 canvas centered on page.

Physics: Implement 3D bounding box collision detection for the cylinder walls and sphere-to-particle momentum transfer. Particles must leave fading colorful motion trails.

Design style: Dark synthwave aesthetic with emissive neon materials, glowing particle vectors, and smooth automatic camera zoom scaling.
