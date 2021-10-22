# 异步代码实现多个IO任务
# @asyncio.coroutine 和 yield from
import asyncio
import time


@asyncio.coroutine
def taskIO_01():
    print('开始运行IO任务1...')
    yield from asyncio.sleep(2)
    print('IO任务1已完成，耗时2s')
    return taskIO_01.__name__


@asyncio.coroutine
def taskIO_02():
    print('开始运行IO任务2...')
    yield from asyncio.sleep(3)
    print('IO任务2已完成，耗时3s')
    return taskIO_02.__name__


@asyncio.coroutine
def main():
    tasks = [taskIO_01(), taskIO_02()]
    done, pending = yield from asyncio.wait(tasks)  # 子生成器。在协程中yield from后面必须是子生成器函数
    for r in done:  # done和pending都是一个任务，所以返回结果需要逐个调用result()
        print('协程无序返回值：'+r.result())


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
    try:
        loop.run_until_complete(main())  # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close()
    end = time.time()
    print('所有IO任务总耗时%.5f秒' % float(end-start))
