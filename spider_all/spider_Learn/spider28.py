# urllib 代理设置学习
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '221.235.239.55.9999'
# 如果遇到需要认证的代理，则只需在代理地址前面加上username：password@即可
# 示例如下 proxy='tutu:123abc@127.0.1.1.9999'

proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
})
opener = build_opener(proxy_handler)

try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

