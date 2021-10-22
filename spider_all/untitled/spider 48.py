from urllib import request, parse
from http import cookiejar
import time
#
# # 创建cookiejar实例对象
# cookie = cookiejar.CookieJar()
#
# # 根据创建的cookie生成cookie的管理器
# cookie_handle = request.HTTPCookieProcessor(cookie)
#
# # 创建http请求管理器
# http_handle = request.HTTPHandler()
#
# # 创建https管理器
# https_handle = request.HTTPSHandler()
#
# # 创建求求管理器，将上面3个管理器作为参数属性
# # 有了opener，就可以替代urlopen来获取请求了
# opener = request.build_opener(http_handle, https_handle, cookie_handle)

filename = "cookie3.txt"
cookie = cookiejar.MozillaCookieJar(filename)
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)  # 创建请求管理器


def login():
    '''
    负责初次登录
    需要传递用户名和密码，来获取登录的cookie凭证
    '''
    # 登录url，需要从登录form的action属性中获取
    url = 'http://www.renren.com/PLogin.do'

    # 登录所需要的数据，数据为字典形式，
    # 此键值需要从form扁担中对应的input的name属性中获取
    data = {
        'email': '13119144223',
        'password': '123456'
    }

    # 将数据解析成urlencode格式
    data = parse.urlencode(data).encode()

    req = request.Request(url=url, data=data)

    # 正常是用request.urlopen(),这里用opener.open()发起请求
    response = opener.open(req)


def getHomePage():
    '''
    获取登录后的页面
    '''

    # 此url是登录后的链接地址
    url = 'http://www.renren.com/965187997/profile'

    # 如果已经执行了上面的login函数，
    # 那么此时的opener已经是包含了cookie信息的一个opener对象
    res = opener.open(url)

    html = res.read().decode()

    with open('renren.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    '''
    依次执行上面两个函数
    '''
    login()
    time.sleep(5)
    getHomePage()
