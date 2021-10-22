# 选择排序
def sort_choice(lst):
    for i in range(len(lst)):
        k = i
        for j in range(i, len(lst)):
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]


lst = [1, 22, 2, 6, 8, 3, 10, 18, 4, 5]
sort_choice(lst)
print(lst)





