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


# Stocks downloaded from 'www.eoddata.com' on 12/9/2020

path = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'

file = open(path, 'r')

tickers = []

for aline in file:
	values = aline.split() 
	tickers.append(values[0])

file.close()


# Setup client
finnhub_client = finnhub.Client(api_key='buugqr748v6rvcd72r80')

#tickers = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG','FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI','LYFT','UBER','DFS','DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA','FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT', 'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX', 'EBON', 'ATEX']
#tickers = ['SNE','TAP','SNOW','F']
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
eps_df.to_csv(r'//Users/alanjackson/Documents/Environments/stocks_env/eps_data.csv')
