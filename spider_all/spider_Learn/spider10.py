from urllib import parse, request
from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email": "13119144223",
        "password": "123456"
    }
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    rsp = opener.open(req)


if __name__ == "__main__":
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
