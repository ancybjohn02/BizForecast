import pandas as pd

def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:

    if df is None or df.empty:
        raise ValueError("Input DataFrame is empty.")
    if 'Close' not in df.columns:
        raise KeyError("Missing 'Close' column in DataFrame.")
    
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    df['RSI'] = rsi
    return df