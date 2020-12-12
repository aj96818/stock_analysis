# premium api key: W1U7T09FFM4DY97N

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json

path_win = 'C:/Users/aljackson/Documents/Environments/py_yfinance/NYSE.txt'
file = open(path_win, 'r')

tickers = []

for aline in file:
	try:
		values = aline.split() 
		tickers.append(values[0])
	except IndexError:
		tickers.append('NA')

file.close()

#tickers = ['SNE', 'TAP','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG', 'FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI']

master_df = pd.DataFrame()
df_list = []
for ticker in tickers:
	try:
		API_URL = "https://www.alphavantage.co/query" 
		data = { 
	    	"function": 'TIME_SERIES_WEEKLY_ADJUSTED', 
	    	"symbol": ticker,
	    	"outputsize" : "compact",
	    	"datatype": "json", 
	    	"apikey": 'W1U7T09FFM4DY97N'} 
	
		response = requests.get(API_URL, data) 
		response_json = response.json()

		x = json.dumps(response_json)
		d = json.loads(x)
		
		date_list = []
		data_list = []

		for line in d['Weekly Adjusted Time Series'].items():
			date, data = line
			date_list.append(date)
			data_list.append(data)

		df_date = pd.DataFrame(date_list)
		df_data = pd.DataFrame(data_list)

		df = pd.concat([df_date, df_data], axis = 1)
		df['Symbol'] = ticker
		df_list.append(df)
		time.sleep(2)
	except:
		pass

master_df = pd.concat(df_list, ignore_index = False)
master_df.columns = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume', 'dividend', 'symbol']

df_2yr = master_df[(master_df['date'] > '2018-01-01')]

mac_write_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_weekly_prices.csv'
win_write_path = r'C:/Users/aljackson/Documents/Environments/py_yfinance/av_weekly_prices.csv'

df_2yr.to_csv(win_write_path)