import re

from math import comb, ceil, floor


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
    # for c in range(5, 13):
    #     lo = c + 1
    #     hi = ceil(4 * c / 3) - 1
    #     for S in range(lo, hi + 1):
    #         print(kruskal_katona(3 * c - 2 * S, 4, 1) <= S)

    # print(kruskal_katona(10, 4, 1))

    cnt = 0
    f = open("C:\\Users\\Davin Park\\Documents\\partitions.txt")
    for line in f:
        partition = [int(s) for s in re.findall(r'\d+', line)]
        S = 126 - sum(partition)
        c = len(partition)
        if kruskal_katona(partition.count(1), 5, 1) <= S and kruskal_katona(partition.count(1) + partition.count(2), 5, 1) - partition.count(2) <= S:
            print(partition)
            cnt += 1
    print(cnt)