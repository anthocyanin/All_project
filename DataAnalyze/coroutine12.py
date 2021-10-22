from gevent import monkey
monkey.patch_all()
import gevent
import urllib.request


def run_task(url):
    print("Visiting %s " % url)
    try:
        response = urllib.request.urlopen(url)
        url_data = response.read()
        print("%d bytes received from %s " % (len(url_data), url))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    urls = ["https://stackoverflow.com/", "http://www.cnblogs.com/", "http://github.com/"]
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)


# 好像报错了。
