def order_new(self, symbol='', side='', type='', time_in_force='', quantity='', quote_order_qty='', price='', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp='', stp_flag=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if side:
        params['side'] = side
    if type:
        params['type'] = type
    if time_in_force:
        params['timeInForce'] = time_in_force
    if quantity:
        params['quantity'] = quantity
    if quote_order_qty:
        params['quoteOrderQty'] = quote_order_qty
    if price:
        params['price'] = price
    if new_client_order_id:
        params['newClientOrderId'] = new_client_order_id
    if stop_price:
        params['stopPrice'] = stop_price
    if new_order_resp_type:
        params['newOrderRespType'] = new_order_resp_type
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    if stp_flag:
        params['stpFlag'] = stp_flag
    return self._post('openapi/v1/order', signed=True, data=params)


def order_cancel_replace(self, symbol='', side='', type='', time_in_force='', quantity='', quote_order_qty='', price='', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp='', stp_flag='',
                         cancelOrderId='', cancelReplaceMode='', cancelRestrictions='', cancelOrigClientOrderId=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if side:
        params['side'] = side
    if type:
        params['type'] = type
    if time_in_force:
        params['timeInForce'] = time_in_force
    if quantity:
        params['quantity'] = quantity
    if quote_order_qty:
        params['quoteOrderQty'] = quote_order_qty
    if price:
        params['price'] = price
    if new_client_order_id:
        params['newClientOrderId'] = new_client_order_id
    if stop_price:
        params['stopPrice'] = stop_price
    if new_order_resp_type:
        params['newOrderRespType'] = new_order_resp_type
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    if stp_flag:
        params['stpFlag'] = stp_flag
    if cancelOrderId:
        params['cancelOrderId'] = cancelOrderId
    if cancelReplaceMode:
        params['cancelReplaceMode'] = cancelReplaceMode
    if cancelRestrictions:
        params['cancelRestrictions'] = cancelRestrictions
    if cancelOrigClientOrderId:
        params['cancelOrigClientOrderId'] = cancelOrigClientOrderId
    return self._post('openapi/v1/order/cancelReplace', signed=True, data=params)


def order_test(self, symbol='', side='', type='', time_in_force='', quantity='', quote_order_qty='', price='', new_client_order_id='', stop_price='', new_order_resp_type='', recv_window='', timestamp='', stp_flag=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if side:
        params['side'] = side
    if type:
        params['type'] = type
    if time_in_force:
        params['timeInForce'] = time_in_force
    if quantity:
        params['quantity'] = quantity
    if quote_order_qty:
        params['quoteOrderQty'] = quote_order_qty
    if price:
        params['price'] = price
    if new_client_order_id:
        params['newClientOrderId'] = new_client_order_id
    if stop_price:
        params['stopPrice'] = stop_price
    if new_order_resp_type:
        params['newOrderRespType'] = new_order_resp_type
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    if stp_flag:
        params['stpFlag'] = stp_flag
    return self._post('openapi/v1/order/test', signed=True, data=params)


def order_detail(self, order_id='', orig_client_order_id='', recv_window='', timestamp=''):
    params = {}
    if order_id:
        params['orderId'] = order_id
    if orig_client_order_id:
        params['origClientOrderId'] = orig_client_order_id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/order', signed=True, params=params)


def order_cancel(self, order_id='', orig_client_order_id='', recv_window='', timestamp=''):
    params = {}
    if order_id:
        params['orderId'] = order_id
    if orig_client_order_id:
        params['origClientOrderId'] = orig_client_order_id
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._delete('openapi/v1/order', signed=True, params=params)


def order_cancel_all(self, symbol='', recv_window='', timestamp=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._delete('openapi/v1/openOrders', signed=True, params=params)


def order_openorders(self, symbol='', recv_window='', timestamp=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/openOrders', signed=True, params=params)


def order_history(self, symbol='', order_id='', start_time='', end_time='', limit='', recv_window='', timestamp=''):
    params = {}
    if symbol:
        params['symbol'] = symbol
    if order_id:
        params['orderId'] = order_id
    if start_time:
        params['startTime'] = start_time
    if end_time:
        params['endTime'] = end_time
    if limit:
        params['limit'] = limit
    if recv_window:
        params['recvWindow'] = recv_window
    if timestamp:
        params['timestamp'] = timestamp
    return self._get('openapi/v1/historyOrders', signed=True, params=params)
