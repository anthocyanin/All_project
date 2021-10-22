import urllib
from lxml import etree
import requests


def Schedule(blocknum, blocksize, totalsize):
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
        print('当前下载进度：%d' % per)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/', headers=headers)
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    real_url = 'http:'+ img_url
    urllib.request.urlretrieve(real_url, 'img' + str(i) + '.jpg', Schedule)
    i += 1
