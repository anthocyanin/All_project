import time


def deco(func):
    def wrapper(a,b):
        start_time = time.time()
        func(a, b)
        end_time = time.time()
        mes = end_time-start_time
        print('程序运行时间%s' % mes)
    return wrapper

@deco
def func(a, b):
    print('argument %d' % a)
    time.sleep(4)
    print('argument %s' % b)


if __name__ == '__main__':
    func(3,5)

