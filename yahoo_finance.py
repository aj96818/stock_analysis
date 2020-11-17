
#pip install yahoo_fin
#pip install yahoo_fin --upgrade
#pip install pandas
#pip install requests
#pip install requests_html
import pandas as pd

from yahoo_fin.stock_info import get_data

#import pandas.io.data as web

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



for key in historical_data:
    for col_name in historical_data[key]:
        for value in historical_data[key][col_name]:
            print(historical_data[key])
            
 

print(historical_data['NIO']['open'])





# for x in historical_data:
#     for y in historical_data[x]:
#         print(len(y))




# for i in historical_data.keys():
#     for x in historical_data[i]:
#         print("{} --- {}".format(i,x))




# for key, value in historical_data.items():
#      print(key, value)







#print(historical_data.keys())

#print(type(historical_data[].values()))

#df = pd.DataFrame.from_dict(historical_data, orient = 'index', columns = ['value'])
#df = pd.DataFrame([historical_data], columns = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker'])

#print([historical_data])

#print(df)


#print(str(historical_data.values()))
#pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk)) for stk in ['NIO', 'LI']))
# print(pdata)
# output = pd.DataFrame()
# output = output.append(historical_data, ignore_index=True)
# print(output.head())
# for ticker in tickers:
#     historical_data[ticker] = get_data(ticker)
#df = pd.DataFrame(list(historical_data.items()), columns = ['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker'])
#nio = historical_data['NIO']
#df = pd.DataFrame([historical_data], columns = historical_data.keys())
#df_table = pd.concat([df_table, df], axis = 0).reset_index()
#print(df)
# amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")
# print(amazon_weekly)
