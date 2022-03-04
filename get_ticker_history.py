import yfinance as yf
from get_random_ticker import ticker

yf_data = yf.Ticker(ticker)

print(yf_data.history(start="2010-01-01", end="2020-07-21").head())
