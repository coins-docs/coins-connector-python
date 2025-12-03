from coins.spot import clent, fiatClient
from pprint import pprint
import time

timestamp = int(time.time() * 1000)


pprint(clent.fiat_support_channel(transaction_type='-1', currency='PHP'))

pprint(fiatClient.fiat_cash_out(data={"internalOrderId": "16810937322990",
                                "currency": "PHP",
                                "amount": "50",
                                "channelName": "SWIFTPAY_PESONET",
                                "channelSubject": "gcash",
                                "extendInfo": {"recipientName": "coins-open-api-test",
                                               "recipientAccountNumber": "123456789"}}))

pprint(clent.fiat_details(internal_order_id='16810937322990'))

pprint(clent.fiat_history_order(page_num='1', page_size='10', internal_order_id='', transaction_type='', transaction_channel='', transaction_subject='', status='', fiat_currency='', start_date='', end_date=''))

pprint(clent.generate_qr_code(requestId='', type='', source='', amount='', currency='PHP', remark='', expiredSeconds='', qrCodeMerchantName=''))


pprint(clent.get_qr_code(requestId='9805e40e-2c5a-4980-8023-53726c3885ec'))

pprint(clent.fiat_history_order_v2(page_num='1', page_size='10', external_order_id='', internal_order_id='', transaction_type='', transaction_channel='', transaction_subject='', status='', fiat_currency='', start_date='', end_date=''))

pprint(clent.generate_static_qr_code(request_id='9805e40e-2c5a-4980-8023-53726c3885ed', source='', currency='PHP', remark='', qr_code_merchant_name='', sub_merchant_id='', recv_window='', timestamp=timestamp))

pprint(clent.cancel_qr_code(reference_id='', recv_window='', timestamp=timestamp))

pprint(clent.update_qr_code(request_id='', status='', recv_window='', timestamp=timestamp))

pprint(clent.get_qr_code_static_list(status='', recv_window='', timestamp=timestamp))
