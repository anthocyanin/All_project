from selenium import webdriver
import time
import pickle
from http import cookiejar
from urllib import request


def get_cookies():
    usname = '18867144948'
    password = 'anthocyanin'
    brower = webdriver.Chrome()
    try:
        brower.get("https://www.zhihu.com/signin")  # 进入登录界面
        brower.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input[name='username']").send_keys(usname)
        brower.find_element_by_css_selector(".SignFlow-password .Input-wrapper input[name='password']").send_keys(password)
        brower.find_element_by_css_selector(".Button.SignFlow-submitButton.Button--primary.Button--blue").click()
        time.sleep(10)  # 登录成功后自动跳转到首页，可以获取浏览cookies，验证已登录

        Cookies = brower.get_cookies()  # 获取cookies

        cookie_dict = {}

        for cookie in Cookies:
            cookie_dict[cookie["name"]] = cookie["value"]
        # 写入文件
        f = open('zhihu_cookies.txt', 'wb')
        pickle.dump(cookie_dict, f)
        f.close()
    except Exception as e:
        print('get_cookies出错了:{0}'.format(e))
    finally:
        brower.close()  # 浏览器关闭


def get_hot_html():
    try:
        cookie = cookiejar.MozillaCookieJar()
        cookie.load("zhihu_cookies.txt", ignore_discard=True, ignore_expires=True)
        cookie_handler = request.HTTPCookieProcessor(cookie)
        http_handler = request.HTTPHandler()
        https_handler = request.HTTPSHandler()
        opener = request.build_opener(http_handler, https_handler, cookie_handler)

        url = "https://www.zhihu.com/hot"  # 知乎热榜url
        rsp = opener.open(url)
        html = rsp.read().decode()
        with open("zhihu_hot.html", "w") as f:
            f.write(html)

    except Exception as e:
        print('get_hot_html出错了：{0}'.format(e))


if __name__ == '__main__':
    get_cookies()
    time.sleep(3)
    get_hot_html()

# 执行此程序会出现两个问题
# 一是出现验证码
# 二是出现报错，调用get_hot_html函数会说load那个zhihu_cookies.txt文件内容，编码不对。