import streamlit as st
import yfinance as yf
import pandas as pd

# Must include: ticker dropdown, date range slider, checkboxes for indicators

st.title("📈 Basic Stock Dashboard")

ticker = st.text_input("Enter stock ticker", "AAPL")

df = yf.download(ticker, start="2022-01-01")
df['MA30'] = df['Close'].rolling(30).mean()

st.line_chart(df[['Close', 'MA30']])
