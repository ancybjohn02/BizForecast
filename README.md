# Advanced Technical Analysis of Emerging Market Leaders

Motivation : beyond the obvious, companies often overlooked in beginner analyses but vital in understanding where the next wave of innovation may surge.

## 📁 Folder Structure 
MVP/
│
├── data/
│   ├── ASML.csv, BR.csv, DXCM.csv, FICO.csv, FTNT.csv, SPGI.csv
│   └── indicator_data/
│       ├── asml.csv, br.csv, dxcm.csv, fico.csv, ftnt.csv, spgi.csv
│
├── indicators/
│   ├── rsi.py, obv.py, macd.py, bollinger_bands.py, moving_averages.py
│
├── notebooks/
│   ├── EDA.ipynb
│   └── indicator_test.ipynb
│
├── utils/
│   ├── data_pull.py
│   └── signal_eval.py
│
├── main.py
├── README.md
└── requirements.txt

* FTNT (Tech / Cybersecurity)
* ASML (Chip hardware)
* DXCM (Healthtech)
* FICO (Fintech / Credit)
* SPGI (Analytics / Finance Infra)
* BR or MKTX (Niche fintech)

Data Pieline : 
Note: for now, the data is fetched only once and is not auto-updating

graph TD
    A[Yahoo Finance] --> B[Load CSV]
    B --> C[Clean Missing Values]
    C --> D[Manual Indicators (RSI, OBV)]
    C --> E[pandas_ta Indicators (MACD, BB, MA)]
    D --> F[Signal Generation & Alerts]
    E --> F
    F --> G[Interactive Visualization Dashboard]

| Indicator        | Source      | Waht it does                                          |
| ---------------- | ----------- | ----------------------------------------------- |
| **RSI (manual)** | `manual` | Show math knowledge (very common in interviews) |
| MACD             | `pandas_ta` | Save time, less prone to bugs                   |
| Bollinger Bands  | `pandas_ta` | Simple to implement, better to auto-use           |
| OBV              | `manual`    | Short + easy to implement                        |
| Moving Averages  | `pandas_ta` | Boilerplate, let lib handle                      


the initial rows had NaN's which is common in rolling calculations like RSI/MACD/Bollinger etc... so these had to be handled

Why??
* RSI: Uses a 14-day rolling average → first 13 rows will be NaN.
* Bollinger Bands: Needs 20 values for a rolling mean → first 19    rows are NaN.
* MACD:
    * EMA-12 and EMA-26 are needed first.
    * MACD Signal line uses a 9-period EMA of MACD line.
    * So expect 33+ days of data before it's fully filled.
* Moving Averages:
    * SMA_20 → first 19 rows will be NaN.
    * SMA_50 → first 49 rows will be NaN.

Sreps : 
* Fetched stock data from Yahoo Finance (manual CSV dump or API).
* Preprocessed for missing values — especially for rolling indicators.
* Engineered Indicators:
    * RSI and OBV from scratch.
    * MACD, Bollinger Bands, and MAs using pandas_ta.
* Generated Buy/Sell Signals with logic based on thresholds and trends.
* Visualized in a clean, interactive, tooltip-rich dashboard.

Feature Engineering : 
* Temporal slicing of data:
    * Focused on recent 30-day trends.
    * Long-term patterns (1Y, 5Y).
* Validated buy/sell signals using multiple indicator confirmations.

Threshold logic : 
| Indicator        | Common Thresholds                               | Interpretation                              |
| ---------------- | ----------------------------------------------- | ------------------------------------------- |
| **RSI**          | 30 (oversold), 70 (overbought)                  | Buy if < 30, Sell if > 70                   |
| **MACD**         | Signal line crossovers                          | MACD > Signal = Bullish, < Signal = Bearish |
| **BBP**          | < 0 = near lower band,<br>> 1 = near upper band | Bounce/reversal possible                    |
| **Price vs EMA** | Cross above/below EMA                           | Bullish/bearish short-term trend shift      |


Tech Stack
* Python
* Pandas, NumPy, pandas_ta
* Streamlit – Dashboard UI
* Matplotlib, Plotly – Visualizations
* Jupyter Notebook – EDA

Insights
| Ticker      | Key Insights                                                        |
| ----------- | ------------------------------------------------------------------- |
| **FTNT**    | Recent RSI dip below 30 → bounce; MACD crossover confirmed uptrend. |
| **ASML**    | BBP hovered below 0.2 for 10 days → price reversal soon.            |
| **DXCM**    | OBV surged before price breakout — smart money entered.             |
| **FICO**    | Consistent bullish EMA crossover + RSI staying in 50–70 zone.       |
| **SPGI**    | Long consolidation with BB squeeze → volatility incoming.           |
| **BR/MKTX** | Lower OBV trend diverging from price — weak rally likely.           |
