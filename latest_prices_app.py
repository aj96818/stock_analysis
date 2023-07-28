
import mysql.connector as mysql

# CoinMarketCap API modules

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

# CoinMarketCap API - get latest crypto prices

api_key = '231f04b7-44ce-4dcd-8dfd-0f0e0e1fbda4'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1'
    , 'limit':'5000'
    , 'convert':'USD'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    json_text = json.loads(response.text)
    data = json_text['data']

    df = pd.json_normalize(data)

    df_short = df[['symbol', 'slug', 'date_added', 'last_updated', 'quote.USD.price', 'quote.USD.volume_24h', 'quote.USD.market_cap', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']]

    crypto_tickers = ['ZRX', '1INCH', 'AAVE', 'AMP', 'AVAX', 'BAL', 'BAT', 'BNB', 'BTC', 'BCH', 'ADA',
                      'LINK', 'CVC', 'ATOM', 'MANA', 'ETH', 'ICP', 'MIOTA', 'KLAY', 'KSM', 'KNC',
                      'LUNA', 'XMR', 'ONT', 'OGN', 'CAKE', 'DOT', 'MATIC', 'REN', 'XRP', 'SOL',
                      'XLM', 'GRT', 'PERP', 'DWEB','THETA', 'RUNE', 'UNI', 'UBT', 'MRPH', 'LSK', 'NEO', 'OMI', 'DAG', 'TRAC'
                        , 'FTM', 'KLIMA', 'GALA', 'SAND', 'EOS','CHZ', 'RBC', 'USDT', 'DAI']

    #df_short.crypto_tickers.isin(crypto_tickers)
    df_out = df_short[df_short['symbol'].isin(crypto_tickers)]
    #  df_out.to_csv(r'coinmarketcap_api_20211014.csv')
    df_out.columns = ['Symbol', 'name', 'date_added', 'last_updated', 'price_usd', 'volume_24h', 'market_cap', 'percent_change_24h', 'percent_change_7d', 'percent_change_30d', 'percent_change_60d', 'percent_change_90d']


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print('except error: check code')

# exclude the following 'names' from coinmktcap df: "luna-coin", "rune", "thorchain-erc20", "unicorn-token"

names_to_exclude = ["genesis-mana", "ruby-currency", "covicoin", "rinnegan", "luna-coin", "golden-ratio-token", "rune", "thorchain-erc20", "unicorn-token", "sol-rune---rune-game"]
df_out = df_out[~df_out.name.isin(names_to_exclude)]


# End Coinmarketcap API Call

# Initialize MySQL connection to 'accounts' table from 'crypto_tracker_db' database.

# How to insert a pandas df into MySQL DB Table
# https://www.dataquest.io/blog/sql-insert-tutorial/


con = mysql.connect(host="localhost", user="root", password="mysqlrootpw", database="crypto_tracker_db")
mycursor = con.cursor()

cols = "`,`".join([str(i) for i in df_out.columns.tolist()])

# Insert DataFrame records one by one.
for i, row in df_out.iterrows():
    sql = "INSERT INTO `prices` (`" + cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    mycursor.execute(sql, tuple(row))

    # the connection is not auto-committed by default, so we must commit to save our changes
    con.commit()

con.close()
