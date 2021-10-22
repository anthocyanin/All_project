from urllib import request, parse
from http import cookiejar

# 创建filecookiejar的实例
filename = "cookie2.txt"
cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)  # 创建请求管理器


def login():
    url = "http://www.renren.com/PLogin.do"
    data = {"email": "13119144223", "password": "123456"}
    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode())

    rsp = opener.open(req)  # 使用opener发起请求
    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == "__main__":
    login()


