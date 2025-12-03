def fiat_support_channel(self, transaction_type='', currency=''):
    params = {}
    if transaction_type:
        params['transactionType'] = transaction_type
    if currency:
        params['currency'] = currency
    return self._post('openapi/fiat/v1/support-channel', signed=True, data=params)


def fiat_cash_out(self, data=''):
    params = {}
    if data:
        params = data
    return self._post('openapi/fiat/v1/cash-out', signed=True, data=params)


def fiat_details(self, internal_order_id=''):
    params = {}
    if internal_order_id:
        params['internalOrderId'] = internal_order_id
    return self._get('openapi/fiat/v1/details', signed=True, params=params)


def fiat_history_order(self, page_num='', page_size='', internal_order_id='', transaction_type='', transaction_channel='', transaction_subject='', status='', fiat_currency='', start_date='', end_date=''):
    params = {}
    if page_num:
        params['pageNum'] = page_num
    if page_size:
        params['pageSize'] = page_size
    if internal_order_id:
        params['internalOrderId'] = internal_order_id
    if transaction_type:
        params['transactionType'] = transaction_type
    if transaction_channel:
        params['transactionChannel'] = transaction_channel
    if transaction_subject:
        params['transactionSubject'] = transaction_subject
    if status:
        params['status'] = status
    if fiat_currency:
        params['fiatCurrency'] = fiat_currency
    if start_date:
        params['startDate'] = start_date
    if end_date:
        params['endDate'] = end_date
    return self._post('openapi/fiat/v1/history', signed=True, data=params)


def generate_qr_code(self, requestId='', type='', source='', amount='', currency='', remark='', expiredSeconds='', qrCodeMerchantName=''):
    params = {}
    if requestId:
        params['requestId'] = requestId
    if type:
        params['type'] = type
    if source:
        params['source'] = source
    if amount:
        params['amount'] = amount
    if currency:
        params['currency'] = currency
    if remark:
        params['remark'] = remark
    if expiredSeconds:
        params['expiredSeconds'] = expiredSeconds
    if qrCodeMerchantName:
        params['qrCodeMerchantName'] = qrCodeMerchantName
    return self._post('openapi/fiat/v1/generate_qr_code', signed=True, data=params)


def get_qr_code(self, requestId=''):
    params = {}
    if requestId:
        params['requestId'] = requestId
    return self._get('openapi/fiat/v1/get_qr_code', signed=True, params=params)


def fiat_history_order_v2(self, page_num='', page_size='', external_order_id='', internal_order_id='', transaction_type='', transaction_channel='', transaction_subject='', status='', fiat_currency='', start_date='', end_date=''):
    params = {}
    if page_num:
        params['pageNum'] = page_num
    if page_size:
        params['pageSize'] = page_size
    if external_order_id:
        params['externalOrderId'] = external_order_id
    if internal_order_id:
        params['internalOrderId'] = internal_order_id
    if transaction_type:
        params['transactionType'] = transaction_type
    if transaction_channel:
        params['transactionChannel'] = transaction_channel
    if transaction_subject:
        params['transactionSubject'] = transaction_subject
    if status:
        params['status'] = status
    if fiat_currency:
        params['fiatCurrency'] = fiat_currency
    if start_date:
        params['startDate'] = start_date
    if end_date:
        params['endDate'] = end_date
    return self._post('openapi/fiat/v2/history', signed=True, data=params)


def generate_static_qr_code(self, request_id='', source='', currency='', remark='', qr_code_merchant_name='', sub_merchant_id='', recv_window='', timestamp=''):
    params = {}
    if request_id:
        params['requestId'] = request_id
    if source:
        params['source'] = source
    if currency:
        params['currency'] = currency
    if remark:
        params['remark'] = remark
    if qr_code_merchant_name:
        params['qrCodeMerchantName'] = qr_code_merchant_name
    if sub_merchant_id:
        params['subMerchantId'] = sub_merchant_id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/fiat/v1/generate/static/qr_code', signed=True, data=params)


def cancel_qr_code(self, reference_id='', recv_window='', timestamp=''):
    params = {}
    if reference_id:
        params['referenceId'] = reference_id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/fiat/v1/cancel_qr_code', signed=True, data=params)


def update_qr_code(self, request_id='', status='', recv_window='', timestamp=''):
    params = {}
    if request_id:
        params['requestId'] = request_id
    if status:
        params['status'] = status
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/fiat/v1/update/qr_code', signed=True, data=params)


def get_qr_code_static_list(self, status='', recv_window='', timestamp=''):
    params = {}
    if status:
        params['status'] = status
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/fiat/v1/get_qr_code/static/list', signed=True, params=params)
