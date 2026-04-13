# The Constitution of Scientific Visualization

**A Unified Framework for the Design, Construction, and Presentation of Visual Data in Scientific Publications**

*Synthesized from the NASA Earth Observatory "Subtleties of Color" series (Simmon, 2013), "Ten Simple Rules for Better Figures" (Rougier, Droettboom & Bourne, 2014), "Ten Guidelines for Effective Data Visualization in Scientific Publications" (Kelleher & Wagener, 2011), Nature Author Instructions, and supplementary practitioner literature on data storytelling, scientific illustration, and figure composition.*

---

## Preamble

A scientific figure is a graphical interface between people and data. Its purpose is to illuminate patterns and relationships that are otherwise hidden in an impenetrable mass of numbers. It is not decoration. It is not an afterthought. It is an argument rendered in light and geometry.

This constitution establishes the governing principles for the construction of scientific figures across all contexts — journal publication, oral presentation, poster display, and digital media. Where principles conflict, the hierarchy of resolution is: **accuracy first, clarity second, aesthetics third.** No figure may be beautiful at the expense of being true, nor precise at the expense of being understood.

The document is organized into ten Articles of principle, followed by six Amendments that impose operational constraints derived from the realities of journal economics, reviewer cognition, and perceptual physics.

---

## ARTICLE 1 — Audience and Intent

**§1.1** Before any visual design begins, two questions must be answered: *Who is the audience?* and *What is the single message this figure must convey?*

**§1.2** The audience determines the level of abstraction. A figure for direct collaborators may omit context that both parties already share. A figure for a journal article must be self-contained — interpretable by any competent scientist in the field without reference to the main text. A figure for a student audience must include scaffolding that makes the concept fully understood. A figure for the general public must be the simplest, most approximate rendering that preserves the salient result without distortion.

**§1.3** Each figure shall communicate exactly one message. This message functions as a decision filter for every subsequent design choice: plot type, color, axis range, annotation, and level of detail. If a figure attempts to convey two messages, it should be split into two figures.

**§1.4** A figure that conveys a striking message at first glance will draw more attention to the research it represents. The message should be visually salient — the eye should land on the answer before the brain has finished reading the caption.

**§1.5 — The Storytelling Frame.** Complex data benefits from narrative structure. The designer should identify the *characters* (the 2–4 most important data elements), the *setting* (the methods, tools, or scientific context that scaffold the story), the *conflict* (the comparison, decrease, increase, or deviation that creates tension), and the *resolution* (the result that the audience must understand at the end). Bold or saturated color is reserved exclusively for the narrative protagonist — the data element whose behavior *is* the message.

---

## ARTICLE 2 — Data Classification

**§2.1** All data fall into one of three types. The classification determines the palette, and violating the mapping between data type and palette type is a first-order error.

**§2.2 — Sequential Data.** Data that varies continuously along a single dimension (temperature, elevation, concentration, income). Sequential data is represented by a palette that varies uniformly in lightness, preferably with a simultaneous shift in hue and saturation. The change must be monotonic: the perceived difference between values 1 and 2 must equal the perceived difference between values 101 and 102. For data spanning orders of magnitude, logarithmic proportionality must be maintained.

**§2.3 — Divergent Data.** Data that varies from a central breakpoint — a zero, an average, a phase transition (profit/loss, departure from norm, magnetic polarity, temperature anomaly). Divergent data requires a bifurcated palette: two sequential ramps of different hues, symmetric in lightness and saturation, meeting at a neutral center (white or light gray). The neutral center must have no hue component; even a slight tint biases perception toward one end of the scale. Black or dark gray as the central value is almost always wrong — it de-emphasizes the extremes. This palette leverages pre-attentive processing: the visual system can discriminate the two hues without conscious effort.

**§2.4 — Qualitative (Categorical) Data.** Discrete classes or categories with no inherent ordering (land cover types, political affiliation, experimental conditions). Qualitative data demands colors as distinct from one another as possible. Due to the limits of simultaneous contrast, the practical ceiling is approximately 12 distinguishable categories. Beyond that, group similar classes under a shared hue family (e.g., four urban densities as shades of red, three forest types as shades of green) and supplement with symbols, hatching, or direct labeling.

