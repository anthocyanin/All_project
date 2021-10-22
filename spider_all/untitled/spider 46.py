import requests
from bs4 import BeautifulSoup
import os
import re

url ='http://www.shicimingju.com/chaxun/list/3710.html'
r = requests.get(url)
html = r.text.encode(r.encoding).decode()
soup = BeautifulSoup(html, 'lxml')
content = soup.find('div', id='shici-content').text
title = soup.find('div', id='shici-content').parent.h1.text
