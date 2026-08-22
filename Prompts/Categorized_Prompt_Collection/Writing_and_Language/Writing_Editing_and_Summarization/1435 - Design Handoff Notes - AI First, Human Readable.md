# Design Handoff Notes — AI-First, Human-Readable

### A structured handoff document optimized for AI implementation agents (Claude Code, Cursor, Copilot) while remaining clear for human developers

---

## About This Prompt

**Description:** Generates a design handoff document that serves as direct implementation instructions for AI coding agents. Unlike traditional handoff notes that describe how a design "should feel," this document provides machine-parseable specifications with zero ambiguity. Every value is explicit, every state is defined, every edge case has a rule. The document is structured so an AI agent can read it top-to-bottom and implement without asking clarifying questions — while a human developer can also read it naturally.

**The core philosophy:** If an AI reads this document and has to guess anything, the document has failed.

**When to use:** After design is finalized, before implementation begins. This replaces Figma handoff, design spec PDFs, and "just make it look like the mockup" conversations.

**Who reads this:**
- Primary: AI coding agents (Claude Code, Cursor, Copilot, etc.)
- Secondary: Human developers reviewing or debugging the AI's output
- Tertiary: You (the designer), when checking if implementation matches intent

**Relationship to CLAUDE.md:** This document assumes a CLAUDE.md design system file already exists in the project root. Handoff Notes reference tokens from CLAUDE.md but don't redefine them. If no CLAUDE.md exists, run the Design System Extraction prompts first.

---

## The Prompt

```
You are a design systems engineer writing implementation specifications.
Your output will be read primarily by AI coding agents (Claude Code, Cursor)
and secondarily by human developers.

Your writing must follow one absolute rule:
**If the reader has to guess, infer, or assume anything, you have failed.**

Every value must be explicit. Every state must be defined. Every edge case
must have a rule. No "as appropriate," no "roughly," no "similar to."

## Project Context
- **Project:** ${name}
- **Framework:** [Next.js 14+ / React / etc.]
- **Styling:** [Tailwind 3.x / CSS Modules / etc.]
- **Component library:** [shadcn/ui / custom / etc.]
- **CLAUDE.md location:** [path — or "not yet created"]
- **Design source:** [uploaded code / live URL / screenshots]
- **Pages to spec:** [all / specific pages]

## Output Format Rules

Before writing any specs, follow these formatting rules exactly:

1. **Values are always code-ready.**
   WRONG: "medium spacing"
   RIGHT: `p-6` (24px)

2. **Colors are always token references + fallback hex.**
   WRONG: "brand blue"
   RIGHT: `text-brand-500` (#2563EB) — from CLAUDE.md tokens

3. **Sizes are always in the project's unit system.**
   If Tailwind: use Tailwind classes as primary, px as annotation
   If CSS: use rem as primary, px as annotation
   WRONG: "make it bigger on desktop"
   RIGHT: `text-lg` (18px) at ≥768px, `text-base` (16px) below

4. **Conditionals use explicit if/else, never "as needed."**
   WRONG: "show loading state as appropriate"
   RIGHT: "if data fetch takes >300ms, show skeleton. If fetch fails, show error state. If data returns empty array, show empty state."

5. **File paths are explicit.**
   WRONG: "create a button component"
   RIGHT: "create `src/components/ui/Button.tsx`"

6. **Every visual property is stated, never inherited by assumption.**
   Even if "obvious" — state it. AI agents don't have visual context.

---

## Document Structure

Generate the handoff document with these sections:

### SECTION 1: IMPLEMENTATION MAP

A priority-ordered table of everything to build.
AI agents should implement in this order to resolve dependencies correctly.

| Order | Component/Section | File Path | Dependencies | Complexity | Notes |
|-------|------------------|-----------|-------------|-----------|-------|
| 1 | Design tokens setup | `tailwind.config.ts` | None | Low | Must be first — all other components reference these |
| 2 | Typography components | `src/components/ui/Text.tsx` | Tokens | Low | Heading, Body, Caption, Label variants |
| 3 | Button | `src/components/ui/Button.tsx` | Tokens, Typography | Medium | 3 variants × 3 sizes × 6 states |
| ... | ... | ... | ... | ... | ... |

Rules:
- Nothing can reference a component that comes later in the table
- Complexity = how many variants × states the component has
- Notes = anything non-obvious about implementation

---

### SECTION 2: GLOBAL SPECIFICATIONS

These apply everywhere. AI agent should configure these BEFORE building any components.

#### 2.1 Breakpoints
Define exact behavior boundaries:

```
BREAKPOINTS {
  mobile:  0px    — 767px
  tablet:  768px  — 1023px
  desktop: 1024px — 1279px
  wide:    1280px — ∞
}
```

For each breakpoint, state:
- Container max-width and padding
- Base font size
- Global spacing multiplier (if it changes)
- Navigation mode (hamburger / horizontal / etc.)

#### 2.2 Transition Defaults
```
TRANSITIONS {
  default:    duration-200 ease-out
  slow:       duration-300 ease-in-out
  spring:     duration-500 cubic-bezier(0.34, 1.56, 0.64, 1)
  none:       duration-0
}

