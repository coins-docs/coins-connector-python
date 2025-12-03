import hashlib
import hmac
import json
import time
import urllib
import requests
from requests.adapters import HTTPAdapter


class Request(object):
    _session = None

    def __init__(self, entry_point, api_key="", secret="", proxies=None):

        if not entry_point.endswith("/"):
            entry_point = entry_point + "/"
        self.api_key = api_key
        self.secret = secret
        self.entry_point = entry_point
        self.proxies = proxies
        # self.ping()

    @classmethod
    def init_connection_args(
        cls, pool_connections=16, pool_maxsize=16, max_retries=5, pool_block=False
    ):
        http_adapter = HTTPAdapter(
            pool_connections, pool_maxsize, max_retries, pool_block
        )
        cls._session = requests.Session()
        # cls._session.keep_alive = False
        cls._session.mount("https://", http_adapter)
        cls._session.mount("http://", http_adapter)

    def _generate_signature(self, data):
        params_str = urllib.parse.urlencode(data)
        params_str = urllib.parse.unquote(params_str)
        digest = hmac.new(
            self.secret.encode(encoding="UTF8"),
            params_str.encode(encoding="UTF8"),
            digestmod=hashlib.sha256,
        ).hexdigest()
        return digest

    def _create_api_uri(self, path):
        return self.entry_point + path

    def _get(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request("GET", uri, signed, **kwargs)

    def _post(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request("POST", uri, signed, **kwargs)

    def _put(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request("PUT", uri, signed, **kwargs)

    def _delete(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request("DELETE", uri, signed, **kwargs)

    def _request(self, method, uri, signed, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = 15

        date_type = "data" if method == "POST" else "params"
        if date_type not in kwargs:
            kwargs[date_type] = {}

        kwargs[date_type]["timestamp"] = int(time.time() * 1000)

        if signed:
            kwargs[date_type]["signature"] = self._generate_signature(kwargs[date_type])

        kwargs["headers"] = {
            "X-COINS-APIKEY": self.api_key,
        }
        if self._session is None:
            response = requests.request(method, uri, proxies=self.proxies, **kwargs)
        else:
            response = self._session.request(
                method, uri, proxies=self.proxies, **kwargs
            )
        return self._handle_response(response)

    @classmethod
    def _handle_response(cls, response):
        try:
            return response.json()
        except:
            return response.text

    def stream_keepalive(self, listen_key=""):
        """
        Keepalive user data stream (USER_STREAM)
        """
        params = {"listenKey": listen_key}
        return self._put("openapi/v1/userDataStream", signed=False, params=params)



class OldRequest(object):
    _session = None

    def __init__(self, entry_point, api_key='', secret='', proxies=None):

        if not entry_point.endswith('/'):
            entry_point = entry_point + '/'
        self.api_key = api_key
        self.secret = secret
        self.entry_point = entry_point
        self.proxies = proxies
        # self.ping()

    @classmethod
    def init_connection_args(cls, pool_connections=16, pool_maxsize=16, max_retries=5, pool_block=False):
        http_adapter = HTTPAdapter(pool_connections, pool_maxsize, max_retries, pool_block)
        cls._session = requests.Session()
        # cls._session.keep_alive = False
        cls._session.mount('https://', http_adapter)
        cls._session.mount('http://', http_adapter)

    def _generate_signature(self, timestamp, url, data,method):
        timestamp_str = timestamp
        if data != {}:
            if method == "POST":
                data_str = str(data)
                sign_str = timestamp_str + url + data_str
            else:
                params_str = urllib.parse.urlencode(data)
                params_str = urllib.parse.unquote(params_str)
                sign_str = timestamp_str + url + '?' + params_str
        else:
            sign_str = timestamp_str + url
        sign_str = sign_str.replace("'", '"', -1)
        sign_str = sign_str.replace(" ", "", -1)
        digest = hmac.new(self.secret.encode(encoding='UTF8'),
                          sign_str.encode(encoding='UTF8'),
                          digestmod=hashlib.sha256).hexdigest()
        return digest

    def _create_api_uri(self, path):
        return self.entry_point + path

    def _get(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request('GET', uri, signed, **kwargs)

    def _post(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request('POST', uri, signed, **kwargs)

    def _request(self, method, uri, signed, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 15

        date_type = 'data' if method == 'POST' else 'params'
        if date_type not in kwargs:
            kwargs[date_type] = {}

        timestamp = str(int(time.time() * 1000))[0:10]

        signature = self._generate_signature(timestamp, uri, kwargs[date_type],method)

        kwargs['headers'] = {
            'ACCESS-KEY': self.api_key,
            'ACCESS-SIGNATURE': signature,
            'ACCESS-NONCE': timestamp,
        }

        if method == "POST":
            kwargs['headers']['Content-Type'] = 'application/json'
            response = requests.post(url=uri,headers=kwargs['headers'],data=json.dumps(kwargs[date_type]))
        if method == "GET":
            if kwargs[date_type] != {}:
                response = requests.get(url=uri, headers=kwargs['headers'],params=kwargs[date_type])
            else:
                response = requests.get(url=uri, headers=kwargs['headers'])
        return self._handle_response(response)

    @classmethod
    def _handle_response(cls, response):
        try:
            return response.json()
        except:
            return response.text



class MerchantRequest(object):
    _session = None

    def __init__(self, entry_point, api_key='', secret='', proxies=None):

        if not entry_point.endswith('/'):
            entry_point = entry_point + '/'
        self.api_key = api_key
        self.secret = secret
        self.entry_point = entry_point
        self.proxies = proxies
        # self.ping()

    @classmethod
    def init_connection_args(cls, pool_connections=16, pool_maxsize=16, max_retries=5, pool_block=False):
        http_adapter = HTTPAdapter(pool_connections, pool_maxsize, max_retries, pool_block)
        cls._session = requests.Session()
        # cls._session.keep_alive = False
        cls._session.mount('https://', http_adapter)
        cls._session.mount('http://', http_adapter)

    def _generate_signature(self, timestamp, url, data, method):
        params_str = urllib.parse.urlencode(data)
        params_str = urllib.parse.unquote(params_str)
        if method == 'GET' and data != {}:
            signStr = str(timestamp) + url + '?' + params_str
        else:
            signStr = str(timestamp) + url + params_str
        digest = hmac.new(self.secret.encode(encoding='UTF8'),
                          signStr.encode(encoding='UTF8'),
                          digestmod=hashlib.sha256).hexdigest()
        return digest

    def _create_api_uri(self, path):
        return self.entry_point + path

    def _get(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request('GET', uri, signed, **kwargs)

    def _post(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request('POST', uri, signed, **kwargs)


    def _request(self, method, uri, signed, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 15

        date_type = 'data' if method == 'POST' else 'params'
        if date_type not in kwargs:
            kwargs[date_type] = {}

        timestamp = str(int(time.time() * 1000))

        signature = self._generate_signature(timestamp, uri, kwargs[date_type], method)

        kwargs['headers'] = {
            'X-Merchant-Key': self.api_key,
            'X-Merchant-Sign': signature,
            'X-Timestamp': timestamp
        }

        if self._session is None:
            response = requests.request(method, uri, proxies=self.proxies, **kwargs)
        else:
            response = self._session.request(method, uri, proxies=self.proxies, **kwargs)
        return self._handle_response(response)

    @classmethod
    def _handle_response(cls, response):
        try:
            return response.json()
        except:
            return response.text


class FiatRequest(object):
    _session = None

    def __init__(self, entry_point, api_key='', secret='', proxies=None):

        if not entry_point.endswith('/'):
            entry_point = entry_point + '/'
        self.api_key = api_key
        self.secret = secret
        self.entry_point = entry_point
        self.proxies = proxies
        # self.ping()

    @classmethod
    def init_connection_args(cls, pool_connections=16, pool_maxsize=16, max_retries=5, pool_block=False):
        http_adapter = HTTPAdapter(pool_connections, pool_maxsize, max_retries, pool_block)
        cls._session = requests.Session()
        # cls._session.keep_alive = False
        cls._session.mount('https://', http_adapter)
        cls._session.mount('http://', http_adapter)

    def _generate_signature(self, data):
        json_str = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
        digest = hmac.new(self.secret.encode(encoding='UTF8'),
                          json_str.encode(encoding='UTF8'),
                          digestmod=hashlib.sha256).hexdigest()
        return digest

    def _create_api_uri(self, path):
        return self.entry_point + path

    def _post(self, uri, signed=False, **kwargs):
        uri = self._create_api_uri(uri)
        return self._request('POST', uri, signed, **kwargs)

    def _request(self, method, uri, signed, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 15
        date_type = 'data' if method == 'POST' else 'params'
        if date_type not in kwargs:
            kwargs[date_type] = {}

        timestamp = str(int(time.time() * 1000))
        signature = self._generate_signature(kwargs[date_type])

        kwargs['headers'] = {
            'X-COINS-APIKEY': self.api_key,
            'timestamp': timestamp,
            'signature': signature,
            'Content-Type':'application/json',
        }
        response = requests.post(url=uri,headers=kwargs['headers'],data=json.dumps(kwargs[date_type]))
        return self._handle_response(response)


    @classmethod
    def _handle_response(cls, response):
        try:
            return response.json()
        except :
            return response.text

