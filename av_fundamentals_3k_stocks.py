
# Alpha Vantage API has a 5 request per minute limit on their API.

# cd into Documents/Environments
# source stocks_env/bin/activate
# cd stocks_env

#pip install alpha_vantage

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json

#tickers = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG','FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI','LYFT','UBER','DFS','DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA','FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT', 'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX', 'EBON', 'ATEX']
#path = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'

path = 'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\NYSE.txt'

file = open(path, 'r')

tickers = []

for aline in file:
	values = aline.split()
	try:
		tickers.append(values[0])
	except IndexError:
		tickers.append('NULL') 
	#tickers.append(values[0])
	#print(values[0])

file.close()

#print(tickers[1:50])

df_list = []
for ticker in tickers:

	API_URL = "https://www.alphavantage.co/query" 
	data = { 
		"function": 'OVERVIEW', 
		"symbol": ticker,
		"outputsize" : "compact",
		"datatype": "json", 
		"apikey": 'YBPBDWS569VUQ3I2'} 

	response = requests.get(API_URL, data) 
	response_json = response.json() # maybe redundant
	
	x = json.dumps(response_json)
	dict_data = json.loads(x)
	df = pd.DataFrame.from_dict(dict_data, orient = 'index')
	df['index_col'] = df.index
	df = df.set_index('index_col')
	df_transposed = df.transpose()
	if set(['Symbol', 'Name','MarketCapitalization', 'EBITDA', 'LatestQuarter', 'PercentInstitutions']).issubset(df_transposed.columns):
		df_short = df_transposed[['Symbol', 'Name','MarketCapitalization', 'EBITDA', 'LatestQuarter', 'PercentInstitutions']]
		df_list.append(df_short)
		time.sleep(15)
		print(str(ticker) + ': data retrieved...')
		


final_df = pd.concat(df_list, ignore_index = True)
final_df.to_csv(r'C:\\Users\\aljackson\\Documents\\Environments\\py_yfinance\\av_fundamentals_3k_stocks.csv')

