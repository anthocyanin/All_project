# 交换排序之冒泡排序
def sort_bubble(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]


lst = [1, 22, 2, 6, 8, 3, 10, 18, 4, 5]

sort_bubble(lst)
print(lst)


