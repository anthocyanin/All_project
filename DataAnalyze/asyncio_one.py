import asyncio


@asyncio.coroutine
def hello():
    print('hello world')
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(5)
    print('hello again!')


# 获取eventloop事件
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()


