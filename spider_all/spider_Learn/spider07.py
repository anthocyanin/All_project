from urllib import request
from lxml import etree


def shanbei(page):
    url = "https://www.shanbay.com/wordlist/104899/202159/?page=%s" % page
    rsp = request.urlopen(url)
    html = rsp.read()
    html = etree.HTML(html)
    tr_list = html.xpath("//tr")
    word = {}

    for tr in tr_list:
        strong = tr.xpath(".//strong")
        if len(strong):
            name = strong[0].text.strip()
            word['name'] = name

        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word['content'] = content

        print(word)
        # if word != {}:
        #     words.append(word)


if __name__ == '__main__':
    shanbei(2)
