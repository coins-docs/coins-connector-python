def invoices(self, amount='', currency='', supported_payment_collectors='', external_transaction_id='', expires_at=''):
    params = {}
    if amount:
        params['amount'] = amount
    if currency:
        params['currency'] = currency
    if supported_payment_collectors:
        params['supported_payment_collectors'] = supported_payment_collectors
    if external_transaction_id:
        params['external_transaction_id'] = external_transaction_id
    if expires_at:
        params['expires_at'] = expires_at
    return self._post('merchant-api/v1/invoices', signed=True, data=params)


def get_invoices(self, invoice_id='', start_time='', end_time='', limit=''):
    params = {}
    if invoice_id:
        params['invoice_id'] = invoice_id
    if start_time:
        params['start_time'] = start_time
    if end_time:
        params['end_time'] = end_time
    if limit:
        params['limit'] = limit
    return self._get('merchant-api/v1/get-invoices', signed=True, params=params)


def invoices_cancel(self, invoice_id=''):
    params = {}
    if invoice_id:
        params['invoice_id'] = invoice_id
    return self._post('merchant-api/v1/invoices-cancel', signed=True, data=params)
