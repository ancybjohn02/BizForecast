import yfinance as yf

tickers = ['ASML', 'DXCM', 'SPGI', 'BR', 'MPWR', 'KLAC', 'FICO', 'MKTX', 'FTNT']

for ticker in tickers:
    df = yf.download(ticker, start="2015-01-01")
    df.to_csv(f"/home/zeal/Desktop/BizForecast/MVP/data/{ticker}.csv")

