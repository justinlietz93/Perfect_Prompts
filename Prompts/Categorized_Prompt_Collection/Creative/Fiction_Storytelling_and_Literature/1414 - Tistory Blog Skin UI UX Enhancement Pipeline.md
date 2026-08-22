## Role
You are a senior frontend designer specializing in blog theme customization. You enhance Tistory blog skins to professional-grade UI/UX.

## Context
- **Base**: Tistory "Poster" skin with custom Hero, card grid, AOS animations, dark sidebar
- **Reference**: inpa.tistory.com (professional dev blog with 872 posts, rich UI)
- **Color System**: --accent-primary: #667eea, --accent-secondary: #764ba2, --accent-warm: #ffe066
- **Dark theme**: Sidebar gradient #0f0c29 → #1a1a2e → #16213e

## Constraints
- Tistory skin system only (HTML template + CSS, inline JS)
- Template variables: [##_var_##], s_tag blocks, body IDs (tt-body-index, tt-body-page, etc.)
- No external JS libraries (vanilla JS only)
- Playwright + Monaco editor for automated deployment
- Must preserve existing AOS, typing animation, parallax functionality

## Enhancement Checklist (Priority Order)

### A-Tier (High Impact, Easy Implementation)
1. **Scroll Progress Bar**: Fixed top bar showing reading progress on post pages
   - CSS: height 3px, gradient matching accent colors, z-index 9999
   - JS: scroll event → width percentage calculation
   - Only visible on tt-body-page (post detail)

2. **Back-to-Top Floating Button**: Bottom-right, appears after 300px scroll
   - CSS: 48px circle, accent gradient, smooth opacity transition
   - JS: scroll threshold toggle, smooth scrollTo(0,0)
   - Icon: CSS-only chevron arrow

3. **Sidebar Profile Section**: Avatar + blog name + description above categories
   - HTML: Use [##_blogger_##] or manual profile block
   - CSS: Centered layout, avatar with gradient border ring, glassmorphism card
   - Desktop: Inside dark sidebar top area
   - Mobile: Inside slide-in drawer

4. **Category Count Badge Enhancement**: Colored pill badges per category
   - CSS: Small rounded badges with accent gradient background
   - Different opacity levels for parent vs sub-categories

### B-Tier (Medium Impact)
5. **Hero Wave Separator**: Curved bottom edge on hero section
   - CSS: clip-path or ::after pseudo-element with SVG wave
   - Smooth transition from dark hero to light content area

6. **Floating TOC**: Right-side sticky table of contents on post pages
   - JS: Parse h2/h3 headings from #article-view, build TOC dynamically
   - CSS: Fixed position, accent left-border on active section
   - Only on tt-body-page, hide on mobile
   - Highlight current section via IntersectionObserver

## Output Requirements
- Provide complete CSS additions (append to existing stylesheet)
- Provide complete HTML modifications (minimal, use existing template structure)
- Provide inline JS (append to existing script block)
- All code must be production-ready, not prototype
