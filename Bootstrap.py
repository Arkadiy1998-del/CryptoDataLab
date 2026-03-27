import pandas as pd
import requests
import os
import json
import openpyxl
import time

file_path = r"e:\users\agabekov_ai\Проекты\CryptoDataLab\prices.xlsx"
coins = ['bitcoin','ethereum','ripple']
df = pd.DataFrame()
if os.path.exists(file_path): os.remove(file_path)  

for name in coins:
    url = f"https://api.coingecko.com/api/v3/coins/{name}/market_chart"
    params = {"vs_currency" : "usd", "days" : 180}
    json_data = requests.get(url, params = params)
    if json_data.status_code == 200:
        time.sleep(20)
    data = json_data.json()
    temp_df = pd.DataFrame(data['prices'])
    temp_df.columns = ["day_id", "price"]
    temp_df['day_id'] = pd.to_datetime(temp_df['day_id'].astype('int64'), unit = 'ms')
    temp_df = temp_df.set_index('day_id')
    temp_df = temp_df.resample('1D')['price'].mean().reset_index()
    temp_df['coin'] = name
    df = pd.concat([df, temp_df], ignore_index = True)


with pd.ExcelWriter(file_path, engine = 'openpyxl', mode = 'w') as writer:
    df.to_excel(writer, sheet_name = 'bootstrap_180', index = False)
      