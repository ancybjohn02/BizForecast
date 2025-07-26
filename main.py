import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from utils.signal_eval import evaluate_signals

# Import indicator functions
from indicators.rsi import calculate_rsi
from indicators.macd import add_macd
from indicators.obv import calculate_obv
from indicators.bollinger_bands import add_bollinger_bands
from indicators.moving_averages import add_moving_averages

st.set_page_config("📊 BizForecast", layout="wide")
st.title("Advanced Technical Analysis of Emerging Market Leaders")


# --- Sidebar ---
st.sidebar.header("Settings")

companies = ['ASML', 'BR', 'DXCM', 'FICO', 'FTNT', 'SPGI']
company = st.sidebar.selectbox("Select Company", companies)

indicator_choices = st.sidebar.multiselect(
    "Select Indicators",
    ["RSI", "MACD", "OBV", "Bollinger Bands", "Moving Averages"]
)

# --- Load Data ---
data_path = f"data/indicator_data/{company.lower()}.csv"
df = pd.read_csv(data_path, parse_dates=True, index_col=0)

# --- Apply Indicators ---
if "RSI" in indicator_choices:
    df = calculate_rsi(df)

if "MACD" in indicator_choices:
    df = add_macd(df)

if "OBV" in indicator_choices:
    df = calculate_obv(df)

if "Bollinger Bands" in indicator_choices:
    df = add_bollinger_bands(df)

if "Moving Averages" in indicator_choices:
    df = add_moving_averages(df)

# --- Main Chart ---
st.subheader(f"{company} - Close Price & Indicators")
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Close'], label='Close Price', color='blue')

if "Bollinger Bands" in indicator_choices:
    ax.plot(df['BBU_20_2.0'], label='Upper Band', linestyle='--', color='gray')
    ax.plot(df['BBL_20_2.0'], label='Lower Band', linestyle='--', color='gray')

if "Moving Averages" in indicator_choices:
    if 'SMA_20' in df.columns:
        ax.plot(df['SMA_20'], label='SMA 20', color='orange')
    if 'EMA_12' in df.columns:
        ax.plot(df['EMA_12'], label='EMA 12', color='green')

ax.set_title(f"{company} Stock Price")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

# --- Secondary Charts ---
if "RSI" in indicator_choices:
    st.subheader("RSI (Relative Strength Index)")
    st.line_chart(df['RSI'])

if "MACD" in indicator_choices:
    st.subheader("MACD & Signal")
    st.line_chart(df[['MACD_12_26_9', 'MACDs_12_26_9']])

if "OBV" in indicator_choices:
    st.subheader("OBV (On-Balance Volume)")
    st.line_chart(df['OBV'])

# --- Simple Insight Section ---
st.markdown("### Strategy Evaluation")
signal_strength, signal_msg = evaluate_signals(df)
st.write(signal_msg)

indicator_info = {
    "RSI": {
        "short": "Shows if a stock is overbought or oversold.",
        "long": """**Relative Strength Index (RSI)**  
RSI is a momentum oscillator that ranges from 0 to 100.  
- Above 70: Overbought → stock may pull back.  
- Below 30: Oversold → potential buying opportunity.  
It helps identify reversal points or confirm trends."""
    },
    "MACD": {
        "short": "Tracks trend direction using EMAs.",
        "long": """**MACD (Moving Average Convergence Divergence)**  
MACD shows the relationship between two exponential moving averages (EMAs).  
- Line crossovers → trend shifts.  
- Histogram → momentum strength.  
Useful for spotting trend reversals and entry/exit points."""
    },
    "MA": {
        "short": "Smooths prices to show the trend.",
        "long": """**Moving Averages (MA)**  
MAs reduce noise by averaging price data over time.  
- Simple MA (SMA) = average of last N days.  
- Exponential MA (EMA) = recent prices weighted more.  
Used to identify direction and support/resistance zones."""
    },
    "Bollinger Bands": {
        "short": "Shows volatility using price bands.",
        "long": """**Bollinger Bands**  
Bollinger Bands consist of a middle moving average and two outer bands at ±2 std deviations.  
- Wide bands → high volatility.  
- Narrow bands → low volatility.  
Price touching bands can signal reversal or continuation."""
    },
    "OBV": {
        "short": "Uses volume to confirm price trends.",
        "long": """**On-Balance Volume (OBV)**  
OBV adds/subtracts volume based on price movements.  
- Rising OBV → buying pressure.  
- Falling OBV → selling pressure.  
Helps validate breakouts or trend strength."""
    }
}

with st.container():
    st.markdown("### Indicator Glossary")

    cols = st.columns(3)  # Adjust number of columns to fit screen

    for idx, (name, info) in enumerate(indicator_info.items()):
        with cols[idx % 3]:  # Rotate through columns
            st.markdown(
                f'<span class="indicator-tooltip" title="{info["short"]}">📌 <b>{name}</b></span>',
                unsafe_allow_html=True
            )
            with st.expander("Explain"):
                st.markdown(info["long"])