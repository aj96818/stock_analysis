# premium api key: W1U7T09FFM4DY97N

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json


startTime = time.time()


crypto = ['BTC', 'ETH', 'ZRX', 'BAL', 'BAT', 'BCH', 'KNC', 'LSK', 'IOTA', 'MRPH', 'NEO',
'ONT', 'DOT', 'POWR', 'REN', 'XLM', 'UBT', 'WPR']

eps_list = []
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
		print(d)

	except:
		pass		





# df_eps = pd.concat(eps_list, ignore_index = True)

# #print(df_eps)

# mac_path = r'//Users/alanjackson/Documents/Environments/stocks_env/AV_EPS_Data.csv'
# win_path = r'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\AV_EPS_Data.csv'

# #df_eps.to_csv(win_path)

# # Get Fundamentals data for all stocks from Alpha Vantage API (Alpha Vantage API).

# fun_list = []
# for ticker in unique_tickers:
# 	try:
# 		API_URL = "https://www.alphavantage.co/query" 
# 		data = { 
# 			"function": 'OVERVIEW', 
# 			"symbol": ticker,
# 			"outputsize" : "compact",
# 			"datatype": "json", 
# 			"apikey": 'W1U7T09FFM4DY97N'} 

# 		response = requests.get(API_URL, data) 
# 		response_json = response.json() # maybe redundant
		
# 		x = json.dumps(response_json)
# 		d = json.loads(x)
# 		subset_d = dict((k, d[k]) for k in ('Symbol', 'Name', 'Sector', 'Industry','FullTimeEmployees', 'FiscalYearEnd', 'LatestQuarter', 'MarketCapitalization', 'EBITDA', 'PERatio', 'PEGRatio', 'BookValue', 'EPS', 'RevenuePerShareTTM', 'ProfitMargin', 'QuarterlyEarningsGrowthYOY', 'QuarterlyRevenueGrowthYOY', 'AnalystTargetPrice', '50DayMovingAverage', '200DayMovingAverage', 'PercentInsiders', 'PercentInstitutions'))
		
# 		df = pd.DataFrame.from_dict(subset_d, orient = 'index')
# 		df = df.transpose()
# 		fun_list.append(df)
# 		time.sleep(2)
# 	except:
# 		pass

# df_fun = pd.concat(fun_list, ignore_index = True)

# mac_fun_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_fun_data.csv'
# win_fun_path = r'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\av_fun_data.csv'

# #df_fun.to_csv(win_fun_path)

# # Get weekly adjusted stock data for all stocks from Alpha Vantage API (Alpha Vantage API)

# master_df = pd.DataFrame()
# stocks_list = []
# for ticker in unique_tickers:
# 	try:
# 		API_URL = "https://www.alphavantage.co/query" 
# 		data = { 
# 			"function": 'TIME_SERIES_WEEKLY_ADJUSTED', 
# 			"symbol": ticker,
# 			"outputsize" : "compact",
# 			"datatype": "json", 
# 			"apikey": 'W1U7T09FFM4DY97N'} 
	
# 		response = requests.get(API_URL, data) 
# 		response_json = response.json()

# 		x = json.dumps(response_json)
# 		d = json.loads(x)
		
# 		date_list = []
# 		data_list = []

# 		for line in d['Weekly Adjusted Time Series'].items():
# 			date, data = line
# 			date_list.append(date)
# 			data_list.append(data)

# 		df_date = pd.DataFrame(date_list)
# 		df_data = pd.DataFrame(data_list)

# 		df = pd.concat([df_date, df_data], axis = 1)
# 		df['Symbol'] = ticker
# 		stocks_list.append(df)
# 		time.sleep(2)
# 	except:
# 		pass

# master_df = pd.concat(stocks_list, ignore_index = False)
# master_df.columns = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume', 'dividend', 'symbol']

# df_2yr = master_df[(master_df['date'] > '2018-01-01')]

# mac_stocks_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_weekly_stocks.csv'
# win_stocks_path = r'C:/Users/aljackson/Documents/Environments/py_yfinance/av_weekly_stocks.csv'


# # Join "df_2yr" with "df_fun"

# merged_left = pd.merge(left = df_2yr, right = df_fun, how = 'left', left_on = 'symbol', right_on = 'Symbol')

# mac_stocks_fun_path = r'//Users/alanjackson/Documents/Environments/stocks_env/av_stocks_fun.csv'
# win_stocks_fun_path = r'C:/Users/aljackson/Documents/Environments/py_yfinance/AV_StocksFundamentals_Merged.csv'

# merged_left.to_csv(win_stocks_fun_path)

# executionTime = (time.time() - startTime)
# print('Execution time in hours: ' + str(executionTime/3600))





