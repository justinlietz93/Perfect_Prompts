Game Concept: A puzzle-platformer named "Gravity Shift" where players rotate the entire world to navigate a 3D low-poly labyrinth. The environment is minimalist, using pastel gradients and sharp geometric shapes.
Technical Prompt:
Build a 3D platformer using Three.js and Cannon.js. The world is a cube-shaped maze. When the user presses 'R', rotate the world.gravity vector by 90 degrees.

JavaScript
// Gravity rotation logic
world.gravity.set(0, -9.82, 0); // Default
function rotateGravity() {
  let newG = new CANNON.Vec3(-world.gravity.y, world.gravity.x, 0);
  world.gravity.copy(newG);
}
Include smooth camera interpolation using Lerp to follow the player's rigid body during shifts.
