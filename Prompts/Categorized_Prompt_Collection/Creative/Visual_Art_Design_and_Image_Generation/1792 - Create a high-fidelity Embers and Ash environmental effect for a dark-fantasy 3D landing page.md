I want you to act as a Technical Artist specializing in atmospheric 3D effects such as volumetric fog, falling embers, and localized weather systems.

Project Goal: Create a high-fidelity "Embers and Ash" environmental effect for a dark-fantasy 3D landing page.

Technical Logic:

Design a particle emitter that simulates the erratic, upward-floating movement of burning embers, including horizontal wind sway.

Implement "Size Over Life" and "Opacity Over Life" curves to ensure particles realistically flicker and vanish.

Use custom sprites with a "Soft Particle" shader to avoid harsh clipping when particles intersect with 3D geometry in the scene.

Add a secondary "Smoke" particle layer using low-frequency noise to simulate volumetric density.

Implement a "Light Scattering" effect where each ember acts as a tiny light source, subtly illuminating nearby meshes.
