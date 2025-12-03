from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(clent.account(recv_window='', timestamp=timestamp))

pprint(clent.config_getall(recv_window='', timestamp=timestamp))

pprint(clent.deposit_address(coin='ETH', network='ETH', recv_window='', timestamp=timestamp))

pprint(clent.deposit_history(coin='', tx_id='', status='', start_time='', end_time='', offset='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.withdraw_apply(coin='', network='', address='', address_tag='', amount='', withdraw_order_id='', recv_window='', timestamp=timestamp))

pprint(clent.withdraw_history(coin='', withdraw_order_id='', status='', start_time='', end_time='', offset='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.transaction_history(token_id='', start_time='', end_time='', sub_user_id='', page_num='', page_size='', recv_window='', timestamp=timestamp))

pprint(clent.address_whitelist(coin='', network='', address='', recv_window='', timestamp=timestamp))

pprint(clent.api_keys(recv_window='', timestamp=timestamp))