RULE: Every interactive element uses `default` unless
      this document specifies otherwise.
RULE: Transitions apply to: background-color, color, border-color,
      opacity, transform, box-shadow. Never to: width, height, padding,
      margin (these cause layout recalculation).
```

#### 2.3 Z-Index Scale
```
Z-INDEX {
  base:       0
  dropdown:   10
  sticky:     20
  overlay:    30
  modal:      40
  toast:      50
  tooltip:    60
}

RULE: No z-index value outside this scale. Ever.
```

#### 2.4 Focus Style
```
FOCUS {
  style:      ring-2 ring-offset-2 ring-brand-500
  applies-to: every interactive element (buttons, links, inputs, selects, checkboxes)
  visible:    only on keyboard navigation (use focus-visible, not focus)
}
```

---

### SECTION 3: PAGE SPECIFICATIONS

For each page, provide a complete implementation spec.

#### Page: ${page_name}
**Route:** `/exact-route-path`
**Layout:** ${which_layout_wrapper_to_use}
**Data requirements:** [what data this page needs, from where]

##### Page Structure (top to bottom)

```
PAGE STRUCTURE: ${page_name}
├── Section: Hero
│   ├── Component: Heading (h1)
│   ├── Component: Subheading (p)
│   ├── Component: CTA Button (primary, lg)
│   └── Component: HeroImage
├── Section: Features
│   ├── Component: SectionHeading (h2)
│   └── Component: FeatureCard × 3 (grid)
├── Section: Testimonials
│   └── Component: TestimonialSlider
└── Section: CTA
    ├── Component: Heading (h2)
    └── Component: CTA Button (primary, lg)
```

##### Section-by-Section Specs

For each section:

**${section_name}**

```
LAYOUT {
  container:    max-w-[1280px] mx-auto px-6 (mobile: px-4)
  direction:    flex-col (mobile) → flex-row (desktop)
  gap:          gap-8 (32px)
  padding:      py-16 (64px) (mobile: py-10)
  background:   bg-white
}

CONTENT {
  heading {
    text:       "${exact_heading_text_or_content_source}"
    element:    h2
    class:      text-3xl font-bold text-gray-900 (mobile: text-2xl)
    max-width:  max-w-[640px]
  }
  body {
    text:       "${exact_body_text_or_content_source}"
    class:      text-lg text-gray-600 leading-relaxed (mobile: text-base)
    max-width:  max-w-[540px]
  }
}

GRID (if applicable) {
  columns:      grid-cols-3 (tablet: grid-cols-2) (mobile: grid-cols-1)
  gap:          gap-6 (24px)
  items:        ${what_component_renders_in_each_cell}
  alignment:    items-start
}

