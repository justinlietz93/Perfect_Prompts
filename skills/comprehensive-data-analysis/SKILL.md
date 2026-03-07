---
name: comprehensive-data-analysis
description: Execute complete, rigorous data analysis workflows from problem understanding through validated results delivery. Specializes in physics/scientific analyses while handling any analytical domain. Delivers publication-quality packages with full reproducibility.
---

# Comprehensive Data Analysis Skill

## Purpose
Execute complete, rigorous data analysis workflows from problem understanding through validated results delivery. Specializes in physics/scientific analyses while handling any analytical domain. Delivers publication-quality packages with full reproducibility.

## Activation Triggers
Use this skill when the user says:
- "analyze this data"
- "run a complete analysis on..."
- "test these predictions against..."
- Any mention of data analysis requiring multi-stage workflows
- Requests involving hypothesis testing, model validation, or scientific investigation

## Core Philosophy

**Scientific Rigor Without Dogma:**
- Maintain highest standards of statistical and methodological rigor
- Never dismiss results for being unconventional, strange, or unexpected
- Any result is scientifically valid unless thoroughly proven otherwise
- Distinguish between "low confidence" and "falsified" - they are not the same
- Strange results demand explanation, not dismissal

**Iterative Validation:**
- Three attempts maximum with full results reporting for each
- Each attempt learns from previous issues
- Confidence must be earned through validation, not assumed

## Workflow Stages

### Stage 1: Problem Understanding & Requirements (5-10 minutes)
**Objective:** Fully comprehend what is being asked and what success looks like.

**Actions:**
1. **Parse the Request:**
   - Identify the core scientific question or hypothesis
   - Extract specific predictions, gates, or falsification criteria
   - Note any pre-specified thresholds or comparison baselines
   - Clarify domain context (physics, biology, economics, etc.)

2. **Requirements Gathering:**
   - What data sources are needed? (files, APIs, databases)
   - What output metrics/statistics are required?
   - What visualizations would illuminate the findings?
   - What validation checks would confirm correctness?
   - Are there timing constraints or computational limits?

3. **Success Criteria:**
   - Define what "confidence-inducing" means for THIS analysis
   - Specify statistical tests that must pass
   - Identify potential failure modes to check
   - Establish falsification boundaries

**Deliverable:** Clear written summary of:
- The scientific question
- Required data and methods
- Success/failure criteria
- Expected outputs

---

### Stage 2: Research & Documentation (10-15 minutes)
**Objective:** Gather domain knowledge, prior work, and technical documentation.

**Actions:**
1. **Literature & Context Search:**
   - Search web for relevant papers, methodologies, and domain knowledge
   - Look for standard analysis approaches in this domain
   - Identify common pitfalls and validation strategies
   - Check for existing libraries/tools for this analysis type

2. **Internal Knowledge Search:**
   - Search user's Google Drive for related prior analyses
   - Look for similar datasets or methods previously used
   - Check for domain-specific conventions or preferences

3. **Technical Documentation:**
   - Read docs for any required libraries (numpy, scipy, astropy, etc.)
   - Understand data format specifications
   - Review API documentation for data sources

4. **Method Selection:**
   - Choose appropriate statistical/analytical methods
   - Justify method choices based on data properties
   - Identify alternative approaches for comparison

**Deliverable:** Research summary including:
- Relevant domain context
- Chosen methodology with justification
- Key references or prior work
- Potential issues to watch for

---

### Stage 3: Analysis Implementation (Iterative, 3 Attempts Max)
**Objective:** Write, execute, and validate analysis code with increasing refinement.

#### Attempt Structure (for each of 3 attempts):

**3A. Code Development:**
1. **Write modular, documented code:**
   - Clear function/class structure
   - Docstrings explaining purpose and logic
   - Inline comments for complex operations
   - Type hints where applicable

2. **Include built-in validation:**
   - Sanity checks on intermediate results
   - Assertions for expected data properties
   - Error handling with informative messages
   - Logging of key decision points

3. **Generate synthetic test data (when applicable):**
   - Create known-answer scenarios
   - Test edge cases
   - Verify method doesn't produce false positives/negatives

