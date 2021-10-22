# 阿布云使用示例
import requests

url = 'http://httpbin.org/get'
# 代理服务器
proxy_host = 'proxy.abuyun.com'
proxy_port = '9020'
# 代理隧道验证信息
proxy_user = 'H01234567890123D'
proxy_pass = '0123456789012345'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass
}
proxies = {
    'http': proxy_meta,
    'https': proxy_meta
}
response = requests.get(url, proxies=proxies)
print(response.status_code)
print(response.text)
