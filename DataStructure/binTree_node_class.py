#  二叉树的结点类
class BinTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


t = BinTNode(1, BinTNode(2), BinTNode(3))


def count_BinTNodes(t):  # 统计结点个数
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


def sum_BinTNdoes(t):  # 求和
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNdoes(t.left) + sum_BinTNdoes(t.right)


def preorder(t, proc):  # proc是具体的结点数据操作, 这是深度优先先根遍历
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)


from queue_link import SQueue


def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        t = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)








