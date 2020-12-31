# premium api key: W1U7T09FFM4DY97N

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json


startTime = time.time()


crypto = ['BTC', 'ETH', 'ZRX', 'BAL', 'BAT', 'BCH', 'KNC', 'LSK', 'IOTA', 'MRPH', 'NEO', 'ONT', 'DOT', 'POWR', 'REN', 'XLM', 'UBT', 'WPR']

df_list = []
for ticker in crypto:
	try:
		API_URL = "https://www.alphavantage.co/query" 
		data = { 
			"function": 'CURRENCY_EXCHANGE_RATE', 
			"from_currency": ticker,
			"to_currency" : 'USD',
			"datatype": "json", 
			"apikey": 'W1U7T09FFM4DY97N'} 

		response = requests.get(API_URL, data) 
		response_json = response.json() # maybe redundant
		
		x = json.dumps(response_json)
		d = json.loads(x)
		e = d['Realtime Currency Exchange Rate']
		a = dict((k, e[k]) for k in ('1. From_Currency Code', '2. From_Currency Name', '3. To_Currency Code', '4. To_Currency Name', '5. Exchange Rate', '6. Last Refreshed', '7. Time Zone', '8. Bid Price', '9. Ask Price'))	

		df = pd.DataFrame.from_dict(a, orient = 'index')
		df = df.transpose()
		df_list.append(df)
		time.sleep(2)
	except:
		pass

final_df = pd.concat(df_list, ignore_index = True)

#print(final_df)

mac_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_fun_v2.csv'
win_path = r'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\av_fun_v2.csv'

final_df.to_csv(win_path)

# executionTime = (time.time() - startTime)
# print('Execution time in hours: ' + str(executionTime/3600))





