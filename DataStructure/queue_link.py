# 队列的顺序表(list, 要变成循环顺序表)实现
class QueueUnderflow(ValueError):
    pass


class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len           # 存储区长度or容量
        self._elems = [0] * init_len   # 元素存储
        self._head = 0                 # 表头元素下标
        self._num = 0                  # 元素个数

    def is_empty(self):
        return self._num is None

    def enqueue(self, e):
        if self._num == self._len:  # 队列满了的话，扩大存储区
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e  # 找到相应的插入位置，放入元素
        self._num += 1  # 维护元素的总数，其他不变。

    def __extend(self):  # 扩大存储区略复杂一点
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]  # 复制原来表中的元素
        self._elems, self._head = new_elems, 0

    def dequeue(self):
        if self._num is None:
            raise QueueUnderflow('无元素')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len  # 找到原来的老二的下标，作为self._head
        self._num -= 1
        return e

    def peek(self):
        if self._num is None:
            raise QueueUnderflow('无元素')
        return self._elems[self._head]
















