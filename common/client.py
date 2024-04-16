from common.base import Request,OldRequest,MerchantRequest,FiatRequest
from config.conf import cf as conf
from config.conf import cf2 as conf2


class BrokerClient(Request):

    def order_new(self,symbol='',side='',type='',time_in_force='',quantity='',quote_order_qty='',price='',new_client_order_id='',stop_price='',new_order_resp_type='', recv_window='', timestamp='',stp_flag=''):
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


    def order_cancel_replace(self,symbol='',side='',type='',time_in_force='',quantity='',quote_order_qty='',price='',new_client_order_id='',stop_price='',new_order_resp_type='', recv_window='', timestamp='',stp_flag='',
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


    def order_test(self,symbol='',side='',type='',time_in_force='',quantity='',quote_order_qty='',price='',new_client_order_id='',stop_price='',new_order_resp_type='', recv_window='', timestamp='', stp_flag=''):
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


    def order_detail(self,order_id='',orig_client_order_id='', recv_window='', timestamp=''):
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


    def order_cancel(self,order_id='',orig_client_order_id='', recv_window='', timestamp=''):
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


    def order_cancel_all(self,symbol='', recv_window='', timestamp=''):
        params = {}
        if symbol:
            params['symbol'] = symbol
        if recv_window:
            params['recvWindow'] = recv_window
        if timestamp:
            params['timestamp'] = timestamp
        return self._delete('openapi/v1/openOrders', signed=True, params=params)



    def order_openorders(self,symbol='', recv_window='', timestamp=''):
        params = {}
        if symbol:
            params['symbol'] = symbol
        if recv_window:
            params['recvWindow'] = recv_window
        if timestamp:
            params['timestamp'] = timestamp
        return self._get('openapi/v1/openOrders', signed=True, params=params)


    def order_history(self,symbol='', order_id='', start_time='', end_time='', limit='', recv_window='', timestamp=''):
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


    def account(self, recv_window='', timestamp=''):
        params = {}
        if recv_window:
            params['recvWindow'] = recv_window
        if timestamp:
            params['timestamp'] = timestamp
        return self._get('openapi/v1/account', signed=True, params=params)


    def my_trades(self,symbol='', order_id='', start_time='', end_time='',from_id='', limit='', recv_window='', timestamp=''):
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


    def get_listen_key(self):
        params = {}
        return self._post('openapi/v1/userDataStream', signed=False, data=params)


    def put_listen_key(self,listen_key=''):
        params = {}
        if listen_key:
            params['listenKey'] = listen_key
        return self._put('openapi/v1/userDataStream', signed=False, data=params)


    def delete_listen_key(self,listen_key=''):
        params = {}
        if listen_key:
            params['listenKey'] = listen_key
        return self._delete('openapi/v1/userDataStream', signed=False, data=params)


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


    def query_order_history(self,  start_time='', end_time='', page='', size='', recv_window='', timestamp=''):
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


    def ping(self):
        params = {}
        return self._get('openapi/v1/ping', signed=False, params=params)


    def time(self):
        params = {}
        return self._get('openapi/v1/time', signed=False, params=params)


    def exchange_info(self,symbol='', symbols=''):
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


    def p2p_transfer(self, account='', amount='', target_address='', client_transfer_id = '',message='', recv_window='', timestamp=''):
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


    def query_transfer(self, id='',client_transfer_id='', page='', per_page='', recv_window='', timestamp=''):
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


    def deposit_address(self,coin='', network='', recv_window='', timestamp=''):
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


    def subAccount_list(self, email='', page='', limit='', recv_window='', timestamp=''):
        'For Master Account'
        params= {}
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
        params= {}
        if account_name:
            params['accountName'] = account_name
        if recv_window:
            params['recvWindow'] = recv_window
        if timestamp:
            params['timestamp'] = timestamp
        return self._post('openapi/v1/sub-account/create', signed=True, data=params)


    def subAccount_asset(self, email='', recv_window='', timestamp=''):
        'For Master Account'
        params= {}
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

    def payment_request(self,payer_contact_info='', receiving_account='', amount='', message='', supported_payment_collectors='', expires_at=''):
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
        return self._post('openapi/v3/payment-request/payment-requests', signed=True, data=params)


    def get_payment_request(self,id='', start_time='', end_time='', limit=''):
        params = {}
        if id:
            params['id'] = id
        if start_time:
            params['start_time'] = start_time
        if end_time:
            params['end_time'] = end_time
        if limit:
            params['limit'] = limit

        return self._get('openapi/v3/payment-request/get-payment-request', signed=True, params=params)


    def cancel_payment_request(self, id=''):
        params = {}
        if id:
            params['id'] = id
        return self._post('openapi/v3/payment-request/delete-payment-request', signed=True, data=params)


    def payment_request_reminder(self, id=''):
        params = {}
        if id:
            params['id'] = id
        return self._post('openapi/v3/payment-request/payment-request-reminder', signed=True, data=params)


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

    def fiat_history_order(self,page_num='', page_size='', internal_order_id='', transaction_type='', transaction_channel='', transaction_subject='', status='', fiat_currency='', start_date='', end_date=''):
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


    def generate_qr_code(self, requestId='', type='', source='', amount='', currency='',remark='',expiredSeconds='',qrCodeMerchantName=''):
        params = {}
        if requestId: params['requestId'] = requestId
        if type: params['type'] = type
        if source: params['source'] = source
        if amount: params['amount'] = amount
        if currency: params['currency'] = currency
        if remark: params['remark'] = remark
        if expiredSeconds: params['expiredSeconds'] = expiredSeconds
        if qrCodeMerchantName: params['qrCodeMerchantName'] = qrCodeMerchantName
        return self._post('openapi/fiat/v1/generate_qr_code', signed=True, data=params)

    def get_qr_code(self, requestId=''):
        params = {}
        if requestId: params['requestId'] = requestId
        return self._get('openapi/fiat/v1/get_qr_code', signed=True, params=params)


class OldClient(OldRequest):

    def sellorder_new(self, payment_outlet='', currency='', base_amount='', bank_account_number='', bank_account_name='', recipient_phone_number=''):
        params = {}
        if base_amount:
            params['base_amount'] = base_amount
        if currency:
            params['currency'] = currency
        if bank_account_number:
            params['bank_account_number'] = bank_account_number
        if bank_account_name:
            params['bank_account_name'] = bank_account_name
        if recipient_phone_number:
            params['recipient_phone_number'] = recipient_phone_number
        if payment_outlet:
            params['payment_outlet'] = payment_outlet

        return self._post('openapi/migration/v4/sellorder', signed=True, data=params)


    def sellorder_query(self, sell_order_id=''):
        params = {}
        path = 'openapi/migration/v4/sellorder'
        if sell_order_id:
            path = path + '/' + sell_order_id

        return self._get(path, signed=True, params=params)


    def validate_field(self, field_type='' , account_number='', account_type='', mobile_number='', region=''):
        params = {}
        if field_type:
            params['field_type'] = field_type
        if account_number:
            params['account_number'] = account_number
        if account_type:
            params['account_type'] = account_type
        if mobile_number:
            params['mobile_number'] = mobile_number
        if region:
            params['region'] = region

        return self._post('openapi/migration/v4/validate-field', signed=True, data=params)


    def payout_outlets(self, outlet_category='', name='', region='', is_enabled='', id=''):
        params = {}
        if outlet_category:
            params['outlet_category'] = outlet_category
        if name:
            params['name'] = name
        if region:
            params['region'] = region
        if is_enabled:
            params['is_enabled'] = is_enabled
        if id:
            params['id'] = id

        return self._get('openapi/migration/v4/payout-outlets', signed=True, params=params)


    def payout_outlet_categories(self, id=''):
        params = {}
        path = 'openapi/migration/v4/payout-outlet-categories'

        if id:
            path = path + '/' + id

        return self._get(path, signed=True, params=params)


    def payout_outlet_fees(self, payment_outlet='', currency=''):
        params = {}
        if payment_outlet:
            params['payment_outlet'] = payment_outlet
        if currency:
            params['currency'] = currency
        return self._get('openapi/migration/v4/payout-outlet-fees', signed=True, params=params)

class MerchantClient(MerchantRequest):


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



class FiatClient(FiatRequest):

    def fiat_cash_out(self, data=''):
        params = {}
        if data:
            params = data
        return self._post('openapi/fiat/v1/cash-out', signed=True, data=params)



userClient = BrokerClient(entry_point=conf.rest_url, api_key=conf.api_key, secret=conf.secret)
merchantClient = MerchantClient(entry_point=conf.rest_url, api_key=conf.invoice_key, secret=conf.invoice_secret)
oldClinet = OldClient(entry_point=conf.rest_url, api_key=conf.api_key, secret=conf.secret)
fiatClient = FiatClient(entry_point=conf.rest_url, api_key=conf.api_key, secret=conf.secret)
userClient2 = BrokerClient(entry_point=conf2.rest_url, api_key=conf2.api_key, secret=conf2.secret)

