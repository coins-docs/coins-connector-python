from coins.websocket.spot.websocket_client import SpotWebsocketClient


def message_handler(_, message):
    print(message)


client = SpotWebsocketClient(on_message=message_handler)
