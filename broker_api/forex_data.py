# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:54:34 2023

@author: nchin
Retrieval and plotting of multiple instruments from Meta Trader
"""

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
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
print("Successfully connected to: ", mt5.terminal_info())
# get data on MetaTrader 5 version
print("MetaTrader 5 version: ", mt5.version())



# request 1000 EURAUD ticks till date (backward data)
euraud_ticks = mt5.copy_ticks_from("EURAUD", datetime(2023,11,20, 13), 1000, mt5.COPY_TICKS_ALL )
# request ticks from AUDUSD within 2022.0.01 13:00 - 2023.01.01 13:00
audusd_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2023,1,1,13), datetime(2023,1,4,13), mt5.COPY_TICKS_ALL)
 
# get bars from different symbols in a number of ways
eurusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, datetime(2023,1,28,13), 1000)
eurgbp_rates = mt5.copy_rates_from_pos("EURGBP", mt5.TIMEFRAME_M1, 0, 1000)
eurcad_rates = mt5.copy_rates_range("EURCAD", mt5.TIMEFRAME_M5, datetime(2023,1,5,13), datetime(2023,2,5,13))

# Create a dictionary with names and corresponding data
symbols_data = {
    'euraud_ticks': euraud_ticks,
    'audusd_ticks': audusd_ticks,
    'eurusd_rates': eurusd_rates,
    'eurgbp_rates': eurgbp_rates,
    'eurcad_rates': eurcad_rates
}

for name, data in symbols_data.items():
    # Print the name and the length of the data
    print(f'Number of {name} data points:', len(data))
    
# Iterate over the dictionary items and plot the data
for name, data in symbols_data.items():
    # Create DataFrame
    if 'tick' in name:
        ticks_frame = pd.DataFrame(data)
        ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')
        # Plot the data
        plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
        plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')
        
        plt.legend()
        plt.title(f'{name} tick data')
        plt.show()
        
    elif 'rates' in name:
        rates_frame = pd.DataFrame(data)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        # Plot the data
        plt.plot(rates_frame['time'], rates_frame['close'], label='close')
        
        plt.legend()
        plt.title(f'{name} data')
        plt.show()


# #PLOT
# # create DataFrame out of the obtained data
# ticks_frame = pd.DataFrame(eurusd_rates)
# # convert time in seconds into the datetime format
# ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
# # display ticks on the chart
# plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
# plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')
 
# # display the legends
# plt.legend(loc='upper left')
 
# # add the header
# plt.title('EURAUD ticks')
 
# # display the chart
# plt.show()