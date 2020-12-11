# Activate Python Virtual Environment:
# cd into Documents/Environments
# source stocks_env/bin/activate
# cd stock_analysis

import time
import pandas as pd
import alpha_vantage
import requests
import requests_html
import json
import finnhub
from yahoo_fin.stock_info import get_data

# Stocks downloaded from 'www.eoddata.com' on 12/9/2020

path = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'

file = open(path, 'r')

tickers = []

for aline in file:
	values = aline.split() 
	tickers.append(values[0])

file.close()


# av_fundamentals.py

#tickers_short = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG','FSLY']
#'RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI','LYFT','UBER','DFS',
#			'DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA','FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA',
 #			'VKTX', 'VXRT', 'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX', 'EBON', 'ATEX']

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
	print(str(ticker) + ' data retrieved...')


av_df = pd.concat(df_list, ignore_index = True)
av_df.to_csv(r'av_fundamentals_full.csv')


# finhub_api.py (for earnings data)

# Setup client
finnhub_client = finnhub.Client(api_key='buugqr748v6rvcd72r80')

companies = ['Sony','Molsen Coors Beverage', 'Snowflake','Ford','Ryder','ServiceNow','Trade Desk','Adobe','DataDog','Fastly','LiveRamp','WisdomTree Emerging Markets High Dividend ETF','Wix','SolarEdge','Agilent','Etsy','Pinterest','Fiverr International','Appian','Li Auto','LYFT','Uber','Discover','WisdomTree Emerging Markets SmallCap Dividend ETF','Home Depot','Southwest Airlines','SPDR Dow Jones Industrial Avg ETF','Salesforce','AMD','Snapchat','Twitter','Nvidia','Facebook','Apple','Splunk','Twilio', 'Amazon', 'Microsoft', 'Netflix', 'Nio (Electric Car)', 'Workhorse Group Inc', 'Nikola Corp',           'Paratek Pharma', 'Eiger Biopharm', 'Atara biotherapeutics', 'Viking Therapeutics', 'Vaxart Pharma', 'Johnson&Johnson', 'Novavax Pharm', 'AstraZeneca Pharm', 'Inovio Pharma', 'Moderna Pharma', 'Titan Pharma', 'Boeing', 'Snowflake', 'First Solar', '51job', 'Digital Turbine', 'Sorento Therapeutics', 'Outset Medical', 'Cerence', 'Cardlytics', 'Ebang', 'Anterix']

df_list = []
for ticker in tickers:
    try:
        data = finnhub_client.company_earnings(symbol = ticker)
        df = pd.DataFrame.from_records(data)
        df_list.append(df)
    except:
        pass

eps_df = pd.concat(df_list, ignore_index = False)
eps_df.to_csv(r'eps_data.csv')


# yahoo_api.py
# filters: > 1 billion 

historical_data = {}
for ticker in tickers:
    try:
        historical_data[ticker] = get_data(ticker)
    except:
        pass

out = []
for df in historical_data:
    out.append(historical_data[df])

yahoo_df = pd.concat(out, ignore_index = False)

yahoo_df.to_csv(r'//Users/alanjackson/Documents/Environments/stocks_env/stock_data_full.csv')




