---
name: accessibility-expert
description: Tests and remediates accessibility issues for WCAG compliance and assistive technology compatibility. Use when (1) auditing UI for accessibility violations, (2) implementing keyboard navigation or screen reader support, (3) fixing color contrast or focus indicator issues, (4) ensuring form accessibility and error handling, (5) creating ARIA implementations.
---

# Accessibility Testing and Remediation

## Configuration

- **WCAG Level**: ${wcag_level:AA}
- **Target Component**: ${component_name:Application}
- **Compliance Standard**: ${compliance_standard:WCAG 2.1}
- **Testing Scope**: ${testing_scope:full-audit}
- **Screen Reader**: ${screen_reader:NVDA}

## WCAG 2.1 Quick Reference

### Compliance Levels
| Level | Requirement | Common Issues |
|-------|-------------|---------------|
| A | Minimum baseline | Missing alt text, no keyboard access, missing form labels |
| ${wcag_level:AA} | Standard target | Contrast < 4.5:1, missing focus indicators, poor heading structure |
| AAA | Enhanced | Contrast < 7:1, sign language, extended audio description |

### Four Principles (POUR)
1. **Perceivable**: Content available to senses (alt text, captions, contrast)
2. **Operable**: UI navigable by all input methods (keyboard, touch, voice)
3. **Understandable**: Content and UI predictable and readable
4. **Robust**: Works with current and future assistive technologies

## Violation Severity Matrix

```
CRITICAL (fix immediately):
  - No keyboard access to interactive elements
  - Missing form labels
  - Images without alt text
  - Auto-playing audio without controls
  - Keyboard traps

HIGH (fix before release):
  - Contrast ratio below ${min_contrast_ratio:4.5}:1 (text) or 3:1 (large text)
  - Missing skip links
  - Incorrect heading hierarchy
  - Focus not visible
  - Missing error identification

MEDIUM (fix in next sprint):
  - Inconsistent navigation
  - Missing landmarks
  - Poor link text ("click here")
  - Missing language attribute
  - Complex tables without headers

LOW (backlog):
  - Timing adjustments
  - Multiple ways to find content
  - Context-sensitive help
```

## Testing Decision Tree

```
Start: What are you testing?
|
+-- New Component
|   +-- Has interactive elements? --> Keyboard Navigation Checklist
|   +-- Has text content? --> Check contrast + heading structure
|   +-- Has images? --> Verify alt text appropriateness
|   +-- Has forms? --> Form Accessibility Checklist
|
+-- Existing Page/Feature
|   +-- Run automated scan first (axe-core, Lighthouse)
|   +-- Manual keyboard walkthrough
|   +-- Screen reader verification
|   +-- Color contrast spot-check
|
+-- Third-party Widget
    +-- Check ARIA implementation
    +-- Verify keyboard support
    +-- Test with screen reader
    +-- Document limitations
```

## Keyboard Navigation Checklist

```markdown
[ ] All interactive elements reachable via Tab
[ ] Tab order follows visual/logical flow
[ ] Focus indicator visible (${focus_indicator_width:2}px+ outline, 3:1 contrast)
[ ] No keyboard traps (can Tab out of all elements)
[ ] Skip link as first focusable element
[ ] Enter activates buttons and links
[ ] Space activates checkboxes and buttons
[ ] Arrow keys navigate within components (tabs, menus, radio groups)
[ ] Escape closes modals and dropdowns
[ ] Modals trap focus until dismissed
```

## Screen Reader Testing Patterns

### Essential Announcements to Verify
```
Interactive Elements:
  Button: "[label], button"
  Link: "[text], link"
  Checkbox: "[label], checkbox, [checked/unchecked]"
  Radio: "[label], radio button, [selected], [position] of [total]"
  Combobox: "[label], combobox, [collapsed/expanded]"

Dynamic Content:
  Loading: Use aria-busy="true" on container
  Status: Use role="status" for non-critical updates
  Alert: Use role="alert" for critical messages
  Live regions: aria-live="${aria_live_politeness:polite}"

Forms:
  Required: "required" announced with label
  Invalid: "invalid entry" with error message
  Instructions: Announced with label via aria-describedby
```

### Testing Sequence
1. Navigate entire page with Tab key, listening to announcements
2. Test headings navigation (H key in screen reader)
3. Test landmark navigation (D key / rotor)
4. Test tables (T key, arrow keys within table)
5. Test forms (F key, complete form submission)
6. Test dynamic content updates (verify live regions)

## Color Contrast Requirements

| Text Type | Minimum Ratio | Enhanced (AAA) |
|-----------|---------------|----------------|
| Normal text (<${large_text_threshold:18}pt) | ${min_contrast_ratio:4.5}:1 | 7:1 |
| Large text (>=${large_text_threshold:18}pt or 14pt bold) | 3:1 | 4.5:1 |
| UI components & graphics | 3:1 | N/A |
| Focus indicators | 3:1 | N/A |

### Contrast Check Process
```
1. Identify all foreground/background color pairs
2. Calculate contrast ratio: (L1 + 0.05) / (L2 + 0.05)
   where L1 = lighter luminance, L2 = darker luminance
3. Common failures to check:
   - Placeholder text (often too light)
   - Disabled state (exempt but consider usability)
   - Links within text (must distinguish from text)
   - Error/success states on colored backgrounds
   - Text over images (use overlay or text shadow)
```

## ARIA Implementation Guide

### First Rule of ARIA
Use native HTML elements when possible. ARIA is for custom widgets only.

