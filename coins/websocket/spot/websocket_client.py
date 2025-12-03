from typing import Optional
from config.conf import cf
from coins.websocket.websocket_client import CoinsWebsocketClient


class SpotWebsocketClient(CoinsWebsocketClient):
    def __init__(
        self,
        stream_url=cf.stream_url,
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        user_data=False,
        proxies: Optional[dict] = None,
        max_reconnect_attempts=5,
        reconnect_delay=5,
    ):

        stream_url = stream_url + "/openapi/quote/stream"
        super().__init__(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            proxies=proxies,
            max_reconnect_attempts=max_reconnect_attempts,
            reconnect_delay=reconnect_delay,
        )
        # logger.info(stream_url)
    def agg_trade(self, symbol: str, id=None, action=None, **kwargs):
        """Aggregate Trade Streams

        The Aggregate Trade Streams push market trade information that is aggregated for a single taker order every 100 milliseconds.
        Only market trades will be aggregated, which means the insurance fund trades and ADL trades won't be aggregated.

        Stream Name: <symbol>@aggTrade

        Update Speed: 100ms
        """
        stream_name = "{}@aggTrade".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)

    def all_order(self, symbol: str, id=None, action=None, **kwargs):

        stream_name = "{}@all-order".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)



    def trade(self, symbol: str, id=None, action=None, **kwargs):
        """The Trade Streams push raw trade information; each trade has a unique buyer and seller.

        Stream Name: <symbol>@trade

        Update Speed: Real-time
        """

        stream_name = "{}@trade".format(symbol.lower())

        self.send_message_to_server(stream_name, action=action, id=id)


    def kline(self, symbol: str, interval: str, id=None, action=None, **kwargs):
        """Kline/Candlestick Streams

        The Kline/Candlestick Stream push updates to the current klines/candlestick every 250 milliseconds (if existing)

        Stream Name: <symbol>@kline_<interval>

        https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-streams

        interval:
        m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

        - 1m
        - 3m
        - 5m
        - 15m
        - 30m
        - 1h
        - 2h
        - 4h
        - 6h
        - 8h
        - 12h
        - 1d
        - 3d
        - 1w
        - 1M

        Update Speed: 2000ms
        """
        stream_name = "{}@kline_{}".format(symbol.lower(), interval)

        self.send_message_to_server(stream_name, action=action, id=id)


    def mini_ticker(self, symbol=None, id=None, action=None, **kwargs):
        """Individual symbol or all symbols mini ticker

        24hr rolling window mini-ticker statistics.
        These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs

        Stream Name: <symbol>@miniTicker or
        Stream Name: !miniTicker@arr

        Update Speed: 1000ms
        """

        if symbol is None or symbol == '':
            stream_name = "!miniTicker@arr"
        else:
            stream_name = "{}@miniTicker".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)

    def ticker(self, symbol=None, id=None, action=None, **kwargs):
        """Individual symbol or all symbols ticker

        24hr rolling window ticker statistics for a single symbol.
        These are NOT the statistics of the UTC day, but a 24hr rolling window from requestTime to 24hrs before.

        Stream Name: <symbol>@ticker or
        Stream Name: !ticker@arr
        Update Speed: 1000ms
        """

        if symbol is None or symbol == '':
            stream_name = "!ticker@arr"
        else:
            stream_name = "{}@ticker".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)

    def book_ticker(self, symbol, id=None, action=None, **kwargs):
        """Individual symbol or all book ticker

        Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

        Stream Name: <symbol>@bookTicker or
        Stream Name: !bookTicker

        Update Speed: Real-time
        """
        if symbol is None or symbol == '':
            stream_name = "!bookTicker"
        else:
            stream_name = "{}@bookTicker".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)

    def partial_book_depth(
        self, symbol: str, level=5, speed=None, id=None, action=None, **kwargs
    ):
        """Partial Book Depth Streams

        Top bids and asks, Valid are 5, 10, or 20.

        Stream Names: <symbol>@depth<levels> OR  <symbol>@depth<levels>@100ms

        Update Speed: 1000ms for 200 levels, 100ms for other levels when there's update
        """
        if speed is None or speed == '':
            stream_name = "{}@depth{}".format(symbol.lower(), level)
        else:
            stream_name = "{}@depth{}@{}ms".format(symbol.lower(), level, speed)



        self.send_message_to_server(stream_name, action=action, id=id)



    def diff_book_depth(self, symbol: str, speed=None, id=None, action=None, **kwargs):
        """Diff. Depth Stream
        Order book price and quantity depth updates used to locally manage an order book.

        Stream Name: <symbol>@depth  OR<symbol>@depth@100ms

        Update Speed: 1000ms for 200 levels, 100ms for other levels when there's update
        """

        if speed is None or speed == '':
            stream_name = "{}@depth".format(symbol.lower())
        else:
            stream_name = "{}@depth@{}ms".format(symbol.lower(), speed)


        self.send_message_to_server(stream_name, action=action, id=id)


    def mark_price(self, symbol: str, id=None, action=None, **kwargs):
        """Mark Price Streams

        Mark price and funding rate for all symbols pushed every 3 seconds or every second.

        Stream Name: <symbol>@markPrice or <symbol>@markPrice@1s

        https://binance-docs.github.io/apidocs/futures/en/#mark-price-stream

        Update Speed: 3000ms or 1000ms
        """

        if symbol is None or symbol == '':
            stream_name = "!markPrice@arr"
        else:
            stream_name = "{}@markPrice@1s".format(symbol.lower())
        self.send_message_to_server(stream_name, action=action, id=id)


    def user_data(self, listen_key: str, id=None, action=None, **kwargs):
        """Listen to user data by using the provided listen_key"""

        self.send_message_to_server(listen_key, action=action, id=id)
