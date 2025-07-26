Advanced Technical Analysis of Emerging Market Leaders

Motication : beyond the obvious

* FTNT (Tech / Cybersecurity)
* ASML (Chip hardware)
* DXCM (Healthtech)
* FICO (Fintech / Credit)
* SPGI (Analytics / Finance Infra)
* BR or MKTX (Niche fintech)

Add 3-5 insights per company (trends, indicator alerts, etc.)

what each indicator means and how it contributes to the analysis

| Indicator        | Source      | Reason                                          |
| ---------------- | ----------- | ----------------------------------------------- |
| **RSI (manual)** | `your_code` | Show math knowledge (very common in interviews) |
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