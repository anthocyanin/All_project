class DemoException(Exception):
    pass


def handle_exception():
    print('start------->')
    while True:
        try:
            x = yield
        except DemoException:
            print('occure demoexception error')
        else:
            print('received------>', x)

    raise RuntimeError('this line should never run')


he = handle_exception()
next(he)

he.send(10)
he.send(20)

he.throw(DemoException)
he.send(40)
he.close()


