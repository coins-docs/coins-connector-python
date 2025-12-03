def payment_request(self, payer_contact_info='', receiving_account='', amount='', message='', supported_payment_collectors='', expires_at='',recv_window='', timestamp=''):
    params = {}
    if payer_contact_info:
        params['payer_contact_info'] = payer_contact_info
    if receiving_account:
        params['receiving_account'] = receiving_account
    if amount:
        params['amount'] = amount
    if message:
        params['message'] = message
    if supported_payment_collectors:
        params['supported_payment_collectors'] = supported_payment_collectors
    if expires_at:
        params['expires_at'] = expires_at
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v3/payment-request/payment-requests', signed=True, data=params)


def get_payment_request(self, id='', start_time='', end_time='', limit='',recv_window='', timestamp=''):
    params = {}
    if id:
        params['id'] = id
    if start_time:
        params['start_time'] = start_time
    if end_time:
        params['end_time'] = end_time
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v3/payment-request/get-payment-request', signed=True, params=params)


def cancel_payment_request(self, id='',recv_window='', timestamp=''):
    params = {}
    if id:
        params['id'] = id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v3/payment-request/delete-payment-request', signed=True, data=params)


def payment_request_reminder(self, id='',recv_window='', timestamp=''):
    params = {}
    if id:
        params['id'] = id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v3/payment-request/payment-request-reminder', signed=True, data=params)
