import requests

url = "http://www.baidu.com"
rsp = requests.get(url)

print(rsp.text)