**3B. Execution:**
1. **Run the analysis:**
   - Execute on actual data
   - Capture all outputs (stdout, stderr, logs)
   - Save intermediate results for inspection
   - Time execution stages

2. **Generate outputs:**
   - At minimum: 1 figure, 1 metadata file, 1 dataset
   - Aim for comprehensive package:
     * Multiple figures showing different aspects
     * Detailed metadata (parameters, timestamps, versions)
     * Processed datasets at key stages
     * Statistical summary tables
     * Log files with execution trace

**3C. Results Review & Critique:**
1. **Compare to expectations:**
   - Do results match predictions/hypotheses?
   - Are magnitudes reasonable for the domain?
   - Do trends make physical/logical sense?
   - Are there unexpected patterns requiring explanation?

2. **Statistical validation:**
   - Check significance levels
   - Verify assumptions are met (normality, independence, etc.)
   - Test for confounds or artifacts
   - Compare to null hypothesis or baseline

3. **Technical validation:**
   - Verify numerical stability (no NaNs, infs, overflow)
   - Check for boundary effects or edge artifacts
   - Confirm units and scales are correct
   - Test reproducibility (same inputs → same outputs)

4. **Critical assessment:**
   - What could be wrong with this result?
   - What alternative explanations exist?
   - What additional tests would increase confidence?
   - Is the uncertainty quantified appropriately?

**3D. Confidence Determination:**

Rate confidence as:
- **HIGH:** Multiple independent validations pass, results are stable and reproducible, alternative explanations ruled out, statistics robust
- **MEDIUM:** Core results solid but some uncertainty in interpretation or edge cases, additional validation would help but not critical
- **LOW:** Results present but significant concerns about validity, artifacts, or methodology; needs revision

**3E. Decision Point:**
- If **HIGH confidence:** Proceed to Stage 4 (packaging)
- If **MEDIUM/LOW confidence:** Document issues and begin next attempt
- After 3 attempts: Proceed to Stage 4 with honest assessment

#### Between Attempts:
- **Document what went wrong:** Specific errors, artifacts, or validity concerns
- **Revise approach:** Change method, fix bugs, add validation steps
- **Learn from failure:** Each attempt should address issues from previous

---

### Stage 4: Package Assembly & Delivery
**Objective:** Create a complete, reproducible analysis package ready for review or publication.

**Package Structure:**
```
analysis_YYYY-MM-DD_HHMMSS/
├── README.md                 # Overview, findings, how to reproduce
├── scripts/
│   ├── main_analysis.py     # Primary analysis script
│   ├── validation.py        # Validation tests
│   └── utilities.py         # Helper functions
├── data/
│   ├── raw/                 # Original input data
│   ├── processed/           # Cleaned/processed datasets
│   └── outputs/             # Result datasets
├── figures/
│   ├── figure_01_*.png      # Numbered, descriptive filenames
│   ├── figure_02_*.png
│   └── ...
├── logs/
│   ├── execution_log.txt    # Complete execution trace
│   ├── validation_log.txt   # Validation check results
│   └── metadata.json        # Structured metadata
└── results/
    ├── summary.txt          # Plain text findings
    ├── statistical_tests.csv # Test results table
    └── interpretation.md    # Detailed interpretation
```

**README.md Contents:**
1. **Executive Summary:**
   - One paragraph: what was analyzed and what was found
   - Key result with confidence assessment
   - Most important figure reference

2. **Analysis Overview:**
   - Scientific question addressed
   - Data sources and preprocessing
   - Methods employed and why
   - Validation strategy

3. **Results Summary:**
   - Main findings with statistics
   - Figures with captions
   - Comparison to predictions/hypotheses
   - Unexpected findings or anomalies

4. **Confidence Assessment:**
   - What validations passed/failed
   - Known limitations or uncertainties
   - Recommendations for follow-up

5. **Reproducibility:**
   - Environment specifications (Python version, key libraries)
   - How to re-run analysis
   - Expected runtime
   - How to interpret outputs

