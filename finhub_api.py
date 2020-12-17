# finhub.io
# email: aj96818@gmail.com
# pw: CheeseWhynot4u
# api key: 'buugqr748v6rvcd72r80'
# sandbox api key: 'sandbox_buugqr748v6rvcd72r8g'
# webhook secret: 'buugqr748v6rvcd72r90'

# api documentation: https://finnhub.io/docs/api

# https://github.com/Finnhub-Stock-API/finnhub-python

#pip install finnhub-python

import finnhub
import pandas as pd
import json
import time

# Stocks downloaded from 'www.eoddata.com' on 12/9/2020

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

# Get earnings data for all stocks from Finhub API: 

finnhub_client = finnhub.Client(api_key='buugqr748v6rvcd72r80')

finhub_list = []

# tickers = ['SNE', 'TAP', 'SNOW']
for ticker in tickers:
	try:
		data = finnhub_client.company_earnings(symbol = ticker)
		df = pd.DataFrame.from_records(data)
		finhub_list.append(df)
		time.sleep(2)
	except:
		pass

win_eps_path = r'C:/Users/aljackson/Documents/Environments/py_yfinance/FinHub_EPS_Data.csv'

eps_df = pd.concat(finhub_list, ignore_index = False)
eps_df.to_csv(win_eps_path)
