from coins.websocket.spot import client


client.partial_book_depth(symbol="BTCUSDT", level=10, speed='100')