**§2.5 — Misclassification.** Applying a sequential palette to categorical data, or a qualitative palette to sequential data, is a structural error analogous to using the wrong statistical test. The rainbow palette, in particular, imposes qualitative boundaries (abrupt jumps at cyan and yellow) onto continuous data, fabricating patterns that do not exist in the data and suppressing patterns that do.

---

## ARTICLE 3 — The Perceptual Color Standard

**§3.1 — Lightness Is Sovereign.** Of the three perceptual dimensions of color — lightness, hue, and saturation — lightness is the strongest. Accurate, one-way changes in lightness are more important than those in hue or saturation. A palette with perfect lightness ramp and imperfect saturation will still read correctly. A palette with perfect hue rotation and broken lightness will mislead.

**§3.2 — The Ideal Sequential Palette** combines a continuous, linear increase in lightness with a simultaneous shift in hue and saturation — a spiral through perceptual color space. The smooth increase in lightness preserves the *form* of the data (patterns, gradients, topology). The shift in hue aids the reading of *exact quantities* (individual values). The change in saturation enhances contrast.

**§3.3 — Perceptual Color Spaces.** Palettes must be defined in a perceptual color space — CIE L\*C\*h or Munsell — not in RGB or HSV, which are engineered for machines and do not model human vision. A constant increase in RGB brightness is not perceived as linear, and the response differs for red, green, and blue. Tools that specify color in RGB or HSV will produce palettes that distort the underlying data.

**§3.4 — Simultaneous Contrast.** The perceived color of any region is shifted by the colors surrounding it. Monochromatic palettes are most susceptible; hue variation dampens the effect. When exact value-reading matters more than pattern-reading, increased hue variation reduces simultaneous-contrast errors.

**§3.5 — Color Blindness.** Approximately 5% of people (predominantly men) have some form of color vision deficiency. Red-green is the most common; blue-red is rarer. A sequential palette with uniform lightness variation remains readable under any form of color deficiency (and in black-and-white print). A divergent palette with matched lightness and differing hues only can be unreadable. Acceptable color-safe pairs include: green/magenta, turquoise/red, yellow/blue. Use Color Brewer's colorblind-safe filter, or simulate with a deuteranopia simulator, before finalizing any palette. The red-green combination is forbidden for encoding contrast.

**§3.6 — The Rainbow Palette.** The default rainbow (jet) colormap is prohibited for quantitative data unless a compelling, explicitly stated reason overrides the prohibition. Its documented failures: it confuses viewers through lack of perceptual ordering, obscures data through uncontrolled luminance variation, and actively misleads through the introduction of non-data-dependent gradients. The rainbow is acceptable only for purely qualitative segmentation where cool/warm associations carry semantic weight (e.g., climate zone maps).

---

## ARTICLE 4 — Composition, Layout, and Decluttering

**§4.1 — Simplicity as Default.** The simplest graph that conveys the intended message is the correct graph. Remove every visual element that does not carry data or aid interpretation. This includes: background shading, gratuitous 3D effects, grid lines that do not align with data, excessive tick marks, frames around legends, and any decorative element that does not tell the viewer something new. Maximize the *data-ink ratio*: the fraction of ink devoted to non-redundant data information versus total ink.

**§4.2 — Two Dimensions Unless Forced.** Three-dimensional plots make it difficult to compare datasets and distinguish values. They are sometimes useful during exploratory analysis but are almost never the correct choice for publication. Multi-dimensional data should be encoded in 2D space using color, shape, size, or panel subdivision (small multiples, coplots, scatter plot matrices).

**§4.3 — Composition Flow.** Design flow should follow reading direction: left to right, top to bottom, or in a circle. The most important data must occupy the visual focal point of the design. Panels within a multi-panel figure should align to an invisible grid and be labeled with lowercase boldface letters (a, b, c, ...) in the top-left corner.

**§4.4 — Data vs. Non-Data Separation.** Color attracts the eye; absence of color causes regions to recede. Areas of missing or invalid data should be rendered in a shade of gray (or black/white) that is clearly distinct from the adjacent data palette. This simultaneously de-emphasizes missing data and separates it from valid measurements. The gray chosen must not be confused with any value in the active palette.

