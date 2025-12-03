def depth(self, symbol='', limit=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if limit:
        params['limit'] = limit
    return self._get('openapi/quote/v1/depth', signed=False, params=params)


def trades(self, symbol='', limit=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if limit:
        params['limit'] = limit
    return self._get('openapi/quote/v1/trades', signed=False, params=params)


def klines(self, symbol='', interval='', strat_time='', end_time='', limit=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if interval:
        params['interval'] = interval
    if strat_time:
        params['startTime'] = strat_time
    if end_time:
        params['endTime'] = end_time
    if limit:
        params['limit'] = limit
    return self._get('openapi/quote/v1/klines', signed=False, params=params)


def avg_price(self, symbol=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    return self._get('openapi/quote/v1/avgPrice', signed=False, params=params)


def ticker_24hr(self, symbol='', symbols=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if symbols:
        params['symbols'] = symbols
    return self._get('openapi/quote/v1/ticker/24hr', signed=False, params=params)


def ticker_price(self, symbol='', symbols=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if symbols:
        params['symbols'] = symbols
    return self._get('openapi/quote/v1/ticker/price', signed=False, params=params)


def ticker_book_ticker(self, symbol='', symbols=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if symbols:
        params['symbols'] = symbols
    return self._get('openapi/quote/v1/ticker/bookTicker', signed=False, params=params)
