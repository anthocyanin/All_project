import threading
import time


count = 0


class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire()
        temp = count + 1
        time.sleep(0.0001)
        count = temp
        lock.release()


lock = threading.Lock()
thre = []

for _ in range(1009):
    th = Mythread()
    th.start()
    thre.append(th)

for t in thre:
    t.join()


print(count)


