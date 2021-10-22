# 归并排序
def sort_merge(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    llist = sort_merge(left)
    rlist = sort_merge(right)
    return merge(llist, rlist)


def merge(left, right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


if __name__ == '__main__':
    lst = [88, 5, 4, 3, 2, 1, 9, 0, 18, 33, 7, 6]
    lst2 = sort_merge(lst)
    print(lst2)
