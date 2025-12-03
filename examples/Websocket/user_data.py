from coins.websocket.spot import client as userclient
from coins.spot import clent


listen_key = clent.get_listen_key()['listenKey']

userclient.user_data(listen_key=listen_key)