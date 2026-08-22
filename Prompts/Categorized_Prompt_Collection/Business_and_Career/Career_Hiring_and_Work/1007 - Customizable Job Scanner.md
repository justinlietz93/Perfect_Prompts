# Customizable Job Scanner - AI Optimized
**Author:** Scott M  
**Version:** 2.0  
**Goal:** Surface 80%+ matching [job sector] roles posted within the specified window (default: last 14 days), using real-time web searches across major job boards and company career sites.  
**Audience:** Job boards (LinkedIn, Indeed, etc.), company career pages  
**Supported AI:** Claude, ChatGPT, Perplexity, Grok, etc.

## Changelog
- **Version 1.0 (Initial Release):**  
  Converted original cybersecurity-specific prompt to a generic template. Added placeholders for sector, skills, companies, etc. Removed Dropbox file fetch.
- **Version 1.1:**  
  Added "How to Update and Customize Effectively" section with tips for maintenance. Introduced Changelog section for tracking changes. Added Version field in header.
- **Version 1.2:**  
  Moved Changelog and How to Update sections to top for easier visibility/maintenance. Minor header cleanup.
- **Version 1.3:**  
  Added "Job Types" subsection to filter full-time/part-time/internship. Expanded "Location" to include onsite/hybrid/remote options, home location, radius, and relocation preferences. Updated tips to cover these new customizations.
- **Version 1.4:**  
  Added "Posting Window" parameter for flexible search recency (e.g., last 7/14/30 days). Updated goal header and tips to reference it.
- **Version 1.5:**  
  Added "Posted Date" column to the output table for better recency visibility. Updated Output format and tips accordingly.
- **Version 1.6:**  
  Added optional "Minimum Salary Threshold" filter to exclude lower-paid roles where salary is listed. Updated Output format notes and tips for salary handling.
- **Version 1.7:**  
  Renamed prompt title to "Customizable Job Scanner" for broader/generic appeal. No other functional changes.
- **Version 1.8:**  
  Added optional "Resume Auto-Extract Mode" at top for lazy/fast setup. AI extracts skills/experience from provided resume text. Updated tips on usage.
- **Version 1.9 (Previous stable release):**  
  - Added optional "If no matches, suggest adjustments" instruction at end.  
  - Added "Common Tags in Sector" fallback list for thin extraction.  
  - Made output table optionally sortable by Posted Date descending.  
  - In Resume Auto-Extract Mode: AI must report extracted key facts and any added tags before showing results.
- **Version 2.0 (Current revised version):**  
  - Added explicit real-time search instruction ("Act as a real-time job aggregator... use current web browsing/search capabilities") to prevent hallucinated or outdated job listings.  
  - Enhanced scoring system: added bonuses for verbatim/near-exact ATS keyword matches, quantifiable alignment, and very recent postings (<7 days).  
  - Expanded "Additional sources" to include Google Jobs, FlexJobs (remote), BuiltIn, AngelList, We Work Remotely, Remote.co.  
  - Improved output table: added columns for Location Type, ATS Keyword Overlap, and brief "Why Strong Match?" rationale (for 85%+ matches).  
  - Top Matches (90%+) section now uses bolded/highlighted rows for better visual distinction.  
  - Expanded no-matches suggestions with more actionable escalations (e.g., include adjacent titles, temporarily allow contract roles, remove salary filter).  
  - Minor wording cleanups for clarity, flow, and consistency across sections.  
  - Strengthened Top Instruction block to enforce live searches and proper sequencing (extract first → then search).

## Top Instruction (Place this at the very beginning when you run the prompt)
"Act as my dedicated real-time job scout with current web browsing and search access.  
First: [If using Resume Auto-Extract Mode: extract and summarize my skills, experience, achievements, and technical stack from the pasted resume text. Report the extraction summary including confidence levels (Expert/Strong/Inferred) before showing any job results.]  
Then: Perform live, current searches only (no internal/training data or outdated knowledge). Pull the freshest postings matching my parameters below. Use the scoring system strictly. Prioritize ATS keyword alignment, recency, and my custom tags/skills."

## Resume Auto-Extract Mode (Optional - For Lazy/Fast Setup)
If skipping manual Skills Reference:  
- Paste your full resume text here:  
  [PASTE RESUME TEXT HERE]  
- Keep the Top Instruction above with the extraction part enabled.  
The AI will output something like:  
"Resume Extraction Summary:  
- Experience: 12+ years in cybersecurity / DevOps / [sector]  
- Key achievements: Led X migration (Y endpoints), reduced Z by A%  
- Top skills (with confidence): CrowdStrike (Expert), Terraform (Strong), Python (Expert), ...  
- Suggested tags added: SIEM, KQL, Kubernetes, CI/CD  
Proceeding with search using these."

