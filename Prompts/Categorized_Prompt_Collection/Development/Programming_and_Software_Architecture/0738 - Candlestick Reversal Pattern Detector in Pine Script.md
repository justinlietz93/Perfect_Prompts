Act as a TradingView Pine Script v5 developer. You are tasked with creating an indicator that automatically detects and plots candlestick reversal patterns on the price chart. 

Your task is to:
- Identify and label the following candlestick patterns:
  - Bullish: Morning Star, Hammer
  - Bearish: Evening Star, Bearish Engulfing
- For each detected pattern:
  - Plot a green upward arrow below the candle for bullish patterns with the text “BUY: Pattern Name”
  - Plot a red downward arrow above the candle for bearish patterns with the text “SELL: Pattern Name”
- Add optional trend confirmation using a moving average (user-selectable length).
  - Only show bullish signals above the MA and bearish signals below the MA (toggleable).
- Include an optional RSI panel:
  - RSI length input
  - Overbought and oversold levels
  - Allow RSI to be used as an additional filter for signals (on/off)
- Ensure the indicator overlays signals on the price chart and uses clear labels and arrows 
- Allow user inputs to enable/disable each candlestick pattern individually
- Make sure the script is clean, optimized, and fully compatible with TradingView.
