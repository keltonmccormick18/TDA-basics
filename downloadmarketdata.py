import yfinance as yf
import pandas as pd

tickers = {
    "S&P 500" : "^GSPC",
    "NASDAQ" : "^IXIC",
    "Russell 2000" : "^RUT"
}

start_date = "1995-01-01"
end_date = "2026-02-26"

for name, ticker in tickers.items():
    df = yf.download(ticker, start=start_date, end=end_date, interval="1d")
    df.to_csv(f"{name.replace(' ','_')}_daily_1995_2025.csv")
    print(f"Saved {name} to {name.replace(' ','_')}_daily_1995_2025.csv")
