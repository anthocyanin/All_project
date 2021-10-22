# 栈的顺序表实现
class StackUnderflow(ValueError):
    pass


class SStack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def push(self, e):
        self._elems.append(e)

    def pop(self):
        if self._elems is None:
            raise StackUnderflow('无元素')
        return self._elems.pop()

    def top(self):
        if self._elems is None:
            raise StackUnderflow('无元素')
        return self._elems[-1]


if __name__ == '__main__':
    st = SStack()
    st.push(1)
    st.push(2)
    while not st.is_empty():
        print(st.pop())





















