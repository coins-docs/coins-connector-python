def get_listen_key(self):
    params = {}
    return self._post('openapi/v1/userDataStream', signed=False, data=params)


def put_listen_key(self, listen_key=''):
    params = {}
    if listen_key:
        params['listenKey'] = listen_key
    return self._put('openapi/v1/userDataStream', signed=False, data=params)


def delete_listen_key(self, listen_key=''):
    params = {}
    if listen_key:
        params['listenKey'] = listen_key
    return self._delete('openapi/v1/userDataStream', signed=False, data=params)
