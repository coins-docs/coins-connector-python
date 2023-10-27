#!/usr/bin/env python3
# coding: utf-8

from common.client import merchantClient as user
from pprint import pprint

pprint(user.invoices(amount='123', currency='PHP', supported_payment_collectors='["coins_peso_wallet"]', external_transaction_id='454545', expires_at=''))

pprint(user.get_invoices(invoice_id='1539174220746990336', start_time='', end_time='', limit=''))

pprint(user.invoices_cancel(invoice_id='1539174220746990336'))