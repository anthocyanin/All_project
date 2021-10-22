import requests
from lxml import html
url = 'https://music.douban.com/'  # 需要爬的网址
page = requests.Session().get(url)
tree = html.fromstring(page.text)
result1 = tree.xpath('//tr//a/text()')
result2 = tree.xpath('//tr//a/@href')
result3 = tree.xpath('//tr[last()]//a/@href')
print(result1)
print(result2)
print(result3)
