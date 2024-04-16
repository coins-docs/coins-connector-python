#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(user.account(recv_window='', timestamp=timestamp))

pprint(user.config_getall(recv_window='', timestamp=timestamp))

pprint(user.deposit_address(coin='ETH', network='ETH', recv_window='', timestamp=timestamp))

pprint(user.deposit_history(coin='', tx_id='', status='', start_time='', end_time='', offset='', limit='', recv_window='', timestamp=timestamp))

pprint(user.withdraw_apply(coin='', network='', address='', address_tag='', amount='', withdraw_order_id='', recv_window='', timestamp=timestamp))

pprint(user.withdraw_history(coin='', withdraw_order_id='', status='', start_time='', end_time='', offset='', limit='', recv_window='', timestamp=timestamp))