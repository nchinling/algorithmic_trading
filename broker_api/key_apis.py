# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:47:25 2023

@author: nchin
"""


import MetaTrader5 as mt5
import pandas as pd
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


def get_position_df():
    positions = mt5.positions_get()
    # positions[0]._asdict().keys()
    if len(positions) > 0:
        pos_df = pd.DataFrame(list(positions),columns=positions[0]._asdict().keys())
        pos_df.time = pd.to_datetime(pos_df.time, unit="s")
        pos_df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    else:
        pos_df = pd.DataFrame()
        
    return pos_df

def get_orders_df():
    orders = mt5.orders_get()
    if len(orders) > 0:
        ord_df = pd.DataFrame(list(orders),columns=orders[0]._asdict().keys())
        ord_df.time_setup = pd.to_datetime(ord_df.time_setup , unit="s")
        #ord_df.drop(['time_update_msc'], axis=1, inplace=True)
    else:
        ord_df = pd.DataFrame()
        
    return ord_df


positions_df = get_position_df()
orders_df = get_orders_df()


