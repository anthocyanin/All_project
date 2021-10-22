import time
import codecs
import datetime
import selenium.webdriver.support.ui as ui

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class QunaSpider():
    def get_hotel(self, driver, tocity, fromdate, todate):
        ele_toCity = driver.find_element_by_name('toCity')
        ele_fromDate = driver.find_element_by_id('fromDate')
        ele_toDate = driver.find_element_by_id('toDate')
        ele_search = driver.find_element_by_class_name('search-btn')

        print(type(ele_search))
        ele_toCity.clear()
        ele_toCity.send_keys(tocity)
        ele_toCity.click()
        time.sleep(3)

        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        time.sleep(3)
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        time.sleep(3)
        ele_search.click()
        print('开始搜索')
        page_num = 0
        while page_num < 50:
            try:
                WebDriverWait(driver, 10).until(
                    EC.title_contains(tocity)
                )
            except Exception as e:
                print(e)
                time.sleep(2)
                print('出错了')
                break
            print('程序要休息15秒')
            time.sleep(15)

            js = "window.scrollTo(0, document.body.scrollHeight)"
            driver.execute_script(js)
            print('程序还要休息5秒')
            time.sleep(5)
            htm_const = driver.page_source
            print(type(htm_const))
            soup = BeautifulSoup(htm_const, "html.parser")
            infos = soup.find_all(class_='item_hotel_info')
            print(type(infos))
            print(len(infos))
            f = codecs.open(tocity + fromdate + '.html', 'a', 'utf-8')
            for info in infos:
                f.write(str(page_num) + '---'*50)
                content = info.get_text().replace(" ", "").replace("\t", "").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
            f.close()
            time.sleep(5)
            print('休息5秒在取下面15条数据')
            try:
                next_page = WebDriverWait(driver, 10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next"))
                )
                next_page.click()
                page_num += 1
                time.sleep(10)
            except Exception as e:
                print(e)
                break

    def crawl(self, root_url, tocity):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Chrome()
        driver.set_page_load_timeout(70)
        driver.get(root_url)
        driver.maximize_window()
        driver.implicitly_wait(10)  # 控制间隔时间，等待浏览器反映
        self.get_hotel(driver, tocity, today, tomorrow)


if __name__ == '__main__':
    spider = QunaSpider()
    spider.crawl('http://hotel.qunar.com/', u"上海")

# 这个代码有两个问题
# 一是我并没有找到 search-btn 这个元素，但是执行时却没报错
# 二是程序成功驱动浏览器查询起来了，但是一直差不出结果，就关了。不知道是不是去哪网反爬措施导致的
# 有可能是目的地，日期，点击过快导致的。







