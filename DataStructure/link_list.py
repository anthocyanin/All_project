# 单链表结点类
class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList:  # 普通单链表，要求有一个首结点引用，尾结点的next为None。

    def __init__(self):
        self._head = None  # 只有首结点引用

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):  # 首端插入
        self._head = Lnode(elem, self._head)  # 这一步相当于 把原来的老大拿过来当我的老二，然后把自己当作老大。

    def prepop(self):  # 首端删除
        if self._head is None:  # 删除元素要先判断是否为空
            raise LinkedListUnderflow('无结点了')
        e = self._head.elem  # 在更改首结点之前拿到首结点值
        self._head = self._head.next  # 把老二 当作老大
        return e

    def append(self, elem):  # 尾端插入
        if self._head is None:  # 空链表添加元素后需要维护self._head
            self._head = Lnode(elem)

        p = self._head
        while p.next is not None:  # 这里一直让他循环着，知道找到最后一个结点。注意条件里是 p.next。不是p
            p = p.next
        p.next = Lnode(elem)

    def pop(self):  # 尾端删除
        if self._head is None:  # 若是空链表
            raise LinkedListUnderflow('无结点了')
        p = self._head
        if p.next is None:  # 若是单元素链表，单元素链表删除后，需要维护self._head
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:  # 找到倒数第二个结点
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):  # 链表按条件pred查找
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')  # 打印一个空白行

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc('<', p.elem, '>', end=',')
            p = p.next
        print(' ')

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def rev(self):  # 反转操作
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p


if __name__ == '__main__':

    mlist = LList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)

    mlist.printall()
    mlist.rev()
    mlist.printall()
    print('=='*30)
    mlist.for_each(print)

    for x in mlist.elements():
        print(x, end='。')































