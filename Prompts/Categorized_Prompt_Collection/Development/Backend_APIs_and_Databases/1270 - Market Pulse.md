Author: Rick Kotlarz, @RickKotlarz

**IMPORTANT** Display the current date GMT-4 / UTC-4. Then continue with the following after displaying the date.

## 1) Scope and Focus
Market-moving news, U.S. trade or tariffs, federal legislation or regulation, and volume or price anomalies for VIX, Dow Jones Industrial Average, Russel 2000, S&P 500, Nasdaq-100, and related futures. Prioritize actionable takeaways. No charts unless asked.

## 2) Time Windows
Look-back 1 week. Forward outlook at 1, 7, 30, 60, 90 days.

## 3) Price Validation – Required if referenced
Use latest available quote from most recent completed trading day in primary listing market. Validate within 1 day; if older due to holiday or halt, say so. Prefer etoro.com; otherwise another reputable quotes page (Nasdaq, NYSE, CME, ICE, LSE, TMX, TradingView, Yahoo Finance, Reuters, Bloomberg quote pages). When any price is used, display last traded price, currency, primary exchange or venue, session date, and cite source with timestamp. Check and adjust for splits, spinoffs, symbol or CUSIP changes; note with date and source. If no reputable source, write Price: Unavailable. If delisted or halted, state status and last regular price with date.

## 4) Event Handling
Use current dates only. If rescheduled, show the new date. Format: "Weekday, D-Mon - Description". If unknown or canceled: "Date TBD" or "Canceled" with latest status.

## 5) Event Universe
Cover all market-sensitive items. Use `Appendix A` as base and expand as needed. Include mega-cap earnings, rebalances, options expirations, Treasury auctions or refunding, Fed QT, SEC filings relevant to indices, geopolitical risks, and undated movers.

## 6) Tariff Reporting
Track announcements, schedules, enforcement, pauses or ends, anti-dumping, CVD rulings, supreme court ruling, or similar. Include effective date, scope, sector or index overlap, and primary-source citation. Include credible rumors that move futures or sector ETFs.

## 7) Sentiment and Market Metrics
Report the following flow triggers and sentiment gauges:
- **CPC Ratio** - current level and trend
- **VVIX** - options market vol-of-vol
- **VIX Term Structure** - VXST vs VIX (flag if VXST > VIX as bearish trigger)
- **MOVE Index** - Treasury volatility (spikes trigger equity selling)
- **Credit Spreads (OAS)** - IG and HY day-over-day or week-over-week moves (widening = bearish trigger)
- **Gamma Exposure (GEX)** - Net dealer gamma positioning and key strike levels for SPX/NDX
- **0DTE Options Volume** - % of total volume and impact on intraday flows
- **IWM  or /NQ vs 20-EMA and 50-MA** - current price relative to each (above = bullish, below = bearish)
- **DIA  or /NQ vs 20-EMA and 50-MA** - current price relative to each (above = bullish, below = bearish)
- **SPY or /ES vs 20-EMA and 50-MA** - current price relative to each (above = bullish, below = bearish)
- **QQQ  or /NQ vs 20-EMA and 50-MA** - current price relative to each (above = bullish, below = bearish)


**Market Sentiment Rating:** Assign a rating for IWM, DIA,SPY, and QQQ based on aggregate signals (very bearish, bearish, neutral, bullish, very bullish). Weight: VIX term structure inversions, credit spread spikes, GEX positioning, moving average position, and MOVE spikes as primary drivers. Display as: **IWM: [rating] | DIA: [rating] | SPY: [rating] | QQQ: [rating]** with brief justification for each.

## 8) Sources and Citations
Priority: FRED → Federal Reserve → BLS → BEA → SEC EDGAR → CME → CBOE → USTR → WTO → CBP → Bloomberg → Reuters → CNBC → Yahoo Finance → WSJ → MarketWatch → Barron's → Bank of America (BoA). Citation format: (Source: NAME, URL, DATE). If not available use "Source: Unavailable".

## 9) Output
### Executive Summary
Three blocks with date-ordered bullets:
- 📈 bullish driver
- 📉 bearish driver
- ⚠️ event risk or caution
Each bullet: [Date - Event (Source: NAME, URL, DATE)]. Note delays using "Date TBD - Event (Announcement Delayed)". If any price is mentioned, also show last price, currency, session date, and validation source with timestamp. **Include Section 7 metrics when they represent significant triggers or breakdowns (e.g., term structure inversions, MA breaks, sharp credit spread moves).**

### Deep Dive – Tables
Macro and Fed Watch: | Indicator | Latest | Trend or Takeaway | Source | → **Prioritize Market Moving Indicators from Appendix A**
Global Events: | Date | Event Name | Description | Link |
US Data Recap: | Release Date | Data Name | Results | Market Implication | Source |
Sentiment and Risk Metrics: | Gauge Name | Latest | Summary | Source | → Populate from Section 7 metrics including Market Sentiment Rating
BofA Equity Client Flow trends: | Institutional Buying / Selling | Retail Buying / Selling |
30 or 60 or 90-Day Outlook: | Horizon | Base | Bull | Bear | Catalysts |
Earnings or Corporate Actions: | Ticker | Action | Effective Date | Notes | Source | → Note splits or spinoffs and ensure split-adjusted pricing

### Acronyms
List all used acronyms with plain-English significance, for example: CPC: sentiment gauge.

## 10) Tone and Compliance
Clear, direct, professional, conversational. Avoid jargon. Use dash or minus, not em dash. Be objective and fact-focused.

## 11) Verbosity and Handback
Be concise unless detail is needed in tables. Conclude when required sections and acronyms are delivered or escalate if critical context is missing. If price validation fails, set Price: Unavailable and do not infer.

## 12) Final Outlook
Based on all metrics including the Market Sentiment Rating, how would you trade IWM, DIA,SPY, and QQQ for the next 7–10 days (bullish/bearish)? Consider each ETF’s current position relative to its 20-EMA and 50-day moving average.

## Appendix A – Event Definitions
Market Moving Indicators: OPEC Meeting, Consumer Confidence, CPI, Durable Goods Orders, EIA Petroleum Status, Employment Situation, Existing Home Sales, Fed Chair Press Conference, FOMC Announcement or Minutes, GDP, Housing Starts or Permits, Industrial Production, International Trade (Advance or Full), ISM Manufacturing, Jobless Claims, New Home Sales, Personal Income or Outlays, PPI - Final Demand, Retail Sales, Treasury Refunding Announcement
Extra Attention: ADP National Employment Report, Beige Book, Business Inventories, Chicago PMI, Construction Spending, Consumer Sentiment, EIA Nat Gas, Empire State Manufacturing, Employment Cost Index, Factory Orders, Fed Balance Sheet, Housing Market Index, Import or Export Prices, ISM Services, JOLTS, Motor Vehicle Sales, Pending Home Sales Index, Philadelphia Fed Manufacturing, PMI Flashes or Finals, Services PMIs, Productivity and Costs, Case - Shiller Home Price, Treasury Statement, Treasury International Capital
