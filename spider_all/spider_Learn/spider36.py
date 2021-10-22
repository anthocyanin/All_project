# selenium 设置代理
from selenium import webdriver
proxy = '125.40.109.154.31610'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http:httpbin.org/get')
