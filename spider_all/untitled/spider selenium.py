from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com")
print("title:(0)", format(driver.title))
