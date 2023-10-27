# !/usr/bin/env python
import asyncio
import websockets
import json
from config.conf import cf as conf
from common.client import userClient as user

async def subscribe(url,subs, callback=None):
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps(subs))
        while True:
            message = json.loads(await websocket.recv())
            print(message)


async def user_data_subscribe(url,callback=None):
    async with websockets.connect(url) as websocket:
        while True:
            message = json.loads(await websocket.recv())
            print(message)


async def handle_ws_data(*args, **kwargs):
    print(*args, **kwargs)



def sub_start(method='SUBSCRIBE', stream_name = '',handle_ws_data = ''):
    url = conf.stream_url + "/ws"
    message = {
                  "method": method,
                  "params": stream_name,
                  "id": 1
                }
    asyncio.get_event_loop().run_until_complete(subscribe(url, message,callback= handle_ws_data))


def user_data_stream(handle_ws_data):
    listenKey = user.get_listen_key()['listenKey']
    url = conf.stream_url + '/openapi/ws/' + listenKey
    asyncio.get_event_loop().run_until_complete(user_data_subscribe(url, callback=handle_ws_data))