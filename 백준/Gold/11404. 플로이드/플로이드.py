import sys
INF = sys.maxsize

n = int(input())
m = int(input())
g = [[INF] * (n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    g[a][b] = min(g[a][b], c)

for t in range(1,n+1):
    for s in range(1,n+1):
        for d in range(1,n+1):
            if s == d:
                g[s][d] = 0
            else:
                g[s][d] = min(g[s][d], g[s][t] + g[t][d])

for i in range(1,n+1):
    for k in range(1,n+1):
        if g[i][k] == INF:
            print(0, end = " ")
        else:
            print(g[i][k], end = " ")
    print()