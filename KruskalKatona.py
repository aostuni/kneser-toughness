import re

from math import comb


def cascade(n, i):
    a = []
    for k in range(i, 1, -1):
        m = 0
        while comb(m, k) < n:
            m += 1
        a.append(m - 1)
        n -= comb(m - 1, k)
    a.append(n)
    a.append(0)
    a.reverse()
    return a


def kruskal_katona(n, i, r):
    a = cascade(n, i)
    s = 1
    for k in range(i, r, -1):
        s += comb(a[k], k - r)
    return s


if __name__ == "__main__":
    # print(kruskal_katona(14, 5, 2))

    # print(kruskal_katona(84, 7, 3))

    print(kruskal_katona(123, 8, 4))

    # cnt = 0
    # f = open("C:\\Users\\Davin Park\\Documents\\partitions.txt")
    # for line in f:
    #     partition = [int(s) for s in re.findall(r'\d+', line)]
    #     S = 126 - sum(partition)
    #     c = len(partition)
    #     x = partition.count(1)
    #     y = partition.count(2)
    #     flag = True
    #     if kruskal_katona(x, 5, 1) > S:
    #         flag = False
    #     for i in range(y):
    #         if kruskal_katona(x + i, 5, 1) - i > S:
    #             flag = False
    #     if flag:
    #         print(partition)
    #         cnt += 1
    # print(cnt)