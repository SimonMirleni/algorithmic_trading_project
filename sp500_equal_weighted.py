import numpy as np
import pandas as pd
import requests
import math
from confidencial import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')

# Function sourced from 
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

symbol_groups = list(chunks(stocks['Ticker'], 100))
symbol_strings = []
for i in chunks(stocks['Ticker'], 100):
    symbol_strings.append(','.join(i))

my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
for symbol_string in symbol_strings:
    batch_api_call_url = f'https://cloud.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_api_call_url).json()
    for symbol in symbol_string.split(','):
        symbol_data = data[symbol]['quote']
        
        final_dataframe.loc[len(final_dataframe)] = [
            symbol,
            symbol_data['latestPrice'],
            symbol_data['marketCap'],
            'N/A'
        ]
        
print(final_dataframe)