import asyncio

# 可以把一个generator标记为coroutine类型


async def wget(host):
    print('wget %s....' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# 这里tasks是一个列表，里面有三个相同函数wget，但是参数各不同。
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


