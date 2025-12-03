#!/usr/bin/env python3
# coding: utf-8
# config
import os

class Config(object):  # default config
    DEBUG = False
    # get attribute
    def __getitem__(self, key):
        return self.__getattribute__(key)


# class account1Config(Config):
#     rest_url = 'https://api.pro.coins.ph'
#     stream_url = "wss://wsapi.pro.coins.ph"
#     invoice_key = ''
#     invoice_secret = ''
#     api_key = ''
#     secret = ''



class account1Config(Config):
    rest_url = 'https://api.9001.pl-qa.coinsxyz.me'
    stream_url = 'wss://ws.9001.pl-qa.coinsxyz.me'
    invoice_key = 'fqcjLq92alD91V9tmLQbvpnO8IcAYGyo9BI4YsV0IsmitrnFwm7Gh9DC1xoxbi41'
    invoice_secret = 'ryJvwV9nfqt5bzm76ESRredhaCCnuQh6jDtXAp20PlToZ8TM5xFoDr2ye8uWpH1r'
    api_key = 'VGkCt1GWUqWsxsCtsTvqLP7xNxOikd6wd7uPbnMIk8RUHQZ2bNd4Gcmq6NgQ6VlK'
    secret = '6AWutFs6ulhj8h1l51wnIt1efLVi13TE9SaHE4p76ovHbHWt782FPJMy7UgGxH1l'




mapping = {'user': account1Config}


APP_ENV = os.environ.get('APP_ENV', 'user').lower()
cf = mapping[APP_ENV]()







