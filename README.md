# Coins Connector Python

A lightweight Python library that works as a connector to the [Coins.ph](https://coins.ph) public API.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
  - [REST API Examples](#rest-api-examples)
  - [WebSocket Examples](#websocket-examples)
- [WebSocket Streams](#websocket-streams)
- [API Reference](#api-reference)
  - [REST API Methods](#rest-api-methods)
  - [WebSocket Methods](#websocket-methods)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Comprehensive REST API Coverage**: Support for spot trading, wallet operations, fiat transactions, and more
- **Real-time WebSocket Streams**: Live market data, order updates, and user account information
- **Easy to Use**: Simple and intuitive interface for both REST and WebSocket APIs
- **Type Safety**: Well-structured parameter handling
- **Flexible Configuration**: Multiple client types for different use cases
- **Extensive Examples**: Sample code for all major operations

## Installation

### Requirements

- Python 3.6 or higher
- `requests` library

### Install via pip

```bash
pip install requests
```

### Clone the Repository

```bash
git clone https://github.com/coins-docs/coins-connector-python.git
cd coins-connector-python
```

## Quick Start

1. **Configure your API credentials** in `config/conf.py`:

```python
class Config:
    # REST API configuration
    api_key = "your_api_key_here"
    secret = "your_secret_key_here"
    rest_url = "https://api.coins.ph/"
    
    # WebSocket configuration
    stream_url = "wss://wsapi.coins.ph"
    
    # For invoice operations
    invoice_key = "your_invoice_key_here"
    invoice_secret = "your_invoice_secret_here"
```

2. **Import and use the client**:

```python
from coins.spot import Client
import time

# Initialize client
client = Client()

# Get server time
response = client.time()
print(response)
```

## Authentication

### API Key Authentication

Most endpoints require API key authentication. You need to:

1. Create an API key from your Coins.ph account
2. Configure the key and secret in `config/conf.py`
3. The library automatically handles signature generation


## Usage Examples

### REST API Examples

#### Get Market Data

```python
from coins.spot import Client

client = Client()

# Get exchange information
response = client.exchange_info(symbol='BTCPHP')

# Get order book depth
response = client.depth(symbol='BTCPHP', limit=10)
```

#### Place an Order

```python
from coins.spot import Client
import time

client = Client()
timestamp = int(time.time() * 1000)

# Place a limit order
response = client.order_new(
    symbol='BTCPHP',
    side='buy',
    type='limit',
    time_in_force='GTC',
    quantity='0.001',
    price='2000000',
    timestamp=timestamp
)
```

#### Get Account Information

```python
from coins.spot import Client
import time

client = Client()
timestamp = int(time.time() * 1000)

# Get account balances
response = client.account(timestamp=timestamp)
```

### WebSocket Examples

#### Subscribe to Ticker Stream

```python
from coins.websocket.spot import client

# Subscribe to ticker updates for a symbol
client.ticker(symbol='BTCPHP')
```

#### Subscribe to Kline/Candlestick Stream

```python
from coins.websocket.spot import client

# Subscribe to kline updates (1 minute interval)
client.kline(symbol='BTCPHP', interval='1m')
```

#### Subscribe to User Data Stream

```python
from coins.websocket.spot import client as ws_client
from coins.spot import Client

# Get listen key for user data stream
rest_client = Client()
listen_key = rest_client.get_listen_key()['listenKey']

# Subscribe to user data (orders, balances, etc.)
ws_client.user_data(listen_key=listen_key)
```

For more examples, please refer to the `examples/` directory.

## WebSocket Streams

The library provides real-time WebSocket streams for market data and user account updates. All WebSocket connections are automatically managed, including reconnection on disconnect.

### Available Streams

#### Market Data Streams

- **Aggregate Trade Stream**: Real-time aggregated trade data
  ```python
  client.agg_trade(symbol='BTCPHP')
  ```

- **Trade Stream**: Raw trade information with unique buyer and seller
  ```python
  client.trade(symbol='BTCPHP')
  ```

- **Kline/Candlestick Stream**: Real-time candlestick updates
  ```python
  client.kline(symbol='BTCPHP', interval='1m')  # Intervals: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
  ```

- **Mini Ticker Stream**: 24hr rolling window mini-ticker statistics
  ```python
  client.mini_ticker(symbol='BTCPHP')  # Single symbol
  client.mini_ticker()  # All symbols
  ```

- **Ticker Stream**: 24hr rolling window ticker statistics
  ```python
  client.ticker(symbol='BTCPHP')  # Single symbol
  client.ticker()  # All symbols
  ```

- **Book Ticker Stream**: Best bid/ask price and quantity updates
  ```python
  client.book_ticker(symbol='BTCPHP')  # Single symbol
  client.book_ticker()  # All symbols
  ```

- **Partial Book Depth Stream**: Top bids and asks (5, 10, or 20 levels)
  ```python
  client.partial_book_depth(symbol='BTCPHP', level=5)  # 5, 10, or 20 levels
  client.partial_book_depth(symbol='BTCPHP', level=20, speed=100)  # With 100ms updates
  ```

- **Diff Book Depth Stream**: Order book depth updates for local management
  ```python
  client.diff_book_depth(symbol='BTCPHP')
  client.diff_book_depth(symbol='BTCPHP', speed=100)  # With 100ms updates
  ```

- **Mark Price Stream**: Mark price and funding rate updates
  ```python
  client.mark_price(symbol='BTCPHP')  # Single symbol
  client.mark_price()  # All symbols
  ```

#### User Data Stream

- **User Data Stream**: Real-time account updates (orders, balances, positions)
  ```python
  # First, get a listen key from REST API
  from coins.spot import Client
  rest_client = Client()
  listen_key = rest_client.get_listen_key()['listenKey']
  
  # Then subscribe to user data stream
  from coins.websocket.spot import client
  client.user_data(listen_key=listen_key)
  ```

- **All Orders Stream**: Real-time order updates for a symbol
  ```python
  client.all_order(symbol='BTCPHP')
  ```

### Custom Message Handler

You can provide a custom message handler to process incoming WebSocket messages:

```python
from coins.websocket.spot.websocket_client import SpotWebsocketClient
import json


def my_message_handler(ws, message):
    data = json.loads(message)
    print(f"Received: {data}")


# Create client with custom handler
ws_client = SpotWebsocketClient(on_message=my_message_handler)
ws_client.ticker(symbol='BTCPHP')
```

## API Reference

### REST API Methods

#### Market Data
- `ping()` - Test connectivity
- `time()` - Get server time
- `exchange_info()` - Get exchange information
- `pairs()` - Get all trading pairs
- `depth()` - Get order book depth
- `trades()` - Get recent trades
- `klines()` - Get kline/candlestick data
- `avg_price()` - Get average price
- `ticker_24hr()` - Get 24hr ticker statistics
- `ticker_price()` - Get ticker price
- `ticker_book_ticker()` - Get best price/qty on the order book

#### Trading
- `order_new()` - Place a new order
- `order_test()` - Test order placement
- `order_detail()` - Query order
- `order_cancel()` - Cancel order
- `order_cancel_all()` - Cancel all open orders
- `order_openorders()` - Get open orders
- `order_history()` - Get order history
- `order_cancel_replace()` - Cancel and replace order
- `my_trades()` - Get trade history
- `trade_fee()` - Get trading fee

#### Wallet
- `account()` - Get account information
- `deposit_address()` - Get deposit address
- `deposit_history()` - Get deposit history
- `withdraw_apply()` - Submit withdrawal
- `withdraw_history()` - Get withdrawal history
- `transaction_history()` - Get transaction history
- `address_whitelist()` - Get withdrawal address whitelist
- `api_keys()` - Get API keys information
- `config_getall()` - Get wallet configuration

#### Sub-Account
- `subAccount_create()` - Create sub-account
- `subAccount_list()` - Get sub-account list
- `subAccount_asset()` - Get sub-account assets
- `subAccount_transfer_universal_transfer()` - Universal transfer
- `subAccount_transfer_sub_to_master()` - Sub-account to master transfer
- `subAccount_transfer_universal_transfer_history()` - Get transfer history
- `subAccount_transfer_sub_history()` - Get sub-account transfer history
- `collect_from_subaccount()` - Collect funds from sub-accounts
- `get_fund_record()` - Get fund collection records
- `wallet_deposit_address()` - Get sub-account deposit address
- `wallet_deposit_history()` - Get sub-account deposit history

#### Fiat
- `fiat_support_channel()` - Get supported channels
- `fiat_details()` - Get transaction details
- `fiat_history_order()` - Get transaction history
- `fiat_history_order_v2()` - Get transaction history (V2)
- `generate_qr_code()` - Generate QR code
- `generate_static_qr_code()` - Generate static QR code
- `cancel_qr_code()` - Cancel QR code
- `update_qr_code()` - Update QR code
- `get_qr_code()` - Get QR code details
- `get_qr_code_static_list()` - Get static QR code list

#### Convert
- `get_supported_trading_pairs()` - Get supported pairs
- `get_quote()` - Get conversion quote
- `accept_quote()` - Accept quote
- `query_order_history()` - Query conversion history

#### P2P Transfer
- `crypto_accounts()` - Get crypto accounts
- `p2p_transfer()` - Execute P2P transfer
- `query_transfer()` - Query transfer

#### Payment
- `payment_request()` - Create payment request
- `get_payment_request()` - Get payment request
- `cancel_payment_request()` - Cancel payment request
- `payment_request_reminder()` - Send payment reminder

#### General
- `user_ip()` - Get user IP
- `check_sys_status()` - Check system status

### WebSocket Methods

#### SpotWebsocketClient

The `SpotWebsocketClient` class provides methods to subscribe to real-time data streams.

**Initialization Parameters:**
- `stream_url` - WebSocket stream URL (default from config)
- `on_message` - Callback function for incoming messages
- `on_open` - Callback function when connection opens
- `on_close` - Callback function when connection closes
- `on_error` - Callback function for errors
- `on_ping` - Callback function for ping frames
- `on_pong` - Callback function for pong frames
- `proxies` - Optional proxy configuration
- `max_reconnect_attempts` - Maximum reconnection attempts (default: 5)
- `reconnect_delay` - Delay between reconnection attempts in seconds (default: 5)

#### Market Data Methods

- `agg_trade(symbol, id=None, action=None)` - Subscribe to aggregate trade stream
- `trade(symbol, id=None, action=None)` - Subscribe to raw trade stream
- `kline(symbol, interval, id=None, action=None)` - Subscribe to kline/candlestick stream
  - Supported intervals: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
- `mini_ticker(symbol=None, id=None, action=None)` - Subscribe to mini ticker stream
  - If symbol is None or empty, subscribes to all symbols
- `ticker(symbol=None, id=None, action=None)` - Subscribe to ticker stream
  - If symbol is None or empty, subscribes to all symbols
- `book_ticker(symbol, id=None, action=None)` - Subscribe to book ticker stream
- `partial_book_depth(symbol, level=5, speed=None, id=None, action=None)` - Subscribe to partial book depth
  - Valid levels: 5, 10, 20
  - Optional speed: 100 (for 100ms updates)
- `diff_book_depth(symbol, speed=None, id=None, action=None)` - Subscribe to differential book depth
  - Optional speed: 100 (for 100ms updates)
- `mark_price(symbol, id=None, action=None)` - Subscribe to mark price stream
  - If symbol is None or empty, subscribes to all symbols
- `all_order(symbol, id=None, action=None)` - Subscribe to all orders stream for a symbol

#### User Data Methods

- `user_data(listen_key, id=None, action=None)` - Subscribe to user data stream
  - Requires a valid listen key obtained from REST API

#### Stream Management

Each subscription method supports optional parameters:
- `id` - Custom identifier for the subscription
- `action` - Action to perform (e.g., subscribe/unsubscribe)

## Error Handling

The library returns the raw API response. You should handle errors based on the response:

```python
from coins.spot import Client
import time

client = Client()
timestamp = int(time.time() * 1000)

response = client.order_new(
    symbol='BTCPHP',
    side='buy',
    type='limit',
    quantity='0.001',
    price='2000000',
    timestamp=timestamp
)

# Check for errors
if isinstance(response, dict):
    if 'code' in response and response['code'] != 200:
        print(f"Error: {response.get('msg', 'Unknown error')}")
    else:
        print("Success:", response)
else:
    print("Response:", response)
```

### Common Error Codes

- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (invalid API key or signature)
- `403` - Forbidden (IP restriction or insufficient permissions)
- `429` - Too Many Requests (rate limit exceeded)
- `500` - Internal Server Error

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/coins-docs/coins-connector-python).

For API documentation, visit [Coins API Documentation](https://docs.coins.ph/rest-api).
