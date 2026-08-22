Act as a Senior Expo + Supabase Architect.

Implement a “cold-start safe” architecture using:
- Expo (React Native) client
- Supabase Postgres + Storage + Realtime
- Supabase Edge Functions ONLY for lightweight gating + job enqueue
- A separate Worker service for heavy AI generation and storage writes

Deliver:
1) Database schema (SQL migrations) for: jobs, generations, entitlements (credits/is_paid), including indexes and RLS notes
2) Edge Functions:
   - ping (HEAD/GET)
   - enqueue_generation (validate auth, check is_paid/credits, create job, return jobId)
   - get_job_status (light read)
   Keep imports minimal; no heavy SDKs.
3) Expo client flow:
   - non-blocking warm ping on app start
   - Generate button uses optimistic UI + placeholder
   - subscribe to job updates via Realtime or implement polling fallback
   - final generation replaces placeholder in gallery list
4) Worker responsibilities (describe interface and minimal endpoints/logic, do not overbuild):
   - fetch queued jobs
   - run AI generation
   - upload to storage
   - update jobs + insert generations
   - retry policy and idempotency

Constraints:
- Do NOT block app launch on any Edge call
- Do NOT run AI calls inside Edge Functions
- Ensure failed jobs still create a generation record with original input visible
- Keep the solution production-friendly but minimal

Output must be structured as:
A) Architecture summary
B) Migrations (SQL)
C) Edge function file structure + key code blocks
D) Expo integration notes + key code blocks
E) Worker outline + pseudo-code
