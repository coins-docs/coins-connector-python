def ping(self):
    params = {}
    return self._get('openapi/v1/ping', signed=False, params=params)


def time(self):
    params = {}
    return self._get('openapi/v1/time', signed=False, params=params)


def exchange_info(self, symbol='', symbols=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if symbols:
        params['symbols'] = symbols
    return self._get('openapi/v1/exchangeInfo', signed=False, params=params)


def pairs(self):
    params = {}
    return self._get('openapi/v1/pairs', signed=False, params=params)


def user_ip(self):
    params = {}
    return self._get('openapi/v1/user/ip', signed=False, params=params)


def check_sys_status(self, business_type='', recv_window='', timestamp=''):
    params = {}
    if business_type:
        params['businessType'] = business_type
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/check-sys-status', signed=True, params=params)
