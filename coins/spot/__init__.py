from coins.base import Request, OldRequest, MerchantRequest, FiatRequest
from coins.spot.invoice import invoices_cancel
from config.conf import cf


class Client(Request):

    def __init__(self, apikey=None, secret=None, **kwargs):
        if apikey is None:
            apikey = cf.api_key
        if secret is None:
            secret = cf.secret
        if "base_url" not in kwargs:
            kwargs["base_url"] = cf.rest_url
        super().__init__(kwargs["base_url"], apikey, secret, 
                        proxies=kwargs.get("proxies"))


    from coins.spot.spotTrading import order_new
    from coins.spot.spotTrading import order_cancel_replace
    from coins.spot.spotTrading import order_test
    from coins.spot.spotTrading import order_detail
    from coins.spot.spotTrading import order_cancel
    from coins.spot.spotTrading import order_cancel_all
    from coins.spot.spotTrading import order_openorders
    from coins.spot.spotTrading import order_history

    from coins.spot.account import account
    from coins.spot.account import my_trades
    from coins.spot.account import trade_fee
    from coins.spot.account import config_getall
    from coins.spot.account import withdraw_apply
    from coins.spot.account import deposit_history
    from coins.spot.account import withdraw_history
    from coins.spot.account import deposit_address
    from coins.spot.account import transaction_history
    from coins.spot.account import address_whitelist
    from coins.spot.account import api_keys

    from coins.spot.market import depth
    from coins.spot.market import trades
    from coins.spot.market import klines
    from coins.spot.market import avg_price
    from coins.spot.market import ticker_24hr
    from coins.spot.market import ticker_price
    from coins.spot.market import ticker_book_ticker

    from coins.spot.convert import get_supported_trading_pairs
    from coins.spot.convert import get_quote
    from coins.spot.convert import accept_quote
    from coins.spot.convert import query_order_history

    from coins.spot.listenKey import get_listen_key
    from coins.spot.listenKey import put_listen_key
    from coins.spot.listenKey import delete_listen_key

    from coins.spot.general import ping
    from coins.spot.general import time
    from coins.spot.general import exchange_info
    from coins.spot.general import pairs
    from coins.spot.general import user_ip
    from coins.spot.general import check_sys_status

    from coins.spot.p2pTransfer import p2p_transfer
    from coins.spot.p2pTransfer import query_transfer
    from coins.spot.p2pTransfer import crypto_accounts

    from coins.spot.subAccount import subAccount_list
    from coins.spot.subAccount import subAccount_create
    from coins.spot.subAccount import subAccount_asset
    from coins.spot.subAccount import subAccount_transfer_universal_transfer
    from coins.spot.subAccount import subAccount_transfer_sub_to_master
    from coins.spot.subAccount import subAccount_transfer_universal_transfer_history
    from coins.spot.subAccount import subAccount_transfer_sub_history
    from coins.spot.subAccount import subAccount_apikey_ip_restriction
    from coins.spot.subAccount import subAccount_apikey_add_ip_restriction
    from coins.spot.subAccount import subAccount_apikey_delete_ip_restriction
    from coins.spot.subAccount import collect_from_subaccount
    from coins.spot.subAccount import get_fund_record
    from coins.spot.subAccount import wallet_deposit_address
    from coins.spot.subAccount import wallet_deposit_history

    from coins.spot.payment import payment_request
    from coins.spot.payment import get_payment_request
    from coins.spot.payment import cancel_payment_request
    from coins.spot.payment import payment_request_reminder

    from coins.spot.fiat import fiat_support_channel
    from coins.spot.fiat import fiat_details
    from coins.spot.fiat import fiat_history_order
    from coins.spot.fiat import fiat_history_order_v2
    from coins.spot.fiat import generate_qr_code
    from coins.spot.fiat import generate_static_qr_code
    from coins.spot.fiat import cancel_qr_code
    from coins.spot.fiat import update_qr_code
    from coins.spot.fiat import get_qr_code
    from coins.spot.fiat import get_qr_code_static_list

    from coins.spot.sellOrder import sellorder_new
    from coins.spot.sellOrder import sellorder_query
    from coins.spot.sellOrder import validate_field
    from coins.spot.sellOrder import payout_outlets
    from coins.spot.sellOrder import payout_outlet_categories
    from coins.spot.sellOrder import payout_outlet_fees

    from coins.spot.invoice import invoices
    from coins.spot.invoice import get_invoices
    from coins.spot.invoice import invoices_cancel


class OldClient(OldRequest):

    def __init__(self, apikey=None, secret=None, **kwargs):
        if apikey is None:
            apikey = cf.api_key
        if secret is None:
            secret = cf.secret
        if "base_url" not in kwargs:
            kwargs["base_url"] = cf.rest_url
        super().__init__(kwargs["base_url"], apikey, secret, 
                        proxies=kwargs.get("proxies"))


    from coins.spot.sellOrder import sellorder_new
    from coins.spot.sellOrder import sellorder_query
    from coins.spot.sellOrder import validate_field
    from coins.spot.sellOrder import payout_outlets
    from coins.spot.sellOrder import payout_outlet_categories
    from coins.spot.sellOrder import payout_outlet_fees


class MerchantClient(MerchantRequest):

    def __init__(self, invoice_key=None, invoice_secret=None, **kwargs):
        if invoice_key is None:
            invoice_key = cf.invoice_key
        if invoice_secret is None:
            invoice_secret = cf.invoice_secret
        if "base_url" not in kwargs:
            kwargs["base_url"] = cf.rest_url
        super().__init__(kwargs["base_url"], invoice_key, invoice_secret, 
                        proxies=kwargs.get("proxies"))

    from coins.spot.invoice import invoices
    from coins.spot.invoice import get_invoices
    from coins.spot.invoice import invoices_cancel


class FiatClient(FiatRequest):

    def __init__(self, apikey=None, secret=None, **kwargs):
        if apikey is None:
            apikey = cf.api_key
        if secret is None:
            secret = cf.secret
        if "base_url" not in kwargs:
            kwargs["base_url"] = cf.rest_url
        super().__init__(kwargs["base_url"], apikey, secret, 
                        proxies=kwargs.get("proxies"))

    from coins.spot.fiat import fiat_cash_out
    from coins.spot.fiat import fiat_history_order_v2
    from coins.spot.fiat import generate_static_qr_code
    from coins.spot.fiat import cancel_qr_code
    from coins.spot.fiat import update_qr_code
    from coins.spot.fiat import get_qr_code_static_list



clent = Client()
sellOrderClient = OldClient()
invoiceClient = MerchantClient()
fiatClient = FiatClient()
