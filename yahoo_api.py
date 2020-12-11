
# Making a change on new_branch Windows 10 from gitbash on remote desktop

#pip install yahoo_fin
#pip install yahoo_fin --upgrade
#pip install pandas
#pip install requests
#pip install requests_html

import pandas as pd
from yahoo_fin.stock_info import get_data

path = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'

file = open(path, 'r')

tickers = []

for aline in file:
	values = aline.split() 
	tickers.append(values[0])

file.close()

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

final_df.to_csv(r'//Users/alanjackson/Documents/Environments/stocks_env/stock_data_full_3k.csv')



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
