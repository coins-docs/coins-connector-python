from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(clent.subAccount_create(account_name='', timestamp=timestamp, recv_window=''))

pprint(clent.subAccount_asset(email='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_list(email='', page='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_transfer_universal_transfer(from_email='', to_email='', amount='', asset='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_transfer_universal_transfer_history(from_email='', to_email='', client_tran_id='', token_id='', start_time='', end_time='', page='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_transfer_sub_to_master(client_tran_id='', amount='', asset='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_transfer_sub_history(asset='', type='', start_time='', end_time='', page='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_apikey_ip_restriction(apikey='',email='',recv_window='',timestamp=timestamp))

pprint(clent.subAccount_apikey_add_ip_restriction(apikey='', email='', ip_address='', ip_restriction='', recv_window='', timestamp=timestamp))

pprint(clent.subAccount_apikey_delete_ip_restriction(apikey='', email='', ip_address='', recv_window='', timestamp=timestamp))

pprint(clent.collect_from_subaccount(client_request_id='12121212', remark='', recv_window='', timestamp=timestamp))

pprint(clent.get_fund_record(client_request_id='', page='', size='', recv_window='', timestamp=timestamp))

pprint(clent.wallet_deposit_address(email='', coin='', network='', recv_window='', timestamp=timestamp))

pprint(clent.wallet_deposit_history(email='', coin='', tx_id='', deposit_id='', start_time='', end_time='', limit='', offset='', status='', recv_window='', timestamp=timestamp))
