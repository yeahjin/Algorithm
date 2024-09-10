import sys

input = sys.stdin.readline


def r(idx, k):
    global n, m
    if k == m:
        for i in s:
            print(i, end=" ")
        print()
        return
    for i in range(idx, n):
        s[k] = i + 1
        r(i, k + 1)


n, m = map(int, input().split())
s = [0 for _ in range(m)]
r(0, 0)
