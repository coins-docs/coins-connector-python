#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(user.get_supported_trading_pairs(recv_window='', timestamp=timestamp))

pprint(user.get_quote(source_currency='PHP', target_currency='BTC', source_amount='200', recv_window='', timestamp=timestamp))

pprint(user.accept_quote(quote_id='', recv_window='', timestamp=timestamp))

pprint(user.query_order_history(start_time='', end_time='', page='', size='', recv_window='', timestamp=timestamp))