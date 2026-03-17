import pandas as pd
import requests
import os
import json

url = r"https://api.coingecko.com/api/v3/simple/price"  

params = {                                              
    "ids" : "bitcoin,ethereum,ripple,tether,solana",
    "vs_currencies" : "usd"
}

json_data = requests.get(url, params = params)          
data = json_data.json()                                 
df = pd.DataFrame(data).T                               
df.reset_index(inplace = True)                          
df.columns = ["coin", "price, usd"]                     

df.to_excel(файл_день с котировками)
