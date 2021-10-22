import time


def deco(func):
    def wrapper():
        start_time = time.time()
        time.sleep(2)
        func()
        end_time = time.time()
        mes = end_time-start_time
        print('程序运行时间%s' % mes)
    return wrapper


@deco
def func():
    print('hello')
    time.sleep(2)
    print('world')


if __name__ == '__main__':
    func()

