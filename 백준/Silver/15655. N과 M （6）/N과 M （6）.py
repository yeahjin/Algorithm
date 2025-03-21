import sys
input = sys.stdin.readline

def dfs(d,k):
    if d == m:
        for i in s:
            print(i, end = " ")
        print()
        return
    for i in range(k, n):
        s[d] = l[i]
        dfs(d+1, i + 1)



n, m = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l)
s = [0] * m
dfs(0,0)
