a = 'asd'
ll = list(a)
print(ll)
print(__name__)


class A:
    """
    zhu shi yi xia
    """
    pass


print(A.__bases__)
print(A.__name__)
print(A.__doc__)
print(A.__module__)
print(A.__dict__)


def fun():
    pass


print(fun.__module__)
print(fun.__doc__)