6. **Attempt History (if >1 attempt):**
   - Brief summary of what changed between attempts
   - Why revisions were needed
   - How final version addresses issues

**Metadata File (JSON format):**
```json
{
  "analysis_id": "unique_identifier",
  "timestamp": "ISO-8601 datetime",
  "analyst": "Claude (Anthropic)",
  "user_request": "original request text",
  "domain": "physics/biology/economics/etc",
  "data_sources": ["list", "of", "sources"],
  "methods": ["statistical_tests", "models", "etc"],
  "attempts": {
    "attempt_1": {
      "confidence": "LOW/MEDIUM/HIGH",
      "issues": ["list of problems"],
      "duration_seconds": 123
    },
    "attempt_2": {...},
    "attempt_3": {...}
  },
  "final_confidence": "LOW/MEDIUM/HIGH",
  "key_results": {
    "statistic_name": "value with units",
    "p_value": 0.001,
    "effect_size": "..."
  },
  "validation_checks": {
    "numerical_stability": "PASS",
    "reproducibility": "PASS",
    "statistical_assumptions": "PASS/FAIL with details"
  },
  "software_environment": {
    "python_version": "3.x.x",
    "key_libraries": {"numpy": "1.x.x", "scipy": "1.x.x"}
  }
}
```

**Delivery:**
1. Copy complete package to `/mnt/user-data/outputs/`
2. Use `present_files` tool to share the package directory
3. Provide brief summary highlighting:
   - Main finding (1-2 sentences)
   - Confidence level and why
   - Most important figure to look at first
   - Any critical caveats

---

## Domain-Specific Considerations

### Physics/Astronomy:
- Always include units and verify dimensional consistency
- Check for common artifacts (aliasing, windowing effects, noise)
- Use domain-appropriate statistical tests (chi-square for Poisson data, etc.)
- Include null hypothesis tests when testing predictions
- Visualize both time and frequency domain (when applicable)

### General Scientific:
- Report effect sizes, not just p-values
- Quantify uncertainty (error bars, confidence intervals)
- Test assumptions explicitly
- Consider multiple hypothesis correction if many tests
- Document any data exclusions with justification

### Computational/Simulation:
- Verify convergence
- Test parameter sensitivity
- Compare to analytical limits when available
- Check for numerical artifacts

---

## Quality Standards

### Figures Must Have:
- Descriptive titles
- Labeled axes with units
- Legends when multiple series
- Clear, readable fonts (minimum 10pt)
- Appropriate color schemes (colorblind-friendly when possible)
- Caption in README explaining what to look for

### Code Must Have:
- No hardcoded paths (use relative paths or config)
- Reproducible random seeds when applicable
- Version control friendly (no binary outputs in code)
- Error handling for common failure modes
- Efficient implementation (avoid unnecessary computation)

### Statistical Reporting Must Include:
- Test statistic and distribution
- Degrees of freedom
- P-value or confidence interval
- Effect size
- Sample size
- Any corrections applied

---

## Handling Unexpected Results

**When results are strange/unexpected:**

1. **First: Verify it's real, not artifact:**
   - Check for bugs in code
   - Test on synthetic data with known answer
   - Verify data quality and preprocessing
   - Look for systematic errors

2. **If real: Explain, don't dismiss:**
   - Quantify how unexpected (compare to baseline/null)
   - Propose physical/logical mechanisms
   - Identify what additional data would help
   - Note whether unexpected = falsification or just surprising

3. **Report honestly:**
   - State clearly: "This result is unexpected but validated"
   - Explain why you believe it's real
   - Acknowledge alternative explanations
   - Suggest follow-up investigations

**Remember:** Science advances by surprising results. If validation is thorough, strange results are scientifically valuable.

---

## Failure Modes & Mitigations

### Common Problems:

**Data access failure:**
- Try alternative sources/APIs
- Check if data is in user's Google Drive
- Document clearly if data unavailable
- Provide template code user can run elsewhere

**Method produces nonsensical results:**
- Verify method is appropriate for data type
- Check for assumption violations
- Try simpler baseline method
- Consult literature for domain-standard approaches

