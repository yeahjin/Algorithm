import sys

input = sys.stdin.readline

n, m = map(int,input().split())
l = list(map(int,input().split()))
v = [0] * n
s = [0] * m
def dfs(d):
    global n, m
    if d == m:
        for i in s:
            print(i, end = " ")
        print()
        return
    for i in range(n):
        if v[i] == 0:
            v[i] = 1
            s[d] = l[i]
            dfs(d+1)
            v[i] = 0

l = sorted(l)
dfs(0)