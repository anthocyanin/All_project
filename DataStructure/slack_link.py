# 栈的链序表实现
class StackUnderflow(ValueError):
    pass


class Lnode:  # 单链表结点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def push(self, e):
        p = Lnode(e, self._head)
        self._head = p

    def pop(self):
        if self._head is None:
            raise StackUnderflow('无元素')
        e = self._head.elem
        self._head = self._head.next
        return e

    def top(self):
        if self._head is None:
            raise StackUnderflow('无元素')
        e = self._head.elem
        return e


if __name__ == '__main__':
    st = LStack()
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        st.push(x)
    list2 = []
    while not st.is_empty():
        list2.append(st.pop())

    for x in list2:
        print(x, end=', ')
























