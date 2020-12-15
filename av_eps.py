# premium api key: W1U7T09FFM4DY97N

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json
import finnhub



# Get stock tickers from www.eoddata.com

win_nyse = 'C:/Users/aljackson/Documents/Environments/py_yfinance/NYSE.txt'
mac_nyse = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'

file = open(win_nyse, 'r')

tickers = []

for aline in file:
	try:
		values = aline.split() 
		tickers.append(values[0])
	except IndexError:
		tickers.append('NA')

file.close()

#tickers = ['SNE', 'GOOG']


# Get Fundamentals data for all stocks from Alpha Vantage API (av api).

eps_list = []
for ticker in tickers:
	try:
		API_URL = "https://www.alphavantage.co/query" 
		data = { 
			"function": 'EARNINGS', 
			"symbol": ticker,
			"outputsize" : "compact",
			"datatype": "json", 
			"apikey": 'W1U7T09FFM4DY97N'} 

		response = requests.get(API_URL, data) 
		response_json = response.json() # maybe redundant
		
		x = json.dumps(response_json)
		d = json.loads(x)
		e = d['quarterlyEarnings'][:5]
		
		for dic in e:
			df = pd.DataFrame.from_dict(dic, orient = 'index')
			df = df.transpose()
			df['symbol'] = ticker
			eps_list.append(df)
	except:
		pass		


df_out = pd.concat(eps_list, ignore_index = True)


mac_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_fun_v2.csv'
win_path = r'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\av_fun_v2.csv'

df_out.to_csv(win_path)


