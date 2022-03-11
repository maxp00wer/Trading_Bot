import pandas as pd
import numpy as np
import asyncio
from binance import BinanceSocketManager
from binance.client import Client

client = Client(API_KEY, API_SECRET)

ST = 7
LT = 25


def gethistoricals(symbol, LT):
    df = pd.DataFrame(
        client.get_historical_klines(
            symbol, "1d", str(LT) + "days ago UTC", "1 day ago UTC"
        )
    )
