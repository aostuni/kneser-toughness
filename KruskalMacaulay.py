from math import comb


def binomial_decomposition(n, i):
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


def kruskal_macaulay(n, i, r):
    a = binomial_decomposition(n, i)
    s = 1
    for k in range(i, r, -1):
        s += comb(a[k], k - r)
    return s


if __name__ == "__main__":
    pass
