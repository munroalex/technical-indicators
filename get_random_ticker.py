import random
from resources import api_key
from stocksymbol import StockSymbol

api_key = api_key
ss = StockSymbol(api_key)
symbol_list_us = ss.get_symbol_list(market="US", symbols_only=True)
symbol_number = random.randint(1, len(symbol_list_us))
ticker = symbol_list_us[symbol_number]
print(ticker)
