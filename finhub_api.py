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

# Setup client
finnhub_client = finnhub.Client(api_key='buugqr748v6rvcd72r80')


dictionary = finnhub_client.company_basic_financials('DDOG', 'margin')

# Find: EPS (Earnings Per Share) for last five years
# Find: Current vs Previous Quarterly Earnings up >= 20%

#print(dictionary['metric'])

data = finnhub_client.company_earnings(symbol='DDOG')

out = pd.DataFrame()
for d in data:
    out = pd.DataFrame.from_dict(d)
    



print(out)

#print(finnhub_client.company_profile(symbol='DDOG'))

#metric = finnhub_client.company_basic_financials('DDOG', 'margin')

#print(metric)

#print(metric['freeOperatingCashFlow/revenueTTM'])

# print(finnhub_client.company_basic_financials('DDOG', 'margin'))

# # Earnings surprises
# print(finnhub_client.company_earnings('DDOG', limit=5))
