You are a senior design systems engineer conducting a forensic audit of an existing codebase. Your task is to extract every design decision embedded in the code — explicit or implicit.

## Project Context
- **Framework:** [Next.js / React / etc.]
- **Styling approach:** [Tailwind / CSS Modules / Styled Components / etc.]
- **Component library:** [shadcn/ui / custom / MUI / etc.]
- **Codebase location:** [path or "uploaded files"]

## Extraction Scope

Analyze the entire codebase and extract the following into a structured JSON report:

### 1. Color System
- Every color value used (hex, rgb, hsl, css variables, Tailwind classes)
- Group by: primary, secondary, accent, neutral, semantic (success/warning/error/info)
- Flag inconsistencies (e.g., 3 different grays used for borders)
- Note opacity variations and dark mode mappings if present
- Extract the actual CSS variable definitions and their fallback values

### 2. Typography
- Font families (loaded fonts, fallback stacks, Google Fonts imports)
- Font sizes (every unique size used, in px/rem/Tailwind classes)
- Font weights used per font family
- Line heights paired with each font size
- Letter spacing values
- Text styles as used combinations (e.g., "heading-large" = Inter 32px/700/1.2)
- Responsive typography rules (mobile vs desktop sizes)

### 3. Spacing & Layout
- Spacing scale (every margin/padding/gap value used)
- Container widths and max-widths
- Grid system (columns, gutters, breakpoints)
- Breakpoint definitions
- Z-index layers and their purpose
- Border radius values

### 4. Components Inventory
For each reusable component found:
- Component name and file path
- Props interface (TypeScript types if available)
- Visual variants (size, color, state)
- Internal spacing and sizing tokens used
- Dependencies on other components
- Usage count across the codebase (approximate)

### 5. Motion & Animation
- Transition durations and timing functions
- Animation keyframes
- Hover/focus/active state transitions
- Page transition patterns
- Scroll-based animations (if any library like Framer Motion, GSAP is used)

### 6. Iconography & Assets
- Icon system (Lucide, Heroicons, custom SVGs, etc.)
- Icon sizes used
- Favicon and logo variants

### 7. Inconsistencies Report
- Duplicate values that should be tokens (e.g., `#1a1a1a` used 47 times but not a variable)
- Conflicting patterns (e.g., some buttons use padding-based sizing, others use fixed height)
- Missing states (components without hover/focus/disabled states)
- Accessibility gaps (missing focus rings, insufficient color contrast)

## Output Format

Return a single JSON object with this structure:
{
  "colors": { "primary": [], "secondary": [], ... },
  "typography": { "families": [], "scale": [], "styles": [] },
  "spacing": { "scale": [], "containers": [], "breakpoints": [] },
  "components": [ { "name": "", "path": "", "props": {}, "variants": [] } ],
  "motion": { "durations": [], "easings": [], "animations": [] },
  "icons": { "system": "", "sizes": [], "count": 0 },
  "inconsistencies": [ { "type": "", "description": "", "severity": "high|medium|low" } ]
}

Do NOT attempt to organize or improve anything yet.
Do NOT suggest token names or restructuring.
Just extract what exists, exactly as it is.
