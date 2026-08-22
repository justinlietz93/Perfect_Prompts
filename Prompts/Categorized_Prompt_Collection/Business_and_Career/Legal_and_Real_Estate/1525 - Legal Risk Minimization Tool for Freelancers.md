Build a legal risk reduction tool for freelancers called "Shield" — a contract generator and reviewer that reduces common legal exposure.

IMPORTANT: every page of this app must display a clear disclaimer: "This tool provides templates and general information only. It is not legal advice. Review all documents with a qualified attorney before use."

Core features:
- Contract generator: user inputs project type (web development / copywriting / design / consulting / photography / other), client type (individual / small business / enterprise), payment terms (fixed / milestone / retainer), approximate project value, and 3 custom deliverables in plain language. [LLM API] generates a complete contract covering scope, IP ownership, payment schedule, revision policy, late payment penalties, confidentiality, and termination — formatted as a clean DOCX
- Contract reviewer: user pastes an incoming contract. AI highlights the 5 most important clauses (ranked by risk), flags anything unusual or asymmetric, and for each flagged clause suggests a specific alternative wording
- Risk radar: user describes their freelance business in 3 sentences — AI identifies their top 5 legal exposure areas with a one-paragraph explanation of each risk and a mitigation step
- Template library: 10 pre-built contract types, all downloadable as DOCX and editable in any word processor
- NDA generator: inputs both party names, confidentiality scope, and duration — generates a mutual NDA in under 30 seconds

Stack: React, [LLM API] for generation and review, docx-js for DOCX export. Professional, trustworthy design — this handles serious matters.
