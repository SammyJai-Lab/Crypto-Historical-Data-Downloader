# About

### Download ByBit Historical Data using the official ByBit api and pybit in a csv format


# Getting Started
## Prerequistes

- pybit
- pandas

To install all of the required libraries, use the following command

```ps
pip install -r requirements.txt
``` 

# Usage

Run **DataDownloader.py** and the historical data will be downloaded in to a csv file

```ps
python DataDownloader.py
```

Modify the following parameters to get the script to download different data

```python
target_trading_pair = 'BTCUSDT' # Trading Pair
interval = '240'                # Timeframe (See Below)
file_name = "BTC_USDT_4h.csv"   # Output File Name
```

### Kline interval (interval)
- 1 - 1 minute
- 3 - 3 minutes
- 5 - 5 minutes
- 15 - 15 minutes
- 30 - 30 minutes
- 60 - 1 hour
- 120 - 2 hours
- 240 - 4 hours
- 360 - 6 hours
- 720 - 12 hours
- D - 1 day
- W - 1 week
- M - 1 month


