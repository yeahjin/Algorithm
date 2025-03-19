import sys
input = sys.stdin.readline

def dfs(d, idx):
    global min_num
    if d == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if v[i] == 0 and v[j] == 0:
                    start += g[i][j]
                if v[i] == 1 and v[j] == 1:
                    link += g[i][j]
        min_num = min(abs(start - link), min_num)
        return
    for i in range(idx,n):
        if v[i] == 0:
            v[i] = 1
            dfs(d+1,i+1)
            v[i] = 0



n = int(input())
g = []

for i in range(n):
    t = list(map(int,input().split()))
    g.append(t)
v = [0] * n
min_num = int(1e9)
dfs(0,0)
print(min_num)