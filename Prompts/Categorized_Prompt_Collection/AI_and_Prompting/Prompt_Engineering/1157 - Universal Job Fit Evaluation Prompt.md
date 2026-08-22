# Universal Job Fit Evaluation Prompt – Fully Generic & Shareable
# Author: Scott M
# Version: 1.6
# Last Modified: 2026-03-06

## Changelog
- **v1.6 (2026-03-06):** Integrated "Read Between the Lines" (Vibe Check), ATS Keyword Translation, and Interview Prep "Gotchas."
- **v1.5 (2026-03-04):** Added "User Action Advice" for blocked URLs. Restored visible author headers.
- **v1.4 (2026-02-17):** Refined scoring weights and portfolio alignment instructions.
- **v1.3 (2026-02-04):** Added Anchor Skill list and confidence levels.

## Goal
Help a candidate objectively evaluate how well a job posting matches their skills, experience, and portfolio, while producing actionable guidance for applications, portfolio alignment, and skill gap mitigation.

---

## Pre-Evaluation Checklist (User: please provide these)
- [ ] Step 0: Candidate Priorities (Remote? Salary? Tech stack?)
- [ ] Step 1: Skills & Experience (Markdown link or pasted text)
- [ ] Step 1a: Key Skills Anchor List (What matters most right now?)
- [ ] Step 2: Portfolio links/descriptions
- [ ] Job Posting: URL or full text

---

## Step 0: Candidate Priorities
- Roles/Domains:
- Location preference (remote / hybrid / city / region):
- Compensation expectations or constraints:
- Non-negotiables (e.g., on-call, travel, clearance, tech stack):
- Nice-to-haves:

---

## Step 1 & 1a: Skills, Experience, & Focus Areas
---

## Step 2: Portfolio / Work Samples
---

## URL Access & Fallback Protocol

**If a provided URL is broken, empty, or blocked by a paywall/login:**
1. **Internal Search:** Attempt to find the job details via LinkedIn, Indeed, or the company’s career page.
2. **Warn:** If data is still missing, display: "⚠️ Inaccessible Source: I cannot read the data at the provided URL."
3. **User Action Advice:** If I cannot access the posting, please try the following:
   - **Direct Paste:** Copy the full job description text from your browser and paste it here.
   - **File Upload:** Save the webpage as a PDF or take a screenshot and upload the file.
   - **Print to PDF:** Use "Print to PDF" in your browser to generate a clean document of the JD.

---

## Task: Job Fit Evaluation

Analyze the **Job Posting** against the **Candidate Info** provided above.

### Scoring Instructions
For each section, assign a percentage match. Use semantic alignment, not just keyword matching.

**Default Weighting:**
- Responsibilities: 30%
- Required Qualifications: 30%
- Skills / Technologies / Edu: 25%
- Preferred Qualifications: 15%

### Specific Analysis Requirements
1. **Read Between the Lines:** Identify "hidden" requirements or red flags (e.g., signs of burnout culture, vague scope, or unstated seniority).
2. **ATS Translation:** List 5-10 specific keywords from the JD that are missing from the candidate's markdown but represent experience they likely have.
3. **Interview Prep "Gotchas":** Identify the 3 toughest questions a recruiter will likely ask based on the candidate's specific gaps or "weakest" match areas.

---

## Output Requirements
- **Overall Fit Percentage** (Weighted average)
- **Confidence Level** (High/Medium/Low based on info completeness)
- **Vibe Check:** Summary of the "Read Between the Lines" analysis.
- **Top 3 Alignments:** Specific areas where the candidate is a perfect match.
- **Top 3 Gaps:** Missing skills or experience with advice on how to mitigate them.
- **Portfolio-Specific Guidance:** Connect a specific job requirement to a concrete portfolio action.
- **Additional Commentary:** Flag location, salary, or culture mismatches.

---

### Final Summary Table (Use This Exact Format)

| Section | Match % | Key Alignments & Gaps | Confidence |
| :--- | :--- | :--- | :--- |
| Responsibilities | XX% | | |
| Required Qualifications | XX% | | |
| Preferred Qualifications | XX% | | |
| Skills / Technologies / Edu | XX% | | |
| **Overall Fit** | **XX%** | | **High/Med/Low** |

---

## Job Posting Source