ANIMATION (if applicable) {
  type:         fade-up on scroll
  trigger:      when section enters viewport (threshold: 0.2)
  stagger:      each child delays 100ms after previous
  duration:     duration-500
  easing:       ease-out
  runs:         once (do not re-trigger on scroll up)
}
```

---

### SECTION 4: COMPONENT SPECIFICATIONS

For each component, provide a complete implementation contract.

#### Component: ${componentname}
**File:** `src/components/${path}/${componentname}.tsx`
**Purpose:** [one sentence — what this component does]

##### Props Interface
```typescript
interface ${componentname}Props {
  variant: 'primary' | 'secondary' | 'ghost'     // visual style
  size: 'sm' | 'md' | 'lg'                        // dimensions
  disabled?: boolean                                // default: false
  loading?: boolean                                 // default: false
  icon?: React.ReactNode                           // optional leading icon
  children: React.ReactNode                         // label content
  onClick?: () => void                              // click handler
}
```

##### Variant × Size Matrix
Define exact values for every combination:

```
VARIANT: primary
  SIZE: sm
    height:           h-8 (32px)
    padding:          px-3 (12px)
    font:             text-sm font-medium (14px)
    background:       bg-brand-500 (#2563EB)
    text:             text-white (#FFFFFF)
    border:           none
    border-radius:    rounded-md (6px)
    shadow:           none

  SIZE: md
    height:           h-10 (40px)
    padding:          px-4 (16px)
    font:             text-sm font-medium (14px)
    background:       bg-brand-500 (#2563EB)
    text:             text-white (#FFFFFF)
    border:           none
    border-radius:    rounded-lg (8px)
    shadow:           shadow-sm

  SIZE: lg
    height:           h-12 (48px)
    padding:          px-6 (24px)
    font:             text-base font-semibold (16px)
    background:       bg-brand-500 (#2563EB)
    text:             text-white (#FFFFFF)
    border:           none
    border-radius:    rounded-lg (8px)
    shadow:           shadow-sm

VARIANT: secondary
  [same structure, different values]

VARIANT: ghost
  [same structure, different values]
```

##### State Specifications
Every state must be defined for every variant:

```
STATES (apply to ALL variants unless overridden):

  hover {
    background:     ${token} — darken one step from default
    transform:      none (no scale/translate on hover)
    shadow:         ${token_or_none}
    cursor:         pointer
    transition:     default (duration-200 ease-out)
  }

  active {
    background:     ${token} — darken two steps from default
    transform:      scale-[0.98]
    transition:     duration-75
  }

  focus-visible {
    ring:           ring-2 ring-offset-2 ring-brand-500
    all other:      same as default state
  }

  disabled {
    opacity:        opacity-50
    cursor:         not-allowed
    pointer-events: none
    ALL hover/active/focus states: do not apply
  }

  loading {
    content:        replace children with spinner (16px, animate-spin)
    width:          maintain same width as non-loading state (prevent layout shift)
    pointer-events: none
    opacity:        opacity-80
  }
```

##### Icon Behavior
```
ICON RULES {
  position:       left of label text (always)
  size:           16px (sm), 16px (md), 20px (lg)
  gap:            gap-1.5 (sm), gap-2 (md), gap-2 (lg)
  color:          inherits text color (currentColor)
  when loading:   icon is hidden, spinner takes its position
  icon-only:      if no children, component becomes square (width = height)
                  add aria-label prop requirement
}
```

---

### SECTION 5: INTERACTION FLOWS

For each user flow, provide step-by-step implementation:

#### Flow: [Flow Name, e.g., "User Signs Up"]
```
TRIGGER:     user clicks "Sign Up" button in header

STEP 1:      Modal opens
             animation:   fade-in (opacity 0→1, duration-200)
             backdrop:    bg-black/50, click-outside closes modal
             focus:       trap focus inside modal, auto-focus first input
             body:        scroll-lock (prevent background scroll)

STEP 2:      User fills form
             fields:      ${list_exact_fields_with_validation_rules}
             validation:  on blur (not on change — reduces noise)
             
             field: email {
               type:       email
               required:   true
               validate:   regex pattern + "must contain @ and domain"
               error:      "That doesn't look like an email — check for typos"
               success:    green checkmark icon appears (fade-in, duration-150)
             }
             
             field: password {
               type:       password (with show/hide toggle)
               required:   true
               validate:   min 8 chars, 1 uppercase, 1 number
               error:      show checklist of requirements, highlight unmet
               strength:   show strength bar (weak/medium/strong)
             }

STEP 3:      User submits
             button:      shows loading state (see Button component spec)
             request:     POST /api/auth/signup
             duration:    expect 1-3 seconds

STEP 4a:     Success
             modal:       content transitions to success message (crossfade, duration-200)
             message:     "Account created! Check your email to verify."
             action:      "Got it" button closes modal
             redirect:    after close, redirect to /dashboard
             toast:       none (the modal IS the confirmation)

STEP 4b:     Error — email exists
             field:       email input shows error state
             message:     "This email already has an account — want to log in instead?"
             action:      "Log in" link switches modal to login form
             button:      returns to default state (not loading)

STEP 4c:     Error — network failure
             display:     error banner at top of modal (not a toast)
             message:     "Something went wrong on our end. Try again?"
             action:      "Try again" button re-submits
             button:      returns to default state

STEP 4d:     Error — rate limited
             display:     error banner
             message:     "Too many attempts. Wait 60 seconds and try again."
             button:      disabled for 60 seconds with countdown visible
```

---

### SECTION 6: RESPONSIVE BEHAVIOR RULES

Don't describe what changes — specify the exact rules:

```
RESPONSIVE RULES:

Rule 1: Navigation
  ≥1024px:    horizontal nav, all items visible
  <1024px:    hamburger icon, slide-in drawer from right
              drawer-width: 80vw (max-w-[320px])
              animation: translate-x (duration-300 ease-out)
              backdrop: bg-black/50, click-outside closes

Rule 2: Grid Sections
  ≥1024px:    grid-cols-3
  768-1023px: grid-cols-2 (last item spans full if odd count)
  <768px:     grid-cols-1

Rule 3: Hero Section
  ≥1024px:    two-column (text left, image right) — 55/45 split
  <1024px:    single column (text top, image bottom)
              image max-height: 400px, object-cover

Rule 4: Typography Scaling
  ≥1024px:    h1=text-5xl, h2=text-3xl, h3=text-xl, body=text-base
  <1024px:    h1=text-3xl, h2=text-2xl, h3=text-lg, body=text-base

Rule 5: Spacing Scaling
  ≥1024px:    section-padding: py-16, container-padding: px-8
  768-1023px: section-padding: py-12, container-padding: px-6
  <768px:     section-padding: py-10, container-padding: px-4

Rule 6: Touch Targets
  <1024px:    all interactive elements minimum 44×44px hit area
              if visual size < 44px, use invisible padding to reach 44px

Rule 7: Images
  all images: use next/image with responsive sizes prop
  hero:       sizes="(max-width: 1024px) 100vw, 50vw"
  grid items: sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
```

---

### SECTION 7: EDGE CASES & BOUNDARY CONDITIONS

This section prevents the "but what happens when..." problems:

```
EDGE CASES:

Text Overflow {
  headings:     max 2 lines, then truncate with text-ellipsis (add title attr for full text)
  body text:    allow natural wrapping, no truncation
  button labels: single line only, max 30 characters, no truncation (design constraint)
  nav items:    single line, truncate if >16 characters on mobile
  table cells:  truncate with tooltip on hover
}

Empty States {
  lists/grids with 0 items: show ${emptystate} component
    - illustration: ${describe_or_reference_asset}
    - heading: "${exact_text}"
    - body: "${exact_text}"
    - CTA: "${exact_text}" → ${action}
  
  user avatar missing: show initials on colored background
    - background: generate from user name hash (deterministic)
    - initials: first letter of first + last name, uppercase
    - font: text-sm font-medium text-white
  
  image fails to load: show gray placeholder with image icon
    - background: bg-gray-100
    - icon: ImageOff from lucide-react, text-gray-400, 24px
}

Loading States {
  page load:      full-page skeleton (not spinner)
  component load: component-level skeleton matching final dimensions
  button action:  inline spinner in button (see Button spec)
  infinite list:  skeleton row × 3 at bottom while fetching next page
  
  skeleton style: bg-gray-200 rounded animate-pulse
  skeleton rule:  skeleton shape must match final content shape
                  (rectangle for text, circle for avatars, rounded-lg for cards)
}

Error States {
  API error (500):     show inline error banner with retry button
  Network error:       show "You seem offline" banner at top (auto-dismiss when reconnected)
  404 content:         show custom 404 component (not Next.js default)
  Permission denied:   redirect to /login with return URL param
  Form validation:     inline per-field (see flow specs), never alert()
}

Data Extremes {
  username 1 character:   display normally
  username 50 characters: truncate at 20 in nav, full in profile
  price $0.00:            show "Free"
  price $999,999.99:      ensure layout doesn't break (test with formatted number)
  list with 1 item:       same layout as multiple (no special case)
  list with 500 items:    paginate at 20, show "Load more" button
  date today:             show "Today" not the date
  date this year:         show "Mar 13" not "Mar 13, 2026"
  date other year:        show "Mar 13, 2025"
}
```

---

### SECTION 8: IMPLEMENTATION VERIFICATION CHECKLIST

After implementation, the AI agent (or human developer) should verify:

```
VERIFICATION:

□ Every component matches the variant × size matrix exactly
□ Every state (hover, active, focus, disabled, loading) works
□ Tab order follows visual order on all pages
□ Focus-visible ring appears on keyboard nav, not on mouse click
□ All transitions use specified duration and easing (not browser default)
□ No layout shift during page load (check CLS)
□ Skeleton states match final content dimensions
□ All edge cases from Section 7 are handled
□ Touch targets ≥ 44×44px on mobile breakpoints
□ No horizontal scroll at any breakpoint
□ All images use next/image with correct sizes prop
□ Z-index values only use the defined scale
□ Error states display correctly (test with network throttle)
□ Empty states display correctly (test with empty data)
□ Text truncation works at boundary lengths
□ Dark mode tokens (if applicable) are all mapped
```

---

## How the AI Agent Should Use This Document

Include this instruction at the top of the generated handoff document
so the implementing AI knows how to work with it:

```
INSTRUCTIONS FOR AI IMPLEMENTATION AGENT:

1. Read this document fully before writing any code.
2. Implement in the order specified in SECTION 1 (Implementation Map).
3. Reference CLAUDE.md for token values. If a token referenced here
   is not in CLAUDE.md, flag it and use the fallback value provided.
4. Every value in this document is intentional. Do not substitute
   with "close enough" values. `gap-6` means `gap-6`, not `gap-5`.
5. Every state must be implemented. If a state is not specified for
   a component, that is a gap in the spec — flag it, do not guess.
6. After implementing each component, run through its state matrix
   and verify all states work before moving to the next component.
7. When encountering ambiguity, prefer the more explicit interpretation.
   If still ambiguous, add a TODO comment: "// HANDOFF-AMBIGUITY: [description]"
```
```

---

## Customization Notes

**If you're not using Tailwind:** Replace all Tailwind class references in the prompt with your system's equivalents. The structure stays the same — only the value format changes. Tell Claude: "Use CSS custom properties as primary, px values as annotations."

**If you're handing off to a specific AI tool:** Add tool-specific notes. For example, for Cursor: "Generate implementation as step-by-step edits to existing files, not full file rewrites." For Claude Code: "Create each component as a complete file, test it, then move to the next."

**If no CLAUDE.md exists yet:** Tell the prompt to generate a minimal token section at the top of the handoff document covering only the tokens needed for this specific handoff. It won't be a full design system, but it prevents hardcoded values.

**For multi-page projects:** Run the prompt once per page, but include Section 1 (Implementation Map) and Section 2 (Global Specs) only in the first run. Subsequent pages reference the same globals.
