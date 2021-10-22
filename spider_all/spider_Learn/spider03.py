from urllib import request, parse
import ssl
from http import cookiejar

ssl._create_default_https_context = ssl._create_unverified_context


cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = "https://security.kaixin001.com/login/login_post.php"
    data = {
        "email": "18867144948",
        "password": "123qwe"
    }
    data = parse.urlencode(data)
    headers = {
        "Content-Length": len(data),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    }

    req = request.Request(url, data=data.encode(), headers=headers)
    rsp = opener.open(req)
    html = rsp.read().decode()
    print(html)


if __name__ == "__main__":
    login()