## How to Update and Customize Effectively
- Use Resume Auto-Extract when short on time; verify the summary before trusting results.  
- Refresh Skills Reference / tags every 3–6 months or after major projects.  
- Use exact phrases from job postings / your resume in tags for ATS alignment.  
- Test across AIs; if too few results → lower threshold, extend window, add adjacent titles/tags.  
- For new sectors: research top keywords via LinkedIn/Indeed/Google Jobs first.

## Skills Reference
(Replace manually or let AI auto-populate from resume)  
**Professional Overview**  
- [Years of experience, key roles/companies]  
- [Major projects/achievements with numbers]  

**Top Skills**  
- [Skill] (Expert/Strong): [tools/technologies]  
- ...  

**Technical Stack**  
- [Category]: [tools/examples]  
- ...

## Common Tags in Sector (Fallback)
If extraction is thin, add relevant ones here (1 point unless core). Examples:  
- Cybersecurity: Splunk, SIEM, KQL, Sentinel, CrowdStrike, Zero Trust, Threat Hunting, Vulnerability Management, ISO 27001, PCI DSS, AWS Security, Azure Sentinel  
- DevOps/Cloud: Kubernetes, Docker, Terraform, CI/CD, Jenkins, Git, AWS, Azure, Ansible, Prometheus  
- Software Engineering: Python, Java, JavaScript, React, Node.js, SQL, REST API, Agile, Microservices  
[Add your sector’s common tags when switching]

## Job Search Parameters
Search for [job sector e.g. Cybersecurity Engineer, Senior DevOps Engineer] jobs posted in the last [Posting Window].

### Posting Window
[last 14 days] (default) / last 7 days / last 30 days / since YYYY-MM-DD

### Minimum Salary Threshold
[e.g. $130,000 or $120K — only filters jobs where salary is explicitly listed; set N/A to disable]

### Priority Companies (check career pages directly if few results)
- [Company 1] ([career page URL])  
- [Company 2] ([career page URL])  
- ...

### Additional Sources
LinkedIn, Indeed, Google Jobs, Glassdoor, ZipRecruiter, Dice, FlexJobs (remote), BuiltIn, AngelList, We Work Remotely, Remote.co, company career sites

### Job Types
Must include: full-time, permanent  
Exclude: part-time, internship, contract, temp, consulting, C2H, contractor

### Location
Must match one of:  
- 100% remote  
- Hybrid (partial remote)  
- Onsite only if within [50 miles] of East Hartford, CT (includes Hartford, Manchester, Glastonbury, etc.)  
Open to relocation: [Yes/No; if Yes → anywhere in US / Northeast only / etc.]

### Role Types to Include
[e.g. Security Engineer, Senior Security Engineer, Cybersecurity Analyst, InfoSec Engineer, Cloud Security Engineer]

### Exclude Titles With
manager, director, head of, principal, lead (unless explicitly wanted)

## Scoring System
Match job descriptions against my tags from Skills Reference + Common Tags:  
- Core/high-value tags: 2 points each  
- Standard tags: 1 point each  
Bonuses:  
+1–2 pts for verbatim / near-exact keyword matches (strong ATS signal)  
+1 pt for quantifiable alignment (e.g. “manage large environments” vs my “120K endpoints”)  
+1 pt for very recent posting (<7 days)  

Match % = (total matched points / max possible points) × 100  
Show only jobs ≥80%

## Output Format
Table:  
| Job Title | Match % | Company | Posted Date | Location Type | Salary | ATS Overlap | URL | Why Strong Match? |

- **Posted Date:** Exact if available (YYYY-MM-DD or "Posted Jan 10, 2026"); otherwise "Approx. X days ago" or N/A  
- **Salary:** Only if explicitly listed; N/A otherwise (no estimates)  
- **Location Type:** Remote / Hybrid / Onsite  
- **ATS Overlap:** e.g. "9/14 top tags matched" or "Strong keyword overlap"  
- **Why Strong Match?:** 2–3 bullet highlights (only for 85%+ matches)  

Sort table by Posted Date descending (most recent first), then Match % descending.  
Remove duplicates (same title + company).  

Put 90%+ matches in a separate section at top called **Top Matches (90%+)** with bolded rows or clear highlighting.

If no strong matches:  
"No strong matches found in the current window."  
Then suggest adjustments:  
- Extend Posting Window to 30 days?  
- Lower threshold to 75%?  
- Add common sector tags (e.g. Splunk, Kubernetes, Python)?  
- Broaden location / include more hybrid options?  
- Include adjacent role titles (e.g. Cloud Engineer, Systems Engineer)?  
- Temporarily allow contract roles?  
- Remove/lower Minimum Salary Threshold?  
- Manually check priority company career pages for unindexed postings?
