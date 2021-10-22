# urllib时
# 如果代理是SOCKS5类型的，则可以如下设置
import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '121.63.198.84', 6668)
socket.socket = socks.socksocket
try:
    response = requests.get('http://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print(e.args)

