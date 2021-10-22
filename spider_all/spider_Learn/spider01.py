# 爬取百度贴吧
from urllib import parse, request

if __name__ == '__main__':
    qs = {
        'kw': '张继科',
        'ie': 'utf-8',
        'pn': 0
    }

    urls = []
    baseurl = 'https://tieba.baidu.com/f?'
    for i in range(10):
        pn = i*50
        qs['pn'] = str(pn)
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)

    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode('utf-8')
        print(url)
        print(html)





