from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)

pprint(clent.exchange_info(symbol='XRPPHP', symbols=[]))

pprint(clent.pairs())

pprint(clent.ping())

pprint(clent.time())

pprint(clent.user_ip())

pprint(clent.check_sys_status(business_type='', recv_window='', timestamp=timestamp))
