
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

tickers = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG','FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI','LYFT','UBER','DFS','DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA','FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT', 'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX', 'EBON', 'ATEX']

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


final_df = pd.concat(df_list, ignore_index = True)
final_df.to_csv(r'av_fundamentals_full.csv')

