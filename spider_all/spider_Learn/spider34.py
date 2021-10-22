# requests 代理设置
# 其实就是在get请求时，传入参数proxies
import requests
proxy = '221.235.239.55.9999'
proxies = {
    'http': 'http://' + proxy,
    'http': 'https://' + proxy
}
try:
    response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print(e.args)
