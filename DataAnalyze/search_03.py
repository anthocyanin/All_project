import http.client
import json
from urllib.parse import quote_plus

base = '/search'


def geocode(address):
    path = '{}?q={}&format=json'.format(base, quote_plus(address))
    user_agent = b'Foundations of Python Network Programming example search3.py'
    headers = {b'User-Agent': user_agent}
    connection = http.client.HTTPSConnection('nominatim.openstreetmap.org')  # 建立连接
    connection.request('GET', path, None, headers)  # 发送请求
    rawreply = connection.getresponse().read()  # 接受响应，并读取
    reply = json.loads(rawreply.decode('utf-8'))  # 用json加载解码后的响应
    print(reply[0]['lat'], reply[0]['lon'])


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')
