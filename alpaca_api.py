
# Alpaca API for automated stock trading

# Endpoint: https://api.alpaca.markets

# API Key ID: AKXYB49NY84FT9HBI6UT

# Secret Key: QgRPozzvjbEjW9EhDtY37MNSnZYhFdJHMbburZ1Y

# pip3 install alpaca-trade-api

import alpaca_trade_api as tradeapi


api = tradeapi.REST('AKXYB49NY84FT9HBI6UT', 'QgRPozzvjbEjW9EhDtY37MNSnZYhFdJHMbburZ1Y', base_url='https://api.alpaca.markets') # or use ENV Vars shown below
account = api.get_account()
api.list_positions()

print(account.status)