**§4.5 — Figure-Ground Awareness.** Small, light-colored regions surrounded by large, dark-colored regions will perceptually advance to the foreground — even if they represent *lower* values. If this conflicts with the intended message, the palette must be adjusted. The designer must test the palette against the spatial distribution of the actual data, not just against an abstract ramp.

**§4.6 — Layering Multiple Datasets.** When two or more datasets are displayed together, their color schemes must be designed together and complement one another. Muted colors for a base dataset leave room for additional overlays (contour lines, shaded relief, category boundaries). This is impossible if a single dataset has already consumed the full rainbow.

**§4.7 — Non-Diverging Breakpoints.** Some sequential data have a physically significant threshold (e.g., freezing point on a temperature map). A full divergent palette is inappropriate because the data is still on a continuum. Instead, maintain consistent lightness change throughout the palette but introduce an abrupt shift in hue and/or saturation at the breakpoint. This preserves pattern while flagging the transition.

---

## ARTICLE 5 — Physical Constraints and Medium Adaptation

**§5.1 — Medium Determines Design.** Each display medium (journal page, poster, projection screen, computer monitor) implies a different figure. A figure designed for a printed article — where the reader controls viewing time and can zoom — may carry dense detail and a full caption. A figure designed for oral presentation — where the viewer has seconds, not minutes — must be stripped to its message, with thicker lines, larger labels, stronger contrast, and no vertical text.

**§5.2 — No Reuse Without Redesign.** The practice of extracting a figure from a journal article and placing it directly into a slide presentation is prohibited. The constraints of the two media are different. Each medium requires its own figure.

**§5.3 — Journal Specification Compliance.** Before beginning figure design, the designer must obtain the target journal's figure requirements: maximum number of figures, column widths (single and double), resolution minimums, acceptable file formats, font requirements, and color policies. These specifications are not formatting afterthoughts — they are the dimensional constraints within which the composition is engineered.

**§5.4 — Font and Line Standards.** Use a single typeface across all figures in a manuscript (Arial, Helvetica, or Times New Roman). At final print size, the optimum font size is 7–9 pt. No line shall be thinner than 0.25 pt (0.09 mm). Axis labels use sentence case (first word capitalized only) with no terminal period. Units must include a space between number and unit symbol. Images should be saved at 300 dpi minimum in RGB color mode.

---

## ARTICLE 6 — Color Economy and Hierarchy

**§6.1 — Color as Scarce Resource.** Color occupies perceptual bandwidth. Each additional hue in a figure competes for attention. A figure with one bold color against a neutral background has a clear hierarchy. A figure with six bold colors has none. Limit active color to 1–2 hues that make the main point stand out from the rest.

**§6.2 — The Question Test.** Before assigning any non-gray color, ask: *Is there a reason this element is blue and not black?* If no answer is available, the element should be black or gray. Color that does not carry information is noise.

**§6.3 — Intuitive Color.** Whenever the data has a natural color association, use it. Vegetation is green. Water is blue. Barren ground is gray or beige. Hot is red/orange/yellow. Cold is blue. Clouds are white. Cultural associations (clean = mint green, malevolent = ochre, abstract = blue) can supplement physical associations but vary by culture and must be used with awareness of audience.

**§6.4 — Consistency Across Figures.** Within a manuscript, the same variable must always be represented by the same color and symbol. Sample A is red triangles in Figure 1; it must be red triangles in Figure 5. Font sizes, marker sizes, line weights, and color assignments must be identical across all panels and all figures.

---

## ARTICLE 7 — Honesty and Anti-Deception

**§7.1 — Objective Representation.** A scientific figure is tied to data. If that tie is loosened — through misleading axis ranges, distorted shapes, or inappropriate chart types — the figure becomes propaganda regardless of the author's intent.

**§7.2 — Axis Origin.** When absolute magnitudes are the point (bar charts, histograms), the vertical axis must include zero. A bar chart beginning at a nonzero value visually exaggerates differences between bars by an arbitrary factor. When relative magnitudes are the point (scatter plots, line charts showing variation), the axis range should create a "lumpy profile" — set limits close to the data range to reveal variability and eliminate dead space.

