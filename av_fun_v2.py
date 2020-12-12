# premium api key: W1U7T09FFM4DY97N
# free api key: YBPBDWS569VUQ3I2


import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json

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

# tickers = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG']

df_list = []
for ticker in tickers:
	try:
		API_URL = "https://www.alphavantage.co/query" 
		data = { 
		    "function": 'OVERVIEW', 
		    "symbol": ticker,
		    "outputsize" : "compact",
		    "datatype": "json", 
		    "apikey": 'W1U7T09FFM4DY97N'} 

		response = requests.get(API_URL, data) 
		response_json = response.json() # maybe redundant
		
		x = json.dumps(response_json)
		d = json.loads(x)
		subset_d = dict((k, d[k]) for k in ('Symbol', 'Name', 'Sector', 'Industry','FullTimeEmployees', 'FiscalYearEnd', 'LatestQuarter', 'MarketCapitalization', 'EBITDA', 'PERatio', 'PEGRatio', 'BookValue', 'EPS', 'RevenuePerShareTTM', 'ProfitMargin', 'QuarterlyEarningsGrowthYOY', 'QuarterlyRevenueGrowthYOY', 'AnalystTargetPrice', '50DayMovingAverage', '200DayMovingAverage', 'PercentInsiders', 'PercentInstitutions'))
		
		df = pd.DataFrame.from_dict(subset_d, orient = 'index')
		df = df.transpose()
		df_list.append(df)
		time.sleep(2)
	except:
		pass


final_df = pd.concat(df_list, ignore_index = True)

mac_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_fun_v2.csv'
win_path = r'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\av_fun_v2.csv'

final_df.to_csv(win_path)



