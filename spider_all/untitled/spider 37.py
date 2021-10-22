'''
1.谷歌浏览器有道翻译-检查-network-all-输入单词-刷新一下-js-fan.min.js-preview即js加密代码
2.根据js代码查找 salt 的加密公式为 t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
3.根据js代码查找 sign 的加密公式为 n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
4.t 是盐，e是输入的单词，另外两个是固定的字符串
'''


def getSalt():
    import time, random
    salt = int(time.time()*1000) + random.randint(0,10)
    return salt


def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign


def getSign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "sr_3(QOHT)L2dx#uuGR@r"
    sign = getMD5(sign)
    return sign


from urllib import request, parse


def spider_youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()

    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key,salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN, zh;q=0.9, en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|;OUTFOX_SEARCH_USER_ID=447844113@115.197.110.97;JSESSIONID=abcXyuC1AfgJt_ZkLaICw;OUTFOX_SEARCH_USER_ID_NCOO=716581220.0966018;___rl__test__cookies=1542529457145",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0(Macintosh;Intel Mac OS X 10_13_6) AppleWebKit/537.36(KHTML, likeGecko) Chrome/70.0.3538.102 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)


if __name__ == "__main__":

    spider_youdao("deliver")

