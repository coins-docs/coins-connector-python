def get_supported_trading_pairs(self, recv_window='', timestamp=''):
    params = {}
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/convert/v1/get-supported-trading-pairs', signed=True, data=params)


def get_quote(self, source_currency='', target_currency='', source_amount='', recv_window='', timestamp=''):
    params = {}
    if source_currency:
        params['sourceCurrency'] = source_currency
    if target_currency:
        params['targetCurrency'] = target_currency
    if source_amount:
        params['sourceAmount'] = source_amount
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/convert/v1/get-quote', signed=True, data=params)


def accept_quote(self, quote_id='', recv_window='', timestamp=''):
    params = {}
    if quote_id:
        params['quoteId'] = quote_id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/convert/v1/accept-quote', signed=True, data=params)


def query_order_history(self, start_time='', end_time='', page='', size='', recv_window='', timestamp=''):
    params = {}
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if page:
        params['page'] = page
    if size:
        params['size'] = size
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/convert/v1/query-order-history', signed=True, data=params)
