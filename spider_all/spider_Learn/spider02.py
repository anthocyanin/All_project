# 批量代理爬取
from urllib import request, error
import random

# 1,设置代理池
proxy_list = [
    # 列表中存放的是dict类型元素
    {"http": "101.248.64.68:8080"},
    {"http": "114.249.112.246:9000"},
    {"http": "51.77.237.253:1080"},
    {"http": "211.24.102.170:80"},
    {"http": "188.93.246.34:8080"}
]

# 2，创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

# 3，创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)

url = 'http://www.baidu.com'

# 4，随即选取opener 并安装Opener
try:
    opener = random.choice(opener_list)
    request.install_opener(opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode('utf-8')
    print(html)

except error.URLError as e:
    print(e)
except Exception as g:
    print(g)




