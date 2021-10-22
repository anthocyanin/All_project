from urllib import request, parse, error
from http import cookiejar
import json


def login():
    url = "http://www.jobbole.com/wp-login.php"
    data = {
        "log": "augsnano",
        "pwd": "123456789",
        "wp-submit": "登录",
        "redirect_to": "http://date.jobbole.com/4965/",
        "rememberme": "on"
    }
    data = parse.urlencode(data).encode()

    f = r'jobbole_cookie.txt'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Connection": "keep-alive"
    }
    cookie_handler = cookiejar.MozillaCookieJar(f)
    http_handler = request.HTTPCookieProcessor(cookie_handler)

    opener = request.build_opener(http_handler)
    req = request.Request(url, data=data, headers=headers)
    try:
        rsp = opener.open(req)
        cookie_handler.save(f, ignore_discard=True, ignore_expires=True)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)


def getInfo():
    url = "http://date.jobbole.com/wp-admin/admin-ajax.php"

    f = r'jobbole_cookie.txt'
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(f, ignore_discard=True, ignore_expires=True)

    http_handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(http_handler)

    data = {
        "action": "get_date_contact",
        "postId": "4965"
    }
    data = parse.urlencode(data).encode()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
        "Connection": "keep-alive"
    }
    req = request.Request(url, data=data, headers=headers)

    try:
        rsp = opener.open(req)
        html = rsp.read().decode()
        html = json.loads(html)
        print(html)

        # fil = "rsp.html"
        # with open(fil, 'w') as f:
        #     f.write(html)

    except error.URLError as e:
        print(e)


if __name__ == '__main__':
    getInfo()

