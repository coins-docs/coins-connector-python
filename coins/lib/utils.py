import time
from urllib.parse import urlencode, urlparse
from loguru import logger


def cleanNoneValue(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def get_timestamp():
    return int(time.time() * 1000)


def encoded_string(query, special=False):
    if special:
        return urlencode(query).replace("%40", "@").replace("%27", "%22")
    else:
        return urlencode(query, True).replace("%40", "@")


def config_logging(logging, logging_devel, log_file=None):
    logging.basicConfig(level=logging_devel, filename=log_file)

def parse_proxies(proxies: dict):
    """Parse proxy url from dict, only support http and https proxy, not support socks5 proxy"""
    proxy_url = proxies.get("http") or proxies.get("https")
    if not proxy_url:
        return {}

    parsed = urlparse(proxy_url)
    return {
        "http_proxy_host": parsed.hostname,
        "http_proxy_port": parsed.port,
        "http_proxy_auth": (parsed.username, parsed.password)
        if parsed.username and parsed.password
        else None,
    }