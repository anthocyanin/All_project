from link_list import Lnode, LList, LinkedListUnderflow
# 循环单链表与普通单链表的差别在于，循环结束控制条件不同，所以这里也不继承单链表了


class LClist:  # 循环单链表, 要求只有尾结点引用，尾结点next为首结点
    def __init__(self):
        self._rear = None  # 只有尾结点引用

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 首端插入
        if self._rear is None:
            p = Lnode(elem, None)
            p.next = p
            self._rear = p
        else:
            p = Lnode(elem, self._rear.next)
            self._rear.next = p

    def prepop(self):  # 首端删除，我的写法，显然多次使用self._rear.next首结点
        if self._rear is None:
            raise LinkedListUnderflow('无结点了')
        if self._rear.next is self._rear:  # 如果是单元素链表
            e = self._rear.next.elem
            self._rear = None  # 单元素链表删除元素后，需要维护尾结点引用要为空，
            return e
        else:
            e = self._rear.next.elem
            self._rear.next = self._rear.next.next
            return e

    def append(self, elem):  # 尾端插入
        if self._rear is None:
            p = Lnode(elem, None)
            p.next = p
            self._rear = p
        else:
            p = Lnode(elem, self._rear.next)
            self._rear.next = p
            self._rear = p   # 这种写法问题是什么？没问题吧
            # self._rear = self._rear.next  # 这样写是正确的，因为它确认了前面一步的有效性

    def pop(self):  # 尾端删除
            pass

    def printall(self):
        if self._rear is None:
            return None
        p = self._rear.next
        # while p is not self._rear:  # 这种写法有点问题，就是只有一个结点时，打印不了
        #     print(p.elem, end=', ')
        #     p = p.next
        # print('')
        # 所以得换一下
        while True:
            print(p.elem, end=', ')
            if p is self._rear:
                break
            p = p.next
        print('')


if __name__ == '__main__':
    lc = LClist()
    for i in range(5):
        lc.prepend(i)

    for i in range(6, 11):
        lc.append(i)
    lc.printall()



