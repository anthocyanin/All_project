from link_list import Lnode, LList, LinkedListUnderflow


class LList1(LList):  # 带尾结点引用的普通单链表，要求首结点，尾结点引用，尾结点的next为None

    name = "zhangsan"
    age = 12

    @staticmethod
    def sa():
        print('hello world')

    @classmethod
    def ss(cls):
        print(cls.name)

    def __init__(self):
        super(LList1, self).__init__()  # 既有首结点引用
        self._rear = None               # 又有尾结点引用

    def prepend(self, elem):  # 首端插入
        if self._head is None:  # 和父类一样 都是用slef._head判断空，若是空表需要维护 self._rear
            self._head = Lnode(elem, self._head)
            self._rear = self._head
        else:
            self._head = Lnode(elem, self._head)

    def prepop(self):  # 首端删除,这里不需要任何更改。因为他不需要维护尾结点引用语self._rear。
        if self._head is None:  # 删除元素要先判断是否为空
            raise LinkedListUnderflow('无结点了')
        e = self._head.elem  # 在更改首结点之前拿到首结点值
        self._head = self._head.next  # 把老二 当作老大
        return e

    def append(self, elem):  # 链表尾端删除
        if self._head is None:  # 空链表添加元素后需要维护self._head
            self._head = Lnode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = Lnode(elem)  # 新结点 当作之前尾结点的next，所以新结点成了尾结点
            self._rear = self._rear.next  # 通过调用self._rear.next能够找到尾结点，把尾结点赋给self._rear

    def pop(self):  # 链表尾端删除
        if self._head is None:
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
        self._rear = p  # 在这里维护self._rear
        return e


if __name__ == '__main__':
    mlist1 = LList1()
    for i in range(10):
        mlist1.prepend(i)
    for x in range(11, 20):
        mlist1.append(x)
    mlist1.printall()
    print(mlist1.__dict__)  # 只存实例属性
    print(mlist1.__dir__())  # 获取一个对象所有有效属性，应使用dir()。
    print(mlist1.__module__)  # 模块名称
    print(mlist1.__class__)  # 所属类型
    print(LList1.__dict__)  # 类的属性和方法
    # print(LList1.__dir__())