```html
<!-- WRONG: ARIA on native element -->
<div role="button" tabindex="0">Submit</div>

<!-- RIGHT: Native button -->
<button type="submit">Submit</button>
```

### When ARIA is Needed
```html
<!-- Custom tabs -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel2">Tab 2</button>
</div>
<div role="tabpanel" id="panel1">Content 1</div>
<div role="tabpanel" id="panel2" hidden>Content 2</div>

<!-- Expandable section -->
<button aria-expanded="false" aria-controls="content">Show details</button>
<div id="content" hidden>Expandable content</div>

<!-- Modal dialog -->
<div role="dialog" aria-modal="true" aria-labelledby="title">
  <h2 id="title">Dialog Title</h2>
  <!-- content -->
</div>

<!-- Live region for dynamic updates -->
<div aria-live="${aria_live_politeness:polite}" aria-atomic="true">
  <!-- Status messages injected here -->
</div>
```

### Common ARIA Mistakes
```
- role="button" without keyboard support (Enter/Space)
- aria-label duplicating visible text
- aria-hidden="true" on focusable elements
- Missing aria-expanded on disclosure buttons
- Incorrect aria-controls reference
- Using aria-describedby for essential information
```

## Form Accessibility Patterns

### Required Form Structure
```html
<form>
  <!-- Explicit label association -->
  <label for="email">Email address</label>
  <input type="email" id="email" name="email"
         aria-required="true"
         aria-describedby="email-hint email-error">
  <span id="email-hint">We'll never share your email</span>
  <span id="email-error" role="alert"></span>

  <!-- Group related fields -->
  <fieldset>
    <legend>Shipping address</legend>
    <!-- address fields -->
  </fieldset>

  <!-- Clear submit button -->
  <button type="submit">Complete order</button>
</form>
```

### Error Handling Requirements
```
1. Identify the field in error (highlight + icon)
2. Describe the error in text (not just color)
3. Associate error with field (aria-describedby)
4. Announce error to screen readers (role="alert")
5. Move focus to first error on submit failure
6. Provide correction suggestions when possible
```

## Mobile Accessibility Checklist

```markdown
Touch Targets:
[ ] Minimum ${touch_target_size:44}x${touch_target_size:44} CSS pixels
[ ] Adequate spacing between targets (${touch_target_spacing:8}px+)
[ ] Touch action not dependent on gesture path

Gestures:
[ ] Alternative to multi-finger gestures
[ ] Alternative to path-based gestures (swipe)
[ ] Motion-based actions have alternatives

Screen Reader (iOS/Android):
[ ] accessibilityLabel set for images and icons
[ ] accessibilityHint for complex interactions
[ ] accessibilityRole matches element behavior
[ ] Focus order follows visual layout
```

## Automated Testing Integration

### Pre-commit Hook
```bash
#!/bin/bash
# Run axe-core on changed files
npx axe-core-cli --exit src/**/*.html

# Check for common issues
grep -r "onClick.*div\|onClick.*span" src/ && \
  echo "Warning: Click handler on non-interactive element" && exit 1
```

### CI Pipeline Checks
```yaml
accessibility-audit:
  script:
    - npx pa11y-ci --config .pa11yci.json
    - npx lighthouse --accessibility --output=json
  artifacts:
    paths:
      - accessibility-report.json
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
```

### Minimum CI Thresholds
```
axe-core: 0 critical violations, 0 serious violations
Lighthouse accessibility: >= ${lighthouse_a11y_threshold:90}
pa11y: 0 errors (warnings acceptable)
```

## Remediation Priority Framework

```
Priority 1 (This Sprint):
  - Blocks user task completion
  - Legal compliance risk
  - Affects many users

Priority 2 (Next Sprint):
  - Degrades experience significantly
  - Automated tools flag as error
  - Violates ${wcag_level:AA} requirement

Priority 3 (Backlog):
  - Minor inconvenience
  - Violates AAA only
  - Affects edge cases

Priority 4 (Enhancement):
  - Improves usability for all
  - Best practice, not requirement
  - Future-proofing
```

## Verification Checklist

Before marking accessibility work complete:

```markdown
Automated:
[ ] axe-core: 0 violations
[ ] Lighthouse accessibility: ${lighthouse_a11y_threshold:90}+
[ ] HTML validation passes
[ ] No console accessibility warnings

Keyboard:
[ ] Complete all tasks keyboard-only
[ ] Focus visible at all times
[ ] Tab order logical
[ ] No keyboard traps

Screen Reader (test with at least one):
[ ] All content announced
[ ] Interactive elements labeled
[ ] Errors and updates announced
[ ] Navigation efficient

Visual:
[ ] All text passes contrast
[ ] UI components pass contrast
[ ] Works at ${zoom_level:200}% zoom
[ ] Works in high contrast mode
[ ] No seizure-inducing flashing

Forms:
[ ] All fields labeled
[ ] Errors identifiable
[ ] Required fields indicated
[ ] Instructions available
```

## Documentation Template

```markdown
# Accessibility Statement

## Conformance Status
This [website/application] is [fully/partially] conformant with ${compliance_standard:WCAG 2.1} Level ${wcag_level:AA}.

## Known Limitations
| Feature | Issue | Workaround | Timeline |
|---------|-------|------------|----------|
| [Feature] | [Description] | [Alternative] | [Fix date] |

## Assistive Technology Tested
- ${screen_reader:NVDA} [version] with Firefox [version]
- VoiceOver with Safari [version]
- JAWS [version] with Chrome [version]

## Feedback
Contact [email] for accessibility issues.
Last updated: [date]
```
