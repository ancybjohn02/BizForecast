import pandas_ta as ta
import pandas as pd

def add_bollinger_bands(df: pd.DataFrame, length: int = 20, std: int = 2) -> pd.DataFrame:
    """
    Adds Bollinger Bands (upper, middle, lower) to the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input dataframe with at least a 'Close' column.
    - length (int): Number of periods to use for moving average.
    - std (int): Number of standard deviations from the mean.

    Returns:
    - pd.DataFrame: DataFrame with 'BBL', 'BBM', and 'BBU' columns added.
    """
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column for Bollinger Bands.")
    
    bbands = ta.bbands(df['Close'], length=length, std=std)
    return df.join(bbands)
