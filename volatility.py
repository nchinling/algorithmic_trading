import yfinance as yf
import numpy as np


# create list of stocks
tickers = ["AMZN", "MSFT", "GOOG", "D05.SI", "BABA" ]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period="6mo", interval="1d")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp


def volatility(DF):
    df = DF.copy()
    # Multiply square root of 252 (trading days) to annualize the standard deviation s
    df["return"] = df["Adj Close"].pct_change()
    vol = df["return"].std()*np.sqrt(252)
    return vol


for ticker in ohlcv_data:
    print("Volatility for {} = {}".format(ticker, volatility(ohlcv_data[ticker])))
