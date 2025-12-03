from coins.spot import clent
from pprint import pprint
import time

timestamp = int(time.time() * 1000)


pprint(clent.payment_request(payer_contact_info='john.zhang+1@coins.ph', receiving_account='1451431230880900352', amount='123', message='message1234', supported_payment_collectors='["coins_peso_wallet"]', expires_at='1w', recv_window='', timestamp=timestamp))

pprint(clent.get_payment_request(id='', start_time='', end_time='', limit='', recv_window='', timestamp=timestamp))

pprint(clent.cancel_payment_request(id='1539181661022855936', recv_window='', timestamp=timestamp))

pprint(clent.payment_request_reminder(id='1539182419067806464', recv_window='', timestamp=timestamp))
