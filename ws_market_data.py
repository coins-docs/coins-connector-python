#!/usr/bin/env python3
# coding: utf-8

from common.websockets import sub_start

def handler(msg):
    print(msg)

sub_start(stream_name=['xrpphp@kline_1m'],handle_ws_data = handler)