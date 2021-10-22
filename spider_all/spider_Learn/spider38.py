# phantomjs 设置代理
from selenium import webdriver

service_args = [
    '--proxy=101.248.64.68:8080',
    '--proxy-type=http'
]
# 加入也需要认证代理的话，service_args改写如下即可
# service_args = [
#     '--proxy=101.248.64.68:8080',
#     '--proxy-type=http',
#     'proxy--auth=username:password'
# ]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http:httpbin.org/get')
print(browser.page_source)