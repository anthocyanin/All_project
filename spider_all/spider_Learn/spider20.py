from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "https://www.baidu.com"
driver = webdriver.Chrome()
driver.get(url)
assert u"百度" in driver.title
elem = driver.find_element_by_name('wd')
elem.clear()
elem.send_keys(u"网络爬虫")
elem.send_keys(Keys.RETURN)
time.sleep(4)
assert u"网络爬虫." not in driver.page_source
time.sleep(4)
driver.close()
