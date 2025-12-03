def subAccount_list(self, email='', page='', limit='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if email:
        params['email'] = email
    if page:
        params['page'] = page
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/list', signed=True, params=params)


def subAccount_create(self, account_name='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if account_name:
        params['accountName'] = account_name
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v1/sub-account/create', signed=True, data=params)


def subAccount_asset(self, email='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if email:
        params['email'] = email
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/asset', signed=True, params=params)


def subAccount_transfer_universal_transfer(self, from_email='', to_email='', client_tran_id='', asset='', amount='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if from_email:
        params['fromEmail'] = from_email
    if to_email:
        params['toEmail'] = to_email
    if client_tran_id:
        params['clientTranId'] = client_tran_id
    if asset:
        params['asset'] = asset
    if amount:
        params['amount'] = amount
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v1/sub-account/transfer/universal-transfer', signed=True, data=params)


def subAccount_transfer_sub_to_master(self, client_tran_id='', asset='', amount='', recv_window='', timestamp=''):
    'For Sub Account'
    params = {}
    if client_tran_id:
        params['clientTranId'] = client_tran_id
    if asset:
        params['asset'] = asset
    if amount:
        params['amount'] = amount
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v1/sub-account/transfer/sub-to-master', signed=True, data=params)


def subAccount_transfer_universal_transfer_history(self, from_email='', to_email='', client_tran_id='', token_id='', start_time='', end_time='', page='', limit='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if from_email:
        params['fromEmail'] = from_email
    if to_email:
        params['toEmail'] = to_email
    if client_tran_id:
        params['clientTranId'] = client_tran_id
    if token_id:
        params['tokenId'] = token_id
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if page:
        params['page'] = page
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/transfer/universal-transfer-history', signed=True, params=params)


def subAccount_transfer_sub_history(self, asset='', type='', start_time='', end_time='', page='', limit='', recv_window='', timestamp=''):
    'For Sub Account'
    params = {}
    if asset:
        params['asset'] = asset
    if type:
        params['type'] = type
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if page:
        params['page'] = page
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/transfer/sub-history', signed=True, params=params)


def subAccount_apikey_ip_restriction(self, apikey='', email='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if apikey:
        params['apikey'] = apikey
    if email:
        params['email'] = email
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/apikey/ip-restriction', signed=True, params=params)


def subAccount_apikey_add_ip_restriction(self, apikey='', email='', ip_address='', ip_restriction='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if apikey:
        params['apikey'] = apikey
    if email:
        params['email'] = email
    if ip_address:
        params['ipAddress'] = ip_address
    if ip_restriction:
        params['ipRestriction'] = ip_restriction
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v1/sub-account/apikey/add-ip-restriction', signed=True, data=params)


def subAccount_apikey_delete_ip_restriction(self, apikey='', email='', ip_address='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if apikey:
        params['apikey'] = apikey
    if email:
        params['email'] = email
    if ip_address:
        params['ipAddress'] = ip_address
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v1/sub-account/apikey/delete-ip-restriction', signed=True, data=params)


def collect_from_subaccount(self, client_request_id='', remark='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if client_request_id:
        params['clientRequestId'] = client_request_id
    if remark:
        params['remark'] = remark
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._post('openapi/v1/fund-collect/collect-from-sub-account', signed=True, data=params)


def get_fund_record(self, client_request_id='', page='', size='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if client_request_id:
        params['clientRequestId'] = client_request_id
    if page:
        params['page'] = page
    if size:
        params['size'] = size
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/fund-collect/get-fund-record', signed=True, params=params)


def wallet_deposit_address(self, email='', coin='', network='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if email:
        params['email'] = email
    if coin:
        params['coin'] = coin
    if network:
        params['network'] = network
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/wallet/deposit/address', signed=True, params=params)


def wallet_deposit_history(self, email='', coin='', tx_id='', deposit_id='', start_time='', end_time='', limit='', offset='', status='', recv_window='', timestamp=''):
    'For Master Account'
    params = {}
    if email:
        params['email'] = email
    if coin:
        params['coin'] = coin
    if tx_id:
        params['txId'] = tx_id
    if deposit_id:
        params['depositId'] = deposit_id
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if limit:
        params['limit'] = limit
    if offset:
        params['offset'] = offset
    if status:
        params['status'] = status
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/sub-account/wallet/deposit/history', signed=True, params=params)
