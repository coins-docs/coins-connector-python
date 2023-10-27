#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from common.client import fiatClient as fiat
from pprint import pprint


pprint(user.fiat_support_channel(transaction_type='-1', currency='PHP'))

pprint(fiat.fiat_cash_out(data={"internalOrderId": "16810937322990",
                                "currency": "PHP",
                                "amount": "50",
                                "channelName": "SWIFTPAY_PESONET",
                                "channelSubject": "gcash",
                                "extendInfo": {"recipientName": "coins-open-api-test",
                                               "recipientAccountNumber": "123456789"}}))

pprint(user.fiat_details(internal_order_id='16810937322990'))

pprint(user.fiat_history_order(page_num='1', page_size='10', internal_order_id='', transaction_type='', transaction_channel='', transaction_subject='', status='', fiat_currency='', start_date='', end_date=''))
