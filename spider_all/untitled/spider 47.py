#-*- coding: utf-8 -*-
import os
import re
import json
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
                         + '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False,) + '\n')
        f.close()


def save_image_file(url, path):
    ir = requests.get(url)
    if ir.status_code == 200:
        with open(path, "wb") as f:
            f.write(ir.content)
            f.close()


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_page(url)
    if not os.path.exists("cover"):
        os.mkdir("cover")
    for item in parse_page(html):
        print(item)
        write_to_file(item)
        save_image_file(item['image'], 'cover/' + '%03d'%int(item['index']) + item['title'] + '.jpg')


if __name__ == "__main__":
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])





