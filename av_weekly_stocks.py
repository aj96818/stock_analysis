# premium api key: W1U7T09FFM4DY97N

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json

tickers = ['SNE', 'TAP']

#,'TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG']


# 'FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI',
# 'LYFT','UBER','DFS','DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA',
# 'FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA',
#  'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT', 'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA',
#   'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX',
#    'EBON', 'ATEX']

master_df = pd.DataFrame()
df_list = []
for ticker in tickers:

	API_URL = "https://www.alphavantage.co/query" 
	data = { 
	    "function": 'TIME_SERIES_WEEKLY_ADJUSTED', 
	    "symbol": ticker,
	    "outputsize" : "compact",
	    "datatype": "json", 
	    "apikey": 'W1U7T09FFM4DY97N'} 

	
	response = requests.get(API_URL, data) 
	response_json = response.json() # maybe redundant

	x = json.dumps(response_json)
	d = json.loads(x)
	
	date_list = []
	data_list = []

	for line in d['Weekly Adjusted Time Series'].items():
 		date, data = line
 		date_list.append(date)
 		data_list.append(data)

#print(date_list)
#print(data_list)

	df_date = pd.DataFrame(date_list)
	df_data = pd.DataFrame(data_list)

#print(date_list)
#print(df_data)

	df = pd.concat([df_date, df_data], axis = 1)
	df['Symbol'] = ticker
	#master_df.append(df)
	df_list.append(df)

master_df = pd.concat(df_list, ignore_index = False)
master_df.columns = ['date', 'open', 'high', 'low', 'close', 'adj close', 'volume', 'dividend', 'symbol']

df_2yr = master_df[(master_df['date'] > '2018-01-01')]

df_2yr.to_csv(r'//Users/alanjackson/Documents/Environments/stocks_env/av_fundamentals_weekly.csv')


#  		for date, df in data.items():
#  			df['Date'] = date

# master_frame = pd.concat(sorted(data.values(), key = lambda df: df['Date'][0]), ignore_index = True)









	# final_df = pd.DataFrame()

	# for key, value in d['Weekly Adjusted Time Series'].items():
	# 	df = value
	# 	df.loc[:, 'Date'] = key
	# 	final_df = pd.concat([df, final_df], 0)

	# print(final_df)

# 	for line in d['Weekly Adjusted Time Series'].items():
# 		date, data = line
# #		print(type(date))
# 		df_date = pd.DataFrame.

# 		df = pd.DataFrame.from_dict(data, orient = 'index')
# 		df2 = pd.concat(date, df)
# 		print(df2)

# #		df.set_index(date)
# #		df_transposed = df.transpose()
# #		print(df_transposed) 
		

	


	#print(dict_data)
	#df = pd.DataFrame.from_dict(data, orient = 'index')

	#df['index_col'] = df.index
	#df = df.set_index('index_col')
	#df_transposed = df.transpose()

	#print(df_transposed)

	# if set(['Symbol', 'Name','MarketCapitalization', 'EBITDA', 'LatestQuarter', 'PercentInstitutions']).issubset(df_transposed.columns):
	# 	df_short = df_transposed[['Symbol', 'Name','MarketCapitalization', 'EBITDA', 'LatestQuarter', 'PercentInstitutions']]
	# 	df_list.append(df_short)
	# time.sleep(2)


#print(df_list)

# final_df = pd.concat(df_list, ignore_index = True)
# final_df.to_csv(r'//Users/alanjackson/Documents/Environments/stocks_env/av_fundamentals_weekly.csv')

