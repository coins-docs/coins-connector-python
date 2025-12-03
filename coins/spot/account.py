def account(self, recv_window='', timestamp=''):
    params = {}
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/account', signed=True, params=params)


def my_trades(self, symbol='', order_id='', start_time='', end_time='', from_id='', limit='', recv_window='', timestamp=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if order_id:
        params['orderId'] = order_id
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if from_id:
        params['fromId'] = from_id
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/myTrades', signed=True, params=params)


def trade_fee(self, symbol='', recv_window='', timestamp=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/asset/tradeFee', signed=True, params=params)


def config_getall(self, recv_window='', timestamp=''):
    params = {}
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/wallet/v1/config/getall', signed=True, params=params)


def withdraw_apply(self, coin='', network='', address='', address_tag='', amount='', withdraw_order_id='', recv_window='', timestamp=''):
    params = {}
    if coin:
        params['coin'] = coin
    if network:
        params['network'] = network
    if address:
        params['address'] = address
    if address_tag:
        params['addressTag'] = address_tag
    if amount:
        params['amount'] = amount
    if withdraw_order_id:
        params['withdrawOrderId'] = withdraw_order_id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/wallet/v1/withdraw/apply', signed=True, data=params)


def deposit_history(self, coin='', tx_id='', status='', start_time='', end_time='', offset='', limit='', recv_window='', timestamp=''):
    params = {}
    if coin:
        params['coin'] = coin
    if tx_id:
        params['txId'] = tx_id
    if status:
        params['status'] = status
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if offset:
        params['offset'] = offset
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/wallet/v1/deposit/history', signed=True, params=params)


def withdraw_history(self, coin='', withdraw_order_id='', status='', start_time='', end_time='', offset='', limit='', recv_window='', timestamp=''):
    params = {}
    if coin:
        params['coin'] = coin
    if withdraw_order_id:
        params['withdrawOrderId'] = withdraw_order_id
    if status:
        params['status'] = status
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if offset:
        params['offset'] = offset
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/wallet/v1/withdraw/history', signed=True, params=params)


def deposit_address(self, coin='', network='', recv_window='', timestamp=''):
    params = {}
    if coin:
        params['coin'] = coin
    if network:
        params['network'] = network
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/wallet/v1/deposit/address', signed=True, params=params)


def transaction_history(self, token_id='', start_time='', end_time='', sub_user_id='', page_num='', page_size='', recv_window='', timestamp=''):
    params = {}
    if token_id:
        params['tokenId'] = token_id
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if sub_user_id:
        params['subUserId'] = sub_user_id
    if page_num:
        params['pageNum'] = page_num
    if page_size:
        params['pageSize'] = page_size
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/asset/transaction/history', signed=True, params=params)


def address_whitelist(self, coin='', network='', address='', recv_window='', timestamp=''):
    params = {}
    if coin:
        params['coin'] = coin
    if network:
        params['network'] = network
    if address:
        params['address'] = address
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/wallet/v1/withdraw/address-whitelist', signed=True, params=params)


def api_keys(self, recv_window='', timestamp=''):
    params = {}
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/api-keys', signed=True, params=params)
