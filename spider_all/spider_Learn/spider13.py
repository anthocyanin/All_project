from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

url = "https://www.baidu.com"
driver = webdriver.Chrome()
driver.get(url)

js = " var q=document.getElementById(\'kw\'); q.style.border=\'3px solid red\';"
driver.execute_script(js)
time.sleep(4)
driver.save_screenshot('baidu2.png')

img = driver.find_element_by_xpath('//*[@id="lg"]/img')
driver.execute_script('$(arguments[0]).fadeOut()', img)


