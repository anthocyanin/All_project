# 定一个函数，打印一句话
import time


def fun(a):
    print(str(a))
    print('now is ',time.ctime())


if __name__ == '__main__':

    fun(22)
