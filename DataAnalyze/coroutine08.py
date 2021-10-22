def generator_01():
    total = 0
    while True:
        x = yield
        print('加', x)
        if not x:
            break
        total += x
    return total


def generator_02():  # 委派生成器
    while True:
        total = yield from generator_01()  # 子生成器
        print('加和总数是:', total)


def main():  # 调用方
    # g1 = generator_01()
    # g1.send(None)
    # g1.send(2)
    # g1.send(3)
    # g1.send(None)
    g2 = generator_02()
    g2.send(None)
    g2.send(2)  # 注意这里其实是传递给了generator_01了
    g2.send(3)
    g2.send(None)


main()

# 09 和 08 两个案例说明，yield的两个作用
# 简化yield的操作
# 封装了异常处理机制
