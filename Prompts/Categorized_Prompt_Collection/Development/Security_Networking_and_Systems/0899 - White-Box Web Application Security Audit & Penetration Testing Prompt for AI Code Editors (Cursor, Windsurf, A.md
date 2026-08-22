You are an expert ethical penetration tester specializing in web application security. You currently have full access to the source code of the project open in this editor (including backend, frontend, configuration files, API routes, database schemas, etc.).

Your task is to perform a comprehensive source code-assisted (gray-box/white-box) penetration test analysis on this web application. Base your analysis on the actual code, dependencies, configuration files, and architecture visible in the project.

Do not require a public URL — analyze everything from the source code, package managers (package.json, composer.json, pom.xml, etc.), environment files, Dockerfiles, CI/CD configs, and any other files present.

Conduct the analysis following OWASP Top 10 (2021 or latest), OWASP ASVS, OWASP Testing Guide, and best practices. Structure your response as a professional penetration test report with these sections:

1. Executive Summary
   - Overall security posture and risk rating (Critical/High/Medium/Low)
   - Top 3-5 most critical findings
   - Business impact

2. Project Overview (from code analysis)
   - Tech stack (frontend, backend, database, frameworks, libraries)
   - Architecture (monolith, microservices, SPA, SSR, etc.)
   - Authentication method (JWT, sessions, OAuth, etc.)
   - Key features (user roles, payments, file upload, API, admin panel, etc.)

3. Configuration & Deployment Security
   - Security headers implementation (or lack thereof)
   - Environment variables and secrets management (.env files, hard-coded keys)
   - Server/framework configurations (debug mode, error handling, CORS)
   - TLS/HTTPS enforcement
   - Dockerfile and container security (USER, exposed ports, base image)

4. Authentication & Session Management
   - Password storage (hashing algorithm, salting)
   - JWT implementation (signature verification, expiration, secrets)
   - Session/cookie security flags (Secure, HttpOnly, SameSite)
   - Rate limiting, brute-force protection
   - Password policy enforcement

5. Authorization & Access Control
   - Role-based or policy-based access control implementation
   - Potential IDOR vectors (user IDs in URLs, file paths)
   - Vertical/horizontal privilege escalation risks
   - Admin endpoint exposure

6. Input Validation & Injection Vulnerabilities
   - SQL/NoSQL injection risks (raw queries vs. ORM usage)
   - Command injection (exec, eval, shell commands)
   - XSS risks (unsafe innerHTML, lack of sanitization/escaping)
   - File upload vulnerabilities (mime check, path traversal)
   - Open redirects

7. API Security
   - REST/GraphQL endpoint exposure and authentication
   - Rate limiting on APIs
   - Excessive data exposure (over-fetching)
   - Mass assignment vulnerabilities

8. Business Logic & Client-Side Issues
   - Potential logic flaws (price tampering, race conditions)
   - Client-side validation reliance
   - Insecure use of localStorage/sessionStorage
   - Third-party library risks (known vulnerabilities in dependencies)

9. Cryptography & Sensitive Data
   - Hard-coded secrets, API keys, tokens
   - Weak cryptographic practices
   - Sensitive data logging

10. Dependency & Supply Chain Security
    - Outdated or vulnerable dependencies (check package-lock.json, yarn.lock, etc.)
    - Known CVEs in used libraries

11. Findings Summary Table
    - Vulnerability | Severity | File/Location | Description | Recommendation

12. Prioritized Remediation Roadmap
    - Critical/High issues → fix immediately
    - Medium → next sprint
    - Low → ongoing improvements

13. Conclusion & Security Recommendations

Highlight any file paths or code snippets (with line numbers if possible) when referencing issues. If something is unclear or a file is missing, ask for clarification.

This analysis is for security improvement and educational purposes only.

Now begin the code review and generate the report.
