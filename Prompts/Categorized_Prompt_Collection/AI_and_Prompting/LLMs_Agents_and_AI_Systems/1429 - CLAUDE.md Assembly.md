You are compiling the definitive CLAUDE.md design system reference file.
This file will live in the project root and serve as the single source of
truth for any AI assistant (or human developer) working on this codebase.

## Inputs
- **Token architecture:** [Phase 2 output]
- **Component documentation:** [Phase 3 output]
- **Project metadata:**
  - Project name: ${name}
  - Tech stack: [Next.js 14+ / React 18+ / Tailwind 3.x / etc.]
  - Node version: ${version}
  - Package manager: [npm / pnpm / yarn]

## CLAUDE.md Structure

Compile the final file with these sections IN THIS ORDER:

### 1. Project Identity
- Project name, description, positioning
- Tech stack summary (one table)
- Directory structure overview (src/ layout)

### 2. Quick Reference Card
A condensed cheat sheet — the most frequently needed info at a glance:
- Primary colors with hex values (max 6)
- Font stack
- Spacing scale (visual representation: 4, 8, 12, 16, 24, 32, 48, 64)
- Breakpoints
- Border radius values
- Shadow values
- Z-index map

### 3. Design Tokens — Full Reference
Organized by tier (Primitive → Semantic → Component).
Each token entry: name, value, CSS variable, Tailwind class equivalent.
Use tables for scannability.

### 4. Typography System
- Type scale table (name, size, weight, line-height, letter-spacing, usage)
- Responsive rules
- Font loading strategy

### 5. Color System
- Full palette with swatches description (name, hex, usage context)
- Semantic color mapping table
- Dark mode mapping (if applicable)
- Contrast ratio compliance notes

### 6. Layout System
- Grid specification
- Container widths
- Spacing system with visual scale
- Breakpoint behavior

### 7. Component Library
[Insert Phase 3 output for each component]

### 8. Motion & Animation
- Named presets table (name, duration, easing, usage)
- Rules: when to animate, when not to
- Performance constraints

### 9. Coding Conventions
- File naming patterns
- Import order
- Component file structure template
- CSS class ordering convention (if Tailwind)
- State management patterns used

### 10. Rules & Constraints
Hard rules that must never be broken:
- "Never use inline hex colors — always reference tokens"
- "All interactive elements must have visible focus states"
- "Minimum touch target: 44x44px"
- "All images must have alt text"
- "No z-index values outside the defined scale"
- [Add project-specific rules]

## Formatting Requirements
- Use markdown tables for all token/value mappings
- Use code blocks for all code examples
- Keep each section self-contained (readable without scrolling to other sections)
- Include a table of contents at the top with anchor links
- Maximum line length: 100 characters for readability
- Prefer explicit values over "see above" references

## Critical Rule
This file must be AUTHORITATIVE. If there's ambiguity between the
CLAUDE.md and the actual code, the CLAUDE.md should be updated to
match reality — never the other way around. This documents what IS,
not what SHOULD BE (that's a separate roadmap).
