import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# create list of stocks
stocks = ["AMZN", "MSFT", "GOOG", "D05.SI", "BABA" ]
start = datetime.datetime.today() - datetime.timedelta(3600)
end = datetime.datetime.today()

cl_price = pd.DataFrame() # Adjusted close prices

# ohlcv_data = {}
# # loop over tickers stored in dictionary
# for ticker in stocks:
#     ohlcv_data[ticker] = yf.download(ticker, start, end)
#     print(ohlcv_data[ticker])
# print(ohlcv_data["D05.SI"]["Open"])

# loop over tickers stored in pandas dataframe
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]

# Backfill missing data
cl_price.fillna(method='bfill', axis=0, inplace=True)

# drop missing data
# cl_price.dropna()


# descriptive statistics (no real value in algo trading)
cl_price.mean()
cl_price.std()
cl_price.median()
cl_price.describe()

# plot adjusted closing price
cl_price.plot()
cl_price.plot(subplots=True, layout=(3,2), title="Stock Prices", grid=True)


# obtain daily return
# daily_return=cl_price.pct_change()
daily_return=cl_price/cl_price.shift(1) - 1 
daily_return.mean(axis=1)
daily_return.std()

# plot daily return using pandas plot function
daily_return.plot(subplots=True, layout=(3,2), title="Daily Return", grid=True)

# plot daily return using matplotlib
fig, ax = plt.subplots()
ax.set(title="Mean Daily Return of Stocks", xlabel="Stocks", ylabel="Mean Return")
plt.style.available
plt.style.use("ggplot")
plt.bar(x=daily_return.columns, height=daily_return.mean())

# plot cumulative return
(1+daily_return).cumprod().plot()

# obtain rolling data using a window period (Simple Moving Average)
daily_return.rolling(window=10).mean()
daily_return.rolling(window=10).std()
daily_return.rolling(window=10).max()
daily_return.rolling(window=10).sum()

# Exponential Moving Average
daily_return.ewm(com=10, min_periods=10).mean()












# loop over tickers stored in dictionary
# for ticker in stocks:
#     ohlcv_data[ticker] = yf.download(ticker, start, end)
#     print(ohlcv_data[ticker])
# print(ohlcv_data["D05.SI"]["Open"])




