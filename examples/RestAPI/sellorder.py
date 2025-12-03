from coins.spot import sellOrderClient
from pprint import pprint


pprint(sellOrderClient.sellorder_new(payment_outlet='allbank_INSTAPAY', currency='PHP', base_amount='120', bank_account_number='55555555', bank_account_name='bankAccountName', recipient_phone_number='1234567890'))

pprint(sellOrderClient.sellorder_query(sell_order_id='1539200414090813441'))

pprint(sellOrderClient.validate_field(field_type='1', account_number='', account_type='', mobile_number='', region=''))

pprint(sellOrderClient.payout_outlets(outlet_category='', name='', region='PH', is_enabled='', id=''))

pprint(sellOrderClient.payout_outlet_fees(payment_outlet='alamanah_SWIFTPAY_PESONET', currency='PHP'))

pprint(sellOrderClient.payout_outlet_categories(id=''))