**§7.3 — Pie Charts and 3D Charts.** Pie charts and 3D bar charts are known to induce incorrect perception of quantities. Both require expertise to use without misleading. When in doubt, use a simpler alternative: a dot plot, a 2D bar chart, or a table.

**§7.4 — Missing Data Integrity.** Lines connecting data points imply continuous, known values between those points. Lines must not be drawn across gaps in time-series data or between non-sequential categories. A gap in the line is the honest representation of a gap in the data.

**§7.5 — Overlapping Points.** In scatter plots, opaque points hide density. Multiple overlapping points render as a single point, concealing the most interesting structure in the data. Use transparency, unfilled markers, decreased point size, or kernel density overlays to make density differences visible.

**§7.6 — Axis Comparability.** When multiple subplots display related variables, maintain identical axis ranges to enable direct visual comparison. Subplots with different axis ranges for the same variable mislead the viewer about relative magnitudes and variabilities.

**§7.7 — Transformations.** Logarithmic, normalized, or other axis transformations alter the visual impression of rates of change. A linear plot emphasizes absolute rate of change; a log plot emphasizes percentage rate of change. The choice of transformation must be driven by the message, and the transformation must be clearly labeled. The Cleveland "banking to 45°" rule provides a useful heuristic for choosing aspect ratios that accurately represent slopes.

---

## ARTICLE 8 — Annotation: Captions, Labels, and Legends

**§8.1 — Captions Are Mandatory.** A figure without a caption is a figure without an argument. The caption explains how to read the figure, identifies all panels, variables, and symbols, and provides methodological context necessary for interpretation. The reader must be able to understand the result by examining the figure and caption alone — without reading the Results section.

**§8.2 — Caption Structure.** Begin with a single title sentence that states the main result of the figure. Then describe what is depicted: all panels, all variables, all methodological information required for interpretation. Captions are not the place for interpretation or conclusions drawn from the data — those belong in the text. Typical length: 50–250 words depending on journal.

**§8.3 — Label Clarity.** Axis titles, legend entries, and annotations must be immediately comprehensible. Spell out uncommon acronyms. Include units always. If only a few data series exist, place labels directly adjacent to the corresponding lines or points rather than using a separate legend box. Minimize the distance the eye must travel between data and its description.

**§8.4 — Simplified Legends.** Remove all redundancy from legends. Instead of "Current-voltage curve 1st run," "Current-voltage curve 2nd run," label as "1st run," "2nd run." If space allows, embed the legend within the plot area to reduce eye travel.

---

## ARTICLE 9 — Aesthetic Calibration

**§9.1 — Aesthetics Matter.** Attractive things work better. This is not an opinion — it is a documented feature of human cognition. A well-designed figure is more likely to be studied carefully and understood correctly. Follow good design practice (typography, alignment, proportion, whitespace) alongside good visualization practice.

**§9.2 — Message Over Beauty.** When aesthetics and message conflict, message wins absolutely. A visually rough figure that communicates clearly is superior to a beautiful figure that obscures the result. Domain-specific conventions exist because they facilitate direct comparison between studies — learn and respect them before inventing new visual idioms.

**§9.3 — Design Awareness.** Consider how the colors of the data interact with labels, axes, and nearby graphical elements. Design for the actual output medium (web, television, print). Be aware of how all elements fit together. A good visualization is better than the sum of its parts.

**§9.4 — Refinement Loop.** It is normal to produce 2–3 versions of a figure before settling on a final design. The refinement process uses three clarity checkpoints: (1) Does the figure show the story when the text is hidden? If not, improve the data visualization. (2) Can unnecessary elements that attract attention be removed or dimmed? (3) Does the color palette enhance or distract from the story?

---

## ARTICLE 10 — Tools, Defaults, and Workflow

**§10.1 — Do Not Trust Defaults.** Every plotting library ships with defaults that are good enough for any figure but best for none. The specific aesthetic of each software package (MATLAB, Excel, matplotlib, ggplot2) is instantly recognizable — and signals that no deliberate design occurred. All plots require manual tuning.

**§10.2 — Separation of Analysis and Presentation.** The software used to analyze data need not be the software used to produce the final figure. Data can be exported. Use the tool that produces the best output for the medium, not the tool that happens to have your data loaded.

