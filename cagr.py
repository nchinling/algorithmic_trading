import yfinance as yf


# create list of stocks
tickers = ["AMZN", "MSFT", "GOOG", "D05.SI", "BABA" ]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period="6mo", interval="1d")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp


def CAGR(DF):
    df = DF.copy()
    df["return"] = df["Adj Close"].pct_change()
    df["cum_return"] = (1+df["return"]).cumprod()
    n=len(df)/252
    CAGR = (df["cum_return"][-1])**(1/n)-1
    return CAGR

# Alternative code 
# def CAGR(DF):
#     df = DF.copy()
#     n=len(df)/252
#     CAGR = (df["Adj Close"][-1] / df["Adj Close"][0])**(1/n) - 1
#     return CAGR
    

for ticker in ohlcv_data:
    print("CAGR for {} = {}".format(ticker, CAGR(ohlcv_data[ticker])))



