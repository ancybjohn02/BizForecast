import pandas_ta as ta
import pandas as pd

def add_moving_averages(df: pd.DataFrame, sma_lengths=[20, 50], ema_lengths=[12, 26]) -> pd.DataFrame:
    """
    Adds Simple and Exponential Moving Averages to the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input dataframe with at least a 'Close' column.
    - sma_lengths (list): List of window sizes for Simple Moving Averages.
    - ema_lengths (list): List of window sizes for Exponential Moving Averages.

    Returns:
    - pd.DataFrame: DataFrame with SMA and EMA columns added.
    """
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column for moving averages.")

    for length in sma_lengths:
        df[f"SMA_{length}"] = ta.sma(df['Close'], length=length)
    for length in ema_lengths:
        df[f"EMA_{length}"] = ta.ema(df['Close'], length=length)
    
    return df