**Cannot achieve high confidence after 3 attempts:**
- Report honestly about limitations
- Explain what blocks higher confidence
- Suggest what would be needed to improve
- Deliver package anyway with caveats

**Computational constraints:**
- Downsample data intelligently
- Use approximations with validation
- Parallelize when possible
- Document computational limitations

---

## Example Use Case

**User Request:** "Run a complete analysis testing whether LIGO ringdown shows two-timescale relaxation predicted by VDM."

**Stage 1 Output:**
- Scientific question: Does black hole ringdown exhibit VDM-predicted expand-pinch dynamics?
- Required data: LIGO GW150914 strain data, ringdown window
- Success criteria: Three prediction gates with pre-specified thresholds
- Outputs: Power ratio time series, parameter evolution, spectral analysis

**Stage 2 Output:**
- Method: Wavelet transform for time-frequency, sliding window fits for parameter evolution
- Prior work: Standard ringdown analysis uses Kerr quasi-normal modes
- Tools: gwpy, scipy, matplotlib
- Validation: Test on synthetic Kerr ringdown (should fail VDM predictions)

**Stage 3 - Attempt 1:**
- Code written, executes cleanly
- Results show possible two-timescale pattern
- Critique: Need to verify not artifact of windowing choice
- Confidence: MEDIUM

**Stage 3 - Attempt 2:**
- Added validation: multiple window sizes, bootstrap resampling
- Pattern persists across variations
- Statistical test: two-exponential fit significantly better than one (χ² improvement factor 3.2)
- Confidence: HIGH

**Stage 4 Package:**
```
ligo_vdm_ringdown_analysis_2026-02-14_143022/
├── README.md (3 pages: findings, methods, interpretation)
├── scripts/ (main_analysis.py, validation.py)
├── data/ (GW150914 strain, processed ringdown window)
├── figures/ (power_ratio_timeseries.png, parameter_evolution.png, spectral_analysis.png)
├── logs/ (execution trace, validation results)
├── results/ (statistical_tests.csv, gate_results.txt)
└── metadata.json (complete provenance)
```

**Delivery Summary:** "Analysis complete with HIGH confidence. Two of three VDM prediction gates PASS, one INCONCLUSIVE. Statistical tests robust across validation checks. See figure_02_parameter_evolution.png for clearest signal. No indication this is artifact."

---

## Final Checklist

Before delivering package, verify:
- [ ] All 3 attempts documented (or fewer if early high confidence)
- [ ] At least 1 figure, 1 metadata file, 1 dataset present
- [ ] README explains findings clearly to domain expert
- [ ] Code is reproducible (no hardcoded paths, clear dependencies)
- [ ] Confidence assessment is justified and honest
- [ ] Unexpected results are explained, not dismissed
- [ ] Statistical tests appropriate for data type
- [ ] Units and dimensions verified
- [ ] Package copied to `/mnt/user-data/outputs/`
- [ ] `present_files` called to share with user

---

## Anti-Patterns to Avoid

❌ **Don't:** Run analysis once and call it done
✅ **Do:** Validate thoroughly, iterate if needed

❌ **Don't:** Dismiss strange results as "probably wrong"
✅ **Do:** Investigate whether strange results are artifacts or real

❌ **Don't:** Report p-value alone without context
✅ **Do:** Include effect size, confidence intervals, practical significance

❌ **Don't:** Hide failed attempts or issues
✅ **Do:** Document attempt history transparently

❌ **Don't:** Use complex methods when simple ones suffice
✅ **Do:** Choose simplest adequate method, justify if complex

❌ **Don't:** Assume high confidence without validation
✅ **Do:** Earn confidence through multiple independent checks

---

## Success Metrics

This skill succeeds when:
1. User can reproduce analysis from package alone
2. Confidence assessment matches reality (no false confidence)
3. Findings are clear even if unexpected
4. Package could be included in publication supplementary materials
5. Any domain expert could review and understand methods
6. Failure modes are documented and explained
7. User trusts the rigor even when results surprise them
