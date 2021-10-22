def quick_sort(the_list, start, end):
    if start < end:
        m, n = start, end
        base = the_list[m]
        while m < n:  # 外层循环让m和n逐渐靠近，外层循环结束时m=n
            while (m < n) and (the_list[n] >= base):  # 内层循环，从n开始往左边走，找到一个小于基准值的把它放到左边去
                n = n - 1
            the_list[m] = the_list[n]
            while (m < n) and (the_list[m] <= base):  # 内层循环，从m开始往右边走，找到一个大于基准值的把它放到右边去
                m = m + 1
            the_list[n] = the_list[m]
        the_list[m] = base
        quick_sort(the_list, start, m-1)
        quick_sort(the_list, n + 1, end)
    return the_list


if __name__ == '__main__':
    the_list = [10, 1, 18, 30, 23, 12, 7, 65, 18, 17, 9, 33, 5, 3]
    start = 0
    end = len(the_list) - 1
    print(the_list)
    print(quick_sort(the_list, start, end))


