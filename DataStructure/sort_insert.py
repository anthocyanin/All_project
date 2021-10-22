# 插入排序
def sort_insert(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x


lst = [1, 22, 2, 6, 8, 3, 10, 18, 4, 5]
sort_insert(lst)
print(lst)

# 外层循环 总是n-1次
# 内层循环最少为 n-1次，最多为n*(n-1)/2次
# 如果加上内层循环的前面两步则是内层循环最少为 2*(n-1)次，最多为2*(n-1)+n*(n-1)/2次

