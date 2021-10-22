def simple_coro(a):
    print('start----->')
    b = yield a
    print('received---->', a, b)
    c = yield a + b
    print('received---->', a, b, c)
    yield a + b + c


sc = simple_coro(5)
aa = next(sc)  # 此处应该打印出start----->
print(aa)  # 此处应该打印5

bb = sc.send(6)  # 此处应该打印received----> 5,6
print(bb)  # 此处应该打印11

cc = sc.send(7)  # 此处应该打印received----> 5,6,7
print(cc)  # 此处应该打印18

