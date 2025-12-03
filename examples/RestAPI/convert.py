from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(clent.get_supported_trading_pairs(recv_window='', timestamp=timestamp))

pprint(clent.get_quote(source_currency='PHP', target_currency='BTC', source_amount='200', recv_window='', timestamp=timestamp))

pprint(clent.accept_quote(quote_id='', recv_window='', timestamp=timestamp))

pprint(clent.query_order_history(start_time='', end_time='', page='', size='', recv_window='', timestamp=timestamp))
