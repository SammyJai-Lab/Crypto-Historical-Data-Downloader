# imports
from pybit.usdt_perpetual import HTTP
import pandas as pd
import numpy as np
import time
from scipy.stats import linregress
session = HTTP("https://api.bybit.com")

# Parameters
target_trading_pair = 'BTCUSDT'
interval_int = 240
file_name = "BTC_USDT_4h.csv"

def get_all_usdt_perceptual(contract_symbol, interval_int, file_name):
    start = 1546300800
    all_df = []
    
    while True:
        data = session.query_kline(symbol=contract_symbol, interval=interval_int, limit=200, from_time=start)
        data_df = pd.DataFrame(data['result'])
        data_df['time'] = pd.to_datetime(data_df['open_time'], unit='s')
        prev = start
        start = data_df['open_time'].tail(1).iloc[0]
        all_df.append(data_df)
        time.sleep(3)
        print(data_df['time'].tail(1).iloc[0])
        if start == prev:
            break
    
    data = pd.concat(all_df)
    data.index = data.time
    data['Open'] = data['open'].astype('float64')
    data['Close'] = data['close'].astype('float64')
    data['High'] = data['high'].astype('float64')
    data['Low'] = data['low'].astype('float64')
    data.to_csv(file_name)
    
    return data

data = get_all_usdt_perceptual(target_trading_pair, interval_int, file_name)