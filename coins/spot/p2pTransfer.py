def p2p_transfer(self, account='', amount='', target_address='', client_transfer_id='', message='', recv_window='', timestamp=''):
    params = {}
    if account:
        params['account'] = account
    if amount:
        params['amount'] = amount
    if target_address:
        params['target_address'] = target_address
    if client_transfer_id:
        params['client_transfer_id'] = client_transfer_id
    if message:
        params['message'] = message
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/transfer/v3/transfers', signed=True, data=params)


def query_transfer(self, id='', client_transfer_id='', page='', per_page='', recv_window='', timestamp=''):
    path = 'openapi/transfer/v3/transfers'
    params = {}
    if id:
        path = path + "/{}".format(id)
    if client_transfer_id:
        params['client_transfer_id'] = client_transfer_id
    if page:
        params['page'] = page
    if per_page:
        params['per_page'] = per_page
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get(path, signed=True, params=params)


def crypto_accounts(self, currency='', recv_window='', timestamp=''):
    params = {}
    if currency:
        params['currency'] = currency
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/account/v3/crypto-accounts', signed=True, params=params)
