Build a paper trading simulation platform called "Paper" — a realistic, risk-free environment for learning to trade and invest.

Core features:
- Portfolio setup: user starts with $100,000 in virtual cash. Real-time stock and ETF prices via Yahoo Finance or Alpha Vantage API
- Trade execution: market and limit orders supported. Simulate 0.1% slippage on market orders. Commission of $1 per trade (realistic friction without being punitive)
- Performance dashboard: P&L chart (daily), total return, annualized return, win rate, average gain and loss, Sharpe ratio, and current sector exposure — all updated with each trade. Built with recharts
- Trade journal: required field on every position close — "What was my thesis entering this trade? What happened? What will I do differently?" Three fields, each max 200 characters. Cannot close a position without completing the journal
- Behavioral analysis: [LLM API] analyzes the last 20 trade journal entries and identifies recurring behavioral patterns — "You consistently exit winning positions early when they approach round-number price levels" — surfaced monthly
- Leaderboard: optional, weekly-resetting leaderboard among friend groups — ranked by risk-adjusted return, not raw P&L

Stack: React, Yahoo Finance or Alpha Vantage for market data, [LLM API] for behavioral analysis, recharts. Terminal-inspired design — data dense, no decorative elements.
