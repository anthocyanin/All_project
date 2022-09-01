#  python 实现方法重载
from functools import singledispatch


@singledispatch
def fun(arg):
    print(arg)


@fun.register
def _(arg: int):
    print(f'arg is int: {arg}')


@fun.register
def _(arg: list):
    print(f'arg is list: {arg}')


@fun.register
def _(arg: str):
    print(f'arg is str: {arg}')


if __name__ == '__main__':
    fun([1, 2, 3])
    fun('abcd')
    fun(12)



