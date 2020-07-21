from math import ceil, floor, comb

from KruskalKatona import kruskal_katona


def visit_partitions(n, m, f, minimum=1):
    """
    Algorithm H from Knuth. http://www.cs.utsa.edu/~wagner/knuth/fasc3b.pdf
    n >= m * minimum
    """
    if m == 1:
        f([n])
        return
    if m == 2:
        for i in range(minimum, floor(n / 2) + 1):
            f([n - i, i])
        return
    a = [n - (m - 1) * minimum]
    for i in range(m - 1):
        a.append(minimum)
    while True:
        f(a)
        while a[1] < a[0] - 1:
            a[0] = a[0] - 1
            a[1] = a[1] + 1
            f(a)
        j = 2
        s = a[0] + a[1] - 1
        while j < m and a[j] >= a[0] - 1:
            s += a[j]
            j += 1
        if j == m:
            return
        x = a[j] + 1
        a[j] = x
        j -= 1
        for i in range(j, 0, -1):
            a[i] = x
            s -= x
        a[0] = s


def u(n, r, S):
    d = comb(n - r, r)
    return min(d * S, floor((d + comb(n - r - 1, r - 1)) * S * (comb(n, r) - S) / comb(n, r)))


def partitions_7_3():
    f = [-1, 4, 6, -1, -1, -1, 12, 14]
    for i in range(8, 26):
        f.append(ceil(2 * i * (35 - i) / 35))
    d = 4
    for c in range(5, 14):
        for S in range(c + 1, floor(4 * c / 3)):
            a_low = ceil((2 * c * (d - 1) - u(7, 3, S)) / (d - 2))
            a_high = 1
            while a_high <= c and kruskal_katona(a_high, 4, 1) <= S:
                a_high += 1
            for a in range(a_low, a_high + 1):
                b_low = ceil((6 * c - 35 + S - 5 * a) / 4)
                b_high = min(c - a, floor((35 - S - a) / 2))
                for b in range(b_low, b_high + 1):
                    if a + b < c:
                        visit_partitions(35 - S - a - 2 * b, c - a - b, print, 6)


def partitions_9_4():
    f = [-1, 5, 8, -1, -1, -1, 18, 24, 27, 28, 33, 32, 35, 36, 35]
    for i in range(16, 116):
        f.append(ceil(2 * i * (126 - i) / 126))
    d = 5
    for c in range(5, 53):
        for S in range(c + 1, floor(5 * c / 4)):
            a_low = ceil((2 * c * (d - 1) - u(9, 4, S)) / (d - 2))
            a_high = 1
            while a_high <= c and kruskal_katona(a_high, 5, 1) <= S:
                a_high += 1
            for a in range(a_low, a_high + 1):
                b_low = ceil((6 * c - 126 + S - 5 * a) / 4)
                b_high = min(c - a, floor((126 - S - a) / 2))
                for b in range(b_low, b_high + 1):
                    if a + b < c:
                        visit_partitions(126 - S - a - 2 * b, c - a - b, print, 6)


if __name__ == "__main__":
    partitions_9_4()
