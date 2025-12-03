from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(clent.crypto_accounts(currency='PHP', recv_window='', timestamp=timestamp))
# #
pprint(clent.p2p_transfer(account='1451431230880900352', amount='50', target_address='john.zhang+1@coins.ph', client_transfer_id='', message='123', recv_window='', timestamp=timestamp))

pprint(clent.query_transfer(id='', client_transfer_id='', page='', per_page='', recv_window='', timestamp=timestamp))
