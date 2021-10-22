def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consuming %s.....' % n)
        r = '200 ok'


def produce(c):  # produce函数需要一个协程作为参数。
    c.send(None)  # 首先要预激协程，c.send(None) 和 next(c) 效果一样
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] producing %s......' % n)
        r = c.send(n)  # 通过c.send(n)切换到consumer执行。直到下一个yield位置处停止，并把yield右边表达式的值返回出去，赋值给r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
