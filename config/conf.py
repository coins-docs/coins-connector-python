#!/usr/bin/env python3
# coding: utf-8
# config
import os

class Config(object):  # default config
    DEBUG = False
    # get attribute
    def __getitem__(self, key):
        return self.__getattribute__(key)


class account1Config(Config):
    rest_url = 'https://api.pro.coins.ph'
    stream_url = "wss://wsapi.pro.coins.ph"
    invoice_key = ''
    invoice_secret = ''
    api_key = ''
    secret = ''



mapping = {'user': account1Config}


APP_ENV = os.environ.get('APP_ENV', 'user').lower()
cf = mapping[APP_ENV]()







