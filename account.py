#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(user.account(recv_window='', timestamp=timestamp))

pprint(user.my_trades(symbol='XRPPHP', order_id='', start_time='', end_time='', from_id='', limit='', recv_window='', timestamp=timestamp))

pprint(user.trade_fee(symbol='XRPPHP', recv_window='', timestamp=timestamp))

pprint(user.order_test(symbol='XRPPHP', side='buy', type='limit', time_in_force='GTC', quantity='5', quote_order_qty='', price='10', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp=timestamp, stp_flag=''))

pprint(user.order_new(symbol='XRPPHP', side='buy', type='limit', time_in_force='GTC', quantity='5', quote_order_qty='', price='10', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp=timestamp, stp_flag=''))

pprint(user.order_openorders(symbol='XRPPHP', recv_window='', timestamp=timestamp))

pprint(user.order_detail(order_id='1539155133216089344', orig_client_order_id='', recv_window='', timestamp=timestamp))

pprint(user.order_cancel(order_id='1539155133216089344', orig_client_order_id='', recv_window='', timestamp=timestamp))

pprint(user.order_cancel_all(symbol='XRPPHP', recv_window='', timestamp=timestamp))

pprint(user.order_history(symbol='XRPPHP', order_id='', start_time='', end_time='', limit='', recv_window='', timestamp=timestamp))