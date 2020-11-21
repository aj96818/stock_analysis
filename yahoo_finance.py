
#pip install yahoo_fin
#pip install yahoo_fin --upgrade
#pip install pandas
#pip install requests
#pip install requests_html

import pandas as pd
from yahoo_fin.stock_info import get_data

# 65 tickers
#tickers = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE']

tickers = ['SNE','TAP','SNOW','F','R','NOW','TTD','ADBE','DDOG','FSLY','RAMP','DEM','WIX','SEDG','A','ETSY','PINS','FVRR','AAPN','LI','LYFT','UBER','DFS','DGS','HD','LUV','DIA','CRM','AMD','SNAP','TWTR','NVDA','FB','AAPL','SPLK', 'TWLO', 'AMZN', 'MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT', 'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS', 'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX', 'EBON', 'ATEX']

companies = ['Sony','Molsen Coors Beverage', 'Snowflake','Ford','Ryder','ServiceNow','Trade Desk','Adobe','DataDog','Fastly','LiveRamp','WisdomTree Emerging Markets High Dividend ETF','Wix','SolarEdge','Agilent','Etsy','Pinterest','Fiverr International','Appian','Li Auto','LYFT','Uber','Discover','WisdomTree Emerging Markets SmallCap Dividend ETF','Home Depot','Southwest Airlines','SPDR Dow Jones Industrial Avg ETF','Salesforce','AMD','Snapchat','Twitter','Nvidia','Facebook','Apple','Splunk','Twilio', 'Amazon', 'Microsoft', 'Netflix', 'Nio (Electric Car)', 'Workhorse Group Inc', 'Nikola Corp',
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



out = []
for df in historical_data:
    out.append(historical_data[df])

final_df = pd.concat(out, ignore_index = False)

final_df.to_csv(r'stock_data_full.csv')



# series_list = []
# for key in historical_data:
#     for col_name in historical_data[key]:
#          series = historical_data[key][col_name]
#          series_list.append(series)


#print(series_list[0:5])


# df_list = []

# for s in series_list:
#     s_df = s.to_frame()
#     df_list.append(s_df)


# df_merge = df_list[0]
# for i in range(0, 6):
#     df_merge = df_merge.merge(df_list[i+1], left_index = True, right_index = True)


# df_merge2 = df_list[7]
# for i in range(7, 13):
#     df_merge2 = df_merge2.merge(df_list[i+1], left_index = True, right_index = True)


# df_merge3 = df_list[14]
# for i in range(14, 20):
#     df_merge3 = df_merge3.merge(df_list[i+1], left_index = True, right_index = True)


# final_df = pd.concat([df_merge, df_merge2, df_merge3], ignore_index = True)
# print(final_df)




# for i in range(len(df_list)):
#     print(i)

# start_index = 0
# end_index = 6
# out = []
# for stock in range(len(tickers)):
#     new_df = df_list[start_index]
#     for i in range(start_index, end_index):
#         new_df = new_df.merge(df_list[i+1], left_index = True, right_index = True)
#     out.append(new_df)
#     start_index += 7
#     end_index += 7


# final_df = pd.concat(out, ignore_index = False)

# #print(out[2])
# #print(final_df)

# final_df.to_csv(r'stock_data_full.csv')

# 433 columns in current stock ticker list











# var 1 (new_df): creates dataframe from 7 columns of df_list
# counter 1: df_list index
# counter 2: begin range counter
# counter 3: end range counter

# stock_counter = 0
# begin = 0
# end = 7
# new_df = pd.DataFrame()

# out = []
# while stock_counter < 2:
#     for i in range(begin, end):
#         new_df = new_df.merge(df_list[i+1], left_index = True, right_index = True)
#     out.append(new_df)
#     begin = begin + 7
#     end = end + 7
#     stock_counter += 1


# print(out)





# for i in range(begin, end):
#     print('this is beginning of for loop: ', begin)
#     print('this is end of for loop: ', end)
#     new_df = df.merge(df_list[i+1], left_index = True, right_index = True)
    
#     begin = begin + 7
#     end = end + 7
#     print(begin)
#     print(end)
#     if end > len(df_list):
#         break


# print(new_df)
























# df = df_merge
# df_idx = 0
# begin = 7
# end = 13

# for i in range(begin, end):
#     new_df = df.merge(df_list[i+1], left_index = True, right_index = True)
#     df.append(new_df)
#     begin = begin + 7
#     end = end + 7
#     print(begin)
#     print(end)
#     if end > len(df_list):
#         break


# print(new_df)

























# while stock_counter <= 1:
#     for i in range(begin, end):
#         df_merge = df_merge.merge(df_list[i], left_index = True, right_index = True)
#     list_of_dfs.append(pd.DataFrame(df_merge, columns = ['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker']))
#     begin = begin + 7
#     end = end + 7
#     stock_counter += 1
#     print('begin print inside for loop: ')
#     print(begin)
#     print('end print inside for loop: ')
#     print(end)















# need to create n-item long list of 7 items per list.
    # input list --> return n-item list of 7 items per list.


# n = 7
# chunked_list = [df_list[i:i + n] for i in range(0, len(df_list), n)]


# df_merge = df_list[0]

# out_list = []

# for c_list in chunked_list:
#     for lst in c_list:
#         out_list.append([df_merge.merge(df_list[lst + 1], left_index = True, right_index = True)])


# stock_counter = 0
# begin = 0
# end = 6
# df_merge = df_list[0]
# output_list = []
# while stock_counter < 3:
#     for i in range(begin, end):
#         df_merge = df_merge.merge(df_list[i+1], left_index = True, right_index = True)
#     begin = begin + 6
#     end = end + 6
#     output_list.append[df_merge]

# print(output_list)

# version 1
# stock_counter = 0
# begin = 0
# end = 6
# df_merge = df_list[0]
# df_collection = {}
# while stock_counter < 3:
#     begin = 0
#     end = 6
#     for i in range(begin, end):
#         df_merge = df_merge.merge(df_list[i+1], left_index = True, right_index = True)
#     begin = begin + 5
#     end = end + 5
#     df_collection = pd.DataFrame(df_merge, columns = ['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker'])
#     stock_counter += 1










# version 2
# stock_counter = 0
# begin = 0
# end = 7
# df_merge = df_list[0]
# list_of_dfs = []
# while stock_counter <= 1:
#     for i in range(begin, end):
#         df_merge = df_merge.merge(df_list[i], left_index = True, right_index = True)
#     list_of_dfs.append(pd.DataFrame(df_merge, columns = ['open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker']))
#     begin = begin + 7
#     end = end + 7
#     stock_counter += 1
#     print('begin print inside for loop: ')
#     print(begin)
#     print('end print inside for loop: ')
#     print(end)


# print('begin: ' + str(begin)) 
# print('end: ' + str(end)) 


# print(list_of_dfs[1])


# print('begin')
# print(begin)
# #print(df_list[7]) open - LI


# print('end')
# print(end)
# #print(df_list[13])

# #print(list_of_dfs[3]) ticker - LI

# print('length of df_list:')
#print(len(df_list))





# # visualizer

# df_list = ['my list' , 'of', 'random', 'strings', 'to', 'vusal', 'dloekf', 'in', 'thel', 'vekwo', 'oeifaj', 'eofifel', 'owiefj', 'sal;sa;sd', 'sldfkfjoe']
# list_of_dfs = []
# stock_counter = 0
# begin = 1
# end = 7
# list_of_dfs = []
# while stock_counter <= 1:
#     for i in range(begin, end):
#         df_list = df_list[i]
#     list_of_dfs.append(df_list)
#     begin = begin + 7
#     end = end + 7
#     stock_counter += 1


















# df_merge = df_list[0]
# output_list = []
# n = 7
# chunked_list = [df_merge.merge(df_list[i + 1], left_index = True, right_index = True) for i in range(0, len(df_list), n)]


# print(chunked_list[1])




# output_list = []

# for x in chunked_list:
#     for i in range(0, 6):
#         output_list = output_list.merge(output_list[i + 1], left_index = True, right_index = True)



# df_merge = df_list[0]
# for i in range(0, 6):
#     df_merge = df_merge.merge(df_list[i+1], left_index = True, right_index = True)










# df_merge = df_list[0]
# for i in range(0, 6):
#     df_merge = df_merge.merge(df_list[i+1], left_index = True, right_index = True)
    


#print(df_merge)









#df = pd.DataFrame([historical_data], columns = ['date', 'open', 'high', 'low', 'close', 'adjclose', 'volume', 'ticker'])


# --------- Initializing Python virtual environment on Windows 10 PC  ---------------- #

# To create virtual environment:
# virtualenv py_yfinance
# To activate virtual environment:

# cd into \Documents\Environments\
# then type:
# C:\Users\aljackson\Documents\Environments\py_yfinance\Scripts\activate.bat
# and hit 'enter'

# python yahoo_finance.py
# to exit out of virtual environment
# enter, "deactivate"
