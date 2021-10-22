import requests

url = "http://www.baidu.com/s?"
kw = {"wd": "王八蛋"}
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"}
rsp = requests.get(url, params=kw, headers=headers)

print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)
print(rsp.text)

