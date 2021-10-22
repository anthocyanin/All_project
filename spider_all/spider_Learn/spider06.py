import requests
from lxml import etree
url = "https://www.qiushibaike.com/8hr/page/1/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}
rsp = requests.get(url, headers=headers)
html = rsp.text
html = etree.HTML(html)
rst = html.xpath('//div[contains(@id,"qiushi_tag")]')

for r in rst:
    # print(type(r))
    # print(r.tag)
    # print(r)
    item = {}
    content = r.xpath('//div[@class="recmd-right"]').text.strip()
    print(content)
