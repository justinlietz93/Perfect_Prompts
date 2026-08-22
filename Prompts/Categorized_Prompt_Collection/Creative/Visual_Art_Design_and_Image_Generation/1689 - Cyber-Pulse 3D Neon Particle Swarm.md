Game Concept: A fast-paced arcade "dodge-em-up" set in a digital void. The player controls a core energy spark, navigating through a fluid-like nebula of 10,000+ blue and purple particles that react to the player's presence.
Technical Prompt:
Create a Three.js scene featuring a Points system with 15,000 particles. Use a custom ShaderMaterial for a glow effect. Implement a repulsion logic where particles fly away from the mouse cursor.

JavaScript
// Core repulsion math
let dist = particlePos.distanceTo(mousePos);
if (dist < 5) {
  direction.subVectors(particlePos, mousePos).normalize();
  particlePos.addScaledVector(direction, 0.2);
}
Include a BloomPass for post-processing and ensure 60FPS performance via
