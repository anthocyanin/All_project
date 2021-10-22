# 双链表
class DLnode:  # 双链表结点类
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class Dlist:  # 双链表 要求 维护一个self._head首结点指针。同时注意首结点的prev，尾结点的next都为None。
    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self, elem):  # 首端插入
        p = DLnode(elem, None, self._head)  # 构建新首结点
        if self._head is None:  # 空表,则p即是首结点，又是尾结点，所以p=self._head, 和self._rear
            self._head = p
            self._rear = p
        else:  # 不是空表
            self._head.prev = p  # 原首结点的prev要修改一下了，要变成p
            self._head = p  # 不是空表不要维护尾结点指针，因为他不受影响

    def prepop(self):  # 首端删除
        if self._head is None:  # 空表报错
            raise LinkedListUnderflow('无结点')
        if self._head.next is None:  # 单结点双链表, 显然我这个代码里多次使用self._head.next
            e = self._head.elem
            self._head = None
            self._rear = None
            return e
        else:
            e = self._head.elem
            self._head.next.prev = None  # 二结点做首结点之前，得把他的prev更新为None
            self._head = self._head.next  # 然后 二结点作为首结点
            return e

    def append(self, elem):  # 尾端插入
        p = DLnode(elem, self._rear, None)  # 构建新尾结点
        if self._head is None:  # 空表插入
            self._head = p
            self._rear = p
        else:  # 不是空表
            self._rear.next = p  # 原首结点的prev要修改一下了，要变成p
            self._rear = p  # 不是空表不要维护尾结点指针，因为他不受影响

    def pop(self):  # 尾端删除
        if self._rear is None:
            raise LinkedListUnderflow('无结点')
        if self._rear.prev is None:  # 单结点双链表, 显然我这个代码里多次使用self._rear.prev
            e = self._rear.elem
            self._rear = None
            self._head = None
            return e
        else:
            e = self._rear.elem
            self._rear.prev.next = None  # 倒二结点做尾结点之前，得把他的next更新为None
            self._rear = self._rear.prev
            return e


if __name__ == '__main__':
    dl = Dlist()
    for i in range(10):
        dl.prepend(i)

    for x in range(11, 20):
        dl.append(x)

    p = dl._head
    while p is not None:
        print(p.elem, end=', ')
        p = p.next
    print('')






































