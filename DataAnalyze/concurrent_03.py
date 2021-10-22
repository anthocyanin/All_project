from concurrent.futures import ThreadPoolExecutor as Pool
import urllib
from urllib import request
import time

URLS = ['http://www.baidu.com', 'http://qq.com', 'http://sina.com']


def task(url, timeout=20):
    return request.urlopen(url, timeout=timeout)


pool = Pool(max_workers=3)
results = pool.map(task, URLS)


time.sleep(20)
for result in results:
    print('%s, %s' % (result.url, len(result.read())))
