You are a senior full-stack engineer and UX/UI architect with 10+ years of experience building production-grade web applications. You specialize in responsive design systems, modern UI/UX patterns, and cross-device performance optimization.

---

## TASK

Generate a **comprehensive, actionable development plan** to enhance the existing web application, ensuring it meets the following criteria:

### 1. RESPONSIVENESS & CROSS-DEVICE COMPATIBILITY
- Ensure the application adapts flawlessly to: mobile (320px+), tablet (768px+), desktop (1024px+), and large screens (1440px+)
- Define a clear **breakpoint strategy** based on the current implementation, with rationale for adjustments
- Specify a **mobile-first vs desktop-first** approach, considering existing user data
- Address: touch targets, tap gestures, hover states, and keyboard navigation
- Handle: notches, safe areas, dynamic viewport units (dvh/svh/lvh)
- Cover: font scaling and image optimization (srcset, art direction), incorporating existing assets

### 2. PERFORMANCE & SMOOTHNESS
- Target performance metrics: 60fps animations, <2.5s LCP, <100ms INP, <0.1 CLS (Core Web Vitals)
- Develop strategies for: lazy loading, code splitting, and asset optimization, evaluating current performance bottlenecks
- Approach to: CSS containment and GPU compositing for animations
- Plan for: offline support or graceful degradation, assessing existing service worker implementations

### 3. MODERN & ELEGANT DESIGN SYSTEM
- Refine or define a **design token architecture**: colors, spacing, typography, elevation, motion
- Specify a color palette strategy that accommodates both light and dark modes
- Include a spacing scale, border radius philosophy, and shadow system consistent with existing styles
- Cover: iconography and illustration styles, ensuring alignment with current design elements
- Detail: component-level visual consistency rules and adjustments for legacy components

### 4. MODERN UX/UI BEST PRACTICES
Apply and plan for the following UX/UI principles, adapting them to the current application:
- **Hierarchy & Scannability**: Ensure effective use of visual weight and whitespace
- **Feedback & Affordance**: Implement loading states, skeleton screens, and micro-interactions
- **Navigation Patterns**: Enhance responsive navigation (hamburger, bottom nav, sidebar), including breadcrumbs and wayfinding
- **Accessibility (WCAG 2.1 AA minimum)**: Analyze current accessibility and propose improvements (contrast ratios, ARIA roles)
- **Forms & Input**: Validate and enhance UX for forms, including inline errors and input types per device
- **Motion Design**: Integrate purposeful animations, considering reduced-motion preferences
- **Empty States & Edge Cases**: Strategically handle zero data, errors, and permissions

### 5. TECHNICAL ARCHITECTURE PLAN
- Recommend updates to the **tech stack** (if needed) with justification, considering current technology usage
- Define: component architecture enhancements, folder structure improvements
- Specify: theming system implementation and CSS strategy (modules, utility-first, CSS-in-JS)
- Include: a testing strategy for responsiveness that addresses current gaps (tools, breakpoints to test, devices)

---

## OUTPUT FORMAT

Structure your plan in the following sections:

1. **Executive Summary** – One paragraph overview of the approach
2. **Responsive Strategy** – Breakpoints, layout system revisions, fluid scaling approach
3. **Performance Blueprint** – Targets, techniques, assessment of current metrics
4. **Design System Specification** – Tokens, color palette, typography, component adjustments
5. **UX/UI Pattern Library Plan** – Key patterns, interactions, and updated accessibility checklist
6. **Technical Architecture** – Stack, structure, and implementation adjustments
7. **Phased Rollout Plan** – Prioritized milestones for integration (MVP → polish → optimization)
8. **Quality Checklist** – Pre-launch verification for responsiveness and quality across all devices

---

## CONSTRAINTS & STYLE

- Be **specific and actionable** — avoid vague recommendations
- Provide **concrete values** where applicable (e.g., "8px base spacing scale", "400ms ease-out for modals")
- Flag **common pitfalls** in integrating changes and how to avoid them
- Where multiple approaches exist, **recommend one with reasoning** rather than listing options
- Assume the target is a **${INSERT_APP_TYPE: e.g., SaaS dashboard / e-commerce / portfolio / social app}**
- Target users are **[${INSERT_USER_TYPE: e.g, non-technical consumers / enterprise professionals / mobile-first users}]**

---

Begin with the Executive Summary, then proceed section by section.
