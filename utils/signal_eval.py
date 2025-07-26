def evaluate_signals(df):
    latest = df.iloc[-1]
    rsi = latest.get("RSI")
    macd = latest.get("MACD_12_26_9")
    signal = latest.get("MACDs_12_26_9")
    close = latest.get("Close")
    ma20 = latest.get("SMA_20")  # or "EMA_20" if you're using exponential

    # Conditions
    rsi_signal = (
        "oversold" if rsi < 30 else
        "overbought" if rsi > 70 else
        "neutral"
    )

    macd_crossover = "bullish" if macd > signal else "bearish"
    above_ma = close > ma20

    # Final signal logic
    if rsi_signal == "oversold" and macd_crossover == "bullish" and above_ma:
        msg = (
            f"**RSI: {rsi:.2f} → Oversold**, "
            f"**MACD Crossover: Bullish**, "
            f"**Price above 20-day MA → Trend reversal likely**\n\n"
            f"✅ **Buy Signal Strength: High**"
        )
        return "strong_buy", msg

    elif rsi_signal == "overbought" and macd_crossover == "bearish" and not above_ma:
        msg = (
            f"**RSI: {rsi:.2f} → Overbought**, "
            f"**MACD Crossover: Bearish**, "
            f"**Price below 20-day MA → Possible drop**\n\n"
            f"🚨 **Sell Signal Strength: High**"
        )
        return "strong_sell", msg

    elif rsi_signal == "oversold" and macd_crossover == "bearish":
        msg = (
            f"**RSI: {rsi:.2f} → Oversold**, but **MACD shows bearish momentum**.\n\n"
            f"⚠️ **Mixed Signal → Hold. Wait for confirmation.**"
        )
        return "hold", msg

    elif rsi_signal == "overbought" and macd_crossover == "bullish":
        msg = (
            f"**RSI: {rsi:.2f} → Overbought**, but **MACD remains bullish**.\n\n"
            f"⚠️ **Momentum continuing → Partial profit booking may be wise.**"
        )
        return "watch", msg

    else:
        msg = (
            f"**RSI: {rsi:.2f} → Neutral**, "
            f"**MACD: {macd:.2f} vs Signal: {signal:.2f}**, "
            f"**Price {'above' if above_ma else 'below'} 20-day MA**\n\n"
            f"ℹ️ **No strong signal. Monitor closely.**"
        )
        return "neutral", msg
