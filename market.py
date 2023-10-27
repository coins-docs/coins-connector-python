#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from pprint import pprint


pprint(user.avg_price(symbol='XRPPHP'))

pprint(user.depth(symbol='XRPPHP', limit=''))

pprint(user.klines(symbol='XRPPHP', interval='1m', strat_time='', end_time='', limit='1'))

pprint(user.ticker_24hr(symbol='XRPPHP', symbols=['']))

pprint(user.ticker_book_ticker(symbol='XRPPHP', symbols=['']))

pprint(user.ticker_price(symbol='XRPPHP', symbols=['']))

pprint(user.trades(symbol='XRPPHP', limit=''))