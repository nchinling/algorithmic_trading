# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:41:30 2023

@author: nchin

Placing orders with MetaTrader 5
"""


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

# sl - stop loss, tp - take profit
def place_market_order(symbol,vol,buy_sell,sl_pip,tp_pip):
    pip_unit = 10*mt5.symbol_info(symbol).point
    if buy_sell.capitalize()[0] == "B":
        direction = mt5.ORDER_TYPE_BUY
        price = mt5.symbol_info_tick(symbol).ask
        sl = price - sl_pip*pip_unit
        tp = price + tp_pip*pip_unit
    else:
        direction = mt5.ORDER_TYPE_SELL
        price = mt5.symbol_info_tick(symbol).bid
        sl = price + sl_pip*pip_unit
        tp = price - tp_pip*pip_unit
    
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": vol,
        "type": direction,
        "price": price,
        "sl": sl,
        "tp":tp,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    
    result = mt5.order_send(request)
    return result

def place_limit_order(symbol,vol,buy_sell,pips_away):
    
    pip_unit = 10*mt5.symbol_info(symbol).point
    
    if buy_sell.capitalize()[0] == "B":
        direction = mt5.ORDER_TYPE_BUY_LIMIT
        price = mt5.symbol_info_tick(symbol).ask - pips_away*pip_unit
    else:
        direction = mt5.ORDER_TYPE_SELL_LIMIT
        price = mt5.symbol_info_tick(symbol).bid + pips_away*pip_unit
        
    
    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": vol,
        "type": direction,
        "price": price,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    
    result = mt5.order_send(request)
    return result
    
    
place_market_order("USDJPY",0.05,"BUY", 20, 40)
place_limit_order("GBPUSD",0.02,"Buy",8)
