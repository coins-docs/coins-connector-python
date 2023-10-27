#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from pprint import pprint

pprint(user.exchange_info(symbol='XRPPHP', symbols=[]))

pprint(user.pairs())

pprint(user.ping())

pprint(user.time())