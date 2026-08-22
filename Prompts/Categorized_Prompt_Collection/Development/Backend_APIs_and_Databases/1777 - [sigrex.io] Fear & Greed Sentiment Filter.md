{{val:symbol=BTCUSDT}}
{{val:rsi_ob=68}}
{{val:rsi_os=32}}

Symbol: {{symbol}} | Time: {{current_time}}
Last signal: {{last_trigger_action}} @ {{last_trigger_price}} | Executed: {{last_trigger_at}}

Signal history:
{{trigger_history}}

Current market sentiment data:
{{get:https://api.alternative.me/fng/?limit=1&format=json}}

STRATEGY RULES:
Use the Fear & Greed value fetched above as a sentiment filter:
- Value 0–30 = Extreme Fear → favor LONG setups only
- Value 31–50 = Fear → allow LONG, avoid SHORT
- Value 51–74 = Greed → allow SHORT, be cautious with LONG
- Value 75–100 = Extreme Greed → favor SHORT setups only

LONG when:
  - Sentiment is Extreme Fear or Fear
  - RSI is below {{rsi_os}} and turning up
  - MACD histogram crosses positive
  - No open position

SHORT when:
  - Sentiment is Extreme Greed or Greed
  - RSI is above {{rsi_ob}} and turning down
  - MACD histogram crosses negative
  - No open position

EXIT when:
  - RSI crosses back to neutral (45–55 range)
  - OR sentiment flips against current position direction

HOLD if sentiment and technicals disagree, or no clear signal.
