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
    # rest_url = 'https://api.pro.coins.ph'
    # stream_url = "wss://wsapi.pro.coins.ph"
    rest_url = 'https://api.9001.pl-qa.coinsxyz.me'
    stream_url = 'wss://ws.9001.pl-qa.coinsxyz.me'
    invoice_key = '05HNAlJ6cnDyjwbjg8NKZZnw3yF0ZIzR6iV7XcGw4QJwUZ9fPQ9MPOGlyC5qDpYt'
    invoice_secret = 'iqTo2mQm0yHGpKy0xsGe75qDeOkqAnKJW04lVhHei7OdcKl1c9TYsBaWePelW4LK'
    api_key = 'VGkCt1GWUqWsxsCtsTvqLP7xNxOikd6wd7uPbnMIk8RUHQZ2bNd4Gcmq6NgQ6VlK'
    secret = '6AWutFs6ulhj8h1l51wnIt1efLVi13TE9SaHE4p76ovHbHWt782FPJMy7UgGxH1l'



class account2Config(Config):
    # rest_url = 'https://api.pro.coins.ph'
    # stream_url = "wss://wsapi.pro.coins.ph"
    rest_url = 'https://api.9001.pl-qa.coinsxyz.me'
    stream_url = 'wss://ws.9001.pl-qa.coinsxyz.me'
    invoice_key = '05HNAlJ6cnDyjwbjg8NKZZnw3yF0ZIzR6iV7XcGw4QJwUZ9fPQ9MPOGlyC5qDpYt'
    invoice_secret = 'iqTo2mQm0yHGpKy0xsGe75qDeOkqAnKJW04lVhHei7OdcKl1c9TYsBaWePelW4LK'
    api_key = 'imEAQ5immThbsBSAwa7jKnnkoUPr9b9X334AVe3UeGqMai2UReBWVvdWXht4VGMq'
    secret = 'Fq0RFogBOARozOAuD9hp251biyhqXihFnJoNNntHrDJ2fuhRwv5lZQ04ua7lYCzl'




mapping = {
                'account1': account1Config,
                'account2': account2Config
            }


APP_ENV = os.environ.get('APP_ENV', 'account1').lower()
cf = mapping[APP_ENV]()


APP_ENV2 = os.environ.get('APP_ENV2', 'account2').lower()
cf2 = mapping[APP_ENV2]()






