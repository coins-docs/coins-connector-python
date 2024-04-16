#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from common.client import userClient2 as sub
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(user.subAccount_create(account_name='', timestamp=timestamp, recv_window=''))

pprint(user.subAccount_asset(email='', recv_window='', timestamp=timestamp))

pprint(user.subAccount_list(email='', page='', limit='', recv_window='', timestamp=timestamp))

pprint(user.subAccount_transfer_universal_transfer(from_email='', to_email='', amount='', asset='', recv_window='', timestamp=timestamp))

pprint(user.subAccount_transfer_universal_transfer_history(from_email='', to_email='', client_tran_id='', token_id='', start_time='', end_time='', page='', limit='', recv_window='', timestamp=timestamp))

pprint(sub.subAccount_transfer_sub_to_master(client_tran_id='', amount='', asset='', recv_window='', timestamp=timestamp))

pprint(sub.subAccount_transfer_sub_history(asset='', type='', start_time='', end_time='', page='', limit='', recv_window='', timestamp=timestamp))

pprint(user.subAccount_apikey_ip_restriction(apikey='',email='',recv_window='',timestamp=timestamp))

pprint(user.subAccount_apikey_add_ip_restriction(apikey='', email='', ip_address='', ip_restriction='', recv_window='', timestamp=timestamp))

pprint(user.subAccount_apikey_delete_ip_restriction(apikey='', email='', ip_address='', recv_window='', timestamp=timestamp))