**§10.3 — Recommended Tools.** matplotlib (Python, publication-quality 2D with some 3D), R/ggplot2 (statistical graphics), Inkscape (vector editing and polish), TikZ/PGF (TeX-native programmatic graphics), GIMP/Photoshop (raster editing), D3.js (interactive web graphics), Cytoscape (network visualization), Circos (relational and multi-layered annotation data). For color: ColorBrewer (all three data types, colorblind-safe filter), NASA Ames Color Tool (CIE L\*C\*h to RGB conversion), chroma.js (perceptual gradient generation), I Want Hue (qualitative palette generation).

**§10.4 — Graph Selection by Purpose.** Define the purpose of the data first, then choose the graph type that matches. The five primary purposes: *explain a process* (flowcharts, diagrams, Sankey diagrams, timelines), *compare or contrast* (bar charts, dot plots, grouped bars, radar charts), *show a change* (line plots, area charts, slope charts), *establish a relationship* (scatter plots, bubble plots, heatmaps, correlation matrices), *show composition* (stacked bars, treemaps, waffle charts). Pie charts are a last resort.

---

## AMENDMENTS

The following Amendments impose operational constraints that override or refine the Articles above. They address realities that the theoretical principles do not fully anticipate: journal economics, reviewer cognition, perceptual physics of printed patterns, and the geometry of deception.

---

### AMENDMENT I — The Law of Hard Formatting Boundaries

*Updates Article 5.*

Visual composition must not begin on an infinite digital canvas; it must be engineered natively for its terminal physical constraints. Figures must be constructed from the outset to exact journal specifications (e.g., exactly 89 mm for a single-column Nature figure or 183 mm for a double-column layout). Scaling a figure down at the end destroys text legibility, line weights, and narrative clarity. The physical geometry dictates the composition, not the other way around.

**Operational rule:** The first action in figure creation is setting the canvas to the journal's published dimensions. All font sizes, line weights, and marker sizes are specified at 100% scale. If the figure does not read correctly at its final print size, it is redesigned — not rescaled.

---

### AMENDMENT II — The Financial and Justification Standard for Color

*Updates Article 6.*

Color is not merely a perceptual tool; it is a budget line item and a cognitive load. Because print journals impose financial penalties for color (often hundreds of dollars per figure), the default state of any scientific visualization is black, white, and solid grayscale. Color is prohibited unless a specific hue is computationally required to encode a distinct data dimension that cannot be encoded by gray value alone, or to highlight the specific narrative protagonist of the data story.

**Operational rule:** For each colored element, the designer must be able to answer: *What information would be lost if this were gray?* If the answer is "none," the element must be gray. Online-only supplements, where color is free, are exempt from the financial constraint but not from the cognitive-load constraint.

---

### AMENDMENT III — The Principle of Intentional Imprecision

*Updates Article 9.*

The aesthetic fidelity of a figure must never exceed the epistemic certainty of the data it represents. If a model is a rough approximation, a mechanism is hypothesized rather than confirmed, or a data point carries large uncertainty, the visual rendering must reflect that status. Perfecting the aesthetic of a guess falsely implies mathematical precision. In these cases, intentional roughness — sketch-style rendering, hand-drawn aesthetics, or explicitly approximate annotation — is the most ethically accurate representation.

**Operational rule:** Conceptual diagrams, hypothetical relationships, and schematic overviews should use a visual style that is clearly distinguishable from data plots. Removing tick labels from axes that carry no measured values, using cartoon-style rendering for hypothetical mechanisms, or explicitly labeling axes as "schematic" are all acceptable implementations. The viewer should never mistake a hypothesis for a measurement.

---

### AMENDMENT IV — The Ban on Optical Vibration

*Updates Article 4.*

The use of fill patterns — cross-hatching, dots, diagonal lines, stippling, or any repeating geometric texture — within bars, shapes, or filled regions is forbidden. These patterns cause visual vibration (moiré effects), distract from the data-ink, interfere with adjacent patterns, and degrade unpredictably when printed, photocopied, projected, or compressed to JPEG. Differentiation between categories must be achieved through solid shades of gray, varying line weights, or direct labeling.

