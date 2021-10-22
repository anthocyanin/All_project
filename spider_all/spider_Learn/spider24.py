from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("file:///Users/gonghuidepro/Desktop/login.html")

username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_xpath("//input[@name='password']")
login_button = driver.find_element_by_xpath("//input[@value='Login']")

username_input.send_keys("qiye")
password_input.send_keys("qiye_pass")
login_button.click()

username_input.clear()
password_input.clear()
