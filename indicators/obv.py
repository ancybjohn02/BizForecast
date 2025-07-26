# OBV - On-balance volume
import pandas as pd
import numpy as np

def calculate_obv(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        raise ValueError("Input DataFrame is empty.")
    if 'Close' not in df.columns or 'Volume' not in df.columns:
        raise KeyError("Missing required columns: 'Close' and/or 'Volume'.")

    direction = np.sign(df['Close'].diff().fillna(0))
    obv = (direction * df['Volume']).fillna(0).cumsum()
    df['OBV'] = obv
    return df

