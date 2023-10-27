#!/usr/bin/env python3
# coding: utf-8

from common.websockets import user_data_stream


def handler(msg):
    print(msg)


user_data_stream(handler)
