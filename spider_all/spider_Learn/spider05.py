from urllib import request
url = "https://maoyan.com/board"
rsp = request.urlopen(url)
html = rsp.read().decode()
# print(html)

import re

s = r'<dd>(.*?)</dd>'
pattern = re.compile(s, re.S)
films = pattern.findall(html)
print(len(films))

for film in films:
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(film)[0]
    print(title)
