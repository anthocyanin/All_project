# 队列的链序表实现
class Lnode:  # 单链表结点类
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class QueueUnderflow(ValueError):
    pass


class LQueue:
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, e):
        if self._head is None:
            p = Lnode(e, None)
            self._head = p
            self._rear = p
        else:
            p = Lnode(e, None)
            self._rear.next = p
            self._rear = p

    def dequeue(self):
        if self._head is None:
            raise QueueUnderflow('无元素')
        e = self._head.elem
        self._head = self._head.next
        return e

    def peek(self):
        if self._head is None:
            raise QueueUnderflow('无元素')
        e = self._head.elem
        return e


