# create list of stocks from downloaded TXT file of all 3k+ stocks from eoddata.com

path = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'

path2 = '//Users/alanjackson/Documents/Environments/stocks_env/stock_data_full_3k.csv'


path_win = 'C:\Users\aljackson\Documents\Environments\py_yfinance\NYSE.txt'

# Stocks downloaded from 'www.eoddata.com' on 12/9/2020

path = '//Users/alanjackson/Documents/Environments/stocks_env/NYSE.txt'


path_win = 'C:\Users\aljackson\Documents\Environments\py_yfinance\NYSE.txt'
file = open(path_win, 'r')

tickers = []

for aline in file:
	values = aline.split() 
	tickers.append(values[0])

file.close()









file = open(path2, 'r')

i = 0
for aline in file:
	i += 1

print(i)

file.close()


