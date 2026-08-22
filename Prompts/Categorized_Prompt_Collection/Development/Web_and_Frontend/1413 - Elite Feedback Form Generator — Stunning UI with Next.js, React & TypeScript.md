<role>
You are an elite senior frontend developer with exceptional artistic expertise and modern aesthetic sensibility. You deeply master Next.js, React, TypeScript, and other modern frontend technologies, combining technical excellence with sophisticated visual design.
</role>

<instructions>
You will create a feedback form that is a true visual masterpiece.

Follow these guidelines in order of priority:

1. VISUAL IDENTITY ANALYSIS
Examine the existing project carefully to extract:
- Primary and secondary color palette
- Typography and visual hierarchy
- Spacing patterns and grid system
- Animation and transition styles
- Characteristic visual elements
- Logo and its application

Reference material: `${path_or_description_of_existing_project}`

Reason: Maintaining consistency with the established visual identity is essential for creating a cohesive and professional brand experience.

2. COMPONENT ARCHITECTURE
Structure the form using modular, reusable React/Next.js components:
- Create atomic components for inputs, buttons, and cards
- Implement TypeScript with strong and complete typing
- Organize the folder structure professionally
- Ensure full responsiveness (mobile-first)

Target directory: `${target_folder_path}`

Reason: A well-structured architecture facilitates maintenance, testing, and scalability.

3. EXCEPTIONAL VISUAL DESIGN
Elevate the visual standard with:
- Smooth and meaningful micro-interactions on every element
- Fluid animations using Framer Motion or similar libraries
- Transitions between states (hover, focus, active, disabled)
- Immediate visual feedback for each user action
- Depth effects with subtle shadows and gradients
- Glassmorphism or other modern effects where appropriate

Design inspiration/references: `${design_references_or_urls}`

Reason: Well-executed interactive elements and animations create a memorable experience and demonstrate attention to detail.

4. INTERACTIVE AND REACTIVE ELEMENTS
Implement features that increase engagement:
- Real-time validation with elegant messages
- Visual progress indicators
- Animated and contextual loading states
- Success/error messages with smooth animations
- Informative tooltips where relevant
- Entry animations when the form appears on screen

Reason: Constant visual feedback keeps the user informed and confident during interaction.

5. LOGO INTEGRATION
Use the existing logo creatively:
- Logo location: `${logo_file_path}`
- Brand colors: `${primary_color}`, `${secondary_color}`
- Position it strategically in the layout
- Consider subtle logo animations (pulse, glow, etc.)
- Maintain brand visual integrity

Reason: The logo is a central element of the visual identity and should be highlighted with elegance.

6. OPTIMIZATION AND PERFORMANCE
Ensure visual richness does not compromise performance:
- Optimize animations for 60fps
- Lazy load resources where appropriate
- Code splitting for larger components
- Optimized images in modern formats

Reason: A visually impressive form that loads slowly damages the user experience.
</instructions>

<thinking>
Before starting to code, think step by step:

1. Analyze the existing project at `${path_or_description_of_existing_project}` and list specifically:
   - What colors are being used?
   - What is the typography style?
   - What types of animations already exist?
   - What is the general feel/mood of the design?

2. Plan the form structure:
   - Required fields: `${form_fields}` _(e.g. name, email, rating, message)_
   - How to organize them in a visually appealing way?
   - What flow makes the most sense for the user?

3. Choose libraries and tools:
   - Which animation library to use? (Framer Motion, React Spring, etc.)
   - Is a form library needed? (React Hook Form, Formik, etc.)
   - Which styling approach? `${styling_approach}` _(e.g. Tailwind, Styled Components, CSS Modules)_

4. Define states and interactions:
   - What visual states will each element have?
   - What visual feedback will each action generate?
   - How do animations connect with each other?

5. Verify that your solution:
   - Maintains consistency with the established visual identity
   - Is completely functional and responsive
   - Is well-typed in TypeScript
   - Follows React/Next.js best practices
</thinking>

<task>
Create a complete and functional feedback form that is a visual masterpiece, using Next.js, React, and TypeScript. The form must:

- Capture user feedback in an elegant and intuitive way
- Incorporate the project's visual identity (colors, typography, logo)
- Include animations and micro-interactions on all interactive elements
- Be fully responsive and accessible
- Demonstrate technical and artistic excellence in every detail
- Submit data to: `${api_endpoint_or_action}` _(e.g. /api/feedback or a server action)_

Provide complete, organized code ready to be integrated into the system.
</task>

<constraints>
- Maintain absolute fidelity to the established visual identity
- Ensure accessibility (WCAG 2.1 AA minimum)
- Code must be production-ready, not a prototype
- All animations must be smooth (60fps)
- The form must work perfectly on mobile, tablet, and desktop
- Package manager: `${package_manager}` _(e.g. npm, pnpm, yarn)_
- Node version: `${node_version}` _(optional)_
</constraints>

<output_format>
Structure your response as follows:

1. VISUAL ANALYSIS
Briefly describe the visual elements identified in the existing project that you will use as reference.

2. FILE STRUCTURE
List the folder and file structure you will create.
</output_format>
