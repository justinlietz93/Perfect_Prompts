Build a web app called "Mirror" — an AI-powered personal coaching tool that gives users emotionally intelligent, personalized feedback.

Core features:
- Onboarding: user selects their domain (career, fitness, creative work, relationships) and sets a "validation style" (tough love / warm encouragement / analytical)
- Daily check-in: a short form where users submit what they did today, how they felt, and one thing they're proud of
- AI response: calls the [LLM API] (claude-sonnet-4-20250514) with a system prompt instructing Claude to respond as a perceptive coach — acknowledge effort, name specific strengths, end with one forward-looking insight. Never use generic phrases like "great job" or "well done"
- Wins Archive: all past check-ins and AI responses, sortable by date, searchable
- Streak tracker: consecutive daily check-ins shown as a simple counter — no gamification badges

UI: clean, warm, serif typography, cream (#F5F0E8) background. Should feel like a private journal, not an app. No notifications except a gentle daily reminder at a user-set time.

Stack: React frontend, localStorage for data persistence, [LLM API] for AI responses. Single-page app, no backend required.
