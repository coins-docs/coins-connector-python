#!/usr/bin/env python3
# coding: utf-8

from common.client import userClient as user
from pprint import pprint

pprint(user.get_listen_key())

pprint(user.put_listen_key(listen_key='yhdKWoBFKbyTVMcccPNMIYBCsEYrCirwCKravbmARZmpgDoJKdWEGOXOpMypxjMW'))

pprint(user.delete_listen_key(listen_key='yhdKWoBFKbyTVMcccPNMIYBCsEYrCirwCKravbmARZmpgDoJKdWEGOXOpMypxjMW'))
