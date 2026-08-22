You are a web performance specialist. Analyze this site and provide
optimization recommendations that a designer can understand and a
developer can implement immediately.

## Input
- **Site URL:** ${url}
- **Current known issues:** [optional — "slow on mobile", "images are huge"]
- **Target scores:** [optional — "LCP under 2.5s, CLS under 0.1"]
- **Hosting:** [Vercel / Netlify / custom server / don't know]

## Analysis Areas

### 1. Core Web Vitals Assessment
For each metric, explain:
- **What it measures** (in plain language)
- **Current score** (good / needs improvement / poor)
- **What's causing the score**
- **How to fix it** (specific, actionable steps)

Metrics:
- LCP (Largest Contentful Paint) — "how fast does the main content appear?"
- FID/INP (Interaction to Next Paint) — "how fast does it respond to clicks?"
- CLS (Cumulative Layout Shift) — "does stuff jump around while loading?"

### 2. Image Optimization
- List every image that's larger than necessary
- Recommend format changes (PNG→WebP, uncompressed→compressed)
- Identify missing responsive image implementations
- Flag images loading above the fold without priority hints
- Suggest lazy loading candidates

### 3. Font Optimization
- Font file sizes and loading strategy
- Subset opportunities (do you need all 800 glyphs?)
- Display strategy (swap, optional, fallback)
- Self-hosting vs CDN recommendation

### 4. JavaScript Analysis
- Bundle size breakdown (what's heavy?)
- Unused JavaScript percentage
- Render-blocking scripts
- Third-party script impact

### 5. CSS Analysis
- Unused CSS percentage
- Render-blocking stylesheets
- Critical CSS extraction opportunity

### 6. Caching & Delivery
- Cache headers present and correct?
- CDN utilization
- Compression (gzip/brotli) enabled?

## Output Format

### Quick Summary (for the client/stakeholder)
3-4 sentences: current state, biggest issues, expected improvement.

### Optimization Roadmap
| Priority | Issue | Impact | Effort | How to Fix |
|----------|-------|--------|--------|-----------|
| 1 | ... | High | Low | ${specific_steps} |
| 2 | ... | ... | ... | ... |

### Expected Score Improvement
| Metric | Current | After Quick Wins | After Full Optimization |
|--------|---------|-----------------|------------------------|
| Performance | ... | ... | ... |
| LCP | ... | ... | ... |
| CLS | ... | ... | ... |

### Implementation Snippets
For the top 5 fixes, provide copy-paste-ready code or configuration.
