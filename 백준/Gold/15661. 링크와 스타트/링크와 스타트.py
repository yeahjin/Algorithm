import sys

input = sys.stdin.readline


def dfs(d):
    global min_num, n
    if d == n:
        if [0] * n == v or [1] * n == v:
            return
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if v[i] == 1 and v[j] == 1:
                    start += g[i][j]
                if v[i] == 0 and v[j] == 0:
                    link += g[i][j]
        min_num = min(abs(start - link), min_num)
        return
    v[d] = 1
    dfs(d + 1)
    v[d] = 0
    dfs(d + 1)


n = int(input())
g = []
v = [0] * n
for i in range(n):
    t = list(map(int, input().split()))
    g.append(t)
min_num = int(1e9)
dfs(0)
print(min_num)
