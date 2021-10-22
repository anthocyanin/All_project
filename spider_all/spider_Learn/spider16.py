"""
拼多多web爬虫

1.专题 -> 全球海淘;品牌清仓;品质水果;99特卖;限时秒杀
2.活动 -> 服饰;女鞋;男装;家居;食品;电器;家纺;水果;母婴;海淘;美妆;运动

:copyright: (c) 2017 by Little Bean Dog.
"""

import time
import os
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from bs4 import BeautifulSoup


# Help functions
def now_ts():
    return int(time.time())


def get_ts_from_str(str_time, str_format="%Y-%m-%d %H:%M:%S"):
    array_time = time.strptime(str_time, str_format)
    ts = str(int(time.mktime(array_time)))
    return ts


# Special Urls
GET_SUPER = "https://www.pinduoduo.com/super.html"          # 品牌清仓
GET_YOU = "https://www.pinduoduo.com/you.html"              # 限时秒杀
GET_GLOBAL = "https://www.pinduoduo.com/global.html"        # 海淘专场
GET_IRY = "https://www.pinduoduo.com/itry.html"             # 品质水果
GET_SALE = "https://www.pinduoduo.com/sale.html"            # 99特卖
SPECIAL_URLS = {
    "品牌清仓": GET_SUPER, "限时秒杀": GET_YOU, "海淘专场": GET_GLOBAL, "品质水果": GET_IRY, "99特卖": GET_SALE
}

# Category Urls
GET_CLOTHES = "https://www.pinduoduo.com/category/clothes.html"     # 服饰
GET_SHOES = "https://www.pinduoduo.com/category/girlshoes.html"     # 女鞋
GET_SHIRT = "https://www.pinduoduo.com/category/boyshirt.html"      # 男装
GET_HOME = "https://www.pinduoduo.com/category/home.html"           # 家居
GET_FOOD = "https://www.pinduoduo.com/category/food.html"           # 食品
GET_3C = "https://www.pinduoduo.com/category/3c.html"               # 电器
GET_HOUSE = "https://www.pinduoduo.com/category/house.html"         # 家纺
GET_FRESH = "https://www.pinduoduo.com/category/fresh.html"         # 水果
GET_MB = "https://www.pinduoduo.com/category/motherbaby.html"       # 母婴
GET_HAITAO = "https://www.pinduoduo.com/haitao.html"                # 海淘
GET_BEAUTY = "https://www.pinduoduo.com/category/beauty.html"       # 美妆
GET_SPORTS = "https://www.pinduoduo.com/category/sports.html"       # 运动
CATEGORY_URLS = {
    "服饰": GET_CLOTHES, "女鞋": GET_SHOES, "男装": GET_SHIRT, "家居": GET_HOME, "食品": GET_FOOD, "电器": GET_3C, "家纺": GET_HOUSE, "水果": GET_FRESH, "母婴": GET_MB, "海淘": GET_HAITAO, "美妆": GET_BEAUTY, "运动": GET_SPORTS
}


# Time params
GMT_START_STR = time.strftime("%Y-%m-%d 00:00:00", time.localtime(time.time()))
GMT_END_STR = time.strftime("%Y-%m-%d 23:59:59", time.localtime(time.time()))
BIZ_START_STR = time.strftime("%Y-%m-%d 00:00:00", time.localtime(time.time() - 3600 * 24))
BIZ_END_STR = time.strftime("%Y-%m-%d 23:59:59", time.localtime(time.time() - 3600 * 24))
GMT_START_TS = get_ts_from_str(GMT_START_STR)
GMT_END_TS = get_ts_from_str(GMT_END_STR)
BIZ_START_TS = get_ts_from_str(BIZ_START_STR)
BIZ_END_TS = get_ts_from_str(BIZ_END_STR)
DATE_SIGN = time.strftime("%Y-%m-%d", time.localtime(time.time()))
LAST_DATE_SIGN = time.strftime("%Y-%m-%d", time.localtime(time.time() - 3600 * 24))

# Path params
CHROME_DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver.exe')


# Process functions
def get_special(url, source="unknown"):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('user-agent=shit')
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
        wait = ui.WebDriverWait(driver, 100)
        driver.get(url)
        # Wait for first page loading
        wait.until(lambda d: d.find_element_by_id("activity-content"))
        # Wait for content loading
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'xml')
        # Content list
        content = soup.html.body.section.select('#pdd-activity-glist')[0].div.ul
        content_list = content.find_all("div", {"class": "pa-glist-item-goods"})
        cnt = 0
        for one_item in content_list:
            cnt += 1
            img_url = one_item.find_all("img", {"class": "pa-goods-img"})[0].attrs['src']
            text_content = one_item.find_all("p", {"class": "act-goods-name"})[0].text
            cur_price = one_item.find_all("span", {"class": "act-goods-price"})[0].span.text
            ori_price = one_item.find_all("span", {"class": "act-goods-mprice"})[0].span.text
            sales_cnt = one_item.find_all("span", {"class": "act-goods-cnt"})[0].span.text
            print(
                ("========= {0}[{1}] ==========\n"
                 "title: {2}\n"
                 "price: {3} out of {4}\n"
                 "sales: {5}\n").format(source, cnt, text_content, cur_price, ori_price, sales_cnt)
            )
        driver.close()
    except Exception as e:
        print(str(e))
        raise Exception


def get_category(url, source="unknown"):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('user-agent=shit')
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
        wait = ui.WebDriverWait(driver, 100)
        driver.get(url)
        # Wait for first page loading

        wait.until(lambda d: d.find_element_by_id("pdd-list"))
        # Wait for content loading
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, 'xml')
        # Content list
        content = soup.html.body.section.select('#pdd-list')[0].div.ul
        content_list = content.find_all("div", {"class": "pa-glist-item-goods"})

        cnt = 0
        for one_item in content_list:
            cnt += 1
            img_url = one_item.find_all("img", {"class": "pa-goods-img"})[0].attrs['src']
            text_content = one_item.find_all("p", {"class": "act-goods-name"})[0].text
            cur_price = one_item.find_all("span", {"class": "act-goods-price"})[0].span.text
            ori_price = one_item.find_all("span", {"class": "act-goods-mprice"})[0].span.text
            sales_cnt = one_item.find_all("span", {"class": "act-goods-cnt"})[0].span.text
            print(
                ("========= {0}[{1}] ==========\n"
                 "title: {2}\n"
                 "price: {3} out of {4}\n"
                 "sales: {5}\n").format(source, cnt, text_content, cur_price, ori_price, sales_cnt)
            )
        driver.close()
    except Exception as e:
        print(str(e))
        raise Exception


if __name__ == '__main__':
    for tag in SPECIAL_URLS:
        get_special(SPECIAL_URLS[tag], tag)

    for tag in CATEGORY_URLS:
        get_category(CATEGORY_URLS[tag], tag)
