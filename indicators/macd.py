import pandas_ta as ta
import pandas as pd

def add_macd(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds MACD line, signal line, and histogram to the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input dataframe with at least a 'Close' column.

    Returns:
    - pd.DataFrame: DataFrame with 'MACD_12_26_9', 'MACDs_12_26_9', and 'MACDh_12_26_9' columns.
    """
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column for MACD.")
    
    macd = ta.macd(df['Close'])
    return df.join(macd)
