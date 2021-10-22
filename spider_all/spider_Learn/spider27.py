import requests
from lxml import etree


class Login():
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')
        return token

    def login(self, usname, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': usname,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        print(response.status_code)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            print('profiles is gonging to work')
            self.profiles(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class,"d-flex")]')
        print(type(dynamics))
        print(dynamics)
        # for item in dynamics:
        #     dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
        #     print(dynamic)

    def profiles(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')
        print(len(name))
        print('profiles 可以正常运行到这里')
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        print(name)
        print(email)


if __name__ == '__main__':
    mygithub = Login()
    try:
        mygithub.login('anthocyanin', 'gonghui21513049')
    except Exception as e:
        print('错误原因是：{0}'.format(e))



