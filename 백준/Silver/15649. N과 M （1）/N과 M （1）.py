import sys

input = sys.stdin.readline

def r(d):
    global n, m
    if d == m:
        for i in s:
            print(i, end = " ")
        print()
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            s[d] = i + 1
            r(d+1)
            v[i] = 0


n,m = map(int,input().split())
s = [0 for _ in range(m)]
v = [0 for _ in range(n)]
r(0)