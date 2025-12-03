from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)


pprint(clent.my_trades(symbol='XRPPHP', order_id='', start_time='', end_time='', from_id='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.trade_fee(symbol='XRPPHP', recv_window='', timestamp=timestamp))

pprint(clent.order_test(symbol='XRPPHP', side='buy', type='limit', time_in_force='GTC', quantity='5', quote_order_qty='', price='10', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp=timestamp, stp_flag=''))

pprint(clent.order_new(symbol='XRPPHP', side='buy', type='limit', time_in_force='GTC', quantity='5', quote_order_qty='', price='10', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp=timestamp, stp_flag=''))

pprint(clent.order_openorders(symbol='XRPPHP', recv_window='', timestamp=timestamp))

open_orders = clent.order_openorders(symbol='XRPPHP', recv_window='', timestamp=timestamp)

pprint(clent.order_cancel_replace(symbol='XRPPHP', side='buy', type='limit', time_in_force='GTC', quantity='6', quote_order_qty='', price='11', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp=timestamp,stp_flag='',cancelOrderId=org_order_id,cancelReplaceMode='ALLOW_FAILURE', cancelOrigClientOrderId='',cancelRestrictions=''))

pprint(clent.order_detail(order_id='1539155133216089344', orig_client_order_id='', recv_window='', timestamp=timestamp))

pprint(clent.order_cancel(order_id='1539155133216089344', orig_client_order_id='', recv_window='', timestamp=timestamp))

pprint(clent.order_cancel_all(symbol='XRPPHP', recv_window='', timestamp=timestamp))

pprint(clent.order_history(symbol='XRPPHP', order_id='', start_time='', end_time='', limit='', recv_window='', timestamp=timestamp))
