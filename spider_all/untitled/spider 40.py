import requests
from lxml import etree
# 简书首页title爬去取


class LxmlSpider:
    def __init__(self):
        self.session = requests.Session()

    def jian_shu_spider(self, url, headers):
        response = requests.get(url, headers=headers).text
        result = etree.HTML(response)
        # title的xpath
        title_list = result.xpath("//div/a[@class='title']")
        for title in title_list:
            print("文章标题：%s" % title.text)


if __name__ == '__main__':
    lxml_soup = LxmlSpider()
    lxml_soup.jian_shu_spider(
        "http://www.jianshu.com",
        {
            "Referer": "https://www.jianshu.com/",
             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
    )
