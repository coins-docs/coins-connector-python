from coins.spot import clent
from pprint import pprint

pprint(clent.get_listen_key())

pprint(clent.put_listen_key(listen_key='IpSWGNyqZQXVGMKBoYKZgKmOYoxBzueuRlQCZwGceWxfIpvzuiFaGZppgzHbzNoA'))

pprint(clent.delete_listen_key(listen_key='IpSWGNyqZQXVGMKBoYKZgKmOYoxBzueuRlQCZwGceWxfIpvzuiFaGZppgzHbzNoA'))
