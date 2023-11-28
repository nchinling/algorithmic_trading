# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:17:41 2023

@author: nchin

Retrieval and plotting of single instrument from Meta Trader
"""

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
import os


os.chdir(r"C:\Users\nchin\OneDrive\Desktop\Programming\keys") #path where login credentials and server details
key = open("mt5_keys.txt","r").read().split()
path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
 
# connect to MetaTrader 5. Supply path, login, key and server
if mt5.initialize(path=path,login=int(key[0]), password=key[1], server=key[2]):
    print("connection established")
# if not mt5.initialize(path=path, login="", server="MetaQuotes-Demo", password=""):
#     print("initialize() failed")
#     mt5.shutdown()
 
# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

hist_data = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M15, dt.datetime(2023, 11, 1), 1000)
hist_data_df = pd.DataFrame(hist_data)
hist_data_df.time = pd.to_datetime(hist_data_df.time, unit="s")
hist_data_df.set_index("time", inplace=True)

# Plot OHLC data
plt.figure(figsize=(10, 6))
plt.plot(hist_data_df.index, hist_data_df['open'], label='Open', marker='o')
plt.plot(hist_data_df.index, hist_data_df['high'], label='High', marker='o')
plt.plot(hist_data_df.index, hist_data_df['low'], label='Low', marker='o')
plt.plot(hist_data_df.index, hist_data_df['close'], label='Close', marker='o')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('EURUSD Historical OHLC Data')

# Add legend
plt.legend()

# Show the plot
plt.show()