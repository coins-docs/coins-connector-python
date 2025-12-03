from coins.spot import invoiceClient
from pprint import pprint

pprint(invoiceClient.invoices(amount='123', currency='PHP', supported_payment_collectors='["coins_peso_wallet"]', external_transaction_id='454545', expires_at=''))

pprint(invoiceClient.get_invoices(invoice_id='1539174220746990336', start_time='', end_time='', limit=''))

pprint(invoiceClient.invoices_cancel(invoice_id='1539174220746990336'))
