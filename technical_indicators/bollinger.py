import yfinance as yf


# create list of stocks
tickers = ["AMZN", "MSFT", "GOOG", "D05.SI", "BABA" ]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker, period="1mo", interval="5m")
    temp.dropna(how="any", inplace=True)
    ohlcv_data[ticker] = temp


def Boll_Band(DF, n=14):
    df = DF.copy()
    df["MB"] = df["Adj Close"].rolling(n).mean()
    df["UB"] = df["MB"] + 2*df["Adj Close"].rolling(n).std(ddof=0)
    df["LB"] = df["MB"] - 2*df["Adj Close"].rolling(n).std(ddof=0)
    df["BB_Width"] = df["UB"] - df["LB"]
    return df[["MB", "UB", "LB", "BB_Width"]]

for ticker in ohlcv_data:
    ohlcv_data[ticker][["MB", "UB", "LB", "BB_Width"]] = \
    Boll_Band(ohlcv_data[ticker],20)

ohlcv_data["AMZN"][["MB", "UB", "LB"]].plot()