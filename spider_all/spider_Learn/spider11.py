from bs4 import BeautifulSoup
from urllib import request


def qq():
    url = 'https://hr.tencent.com/position.php?&start=10#a'
    rsp = request.urlopen(url)
    html = rsp.read()
    soup = BeautifulSoup(html, 'lxml')
    tr1 = soup.select("tr[class='even']")
    tr2 = soup.select("tr[class='odd']")
    trs = tr1 + tr2
    for tr in trs:
        name = tr.select('td a')[0].get_text()
        print(name)
        href = tr.select('td a')[0].attrs['href']
        print(href)
        catalog = tr.select('td')[1].get_text()
        print(catalog)
        num = tr.select('td')[2].get_text()
        print(num)
        location = tr.select('td')[3].get_text()
        print(location)
        year = tr.select('td')[4].get_text()
        print(year)


if __name__ == '__main__':
    qq()