**Operational rule:** If a reviewer or journal style guide requests hatching to distinguish categories in a bar chart, substitute solid gray values (e.g., 20%, 40%, 60%, 80% gray) or use an alternative encoding such as a Cleveland dot plot.

---

### AMENDMENT V — The Geometric Integrity of Scale

*Updates Article 7.*

When mapping quantitative data to two-dimensional shapes (scatter plot bubbles, proportional symbols, circle-encoded values), the data must scale to the shape's **area**, never its radius or diameter. Mapping a linear data increase to a radius produces a quadratic distortion of the perceived size, because area scales as the square of the radius. A value of 30 represented by radius will appear nine times larger than a value of 10, when the true ratio is 3:1.

**Operational rule:** In any plotting library, verify whether the `size` parameter controls radius or area. In matplotlib, the `s` parameter in `scatter()` controls area (correct). In some other libraries, it controls radius (incorrect for proportional encoding). When in doubt, compute area values explicitly: `display_size = data_value * scaling_constant`.

---

### AMENDMENT VI — The Reviewer Workflow Mandate

*Updates Article 8.*

During the initial submission phase, the reviewer's cognitive load is the ultimate bottleneck. All figures and their corresponding captions must be embedded directly in the flow of the manuscript text, at or near the point of first reference. Forcing a reviewer to toggle between a multi-page manuscript and a separate folder of high-resolution figure files breaks concentration and increases the probability of superficial review.

**Operational rule:** For initial submission, produce a single PDF or Word file containing text, figures, and captions integrated together. Each figure legend appears on the same page as its figure. High-resolution separation into individual image files is reserved strictly for the final typesetting phase after acceptance. Nature's own author instructions explicitly endorse this practice.

---

## APPENDIX A — Quick-Reference Decision Tree

**What kind of data do I have?**

- Continuous, one direction → **Sequential palette** (uniform lightness ramp + hue shift)
- Continuous, with a meaningful center → **Divergent palette** (two hues from neutral center)
- Discrete categories → **Qualitative palette** (maximally distinct hues, ≤12)

**What is the purpose of my figure?**

- Explain a process → Flowchart, diagram, Sankey, timeline
- Compare or contrast → Bar chart, dot plot, grouped bar, table
- Show a change → Line plot, area chart, slope chart
- Establish a relationship → Scatter plot, bubble plot, heatmap
- Show composition → Stacked bar, treemap, waffle chart

**Should this element be in color?**

1. Would information be lost if it were gray? → If no: use gray.
2. Is it the narrative protagonist of the figure? → If yes: color.
3. Does the data type require hue to encode a dimension? → If yes: color.
4. All other cases → gray or black.

---

## APPENDIX B — Pre-Submission Checklist

- [ ] Each figure communicates exactly one message
- [ ] Plot type matches data type and purpose
- [ ] Palette type matches data classification (sequential / divergent / qualitative)
- [ ] Lightness ramp is monotonic and perceptually uniform
- [ ] No rainbow palette on quantitative data without explicit justification
- [ ] Colorblind-safe (simulated with deuteranopia filter)
- [ ] No fill patterns (Amendment IV)
- [ ] Bubble/symbol sizes scale to area, not radius (Amendment V)
- [ ] Canvas set to journal column width from the start (Amendment I)
- [ ] Fonts 7–9 pt at print size; lines ≥ 0.25 pt
- [ ] Consistent color, symbols, fonts across all figures
- [ ] Gray or neutral tone for missing/no-data regions
- [ ] Axis starts at zero for bar charts; "lumpy profile" for scatter/line plots
- [ ] No lines drawn across data gaps
- [ ] Overlapping scatter points use transparency or unfilled markers
- [ ] Captions begin with a result sentence, explain all panels and symbols
- [ ] Figures embedded in manuscript for initial submission (Amendment VI)
- [ ] Grayscale default; color justified per Amendment II
- [ ] Aesthetic fidelity does not exceed epistemic certainty (Amendment III)
- [ ] Defaults overridden — no software-recognizable styling
- [ ] Figure reviewed by at least one colleague for interpretation check

---

*Ratified from the accumulated knowledge of cartographers, perceptual scientists, graphic designers, and working researchers. Subject to amendment as the science of visualization advances.*
