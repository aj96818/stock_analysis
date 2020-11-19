
#pip install yahoo_fin
#pip install yahoo_fin --upgrade
#pip install pandas
#pip install requests
#pip install requests_html

import pandas as pd
from yahoo_fin.stock_info import get_data



tickers = ['NIO', 'LI']

# tickers = ['SNE','TAP','KO','SNOW','F','R','NOW','TTD','ADBE','DDOG','FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI','LYFT','UBER','DFS','DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA','FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT',
#             'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM',
#             'CRNC', 'CDLX', 'EBON', 'ATEX']

companies = ['Sony','Molsen Coors Beverage','Coca-Cola','Snowflake','Ford','Ryder','ServiceNow','Trade Desk','Adobe','DataDog','Fastly','LiveRamp','WisdomTree Emerging Markets High Dividend ETF','Wix','SolarEdge','Agilent','Etsy','Pinterest','Fiverr International','Appian','Li Auto','LYFT','Uber','Discover','WisdomTree Emerging Markets SmallCap Dividend ETF','Home Depot','Southwest Airlines','SPDR Dow Jones Industrial Avg ETF','Salesforce','AMD','Snapchat','Twitter','Nvidia','Facebook','Apple','Splunk','Twilio', 'Amazon', 'Microsoft', 'Netflix', 'Nio (Electric Car)', 'Workhorse Group Inc', 'Nikola Corp',
            'Paratek Pharma', 'Eiger Biopharm', 'Atara biotherapeutics', 'Viking Therapeutics',
            'Vaxart Pharma', 'Johnson&Johnson', 'Novavax Pharm', 'AstraZeneca Pharm', 
            'Inovio Pharma', 'Moderna Pharma', 'Titan Pharma', 'Boeing', 'Snowflake', 
            'First Solar', '51job', 'Digital Turbine', 'Sorento Therapeutics', 'Outset Medical', 'Cerence', 'Cardlytics', 'Ebang', 'Anterix']

historical_data = {}

for ticker in tickers:
    try:
        historical_data[ticker] = get_data(ticker)
    except:
        pass


series_list = []

for key in historical_data:
    for col_name in historical_data[key]:
         series = historical_data[key][col_name]
         series_list.append(series)


df_list = []

for s in series_list:
    s_df = s.to_frame()
    df_list.append(s_df)


df_merge = df_list[0]

for lst in df_list[1:7]:
    df_merge = df_merge.merge(lst, left_index = True, right_index = True)





#df1 = df_list[0]
#df2 = df_list[1]

#df_merge = df1.merge(df2, left_index = True, right_index = True)


print(df_merge)

#for col in df_list:
   
#range(0, 7)



#df = pd.DataFrame([historical_data], columns = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker'])


# --------- Initializing Python virtual environment on Windows 10 PC  ---------------- #

# To create virtual environment:
# virtualenv py_yfinance
# To activate virtual environment:

# cd into \Documents\Environments\py_yfinance
# then type:
# C:\Users\aljackson\Documents\Environments\py_yfinance\Scripts\activate.bat
# and hit 'enter'

# python yahoo_finance.py
# to exit out of virtual environment
# enter, "deactivate"
