from coins.spot import clent
from pprint import pprint


pprint(clent.avg_price(symbol='XRPPHP'))

pprint(clent.depth(symbol='XRPPHP', limit=''))

pprint(clent.klines(symbol='XRPPHP', interval='1m', strat_time='', end_time='', limit='1'))

pprint(clent.ticker_24hr(symbol='XRPPHP', symbols=['']))

pprint(clent.ticker_book_ticker(symbol='XRPPHP', symbols=['']))

pprint(clent.ticker_price(symbol='XRPPHP', symbols=['']))

pprint(clent.trades(symbol='XRPPHP', limit=''))
